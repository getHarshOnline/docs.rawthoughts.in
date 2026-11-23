---
title: "backend/app/simulation_platform/registry.py"
noindex: true
---

```py
"""Module-level registry of :class:`SimulationUseCase` instances.

The registry is the single lookup the HTTP layer, frontend catalog,
and conformance suite share. It is intentionally a process-wide
singleton (a module-level dict) rather than an injected dependency:
the simulation platform composes use cases at import time, and
threading a registry object through every call site would buy nothing
but boilerplate.

Registration is idempotent: re-registering the same
``(use_case_id, instance)`` is a no-op, but registering a DIFFERENT
instance under an already-taken id raises :class:`ValueError`. That
asymmetry catches the genuine error mode (two use cases colliding on
the same id) while letting tests safely call :func:`register` more
than once.
"""
from __future__ import annotations

from typing import Any, Callable, Dict, List

from .use_case import SimulationUseCase


# Module-level mutable state -- a deliberate process-wide singleton.
# Tests that need isolation should snapshot+restore via the helpers in
# :mod:`tests_helpers`; per-call dependency injection is intentionally
# not offered here (see module docstring).
_REGISTRY: Dict[str, SimulationUseCase] = {}

#: Observers fired AFTER a successful new-id registration. Each
#: callback receives the freshly-registered ``use_case_id``. Used by
#: the auto-report watcher fleet to start a daemon for lanes that
#: register after the app factory ran. Test code that registers
#: throwaway adapters between cases SHOULD NOT install observers
#: here; they live for the life of the process.
_POST_REGISTER_OBSERVERS: List[Callable[[str], Any]] = []


def add_post_register_observer(
    observer: Callable[[str], Any],
) -> None:
    """Install ``observer`` to be called after every NEW registration.

    ``observer`` must accept a single positional ``use_case_id``
    argument. Observer exceptions are logged and dropped (the
    registration itself still succeeds). Idempotent: registering the
    same callable twice still only calls it once per registration.
    """
    if observer not in _POST_REGISTER_OBSERVERS:
        _POST_REGISTER_OBSERVERS.append(observer)

# Monotonic version counter bumped on every successful ``register``
# (and on the snapshot/restore helpers in :mod:`tests_helpers`). Cache
# layers above the registry use this as part of their cache key so a
# late-registered adapter invalidates the cache on the next request
# without forcing the cache layers to introspect ``_REGISTRY`` directly.
_REGISTRY_VERSION: int = 0


def registry_version() -> int:
    """Return the current registry-version counter.

    Bumped monotonically on every successful :func:`register` call.
    Cache layers can use this as a cheap invalidation key: a stable
    version means "no adapter registered since last time".
    """
    return _REGISTRY_VERSION


def register(uc: SimulationUseCase) -> None:
    """Register ``uc`` under its declared :meth:`use_case_id`.

    Idempotent on the exact same instance; raises :class:`ValueError`
    if a DIFFERENT instance is already registered under the same id.
    The id-collision branch is what protects against two unrelated
    use cases shipping with the same id and the second silently
    shadowing the first.

    Structural conformance is enforced at registration time. The
    :class:`SimulationUseCase` Protocol is ``@runtime_checkable`` and
    declares every method / attribute the dispatch layer reads
    (notably ``report_schema`` and ``guardrail_capabilities``).
    Registering a malformed adapter that fails ``isinstance(uc,
    SimulationUseCase)`` raises :class:`TypeError` here -- BEFORE
    the first request lands on a route that would otherwise see an
    ``AttributeError`` deep in dispatch. This pulls the failure mode
    forward to import time where it is easy to fix.
    """
    if not isinstance(uc, SimulationUseCase):
        # ``@runtime_checkable`` only validates method PRESENCE, not
        # signatures, but that is enough to catch the typical
        # "adapter forgot to declare X" mistake. The error message
        # names every required member so a contributor can fix the
        # adapter without grepping the Protocol definition.
        from .use_case import SimulationUseCase as _SUC
        required = sorted(getattr(_SUC, "__protocol_attrs__", set())) or [
            "use_case_id", "catalog", "validate_scenario",
            "rehydrate_scenario", "parse_seed",
            "load_presets", "build_ontology", "write_prepare_artifacts",
            "run_simulation", "generate_report", "artifact_names",
            "run_sensitivity", "report_schema", "guardrail_capabilities",
        ]
        present = sorted(name for name in required if hasattr(uc, name))
        missing = sorted(set(required) - set(present))
        raise TypeError(
            f"simulation_platform.register: {type(uc).__name__!r} does not "
            f"satisfy the SimulationUseCase Protocol; missing members: "
            f"{missing!r}; present: {present!r}"
        )

    uid = uc.use_case_id()
    existing = _REGISTRY.get(uid)
    if existing is not None and existing is not uc:
        raise ValueError(
            f"simulation_platform: use_case_id {uid!r} already registered "
            f"with a different instance"
        )
    is_new_registration = existing is None
    if is_new_registration:
        # New registration -- bump the version counter so cache layers
        # know the catalog payload may have changed. Idempotent
        # re-registration of the same instance does NOT bump (the
        # observable surface is identical).
        global _REGISTRY_VERSION
        _REGISTRY_VERSION += 1
    _REGISTRY[uid] = uc
    if is_new_registration:
        #: Notify post-register observers AFTER the registry mutation
        #: has landed. The auto-report watcher fleet uses this so a
        #: lane registered AFTER the app factory ran picks up its
        #: own watcher daemon without waiting for the next process
        #: restart. Each observer is best-effort: a raising observer
        #: is logged and dropped from this notification pass; the
        #: registration itself succeeds either way.
        for obs in list(_POST_REGISTER_OBSERVERS):
            try:
                obs(uid)
            except Exception:  # noqa: BLE001
                import logging
                logging.getLogger(
                    "rawfish.simulation_platform.registry",
                ).exception(
                    "post-register observer raised for use_case_id=%s",
                    uid,
                )


def get(use_case_id: str) -> SimulationUseCase:
    """Look up the registered use case by id.

    Raises :class:`KeyError` if ``use_case_id`` is unknown. Callers
    that want a soft lookup should catch the KeyError themselves --
    the registry intentionally does not return ``None`` so a missing
    id never silently propagates as an attribute error two layers
    later.
    """

    try:
        return _REGISTRY[use_case_id]
    except KeyError as exc:
        raise KeyError(
            f"simulation_platform: no use case registered for "
            f"use_case_id={use_case_id!r}"
        ) from exc


def list_use_cases() -> List[str]:
    """Return the registered use-case ids in registration order.

    Ordering matches insertion order (CPython dict guarantee since
    3.7); the frontend renders the use-case picker in this order so
    deterministic ordering matters even though the platform itself
    doesn't depend on it.
    """

    return list(_REGISTRY.keys())


__all__ = [
    "register",
    "registry_version",
    "get",
    "list_use_cases",
]
```
