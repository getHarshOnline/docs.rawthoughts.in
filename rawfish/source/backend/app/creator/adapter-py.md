---
title: "backend/app/creator/adapter.py"
noindex: true
---

```py
"""Creator lane adapter: registers this use case with the platform.

Thin adapter -- delegates every Protocol method to the helpers in
sibling modules (:mod:`catalog`, :mod:`defaults`, :mod:`report_generator`).
The same module-level-singleton pattern the policy adapter uses keeps
:func:`app.simulation_platform.registry.register` idempotent across
repeated ``create_app()`` calls in the same process.

Platform infrastructure reused (not duplicated) by this adapter:

* :mod:`app.simulation_platform.registry` -- the in-process registry
  this adapter joins via :func:`register`.
* :mod:`app.simulation_platform.catalog` -- the
  :class:`~app.simulation_platform.catalog.CatalogPayload` /
  :class:`~app.simulation_platform.catalog.PersonaSpec` wire shapes the
  frontend wizard reads.
* :mod:`app.simulation_platform.use_case` -- the
  :class:`~app.simulation_platform.use_case.SimulationUseCase` Protocol
  this class structurally satisfies.
* :mod:`app.simulation_platform.artifact_manifest` /
  :mod:`app.simulation_platform.idempotency` /
  :mod:`app.simulation_platform.state_machine` --
  cross-use-case primitives a future HTTP-dispatching layer will share
  across adapters; this adapter does not re-implement any of them.

Persona vocabulary, segment-type allowlist, and report shape are owned
by sibling modules in this package -- the policy adapter's enums and
Pydantic models are NOT imported here on purpose: each use case owns
its own product schema.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from app.simulation_platform.guardrails import GuardrailCapabilities
from app.simulation_platform.catalog import (
    CatalogPayload,
    PersonaSpec,
    build_minimal_lane_manifest,
)
from app.simulation_platform.statistical import runtime_overrides_from_settings
from app.utils.atomic_io import atomic_write_json, atomic_write_text

from .catalog import CREATOR_SEGMENT_TYPES, CreatorPersona
from .defaults import (
    capabilities_for,
    cohort_question_for,
    label_for,
    report_sections_for,
)
from .report_generator import (
    CANONICAL_CLAIM_TAGS,
    CreatorReportGenerator,
    CreatorReport,
    CreatorReportLLMDraft,
    CreatorScenario,
)


def _creator_render_markdown(report: Any) -> str:
    """GuardrailCapabilities hook: render a creator report to markdown.

    Creator does not ship a dedicated markdown renderer; this hook
    produces a compact text bundle that round-trips the
    :class:`CreatorReport` fields the operator typically wants in a
    pasted-into-doc context. Title + persona + sections (titles +
    claims) + field-validation questions. The result is plain
    markdown -- no template engine, no policy-specific chrome.
    """
    if hasattr(report, "model_dump"):
        data = report.model_dump(mode="python")
    else:
        data = dict(report)
    lines: list[str] = []
    lines.append("# Creator response report")
    persona = data.get("persona")
    if persona:
        lines.append(f"- **Persona:** {persona}")
    rid = data.get("report_id")
    if rid:
        lines.append(f"- **Report id:** `{rid}`")
    lines.append("")
    exec_summary = data.get("executive_summary") or []
    if exec_summary:
        lines.append("## Executive summary")
        for claim in exec_summary:
            text = claim.get("text") if isinstance(claim, dict) else None
            tag = claim.get("tag") if isinstance(claim, dict) else None
            if text:
                tag_str = f" _({tag})_" if tag else ""
                lines.append(f"- {text}{tag_str}")
        lines.append("")
    for section in data.get("sections") or []:
        title = section.get("title") if isinstance(section, dict) else None
        if not title:
            continue
        lines.append(f"## {title}")
        for claim in section.get("claims", []) or []:
            text = claim.get("text") if isinstance(claim, dict) else None
            tag = claim.get("tag") if isinstance(claim, dict) else None
            if text:
                tag_str = f" _({tag})_" if tag else ""
                lines.append(f"- {text}{tag_str}")
        lines.append("")
    fvq = data.get("field_validation_questions") or []
    if fvq:
        lines.append("## Field validation questions")
        for q in fvq:
            lines.append(f"- {q}")
        lines.append("")
    return "\n".join(lines)


def _creator_assert_render_contract(rendered_markdown: str) -> None:
    """GuardrailCapabilities hook: enforce the hedged-language
    contract on the rendered creator markdown.

    Reuses :func:`app.services.policy.language_guard.assert_no_unhedged_banned_tokens`
    -- the same regex set is the platform language contract for any
    lane that surfaces narrative prose to operators. A future
    creator-specific contract would replace this with a lane-private
    helper; for now the shared regex set is the right contract.
    """
    from app.services.policy.language_guard import (
        assert_no_unhedged_banned_tokens,
    )
    assert_no_unhedged_banned_tokens(rendered_markdown)


CREATOR_GUARDRAIL_CAPABILITIES = GuardrailCapabilities(
    render_markdown=_creator_render_markdown,
    assert_render_contract=_creator_assert_render_contract,
)


# Filename written under each ``run_dir`` by :meth:`write_prepare_artifacts`.
# Carries the canonical scenario snapshot for the run; the read-path
# consumer (future HTTP-dispatched route) loads it back via
# :class:`CreatorScenario.model_validate_json`.
_PREPARE_ARTIFACT_FILENAME: str = "creator_prepare.json"


# Filename written by the report generator. Kept here AND in the
# generator module so :meth:`artifact_names` can publish it without
# importing the generator at module load (the generator pulls in
# pydantic which would slow adapter import on cold start). The
# generator's actual write path uses the SAME literal -- a unit test
# pinning the two against each other lives in the conformance suite
# below.
_REPORT_ARTIFACT_FILENAME: str = "creator_report.json"
_STATISTICAL_ARTIFACT_FILENAME: str = "statistical_settings.json"


def _statistical_context_from_run_dir(run_dir: Path) -> Dict[str, Any]:
    state_path = Path(run_dir) / "state.json"
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    if not isinstance(state, dict):
        return {}
    settings = state.get("statistical_settings")
    if not isinstance(settings, dict):
        return {}
    return {
        "lane_id": state.get("use_case_id"),
        "settings": settings,
        "statistical_settings_hash": state.get("statistical_settings_hash"),
        "version": state.get("statistical_settings_version"),
        "runtime_overrides": runtime_overrides_from_settings(settings).model_dump(
            mode="json",
            exclude_none=True,
        ),
        "variant_lineage": state.get("statistical_variant_lineage") or [],
    }


class CreatorUseCase:
    """Adapter implementing
    :class:`app.simulation_platform.use_case.SimulationUseCase` for the
    creator surface.

    Every method delegates to a sibling helper; no product behaviour
    lives in this class. Adding logic here would make the adapter the
    de-facto source of truth instead of a thin wrapper, defeating the
    platform-seam design.
    """

    #: GuardrailCapabilities populated with two hooks the generic
    #: dispatch + auto-report watcher can drive:
    #:
    #:   * ``render_markdown`` -- compact text bundle of the report.
    #:   * ``assert_render_contract`` -- shared platform language
    #:     guard (un-hedged banned tokens raise).
    #:
    #: The remaining hooks (``build_evidence_catalog``,
    #: ``run_advisory_claim_pass``, ``apply_transparency_flags``)
    #: stay ``None`` until the creator lane ships an evidence store
    #: + transparency-flag synthesis surface.
    guardrail_capabilities: Optional[GuardrailCapabilities] = (
        CREATOR_GUARDRAIL_CAPABILITIES
    )

    #: Read-side schema for the persisted creator
    #: report. The generic
    #: ``GET /api/sim/use-cases/creator/simulation/<id>/report``
    #: dispatch route validates the on-disk JSON via
    #: ``CreatorReport.model_validate`` before returning, so a
    #: corrupt-but-JSON artifact (schema drift, hand-edit, truncated
    #: write) surfaces as ``REPORT_CORRUPTED`` rather than passing
    #: through as raw, possibly-malformed JSON.
    report_schema: Optional[type] = CreatorReport

    #: LLM-owned subset of :class:`CreatorReport`. The generator
    #: instructs the LLM not to emit provenance fields
    #: (``report_id`` / ``simulation_id`` / ``persona`` /
    #: ``scenario_hash`` / ``seed_hash`` / ``generated_at``); those
    #: are merged in by the generator AFTER the LLM response. A
    #: strict-JSON-mode wrapper (``StructuredOutputClient``)
    #: validates the raw response BEFORE that merge, so the target
    #: schema MUST be the draft -- using the full
    #: :class:`CreatorReport` would reject every valid LLM response
    #: for missing provenance.
    report_draft_schema: Optional[type] = CreatorReportLLMDraft

    #: Optional Pydantic class for the on-disk ``artifact_manifest.json``
    #: written by ``/prepare``. Creator does NOT yet ship a typed
    #: manifest schema; declared as ``None`` so the Protocol's
    #: structural dispatch can ``getattr`` the field without a
    #: defensive fallback. A future schema lift sets this to the
    #: concrete model class and the dispatch route picks it up
    #: automatically.
    prepare_manifest_schema: Optional[type] = None

    #: Creator's :meth:`generate_report` does NOT internally run
    #: advisory / transparency / language-contract passes; the
    #: generic dispatch route applies whichever hooks the adapter
    #: wires on :attr:`guardrail_capabilities`. Declared as
    #: ``False`` so the dispatch + watcher run the standard
    #: post-generate hook chain on the returned report.
    adapter_runs_guardrails_internally: bool = False

    # ------------------------------------------------------------------
    # Identity / metadata
    # ------------------------------------------------------------------

    def use_case_id(self) -> str:
        """Stable id; the registry forbids id collisions across adapters."""
        return "creator"

    def catalog(self) -> CatalogPayload:
        """Publish persona + segment-type metadata for the wizard."""
        personas: List[PersonaSpec] = []
        for persona in (
            CreatorPersona.VIDEO_CREATOR,
            CreatorPersona.NEWSLETTER_WRITER,
            CreatorPersona.PODCASTER,
        ):
            segment_types_by_scope: Dict[Optional[str], List[str]] = {
                None: list(CREATOR_SEGMENT_TYPES[persona]),
            }
            report_sections_by_scope: Dict[Optional[str], List[str]] = {
                None: [s["title"] for s in report_sections_for(persona)],
            }
            defaults: Dict[str, Any] = {
                "capabilities": capabilities_for(persona),
                "hypothesis_tags": sorted(CANONICAL_CLAIM_TAGS),
            }
            personas.append(
                PersonaSpec(
                    persona_id=persona.value,
                    label=label_for(persona),
                    cohort_question=cohort_question_for(persona),
                    scopes=None,
                    segment_types_by_scope=segment_types_by_scope,
                    defaults=defaults,
                    report_sections_by_scope=report_sections_by_scope,
                )
            )
        report_section_labels: List[str] = []
        for spec in personas:
            for sections in spec.report_sections_by_scope.values():
                report_section_labels.extend(sections)
        return CatalogPayload(
            use_case_id=self.use_case_id(),
            lane_manifest=build_minimal_lane_manifest(
                lane_id=self.use_case_id(),
                label="Creator",
                summary="Pre-mortem cockpit for creator audience reaction.",
                report_sections=report_section_labels or None,
            ),
            personas=personas,
        )

    def artifact_names(self) -> Dict[str, str]:
        """Map logical artifact ids to filenames written under ``run_dir``.

        The filenames must NOT collide with the policy adapter's
        (``policy_report.json``, ``policy_report.md``, ``sensitivity.json``).
        Distinct prefixes keep a future shared-run-directory layout
        unambiguous; the platform conformance suite has an explicit
        no-collision test that pins this.
        """
        return {
            "report_json": _REPORT_ARTIFACT_FILENAME,
            "prepare": _PREPARE_ARTIFACT_FILENAME,
            "statistical_settings": _STATISTICAL_ARTIFACT_FILENAME,
        }

    # ------------------------------------------------------------------
    # Authoring inputs
    # ------------------------------------------------------------------

    def validate_scenario(self, payload: Any) -> CreatorScenario:
        """Validate an inbound scenario payload.

        Runs :func:`CreatorScenario.model_validate` AND the explicit
        persona-aware segment-type check that lives on the model
        (Pydantic field validators cannot see persona context without
        leaking the catalog import into the leaf model). Returns the
        validated scenario; raises ``pydantic.ValidationError`` or
        ``ValueError`` on failure.
        """
        scenario = CreatorScenario.model_validate(payload)
        return scenario.validate_segment_types()

    def rehydrate_scenario(self, state_dict: Dict[str, Any]) -> CreatorScenario:
        """Rebuild the :class:`CreatorScenario` from a persisted ``state.json`` dict.

        Delegates to :meth:`validate_scenario` on the
        ``state_dict["scenario"]`` payload so the persona-aware
        segment-type check runs on the round-trip path the same way
        it does on the create path.
        """
        return self.validate_scenario(state_dict["scenario"])

    def parse_seed(
        self,
        seed_text: str,
        stress_question: str,
        persona: str,
        scope: Optional[str],
    ) -> Dict[str, Any]:
        """Return a minimal scenario-draft dict from free-form inputs.

        The platform Protocol does not mandate the draft shape; we
        return a dict carrying the input fields under their canonical
        keys. ``scope`` is accepted for Protocol conformance and ignored
        -- this use case has no scope dimension (see
        :class:`PersonaSpec.scopes`).
        """
        del scope  # Accepted per Protocol; no scope dimension here.
        draft: Dict[str, Any] = {
            "persona": persona,
            "seed_text": seed_text,
            "stress_question": stress_question,
        }
        return draft

    def load_presets(self) -> List[Any]:
        """No authored presets on disk for this surface today.

        The Protocol requires the method exist; returning an empty list
        is the correct "no presets yet" signal for the frontend to
        render an empty preset picker rather than the unauthored fallback.
        """
        return []

    # ------------------------------------------------------------------
    # Prepare phase
    # ------------------------------------------------------------------

    def build_ontology(self, scenario: Any, run_dir: Path) -> None:
        """No-op for this use case today.

        The policy adapter's prepare phase materialises the audience
        store via the Graphiti seam. The creator
        surface does not yet wire an audience store; the Protocol
        method must exist (``@runtime_checkable`` enforces structural
        conformance) so the platform conformance suite accepts the
        adapter. When a store seam is wired this method will publish
        the per-segment ontology nodes; until then it is intentionally
        a no-op.
        """
        del scenario, run_dir  # Protocol args; no store wired yet.

    def write_prepare_artifacts(
        self, scenario: Any, run_dir: Path
    ) -> Dict[str, Any]:
        """Persist the validated scenario snapshot under ``run_dir``.

        The on-disk artifact is the canonical
        :class:`CreatorScenario` JSON; the read-path consumer reloads
        it via ``CreatorScenario.model_validate_json``. Returns an
        artifact-manifest-shaped dict whose ``artifacts`` mapping uses
        the same logical-id keys as :meth:`artifact_names`.
        """
        if not isinstance(scenario, CreatorScenario):
            scenario = self.validate_scenario(scenario)
        out = Path(run_dir) / _PREPARE_ARTIFACT_FILENAME
        # Atomic write: a torn write would leave a half-written
        # prepare artifact next to the run dir, which the start /
        # report routes downstream would mis-validate. ``atomic_write_text``
        # (temp file + ``os.replace``) is the same primitive the
        # platform's report-write path uses.
        atomic_write_text(
            str(out), scenario.model_dump_json(indent=2),
        )
        statistical_context = _statistical_context_from_run_dir(Path(run_dir))
        artifacts = {
            "prepare": _PREPARE_ARTIFACT_FILENAME,
        }
        if statistical_context:
            statistical_out = Path(run_dir) / _STATISTICAL_ARTIFACT_FILENAME
            atomic_write_text(
                str(statistical_out),
                json.dumps(statistical_context, indent=2, sort_keys=True),
            )
            artifacts["statistical_settings"] = _STATISTICAL_ARTIFACT_FILENAME
        return {
            "artifacts": artifacts,
        }

    # ------------------------------------------------------------------
    # Report phase
    # ------------------------------------------------------------------

    def generate_report(
        self,
        scenario: Any,
        run_metadata: Any,
        evidence_catalog: Any,
        llm_client: Any = None,
    ) -> Any:
        """Produce the creator report.

        ``run_metadata`` is read in a duck-typed way: this adapter does
        not depend on the policy ``RunMetadata`` class. The required
        attributes are ``simulation_id``, ``scenario_hash``,
        ``seed_hash``, and ``persona``. ``evidence_catalog`` is accepted
        for Protocol conformance and not yet consumed; the binding step
        will land alongside the use case's evidence-store wiring.

        ``llm_client`` (when non-None) is the caller-built LLM client
        the generator uses; when ``None`` the adapter constructs a
        RawFish-router client through the shared provider factory.
        """
        del evidence_catalog  # Protocol-required; not yet consumed.

        if not isinstance(scenario, CreatorScenario):
            scenario = self.validate_scenario(scenario)

        run_persona = self._coerce_run_persona(getattr(run_metadata, "persona"))

        if llm_client is None:
            from app.simulation_platform.llm.provider import (
                build_llm_client_for_run,
            )
            llm_client = build_llm_client_for_run(adapter=self)
        gen = CreatorReportGenerator(
            scenario=scenario, llm=llm_client,
        )
        return gen.generate(
            simulation_id=str(run_metadata.simulation_id),
            scenario_hash=str(run_metadata.scenario_hash),
            seed_hash=str(run_metadata.seed_hash),
            run_persona=run_persona,
        )

    @staticmethod
    def _coerce_run_persona(value: Any) -> CreatorPersona:
        """Normalise the run-metadata persona value to a CreatorPersona.

        Accepts either a :class:`CreatorPersona` instance (the generator
        is invoked directly from a test that owns the type) or a string
        value matching one of the enum members. Anything else raises
        ``ValueError`` -- the platform Protocol leaves ``run_metadata``
        typed as ``Any``, so a sloppy caller passing a policy persona
        would otherwise produce a confusing AttributeError elsewhere.
        """
        if isinstance(value, CreatorPersona):
            return value
        if isinstance(value, str):
            try:
                return CreatorPersona(value)
            except ValueError as exc:
                raise ValueError(
                    f"run_metadata.persona={value!r} is not a valid "
                    f"CreatorPersona; allowed: "
                    f"{[p.value for p in CreatorPersona]!r}"
                ) from exc
        # Enum-like objects with a ``.value`` (e.g. the policy Persona
        # enum) reach here -- we reject explicitly so the wrong-persona
        # case fails with a clear message rather than silently slipping
        # into the str branch via __str__.
        raise ValueError(
            f"run_metadata.persona has unsupported type "
            f"{type(value).__name__}; pass a CreatorPersona or its "
            "string value."
        )

    # ------------------------------------------------------------------
    # Run phase
    # ------------------------------------------------------------------

    def run_simulation(self, scenario: Any, run_dir: Path) -> Optional[str]:
        """Deterministic-mock runner: writes a minimal
        ``run_state.json`` marker under ``run_dir`` so the
        run-resolution layer sees the run as finished, then
        returns.

        The creator lane does not yet ship a subprocess runner; the
        deterministic mock makes the lifecycle real. The method
        returns ``None`` (the state-authority signal documented on
        the :class:`SimulationUseCase` Protocol) so the generic
        dispatch route OWNS the post-handoff
        ``state["phase"] = "completed"`` transition -- the
        deterministic-mock path finished by the time the call
        returned, so the route's ``completed`` flip is honest. A
        future lane that wires a real subprocess runner returns the
        persisted-status string instead so the route mirrors the
        in-flight ``"running"`` without lying.
        """
        del scenario  # the deterministic mock does not consume the scenario
        run_dir = Path(run_dir)
        run_dir.mkdir(parents=True, exist_ok=True)
        marker = run_dir / "run_state.json"
        statistical_context = _statistical_context_from_run_dir(run_dir)
        statistical_settings = statistical_context.get("settings")
        if not isinstance(statistical_settings, dict):
            statistical_settings = {}
        statistical_overrides = statistical_context.get("runtime_overrides")
        if not isinstance(statistical_overrides, dict):
            statistical_overrides = {}
        # Atomic write so a concurrent read of the run-state marker
        # (the run-resolution layer polls this) cannot observe a
        # half-written JSON. Same primitive the policy lane's
        # state.json writes use.
        atomic_write_json(str(marker), {
            "use_case_id": self.use_case_id(),
            "status": "completed",
            "runner": "creator_deterministic_mock_v1",
            "statistical_settings_hash": statistical_context.get(
                "statistical_settings_hash",
            ),
            "statistical_seed": statistical_overrides.get(
                "run_seed",
                statistical_settings.get("run.run_seed"),
            ),
            "active_hours": statistical_overrides.get(
                "active_hours",
                statistical_settings.get("cohort.active_hours"),
            ),
            "active_hours_by_cohort": statistical_overrides.get(
                "active_hours_by_cohort",
                {},
            ),
            "cohort_overrides": statistical_overrides.get(
                "cohort_overrides",
                statistical_settings.get("cohorts", {}),
            ),
            "statistical_runtime_overrides": statistical_overrides,
        })
        # ``None`` = "I did not write state.json myself; route flips
        # phase to completed". See SimulationUseCase.run_simulation
        # docstring for the full state-authority contract.
        return None

    # ------------------------------------------------------------------
    # Optional sensitivity surface
    # ------------------------------------------------------------------

    def run_sensitivity(self, simulation_id: str, body: Any) -> Any:
        """Sensitivity sweep not supported for this use case.

        The Protocol cannot mark members optional in a
        ``@runtime_checkable`` way; raising ``NotImplementedError`` is
        the canonical opt-out signal the conformance suite recognises.
        """
        raise NotImplementedError(
            "creator does not implement run_sensitivity; the use case "
            "opts out via NotImplementedError per the conformance contract."
        )


# Module-level singleton. Repeated ``create_app()`` calls in the same
# process register the SAME instance -- the registry's idempotency
# contract treats that as a no-op. Constructing a fresh adapter on
# every boot would trip the "different instance under same id" branch.
CREATOR_USE_CASE: CreatorUseCase = (
    CreatorUseCase()
)


# Helpers exposed for test fixtures that need to compute deterministic
# hashes over a payload without re-implementing the policy
# ``scenario_hash`` / ``seed_hash`` derivation. Kept on the adapter
# module rather than the generator because they are caller-side
# helpers, not generator-internal.


def hash_scenario(scenario: CreatorScenario) -> str:
    """Return a deterministic 64-char sha256 of the scenario JSON.

    Used by fixtures to build a ``scenario_hash`` that matches the
    on-disk canonical serialisation. Schema-shape stable: re-runs of
    the same scenario yield the same digest.
    """
    payload = scenario.model_dump_json()
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def hash_seed_text(seed_text: str) -> str:
    """Return a deterministic 64-char sha256 of the seed text."""
    return hashlib.sha256(seed_text.encode("utf-8")).hexdigest()


__all__ = [
    "CreatorUseCase",
    "CREATOR_USE_CASE",
    "hash_scenario",
    "hash_seed_text",
]
```
