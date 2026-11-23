---
title: "backend/app/simulation_platform/use_case.py"
noindex: true
---

```py
"""``SimulationUseCase`` Protocol -- the platform-boundary contract.

A "use case" is one product surface (policy stress, creator audience
reaction, etc.) that plugs into the simulation platform. Each use case
satisfies this Protocol structurally; the HTTP layer, frontend
catalog, and conformance tests depend on the Protocol -- never on a
concrete use case -- so a new use case can be registered without
editing the platform glue.

Return types for ``validate_scenario`` / ``parse_seed`` /
``generate_report`` / ``run_sensitivity`` are intentionally typed as
``Any`` at the Protocol boundary. The platform does not own those
schemas; each use case owns its own scenario, report, and sensitivity
shapes (Pydantic models in the use case's own module). Pinning a
concrete cross-use-case type here would force every use case to adopt
the first one's schema, which defeats the point of the seam. The
conformance tests assert the structural properties the platform
actually relies on (presence of a ``scenario_id``, a serialisable
report payload, etc.) without leaking those shapes into this module.

``artifact_names`` is the one explicit dictionary contract -- it maps
logical artifact ids (e.g. ``"report_json"``, ``"manifest"``) to the
file names the use case writes inside ``run_dir``. This is the only
hook the run-resolution layer needs to find a use case's artifacts on
disk without knowing the use case's filename conventions.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional, Protocol, runtime_checkable

from .catalog import CatalogPayload
from .guardrails import GuardrailCapabilities


@runtime_checkable
class SimulationUseCase(Protocol):
    """Structural contract every registered use case must satisfy.

    Methods are grouped by lifecycle phase:

    * Identity / metadata: :meth:`use_case_id`, :meth:`catalog`,
      :meth:`artifact_names`.
    * Authoring inputs: :meth:`validate_scenario`, :meth:`parse_seed`,
      :meth:`load_presets`.
    * Prepare phase (pre-run): :meth:`build_ontology`,
      :meth:`write_prepare_artifacts`, :attr:`prepare_manifest_schema`.
    * Run phase: :meth:`run_simulation`.
    * Report phase (post-run): :meth:`generate_report`,
      :attr:`report_schema`.
    * Sensitivity / surrogate-explainer surface: :meth:`run_sensitivity`.

    Structural conformance is checked at runtime via
    ``@runtime_checkable`` so the registry can ``isinstance``-dispatch
    incoming use cases when needed. The conformance test suite (see
    ``tests/simulation_platform/``) pins the per-method invariants.

    Opt-out signal: methods whose lane does not support them MUST
    raise :class:`NotImplementedError`. The generic dispatch layer
    surfaces those raises as ``501 CAPABILITY_UNSUPPORTED`` so a
    client can distinguish "lane chose not to expose this" from a
    transient runtime error.
    """

    guardrail_capabilities: Optional[GuardrailCapabilities]
    """Optional opt-in container for adapter-defined guardrail hooks.

    The base Protocol covers the routing / persistence / catalog
    surface every lane needs; the richer methodological guardrails
    (language contract, evidence binding, transparency flags,
    markdown render, advisory claim demotions) are lane-specific
    and live behind this opt-in. See
    :mod:`app.simulation_platform.guardrails` for the per-hook
    signatures.

    Adapters that have no guardrails wired set this to ``None``. The
    Protocol's structural check
    requires the attribute to exist on every registered adapter so
    a future dispatch-layer call site that reads it can do so
    without a defensive ``getattr``.
    """

    report_schema: Optional[type]
    """Optional Pydantic model class for read-side report validation.

    When set, the generic ``GET /api/sim/use-cases/<id>/simulation/<sim_id>/report``
    route validates the on-disk JSON via ``report_schema.model_validate``
    before returning it, so a corrupt-on-disk artifact surfaces as
    ``REPORT_CORRUPTED`` rather than passing through as raw JSON.

    Adapters that want validation set this to their report Pydantic
    class (e.g. ``Report`` for policy, ``CreatorReport`` for the
    creator surface). Adapters that have no canonical schema yet
    MUST set this to ``None`` explicitly so the attribute is always
    reachable -- the Protocol's structural check needs the attribute
    present even when no schema is wired.
    """

    report_draft_schema: Optional[type]
    """Optional Pydantic model class for the LLM-owned draft subset.

    When set, the generic ``/report/generate`` route and the
    auto-report watcher wrap the LLM through ``StructuredOutputClient``
    with ``target_schema=report_draft_schema`` -- the strict-mode
    JSON schema the provider enforces is the LLM-owned subset of
    the persisted :attr:`report_schema`, not the persisted shape
    itself. Adapters whose ``generate_report`` merges caller-owned
    provenance fields (header.persona/scope, simulation_id,
    scenario_hash, seed_hash, embedded run_metadata) into the LLM
    output before validating against the full :attr:`report_schema`
    set this to their draft model so the LLM is not asked to
    fabricate provenance the route is about to merge in itself.

    Adapters that have no draft / provenance-merge step (the LLM's
    output IS the persisted shape) leave this as ``None``; the
    structured-output wrapper falls back to :attr:`report_schema`
    in that case. The Protocol's structural check requires the
    attribute to exist on every registered adapter so the resolver
    can read it without a defensive ``getattr``.
    """

    adapter_runs_guardrails_internally: bool
    """Whether the adapter's ``generate_report`` runs its own guardrails.

    Adapters whose ``generate_report`` internally drives the full
    guardrail chain (evidence binding, advisory claim demotion,
    transparency-flag synthesis, markdown render, language-contract
    assertion) declare this as ``True``. The generic dispatch route
    and the auto-report watcher then SKIP the post-generate hook
    pipeline on ``adapter.guardrail_capabilities`` -- the hooks
    would re-run the same side effects (warnings, demotions) the
    adapter already applied, compounding them.

    ``build_evidence_catalog`` is NOT part of the skipped chain:
    it runs BEFORE the adapter call (as input to
    ``generate_report``) and the adapter consumes the catalog
    internally. Only the post-generate hooks
    (``run_advisory_claim_pass``, ``apply_transparency_flags``,
    ``render_markdown``, ``assert_render_contract``) are gated by
    this flag.

    Adapters whose ``generate_report`` returns a raw Report and
    relies on the dispatch layer to apply guardrails declare
    ``False`` -- the generic dispatch then runs every hook the
    adapter wired on its ``GuardrailCapabilities``.
    """

    prepare_manifest_schema: Optional[type]
    """Optional Pydantic model class for ``/prepare`` manifest validation.

    Mirrors :attr:`report_schema` on the write side: when set, the
    generic ``POST /api/sim/use-cases/<id>/simulation/<sim_id>/prepare``
    dispatch validates the on-disk ``artifact_manifest.json`` (the
    adapter's prepare-time output, captured under the artifact name
    declared by :meth:`artifact_names`) via
    ``prepare_manifest_schema.model_validate`` BEFORE the state.json
    transition lands. A corrupt or schema-drifted manifest surfaces
    as the canonical ``STATE_CORRUPTED`` / ``REPORT_CORRUPTED`` 500
    envelope rather than silently advancing the lifecycle.

    Adapters that want validation set this to their prepare-manifest
    Pydantic class. Adapters that have no canonical manifest schema
    yet MUST set this to ``None`` explicitly so the attribute is
    always reachable -- the Protocol's structural check needs the
    attribute present even when no schema is wired.
    """

    def use_case_id(self) -> str:
        """Return the stable identifier for this use case.

        Must be unique across registered use cases (the registry
        enforces this). The HTTP layer uses this as the URL path
        component for use-case-scoped endpoints.
        """
        ...

    def catalog(self) -> CatalogPayload:
        """Return the lane catalog used by cockpit setup and manifests.

        The payload supplies personas, cohorts, connector capabilities,
        report sections, and the lane manifest through one adapter-owned
        contract instead of hardcoded frontend options.
        """
        ...

    def validate_scenario(self, payload: Any) -> Any:
        """Validate an inbound scenario payload.

        Implementations typically run their Pydantic model's
        ``model_validate`` and return either the validated model or a
        structured error envelope. Return type stays ``Any`` so the
        platform doesn't pin a single envelope shape across use cases
        with different validation contracts.
        """
        ...

    def rehydrate_scenario(self, state_dict: Dict[str, Any]) -> Any:
        """Rebuild the scenario object from a persisted ``state.json`` dict.

        Called by the platform's state-machine layer when a
        ``create``-d simulation has to be revived (sensitivity
        sweeps, report generation, status lookups). The default
        contract:

          * ``state_dict`` is the full parsed ``state.json``; the
            scenario payload is conventionally stored under the
            ``"scenario"`` key.
          * The return value MUST be the same shape this adapter's
            :meth:`validate_scenario` produces (so the rehydrated
            object slots into every downstream use-case-typed code
            path without further coercion).
          * Lanes that need additional context (e.g. the policy
            scale-cap admittance flag) are responsible for reading
            their own per-call env / context inside this method;
            the Protocol does not thread a context channel.

        Adapters that do not yet ship a typed scenario can return
        ``state_dict["scenario"]`` unchanged (the fake use case in
        :mod:`app.simulation_platform.tests_helpers` does this).
        """
        ...

    def parse_seed(
        self,
        seed_text: str,
        stress_question: str,
        persona: str,
        scope: Optional[str],
    ) -> Any:
        """Parse free-form authoring input into a scenario draft.

        ``seed_text`` is the operator's situational description;
        ``stress_question`` is the hypothesis they want stressed;
        ``persona`` / ``scope`` come from the wizard's picker step.
        The return value is the use case's scenario-draft type --
        typically a partially-populated Pydantic model the operator
        can refine before submitting for a run.
        """
        ...

    def load_presets(self) -> List[Any]:
        """Return the use case's authored preset summaries.

        Each entry is a use-case-defined "preset summary" shape (id,
        label, short description, expected risk tags). The frontend
        renders these in the preset picker. Ordering is significant.
        """
        ...

    def build_ontology(self, scenario: Any, run_dir: Path) -> None:
        """Build the in-memory ontology object for ``scenario``.

        **Pure**: constructs the typed ``Ontology`` and returns. The
        audience-store side-effect (Graphiti / mock / cloud shim
        write keyed by the run id) is OWNED BY THE HTTP ROUTE LAYER
        today, not by this adapter method, because the seam-client
        construction depends on per-request env. A generic
        registry-dispatched route MUST therefore drive the
        audience-store write itself; calling this method does NOT
        update the store.

        ``run_dir`` is the per-run scratch directory; today's
        adapters do not persist the ontology to disk from this
        method (the prepare artifacts writer handles that path).

        Returns ``None`` because the Protocol does not commit to a
        concrete ontology shape (each use case owns its own).
        Callers that need the constructed ontology back must invoke
        the underlying loader directly.
        """
        ...

    def write_prepare_artifacts(self, scenario: Any, run_dir: Path) -> Any:
        """Write the prepare-phase artifacts to ``run_dir``.

        Examples: cohort priors JSON, ontology JSON, persona-defaults
        JSON. Returns an artifact-manifest shape (use-case-defined --
        typically a Pydantic model listing ``{logical_id: relative
        path}``) the run-resolution layer indexes to find these files
        later.
        """
        ...

    # Dual-port note: an adapter MAY additionally expose ``async``
    # variants of :meth:`run_simulation` and :meth:`generate_report`
    # under the names ``async_run_simulation`` and
    # ``async_generate_report``. These are NOT declared on the
    # Protocol (so they remain optional and adapters that have no
    # async path are not forced to ``raise NotImplementedError``
    # boilerplate). The generic dispatcher's invocation seam
    # (:func:`invoke_lane_run_simulation` /
    # :func:`invoke_lane_generate_report` in this module) probes
    # for the async method first and falls back to the sync one.
    # Lanes that opt into the async path release the request thread
    # while the call is in flight; lanes that stay sync run the
    # sync path unchanged.

    def run_simulation(self, scenario: Any, run_dir: Path) -> Optional[str]:
        """Drive the simulation kernel for ``scenario`` under ``run_dir``.

        Called by the generic ``POST .../simulation/<sim_id>/start``
        dispatch route AFTER ``write_prepare_artifacts`` has written
        the prepare manifest. The adapter owns the runner contract --
        subprocess management, deterministic-mock semantics,
        provider failover -- and writes ``run_state.json`` (the
        terminal-marker file the run-resolution layer reads back) by
        the time it returns.

        Return value (state-authority signal):

          * ``None`` -- the adapter has NOT written a terminal status
            to ``state.json``. The generic route flips
            ``state["phase"] = "completed"`` once this method returns
            without raising (creator deterministic-mock path).
          * A string (``running`` / ``completed`` / ``failed``) -- the
            adapter (or a service it delegates to) already wrote
            authoritative state. The generic route MUST mirror this
            value into the dispatch ``phase`` field instead of
            flipping to ``completed`` -- otherwise ``/status`` lies
            about in-flight runs. Policy returns ``"running"`` because
            its service writes ``state["status"] = "running"`` before
            returning (subprocess in flight).

        Raises:

          * :class:`NotImplementedError` -- the lane opts out of
            generic dispatch entirely. The route surfaces
            ``CAPABILITY_UNSUPPORTED`` (501).
          * Any other exception -- the route surfaces
            ``RUNNER_START_FAILED`` (502). Lanes that have their own
            scale-guard refusal type re-raise as
            :class:`app.simulation_platform.scale_guard.PlatformScaleGuardRefused`
            so the route can map to ``SCALE_GUARD_EXCEEDED`` (400)
            with structured details instead of the broad 502.
        """
        ...

    def generate_report(
        self,
        scenario: Any,
        run_metadata: Any,
        evidence_catalog: Any,
        llm_client: Any = None,
    ) -> Any:
        """Produce the use case's final report artifact **in-memory**.

        Called after the simulation completes. Returns a validated
        report Pydantic model (the use case's own type).

        **NOT a persist call.** This method runs the
        ``generate``-only path; the artifact is NOT written to disk
        and the run's metadata is NOT refreshed. A generic
        registry-dispatched route that wants persisted artifacts must
        either:

          * call this method then write the result + refresh
            ``run_metadata.json`` itself, OR
          * invoke the use case's own persist helper directly (e.g.
            ``PolicyReportGenerator.generate_and_persist``) -- which
            the policy HTTP route does today.

        ``run_metadata`` is the cross-use-case run record (start /
        end timestamps, ensemble config, LLM audit summary);
        ``evidence_catalog`` is the per-claim evidence binding
        produced during the run.

        ``llm_client`` is an optional pre-constructed LLM client
        (typically :class:`AuditedLLMClient` wrapping a
        :class:`StructuredOutputClient` or lane-specific seam). The
        adapter MUST use this client when non-None so the caller's
        audit sink + structured-output wrapping are exercised. When
        ``None`` the adapter constructs its own client from env.
        """
        ...

    def artifact_names(self) -> Dict[str, str]:
        """Return the ``{logical_id: filename}`` artifact map.

        Examples::

            {
                "report_json": "policy_report.json",
                "manifest": "artifact_manifest.json",
                "ontology": "ontology.json",
            }

        The run-resolution layer joins each filename onto the run
        directory to locate artifacts; the use case is the single
        source of truth for its own filenames.
        """
        ...

    def run_sensitivity(
        self,
        simulation_id: str,
        body: Any,
    ) -> Any:
        """Optional: run a post-hoc sensitivity sweep on a completed run.

        Use cases that do not support sensitivity should still expose
        this method (Protocols cannot mark members optional in a way
        ``@runtime_checkable`` enforces) but raise
        :class:`NotImplementedError` -- conformance tests treat that
        as the "not supported" signal. ``body`` carries the
        per-use-case sweep request shape; the return value is the
        per-use-case sensitivity report shape.
        """
        ...


def invoke_lane_run_simulation(
    adapter: "SimulationUseCase",
    scenario: Any,
    run_dir: Path,
) -> Optional[str]:
    """Drive an adapter's ``run_simulation`` through the dual-port seam.

    Probes the adapter for an ``async_run_simulation`` method. When
    present, drives it via :func:`asyncio.run` and returns when the
    coroutine resolves; otherwise falls through to the sync
    :meth:`run_simulation` directly.

    Return contract (state-authority signal):

      * ``None`` -- the adapter did NOT write a terminal status to
        ``state.json``. The generic route OWNS the post-handoff
        ``state["phase"] = "completed"`` transition (this is the
        deterministic in-process path the creator lane takes today:
        the call returns once the deterministic mock has finished, so
        the route legitimately flips the lifecycle to ``completed``).
      * A string -- the adapter (or the service it delegates to)
        already wrote authoritative state. The string is the
        persisted lifecycle status (``running`` while a subprocess is
        in flight, or ``completed`` / ``failed`` when synchronous
        terminal state landed). The route MUST NOT override this with
        ``completed``; it mirrors the value into the dispatch
        ``phase`` field instead so ``/status`` reads the truthful
        on-disk state.

    Threading caveat: under sync Flask/Gunicorn, ``asyncio.run``
    BLOCKS the calling request thread until the coroutine completes
    -- the dual-port seam does NOT release the Gunicorn worker. The
    async variant pays off when the adapter performs concurrent I/O
    INTERNALLY (e.g. fan-out via ``asyncio.gather``); the wall-clock
    win comes from inside the coroutine, not from giving the worker
    back. The seam ALSO lets an ASGI route (Quart, FastAPI mount,
    or a background job worker) await the adapter directly and get
    real worker-release behavior in that environment.

    Opt-out + failure mapping is unchanged across both variants:
    ``NotImplementedError`` from either propagates so the route
    layer can surface ``CAPABILITY_UNSUPPORTED`` (501); any other
    exception surfaces as ``RUNNER_START_FAILED`` (502).
    """
    async_fn = getattr(adapter, "async_run_simulation", None)
    if async_fn is not None and callable(async_fn):
        import asyncio
        from typing import Coroutine, cast
        coro = cast(
            Coroutine[Any, Any, Optional[str]], async_fn(scenario, run_dir),
        )
        return asyncio.run(coro)
    return adapter.run_simulation(scenario, run_dir)


def invoke_lane_generate_report(
    adapter: "SimulationUseCase",
    scenario: Any,
    run_metadata: Any,
    evidence_catalog: Any,
    llm_client: Any = None,
) -> Any:
    """Drive an adapter's ``generate_report`` through the dual-port seam.

    Mirrors :func:`invoke_lane_run_simulation` for the report-phase
    surface. Probes for ``async_generate_report``; when present,
    drives it via :func:`asyncio.run` and returns the resolved
    result. Same threading caveat: under sync Flask/Gunicorn the
    request thread is BLOCKED until the coroutine completes; the
    real wall-clock win comes from concurrent I/O INSIDE the
    coroutine (e.g. fanning out multiple LLM calls via
    ``asyncio.gather``), not from releasing the worker.
    """
    async_fn = getattr(adapter, "async_generate_report", None)
    if async_fn is not None and callable(async_fn):
        import asyncio
        from typing import Coroutine, cast
        coro = cast(
            Coroutine[Any, Any, Any],
            async_fn(
                scenario=scenario,
                run_metadata=run_metadata,
                evidence_catalog=evidence_catalog,
                llm_client=llm_client,
            ),
        )
        return asyncio.run(coro)
    return adapter.generate_report(
        scenario=scenario,
        run_metadata=run_metadata,
        evidence_catalog=evidence_catalog,
        llm_client=llm_client,
    )


__all__ = [
    "SimulationUseCase",
    "invoke_lane_run_simulation",
    "invoke_lane_generate_report",
]
```
