"""Policy-path LLM client hardening (seam wrapper).

:class:`PolicyLLMClient` subclasses ``app.utils.llm_client.LLMClient`` and
adds: a two-tier ``chat_json`` (Tier 1 forces ``response_format=json_object``,
Tier 2 -- only when ``LLM_JSON_MODE`` is not ``strict`` -- runs a 5-stage
repair pipeline); rejection of
delimiter-injection payloads (``</UNTRUSTED_USER_DOCUMENT>``) in
user-role content; and a single ``_chat_internal`` indirection so tests
can mock without patching the provider router.
"""
from __future__ import annotations

import os
import re
import json
from typing import Any, Dict, List, Optional

from app.simulation_platform.llm.protocols import LLMCapabilities
from app.utils.llm_client import LLMClient
from app.utils.logger import get_logger


logger = get_logger('rawfish.seam.llm')


def _read_bool_env(name: str, default: bool = False) -> bool:
    """Read a truthy/falsy env var. ``"1"``, ``"true"``, ``"yes"``, ``"on"``
    (case-insensitive) -> ``True``; everything else -> ``False``. Missing /
    empty falls back to ``default``.
    """
    raw = os.getenv(name)
    if raw is None or raw == "":
        return default
    return raw.strip().lower() in {"1", "true", "yes", "on"}


# ---------------------------------------------------------------------------
# Exception surface
# ---------------------------------------------------------------------------


class LLMJSONParseError(Exception):
    """Raised when an LLM response cannot be parsed as JSON after all repair stages.

    The raw payload is truncated to 500 characters and stored on ``self.excerpt``
    for debugging. ``__repr__`` / ``__str__`` deliberately do NOT include the
    excerpt so that tracebacks and logs cannot leak sensitive content. Use
    ``self.excerpt`` directly when payload inspection is required.
    """

    def __init__(self, excerpt: str = ''):
        # Cap at 500 chars; never pass excerpt to super().__init__ — that would
        # surface the payload via the default ``args`` tuple.
        self.excerpt = excerpt[:500]
        super().__init__()

    def __repr__(self) -> str:  # noqa: D401
        return f"LLMJSONParseError(excerpt_len={len(self.excerpt)})"

    def __str__(self) -> str:
        return f"LLMJSONParseError(excerpt_len={len(self.excerpt)})"

    def __reduce__(self):
        # Pickling path: rebuild with an EMPTY excerpt so that pickled
        # tracebacks (e.g. multiprocessing logs) never leak the payload.
        return (LLMJSONParseError, ('',))


# ---------------------------------------------------------------------------
# Env helpers
# ---------------------------------------------------------------------------


_VALID_JSON_MODES = {'strict', 'loose', 'off'}


def _read_float_env(name: str, default: float) -> float:
    raw = os.getenv(name)
    if raw is None or raw == '':
        return default
    try:
        return float(raw)
    except (TypeError, ValueError):
        logger.warning(
            "env var %s could not be parsed as float (got %r); using default %r",
            name, raw, default,
        )
        return default


def _read_int_env(name: str, default: int) -> int:
    raw = os.getenv(name)
    if raw is None or raw == '':
        return default
    try:
        return int(raw)
    except (TypeError, ValueError):
        logger.warning(
            "env var %s could not be parsed as int (got %r); using default %r",
            name, raw, default,
        )
        return default


# ---------------------------------------------------------------------------
# Balanced-brace extraction (Stage 4 helper)
# ---------------------------------------------------------------------------


def _extract_balanced(text: str) -> Optional[str]:
    """Return the first balanced ``{...}`` or ``[...]`` substring in ``text``.

    Walks character-by-character tracking string-literal state so that braces
    inside double-quoted strings (e.g. ``{"x": "}"}``) do not break the depth
    counter. Returns ``None`` if no balanced structure is found.
    """
    if not text:
        return None

    # Find the first '{' or '[' and pin our matching close char.
    start = -1
    open_char = ''
    close_char = ''
    for i, ch in enumerate(text):
        if ch == '{':
            start = i
            open_char, close_char = '{', '}'
            break
        if ch == '[':
            start = i
            open_char, close_char = '[', ']'
            break
    if start == -1:
        return None

    depth = 0
    in_string = False
    escape_next = False
    for i in range(start, len(text)):
        ch = text[i]
        if escape_next:
            escape_next = False
            continue
        if in_string:
            if ch == '\\':
                escape_next = True
            elif ch == '"':
                in_string = False
            continue
        # Not in a string literal.
        if ch == '"':
            in_string = True
            continue
        if ch == open_char:
            depth += 1
        elif ch == close_char:
            depth -= 1
            if depth == 0:
                return text[start:i + 1]
    return None


# ---------------------------------------------------------------------------
# PolicyLLMClient
# ---------------------------------------------------------------------------


class PolicyLLMClient(LLMClient):
    """Hardened ``LLMClient`` subclass for policy-path LLM calls.

    Adds:
      * Provider transport inherited from the RawFish router-backed
        ``LLMClient``.
      * ``LLM_JSON_MODE``-gated two-tier ``chat_json`` (response_format ->
        repair fallback).
      * 5-stage JSON repair pipeline via ``_parse_llm_json``.
      * Delimiter-injection guard on user-role content.

    The base ``LLMClient`` is not modified.
    """

    def __init__(
        self,
        api_key: Optional[str] = None,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
    ):
        super().__init__(api_key=api_key, base_url=base_url, model=model)

        # --- env config --------------------------------------------------
        raw_mode = (os.getenv('LLM_JSON_MODE') or 'loose').strip().lower()
        if raw_mode not in _VALID_JSON_MODES:
            logger.warning(
                "LLM_JSON_MODE=%r is invalid; falling back to 'loose' (valid: %s)",
                raw_mode, sorted(_VALID_JSON_MODES),
            )
            raw_mode = 'loose'
        self.json_mode: str = raw_mode

        self.timeout_seconds: float = _read_float_env('LLM_TIMEOUT_SECONDS', 60.0)
        self.max_retries: int = _read_int_env('LLM_MAX_RETRIES', 2)
        self.policy_max_tokens_ontology: int = _read_int_env(
            'POLICY_MAX_TOKENS_ONTOLOGY', 8192,
        )
        self.policy_max_tokens_report: int = _read_int_env(
            'POLICY_MAX_TOKENS_REPORT', 16384,
        )

        # --- platform capability advertisement ----------------------------
        # The simulation_platform.llm wrappers (notably
        # :class:`StructuredOutputClient`) probe this attribute to decide
        # whether the provider supports
        # ``response_format={"type": "json_schema", ...}`` with
        # ``strict=True`` semantics. The flag is env-gated
        # (``LLM_SUPPORTS_JSON_SCHEMA=true``) so operators can opt into
        # the strict-decode path without code edits, and so unit tests
        # default to the conservative ``False`` setting (which keeps the
        # decorator transparent and preserves the existing repair
        # pipeline). Unknown providers default to ``False``.
        self.capabilities: LLMCapabilities = LLMCapabilities(
            supports_json_schema=_read_bool_env(
                'LLM_SUPPORTS_JSON_SCHEMA', default=False,
            ),
        )

    # ------------------------------------------------------------------
    # Single mockable LLM call site
    # ------------------------------------------------------------------

    def _chat_internal(
        self,
        messages: List[Dict[str, str]],
        temperature: float,
        max_tokens: int,
        response_format: Optional[Dict[str, Any]],
    ) -> str:
        """Thin wrapper around inherited ``chat`` -- the single LLM call site.

        Tests mock this method instead of patching the provider router so that
        Tier-1 / Tier-2 branching is exercised deterministically.
        """
        return self.chat(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format=response_format,
        )

    # ------------------------------------------------------------------
    # JSON repair pipeline
    # ------------------------------------------------------------------

    def _parse_llm_json(self, raw: str):
        """Parse ``raw`` as JSON, repairing common LLM output defects.

        Stages (in order):

          1. Markdown fence strip (byte-identical to upstream regex).
          2. Strict ``json.loads``.
          3. ``JSONDecoder().raw_decode`` from the first ``{`` or ``[``.
          4. Balanced-brace extraction respecting string literals.
          5. Control-char strip + trailing-comma repair, then ``json.loads``.

        Raises ``LLMJSONParseError`` with a 500-char excerpt on final failure.
        """
        # Whitespace-only -> immediate fail.
        if raw.strip() == '':
            raise LLMJSONParseError(raw[:500])

        # --- Stage 1: markdown fence strip -----------------------------
        # Patterns are byte-identical to upstream llm_client.py:95-96.
        stripped = raw.strip()
        stripped = re.sub(
            r'^```(?:json)?\s*\n?', '', stripped, flags=re.IGNORECASE,
        )
        stripped = re.sub(r'\n?```\s*$', '', stripped)
        stripped = stripped.strip()

        if stripped == '':
            raise LLMJSONParseError(raw[:500])

        # --- Stage 2: strict json.loads --------------------------------
        try:
            return json.loads(stripped)
        except (json.JSONDecodeError, ValueError):
            pass

        # --- Stage 3: JSONDecoder.raw_decode (prose-wrapped) -----------
        try:
            first_obj = stripped.find('{')
            first_arr = stripped.find('[')
            candidates = [i for i in (first_obj, first_arr) if i != -1]
            if candidates:
                idx = min(candidates)
                decoder = json.JSONDecoder()
                obj, _ = decoder.raw_decode(stripped[idx:])
                return obj
        except (json.JSONDecodeError, ValueError):
            pass

        # --- Stage 4: balanced-brace extraction ------------------------
        try:
            extracted = _extract_balanced(stripped)
            if extracted is not None:
                return json.loads(extracted)
        except (json.JSONDecodeError, ValueError):
            pass

        # --- Stage 5: control-char strip + trailing-comma repair -------
        try:
            s2 = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', '', stripped)
            s2 = re.sub(r',(\s*[}\]])', r'\1', s2)
            return json.loads(s2)
        except (json.JSONDecodeError, ValueError):
            pass

        # Final failure.
        raise LLMJSONParseError(raw[:500])

    # ------------------------------------------------------------------
    # Two-tier chat_json
    # ------------------------------------------------------------------

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ) -> Dict[str, Any]:
        """Send a chat request and return parsed JSON, hardened against defects.

        Behavior is gated by ``LLM_JSON_MODE`` (see ``__init__``):

          * ``strict``: Tier 1 only. Any exception re-raises *unwrapped*.
          * ``loose``  (default): Tier 1, then fall through to Tier 2 on
            exception with a warn log.
          * ``off``  : Tier 2 only (never sends ``response_format``).

        Pre-call: rejects messages whose ``role == 'user'`` content contains
        the delimiter-injection payload ``</UNTRUSTED_USER_DOCUMENT>``.
        """
        # --- Delimiter-injection guard (user-role only) ---------------
        # Delegate to the shared single-source-of-truth predicate so the
        # seam path and the StructuredOutputClient strict-schema path
        # cannot drift. Translate the platform's
        # ``DelimiterInjectionRejected`` (a ``ValueError`` subclass)
        # into the seam's historical ``LLMJSONParseError`` exception
        # class so existing callers that ``except LLMJSONParseError``
        # continue to catch the rejection unchanged.
        from app.simulation_platform.llm.security import (
            DelimiterInjectionRejected,
            assert_no_user_role_delimiter_injection,
        )
        try:
            assert_no_user_role_delimiter_injection(messages or [])
        except DelimiterInjectionRejected as exc:
            raise LLMJSONParseError('delimiter injection rejected') from exc

        # --- Tier 1: response_format = json_object --------------------
        if self.json_mode != 'off':
            try:
                raw = self._chat_internal(
                    messages=messages,
                    temperature=temperature,
                    max_tokens=max_tokens,
                    response_format={'type': 'json_object'},
                )
                return self._parse_llm_json(raw)
            except Exception as e:
                if self.json_mode == 'strict':
                    # Re-raise the ORIGINAL exception — no wrapping.
                    raise
                # loose: log and fall through to Tier 2.
                logger.warning(
                    "chat_json fallback",
                    extra={
                        'event': 'chat_json_fallback',
                        'tier': 1,
                        'exception_class': type(e).__name__,
                    },
                )

        # --- Tier 2: no response_format, full repair ------------------
        raw = self._chat_internal(
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format=None,
        )
        return self._parse_llm_json(raw)
