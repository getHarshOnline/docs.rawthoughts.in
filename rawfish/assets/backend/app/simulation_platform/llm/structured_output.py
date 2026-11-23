"""Strict JSON-Schema decode decorator.

:class:`StructuredOutputClient` wraps an :class:`LLMClientProtocol` and,
when the wrapped client advertises ``supports_json_schema=True``, asks
the provider for ``response_format={"type": "json_schema", ...}`` with
``strict=True`` semantics so the model output is forced to match a
caller-supplied schema. When the wrapped client does NOT advertise that
capability, this decorator is *transparent*: every ``chat_json`` call is
forwarded verbatim and the wrapped client's repair pipeline handles
parsing.

Why a wrapper and not a subclass: ``app.utils.llm_client`` and
``app.seam.llm_patches`` are protected. Inserting strict-schema support
is a *composition* layer on top of either, and must degrade silently
when stacked over a client whose provider does not support the feature.

The decorator preserves the :class:`LLMClientProtocol` shape so it can
be wrapped again (e.g. by :class:`AuditedLLMClient`).

Target-schema (Pydantic) mode
-----------------------------

In addition to the raw ``json_schema`` dict the decorator also accepts a
``target_schema`` Pydantic model class. When supplied:

  * The request body's ``json_schema`` is derived from
    ``target_schema.model_json_schema()`` (unless ``json_schema`` is
    also passed, in which case the raw dict wins -- giving callers an
    escape hatch for legacy schemas that diverge from the canonical
    model).
  * The parsed response is validated with
    ``target_schema.model_validate``. On
    :class:`pydantic.ValidationError`, the decorator re-calls the
    provider with a tail system message that quotes the validation
    error and asks for a corrected payload. Up to ``max_retries``
    (default 2) retries are issued; on the third failure (initial call
    + 2 retries) the :class:`pydantic.ValidationError` is re-raised so
    the caller can map it to its domain error code (the policy report
    route already maps Pydantic ValidationError to ``REPORT_CORRUPTED``).

Provider-error (transport / HTTP / model rejection) failures in the
strict-schema path continue to fall back to the wrapped client's
``chat_json`` (the wrapped client owns the repair pipeline and we MUST
not bypass it). Pydantic validation failures are NOT swallowed by that
fallback -- they drive the retry loop and ultimately re-raise, because
"the LLM produced a syntactically valid JSON object whose shape is
wrong" is exactly what the retry loop exists to handle.
"""
from __future__ import annotations

import json as _json
from typing import Any, Dict, List, Optional, Type

from pydantic import BaseModel, ValidationError

from .protocols import LLMCapabilities, LLMClientProtocol, UsageInfo, get_capabilities
from .security import assert_no_user_role_delimiter_injection


# Default maximum number of additional validation-retry calls. The first
# call does NOT count against this budget; a value of 2 means the
# decorator may issue up to 3 LLM calls (initial + 2 retries) before
# re-raising the final ValidationError.
_DEFAULT_MAX_VALIDATION_RETRIES: int = 2


# Tail-message template appended (as a ``system`` role entry) to the
# message list on each validation-retry call. The template includes the
# pydantic error verbatim so the model can map specific field paths to
# corrections. Wording is deliberately neutral product vocabulary so the
# banned-token guard never trips on these synthetic messages.
_RETRY_INSTRUCTION_TEMPLATE: str = (
    "Your previous response failed validation: {error}. "
    "Please return a corrected JSON conforming to the schema."
)


class StructuredOutputClient:
    """Strict JSON-Schema wrapper around an :class:`LLMClientProtocol`.

    Construction-time arguments:
      * ``wrapped`` -- the underlying client. MUST satisfy
        :class:`LLMClientProtocol` structurally.
      * ``json_schema`` -- optional schema dict the caller wants the
        provider to enforce. When omitted AND ``target_schema`` is also
        omitted, the decorator is a no-op forwarder regardless of
        capability flags.
      * ``target_schema`` -- optional Pydantic model class. When given,
        the request body's ``json_schema`` is derived via
        ``target_schema.model_json_schema()`` (unless ``json_schema``
        is also provided explicitly) AND the parsed response is
        validated with ``target_schema.model_validate``; validation
        failures drive a retry loop (see module docstring).
      * ``schema_name`` -- the ``name`` field required by the OpenAI
        ``response_format=json_schema`` contract. Defaults to
        ``"output"`` which matches the OpenAI examples.
      * ``max_validation_retries`` -- maximum number of EXTRA calls
        (beyond the initial call) the decorator issues to recover from
        Pydantic validation failures. Defaults to 2.

    Behaviour:
      * If no schema (neither ``json_schema`` nor ``target_schema``) is
        supplied, OR the wrapped client does not advertise
        ``supports_json_schema``, ``chat_json`` is a verbatim
        pass-through (the underlying client's existing JSON handling
        applies).
      * Otherwise, the decorator routes through the wrapped client's
        OpenAI ``client`` (when available) with the strict-schema
        ``response_format``. Provider-error (transport / HTTP / model-
        side rejection) failures fall back to the wrapped client's
        ``chat_json`` so a provider that silently rejects
        ``json_schema`` does not break the call. Pydantic
        :class:`ValidationError` failures DO NOT fall back -- they
        trigger the retry loop and ultimately re-raise on the third
        failure (initial + 2 retries by default).
    """

    def __init__(
        self,
        wrapped: LLMClientProtocol,
        *,
        json_schema: Optional[Dict[str, Any]] = None,
        target_schema: Optional[Type[BaseModel]] = None,
        schema_name: str = "output",
        max_validation_retries: int = _DEFAULT_MAX_VALIDATION_RETRIES,
    ) -> None:
        self._wrapped = wrapped
        self._target_schema = target_schema
        # When the caller supplies a Pydantic model but no raw dict,
        # derive the request-body schema from the model. The raw dict
        # takes precedence when both are passed so a caller can still
        # send a legacy or hand-tuned schema while keeping validation
        # against the canonical model.
        if json_schema is None and target_schema is not None:
            json_schema = target_schema.model_json_schema()
        self._schema = json_schema
        self._schema_name = schema_name
        if max_validation_retries < 0:
            raise ValueError(
                "max_validation_retries must be non-negative; got "
                f"{max_validation_retries!r}"
            )
        self._max_validation_retries = max_validation_retries
        # Per-call usage aggregator. The strict-schema branch can issue
        # up to ``1 + max_validation_retries`` actual provider calls;
        # writing each retry's ``response.usage`` to
        # ``self._wrapped.last_usage`` (a backward-compat slot the
        # seam client owns) OVERWRITES the previous retry, so an
        # outer auditor reading ``last_usage`` after the call sees
        # only the FINAL retry's tokens and under-counts spend on
        # any call that retried. This slot is the sum across every
        # retry the latest ``chat_json`` issued; the ``last_usage``
        # property below prefers it over the seam slot so an outer
        # :class:`AuditedLLMClient` reads the aggregate.
        self._last_call_usage: Optional[UsageInfo] = None

    # ------------------------------------------------------------------
    # Protocol surface (pass-through attributes)
    # ------------------------------------------------------------------

    @property
    def model(self) -> str:
        return self._wrapped.model

    @property
    def json_mode(self) -> str:
        return self._wrapped.json_mode

    @property
    def last_usage(self) -> Optional[UsageInfo]:
        """Per-call token spend.

        Prefers the per-call aggregate populated by the strict-schema
        branch (sum across every retry) and falls back to the seam
        client's ``last_usage`` slot when the strict-schema branch
        did not run (fallback path: ``self._schema is None`` or
        ``not caps.supports_json_schema``). The fallback path
        forwards to ``self._wrapped.chat_json`` which sets the seam
        slot itself, so reading the seam value there is correct.

        An outer :class:`AuditedLLMClient` reads this property to
        build the per-call :class:`LLMAuditEntry`. The aggregate
        value here is the load-bearing fix: without it, every
        strict-schema retry's tokens would be silently dropped from
        the audit trail and the cost summary would under-count.
        """
        if self._last_call_usage is not None:
            return self._last_call_usage
        return getattr(self._wrapped, "last_usage", None)

    @property
    def capabilities(self) -> LLMCapabilities:
        return get_capabilities(self._wrapped)

    def __getattr__(self, name: str) -> Any:
        # Forward unknown attribute reads onto the wrapped client so
        # decorator-aware callers (e.g.
        # :class:`app.services.policy.policy_report_generator.PolicyReportGenerator`,
        # which reads ``self._llm.policy_max_tokens_report``) see the
        # same surface they would on the bare seam client. Matches the
        # forwarding pattern used by :class:`AuditedLLMClient` so the
        # full decorator stack
        # ``Audited(StructuredOutput(PolicyLLMClient))``
        # exposes ``policy_max_tokens_report`` through both layers.
        #
        # ``__getattr__`` only fires when normal lookup fails, so the
        # decorator-internal state (``_wrapped``, ``_schema``, etc.) is
        # unaffected. Underscore-prefixed names are rejected explicitly
        # to keep partial-init paths from recursing forever.
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
        # Security preflight: reject any user-role message that
        # smuggles the ``</UNTRUSTED_USER_DOCUMENT>`` delimiter. The
        # wrapped seam client (:class:`PolicyLLMClient.chat_json`)
        # runs the SAME check, but the strict-schema branch below
        # bypasses ``chat_json`` and dispatches directly to the
        # upstream OpenAI client -- without the preflight here, a
        # delimiter-injection payload smuggled in via a free-form
        # scenario field would skip the guard entirely when the
        # provider advertises ``response_format=json_schema`` support.
        #
        # The shared :func:`assert_no_user_role_delimiter_injection`
        # function is the single source of truth so the two call
        # sites cannot drift; the platform conformance suite pins
        # that the same input rejected here is also rejected by the
        # seam client.
        assert_no_user_role_delimiter_injection(messages)

        # Reset the per-call usage accumulator BEFORE any branching.
        # The strict-schema branch below rebuilds it on each retry;
        # the fallback branches (no schema OR provider missing the
        # capability) leave it ``None`` and the ``last_usage`` property
        # falls through to the wrapped seam slot. Putting the reset
        # here (not inside the strict branch) prevents stale spend
        # from a previous strict call leaking into the audit entry
        # of a follow-on fallback call on the same decorator instance.
        self._last_call_usage = None

        caps = get_capabilities(self._wrapped)
        if self._schema is None or not caps.supports_json_schema:
            return self._wrapped.chat_json(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

        # Provider-supported strict-schema path. We reach through to the
        # wrapped client's OpenAI ``client`` so the request body carries
        # the ``response_format=json_schema`` payload. The wrapped
        # client's ``chat_json`` (with its repair pipeline) is the
        # fallback for *provider* errors only; Pydantic
        # ValidationErrors drive the retry loop instead.
        openai_client = getattr(self._wrapped, "client", None)
        if openai_client is None:
            return self._wrapped.chat_json(
                messages=messages,
                temperature=temperature,
                max_tokens=max_tokens,
            )

        response_format = {
            "type": "json_schema",
            "json_schema": {
                "name": self._schema_name,
                "schema": self._schema,
                "strict": True,
            },
        }

        # Mutable per-call message list. The retry loop appends a
        # synthetic system message containing the validation error so
        # the model can see exactly what to fix. We copy the caller's
        # list so successive retries layer on top of one another (the
        # model sees ALL prior failure messages, which is the only way
        # to discourage it from repeating the same mistake).
        working_messages: List[Dict[str, str]] = list(messages)

        # Reset the per-call usage accumulator at the START of every
        # logical call so the property ``last_usage`` reflects ONLY
        # this call's spend (not stale spend from an earlier call).
        # We rebuild the sum on each retry below.
        self._last_call_usage = None
        sum_tokens_in = 0
        sum_tokens_out = 0

        last_validation_error: Optional[ValidationError] = None
        # Total calls allowed = 1 (initial) + max_validation_retries.
        total_calls = 1 + self._max_validation_retries
        for attempt in range(total_calls):
            try:
                # Pass a shallow copy of the message list on each call
                # so the provider sees a per-call snapshot and a caller
                # inspecting kwargs from a fake / mock cannot observe
                # later mutations to ``working_messages``. The dict
                # entries themselves are not mutated by the retry loop;
                # only new ``system`` entries are appended.
                response = openai_client.chat.completions.create(
                    model=self._wrapped.model,
                    messages=list(working_messages),
                    temperature=temperature,
                    max_tokens=max_tokens,
                    response_format=response_format,
                )
            except Exception:
                # Provider-side failure (transport / HTTP / model
                # rejection). Defer to the wrapped client's
                # chat_json + repair pipeline. We do NOT retry the
                # strict-schema path because the provider has signaled
                # something the strict-schema route cannot recover from.
                return self._wrapped.chat_json(
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

            content = response.choices[0].message.content

            # Mirror the per-retry usage:
            #   1. Onto the wrapped client's ``last_usage`` slot so
            #      callers that inspect the client directly still see
            #      the latest retry.
            #   2. Accumulate into the per-call sum on this decorator,
            #      so the outer :class:`AuditedLLMClient` can read
            #      the AGGREGATE via ``self.last_usage`` and capture
            #      every retry's tokens in the persisted audit
            #      entry. Without the accumulator, an audit entry
            #      for a call that retried twice would record only
            #      the third (successful) retry's tokens and
            #      under-count the spend by ~2x.
            usage = getattr(response, "usage", None)
            if usage is not None:
                try:
                    attempt_tokens_in = int(
                        getattr(usage, "prompt_tokens", 0) or 0
                    )
                    attempt_tokens_out = int(
                        getattr(usage, "completion_tokens", 0) or 0
                    )
                except Exception:
                    attempt_tokens_in = 0
                    attempt_tokens_out = 0
                sum_tokens_in += attempt_tokens_in
                sum_tokens_out += attempt_tokens_out
                self._last_call_usage = UsageInfo(
                    tokens_in=sum_tokens_in,
                    tokens_out=sum_tokens_out,
                )
                if hasattr(self._wrapped, "last_usage"):
                    try:
                        self._wrapped.last_usage = UsageInfo(
                            tokens_in=attempt_tokens_in,
                            tokens_out=attempt_tokens_out,
                        )
                    except Exception:
                        # Never let usage bookkeeping abort a successful call.
                        pass

            try:
                parsed = _json.loads(content)
            except Exception:
                # The provider returned non-JSON despite the strict
                # schema. Treat as a provider-side failure and defer
                # to the wrapped client's repair pipeline (which is
                # exactly the situation the pipeline exists for).
                return self._wrapped.chat_json(
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                )

            # If no target Pydantic model was supplied, the decorator
            # cannot run shape validation -- return the parsed dict
            # immediately. The caller is responsible for any further
            # validation in that case (the legacy ``json_schema``-only
            # path falls here).
            if self._target_schema is None:
                return parsed

            try:
                # Validate the LLM's shape against the canonical model.
                # We return the parsed dict (not the model instance) so
                # the caller's downstream merge step (e.g.
                # PolicyReportGenerator) keeps owning the
                # provenance-merge contract and can call
                # ``Report.model_validate`` itself after the merge.
                self._target_schema.model_validate(parsed)
                return parsed
            except ValidationError as ve:
                last_validation_error = ve
                # If we have retries left, append the validation error
                # to the working message list as a synthetic system
                # message and re-issue the call. The next iteration of
                # the loop sees the augmented messages.
                if attempt < total_calls - 1:
                    working_messages.append({
                        "role": "system",
                        "content": _RETRY_INSTRUCTION_TEMPLATE.format(
                            error=str(ve),
                        ),
                    })
                    continue
                # Out of retries: re-raise so the caller maps it to its
                # domain error code (REPORT_CORRUPTED in the policy
                # report path).
                raise

        # Defensive: the loop body either returns on success, falls
        # back to chat_json on provider error, or re-raises on the
        # final ValidationError. The line below is unreachable; it
        # exists only so static type-checkers see a return on every
        # path.
        if last_validation_error is not None:
            raise last_validation_error
        return {}  # pragma: no cover


__all__ = ["StructuredOutputClient"]
