"""Shared orchestration body for the policy lane's start flow.

The generic RawFish route delegates here for policy-lane lifecycle behaviour:
scale-guard re-check, persona-scale resolution, ``starting`` state flip,
runner-factory invocation, ``RunMetadata`` build + atomic write, and
``running`` / terminal state flip.

The service is intentionally narrow:

* It receives an already-validated :class:`Scenario`, an
  already-loaded ``state`` dict, the resolved ``run_dir``, the
  ``zep_mode`` string, and the runner factory the caller wants to
  drive. The HTTP-layer concerns (body parsing, idempotency, auth,
  exception-to-envelope mapping) stay in the calling route.
* It owns ONLY the ``state.json`` writes the policy lane needs
  (``starting`` -> terminal) plus the ``run_metadata.json`` write on
  success and the failure-context ``run_metadata.json`` write on the
  factory-raised path. The generic dispatch route owns its own
  namespaced ``state.json`` transitions; calling the service from the
  adapter therefore writes a flat-path ``state.json`` as well, which
  is harmless: the generic ``/status`` endpoint reads only the
  namespaced state.
* On a factory exception the service raises
  :class:`PolicyRunnerStartFailed` after writing the failure-context
  metadata + transitioning to ``failed``. The caller maps the
  exception to its own HTTP envelope; the generic dispatch wrapper surfaces
  ``502 RUNNER_START_FAILED``.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass
from datetime import datetime
from typing import Any, Dict, Optional

from app.policy.persona_defaults import scale_defaults_for
from app.policy.run_metadata import RunMetadata, ScaleCaps
from app.policy.run_resolution import resolve_rounds
from app.policy.schema import SCALE_CAP_LARGE, SCALE_CAP_POC, Scenario
from app.seam.zep_mock import resolve_master_seed
from app.simulation_platform.artifact_manifest import (
    artifact_hashes_from_manifest,
    artifact_paths_from_manifest,
    read_manifest,
)
from app.api.error_codes import ErrorCode
from app.simulation_platform.error_envelope import safe_error
from app.simulation_platform.runner_adapter import RunnerAdapter
from app.simulation_platform.runner_types import SimulationRunnerFactory
from app.simulation_platform.scale_guard import (
    ScaleGuardExceeded,
    evaluate_scale_guard,
)
from app.simulation_platform.state_machine import STATE_MACHINE
from app.utils.atomic_io import atomic_write_json, atomic_write_text
from app.utils.logger import get_logger
from app.utils.runtime_env import get_allow_expensive

logger = get_logger("rawfish.services.policy.policy_runner_service")


@dataclass(frozen=True)
class StartResult:
    """Successful start orchestration output.

    Carries the start response's ``data`` section fields
    (``task_id``, ``status``, ``token_usage_estimate``) plus
    ``persisted_status`` -- the literal status the service just wrote
    to ``state.json`` (one of ``running`` / ``completed`` / ``failed``).
    The API response reads ``status`` (the ack-shape that says
    ``"starting"`` while the subprocess is in flight); the generic
    dispatch route reads ``persisted_status`` so it can mirror the
    on-disk truth into the dispatch ``phase`` field without lying.
    """

    task_id: str
    status: str
    token_usage_estimate: Dict[str, Any]
    persisted_status: str


class PolicyRunnerStartFailed(RuntimeError):
    """Raised when the runner factory's ``start`` call raises.

    Carries the stable ``error_code`` (always
    :data:`ErrorCode.RUNNER_START_FAILED`) plus a sanitized
    ``message`` so the calling route can populate the HTTP envelope
    without re-deriving the values. The service has already
    transitioned ``state.json`` to ``failed`` and written the
    failure-context ``run_metadata.json`` before the raise lands.
    """

    def __init__(self, *, error_code: ErrorCode, message: str) -> None:
        super().__init__(message)
        self.error_code = error_code
        self.message = message


class PolicyScaleGuardExceeded(RuntimeError):
    """Raised when the runtime scale guard refuses the resolved product.

    A scenario admitted at create-time may still fail the runtime
    guard if ``ZEP_MODE`` flipped between create and start (the
    per-persona scale defaults change with the mode). The service
    raises with the structured ``details`` payload the calling route
    feeds into its ``400 SCALE_GUARD_EXCEEDED`` envelope verbatim.
    """

    def __init__(
        self,
        *,
        message: str,
        details: Dict[str, Any],
    ) -> None:
        super().__init__(message)
        self.message = message
        self.details = details


def _utcnow() -> str:
    """Return current wall-clock UTC time as an ISO 8601 string."""
    from datetime import timezone

    return datetime.now(timezone.utc).isoformat()


def _rough_cost_estimate(
    *,
    seed_text: str,
    stress_question: str,
    agents: int,
    rounds: int,
    ensemble_n: int,
) -> Dict[str, Any]:
    """Pre-flight token estimate (``method='phase4_v2'``).

    Keeps the response envelope's ``token_usage_estimate`` payload
    stable for callers.
    """
    base_tokens_per_call = (len(seed_text) + len(stress_question)) // 4
    total_llm_calls = max(1, agents) * max(1, rounds) * max(1, ensemble_n) * 2
    est_total_tokens = base_tokens_per_call * total_llm_calls
    return {
        "base_tokens_per_call": base_tokens_per_call,
        "total_llm_calls": total_llm_calls,
        "est_total_tokens": est_total_tokens,
        "method": "phase4_v2",
    }


class PolicyRunnerService:
    """Encapsulates the lock-protected orchestration body of start.

    The single :meth:`start` classmethod is the only public entry
    point. The class itself is stateless -- consumers do not need to
    instantiate it.
    """

    @classmethod
    def start(
        cls,
        *,
        simulation_id: str,
        scenario: Scenario,
        run_dir: str,
        state: Dict[str, Any],
        zep_mode: str,
        rounds_override: Optional[int],
        ensemble_n_override: Optional[int],
        runner_factory: SimulationRunnerFactory,
        seed_override: Optional[int] = None,
    ) -> StartResult:
        """Drive the prepared -> starting -> running lifecycle.

        Sequence:

        1. Persona-scale resolution + scale-guard re-check (raises
           :class:`PolicyScaleGuardExceeded` on refusal).
        2. State flip to ``starting`` with ``started_at`` stamp.
        3. Runner factory ``start`` invocation. On exception, flip
           ``state.json`` to ``failed`` + write failure-context
           ``run_metadata.json`` + raise
           :class:`PolicyRunnerStartFailed`.
        4. On success: build typed :class:`RunMetadata` from the
           prepare manifest provenance, write ``run_metadata.json``,
           flip ``state.json`` to ``running`` (or to the synchronous
           terminal status the factory hinted at).
        5. Return a :class:`StartResult` carrying the response data
           fields the legacy envelope needs.

        Caller responsibilities (NOT done here):

        * Acquire the per-simulation start lock around this call.
        * Honour idempotency replay before this call.
        * Map raised exceptions to the wire-side HTTP envelope.
        """
        # Two distinct multipliers live here -- do not conflate them:
        #   * ``stakeholder_count`` feeds the ADMISSION guard. Mirrors
        #     the schema's create-time formula
        #     (ensemble_n * len(stakeholders) * rounds) so a scenario
        #     admitted by ``Scenario._enforce_scale_cap`` cannot be
        #     rejected here for a different reason -- and vice versa.
        #   * ``agents`` (persona-scale OASIS agent count) feeds only
        #     the pre-flight COST ESTIMATE. The cost math uses the
        #     larger value so token projections do not undercount the
        #     runtime spend; the admission decision stays canonical.
        persona_scale = scale_defaults_for(
            scenario.persona, scenario.scope, zep_mode,
        )
        agents = int(persona_scale["agents"])
        stakeholder_count = len(scenario.stakeholders)

        # Rounds resolution lives in
        # ``app.policy.run_resolution.resolve_rounds`` (single SSoT for
        # the dual-place chain). Chain (first non-None wins):
        #   override -> scenario.drift_horizon_rounds (root canonical)
        #     -> scenario.run.drift_horizon_rounds (legacy; warns)
        #     -> scale_defaults_for(persona, scope, zep_mode)['rounds']
        rounds = resolve_rounds(rounds_override, scenario, zep_mode)

        ensemble_n = (
            ensemble_n_override
            if ensemble_n_override is not None
            else int(scenario.run.ensemble_n)
        )

        expensive = get_allow_expensive()
        ok, cap, payload = evaluate_scale_guard(
            ensemble_n=ensemble_n,
            stakeholders=stakeholder_count,
            rounds=rounds,
            allow_expensive_env=expensive,
        )
        if expensive:
            product = (
                max(1, stakeholder_count)
                * max(1, rounds)
                * max(1, ensemble_n)
            )
            logger.warning(
                "POLICY_ALLOW_EXPENSIVE=true -- scale guard cap relaxed "
                "to SCALE_CAP_LARGE=%d (stakeholders=%d rounds=%d "
                "ensemble_n=%d product=%d)",
                cap, stakeholder_count, rounds, ensemble_n, product,
            )
        if not ok:
            assert payload is not None  # invariant
            guard_exc = ScaleGuardExceeded(
                stakeholders=payload["stakeholders"],
                rounds=payload["rounds"],
                ensemble_n=payload["ensemble_n"],
                product=payload["product"],
                cap=payload["cap"],
            )
            raise PolicyScaleGuardExceeded(
                message=str(guard_exc),
                details=guard_exc.to_details(),
            )

        cost = _rough_cost_estimate(
            seed_text=scenario.seed_text,
            stress_question=scenario.stress_question,
            agents=agents,
            rounds=rounds,
            ensemble_n=ensemble_n,
        )

        # Lifecycle step 1: flip state.json to 'starting' BEFORE the
        # factory call. This ordering is load-bearing -- a crash inside
        # the factory leaves the on-disk state truthful (the run is
        # mid-launch) rather than stuck at ``prepared``.
        # ``from_phase=None`` matches the legacy unconditional write:
        # the SIM_NOT_PREPARED + manifest gates above are the
        # start-side admission controls; we deliberately do not also
        # assert ``state.status == 'prepared'`` here so a re-issued
        # /start against a run already mid-flight does not regress on
        # a benign status drift.
        STATE_MACHINE.transition(
            simulation_id,
            None,
            "starting",
            state=state,
            extra_fields={"started_at": _utcnow()},
            run_dir=run_dir,
        )

        sim_config_path = os.path.join(run_dir, "simulation_config.json")
        with open(sim_config_path, "r", encoding="utf-8") as fh:
            sim_config = json.load(fh)

        try:
            handle = RunnerAdapter.start(
                factory=runner_factory,
                simulation_id=simulation_id,
                run_dir=run_dir,
                config=sim_config,
            )
        except Exception as start_exc:
            logger.exception("simulation/start: runner factory raised")
            failed_at = _utcnow()
            err_msg = safe_error(start_exc)
            # ``from_phase=None`` so the failure path can record
            # ``failed`` from any prior status (we just wrote
            # ``starting`` a few lines above, but the on-disk value may
            # have been mutated by an unrelated tool between the write
            # and the runner crash).
            STATE_MACHINE.transition(
                simulation_id,
                None,
                "failed",
                state=state,
                extra_fields={
                    "completed_at": failed_at,
                    "error_code": ErrorCode.RUNNER_START_FAILED.value,
                    "error_message": err_msg,
                },
                run_dir=run_dir,
            )
            # Failure-context metadata: distinct shape from the typed
            # ``RunMetadata`` written on success (which requires
            # ``runner_task_id``). ``status='failed'`` is the
            # discriminator any consumer should branch on before
            # reading ``runner_task_id`` / ``scale_caps`` / etc.
            failure_metadata = {
                "simulation_id": simulation_id,
                "status": "failed",
                "failed_at": failed_at,
                "error_code": ErrorCode.RUNNER_START_FAILED.value,
                "error_message": err_msg,
                "zep_mode": zep_mode,
            }
            atomic_write_json(
                os.path.join(run_dir, "run_metadata.json"),
                failure_metadata,
            )
            raise PolicyRunnerStartFailed(
                error_code=ErrorCode.RUNNER_START_FAILED,
                message=err_msg,
            ) from start_exc

        # Build the typed :class:`RunMetadata`. The cost-estimate dict
        # + ``expensive_override`` flag stay on the response envelope
        # (returned to the client) rather than the persisted metadata;
        # the on-disk shape is the strict ``extra='forbid'`` model.
        # ``cap_value`` reflects which ceiling was effectively in play
        # (``SCALE_CAP_LARGE`` under POLICY_ALLOW_EXPENSIVE, otherwise
        # ``SCALE_CAP_POC``) so post-hoc analysis can reconstruct
        # admission. ``runner_task_id`` comes from the factory handle
        # so ``/status`` can correlate the run with the runner-side
        # bookkeeping.
        manifest = read_manifest(run_dir)
        scen_hash = manifest["scenario_hash"]
        # ``prepared_at`` is the wall-clock time prepare
        # was called, captured into state.json at that point. The
        # manifest's ``created_at_iso`` is deterministic (derived from
        # scenario_hash to keep manifest bytes idempotent across
        # re-runs) and would lie about WHEN prepare actually ran.
        # ``RunMetadata`` wants the truthful wall-clock; the persisted
        # ``state["prepared_at"]`` is the source.
        prepared_at_dt = datetime.fromisoformat(state["prepared_at"])
        artifact_paths: Dict[str, str] = artifact_paths_from_manifest(manifest)
        artifact_hashes: Dict[str, str] = artifact_hashes_from_manifest(manifest)
        # ``seed_hash``: hex sha256 of the master-seed integer (resolved
        # via the same precedence the seam uses -- explicit >
        # RAWFISH_RUN_SEED > POLICY_RANDOM_SEED > scenario_hash
        # prefix). Hashing the int gives a stable fixed-length hex
        # string consistent with scenario_hash's shape and avoids
        # leaking the raw seed value to consumers that only need a
        # fingerprint.
        master_seed = resolve_master_seed(scen_hash, seed_override)
        seed_hash = hashlib.sha256(
            str(master_seed).encode("utf-8"),
        ).hexdigest()

        cap_value = SCALE_CAP_LARGE if expensive else SCALE_CAP_POC
        run_metadata = RunMetadata.from_policy_dict(
            {
                "simulation_id": simulation_id,
                "created_at": _utcnow(),
                "zep_mode": zep_mode,
            },
            persona=scenario.persona,
            scenario_preset_id=scenario.preset_id,
            scenario_hash=scen_hash,
            seed_hash=seed_hash,
            prepared_at=prepared_at_dt,
            artifact_paths=artifact_paths,
            artifact_hashes=artifact_hashes,
            scale_caps=ScaleCaps(
                ensemble_n=ensemble_n,
                stakeholders=stakeholder_count,
                rounds=rounds,
                cap_value=cap_value,
            ),
            statistical_settings_hash=state.get("statistical_settings_hash"),
            statistical_settings_version=state.get("statistical_settings_version"),
            statistical_settings=(
                state.get("statistical_settings")
                if isinstance(state.get("statistical_settings"), dict)
                else {}
            ),
            resolved_statistical_config=(
                state.get("statistical_settings")
                if isinstance(state.get("statistical_settings"), dict)
                else {}
            ),
            statistical_runtime_overrides=(
                state.get("statistical_runtime_overrides")
                if isinstance(state.get("statistical_runtime_overrides"), dict)
                else {}
            ),
            statistical_variant_lineage=(
                state.get("statistical_variant_lineage")
                if isinstance(state.get("statistical_variant_lineage"), list)
                else []
            ),
            variant_lineage=(
                state.get("statistical_variant_lineage")
                if isinstance(state.get("statistical_variant_lineage"), list)
                else []
            ),
            persona_salts_resolved=(
                state.get("persona_salts_resolved")
                if isinstance(state.get("persona_salts_resolved"), dict)
                else {}
            ),
            prior_attachments=(
                state.get("prior_attachments")
                if isinstance(state.get("prior_attachments"), dict)
                else {}
            ),
            provenance_per_field=(
                state.get("provenance_per_field")
                if isinstance(state.get("provenance_per_field"), dict)
                else {}
            ),
            lock_state_per_field=(
                state.get("lock_state_per_field")
                if isinstance(state.get("lock_state_per_field"), dict)
                else {}
            ),
            runner_task_id=handle.task_id,
        )
        atomic_write_text(
            os.path.join(run_dir, "run_metadata.json"),
            run_metadata.model_dump_json(indent=2),
        )

        # Lifecycle step 2: flip state.json to the post-handoff
        # terminal value. The default is ``running`` (subprocess kicked
        # off, run is in-flight); a non-None ``terminal_status`` on the
        # handle means the factory completed synchronously (test stubs
        # use this) and we jump straight to ``completed`` / ``failed``.
        # ``from_phase=None`` because the writer just flipped state to
        # ``starting`` above; asserting it here would only catch a
        # concurrent mutation race that does not affect correctness.
        terminal_status = handle.terminal_status or "running"
        terminal_extras: Dict[str, Any] = {}
        if terminal_status in ("completed", "failed"):
            terminal_extras["completed_at"] = _utcnow()
            if terminal_status == "failed" and handle.error:
                terminal_extras["error"] = handle.error
        STATE_MACHINE.transition(
            simulation_id,
            None,
            terminal_status,
            state=state,
            extra_fields=terminal_extras,
            run_dir=run_dir,
        )

        # The response ``status`` is an ack-shape distinct from the
        # persisted lifecycle status in state.json. We just flipped
        # state.json to ``running`` (subprocess is in-flight); the
        # response says ``starting`` to match the originally-shipped
        # client contract where /start acks the launch attempt and the
        # caller polls /status for the lifecycle transition.
        # ``completed`` / ``failed`` pass through unchanged because
        # those are terminal and there is no further state to poll for.
        response_status = (
            terminal_status if terminal_status != "running" else "starting"
        )
        return StartResult(
            task_id=handle.task_id,
            status=response_status,
            token_usage_estimate=cost,
            persisted_status=terminal_status,
        )


__all__ = [
    "PolicyRunnerService",
    "PolicyRunnerStartFailed",
    "PolicyScaleGuardExceeded",
    "StartResult",
]
