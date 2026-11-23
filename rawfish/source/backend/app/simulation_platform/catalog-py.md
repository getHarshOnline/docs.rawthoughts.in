---
title: "backend/app/simulation_platform/catalog.py"
noindex: true
---

```py
"""Catalog data shapes exposed by the simulation-platform boundary.

A "catalog" is the persona / cohort metadata a registered use case
publishes to its callers (HTTP layer, frontend wizard, conformance
tests). Keeping this shape on the platform side -- not inside any one
use case -- lets the frontend consume a single normalized payload no
matter which use case is registered.

:class:`PersonaSpec` describes one persona option a user can pick at the
top of a wizard: how to label it, what cohort question to ask, which
scopes are valid, and the segment-type allowlist per scope. Defaults
are a free-form dict so a use case can ship trait/prior templates
without leaking its internal Pydantic types through the platform
boundary.

:class:`CatalogPayload` is the aggregate envelope: ``use_case_id`` plus
the list of :class:`PersonaSpec` rows. Both models use
``extra='forbid'`` so a typo at the publication boundary surfaces
immediately rather than silently dropping data the frontend was
expecting.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field, model_validator


def _strict_config() -> ConfigDict:
    """Strict model config used by every platform-boundary data shape.

    ``extra='forbid'`` is the load-bearing knob: at the platform seam a
    silently-dropped key would mean the frontend receives partial
    metadata and the user never knows. ``populate_by_name`` is on for
    parity with the rest of the codebase's Pydantic configs.
    """

    return ConfigDict(
        populate_by_name=True,
        extra="forbid",
    )


class PersonaSpec(BaseModel):
    """One persona option published by a use case.

    Attributes
    ----------
    persona_id
        Stable identifier the frontend and API both reference (e.g.
        ``"creator"``, ``"policy"``). Lowercase ASCII conventionally,
        though the platform does not enforce the shape -- the use case
        owns its own id namespace.
    label
        Human-readable label rendered in the wizard's persona picker.
    cohort_question
        The question shown to the operator immediately after they pick
        this persona (e.g. "Who is your audience?" for creators).
    scopes
        Optional ordered list of scope tags valid for this persona.
        ``None`` means "this persona has no scope dimension"; an empty
        list would mean "scope is required but no values are
        published", which is almost certainly a misconfiguration --
        callers should treat ``None`` and ``[]`` distinctly.
    segment_types_by_scope
        For each scope (or the sentinel ``None`` key when scope is
        absent), the list of segment-type strings valid for
        ``AudienceSegment.type``. The frontend uses this to populate
        the segment-type dropdown without hardcoding the allowlist.
    defaults
        Free-form bag of per-persona defaults (trait templates, prior
        templates, narrative knobs). Kept untyped at the platform
        boundary so a new use case can publish whatever its wizard
        needs without expanding this surface.
    report_sections_by_scope
        For each scope (or ``None``), the ordered list of report
        section ids the use case produces. The frontend renders the
        report's table-of-contents from this list rather than guessing
        from the rendered HTML.
    """

    model_config = _strict_config()

    persona_id: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    cohort_question: str = Field(..., min_length=1)
    # Identity of the registered use case this persona belongs to.
    # Authors may leave it ``None`` at construction time when the spec
    # is being placed inside a :class:`CatalogPayload`; the envelope's
    # post-validator backfills the field from its own ``use_case_id``
    # so every downstream consumer sees a fully self-describing row.
    # Specs constructed outside an envelope (e.g. ad-hoc fixtures,
    # debug logs) SHOULD set this explicitly so the row stays
    # identifiable on its own.
    use_case_id: Optional[str] = Field(default=None)
    # ``scopes=None`` and ``scopes=[]`` carry distinct meanings (see
    # docstring) so we keep Optional[list] rather than collapsing to a
    # default-empty list.
    scopes: Optional[List[str]] = Field(default=None)
    segment_types_by_scope: Dict[Optional[str], List[str]] = Field(
        default_factory=dict
    )
    defaults: Dict[str, Any] = Field(default_factory=dict)
    report_sections_by_scope: Dict[Optional[str], List[str]] = Field(
        default_factory=dict
    )


class LaneManifest(BaseModel):
    """Cockpit-facing manifest every RawFish lane publishes.

    The backend keeps this model intentionally compact: it validates the
    fields the cockpit and platform gates need to trust, while allowing
    lane-owned slot payloads to grow without changing the platform package
    for every UI iteration.
    """

    model_config = ConfigDict(
        populate_by_name=True,
        extra="allow",
    )

    lane_id: str = Field(..., min_length=1)
    label: str = Field(..., min_length=1)
    summary: str = Field(..., min_length=1)
    cockpit_slots: List[str] = Field(default_factory=list)
    eval_instruments: Dict[str, Any] = Field(default_factory=dict)
    connector_capabilities: List[Dict[str, Any]] = Field(default_factory=list)
    report_sections: List[Dict[str, Any]] = Field(default_factory=list)
    analysis_panels: Dict[str, Any] = Field(default_factory=dict)
    statistical_manifest_path: str = Field(
        default="statistical.manifest.json",
        min_length=1,
    )


def build_minimal_lane_manifest(
    *,
    lane_id: str,
    label: str,
    summary: str,
    report_sections: Optional[List[str]] = None,
    provider_modes: Optional[List[str]] = None,
    analysis_panels: Optional[Dict[str, Any]] = None,
) -> LaneManifest:
    """Create a cockpit manifest shared by backend adapters.

    The lane-owned JSON manifest under ``frontend/src/lanes`` is the richer
    product source. This helper loads it when present, then fills any backend
    defaults needed by tests or non-frontend callers.
    """

    modes = provider_modes or [
        "local_ollama",
        "local_openai_compatible",
        "external",
    ]
    sections = [
        {"id": section.lower().replace(" ", "_"), "label": section}
        for section in (report_sections or ["Summary"])
    ]
    payload: Dict[str, Any] = {}
    manifest_path = (
        Path(__file__).resolve().parents[3]
        / "frontend"
        / "src"
        / "lanes"
        / lane_id
        / "lane_manifest.json"
    )
    if manifest_path.is_file():
        try:
            loaded = json.loads(manifest_path.read_text(encoding="utf-8"))
            if isinstance(loaded, dict):
                payload.update(loaded)
        except (OSError, json.JSONDecodeError):
            payload = {}
    payload.update({
        "lane_id": lane_id,
        "label": label,
        "summary": summary,
    })
    payload.setdefault("cockpit_slots", [
            "launch_tile",
            "smart_console",
            "scenario_ribbon",
            "scenario_editor",
            "cohort_graph",
            "preflight_meter",
            "boot_sequence",
            "run_timeline",
            "monitor_console",
            "report_header_bar",
            "report_renderer",
            "claim_cards",
            "evidence_rail",
            "interview_chat",
            "analysis_compare_panel",
            "statistical_workbench_inline_editor",
            "statistical_workbench_override_badge",
            "statistical_workbench_provenance_chip",
            "statistical_workbench_validity_strip",
            "statistical_workbench_variant_strip",
            "statistical_workbench_impact_tooltip",
            "statistical_workbench_preflight_meter",
            "statistical_workbench_drift_subpanel",
            "statistical_workbench_salt_seed_panel",
            "statistical_workbench_priors_attach_panel",
            "statistical_workbench_active_hours_grid",
            "statistical_workbench_manifest_chip",
        ])
    payload.setdefault("eval_instruments", {
            "readiness_checklist": [
                {
                    "id": "stress_question",
                    "label": "stress question",
                    "validator_key": "non_empty",
                },
                {
                    "id": "min_one_segment",
                    "label": "at least one segment",
                    "validator_key": "segments_count_gte_1",
                },
            ],
            "cost_preflight": {
                "default_ensemble_n": 5,
                "default_rounds": 16,
                "budget_cap": 500,
                "provider_modes": modes,
                "provider_selection_scope": "per_run",
                "external_budget": {"currency": "USD", "warn_at": 1.00},
            },
        })
    payload.setdefault("connector_capabilities", [])
    payload.setdefault("report_sections", sections)
    payload.setdefault("analysis_panels", analysis_panels or {
            "compare": {"enabled": True},
            "counterfactual": {"enabled": False},
            "sensitivity": {"enabled": False},
        })
    return LaneManifest.model_validate(payload)


class CatalogPayload(BaseModel):
    """Aggregate envelope returned by :meth:`SimulationUseCase.catalog`.

    ``use_case_id`` echoes :meth:`SimulationUseCase.use_case_id` so a
    consumer that fans out across multiple registered use cases can
    keep them straight without threading the id separately.
    ``personas`` is the ordered persona list -- order is significant
    because the frontend renders the wizard's persona picker in this
    order.
    """

    model_config = _strict_config()

    use_case_id: str = Field(..., min_length=1)
    lane_manifest: LaneManifest
    personas: List[PersonaSpec] = Field(default_factory=list)

    @model_validator(mode="after")
    def _backfill_and_check_persona_use_case_id(self) -> "CatalogPayload":
        """Stamp envelope ``use_case_id`` onto every persona row.

        Two invariants:

        1. Backfill: any :class:`PersonaSpec` constructed without an
           explicit ``use_case_id`` inherits the envelope's id, so
           every persona that leaves this validator is self-describing.
           This is the common-case ergonomic for use-case authors --
           they pass ``use_case_id`` once at the envelope and the
           per-row redundancy is handled mechanically.
        2. Consistency: a :class:`PersonaSpec` constructed with an
           explicit ``use_case_id`` MUST match the envelope's id. A
           mismatch (a foreign persona placed in the wrong envelope)
           surfaces as a ValidationError rather than silently
           propagating downstream.
        """

        if self.lane_manifest.lane_id != self.use_case_id:
            raise ValueError(
                f"lane_manifest.lane_id={self.lane_manifest.lane_id!r} "
                f"must match CatalogPayload(use_case_id={self.use_case_id!r})"
            )

        for spec in self.personas:
            if spec.use_case_id is None:
                spec.use_case_id = self.use_case_id
            elif spec.use_case_id != self.use_case_id:
                raise ValueError(
                    f"PersonaSpec(persona_id={spec.persona_id!r}) declares "
                    f"use_case_id={spec.use_case_id!r} but is hosted in "
                    f"CatalogPayload(use_case_id={self.use_case_id!r}); "
                    f"a persona spec cannot live inside the wrong envelope"
                )
        return self


__all__ = [
    "LaneManifest",
    "PersonaSpec",
    "CatalogPayload",
    "build_minimal_lane_manifest",
]
```
