"""Generic use-case lifecycle dispatch.

Single Flask blueprint that serves the lane-agnostic lifecycle
routes under ``/api/sim/use-cases/<use_case_id>/...`` and delegates
every operation through the platform registry to the registered
:class:`app.simulation_platform.use_case.SimulationUseCase` adapter.
RawFish lanes drive create / prepare / start / status / report /
sensitivity through these endpoints without the policy blueprint owning
any of the dispatch.

Surface (per registered use case):

  * ``GET /api/sim/use-cases/<use_case_id>/personas``
    Registry-aggregated catalog filtered to ``use_case_id``.
  * ``POST /api/sim/use-cases/<use_case_id>/simulation/create``
    Create a fresh simulation row under the platform's state-
    machine layer. Body: ``{ scenario: {...} }``.
  * ``POST /api/sim/use-cases/<use_case_id>/simulation/<sim_id>/prepare``
    Adapter ``build_ontology`` + ``write_prepare_artifacts``. Lanes that
    need an audience-store side effect publish it inside
    ``build_ontology``; lanes without that requirement keep the method
    pure.
  * ``POST /api/sim/use-cases/<use_case_id>/simulation/<sim_id>/start``
    Deterministic-mock runner: transitions state.json to
    ``completed`` immediately; production runners are wired per-
    lane via the same Protocol the policy lane uses.
  * ``GET /api/sim/use-cases/<use_case_id>/simulation/<sim_id>/status``
    Returns the state-machine view (phase, warnings, errors).
  * ``POST /api/sim/use-cases/<use_case_id>/simulation/<sim_id>/report/generate``
    Adapter ``generate_report``; the result is persisted via the
    adapter's ``artifact_names`` mapping. ``report_json`` is
    written verbatim; if the returned object has
    ``.model_dump_json``, that is used. The wire response includes
    the persisted filenames + sha256 digests, mirroring the policy
    contract.
  * ``GET /api/sim/use-cases/<use_case_id>/simulation/<sim_id>/report``
    Returns the persisted report JSON (lane-defined shape).
  * ``POST /api/sim/use-cases/<use_case_id>/simulation/<sim_id>/sensitivity``
    Delegates to adapter ``run_sensitivity``. When the adapter
    raises :class:`NotImplementedError`, surfaces a structured
    501 with ``details.reason = "capability_unsupported"`` so
    clients can tell "lane doesn't support it" from "transient
    failure" without parsing message text.

Error envelope: every error response uses the shared
:func:`app.simulation_platform.error_envelope.make_err` shape, so
frontend and smoke clients can branch on stable ``error.code`` values
instead of parsing message text.

The blueprint never imports ``app.policy.*`` or
``app.services.policy.*`` -- the dispatch is purely through the
registry's :class:`SimulationUseCase` adapter surface plus the
lane-agnostic state-machine helpers in
:mod:`app.simulation_platform.state_machine`.
"""
from __future__ import annotations

import hashlib
import json
import os
import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple, cast

from ..simulation_platform.use_case import (
    SimulationUseCase,
    invoke_lane_generate_report,
    invoke_lane_run_simulation,
)

from flask import Blueprint, current_app, request

from ..api.error_codes import ErrorCode
from ..config import Config
from ..simulation_platform import idempotency as _idempotency
from ..simulation_platform import registry as platform_registry
from ..simulation_platform.error_codes import PlatformErrorCode
from ..simulation_platform.error_envelope import make_err, make_ok
from ..simulation_platform.auto_report_watcher import (
    AUTO_REPORT_LOCK_FILENAME as _AUTO_REPORT_LOCK_FILENAME,
)
from ..simulation_platform.run_locks import (
    StartLockBusy as _StartLockBusy,
    start_lock as _start_lock,
)
from ..simulation_platform.scale_guard import (
    evaluate_scale_guard,
    PlatformScaleGuardRefused as _PlatformScaleGuardRefused,
)
from ..simulation_platform.llm.router import (
    PreflightMeterPayload,
    check_provider_readiness,
    estimate_external_cost,
    provider_budget_state,
    provider_config_from_payload,
    provider_config_from_state,
)
from ..simulation_platform.statistical import (
    StatisticalConfigError,
    StatisticalConfigPayload,
    StatisticalRuntimeContext,
    apply_statistical_json_patch,
    build_reseed_lineage_event,
    build_statistical_config_payload,
    build_statistical_runtime_context_from_config,
    load_statistical_manifest,
    statistical_settings_diff_ops,
)
from ..utils.atomic_io import atomic_write_json, atomic_write_text
from ..utils.id_validator import safe_join, validate_safe_id
from ..utils.logger import get_logger


logger = get_logger("rawfish.api.use_cases")

_AGENT_ACTIVITY_SETTING_KEYS = {
    "activity_level": ("cohort.activity_level",),
    "posts_per_hour": ("cohort.posts_per_hour",),
    "comments_per_hour": ("cohort.comments_per_hour",),
    "sentiment_bias": ("cohort.sentiment_bias",),
    "influence_weight": ("cohort.influence_weight",),
    "active_hours": ("cohort.active_hours",),
}

_AGENT_ACTIVITY_COHORT_FIELDS = {
    "activity_level": "activity_level",
    "posts_per_hour": "posts_per_hour",
    "comments_per_hour": "comments_per_hour",
    "sentiment_bias": "sentiment_bias",
    "influence_weight": "influence_weight",
    "active_hours": "active_hours",
}

_SOURCE_MODES = frozenset({"paste", "cached", "live", "graph"})
_REPORT_JOB_FILENAME = "report_job.json"
_REPORT_JOBS: Dict[str, Dict[str, Any]] = {}
_REPORT_JOB_FUTURES: Dict[str, Any] = {}
_REPORT_JOBS_LOCK = threading.Lock()
try:
    _REPORT_JOB_MAX_WORKERS = max(
        1,
        int(os.environ.get("RAWFISH_REPORT_JOB_WORKERS", "2")),
    )
except ValueError:
    _REPORT_JOB_MAX_WORKERS = 2
_REPORT_EXECUTOR = ThreadPoolExecutor(
    max_workers=_REPORT_JOB_MAX_WORKERS,
    thread_name_prefix="rawfish-report",
)

# Single blueprint mounted at /api/sim/use-cases/ in the app factory.
use_cases_bp = Blueprint("use_cases", __name__)


# ----------------------------------------------------------------------
# Auth envelope normalizer
# ----------------------------------------------------------------------
#
# The app-wide ``require_api_key`` middleware returns a flat
# ``{"error": "Unauthorized"}`` shape. The generic blueprint upgrades
# that into the structured envelope every product route uses.
@use_cases_bp.after_request
def _normalize_auth_envelope(response):
    if response.status_code != 401:
        return response
    if not response.is_json:
        return response
    try:
        body = response.get_json(silent=True)
    except Exception:  # noqa: BLE001
        return response
    if not isinstance(body, dict):
        return response
    err = body.get("error")
    if not isinstance(err, str):
        return response
    structured = {
        "success": False,
        "error": {
            "code": "UNAUTHORIZED",
            "message": "Missing or invalid API key.",
            "details": {},
        },
    }
    response.set_data(json.dumps(structured))
    response.content_type = "application/json"
    return response


# ----------------------------------------------------------------------
# Local helpers (lane-agnostic; no app.policy imports)
# ----------------------------------------------------------------------


def _ok(data: Any, status: int = 200):
    return make_ok(data, status)


def _err(
    code: "ErrorCode | PlatformErrorCode | str",
    message: str,
    status: int,
    details: Optional[Dict[str, Any]] = None,
):
    # Release the per-Idempotency-Key claim sentinel BEFORE returning the error
    # envelope. A first-writer that errored MUST drop the sentinel so a same-key
    # retry of a corrected payload is not blocked behind a stale claim for the
    # full 5s wait window. The ownership-gated implementation in
    # :func:`app.simulation_platform.idempotency.release_claim_if_any`
    # no-ops for losers / replays / requests without the header, so
    # this is safe to call unconditionally on every error path.
    _idempotency.release_claim_if_any()
    return make_err(code, message, status, details)


def _audience_store_prepare_error(
    exc: Exception,
    *,
    use_case_id: str,
    simulation_id: str,
):
    """Map audience-store setup failures to operator-fixable responses."""

    message = str(exc)
    details = {
        "use_case_id": use_case_id,
        "simulation_id": simulation_id,
    }
    if (
        "ZEP_MODE=" in message
        and "is not supported; expected one of" in message
    ):
        details["reason"] = "invalid_zep_mode"
        return _err(
            ErrorCode.INVALID_ZEP_MODE,
            message,
            400,
            details,
        )
    if "ZEP_MODE=experimental_cloud requires ZEP_API_KEY" in message:
        details["reason"] = "zep_api_key_missing"
        return _err(
            ErrorCode.ZEP_API_KEY_MISSING,
            "ZEP_MODE=experimental_cloud requires ZEP_API_KEY before "
            "prepare can publish the lane ontology.",
            400,
            details,
        )
    if "ZEP_MODE=graphiti requires NEO4J_URI" in message:
        details["reason"] = "neo4j_uri_missing"
        return _err(
            ErrorCode.ZEP_GRAPHITI_UNAVAILABLE,
            "ZEP_MODE=graphiti requires NEO4J_URI before prepare can "
            "publish the lane ontology.",
            503,
            details,
        )
    if exc.__class__.__name__ == "GraphitiInitError":
        details["reason"] = "graphiti_init_failed"
        return _err(
            ErrorCode.ZEP_GRAPHITI_UNAVAILABLE,
            f"Graphiti audience store is unavailable: {message}",
            503,
            details,
        )
    return None


def _resolve_use_case(
    use_case_id: str,
) -> Tuple[Optional[SimulationUseCase], Optional[Any]]:
    """Look up the registered adapter or return a 404 envelope.

    Returns ``(adapter, None)`` on success and ``(None, err_response)``
    on miss. Callers that have already guarded ``err is not None`` may
    assume ``adapter`` is non-None; the type checker cannot correlate
    the two ``Optional``s across the tuple unpack, so call sites use
    ``assert adapter is not None`` after the early return to narrow.
    """
    try:
        adapter = platform_registry.get(use_case_id)
    except KeyError:
        return None, _err(
            PlatformErrorCode.USE_CASE_NOT_REGISTERED,
            f"no use case registered for {use_case_id!r}",
            404,
            {"use_case_id": use_case_id},
        )
    return cast(SimulationUseCase, adapter), None


def _safe_basename_artifact(name: str, *, field: str) -> Optional[Tuple[Any, int]]:
    """Reject an adapter ``artifact_names`` entry that is anything
    other than a simple basename inside the run dir.

    Three failure shapes:
      * empty / non-string  -- the adapter contract is violated.
      * contains a path separator (``/`` or os.sep) -- could escape
        the run dir via ``Path(run_dir) / "../../escape"``.
      * absolute path       -- ``Path(run_dir) / "/etc/passwd"`` in
        Python ignores the run_dir entirely and lands at the
        absolute path.

    Returns ``None`` on success (the caller proceeds), or an error
    envelope tuple on failure so the caller can ``return`` it.
    """
    if not isinstance(name, str) or not name:
        return _err(
            PlatformErrorCode.INVALID_ADAPTER_ARTIFACT_NAME,
            f"adapter artifact_names[{field!r}] must be a non-empty string",
            500,
            {"field": field, "value": repr(name)},
        )
    # Reject any path separator or absolute path. ``os.sep`` covers
    # the platform-native separator; we additionally check ``"/"``
    # explicitly because adapters may have been authored on a
    # POSIX dev box and run on a Windows host where ``os.sep`` is
    # ``\\``.
    if "/" in name or os.sep in name or name.startswith("/"):
        return _err(
            PlatformErrorCode.INVALID_ADAPTER_ARTIFACT_NAME,
            (
                f"adapter artifact_names[{field!r}] must be a basename, "
                f"not a path; got {name!r}"
            ),
            500,
            {"field": field, "value": name},
        )
    if name in {".", ".."}:
        return _err(
            PlatformErrorCode.INVALID_ADAPTER_ARTIFACT_NAME,
            f"adapter artifact_names[{field!r}] is a path-traversal token: {name!r}",
            500,
            {"field": field, "value": name},
        )
    return None


def _wrap_idempotent(handler):
    """Decorator: every mutating route in this blueprint must run
    through the platform's :func:`idempotency.lookup` / :func:`store`
    helpers so a same-key replay returns the cached response and a
    same-key different-body replay returns IDEMPOTENCY_KEY_MISMATCH
    (instead of letting the handler double-execute its side effects).

    The handler receives the parsed request body verbatim; the
    decorator owns reading + lookup + invoking the handler + storing
    the response on 2xx.

    No-ops when the request omits the ``Idempotency-Key`` header --
    the body is still parsed but lookup/store skip. This preserves
    existing tests that don't send the header.
    """
    from functools import wraps

    @wraps(handler)
    def _wrapped(*args, **kwargs):
        body = request.get_json(silent=True) or {}
        cached = _idempotency.lookup(body, _err)
        if cached is not None:
            return cached
        response = handler(body, *args, **kwargs)
        # ``response`` is the Flask tuple ``(json_body, status)``
        # returned by ``_ok`` / ``_err``. Cache only 2xx (idempotency
        # store helper's own 2xx-only check kicks in too; this is
        # belt-and-braces so the contract is obvious at the wrapper
        # site).
        try:
            _, status = response
        except (TypeError, ValueError):
            status = 200
        try:
            json_payload = (
                response[0].get_json()
                if hasattr(response[0], "get_json")
                else response[0]
            )
        except Exception:  # noqa: BLE001
            json_payload = None
        if isinstance(status, int) and json_payload is not None:
            _idempotency.store(body, json_payload, status)
        return response

    return _wrapped


def _run_dir_for(use_case_id: str, simulation_id: str) -> Path:
    """Resolve the per-run scratch directory under the use-case namespace."""
    base = safe_join(Config.OASIS_SIMULATION_DATA_DIR, use_case_id)
    os.makedirs(base, exist_ok=True)
    return Path(safe_join(base, simulation_id))


# ----------------------------------------------------------------------
# Routes
# ----------------------------------------------------------------------


@use_cases_bp.route("", methods=["GET"])
@use_cases_bp.route("/", methods=["GET"])
def list_use_cases():
    """Return registered RawFish lanes and their published manifests."""

    lanes = []
    for lane_id in platform_registry.list_use_cases():
        try:
            adapter = platform_registry.get(lane_id)
            catalog = adapter.catalog()
        except Exception as exc:  # noqa: BLE001
            return _err(
                PlatformErrorCode.ADAPTER_CATALOG_FAILED,
                f"adapter {lane_id!r} catalog() raised {type(exc).__name__}",
                502,
                {"use_case_id": lane_id},
            )
        lanes.append({
            "use_case_id": lane_id,
            "lane_manifest": catalog.lane_manifest.model_dump(mode="json"),
        })
    return _ok({
        "lane_ids": [lane["use_case_id"] for lane in lanes],
        "use_cases": lanes,
    })


@use_cases_bp.route(
    "/<use_case_id>/personas", methods=["GET"],
)
def get_personas(use_case_id: str):
    """Return the per-use-case catalog rows + per-persona indexes.

    Filters the registry-aggregated catalog down to the rows whose
    ``use_case_id`` matches the URL parameter.
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    try:
        catalog = adapter.catalog()
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_CATALOG_FAILED,
            f"adapter {use_case_id!r} catalog() raised {type(exc).__name__}",
            502,
            {"use_case_id": use_case_id},
        )
    personas = []
    scopes_by_persona: Dict[str, Any] = {}
    segment_types_by_persona: Dict[str, Any] = {}
    report_sections_by_persona: Dict[str, Any] = {}
    for spec in catalog.personas:
        row: Dict[str, Any] = {
            "persona": spec.persona_id,
            "use_case_id": spec.use_case_id or use_case_id,
            "label": spec.label,
            "cohort_question": spec.cohort_question,
        }
        if spec.scopes is not None:
            row["scope_options"] = list(spec.scopes)
            scopes_by_persona[spec.persona_id] = list(spec.scopes)
        if spec.defaults:
            row["defaults"] = dict(spec.defaults)
        for scope_key, allowed in spec.segment_types_by_scope.items():
            key = (
                spec.persona_id
                if scope_key is None
                else f"{spec.persona_id}:{scope_key}"
            )
            segment_types_by_persona[key] = list(allowed)
        # Surface ``report_sections`` (unscoped) directly on the row
        # so a frontend TOC renderer can read it without traversing
        # the by-scope index. The denormalised
        # ``report_sections_by_persona`` index also lands so
        # scoped personas (key = ``<persona>:<scope>``) are
        # reachable through the same shape as ``segment_types_by_persona``.
        for scope_key, sections in spec.report_sections_by_scope.items():
            section_list = list(sections)
            if scope_key is None and len(spec.report_sections_by_scope) == 1:
                row["report_sections"] = section_list
            else:
                row.setdefault("report_sections_by_scope", {})[
                    str(scope_key)
                ] = section_list
            persona_key = (
                spec.persona_id
                if scope_key is None
                else f"{spec.persona_id}:{scope_key}"
            )
            report_sections_by_persona[persona_key] = section_list
        personas.append(row)
    return _ok({
        "use_case_id": use_case_id,
        "lane_manifest": catalog.lane_manifest.model_dump(mode="json"),
        "personas": personas,
        "scopes_by_persona": scopes_by_persona,
        "segment_types_by_persona": segment_types_by_persona,
        "report_sections_by_persona": report_sections_by_persona,
    })


@use_cases_bp.route(
    "/<use_case_id>/catalog", methods=["GET"],
)
def get_catalog(use_case_id: str):
    """Return the full RawFish catalog payload including lane_manifest."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    try:
        catalog = adapter.catalog()
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_CATALOG_FAILED,
            f"adapter {use_case_id!r} catalog() raised {type(exc).__name__}",
            502,
            {"use_case_id": use_case_id},
        )
    return _ok(catalog.model_dump(mode="json"))


@use_cases_bp.route(
    "/<use_case_id>/scenario/parse", methods=["POST"],
)
def parse_scenario_seed(use_case_id: str):
    """Parse operator seed text into a lane-authored scenario draft."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    body = request.get_json(silent=True) or {}
    if not isinstance(body, dict):
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "request body must be an object",
            400,
            {"use_case_id": use_case_id, "reason": "parse_body_invalid"},
        )
    seed_text = str(body.get("seed_text") or "").strip()
    if not seed_text:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "seed_text is required",
            400,
            {"use_case_id": use_case_id, "reason": "seed_text_required"},
        )
    stress_question = str(body.get("stress_question") or seed_text).strip()
    try:
        catalog = adapter.catalog()
        default_persona = (
            catalog.personas[0].persona_id if catalog.personas else "default"
        )
        persona = str(body.get("persona") or default_persona).strip()
        scope_raw = body.get("scope")
        scope = None if scope_raw in (None, "") else str(scope_raw)
        draft = adapter.parse_seed(
            seed_text=seed_text,
            stress_question=stress_question,
            persona=persona,
            scope=scope,
        )
    except Exception as exc:  # noqa: BLE001 -- adapter owns parse exceptions
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            f"scenario parse failed: {type(exc).__name__}: {exc}",
            400,
            {"use_case_id": use_case_id, "reason": "scenario_parse_failed"},
        )
    if hasattr(draft, "model_dump"):
        draft_payload = draft.model_dump(mode="json")
    else:
        draft_payload = draft
    parse_source = "fallback"
    parser = "adapter.parse_seed"
    if isinstance(draft_payload, dict):
        draft_payload = dict(draft_payload)
        meta = draft_payload.pop("_parse_meta", None)
        if isinstance(meta, dict):
            parse_source = str(meta.get("parse_source") or parse_source)
            parser = str(meta.get("parser") or parser)
        parse_source = str(
            draft_payload.pop("parse_source", draft_payload.pop("_parse_source", parse_source))
            or parse_source
        )
        parser = str(
            draft_payload.pop("parser", draft_payload.pop("_parser", parser))
            or parser
        )
    return _ok({
        "use_case_id": use_case_id,
        "parse_source": parse_source,
        "parser": parser,
        "scenario_draft": draft_payload,
    })


@use_cases_bp.route(
    "/<use_case_id>/evals", methods=["GET"],
)
def list_evals(use_case_id: str):
    """Return eval instruments advertised by this lane."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    catalog = adapter.catalog()
    instruments = catalog.lane_manifest.eval_instruments
    evals = [
        {"eval_id": "readiness", "slot": "scenario_editor", "caveat": None},
        {"eval_id": "preflight_meter", "slot": "preflight_meter", "caveat": None},
    ]
    analysis = getattr(catalog.lane_manifest, "analysis_panels", {}) or {}
    if analysis.get("sensitivity", {}).get("enabled"):
        evals.append({
            "eval_id": "sensitivity_tornado",
            "slot": "analysis_sensitivity_panel",
            "caveat": "static_kernel_v1",
        })
    if analysis.get("counterfactual", {}).get("enabled"):
        evals.append({
            "eval_id": "counterfactual_fork",
            "slot": "analysis_counterfactual_panel",
            "caveat": None,
        })
    return _ok({
        "use_case_id": use_case_id,
        "evals": evals,
        "eval_instruments": instruments,
    })


def _load_statistical_manifest_or_err(use_case_id: str, adapter: SimulationUseCase):
    """Load a lane's Statistical Workbench manifest or return an envelope."""
    try:
        catalog = adapter.catalog()
        manifest_name = catalog.lane_manifest.statistical_manifest_path
        return load_statistical_manifest(
            use_case_id,
            manifest_filename=manifest_name,
        ), None
    except StatisticalConfigError as exc:
        return None, _err(
            PlatformErrorCode.INVALID_INPUT,
            str(exc),
            500,
            {"use_case_id": use_case_id, "reason": "statistical_manifest_invalid"},
        )
    except Exception as exc:  # noqa: BLE001
        return None, _err(
            PlatformErrorCode.ADAPTER_CATALOG_FAILED,
            f"adapter {use_case_id!r} catalog() raised {type(exc).__name__}",
            502,
            {"use_case_id": use_case_id},
        )


def _resolve_statistical_config_or_err(
    use_case_id: str,
    adapter: SimulationUseCase,
    state: Dict[str, Any],
    *,
    required: bool = True,
    invalid_status: int = 500,
    invalid_code: PlatformErrorCode = PlatformErrorCode.STATE_CORRUPTED,
    invalid_reason: str = "statistical_settings_state_invalid",
) -> Tuple[Optional[StatisticalConfigPayload], Optional[Any]]:
    """Return the run's resolved Statistical Workbench config.

    Missing ``state["statistical_settings"]`` means "use manifest
    defaults", not "skip the workbench". This makes default workbench
    values load-bearing even when a client creates a run and moves
    directly to prepare/start without an explicit settings POST.
    """

    manifest, manifest_err = _load_statistical_manifest_or_err(
        use_case_id, adapter,
    )
    if manifest_err is not None:
        if not required and not isinstance(state.get("statistical_settings"), dict):
            return None, None
        return None, manifest_err
    assert manifest is not None
    try:
        settings = state.get("statistical_settings")
        if not isinstance(settings, dict):
            settings = None
        return build_statistical_config_payload(manifest, settings), None
    except StatisticalConfigError as exc:
        message_prefix = (
            "statistical settings invalid"
            if invalid_status == 400 else
            "persisted statistical settings invalid"
        )
        return None, _err(
            invalid_code,
            f"{message_prefix}: {exc}",
            invalid_status,
            {
                "use_case_id": use_case_id,
                "simulation_id": state.get("simulation_id"),
                "reason": invalid_reason,
            },
        )


def _apply_statistical_config_to_state(
    state: Dict[str, Any],
    config: StatisticalConfigPayload,
) -> StatisticalRuntimeContext:
    """Persist the canonical Statistical Workbench config into state."""

    context = build_statistical_runtime_context_from_config(config)
    state["statistical_settings"] = config.settings
    state["statistical_settings_hash"] = config.statistical_settings_hash
    state["statistical_settings_version"] = config.version
    state["provenance_per_field"] = config.provenance_per_field
    state["lock_state_per_field"] = config.lock_state_per_field
    state["persona_salts_resolved"] = config.persona_salts_resolved
    state["prior_attachments"] = config.prior_attachments
    state["statistical_runtime_overrides"] = context.runtime_overrides.model_dump(
        mode="json",
        exclude_none=True,
    )
    state["statistical_config_path"] = "statistical_settings.json"
    return context


def _scenario_cohort_ids_from_state(state: Dict[str, Any]) -> set[str]:
    """Return the stakeholder ids that are valid for run-scoped settings."""

    scenario = state.get("scenario")
    if not isinstance(scenario, dict):
        return set()
    cohort_ids: set[str] = set()
    for key in ("stakeholders", "audience_segments", "segments"):
        entries = scenario.get(key)
        if not isinstance(entries, list):
            continue
        for index, entry in enumerate(entries):
            if not isinstance(entry, dict):
                continue
            raw_id = (
                entry.get("segment_id")
                or entry.get("cohort_id")
                or entry.get("id")
                or f"cohort_{index + 1}"
            )
            cohort_id = str(raw_id).strip()
            if cohort_id:
                cohort_ids.add(cohort_id)
    return cohort_ids


def _validate_statistical_ops_for_run_cohorts(
    *,
    applied_ops: List[Dict[str, Any]],
    state: Dict[str, Any],
    use_case_id: str,
    sim_id: str,
) -> Optional[Any]:
    """Reject Workbench ops that name cohorts outside the run scenario."""

    allowed_cohort_ids = _scenario_cohort_ids_from_state(state)
    if not allowed_cohort_ids:
        return None
    requested: set[str] = set()
    for op in applied_ops:
        cohort_id = op.get("cohort_id")
        if isinstance(cohort_id, str) and cohort_id:
            requested.add(cohort_id)
        elif op.get("field_id") == "run.persona_salts":
            map_key = op.get("map_key")
            if isinstance(map_key, str) and map_key:
                requested.add(map_key)
    invalid = sorted(requested - allowed_cohort_ids)
    if not invalid:
        return None
    return _err(
        PlatformErrorCode.INVALID_INPUT,
        "statistical settings patch references unknown run cohorts",
        422,
        {
            "use_case_id": use_case_id,
            "simulation_id": sim_id,
            "reason": "cohort_not_in_run",
            "invalid_cohort_ids": invalid,
            "allowed_cohort_ids": sorted(allowed_cohort_ids),
        },
    )


def _validate_statistical_settings_for_run_cohorts(
    *,
    settings: Dict[str, Any],
    state: Dict[str, Any],
    use_case_id: str,
    sim_id: str,
) -> Optional[Any]:
    """Reject persisted settings that name cohorts outside the run scenario."""

    allowed_cohort_ids = _scenario_cohort_ids_from_state(state)
    if not allowed_cohort_ids:
        return None
    requested: set[str] = set()
    cohort_settings = settings.get("cohorts")
    if isinstance(cohort_settings, dict):
        requested.update(str(cohort_id) for cohort_id in cohort_settings)
    persona_salts = settings.get("run.persona_salts")
    if isinstance(persona_salts, dict):
        requested.update(str(cohort_id) for cohort_id in persona_salts)
    invalid = sorted(
        cohort_id for cohort_id in requested if cohort_id not in allowed_cohort_ids
    )
    if not invalid:
        return None
    return _err(
        PlatformErrorCode.INVALID_INPUT,
        "statistical settings reference unknown run cohorts",
        422,
        {
            "use_case_id": use_case_id,
            "simulation_id": sim_id,
            "reason": "cohort_not_in_run",
            "invalid_cohort_ids": invalid,
            "allowed_cohort_ids": sorted(allowed_cohort_ids),
        },
    )


def _json_pointer_escape(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def _file_artifact_entry(name: str, path: Path) -> Dict[str, Any]:
    raw = path.read_bytes()
    return {
        "name": name,
        "relative_path": name,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
    }


def _upsert_prepare_artifact(
    manifest: Dict[str, Any],
    *,
    name: str,
    path: Path,
) -> None:
    artifacts = manifest.get("artifacts")
    if isinstance(artifacts, dict):
        artifacts[name] = name
        return
    entry = _file_artifact_entry(name, path)
    if not isinstance(artifacts, list):
        manifest["artifacts"] = [entry]
        return
    for index, existing in enumerate(artifacts):
        if not isinstance(existing, dict):
            continue
        if existing.get("name") == name or existing.get("relative_path") == name:
            artifacts[index] = entry
            return
    artifacts.append(entry)


def _prepare_artifact_maps(
    *,
    run_dir: Path,
    manifest: Any,
) -> Tuple[Dict[str, str], Dict[str, str]]:
    """Extract relative prepare artifact paths and current file hashes."""

    if hasattr(manifest, "model_dump"):
        manifest_payload = manifest.model_dump(mode="json")
    elif isinstance(manifest, dict):
        manifest_payload = manifest
    else:
        manifest_payload = {}
    artifacts = manifest_payload.get("artifacts")
    relative_paths: Dict[str, str] = {}
    if isinstance(artifacts, dict):
        for name, relative_path in artifacts.items():
            if isinstance(name, str) and isinstance(relative_path, str):
                relative_paths[name] = relative_path
    elif isinstance(artifacts, list):
        for item in artifacts:
            if not isinstance(item, dict):
                continue
            name = item.get("name")
            relative_path = item.get("relative_path") or item.get("path")
            if isinstance(name, str) and isinstance(relative_path, str):
                relative_paths[name] = relative_path
    if not relative_paths:
        manifest_path = run_dir / "manifest.json"
        if manifest_path.is_file():
            relative_paths["manifest.json"] = "manifest.json"

    hashes: Dict[str, str] = {}
    safe_paths: Dict[str, str] = {}
    for name, relative_path in relative_paths.items():
        try:
            path = Path(relative_path)
            if path.is_absolute() or ".." in path.parts:
                continue
            artifact_path = run_dir / path
            if not artifact_path.is_file():
                continue
            digest = hashlib.sha256(artifact_path.read_bytes()).hexdigest()
        except OSError:
            continue
        safe_paths[name] = relative_path
        hashes[name] = digest
    return safe_paths, hashes


def _persist_run_metadata_if_missing(
    *,
    run_dir: Path,
    state: Dict[str, Any],
    manifest: Any,
) -> None:
    """Create a lane-neutral ``run_metadata.json`` for generic lanes.

    Policy adapters that own richer typed metadata can write the same file
    themselves; this helper only fills the gap when no durable metadata exists.
    """

    meta_path = run_dir / "run_metadata.json"
    if meta_path.exists():
        return

    from ..simulation_platform.run_metadata import RunMetadata, RunPersona, ScaleCaps

    scenario_payload = state.get("scenario") or {}
    if not isinstance(scenario_payload, dict):
        scenario_payload = {}
    raw_scenario = json.dumps(
        scenario_payload,
        sort_keys=True,
        default=str,
    ).encode("utf-8")
    artifact_paths, artifact_hashes = _prepare_artifact_maps(
        run_dir=run_dir,
        manifest=manifest,
    )
    if not artifact_paths or not artifact_hashes:
        return
    runtime_overrides = state.get("statistical_runtime_overrides")
    if not isinstance(runtime_overrides, dict):
        runtime_overrides = {}
    settings = state.get("statistical_settings")
    if not isinstance(settings, dict):
        settings = {}
    lineage = state.get("statistical_variant_lineage")
    if not isinstance(lineage, list):
        lineage = []
    provenance = state.get("provenance_per_field")
    if not isinstance(provenance, dict):
        provenance = {}
    locks = state.get("lock_state_per_field")
    if not isinstance(locks, dict):
        locks = {}
    persona_salts = runtime_overrides.get("persona_salts")
    if not isinstance(persona_salts, dict):
        persona_salts = {}
    prior_attachments = state.get("prior_attachments")
    if not isinstance(prior_attachments, dict):
        prior_attachments = {}

    rounds = _coerce_positive_int(
        runtime_overrides.get("rounds")
        or runtime_overrides.get("drift_horizon_rounds")
        or scenario_payload.get("drift_horizon_rounds"),
        1,
    )
    ensemble_n = _coerce_positive_int(runtime_overrides.get("ensemble_n"), 1)
    stakeholders_raw = scenario_payload.get("stakeholders")
    stakeholders = len(stakeholders_raw) if isinstance(stakeholders_raw, list) else 1

    metadata = RunMetadata(
        simulation_id=str(state.get("simulation_id") or run_dir.name),
        created_at=datetime.fromisoformat(
            str(state.get("created_at") or _utcnow()),
        ),
        persona=RunPersona.CREATOR,
        scenario_hash=hashlib.sha256(raw_scenario).hexdigest(),
        seed_hash=hashlib.sha256(
            (str(state.get("simulation_id") or run_dir.name) + ":seed").encode(
                "utf-8",
            ),
        ).hexdigest(),
        prepared_at=datetime.fromisoformat(
            str(state.get("prepared_at") or _utcnow()),
        ),
        artifact_paths=artifact_paths,
        artifact_hashes=artifact_hashes,
        zep_mode="mock",
        scale_caps=ScaleCaps(
            ensemble_n=ensemble_n,
            stakeholders=max(1, stakeholders),
            rounds=rounds,
            cap_value=_coerce_positive_int(os.environ.get("SCALE_CAP_POC"), 100),
        ),
        statistical_settings_hash=state.get("statistical_settings_hash"),
        statistical_settings_version=state.get("statistical_settings_version"),
        statistical_settings=settings,
        statistical_runtime_overrides=runtime_overrides,
        statistical_variant_lineage=[
            item for item in lineage if isinstance(item, dict)
        ],
        persona_salts_resolved={
            str(key): str(value) for key, value in persona_salts.items()
        },
        prior_attachments=prior_attachments,
        provenance_per_field={
            str(key): str(value) for key, value in provenance.items()
        },
        lock_state_per_field={
            str(key): bool(value) for key, value in locks.items()
        },
    )
    atomic_write_text(str(meta_path), metadata.model_dump_json(indent=2))


def _normalized_agent_active_hours(value: Any) -> Optional[List[int]]:
    if not isinstance(value, list):
        return None
    hours = sorted({
        int(hour) for hour in value
        if isinstance(hour, int) and not isinstance(hour, bool) and 0 <= int(hour) <= 23
    })
    return hours or None


def _normalized_agent_scalar(value: Any) -> Optional[float]:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    return float(value)


def _agent_activity_overrides_from_settings(
    settings: Dict[str, Any],
) -> Dict[str, Any]:
    overrides: Dict[str, Any] = {}
    for target_field, setting_keys in _AGENT_ACTIVITY_SETTING_KEYS.items():
        for setting_key in setting_keys:
            if setting_key not in settings:
                continue
            raw_value = settings[setting_key]
            normalized = (
                _normalized_agent_active_hours(raw_value)
                if target_field == "active_hours"
                else _normalized_agent_scalar(raw_value)
            )
            if normalized is not None:
                overrides[target_field] = normalized
            break
    return overrides


def _cohort_agent_activity_overrides_from_runtime(
    runtime_overrides: Any,
) -> Dict[str, Dict[str, Any]]:
    cohort_overrides = getattr(runtime_overrides, "cohort_overrides", None) or {}
    if not isinstance(cohort_overrides, dict):
        return {}

    agent_overrides: Dict[str, Dict[str, Any]] = {}
    for cohort_id, sections in cohort_overrides.items():
        if not isinstance(cohort_id, str) or not isinstance(sections, dict):
            continue
        statistical = sections.get("statistical")
        if not isinstance(statistical, dict):
            continue
        for source_field, target_field in _AGENT_ACTIVITY_COHORT_FIELDS.items():
            if source_field not in statistical:
                continue
            raw_value = statistical[source_field]
            normalized = (
                _normalized_agent_active_hours(raw_value)
                if target_field == "active_hours"
                else _normalized_agent_scalar(raw_value)
            )
            if normalized is None:
                continue
            agent_overrides.setdefault(cohort_id, {})[target_field] = normalized

    active_hours_by_cohort = (
        getattr(runtime_overrides, "active_hours_by_cohort", None) or {}
    )
    if isinstance(active_hours_by_cohort, dict):
        for cohort_id, hours in active_hours_by_cohort.items():
            if not isinstance(cohort_id, str):
                continue
            normalized = _normalized_agent_active_hours(hours)
            if normalized is not None:
                agent_overrides.setdefault(cohort_id, {})["active_hours"] = normalized

    return agent_overrides


def _persist_statistical_prepare_artifacts(
    *,
    run_dir: Path,
    config: StatisticalConfigPayload,
    manifest: Any,
) -> Any:
    """Persist resolved workbench settings into prepare/runtime artifacts.

    This makes the supported settings load-bearing without pretending
    every manifest field changes the simulation kernel. Known runtime
    knobs are applied where a real seam exists: supported agent activity
    fields go into ``simulation_config.json`` agent configs, while the full
    resolved settings and hash are persisted as an auditable artifact for
    every lane.
    """

    manifest_payload: Optional[Dict[str, Any]]
    if hasattr(manifest, "model_dump"):
        manifest_payload = manifest.model_dump(mode="json")
    elif isinstance(manifest, dict) and manifest:
        manifest_payload = dict(manifest)
    else:
        manifest_path = run_dir / "manifest.json"
        if manifest_path.exists():
            try:
                loaded_manifest = json.loads(
                    manifest_path.read_text(encoding="utf-8"),
                )
            except (OSError, json.JSONDecodeError):
                loaded_manifest = None
            manifest_payload = (
                loaded_manifest if isinstance(loaded_manifest, dict) else None
            )
        else:
            manifest_payload = None

    context = build_statistical_runtime_context_from_config(config)
    settings_artifact = run_dir / "statistical_settings.json"
    atomic_write_json(
        str(settings_artifact),
        {
            **context.model_dump(mode="json"),
            "field_ids": config.field_ids,
            "provenance_per_field": config.provenance_per_field,
            "lock_state_per_field": config.lock_state_per_field,
        },
    )
    if isinstance(manifest_payload, dict):
        manifest_payload["statistical_settings_hash"] = (
            config.statistical_settings_hash
        )
        manifest_payload["provenance_per_field"] = config.provenance_per_field
        manifest_payload["lock_state_per_field"] = config.lock_state_per_field
        _upsert_prepare_artifact(
            manifest_payload,
            name="statistical_settings.json",
            path=settings_artifact,
        )

    runtime_overrides = context.runtime_overrides
    global_agent_overrides = _agent_activity_overrides_from_settings(
        config.settings,
    )
    cohort_agent_overrides = _cohort_agent_activity_overrides_from_runtime(
        runtime_overrides,
    )
    scenario_cohort_ids: List[str] = []
    state_path = run_dir / "state.json"
    try:
        state_payload = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        state_payload = {}
    if isinstance(state_payload, dict):
        scenario_payload = state_payload.get("scenario")
        if isinstance(scenario_payload, dict):
            stakeholders = scenario_payload.get("stakeholders")
            if isinstance(stakeholders, list):
                for idx, stakeholder in enumerate(stakeholders):
                    if isinstance(stakeholder, dict):
                        scenario_cohort_ids.append(
                            str(stakeholder.get("segment_id") or f"cohort_{idx + 1}")
                        )
    sim_config_path = run_dir / "simulation_config.json"
    if sim_config_path.is_file():
        try:
            sim_config = json.loads(sim_config_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            sim_config = None
        if isinstance(sim_config, dict):
            sim_config["statistical_settings_hash"] = (
                config.statistical_settings_hash
            )
            agent_configs = sim_config.get("agent_configs")
            if isinstance(agent_configs, list):
                for idx, agent_config in enumerate(agent_configs):
                    if not isinstance(agent_config, dict):
                        continue
                    cohort_id = (
                        scenario_cohort_ids[idx]
                        if idx < len(scenario_cohort_ids)
                        else None
                    )
                    overrides = dict(global_agent_overrides)
                    if cohort_id is not None:
                        overrides.update(cohort_agent_overrides.get(cohort_id, {}))
                    for field_name, value in overrides.items():
                        agent_config[field_name] = value
            atomic_write_json(str(sim_config_path), sim_config)
            if manifest_payload is not None:
                _upsert_prepare_artifact(
                    manifest_payload,
                    name="simulation_config.json",
                    path=sim_config_path,
                )

    if manifest_payload is not None:
        manifest_path = run_dir / "manifest.json"
        if manifest_path.exists():
            atomic_write_json(str(manifest_path), manifest_payload)
        return manifest_payload
    return manifest


def _create_body_statistical_settings(body: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Extract optional create-time Statistical Workbench settings."""

    direct = body.get("statistical_settings")
    if isinstance(direct, dict):
        return direct
    nested = body.get("statistical_config")
    if isinstance(nested, dict) and isinstance(nested.get("settings"), dict):
        return nested["settings"]
    return None


@use_cases_bp.route(
    "/<use_case_id>/statistical-manifest", methods=["GET"],
)
def get_statistical_manifest(use_case_id: str):
    """Return the lane-owned Statistical Workbench manifest plus defaults."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    manifest, manifest_err = _load_statistical_manifest_or_err(use_case_id, adapter)
    if manifest_err is not None:
        return manifest_err
    assert manifest is not None
    config = build_statistical_config_payload(manifest)
    return _ok({
        "manifest": manifest.model_dump_public(),
        "default_config": config.model_dump(mode="json"),
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/statistical-config", methods=["GET"],
)
def get_statistical_config(use_case_id: str, sim_id: str):
    """Return the persisted or default Statistical Workbench config for a run."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None
    manifest, manifest_err = _load_statistical_manifest_or_err(use_case_id, adapter)
    if manifest_err is not None:
        return manifest_err
    assert manifest is not None
    config = build_statistical_config_payload(
        manifest,
        state.get("statistical_settings"),
    )
    return _ok(config.model_dump(mode="json"))


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/statistical-config", methods=["PATCH"],
)
@_wrap_idempotent
def patch_statistical_config(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Apply the Workbench JSON Pointer patch surface.

    Request paths use the Workbench JSON Pointer shape
    (``/run/run_seed``, ``/run/persona_salts/<cohort>``, selected
    ``/cohorts/*/...`` controls). The mapper in ``statistical.py`` resolves
    them to canonical setting keys and rejects paths that the active lane
    manifest does not declare.
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    try:
        run_dir.mkdir(parents=True, exist_ok=True)
        with _start_lock(str(run_dir), sim_id):
            return _patch_statistical_config_locked(
                body=body,
                adapter=adapter,
                use_case_id=use_case_id,
                sim_id=sim_id,
                run_dir=run_dir,
            )
    except _StartLockBusy:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"a /start is in flight for simulation {sim_id!r}; "
            "cannot patch statistical settings",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "statistical_patch_blocked_by_start_in_progress",
            },
        )


def _patch_statistical_config_locked(
    *,
    body: Dict[str, Any],
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None
    if state.get("phase") in {"starting", "running", "completed", "reported"}:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            "statistical settings cannot be patched after start; fork a variant instead",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "current_phase": state.get("phase"),
                "reason": "statistical_settings_locked_after_start",
            },
        )
    manifest, manifest_err = _load_statistical_manifest_or_err(use_case_id, adapter)
    if manifest_err is not None:
        return manifest_err
    assert manifest is not None
    current_settings = state.get("statistical_settings")
    if not isinstance(current_settings, dict):
        current_settings = {}
    current_config = build_statistical_config_payload(manifest, current_settings)
    expected_hash = body.get("expected_hash") or request.headers.get("If-Match")
    if expected_hash and expected_hash != current_config.statistical_settings_hash:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            "statistical settings hash is stale",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "stale_config",
                "expected_hash": expected_hash,
                "statistical_settings_hash": current_config.statistical_settings_hash,
                "current_config": current_config.model_dump(mode="json"),
            },
        )
    try:
        ops_payload = cast(Any, body.get("ops"))
        config, applied_ops = apply_statistical_json_patch(
            manifest,
            current_config.settings,
            ops_payload,
        )
        cohort_err = _validate_statistical_ops_for_run_cohorts(
            applied_ops=applied_ops,
            state=state,
            use_case_id=use_case_id,
            sim_id=sim_id,
        )
        if cohort_err is not None:
            return cohort_err
    except StatisticalConfigError as exc:
        reason = (
            "path_not_in_allowlist"
            if "path_not_in_allowlist" in str(exc)
            else "statistical_patch_invalid"
        )
        status = 422 if reason == "path_not_in_allowlist" else 400
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            str(exc),
            status,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": reason,
            },
        )
    _apply_statistical_config_to_state(state, config)
    state["statistical_settings_updated_at"] = _utcnow()
    if state.get("phase") == "prepared":
        state["statistical_settings_requires_reprepare"] = True
    _persist_statistical_prepare_artifacts(
        run_dir=run_dir,
        config=config,
        manifest=manifest,
    )
    atomic_write_json(str(run_dir / "state.json"), state)
    return _ok({
        "statistical_settings_hash": config.statistical_settings_hash,
        "settings": config.settings,
        "applied_ops": applied_ops,
        "rejected_ops": [],
        "validity_flags": [],
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/statistical-config/reseed",
    methods=["POST"],
)
@_wrap_idempotent
def reseed_statistical_config(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Persist a settings variant and append lineage metadata.

    ``seed`` preserves the original seed-only reseed API. ``patch`` and
    ``settings`` support validated Workbench deltas across any exposed
    canonical statistical setting.
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    try:
        run_dir.mkdir(parents=True, exist_ok=True)
        with _start_lock(str(run_dir), sim_id):
            return _reseed_statistical_config_locked(
                body=body,
                adapter=adapter,
                use_case_id=use_case_id,
                sim_id=sim_id,
                run_dir=run_dir,
            )
    except _StartLockBusy:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"a /start is in flight for simulation {sim_id!r}; "
            "cannot reseed statistical settings",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "statistical_reseed_blocked_by_start_in_progress",
            },
        )


def _reseed_statistical_config_locked(
    *,
    body: Dict[str, Any],
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None
    if state.get("phase") in {"starting", "running", "completed", "reported"}:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            "statistical settings cannot be reseeded after start; fork a new run instead",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "current_phase": state.get("phase"),
                "reason": "statistical_settings_locked_after_start",
            },
        )
    manifest, manifest_err = _load_statistical_manifest_or_err(use_case_id, adapter)
    if manifest_err is not None:
        return manifest_err
    assert manifest is not None
    patch_ops = body.get("statistical_patch")
    if not isinstance(patch_ops, list):
        patch_ops = body.get("ops")
    if not isinstance(patch_ops, list):
        patch_ops = None
    scope = str(body.get("scope") or "").strip()
    generated_ops: List[Dict[str, Any]] = []
    if scope in {"run", "new_run_seed"} and "new_run_seed" in body:
        generated_ops.append({
            "op": "replace",
            "path": "/run/run_seed",
            "value": body.get("new_run_seed"),
        })
    elif patch_ops is not None and scope == "new_run_seed":
        generated_ops.append({
            "op": "replace",
            "path": "/run/run_seed",
            "value": int(datetime.now(timezone.utc).timestamp()),
        })
    if scope.startswith("cohort:") and "new_salt" in body:
        cohort_id = scope.split(":", 1)[1].strip()
        if cohort_id:
            generated_ops.append({
                "op": "replace",
                "path": f"/run/persona_salts/{_json_pointer_escape(cohort_id)}",
                "value": str(body.get("new_salt")),
            })
    if generated_ops:
        patch_ops = [*(patch_ops or []), *generated_ops]
    patch_payload = body.get("patch")
    if not isinstance(patch_payload, dict):
        patch_payload = body.get("settings")
    if not isinstance(patch_payload, dict):
        patch_payload = None
    has_seed = "seed" in body
    if not has_seed and patch_payload is None and patch_ops is None:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "request body must include `seed`, `patch`, `settings`, or `statistical_patch`",
            400,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "statistical_patch_missing",
            },
        )
    try:
        seed = int(body["seed"]) if has_seed else None
        current_settings = state.get("statistical_settings")
        if not isinstance(current_settings, dict):
            current_settings = {}
        if patch_ops is not None:
            expected_hash = body.get("expected_statistical_settings_hash")
            if expected_hash:
                current_config = build_statistical_config_payload(
                    manifest,
                    current_settings,
                )
                if expected_hash != current_config.statistical_settings_hash:
                    return _err(
                        PlatformErrorCode.INVALID_STATE,
                        "statistical config is stale",
                        409,
                        {
                            "use_case_id": use_case_id,
                            "simulation_id": sim_id,
                            "reason": "stale_config",
                            "statistical_settings_hash": (
                                current_config.statistical_settings_hash
                            ),
                        },
                    )
            config, applied_ops = apply_statistical_json_patch(
                manifest,
                current_settings,
                patch_ops,
            )
            cohort_err = _validate_statistical_ops_for_run_cohorts(
                applied_ops=applied_ops,
                state=state,
                use_case_id=use_case_id,
                sim_id=sim_id,
            )
            if cohort_err is not None:
                return cohort_err
            event_patch: Dict[str, Any] = {}
            for op in applied_ops:
                if op.get("cohort_id"):
                    event_patch["cohorts"] = config.settings.get("cohorts", {})
                else:
                    field_id = str(op.get("field_id") or "")
                    if field_id:
                        event_patch[field_id] = config.settings.get(field_id)
            event = build_reseed_lineage_event(
                manifest=manifest,
                current_settings=current_settings,
                patch=event_patch,
                reason=str(body.get("reason") or body.get("scope") or "operator_reseed"),
                created_at=_utcnow(),
            )
            event.applied_ops = applied_ops
            config = build_statistical_config_payload(manifest, event.settings)
        else:
            event = build_reseed_lineage_event(
                manifest=manifest,
                current_settings=current_settings,
                seed=seed,
                patch=patch_payload,
                reason=str(body.get("reason") or "operator_reseed"),
                created_at=_utcnow(),
            )
            config = build_statistical_config_payload(manifest, event.settings)
    except (StatisticalConfigError, TypeError, ValueError) as exc:
        status = 422 if "path_not_in_allowlist" in str(exc) else 400
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            str(exc),
            status,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": (
                    "path_not_in_allowlist"
                    if status == 422 else "statistical_reseed_invalid"
                ),
            },
        )
    lineage = list(state.get("statistical_variant_lineage") or [])
    lineage.append(event.model_dump(mode="json"))
    _apply_statistical_config_to_state(state, config)
    state["statistical_settings_updated_at"] = event.created_at
    state["statistical_variant_lineage"] = lineage
    if state.get("phase") == "prepared":
        state["statistical_settings_requires_reprepare"] = True
    _persist_statistical_prepare_artifacts(
        run_dir=run_dir,
        config=config,
        manifest=manifest,
    )
    atomic_write_json(str(run_dir / "state.json"), state)
    return _ok({
        "config": config.model_dump(mode="json"),
        "variant": event.model_dump(mode="json"),
        "lineage_count": len(lineage),
        "preflight": _statistical_preflight_snapshot(state, config),
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/statistical-lineage", methods=["GET"],
)
def get_statistical_lineage(use_case_id: str, sim_id: str):
    """Return deterministic settings-variant lineage for a run."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None
    manifest, manifest_err = _load_statistical_manifest_or_err(use_case_id, adapter)
    if manifest_err is not None:
        return manifest_err
    assert manifest is not None
    return _ok({
        "use_case_id": use_case_id,
        "simulation_id": sim_id,
        "version": manifest.version,
        "statistical_settings_hash": state.get("statistical_settings_hash"),
        "lineage": list(state.get("statistical_variant_lineage") or []),
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/variants", methods=["GET"],
)
def get_statistical_variants(use_case_id: str, sim_id: str):
    """Return Workbench statistical variants for the variant strip."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None
    lineage = list(state.get("statistical_variant_lineage") or [])
    variants = [{
        "variant_id": "base",
        "base_run_id": sim_id,
        "diff_hash": None,
        "statistical_settings_hash": state.get("statistical_settings_hash"),
        "created_at": state.get("created_at"),
        "label": "Base",
    }]
    for event in lineage:
        if not isinstance(event, dict):
            continue
        variants.append({
            "variant_id": event.get("variant_id"),
            "base_run_id": sim_id,
            "diff_hash": event.get("statistical_settings_hash"),
            "statistical_settings_hash": event.get("statistical_settings_hash"),
            "created_at": event.get("created_at"),
            "label": event.get("operation") or "Statistical variant",
        })
    return _ok({
        "use_case_id": use_case_id,
        "simulation_id": sim_id,
        "status": (
            "requires_reprepare"
            if state.get("statistical_settings_requires_reprepare") else "current"
        ),
        "axis": request.args.get("axis") or "statistical",
        "variants": variants,
    })


def _read_state_for_subject(use_case_id: str, subject_id: str) -> Optional[Dict[str, Any]]:
    """Read a run state by id without creating directories."""
    try:
        validate_safe_id(use_case_id, "use_case_id")
        validate_safe_id(subject_id, "subject_id")
        run_dir = Path(safe_join(
            safe_join(Config.OASIS_SIMULATION_DATA_DIR, use_case_id),
            subject_id,
        ))
    except ValueError:
        return None
    return _read_state_unsafe(run_dir)


def _statistical_subject(
    use_case_id: str,
    subject_id: str,
) -> Tuple[Optional[Dict[str, Any]], Optional[Dict[str, Any]]]:
    """Resolve a run id or a persisted statistical variant id."""
    state = _read_state_for_subject(use_case_id, subject_id)
    if isinstance(state, dict):
        return {
            "id": subject_id,
            "kind": "run",
            "settings": state.get("statistical_settings") or {},
            "statistical_settings_hash": state.get("statistical_settings_hash"),
        }, None

    try:
        validate_safe_id(use_case_id, "use_case_id")
        validate_safe_id(subject_id, "subject_id")
        lane_dir = Path(safe_join(Config.OASIS_SIMULATION_DATA_DIR, use_case_id))
    except ValueError:
        return None, {"subject_id": subject_id, "reason": "invalid_id"}
    if not lane_dir.is_dir():
        return None, {"subject_id": subject_id, "reason": "not_found"}
    for state_path in lane_dir.glob("*/state.json"):
        candidate = _read_state_unsafe(state_path.parent)
        if not isinstance(candidate, dict):
            continue
        for event in candidate.get("statistical_variant_lineage") or []:
            if isinstance(event, dict) and event.get("variant_id") == subject_id:
                return {
                    "id": subject_id,
                    "kind": "statistical_variant",
                    "base_run_id": candidate.get("simulation_id") or state_path.parent.name,
                    "parent_settings": event.get("parent_settings") or {},
                    "parent_statistical_settings_hash": event.get(
                        "parent_statistical_settings_hash",
                    ),
                    "settings": event.get("settings") or {},
                    "statistical_settings_hash": event.get("statistical_settings_hash"),
                }, None
    return None, {"subject_id": subject_id, "reason": "not_found"}


@use_cases_bp.route(
    "/<use_case_id>/simulation/compare", methods=["POST"],
)
@_wrap_idempotent
def compare_statistical_simulations(body: Dict[str, Any], use_case_id: str):
    """Compare Workbench settings between two runs or variants."""
    return _compare_statistical_simulations(body, use_case_id)


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/statistical-config/compare",
    methods=["POST"],
)
@_wrap_idempotent
def compare_statistical_config_for_run(
    body: Dict[str, Any],
    use_case_id: str,
    sim_id: str,
):
    """Compare one run against another run or a persisted statistical variant."""
    body = dict(body)
    body.setdefault("base_run_id", sim_id)
    return _compare_statistical_simulations(body, use_case_id)


def _compare_statistical_simulations(body: Dict[str, Any], use_case_id: str):
    """Compare Workbench settings between two runs or variants."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    del adapter
    base_id = str(body.get("base_run_id") or "").strip()
    variant_id = str(body.get("variant_run_id") or "").strip()
    if not base_id or not variant_id:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "request body must include base_run_id and variant_run_id",
            400,
            {"use_case_id": use_case_id, "reason": "compare_ids_required"},
        )
    base, base_missing = _statistical_subject(use_case_id, base_id)
    variant, variant_missing = _statistical_subject(use_case_id, variant_id)
    missing = [
        item for item in (base_missing, variant_missing)
        if item is not None
    ]
    if base is None or variant is None:
        return _ok({
            "use_case_id": use_case_id,
            "base_run_id": base_id,
            "variant_run_id": variant_id,
            "statistical_diff": [],
            "findings_diff": {"present": [], "missing": missing, "corrupted": []},
            "statistical_settings_hash_pair": [
                base.get("statistical_settings_hash") if base else None,
                variant.get("statistical_settings_hash") if variant else None,
            ],
        })
    if (
        variant.get("kind") == "statistical_variant"
        and variant.get("base_run_id") == base_id
        and isinstance(variant.get("parent_settings"), dict)
    ):
        base = {
            **base,
            "settings": variant.get("parent_settings") or {},
            "statistical_settings_hash": variant.get(
                "parent_statistical_settings_hash",
            ) or base.get("statistical_settings_hash"),
        }
    diff = statistical_settings_diff_ops(
        base.get("settings"),
        variant.get("settings"),
    )
    return _ok({
        "use_case_id": use_case_id,
        "base_run_id": base_id,
        "variant_run_id": variant_id,
        "axes": body.get("axes") or ["statistical"],
        "statistical_diff": diff,
        "findings_diff": {
            "present": [base_id, variant_id],
            "missing": [],
            "corrupted": [],
        },
        "statistical_settings_hash_pair": [
            base.get("statistical_settings_hash"),
            variant.get("statistical_settings_hash"),
        ],
    })


def _coerce_positive_int(value: Any, default: int) -> int:
    try:
        return max(1, int(value))
    except Exception:  # noqa: BLE001
        return default


def _stakeholder_count_from_payload(body: Dict[str, Any]) -> int:
    if "stakeholders" in body:
        return _coerce_positive_int(body.get("stakeholders"), 1)
    scenario = body.get("scenario")
    if isinstance(scenario, dict):
        for key in ("audience_segments", "segments", "stakeholders"):
            value = scenario.get(key)
            if isinstance(value, list) and value:
                return len(value)
    return 1


def _statistical_preflight_snapshot(
    state: Dict[str, Any],
    config: StatisticalConfigPayload,
) -> Dict[str, Any]:
    """Return the compact Workbench preflight block for reseed responses."""

    context = build_statistical_runtime_context_from_config(config)
    overrides = context.runtime_overrides
    stakeholders = _stakeholder_count_from_payload({
        "scenario": state.get("scenario") or {},
    })
    rounds = overrides.rounds or _coerce_positive_int(
        state.get("rounds"),
        16,
    )
    ensemble_n = overrides.ensemble_n or _coerce_positive_int(
        state.get("ensemble_n"),
        5,
    )
    allow_expensive = (
        os.environ.get("POLICY_ALLOW_EXPENSIVE", "").strip().lower() == "true"
    )
    scale_ok, cap, scale_error = evaluate_scale_guard(
        ensemble_n=ensemble_n,
        stakeholders=stakeholders,
        rounds=rounds,
        allow_expensive_env=allow_expensive,
    )
    scale_product = ensemble_n * stakeholders * rounds
    token_estimate = scale_product * 150
    provider_config = provider_config_from_state(state.get("llm_provider"))
    provider_readiness = check_provider_readiness(provider_config, probe=False)
    return {
        "ensemble_n": ensemble_n,
        "stakeholders": stakeholders,
        "rounds": rounds,
        "cap_value": cap,
        "scale_guard": "ok" if scale_ok else "blocked",
        "scale_error": scale_error,
        "token_estimate": token_estimate,
        "llm_provider_mode": provider_config.mode,
        "llm_provider_readiness": provider_readiness.model_dump(mode="json"),
        "estimated_external_cost": estimate_external_cost(
            provider_config,
            token_estimate=token_estimate,
        ),
        "estimated_latency_ms": provider_readiness.latency_ms,
        "statistical_settings_hash": config.statistical_settings_hash,
    }


def _reject_inline_provider_secret(body: Dict[str, Any], use_case_id: str):
    provider_payload = body.get("provider")
    if not isinstance(provider_payload, dict):
        return None
    if "api_key" not in provider_payload:
        return None
    return _err(
        PlatformErrorCode.INVALID_INPUT,
        (
            "inline provider api_key is not supported; configure "
            "RAWFISH_LLM_API_KEY in the backend runtime for external providers"
        ),
        400,
        {
            "use_case_id": use_case_id,
            "reason": "inline_external_secret_unsupported",
        },
    )


def _source_context_from_payload(
    raw: Any,
    *,
    use_case_id: str,
):
    """Normalize cockpit source-mode intent without weakening scenario schemas."""

    if raw is None:
        return {}, None
    if not isinstance(raw, dict):
        return None, _err(
            PlatformErrorCode.INVALID_INPUT,
            "source_context must be an object",
            400,
            {"use_case_id": use_case_id, "reason": "source_context_invalid"},
        )
    mode = str(raw.get("mode") or "paste").strip().lower()
    if mode not in _SOURCE_MODES:
        return None, _err(
            PlatformErrorCode.INVALID_INPUT,
            f"source_context.mode must be one of {sorted(_SOURCE_MODES)!r}",
            400,
            {
                "use_case_id": use_case_id,
                "reason": "source_mode_invalid",
                "mode": mode,
            },
        )
    items: List[Dict[str, str]] = []
    for item in raw.get("items") or []:
        if not isinstance(item, dict):
            continue
        item_id = str(item.get("id") or "").strip()[:80]
        label = str(item.get("label") or "").strip()[:160]
        status = str(item.get("status") or "").strip()[:240]
        if item_id and label:
            items.append({"id": item_id, "label": label, "status": status})
    connectors: List[Dict[str, str]] = []
    for connector in raw.get("connectors") or []:
        if not isinstance(connector, dict):
            continue
        connector_id = str(connector.get("id") or "").strip()[:80]
        label = str(connector.get("label") or "").strip()[:160]
        state = str(connector.get("state") or "declared").strip()[:80]
        if connector_id and label:
            connectors.append({
                "id": connector_id,
                "label": label,
                "state": state,
            })
    normalized = {
        "mode": mode,
        "label": str(raw.get("label") or mode).strip()[:120],
        "items": items[:12],
        "connectors": connectors[:12],
    }
    parse_provenance_raw = raw.get("parse_provenance")
    if isinstance(parse_provenance_raw, dict):
        source = str(parse_provenance_raw.get("source") or "").strip()[:80]
        parser = str(parse_provenance_raw.get("parser") or "").strip()[:160]
        if source or parser:
            normalized["parse_provenance"] = {
                "source": source or "unknown",
                "parser": parser or "unknown",
            }
    return normalized, None


@use_cases_bp.route(
    "/<use_case_id>/evals/preflight_meter", methods=["POST"],
)
def preflight_meter(use_case_id: str):
    """Evaluate scale/token/provider readiness before launch."""
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    body = request.get_json(silent=True) or {}
    if not isinstance(body, dict):
        body = {}
    inline_secret_err = _reject_inline_provider_secret(body, use_case_id)
    if inline_secret_err is not None:
        return inline_secret_err
    source_context, source_err = _source_context_from_payload(
        body.get("source_context"),
        use_case_id=use_case_id,
    )
    if source_err is not None:
        return source_err
    catalog = adapter.catalog()
    cost_preflight = (
        catalog.lane_manifest.eval_instruments.get("cost_preflight", {})
        if catalog.lane_manifest.eval_instruments else {}
    )
    default_rounds = _coerce_positive_int(
        cost_preflight.get("default_rounds"), 16,
    )
    default_ensemble = _coerce_positive_int(
        cost_preflight.get("default_ensemble_n"), 5,
    )
    stakeholders = _stakeholder_count_from_payload(body)
    rounds = _coerce_positive_int(body.get("rounds"), default_rounds)
    ensemble_n = _coerce_positive_int(body.get("ensemble_n"), default_ensemble)
    allow_expensive = (
        os.environ.get("POLICY_ALLOW_EXPENSIVE", "").strip().lower() == "true"
    )
    scale_ok, cap, scale_error = evaluate_scale_guard(
        ensemble_n=ensemble_n,
        stakeholders=stakeholders,
        rounds=rounds,
        allow_expensive_env=allow_expensive,
    )
    scale_product = stakeholders * rounds * ensemble_n
    # Conservative cockpit estimate until per-lane token accounting lands.
    token_estimate = _coerce_positive_int(
        body.get("token_estimate"),
        scale_product * 150,
    )
    try:
        provider_config = provider_config_from_payload(body.get("provider"))
    except ValueError as exc:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            str(exc),
            400,
            {
                "use_case_id": use_case_id,
                "reason": "provider_config_invalid",
            },
        )
    readiness = check_provider_readiness(
        provider_config,
        probe=bool(body.get("probe_provider")),
    )
    estimated_external_cost = estimate_external_cost(
        provider_config,
        token_estimate=token_estimate,
    )
    external_budget = cost_preflight.get("external_budget")
    warn_at = (
        external_budget.get("warn_at")
        if isinstance(external_budget, dict)
        else None
    )
    external_budget_status = provider_budget_state(
        estimated_external_cost,
        warn_at=warn_at,
    )
    payload = PreflightMeterPayload(
        scale_product=scale_product,
        scale_cap=cap,
        scale_ok=scale_ok,
        scale_error=scale_error,
        token_estimate=token_estimate,
        provider=provider_config.public_dict(),
        provider_readiness=readiness,
        estimated_latency_ms=readiness.latency_ms,
        estimated_external_cost=estimated_external_cost,
        external_budget_status=external_budget_status.model_dump(mode="json"),
    )
    response_payload = payload.model_dump(mode="json")
    if source_context:
        response_payload["source_context"] = source_context
    return _ok(response_payload)


@use_cases_bp.route(
    "/<use_case_id>/simulation/create", methods=["POST"],
)
@_wrap_idempotent
def create_simulation(body: Dict[str, Any], use_case_id: str):
    """Create a fresh simulation row for ``use_case_id``.

    Body: ``{"scenario": {...}}`` -- the adapter validates the
    scenario via :meth:`SimulationUseCase.validate_scenario`. On
    success returns ``{"simulation_id": ..., "use_case_id": ...,
    "phase": "created"}``.

    Idempotency-Key supported: a same-key replay returns the
    cached response (same simulation_id) without re-running
    the validation or re-minting a row.
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    scenario_dict = body.get("scenario")
    if not isinstance(scenario_dict, dict):
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "request body must include a `scenario` object",
            400,
            {"use_case_id": use_case_id},
        )
    try:
        scenario = adapter.validate_scenario(scenario_dict)
    except Exception as exc:  # noqa: BLE001 -- adapter chose its own error class
        return _err(
            PlatformErrorCode.SCENARIO_INVALID,
            f"scenario validation failed: {type(exc).__name__}: {exc}",
            400,
            {"use_case_id": use_case_id},
        )
    inline_secret_err = _reject_inline_provider_secret(body, use_case_id)
    if inline_secret_err is not None:
        return inline_secret_err
    source_context, source_err = _source_context_from_payload(
        body.get("source_context"),
        use_case_id=use_case_id,
    )
    if source_err is not None:
        return source_err
    try:
        provider_config = provider_config_from_payload(body.get("provider"))
    except ValueError as exc:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            str(exc),
            400,
            {
                "use_case_id": use_case_id,
                "reason": "provider_config_invalid",
            },
        )
    readiness = check_provider_readiness(provider_config, probe=False)
    if not readiness.ready:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            readiness.reason or readiness.status,
            400,
            {
                "use_case_id": use_case_id,
                "reason": "provider_not_ready",
                "provider_status": readiness.status,
            },
        )
    statistical_seed_state: Dict[str, Any] = {}
    create_settings = _create_body_statistical_settings(body)
    if create_settings is not None:
        statistical_seed_state["statistical_settings"] = create_settings
    statistical_config, statistical_err = _resolve_statistical_config_or_err(
        use_case_id,
        adapter,
        statistical_seed_state,
        required=False,
        invalid_status=400,
        invalid_code=PlatformErrorCode.INVALID_INPUT,
        invalid_reason="statistical_settings_invalid",
    )
    if statistical_err is not None:
        return statistical_err

    simulation_id = _mint_simulation_id(use_case_id)
    run_dir = _run_dir_for(use_case_id, simulation_id)
    # Persist the CANONICAL form of the scenario when the adapter
    # returns a Pydantic model from ``validate_scenario`` -- this
    # ensures that semantically-identical request bodies (e.g. ones
    # using extra-tolerant aliases or differing key orders) collapse
    # to the same on-disk shape, so the deterministic
    # ``_build_run_metadata`` scenario_hash is computed over the
    # canonical payload rather than the raw request body. Adapters
    # that return a plain dict from ``validate_scenario`` (no
    # ``model_dump``) keep the raw-dict round-trip.
    if hasattr(scenario, "model_dump"):
        scenario_persisted = scenario.model_dump(mode="json")
    else:
        scenario_persisted = scenario_dict
    state = {
        "simulation_id": simulation_id,
        "use_case_id": use_case_id,
        "phase": "created",
        "created_at": _utcnow(),
        # Persist the canonical scenario payload; the adapter's typed
        # ``scenario`` is in-memory only because lane-specific
        # Scenario shapes have lane-specific JSON encoders.
        "scenario": scenario_persisted,
        "llm_provider": provider_config.public_dict(),
        "preflight_meter": body.get("preflight_meter"),
        "source_context": source_context,
    }
    if statistical_config is not None and create_settings is not None:
        cohort_err = _validate_statistical_settings_for_run_cohorts(
            settings=create_settings,
            state=state,
            use_case_id=use_case_id,
            sim_id=simulation_id,
        )
        if cohort_err is not None:
            return cohort_err
    os.makedirs(run_dir, exist_ok=True)
    if statistical_config is not None:
        _apply_statistical_config_to_state(state, statistical_config)
        _persist_statistical_prepare_artifacts(
            run_dir=run_dir,
            config=statistical_config,
            manifest={},
        )
    atomic_write_json(str(run_dir / "state.json"), state)
    return _ok({
        "simulation_id": simulation_id,
        "use_case_id": use_case_id,
        "phase": "created",
        "llm_provider": provider_config.public_dict(),
    }, status=201)


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/prepare", methods=["POST"],
)
@_wrap_idempotent
def prepare_simulation(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Run the adapter's prepare phase: ontology build + artifact writes."""
    del body  # prepare takes no body; the idempotency seam still runs.
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    #: Per-simulation start lock: ``/prepare`` and ``/start`` MUST
    #: serialise. Without the lock here, a concurrent ``/start`` can
    #: transition the lifecycle to ``starting`` / ``running`` between
    #: this route's read of ``state.json`` and its eventual write of
    #: ``phase="prepared"``, rewinding a live run back to ``prepared``.
    #: The lock is the same primitive ``/start`` already uses.
    try:
        run_dir.mkdir(parents=True, exist_ok=True)
        with _start_lock(str(run_dir), sim_id):
            return _prepare_simulation_locked(
                adapter=adapter,
                use_case_id=use_case_id,
                sim_id=sim_id,
                run_dir=run_dir,
            )
    except _StartLockBusy:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"a /start is in flight for simulation {sim_id!r}; "
            "cannot re-prepare",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "prepare_blocked_by_start_in_progress",
            },
        )


def _prepare_simulation_locked(
    *,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    """Per-simulation-locked body of generic /prepare.

    Extracted so the ``start_lock`` wraps the FULL read-check-write
    sequence (state read + regression guard + artifact writes +
    transition to ``prepared``). Returns the same Flask tuple shape
    as the calling route.
    """
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None  # narrowed by state_err-guard above
    #: Lifecycle regression guard: /prepare against an in-flight run
    #: (``starting`` / ``running``) would clobber artifacts the runner
    #: is mid-write of and reset the lifecycle phase under the
    #: runner's feet. Reject with 409 so the operator must wait /
    #: explicitly cancel before re-preparing.
    current_phase = state.get("phase")
    #: Lifecycle reconciliation: the runner subprocess writes terminal
    #: markers into ``run_state.json`` (flat or namespaced) without
    #: ever touching ``state.json``, so a finished subprocess-driven
    #: run can look like ``running`` on disk but is in fact terminal.
    #: Reconcile here so the regression guard below sees the EFFECTIVE
    #: lifecycle, not the pre-reconciliation snapshot. Without this an
    #: operator who saw ``/status`` flip to ``completed`` would still
    #: be blocked from ``/prepare`` by an unreconciled ``running``
    #: state.
    if current_phase in {"starting", "running"}:
        effective_phase, _runner_err = _reconcile_effective_phase(
            run_dir, sim_id, state,
        )
        if effective_phase != current_phase:
            current_phase = effective_phase
    if current_phase in {"starting", "running"}:
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"simulation phase {current_phase!r} cannot be re-prepared "
            "while a run is in flight",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "prepare_blocked_by_in_flight_run",
                "current_phase": current_phase,
            },
        )
    #: Terminal-phase re-prepare: ``completed`` / ``failed`` /
    #: ``reported`` runs CAN be re-prepared (operator's intentional
    #: re-run), but the prior run's downstream artifacts must be
    #: cleaned so a stale ``report.json`` does not remain readable
    #: after the lifecycle rewinds to ``prepared``. Stale report
    #: + ``state.report_path`` would make the read route surface the
    #: prior run's output as if it belonged to the freshly-prepared
    #: lifecycle. Best-effort unlink: a missing file is fine
    #: (the artifact was never written), an OSError is logged but
    #: does not block the re-prepare.
    if current_phase in {"completed", "failed", "reported"}:
        artifact_names = adapter.artifact_names() if hasattr(
            adapter, "artifact_names",
        ) else {}
        stale_candidates = []
        for key in ("report_json", "report_md"):
            name = artifact_names.get(key) if isinstance(
                artifact_names, dict,
            ) else None
            if isinstance(name, str) and name and "/" not in name and (
                name not in {".", ".."}
            ):
                stale_candidates.append(run_dir / name)
        for stale_path in stale_candidates:
            try:
                if stale_path.exists():
                    stale_path.unlink()
            except OSError as exc:  # noqa: BLE001
                logger.warning(
                    "generic /prepare: could not unlink stale artifact "
                    "%s before re-prepare: %s", stale_path, exc,
                )
        for stale_key in (
            "report_path", "report_sha256",
            "report_md_path", "report_md_sha256",
            "completed_at", "failed_at",
            "reported_at", "error",
        ):
            state.pop(stale_key, None)
    statistical_config, statistical_err = _resolve_statistical_config_or_err(
        use_case_id,
        adapter,
        state,
        required=False,
    )
    if statistical_err is not None:
        return statistical_err
    if statistical_config is not None:
        _apply_statistical_config_to_state(state, statistical_config)
        atomic_write_json(str(run_dir / "state.json"), state)
    try:
        scenario = adapter.validate_scenario(state.get("scenario") or {})
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.SCENARIO_INVALID,
            f"persisted scenario re-validation failed: {type(exc).__name__}",
            500,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    try:
        adapter.build_ontology(scenario, run_dir)
    except Exception as exc:  # noqa: BLE001
        audience_store_err = _audience_store_prepare_error(
            exc,
            use_case_id=use_case_id,
            simulation_id=sim_id,
        )
        if audience_store_err is not None:
            return audience_store_err
        return _err(
            PlatformErrorCode.ADAPTER_PREPARE_FAILED,
            f"build_ontology raised {type(exc).__name__}: {exc}",
            502,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    try:
        manifest = adapter.write_prepare_artifacts(scenario, run_dir)
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_PREPARE_FAILED,
            f"write_prepare_artifacts raised {type(exc).__name__}: {exc}",
            502,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    if statistical_config is not None:
        try:
            manifest = _persist_statistical_prepare_artifacts(
                run_dir=run_dir,
                config=statistical_config,
                manifest=manifest,
            )
        except Exception as exc:  # noqa: BLE001
            return _err(
                PlatformErrorCode.ADAPTER_PREPARE_FAILED,
                f"statistical prepare artifact write raised {type(exc).__name__}: {exc}",
                502,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "statistical_prepare_artifact_failed",
                },
            )

    # Manifest-schema gate: when the adapter declares
    # ``prepare_manifest_schema`` (a Pydantic model class), validate
    # the returned manifest against it BEFORE the state.json
    # transition lands. A schema-drifted manifest surfaces as
    # ``REPORT_CORRUPTED`` 500 with a discriminator reason rather
    # than silently advancing the lifecycle on a malformed payload.
    # Adapters that set the field to ``None`` (no canonical schema
    # yet) skip this gate honestly.
    manifest_schema = getattr(adapter, "prepare_manifest_schema", None)
    if manifest_schema is not None and hasattr(
        manifest_schema, "model_validate",
    ):
        try:
            # Two acceptable manifest shapes: a Pydantic model
            # instance (validate via re-dump+re-validate) or a
            # plain dict / dict-like (validate directly). Both
            # paths share the same failure mode.
            if hasattr(manifest, "model_dump"):
                manifest_schema.model_validate(
                    manifest.model_dump(mode="python"),
                )
            else:
                manifest_schema.model_validate(manifest)
        except Exception as exc:  # noqa: BLE001
            return _err(
                ErrorCode.REPORT_CORRUPTED,
                "adapter.write_prepare_artifacts payload failed "
                f"adapter.prepare_manifest_schema: {type(exc).__name__}",
                500,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "prepare_manifest_schema_invalid",
                },
            )

    _set_lifecycle_phase(state, "prepared")
    state["prepared_at"] = _utcnow()
    if statistical_config is not None:
        state["prepared_statistical_settings_hash"] = (
            statistical_config.statistical_settings_hash
        )
        state["statistical_settings_artifact"] = "statistical_settings.json"
    try:
        _persist_run_metadata_if_missing(
            run_dir=run_dir,
            state=state,
            manifest=manifest,
        )
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.STATE_CORRUPTED,
            f"run_metadata.json creation failed: {type(exc).__name__}: {exc}",
            500,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "run_metadata_create_failed",
            },
        )
    atomic_write_json(str(run_dir / "state.json"), state)
    return _ok({
        "simulation_id": sim_id,
        "use_case_id": use_case_id,
        "phase": "prepared",
        "manifest": (
            manifest.model_dump(mode="json")
            if hasattr(manifest, "model_dump") else manifest
        ),
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/start", methods=["POST"],
)
@_wrap_idempotent
def start_simulation(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Start the run.

    The :class:`SimulationUseCase` Protocol declares
    ``run_simulation(scenario, run_dir) -> None``; this route
    invokes it. Adapters without a runnable start implementation raise
    :class:`NotImplementedError` from ``run_simulation`` so the
    generic dispatch surface returns a structured ``501
    CAPABILITY_UNSUPPORTED`` envelope -- generic dispatch never
    transitions a run to ``completed`` without a real adapter-owned
    runner step.
    """
    del body  # start takes no body; the idempotency seam still runs.
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    # Per-simulation lock guarding the ENTIRE read/check/run/write
    # block. Two concurrent /start POSTs against the same simulation
    # would otherwise both pass the phase check and both call
    # ``adapter.run_simulation`` -- which can clobber run_state.json,
    # log files, and downstream artifacts. The lock is non-blocking:
    # a loser request gets 409 ``start_in_progress`` immediately so
    # the operator sees a meaningful retry signal.
    try:
        run_dir.mkdir(parents=True, exist_ok=True)
        with _start_lock(str(run_dir), sim_id):
            return _start_simulation_locked(
                adapter=adapter,
                use_case_id=use_case_id,
                sim_id=sim_id,
                run_dir=run_dir,
            )
    except _StartLockBusy:
        return _err(
            ErrorCode.INVALID_REQUEST,
            f"a /start is already in flight for simulation {sim_id!r}",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "start_in_progress",
            },
        )


def _start_simulation_locked(
    *,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    """Per-simulation-locked body of the generic /start route.

    Extracted so the lock context manager wraps the full
    read/check/run/write sequence cleanly. Returns the same Flask
    tuple shape as the calling route.
    """
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None  # narrowed by state_err-guard above
    #: /start accepts ONLY ``prepared``. A ``completed`` sim that needs
    #: to be re-run MUST be re-/prepare'd first so prior artifacts are
    #: cleaned and the lifecycle re-enters ``prepared`` cleanly --
    #: starting a ``completed`` sim in place would mix prior outputs
    #: with the new run's writes. Other phases (``created`` /
    #: ``starting`` / ``running`` / ``failed`` / ``reported``) are
    #: invalid sources for /start.
    if state.get("phase") != "prepared":
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"simulation phase {state.get('phase')!r} cannot transition to running",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "start_requires_prepared_phase",
                "current_phase": state.get("phase"),
            },
        )
    statistical_config, statistical_err = _resolve_statistical_config_or_err(
        use_case_id,
        adapter,
        state,
        required=False,
    )
    if statistical_err is not None:
        return statistical_err
    if statistical_config is not None:
        _apply_statistical_config_to_state(state, statistical_config)
        prepared_hash = state.get("prepared_statistical_settings_hash")
        current_hash = statistical_config.statistical_settings_hash
        if prepared_hash != current_hash:
            return _err(
                PlatformErrorCode.INVALID_STATE,
                "statistical settings changed after prepare; re-run prepare before start",
                409,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "statistical_settings_changed_after_prepare",
                    "prepared_statistical_settings_hash": prepared_hash,
                    "statistical_settings_hash": current_hash,
                },
            )
        atomic_write_json(str(run_dir / "state.json"), state)
    # ``run_simulation`` is part of the SimulationUseCase Protocol.
    # The Protocol's ``@runtime_checkable`` structural check accepts an
    # adapter only when the method is present; lanes with no runnable
    # implementation raise NotImplementedError from the body to opt out
    # (mapped to 501 below).
    try:
        scenario = adapter.validate_scenario(state.get("scenario") or {})
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.SCENARIO_INVALID,
            f"persisted scenario re-validation failed: {type(exc).__name__}",
            500,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    # Durable ``starting`` transition BEFORE the adapter call so a
    # crash mid-run / late status poll observes the in-flight state.
    # On adapter failure (Exception, not NotImplementedError -- the
    # opt-out path is informational only and does not change state),
    # the state advances to ``failed`` with structured error details.
    _set_lifecycle_phase(state, "starting")
    state["started_at"] = _utcnow()
    state.pop("error", None)
    atomic_write_json(str(run_dir / "state.json"), state)
    try:
        terminal_hint = invoke_lane_run_simulation(adapter, scenario, run_dir)
    except NotImplementedError as nie:
        # Opt-out is NOT a runtime failure -- the adapter declared the
        # capability is not available via generic dispatch. Restore
        # ``prepared`` so a re-attempt against the lane's correct
        # surface still works.
        _set_lifecycle_phase(state, "prepared")
        state.pop("started_at", None)
        atomic_write_json(str(run_dir / "state.json"), state)
        return _err(
            PlatformErrorCode.CAPABILITY_UNSUPPORTED,
            f"adapter {use_case_id!r} opted out of generic run_simulation dispatch",
            501,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "capability_unsupported",
                "capability": "run_simulation",
                "message": str(nie),
            },
        )
    except _PlatformScaleGuardRefused as guard_exc:
        # Scale-guard refusal is a 400 (caller error -- the resolved
        # product exceeded the active cap), NOT a 502 runner failure.
        # The generic dispatch surface emits the adapter-preserved
        # ``message`` and ``details`` payload. The adapter is responsible
        # for re-raising its lane-specific wrapper as the lane-agnostic
        # :class:`PlatformScaleGuardRefused` so this seam does not need
        # to know about per-lane exception types.
        # Restore phase so a re-issued /start with a smaller scale
        # works. State on disk was last set to ``starting``; revert.
        _set_lifecycle_phase(state, "prepared")
        state.pop("started_at", None)
        atomic_write_json(str(run_dir / "state.json"), state)
        return _err(
            ErrorCode.SCALE_GUARD_EXCEEDED,
            guard_exc.message,
            400,
            guard_exc.details,
        )
    except Exception as exc:  # noqa: BLE001
        # Durable failure: persist ``failed`` + error details so
        # ``/status`` can surface the diagnostic without a re-call.
        _set_lifecycle_phase(state, "failed")
        state["failed_at"] = _utcnow()
        state["error"] = {
            "code": "RUNNER_START_FAILED",
            "kind": type(exc).__name__,
            "message": str(exc),
        }
        atomic_write_json(str(run_dir / "state.json"), state)
        return _err(
            ErrorCode.RUNNER_START_FAILED,
            f"run_simulation raised {type(exc).__name__}: {exc}",
            502,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "runner_start_failed",
                "kind": type(exc).__name__,
            },
        )
    # State-authority dispatch:
    #   * ``terminal_hint is None`` -- the adapter did NOT write
    #     ``state.json`` on its own (creator deterministic-mock path).
    #     The route OWNS the post-handoff ``completed`` transition.
    #   * ``terminal_hint`` is a string -- the adapter (or its
    #     delegated service, e.g. :class:`PolicyRunnerService`) wrote
    #     authoritative state. The route mirrors the value into the
    #     dispatch ``phase`` field instead of lying with
    #     ``"completed"``. The on-disk state is re-read so the
    #     dispatch-owned ``state["phase"]`` lines up with the service-
    #     owned ``state["status"]`` (watcher and dispatch readers
    #     otherwise observe drift).
    if terminal_hint is None:
        _set_lifecycle_phase(state, "completed")
        state["completed_at"] = _utcnow()
        atomic_write_json(str(run_dir / "state.json"), state)
        response_phase = "completed"
    else:
        # The service wrote state["status"] = terminal_hint at the
        # namespaced state.json. Re-load the on-disk dict so the
        # phase mirror lands on the fresh state (the in-memory
        # ``state`` here is the route's pre-call snapshot and would
        # clobber the service's writes if used as the base for the
        # write-back).
        disk_state = _read_state_unsafe(run_dir) or state
        _set_lifecycle_phase(disk_state, terminal_hint)
        atomic_write_json(str(run_dir / "state.json"), disk_state)
        response_phase = terminal_hint
    return _ok({
        "simulation_id": sim_id,
        "use_case_id": use_case_id,
        "phase": response_phase,
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/status", methods=["GET"],
)
def get_status(use_case_id: str, sim_id: str):
    """Return ``{phase, warnings, errors, use_case_id, simulation_id}``.

    Two persistence surfaces are reconciled:

      * The namespaced ``state.json`` written by the generic dispatch
        + lane adapters owns the pre-spawn lifecycle markers
        (``created`` -> ``prepared`` -> ``starting`` -> ``running``).
      * ``run_state.json`` written by an out-of-process runner
        subprocess owns the post-spawn terminal markers
        (``completed`` / ``failed``). The runner never writes back to
        ``state.json``, so without this reconciliation a finished
        subprocess-driven run would remain externally ``running``.

    Probe order: the namespaced ``run_dir`` first, then the protected
    runner's flat directory (``SimulationRunner.RUN_STATE_DIR/<sim_id>/``)
    where production policy subprocesses write. Either path may carry
    the terminal marker. The probe is lane-agnostic: lanes whose
    ``run_simulation`` writes terminal status into ``state.json``
    itself (creator's in-process runner) see no ``run_state.json``
    on disk and the reconciliation is a no-op for them.
    """
    _adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None  # narrowed by state_err-guard above

    effective_phase, effective_error = _reconcile_effective_phase(
        run_dir, sim_id, state,
    )

    errors_list = list(state.get("errors", []) or [])
    if effective_error and effective_error not in errors_list:
        errors_list.append(effective_error)
    # Surface the structured ``state["error"]`` dict from the generic
    # /start failure handler (``RUNNER_START_FAILED`` + ``kind`` +
    # ``message``) as a single line so a polled /status carries the
    # diagnostic without needing to fish state.json off disk.
    structured_error = state.get("error")
    if isinstance(structured_error, dict):
        msg = structured_error.get("message")
        code = structured_error.get("code")
        if msg and code:
            line = f"{code}: {msg}"
            if line not in errors_list:
                errors_list.append(line)
        elif msg and msg not in errors_list:
            errors_list.append(msg)

    return _ok({
        "simulation_id": sim_id,
        "use_case_id": use_case_id,
        "phase": effective_phase,
        "warnings": state.get("warnings", []),
        "errors": errors_list,
    })


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/graph", methods=["GET"],
)
def get_run_graph(use_case_id: str, sim_id: str):
    """Return a lane-generic graph payload for the cockpit graph pane."""

    _adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None

    for key in (
        "graph_data",
        "runtime_graph",
        "knowledge_graph",
        "artifact_graph",
    ):
        candidate = state.get(key)
        if isinstance(candidate, dict) and isinstance(candidate.get("nodes"), list):
            return _ok({
                "simulation_id": sim_id,
                "use_case_id": use_case_id,
                "graph_data": candidate,
                "source": f"state.{key}",
            })

    scenario_raw = state.get("scenario")
    scenario: Dict[str, Any] = scenario_raw if isinstance(scenario_raw, dict) else {}
    stakeholders = scenario.get("stakeholders")
    if not isinstance(stakeholders, list) or not stakeholders:
        stakeholders = [{
            "segment_id": "cohort_1",
            "name": "Run cohort",
            "question": scenario.get("stress_question") or "",
        }]
    root_id = str(state.get("simulation_id") or sim_id)
    source_context_raw = state.get("source_context")
    source_context: Dict[str, Any] = (
        source_context_raw if isinstance(source_context_raw, dict) else {}
    )
    nodes: List[Dict[str, Any]] = [{
        "id": root_id,
        "label": scenario.get("title") or root_id,
        "type": "run",
        "attributes": {
            "lane": use_case_id,
            "phase": state.get("phase"),
            "source_mode": source_context.get("mode") or "paste",
            "statistical_settings_hash": state.get("statistical_settings_hash"),
        },
    }]
    edges: List[Dict[str, Any]] = []
    for index, stakeholder in enumerate(stakeholders):
        if not isinstance(stakeholder, dict):
            continue
        cohort_id = str(
            stakeholder.get("segment_id")
            or stakeholder.get("id")
            or f"cohort_{index + 1}"
        )
        node_id = f"{root_id}:{cohort_id}"
        nodes.append({
            "id": node_id,
            "label": stakeholder.get("name") or stakeholder.get("label") or cohort_id,
            "type": stakeholder.get("type") or "cohort",
            "attributes": {
                "question": (
                    stakeholder.get("question")
                    or stakeholder.get("cohort_question")
                    or scenario.get("stress_question")
                    or ""
                ),
            },
        })
        edges.append({
            "id": f"{root_id}:{cohort_id}:edge",
            "source": root_id,
            "target": node_id,
            "label": "TESTS_AGAINST",
        })
    return _ok({
        "simulation_id": sim_id,
        "use_case_id": use_case_id,
        "graph_data": {"nodes": nodes, "edges": edges},
        "source": "state.scenario",
        "source_context": source_context,
    })


def _reconcile_effective_phase(
    run_dir: Path, sim_id: str, state: Dict[str, Any],
) -> Tuple[str, Optional[str]]:
    """Return ``(effective_phase, runner_error)`` reconciling
    ``state.json`` with ``run_state.json``.

    Two persistence surfaces:

      * Namespaced ``state.json`` -- pre-spawn lifecycle markers
        (``created`` / ``prepared`` / ``starting`` / ``running``).
      * ``run_state.json`` -- the runner subprocess's terminal
        markers (``completed`` / ``failed``). The runner never
        writes back to ``state.json``; without this reconciliation
        a finished subprocess-driven run would remain externally
        ``running``.

    Probe order: the namespaced ``run_dir`` first, then the
    protected runner's flat directory
    (``SimulationRunner.RUN_STATE_DIR/<sim_id>/``) where production
    policy subprocesses write. Either path may carry the terminal
    marker. Lanes whose ``run_simulation`` writes terminal status
    into ``state.json`` itself (creator's in-process runner) see no
    ``run_state.json`` on disk and the reconciliation is a no-op
    for them.

    Shared by ``/status``, ``/report/generate`` (so a completed
    subprocess run is reportable through the generic dispatch), and
    the auto-report watcher (so the same completed run auto-emits).
    """
    from ..simulation_platform.runner_adapter import RunnerAdapter
    effective_phase = state.get("phase", "unknown")
    effective_error: Optional[str] = None

    candidate_dirs: list[str] = [str(run_dir)]
    try:
        from ..services.simulation_runner import SimulationRunner
        flat_dir = os.path.join(
            SimulationRunner.RUN_STATE_DIR, sim_id,
        )
        if flat_dir not in candidate_dirs:
            candidate_dirs.append(flat_dir)
    except Exception:  # noqa: BLE001
        pass

    for probe_dir in candidate_dirs:
        try:
            run_state = RunnerAdapter.read_run_state(probe_dir)
        except (OSError, json.JSONDecodeError) as exc:
            logger.warning(
                "run_state.json unreadable for %s under %r: %s; "
                "continuing with the next probe path.",
                sim_id, probe_dir, exc,
            )
            run_state = None
        if run_state is None:
            continue
        runner_status = (run_state.get("runner_status") or "").lower()
        if runner_status in ("completed", "failed"):
            effective_phase = runner_status
            if runner_status == "failed":
                effective_error = run_state.get("error") or None
            break

    return effective_phase, effective_error


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/report/generate", methods=["POST"],
)
@_wrap_idempotent
def generate_report(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Adapter ``generate_report`` + persist via ``artifact_names``.

    Wrapped in the per-simulation :func:`start_lock` so the
    state-check / adapter call / artifact write / state transition
    sequence cannot be interleaved by a concurrent manual report or
    auto-report tick against the same simulation. Without this lock,
    two writers would race on ``state.json`` + ``report_path`` and
    last-writer-wins the canonical artifact (and audit metadata).
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    if body.get("async") is True or body.get("mode") == "async":
        return _enqueue_report_job(
            adapter=adapter,
            use_case_id=use_case_id,
            sim_id=sim_id,
            run_dir=run_dir,
        )
    return _generate_report_sync(
        adapter=adapter,
        use_case_id=use_case_id,
        sim_id=sim_id,
        run_dir=run_dir,
    )


def _generate_report_sync(
    *,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    try:
        run_dir.mkdir(parents=True, exist_ok=True)
        with _start_lock(str(run_dir), sim_id):
            return _generate_report_locked(
                adapter=adapter,
                use_case_id=use_case_id,
                sim_id=sim_id,
                run_dir=run_dir,
            )
    except _StartLockBusy:
        return _err(
            ErrorCode.INVALID_REQUEST,
            f"a report-generate is already in flight for simulation {sim_id!r}",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "report_generate_in_progress",
            },
        )


def _report_job_id(use_case_id: str, sim_id: str) -> str:
    seed = f"{use_case_id}:{sim_id}:{_utcnow()}"
    return hashlib.sha256(seed.encode("utf-8")).hexdigest()[:16]


def _job_response_payload(response: Any) -> Tuple[Dict[str, Any], int]:
    try:
        payload_obj, status = response
    except (TypeError, ValueError):
        payload_obj, status = response, 200
    try:
        payload = (
            payload_obj.get_json()
            if hasattr(payload_obj, "get_json")
            else payload_obj
        )
    except Exception:  # noqa: BLE001
        payload = None
    if not isinstance(payload, dict):
        payload = {"raw": str(payload)}
    return payload, int(status or 200)


def _report_job_path(run_dir: Path) -> Path:
    return run_dir / _REPORT_JOB_FILENAME


def _persist_report_job(run_dir: Path, job: Dict[str, Any]) -> None:
    atomic_write_json(str(_report_job_path(run_dir)), job)


def _load_report_job(run_dir: Path, job_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
    try:
        with open(_report_job_path(run_dir), "r", encoding="utf-8") as fh:
            payload = json.load(fh)
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(payload, dict):
        return None
    if job_id is not None and payload.get("job_id") != job_id:
        return None
    return dict(payload)


def _set_report_job(
    job_id: str,
    updates: Dict[str, Any],
    *,
    run_dir: Optional[Path] = None,
) -> Dict[str, Any]:
    with _REPORT_JOBS_LOCK:
        job = dict(_REPORT_JOBS.get(job_id) or {})
        job.update(updates)
        _REPORT_JOBS[job_id] = job
        snapshot = dict(job)
    if run_dir is not None:
        _persist_report_job(run_dir, snapshot)
    return snapshot


def _find_active_report_job(
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
) -> Optional[Dict[str, Any]]:
    with _REPORT_JOBS_LOCK:
        for job in _REPORT_JOBS.values():
            if (
                job.get("use_case_id") == use_case_id
                and job.get("simulation_id") == sim_id
                and job.get("status") in {"queued", "running"}
            ):
                return dict(job)
    persisted = _load_report_job(run_dir)
    if not persisted or persisted.get("status") not in {"queued", "running"}:
        return None
    job_id = str(persisted.get("job_id") or "")
    with _REPORT_JOBS_LOCK:
        future = _REPORT_JOB_FUTURES.get(job_id)
        if future is not None and not future.done():
            _REPORT_JOBS[job_id] = persisted
            return dict(persisted)
    _set_report_job(
        job_id,
        {
            **persisted,
            "status": "failed",
            "finished_at": _utcnow(),
            "reason": "worker_not_available",
            "message": (
                "report job was queued/running but no worker owns it in this "
                "process; enqueue a new report job"
            ),
        },
        run_dir=run_dir,
    )
    return None


def _run_report_job(
    *,
    app,
    job_id: str,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
) -> None:
    try:
        with app.app_context():
            _set_report_job(
                job_id,
                {
                    "status": "running",
                    "started_at": _utcnow(),
                },
                run_dir=run_dir,
            )
            response = _generate_report_sync(
                adapter=adapter,
                use_case_id=use_case_id,
                sim_id=sim_id,
                run_dir=run_dir,
            )
            payload, status_code = _job_response_payload(response)
            success = 200 <= status_code < 300
            _set_report_job(
                job_id,
                {
                    "status": "succeeded" if success else "failed",
                    "finished_at": _utcnow(),
                    "status_code": status_code,
                    "response": payload,
                },
                run_dir=run_dir,
            )
    except Exception as exc:  # noqa: BLE001
        _set_report_job(job_id, {
            "status": "failed",
            "finished_at": _utcnow(),
            "reason": "report_job_worker_failed",
            "message": f"{type(exc).__name__}: {exc}",
        }, run_dir=run_dir)
    finally:
        with _REPORT_JOBS_LOCK:
            _REPORT_JOB_FUTURES.pop(job_id, None)


def _enqueue_report_job(
    *,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    run_dir.mkdir(parents=True, exist_ok=True)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None
    effective_phase, _runner_err = _reconcile_effective_phase(run_dir, sim_id, state)
    if effective_phase != "completed":
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"simulation phase {effective_phase!r} is not 'completed'; "
            "cannot generate report",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "current_phase": effective_phase,
            },
        )
    active = _find_active_report_job(use_case_id, sim_id, run_dir)
    if active is not None:
        return _ok(active, status=202)
    job_id = _report_job_id(use_case_id, sim_id)
    app = cast(Any, current_app)._get_current_object()
    job = _set_report_job(
        job_id,
        {
            "job_id": job_id,
            "use_case_id": use_case_id,
            "simulation_id": sim_id,
            "status": "queued",
            "created_at": _utcnow(),
        },
        run_dir=run_dir,
    )
    try:
        future = _REPORT_EXECUTOR.submit(
            _run_report_job,
            app=app,
            job_id=job_id,
            adapter=adapter,
            use_case_id=use_case_id,
            sim_id=sim_id,
            run_dir=run_dir,
        )
    except Exception as exc:  # noqa: BLE001
        failed = _set_report_job(
            job_id,
            {
                "status": "failed",
                "finished_at": _utcnow(),
                "reason": "report_job_submit_failed",
                "message": f"{type(exc).__name__}: {exc}",
            },
            run_dir=run_dir,
        )
        return _err(
            PlatformErrorCode.ADAPTER_REPORT_FAILED,
            "report job could not be queued",
            503,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "job_id": job_id,
                "reason": "report_job_submit_failed",
                "job": failed,
            },
        )
    with _REPORT_JOBS_LOCK:
        _REPORT_JOB_FUTURES[job_id] = future
    return _ok(job, status=202)


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/report/jobs/<job_id>",
    methods=["GET"],
)
def get_report_job(use_case_id: str, sim_id: str, job_id: str):
    """Return in-process status for an async report generation job."""

    _adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    try:
        validate_safe_id(job_id, "job_id")
    except ValueError as exc:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            str(exc),
            400,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    run_dir = _run_dir_for(use_case_id, sim_id)
    with _REPORT_JOBS_LOCK:
        job = dict(_REPORT_JOBS.get(job_id) or {})
    if not job:
        job = _load_report_job(run_dir, job_id) or {}
    if job and job.get("status") in {"queued", "running"}:
        with _REPORT_JOBS_LOCK:
            future = _REPORT_JOB_FUTURES.get(job_id)
        if future is None:
            job = _set_report_job(
                job_id,
                {
                    **job,
                    "status": "failed",
                    "finished_at": _utcnow(),
                    "reason": "worker_not_available",
                    "message": (
                        "report job status was recovered from disk, but no "
                        "active worker owns it in this process"
                    ),
                },
                run_dir=run_dir,
            )
    if not job or job.get("use_case_id") != use_case_id or job.get("simulation_id") != sim_id:
        return _err(
            ErrorCode.SIMULATION_NOT_FOUND,
            f"report job {job_id!r} not found",
            404,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "job_id": job_id,
            },
        )
    return _ok(job)


def _generate_report_locked(
    *,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
):
    """Per-simulation-locked body of generic /report/generate.

    Two-lock pattern: the outer ``start_lock`` (acquired by the route)
    guards the request thread against multiple manual clicks; the
    inner ``.auto_report.lock`` acquired here guards the generate +
    persist sequence against a concurrent auto-report watcher tick.
    Both locks live in the same run dir but they protect different
    things -- start_lock blocks request-thread reentry, the auto-
    report sentinel blocks the watcher (which never goes through the
    start_lock).
    """
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None  # narrowed by state_err-guard above
    # Lifecycle gate: reconcile flat ``run_state.json`` the same way
    # ``/status`` does so a real subprocess-runner completion (which
    # never writes back to ``state.json``) is admissible here. Without
    # this reconciliation the route rejects every generic policy
    # subprocess run because ``state["phase"]`` is still ``running``
    # even though the subprocess finished.
    effective_phase, _runner_err = _reconcile_effective_phase(
        run_dir, sim_id, state,
    )
    if effective_phase != "completed":
        return _err(
            PlatformErrorCode.INVALID_STATE,
            f"simulation phase {effective_phase!r} is not 'completed'; "
            "cannot generate report",
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "current_phase": effective_phase,
            },
        )
    # If the reconciliation lifted ``state["phase"]`` from
    # ``running`` to ``completed``, OR if ``state["status"]`` is
    # missing / stale relative to the effective phase, persist the
    # backfill to disk so downstream readers (watcher, other
    # route handlers, subsequent ``/status`` polls) see the
    # lifecycle truth without repeating the probe. ``_set_lifecycle_phase``
    # writes BOTH ``phase`` and ``status`` so they stay aligned;
    # the watcher reads ``status``, the dispatch reads ``phase``,
    # and a drift between the two would silently break auto-report.
    if (
        state.get("phase") != effective_phase
        or state.get("status") != effective_phase
    ):
        _set_lifecycle_phase(state, effective_phase)
        atomic_write_json(str(run_dir / "state.json"), state)

    # Acquire the auto-report sentinel that the watcher checks. The
    # watcher's ``_maybe_generate`` uses O_CREAT|O_EXCL on the same
    # filename in the same run dir: if it sees the file the manual
    # caller created, it backs off with ``report_generate_in_progress``
    # rather than racing the manual generator on the same artifacts.
    # The sentinel is removed in the finally clause below regardless of
    # which return path the rest of this function takes.
    auto_lock_path = run_dir / _AUTO_REPORT_LOCK_FILENAME
    try:
        lock_fd = os.open(
            str(auto_lock_path),
            os.O_CREAT | os.O_EXCL | os.O_WRONLY,
            0o600,
        )
    except FileExistsError:
        return _err(
            ErrorCode.INVALID_REQUEST,
            (
                "another report generation is in flight for "
                f"{sim_id!r}; retry shortly"
            ),
            409,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "auto_report_in_progress",
            },
        )
    try:
        os.write(lock_fd, str(os.getpid()).encode("utf-8"))
    except OSError:
        pass
    finally:
        try:
            os.close(lock_fd)
        except OSError:
            pass

    try:
        return _generate_report_inner(
            adapter=adapter,
            use_case_id=use_case_id,
            sim_id=sim_id,
            run_dir=run_dir,
            state=state,
        )
    finally:
        try:
            os.unlink(str(auto_lock_path))
        except OSError:
            # Sentinel removed out of band or transient FS error. The
            # next caller's O_CREAT|O_EXCL will observe a clean run dir
            # (success path) or re-fail (retry).
            pass


def _generate_report_inner(
    *,
    adapter: SimulationUseCase,
    use_case_id: str,
    sim_id: str,
    run_dir: Path,
    state: Dict[str, Any],
):
    """Body of /report/generate that runs UNDER the auto-report lock.

    Split out so the lock-acquire / lock-release plumbing in
    :func:`_generate_report_locked` stays linear and the finally
    cleanup always fires regardless of which return path the inner
    body takes.
    """
    try:
        scenario = adapter.validate_scenario(state.get("scenario") or {})
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.SCENARIO_INVALID,
            f"persisted scenario re-validation failed: {type(exc).__name__}",
            500,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    # Resolve the run-metadata input to the adapter. Adapters whose
    # ``generate_report`` consumes the full typed :class:`RunMetadata`
    # (enum persona, scale_caps, artifact_hashes, etc.) declare
    # :attr:`SimulationUseCase.adapter_runs_guardrails_internally` as
    # ``True`` -- the route then loads ``run_metadata.json`` from disk
    # and validates it through ``RunMetadata.model_validate_json``. A
    # missing or corrupt metadata file under that contract is
    # ``STATE_CORRUPTED`` 500 with a discriminator reason so a client
    # can tell "the adapter required typed run metadata and the run
    # dir is in a bad state" from a transient runner failure.
    #
    # Adapters that do not require the typed shape (creator, fake,
    # other lanes that read only ``simulation_id`` / ``scenario_hash``
    # / ``seed_hash`` / ``persona`` off the metadata object) flow
    # through :func:`_build_run_metadata` -- the duck-typed
    # ``SimpleNamespace`` derived from ``state.json``. This branch is
    # reachable for lanes that have not minted ``run_metadata.json``
    # at all (the platform Protocol does not force a metadata-write
    # step), so the route MUST NOT 500 on its absence.
    if getattr(adapter, "adapter_runs_guardrails_internally", False):
        from ..simulation_platform.run_metadata import RunMetadata
        from pydantic import ValidationError
        meta_path = run_dir / "run_metadata.json"
        if not meta_path.is_file():
            return _err(
                PlatformErrorCode.STATE_CORRUPTED,
                f"run_metadata.json missing for {sim_id!r} under adapter "
                f"{use_case_id!r} (declares "
                f"adapter_runs_guardrails_internally=True)",
                500,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "run_metadata_missing",
                },
            )
        try:
            rm = RunMetadata.model_validate_json(
                meta_path.read_text(encoding="utf-8"),
            )
        except (OSError, ValidationError) as exc:
            return _err(
                PlatformErrorCode.STATE_CORRUPTED,
                f"run_metadata.json invalid for {sim_id!r}: "
                f"{type(exc).__name__}",
                500,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "run_metadata_corrupt",
                },
            )
    else:
        rm = _build_run_metadata(state)
    # Discover the adapter's optional guardrail hooks (Protocol
    # attribute ``guardrail_capabilities``). When the adapter wires
    # ``build_evidence_catalog``, the catalog is constructed BEFORE
    # ``generate_report`` so the adapter can demote unsupported
    # claims at generation time. Adapters that leave the hook as
    # ``None`` get the JSON-only path (evidence_catalog=None) -- the
    # contract is opt-in by hook field; no silent skip.
    caps = getattr(adapter, "guardrail_capabilities", None)
    evidence_catalog = None
    if caps is not None and caps.build_evidence_catalog is not None:
        try:
            evidence_catalog = caps.build_evidence_catalog(run_dir, scenario)
        except Exception as exc:  # noqa: BLE001
            return _err(
                PlatformErrorCode.ADAPTER_REPORT_FAILED,
                f"build_evidence_catalog raised {type(exc).__name__}: {exc}",
                502,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "guardrail_evidence_catalog_failed",
                },
            )
    # Build the caller-owned LLM client chain so the adapter exercises
    # the audit sink + strict-mode wrapping configured here rather than
    # constructing its own from env. The route resolves the LLM client
    # through the lane-neutral provider factory
    # (:func:`simulation_platform.llm.provider.get_llm_provider_factory`)
    # so the platform layer does NOT bind report generation directly
    # to one provider. Adapters can expose ``llm_provider_factory``;
    # factories that understand run-scoped config receive the
    # persisted RawFish provider/model binding for this run.
    try:
        from ..simulation_platform.llm import (
            AuditedLLMClient,
            RunMetadataAuditSink,
            StructuredOutputClient,
        )
        from ..simulation_platform.llm import provider as _llm_provider
        provider_config = provider_config_from_state(state.get("llm_provider"))
        provider_readiness = check_provider_readiness(provider_config, probe=False)
        if not provider_readiness.ready:
            return _err(
                PlatformErrorCode.ADAPTER_REPORT_FAILED,
                provider_readiness.reason or provider_readiness.status,
                502,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "llm_provider_not_ready",
                    "provider_status": provider_readiness.status,
                },
            )
        raw_llm = _llm_provider.build_llm_client_for_run(
            adapter=adapter,
            provider_config=provider_config,
        )
        inner = raw_llm
        # Strict-mode JSON target: prefer the LLM-owned
        # :attr:`report_draft_schema` (the subset the model is
        # actually permitted to emit) over the persisted
        # :attr:`report_schema`. Adapters whose ``generate_report``
        # merges caller-owned provenance into the LLM output BEFORE
        # validating against the persisted schema (policy lane:
        # :class:`PolicyReportGenerator.generate` merges
        # simulation_id, scenario_hash, seed_hash, embedded
        # run_metadata) would have the strict-schema preflight
        # reject every legitimate draft because the provenance
        # fields are not in the LLM payload yet. The draft
        # schema captures exactly what the model is permitted to
        # emit; the persisted schema is enforced downstream by
        # the adapter's own merge + ``model_validate`` step.
        strict_schema = (
            getattr(adapter, "report_draft_schema", None)
            or getattr(adapter, "report_schema", None)
        )
        if strict_schema is not None:
            inner = StructuredOutputClient(  # type: ignore[assignment]
                raw_llm,  # type: ignore[arg-type]
                target_schema=strict_schema,
                schema_name=f"{use_case_id}_report",
            )
        llm_client = AuditedLLMClient(
            inner,  # type: ignore[arg-type]
            sink=RunMetadataAuditSink(run_dir=str(run_dir)),
            phase="report",
        )
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_REPORT_FAILED,
            f"provider client construction failed: {type(exc).__name__}: {exc}",
            502,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "provider_client_build_failed",
                "kind": type(exc).__name__,
            },
        )
    try:
        report_obj = invoke_lane_generate_report(
            adapter,
            scenario=scenario,
            run_metadata=rm,
            evidence_catalog=evidence_catalog,
            llm_client=llm_client,
        )
    except NotImplementedError as nie:
        return _err(
            PlatformErrorCode.CAPABILITY_UNSUPPORTED,
            f"adapter {use_case_id!r} does not implement generate_report",
            501,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "capability_unsupported",
                "capability": "generate_report",
                "message": str(nie),
            },
        )
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_REPORT_FAILED,
            f"generate_report raised {type(exc).__name__}: {exc}",
            502,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    # Guardrail hook pipeline (post-generate, pre-persist). Each hook
    # is an opt-in member of ``adapter.guardrail_capabilities``. When
    # the field is None or a specific hook is None, that stage is
    # skipped honestly -- no silent fallback. Hooks fire in a pinned
    # order so a lane that opts in to advisory + transparency gets
    # the same sequence for manual report generation and auto-report:
    #
    #   1. ``run_advisory_claim_pass(report, evidence_catalog)``
    #      -- numeric / overclaim demotion to ``requires_validation``.
    #   2. ``apply_transparency_flags(report, run_metadata)``
    #      -- validity-flag synthesis onto the report.
    #   3. ``assert_render_contract(rendered_markdown)``
    #      -- runs after ``render_markdown(report)`` so the rendered
    #         text is checked against the lane's language contract.
    #
    # Adapter-internal-guardrails gate: lanes whose ``generate_report``
    # already drives advisory / transparency / language-contract
    # passes internally declare
    # :attr:`SimulationUseCase.adapter_runs_guardrails_internally` as
    # ``True``. The route then SKIPS the four post-generate hooks
    # below so the side effects (warnings, demotions, validity-flag
    # synthesis) do not compound on the same report. The
    # ``build_evidence_catalog`` hook ran BEFORE the adapter call
    # (the adapter consumes the catalog as an input) and is not
    # part of this skip.
    #
    # Persist safety (after hooks):
    #   1. Validate adapter's filename is a basename (no path
    #      separators / absolute paths).
    #   2. Validate the just-generated payload against
    #      ``adapter.report_schema`` BEFORE writing so a corrupt /
    #      schema-drifted return does not land on disk.
    #   3. Write through ``atomic_write_text`` so a crash mid-write
    #      leaves the previous file (or no file) -- never half.
    #   4. ORDER: artifacts first, then state.json. Inverse order
    #      would let a crash mid-sequence leave state.json
    #      advertising an artifact that's not on disk.
    runs_guardrails_internally = bool(
        getattr(adapter, "adapter_runs_guardrails_internally", False),
    )
    rendered_markdown: Optional[str] = None
    if not runs_guardrails_internally:
        if caps is not None and caps.run_advisory_claim_pass is not None:
            try:
                report_obj = caps.run_advisory_claim_pass(
                    report_obj, evidence_catalog,
                )
            except Exception as exc:  # noqa: BLE001
                return _err(
                    PlatformErrorCode.ADAPTER_REPORT_FAILED,
                    f"run_advisory_claim_pass raised {type(exc).__name__}: "
                    f"{exc}",
                    502,
                    {
                        "use_case_id": use_case_id,
                        "simulation_id": sim_id,
                        "reason": "guardrail_advisory_pass_failed",
                    },
                )
        if caps is not None and caps.apply_transparency_flags is not None:
            try:
                report_obj = caps.apply_transparency_flags(report_obj, rm)
            except Exception as exc:  # noqa: BLE001
                return _err(
                    PlatformErrorCode.ADAPTER_REPORT_FAILED,
                    f"apply_transparency_flags raised {type(exc).__name__}: "
                    f"{exc}",
                    502,
                    {
                        "use_case_id": use_case_id,
                        "simulation_id": sim_id,
                        "reason": "guardrail_transparency_failed",
                    },
                )
        if caps is not None and caps.render_markdown is not None:
            try:
                rendered_markdown = caps.render_markdown(report_obj)
            except Exception as exc:  # noqa: BLE001
                return _err(
                    PlatformErrorCode.ADAPTER_REPORT_FAILED,
                    f"render_markdown raised {type(exc).__name__}: {exc}",
                    502,
                    {
                        "use_case_id": use_case_id,
                        "simulation_id": sim_id,
                        "reason": "guardrail_markdown_render_failed",
                    },
                )
            if caps.assert_render_contract is not None:
                try:
                    caps.assert_render_contract(rendered_markdown)
                except Exception as exc:  # noqa: BLE001
                    return _err(
                        ErrorCode.REPORT_CORRUPTED,
                        f"assert_render_contract raised {type(exc).__name__}: "
                        f"{exc}",
                        500,
                        {
                            "use_case_id": use_case_id,
                            "simulation_id": sim_id,
                            "reason": "render_contract_violation",
                        },
                    )
    artifact_names = adapter.artifact_names()
    report_filename = artifact_names.get("report_json", "report.json")
    artifact_err = _safe_basename_artifact(report_filename, field="report_json")
    if artifact_err is not None:
        return artifact_err
    # Validate the markdown filename UP FRONT (before the JSON write
    # lands). An unsafe declaration of ``report_md`` after a JSON
    # write would otherwise leave an orphan JSON artifact behind --
    # the watcher would then skip the run as ``report_json``-present
    # and the markdown write would never complete.
    md_filename: Optional[str] = None
    md_sha: Optional[str] = None
    if rendered_markdown is not None:
        md_filename = artifact_names.get("report_md", "report.md")
        md_artifact_err = _safe_basename_artifact(
            md_filename, field="report_md",
        )
        if md_artifact_err is not None:
            return md_artifact_err
    report_path = run_dir / report_filename
    if hasattr(report_obj, "model_dump_json"):
        payload = report_obj.model_dump_json(indent=2)
    else:
        payload = json.dumps(report_obj, indent=2, default=str)
    # Write-time schema gate. ``adapter.report_schema`` (Protocol
    # member, can be None) is the same model the read route uses,
    # so a payload that fails here would also fail there. Failing
    # early keeps the corrupt bytes off disk.
    schema = adapter.report_schema
    if schema is not None and hasattr(schema, "model_validate_json"):
        try:
            schema.model_validate_json(payload)
        except Exception as exc:  # noqa: BLE001 -- Pydantic ValidationError + friends
            return _err(
                ErrorCode.REPORT_CORRUPTED,
                f"adapter.generate_report payload failed adapter.report_schema: "
                f"{type(exc).__name__}",
                500,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "generated_report_schema_invalid",
                },
            )
    atomic_write_text(str(report_path), payload)
    sha = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    if rendered_markdown is not None:
        assert md_filename is not None  # validated above
        atomic_write_text(str(run_dir / md_filename), rendered_markdown)
        md_sha = hashlib.sha256(
            rendered_markdown.encode("utf-8"),
        ).hexdigest()
    # Refresh ``run_metadata.output_paths`` / ``artifact_hashes`` so
    # consumers reading the metadata see canonical pointers + digests
    # after the route emits. Mirrors the auto-report watcher: the
    # helper is the single canonical write path for these fields.
    # ``refresh_output_path`` returns ``False``
    # without raising when ``run_metadata.json`` is absent (lanes that
    # have not minted the file get the no-op honestly); a corrupt
    # metadata file raises ``ValidationError`` which the route maps to
    # ``REPORT_CORRUPTED`` 500 so a stale record next to a fresh
    # artifact does not silently persist.
    from ..simulation_platform.run_metadata import (
        refresh_cost_summary as _refresh_cost_summary,
        refresh_output_path as _refresh,
    )
    from pydantic import ValidationError as _ValidationError
    try:
        _refresh(run_dir, artifact_name=report_filename, sha256_hex=sha)
        if md_filename is not None and md_sha is not None:
            _refresh(
                run_dir,
                artifact_name=md_filename,
                sha256_hex=md_sha,
            )
        _refresh_cost_summary(run_dir)
    except (_ValidationError, OSError) as exc:
        return _err(
            ErrorCode.REPORT_CORRUPTED,
            f"run_metadata.json refresh failed: {type(exc).__name__}",
            500,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "run_metadata_refresh_failed",
            },
        )

    _set_lifecycle_phase(state, "reported")
    state["report_path"] = str(report_filename)
    state["report_sha256"] = f"sha256:{sha}"
    if md_filename is not None and md_sha is not None:
        state["report_md_path"] = str(md_filename)
        state["report_md_sha256"] = f"sha256:{md_sha}"
    atomic_write_json(str(run_dir / "state.json"), state)
    response_payload: Dict[str, Any] = {
        "simulation_id": sim_id,
        "use_case_id": use_case_id,
        "phase": "reported",
        "report_path": str(report_filename),
        "sha256_json": f"sha256:{sha}",
    }
    if md_filename is not None and md_sha is not None:
        response_payload["report_md_path"] = str(md_filename)
        response_payload["sha256_md"] = f"sha256:{md_sha}"
    return _ok(response_payload)


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/report", methods=["GET"],
)
def get_report(use_case_id: str, sim_id: str):
    """Return the persisted report JSON for ``sim_id``.

    Adapter schema validation: the :class:`SimulationUseCase`
    Protocol declares ``report_schema: Optional[type]``. When the
    adapter sets it to a Pydantic model class (e.g. ``CreatorReport``
    on the creator adapter, ``Report`` on the policy adapter), the
    persisted JSON is validated against it before returning so a
    corrupt-on-disk artifact surfaces as REPORT_CORRUPTED (500)
    rather than passing through as raw possibly-malformed JSON.
    Adapters that explicitly set ``report_schema = None`` get the
    raw-parse path.
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    run_dir = _run_dir_for(use_case_id, sim_id)
    # Validate the run's state.json BEFORE the artifact lookup so a
    # missing simulation surfaces as SIMULATION_NOT_FOUND (404) and a
    # corrupt-on-disk state.json surfaces as STATE_CORRUPTED (500)
    # instead of being indistinguishable from a "report not yet
    # generated" 404 or being treated as an orphan artifact read.
    _state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    artifact_names = adapter.artifact_names()
    report_filename = artifact_names.get("report_json", "report.json")
    artifact_err = _safe_basename_artifact(report_filename, field="report_json")
    if artifact_err is not None:
        return artifact_err
    report_path = run_dir / report_filename
    if not report_path.is_file():
        return _err(
            ErrorCode.REPORT_NOT_READY,
            f"report not yet generated for {sim_id!r}",
            404,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    try:
        raw = report_path.read_text(encoding="utf-8")
    except OSError as exc:
        return _err(
            ErrorCode.REPORT_CORRUPTED,
            f"persisted report unreadable: {type(exc).__name__}",
            500,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    try:
        parsed = json.loads(raw)
    except json.JSONDecodeError as exc:
        return _err(
            ErrorCode.REPORT_CORRUPTED,
            f"persisted report JSON parse failed: {type(exc).__name__}",
            500,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    # Adapter schema validation. ``SimulationUseCase`` declares
    # ``report_schema: Optional[type]``; the structural check enforces
    # the attribute is present on every registered adapter. Adapters
    # that have no schema set ``= None`` (the raw-parse fallback);
    # adapters that want validation set ``= MyReportModel``.
    schema = adapter.report_schema
    if schema is not None and hasattr(schema, "model_validate"):
        try:
            schema.model_validate(parsed)
        except Exception as exc:  # noqa: BLE001 -- Pydantic ValidationError + friends
            return _err(
                ErrorCode.REPORT_CORRUPTED,
                f"persisted report failed adapter schema: {type(exc).__name__}",
                500,
                {"use_case_id": use_case_id, "simulation_id": sim_id},
            )
    return _ok(parsed)


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/report/chat", methods=["POST"],
)
@_wrap_idempotent
def chat_with_report(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Answer questions against the persisted report via the run provider."""

    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    if not isinstance(body, dict):
        body = {}
    message = str(body.get("message") or "").strip()
    if not message:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "request body must include a non-empty `message`",
            400,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    if len(message) > 4000:
        return _err(
            PlatformErrorCode.INVALID_INPUT,
            "report chat message is too long",
            413,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "message_too_long",
                "max_chars": 4000,
            },
        )
    run_dir = _run_dir_for(use_case_id, sim_id)
    state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    assert state is not None

    artifact_names = adapter.artifact_names()
    report_filename = artifact_names.get("report_json", "report.json")
    artifact_err = _safe_basename_artifact(report_filename, field="report_json")
    if artifact_err is not None:
        return artifact_err
    report_path = run_dir / report_filename
    if not report_path.is_file():
        return _err(
            ErrorCode.REPORT_NOT_READY,
            f"report not yet generated for {sim_id!r}",
            404,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    try:
        report_payload = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        return _err(
            ErrorCode.REPORT_CORRUPTED,
            f"persisted report unreadable: {type(exc).__name__}",
            500,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    schema = adapter.report_schema
    if schema is not None and hasattr(schema, "model_validate"):
        try:
            schema.model_validate(report_payload)
        except Exception as exc:  # noqa: BLE001
            return _err(
                ErrorCode.REPORT_CORRUPTED,
                f"persisted report failed adapter schema: {type(exc).__name__}",
                500,
                {"use_case_id": use_case_id, "simulation_id": sim_id},
            )

    history_raw = body.get("chat_history")
    history = history_raw if isinstance(history_raw, list) else []
    sanitized_history = []
    for turn in history[-8:]:
        if not isinstance(turn, dict):
            continue
        role = turn.get("role")
        content = turn.get("content")
        if role in {"user", "assistant"} and isinstance(content, str):
            sanitized_content = content.strip()[:2000]
            if sanitized_content:
                sanitized_history.append(
                    {"role": role, "content": sanitized_content}
                )

    report_json = json.dumps(report_payload, sort_keys=True, default=str)
    if len(report_json) > 24000:
        report_json = report_json[:24000] + "\n...<truncated>"

    try:
        from pydantic import ValidationError as _ValidationError
        from ..simulation_platform.run_metadata import (
            refresh_cost_summary as _refresh_cost_summary,
        )
        from ..simulation_platform.llm import AuditedLLMClient, RunMetadataAuditSink
        from ..simulation_platform.llm import provider as _llm_provider
        provider_config = provider_config_from_state(state.get("llm_provider"))
        provider_readiness = check_provider_readiness(provider_config, probe=False)
        if not provider_readiness.ready:
            return _err(
                PlatformErrorCode.ADAPTER_REPORT_FAILED,
                provider_readiness.reason or provider_readiness.status,
                502,
                {
                    "use_case_id": use_case_id,
                    "simulation_id": sim_id,
                    "reason": "llm_provider_not_ready",
                    "provider_status": provider_readiness.status,
                },
            )
        raw_llm = _llm_provider.build_llm_client_for_run(
            adapter=adapter,
            provider_config=provider_config,
        )
        llm_client = AuditedLLMClient(
            raw_llm,
            sink=RunMetadataAuditSink(run_dir=str(run_dir)),
            phase="report",
        )
        response = llm_client.chat_json(
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are the RawFish report agent. Answer only from "
                        "the supplied persisted report JSON and prior chat. "
                        "Return JSON with keys response and sources."
                    ),
                },
                *sanitized_history,
                {
                    "role": "user",
                    "content": (
                        f"Persisted report JSON:\n{report_json}\n\n"
                        f"Question: {message}"
                    ),
                },
            ],
            max_tokens=1200,
        )
        _refresh_cost_summary(run_dir)
        if not isinstance(response, dict):
            raise ValueError("report chat response must be an object")
        response_text = response.get("response")
        sources = response.get("sources")
        if not isinstance(response_text, str) or not response_text.strip():
            raise ValueError("report chat response must include non-empty response")
        if sources is None:
            sources = []
        if not isinstance(sources, list):
            raise ValueError("report chat sources must be a list")
        safe_sources: List[Any] = []
        for source in sources[:20]:
            if isinstance(source, (str, int, float, bool)) or source is None:
                safe_sources.append(source)
            elif isinstance(source, dict):
                safe_sources.append(source)
            else:
                raise ValueError("report chat sources must be JSON-compatible")
        response = {
            "response": response_text.strip(),
            "sources": safe_sources,
        }
    except (_ValidationError, OSError) as exc:
        return _err(
            ErrorCode.REPORT_CORRUPTED,
            f"run_metadata.json refresh failed: {type(exc).__name__}",
            500,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "run_metadata_refresh_failed",
            },
        )
    except ValueError as exc:
        return _err(
            PlatformErrorCode.ADAPTER_REPORT_FAILED,
            str(exc),
            502,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "report_chat_schema_invalid",
            },
        )
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_REPORT_FAILED,
            f"report chat failed: {type(exc).__name__}: {exc}",
            502,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "report_chat_failed",
                "kind": type(exc).__name__,
            },
        )
    return _ok(response)


@use_cases_bp.route(
    "/<use_case_id>/simulation/<sim_id>/sensitivity", methods=["POST"],
)
@_wrap_idempotent
def run_sensitivity(body: Dict[str, Any], use_case_id: str, sim_id: str):
    """Delegate to adapter ``run_sensitivity``; surface a typed
    501 ``CAPABILITY_UNSUPPORTED`` envelope when the adapter raises
    :class:`NotImplementedError`.

    The generic ``/sensitivity`` surface is reserved for lanes that
    wire a real-ensemble sensitivity runner. Lanes without that
    capability return a typed 501 instead of a redirect to another surface.
    """
    adapter, err = _resolve_use_case(use_case_id)
    if err is not None:
        return err
    assert adapter is not None  # narrowed by err-guard above
    state_err = _validate_safe_ids(use_case_id, sim_id)
    if state_err is not None:
        return state_err
    # Existence + integrity check on state.json BEFORE the adapter
    # call (and before any lane-level policy short-circuit). Missing
    # state -> 404 SIMULATION_NOT_FOUND; corrupt state -> 500
    # STATE_CORRUPTED. Without this check the adapter would either
    # be invoked against a non-existent run (silent orphan) or the
    # corrupt-state condition would be masked by a downstream
    # capability/policy response.
    run_dir = _run_dir_for(use_case_id, sim_id)
    _state, state_err = _read_state_or_err(run_dir, use_case_id, sim_id)
    if state_err is not None:
        return state_err
    # No per-lane hardcode here: lanes opt out by raising
    # NotImplementedError from ``run_sensitivity``. The catch below
    # maps that to a documented generic 501 without pointing callers
    # at removed routes.
    try:
        result = adapter.run_sensitivity(sim_id, body)
    except NotImplementedError as nie:
        details: Dict[str, Any] = {
            "use_case_id": use_case_id,
            "simulation_id": sim_id,
            "reason": "real_sensitivity_unsupported",
            "capability": "real_sensitivity",
            "message": str(nie),
        }
        return _err(
            PlatformErrorCode.CAPABILITY_UNSUPPORTED,
            (
                f"adapter {use_case_id!r} does not implement "
                "real sensitivity (ensemble re-runs)"
            ),
            501,
            details,
        )
    except Exception as exc:  # noqa: BLE001
        return _err(
            PlatformErrorCode.ADAPTER_SENSITIVITY_FAILED,
            f"run_sensitivity raised {type(exc).__name__}: {exc}",
            502,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    if hasattr(result, "model_dump"):
        result = result.model_dump(mode="json")
    return _ok(result)


# ----------------------------------------------------------------------
# Local utilities (no app.policy imports)
# ----------------------------------------------------------------------


def _validate_safe_ids(use_case_id: str, sim_id: str):
    """Reject path-traversal in either id; return an error tuple or None."""
    for field_name, value in (
        ("use_case_id", use_case_id),
        ("simulation_id", sim_id),
    ):
        try:
            validate_safe_id(value, field_name)
        except ValueError as ve:
            return _err(
                ErrorCode.INVALID_ID,
                str(ve),
                400,
                {"field": field_name},
            )
    return None


def _utcnow() -> str:
    return datetime.now(timezone.utc).isoformat()


def _set_lifecycle_phase(state: Dict[str, Any], phase: str) -> None:
    """Set the lifecycle field on ``state`` under BOTH wire spellings.

    Vocabulary unification across the two on-disk readers:

      * :mod:`app.simulation_platform.state_machine` writes
        ``state["status"]`` and the auto-report watcher reads it.
      * The generic dispatch's lifecycle routes (this module) write
        ``state["phase"]`` and read it.

    Without unification, generic-dispatch sims leave ``state["status"]``
    unset (the watcher cannot tell what lifecycle phase the run is in)
    and callers that swap on ``state["status"]`` see ``None`` for
    every generic-dispatch run. Writing both keys with the SAME value
    at every transition site makes the two surfaces consistent without
    rewriting the readers in lockstep.

    The forward-compatible direction is ``status`` (matches the
    state-machine writer and the watcher); ``phase`` is retained as the in-
    flight alias the dispatch route already uses. A later pass can
    drop ``phase`` once every reader migrates to ``status``.
    """
    state["phase"] = phase
    state["status"] = phase


def _mint_simulation_id(use_case_id: str) -> str:
    """Generate a stable per-use-case simulation id.

    Format: ``<use_case_id>_sim_<8-char hex>``. Deterministic enough
    to be operator-readable; entropy comes from os.urandom so two
    concurrent creates collide with negligible probability.
    """
    suffix = os.urandom(4).hex()
    return f"{use_case_id}_sim_{suffix}"


def _read_state_unsafe(run_dir: Path) -> Optional[Dict[str, Any]]:
    """Best-effort read that COLLAPSES missing-and-corrupt into None.

    Marked ``_unsafe`` because every mutating route MUST distinguish
    "no simulation yet" (404 SIMULATION_NOT_FOUND) from "state.json
    exists but is corrupt" (500 STATE_CORRUPTED). The honest variant
    is :func:`_read_state_or_err`; this helper is retained ONLY for
    contexts that genuinely want the silent-skip semantic. Call sites
    that need the distinguishing read MUST NOT call this function.
    """
    path = run_dir / "state.json"
    if not path.is_file():
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None


def _read_state_or_err(
    run_dir: Path,
    use_case_id: str,
    sim_id: str,
) -> Tuple[Optional[Dict[str, Any]], Optional[Any]]:
    """Read ``state.json`` and distinguish missing (404) from
    corrupt (500).

    Returns ``(state, None)`` on a clean read or
    ``(None, error_envelope)`` when the caller should ``return``
    the envelope. Missing -> ``SIMULATION_NOT_FOUND``; unreadable
    or invalid JSON -> ``STATE_CORRUPTED`` with a
    ``details.reason`` discriminator.
    """
    path = run_dir / "state.json"
    if not path.is_file():
        return None, _err(
            ErrorCode.SIMULATION_NOT_FOUND,
            f"no simulation {sim_id!r} for use_case {use_case_id!r}",
            404,
            {"use_case_id": use_case_id, "simulation_id": sim_id},
        )
    try:
        raw = path.read_text(encoding="utf-8")
    except OSError as exc:
        return None, _err(
            PlatformErrorCode.STATE_CORRUPTED,
            f"state.json unreadable: {type(exc).__name__}",
            500,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "state_unreadable",
            },
        )
    try:
        state = json.loads(raw)
    except json.JSONDecodeError as exc:
        return None, _err(
            PlatformErrorCode.STATE_CORRUPTED,
            f"state.json JSON parse failed: {type(exc).__name__}",
            500,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "state_json_parse_failed",
            },
        )
    if not isinstance(state, dict):
        return None, _err(
            PlatformErrorCode.STATE_CORRUPTED,
            f"state.json top level must be an object; got {type(state).__name__}",
            500,
            {
                "use_case_id": use_case_id,
                "simulation_id": sim_id,
                "reason": "state_wrong_top_level_type",
            },
        )
    return state, None


def _build_run_metadata(state: Dict[str, Any]) -> Any:
    """Build a minimal duck-typed run-metadata object from ``state``.

    Lane adapters read four attributes today: ``simulation_id``,
    ``scenario_hash``, ``seed_hash``, ``persona``. The generic
    route module synthesizes those four from ``state.json`` so an
    adapter that never depended on the policy lane's full
    :class:`RunMetadata` shape still receives the inputs it needs.
    The synthesised object is a :class:`types.SimpleNamespace` so
    attribute access works without re-defining a Pydantic model
    here.
    """
    import hashlib as _hashlib
    from types import SimpleNamespace

    scenario_payload = state.get("scenario") or {}
    raw_scenario = json.dumps(scenario_payload, sort_keys=True).encode("utf-8")
    return SimpleNamespace(
        simulation_id=state.get("simulation_id", ""),
        # Deterministic hashes derived from the persisted scenario so
        # two runs of the same scenario yield byte-identical metadata.
        scenario_hash=_hashlib.sha256(raw_scenario).hexdigest(),
        seed_hash=_hashlib.sha256(
            (state.get("simulation_id", "") + ":seed").encode("utf-8")
        ).hexdigest(),
        persona=scenario_payload.get("persona", ""),
        statistical_settings=state.get("statistical_settings") or {},
        resolved_statistical_config=state.get("statistical_settings") or {},
        statistical_settings_hash=state.get("statistical_settings_hash"),
        statistical_settings_version=state.get("statistical_settings_version"),
        provenance_per_field=state.get("provenance_per_field") or {},
        lock_state_per_field=state.get("lock_state_per_field") or {},
        persona_salts_resolved=(
            state.get("statistical_runtime_overrides") or {}
        ).get("persona_salts") or {},
        prior_attachments=state.get("prior_attachments") or {},
        variant_lineage=state.get("statistical_variant_lineage") or [],
        statistical_variant_lineage=state.get("statistical_variant_lineage") or [],
    )


__all__ = ["use_cases_bp"]
