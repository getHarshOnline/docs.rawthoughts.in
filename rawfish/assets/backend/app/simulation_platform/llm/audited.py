"""Per-call audit decorator.

:class:`AuditedLLMClient` wraps an :class:`LLMClientProtocol`. On every
``chat_json`` call it captures a typed
:class:`app.policy.run_metadata.LLMAuditEntry` and pushes it to a
pluggable :class:`AuditSink`. The wrapped client is NOT modified.

Captured fields:
  * ``call_id``    -- caller-supplied via constructor factory, or a
    fresh ``uuid4().hex`` per call when no factory is supplied.
  * ``model``      -- read from the wrapped client's ``.model``.
  * ``mode``       -- read from the wrapped client's ``.json_mode``;
    coerced into the typed ``Literal["loose","strict","off"]`` (with
    ``"loose"`` fallback for any out-of-spec value).
  * ``tokens_in`` / ``tokens_out`` -- read from the wrapped client's
    ``.last_usage`` after the call returns. Falls back to ``0`` when
    the wrapped client does not surface usage (the upstream OpenAI
    client may or may not populate it for every endpoint). When the
    wrapped client is a :class:`StructuredOutputClient` whose
    strict-schema retry loop ran more than once, ``.last_usage``
    returns the AGGREGATE token count summed across every retry
    (the per-call accumulator on that decorator) -- so a single
    audit entry per logical ``chat_json`` invocation faithfully
    records the TOTAL spend of that call without needing per-retry
    audit entries.
  * ``latency_ms`` -- wall-clock duration measured client-side.
  * ``phase``      -- constructor arg; one of the literals defined on
    :class:`LLMAuditEntry`.
  * ``timestamp``  -- ``datetime.now(timezone.utc)``.
  * ``error``      -- on exception, captured as a short string before
    the exception is re-raised.

Construction-time idempotency: wrapping an already-audited client
returns the same instance (no double-instrumentation). The class uses
``__new__`` to enforce this so two-layer construction in different
modules cannot accidentally compound.

Audit granularity
-----------------

This decorator records ONE :class:`LLMAuditEntry` per LOGICAL
``chat_json`` invocation. When the wrapped client is a
:class:`StructuredOutputClient` whose strict-schema branch retries on
:class:`pydantic.ValidationError`, that single logical call may
issue multiple actual provider requests under the hood. The audit
entry's ``tokens_in`` / ``tokens_out`` reflect the SUM across every
retry (via the per-call accumulator on the structured wrapper); the
``latency_ms`` reflects the end-to-end wall-clock of the whole call
chain.

Per-retry audit entries would conflate two concerns: "what did this
logical operation cost?" (the entry's natural granularity) vs "what
did each provider request cost?" (a different telemetry surface).
Cost summaries and timeline views consume the one-entry-per-call
shape; a future per-retry telemetry view would be an additive change
on the structured wrapper, NOT a re-granulation of this audit
stream.
"""
from __future__ import annotations

import time
import uuid
from datetime import datetime, timezone
from typing import Any, Callable, Dict, List, Optional, Protocol

from .audit_models import LLMAuditEntry
from .protocols import LLMClientProtocol, UsageInfo


_VALID_PHASES = frozenset(
    {"ontology", "profiles", "simulation", "report",
     "parse", "sensitivity", "other"}
)
_VALID_MODES = frozenset({"loose", "strict", "off"})


class AuditSink(Protocol):
    """Pluggable sink the audit decorator writes :class:`LLMAuditEntry` to.

    Tests substitute a list-backed sink; production wires
    :class:`app.simulation_platform.llm.audit_sink.RunMetadataAuditSink`.
    The sink MUST accept the entry by value (no further validation is
    done by the caller -- the entry has already been validated by
    Pydantic at construction).
    """

    def append(self, entry: LLMAuditEntry) -> None:
        ...


class AuditedLLMClient:
    """Audit decorator around an :class:`LLMClientProtocol`.

    Idempotent: ``AuditedLLMClient(AuditedLLMClient(c, sink, phase))``
    returns the inner instance unchanged -- the second construction
    does NOT add a second audit hop. This guarantees that two
    independent modules each wrapping a shared client cannot double-log.
    """

    # Protocol-satisfying attribute declarations. The actual values are
    # mirrored from the wrapped client via the per-call dispatch below;
    # declaring them here lets static type-checkers see that the
    # decorator structurally satisfies :class:`LLMClientProtocol` so a
    # caller can stack wrappers (e.g. AuditedLLMClient(AuditedLLMClient(...))).
    model: str
    json_mode: str
    last_usage: Optional[UsageInfo]

    def __new__(
        cls,
        wrapped: LLMClientProtocol,
        sink: "AuditSink",
        phase: str,
        *,
        call_id_factory: Optional[Callable[[], str]] = None,
        clock: Optional[Callable[[], datetime]] = None,
    ) -> "AuditedLLMClient":
        if isinstance(wrapped, AuditedLLMClient):
            # Construction-time idempotency: never double-instrument.
            return wrapped
        return super().__new__(cls)

    def __init__(
        self,
        wrapped: LLMClientProtocol,
        sink: "AuditSink",
        phase: str,
        *,
        call_id_factory: Optional[Callable[[], str]] = None,
        clock: Optional[Callable[[], datetime]] = None,
    ) -> None:
        # __new__ may have returned the already-audited wrapped instance.
        # In that case __init__ runs against the SAME object, so the
        # guard below avoids re-binding its fields (which would silently
        # replace the existing sink/phase with the new caller's values).
        if getattr(self, "_audited_initialised", False):
            return
        if phase not in _VALID_PHASES:
            raise ValueError(
                f"phase {phase!r} not in {sorted(_VALID_PHASES)}"
            )
        self._wrapped = wrapped
        self._sink = sink
        self._phase = phase
        self._call_id_factory = call_id_factory or (lambda: uuid.uuid4().hex)
        self._clock = clock or (lambda: datetime.now(timezone.utc))
        self._audited_initialised = True

    # ------------------------------------------------------------------
    # Protocol surface (pass-through attributes)
    # ------------------------------------------------------------------

    def __getattr__(self, name: str) -> Any:
        # Forward unknown attribute reads onto the wrapped client so
        # that ``model``, ``json_mode``, ``last_usage``, ``capabilities``
        # and any other protocol attribute is satisfied without
        # re-declaring each as a property here. ``__getattr__`` only
        # fires when normal lookup fails, so the audit-internal state
        # (``_wrapped``, ``_sink``, etc.) is unaffected. Audit-internal
        # underscore-prefixed names are rejected explicitly to keep a
        # half-constructed instance from recursing forever (the
        # ``__init__`` guard uses ``getattr(self, "_audited_initialised",
        # False)`` which would otherwise trip this path before
        # ``_wrapped`` is set).
        if name.startswith("_"):
            raise AttributeError(name)
        wrapped = self.__dict__.get("_wrapped")
        if wrapped is None:
            raise AttributeError(name)
        return getattr(wrapped, name)

    # ------------------------------------------------------------------
    # chat_json
    # ------------------------------------------------------------------

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ) -> Dict[str, Any]:
        call_id = self._call_id_factory()
        started = time.monotonic()
        err: Optional[BaseException] = None
        try:
            return self._wrapped.chat_json(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except BaseException as exc:  # noqa: BLE001 -- captured + re-raised
            err = exc
            raise
        finally:
            latency_ms = int((time.monotonic() - started) * 1000)
            usage = getattr(self._wrapped, "last_usage", None)
            tokens_in = int(usage.tokens_in) if isinstance(usage, UsageInfo) else 0
            tokens_out = int(usage.tokens_out) if isinstance(usage, UsageInfo) else 0
            raw_mode = getattr(self._wrapped, "json_mode", "loose") or "loose"
            mode = raw_mode if raw_mode in _VALID_MODES else "loose"
            entry = LLMAuditEntry(
                call_id=call_id,
                model=str(getattr(self._wrapped, "model", "unknown")),
                mode=mode,  # type: ignore[arg-type]
                tokens_in=tokens_in,
                tokens_out=tokens_out,
                latency_ms=latency_ms,
                phase=self._phase,  # type: ignore[arg-type]
                timestamp=self._clock(),
                error=(repr(err)[:200] if err is not None else None),
            )
            try:
                self._sink.append(entry)
            except Exception:
                # Audit failures MUST NOT mask the caller's real exception
                # (or success). The sink is best-effort from the
                # decorator's perspective; production sinks log their own
                # failures.
                pass


__all__ = ["AuditSink", "AuditedLLMClient"]
