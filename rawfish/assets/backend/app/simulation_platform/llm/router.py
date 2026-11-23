"""RawFish LiteLLM-backed provider router.

RawFish is local-first, not local-only. This module gives the platform a
single provider seam for local Ollama, local OpenAI-compatible endpoints,
and explicitly configured external providers without binding product paths
directly to OpenAI APIs.
"""
from __future__ import annotations

import json
import os
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, ConfigDict, Field

from ...config import Config
from .protocols import LLMCapabilities, LLMClientProtocol, UsageInfo


ProviderMode = str
VALID_PROVIDER_MODES = {
    "local_ollama",
    "local_openai_compatible",
    "external",
}
_MODEL_COST_OVERRIDE_PATH_ENVS = (
    "RAWFISH_LLM_MODEL_COST_OVERRIDES_PATH",
    "RAWFISH_MODEL_COST_OVERRIDES_PATH",
    "LLM_MODEL_COST_OVERRIDES_PATH",
)
_BUNDLED_MODEL_COST_OVERRIDES_PATH = Path(__file__).with_name(
    "model_cost_overrides.json",
)


class ProviderConfig(BaseModel):
    """Resolved provider choice, persisted per run."""

    model_config = ConfigDict(extra="forbid")

    mode: ProviderMode = Field(default="local_ollama")
    model: str = Field(default="qwen3-coder:30b")
    provider: Optional[str] = None
    base_url: Optional[str] = None
    api_key: Optional[str] = None

    def public_dict(self) -> Dict[str, Any]:
        data = self.model_dump(mode="json")
        data.pop("api_key", None)
        return data


class ProviderReadiness(BaseModel):
    model_config = ConfigDict(extra="forbid")

    ready: bool
    status: str
    configured: bool
    probed: bool = False
    reason: Optional[str] = None
    latency_ms: Optional[int] = None


class PreflightMeterPayload(BaseModel):
    model_config = ConfigDict(extra="forbid")

    scale_product: int
    scale_cap: int
    scale_ok: bool
    scale_error: Optional[Dict[str, int]] = None
    token_estimate: int
    provider: Dict[str, Any]
    provider_readiness: ProviderReadiness
    estimated_latency_ms: Optional[int] = None
    estimated_external_cost: Optional[Dict[str, Any]] = None
    external_budget_status: Optional[Dict[str, Any]] = None


class ProviderBudgetState(BaseModel):
    """Advisory budget status for external-provider preflight callers."""

    model_config = ConfigDict(extra="forbid")

    status: str
    currency: str = "USD"
    amount: Optional[float] = None
    warn_at: Optional[float] = None
    warning: bool = False
    reason: Optional[str] = None


def _env_first(*names: str, default: Optional[str] = None) -> Optional[str]:
    for name in names:
        value = os.environ.get(name)
        if value not in (None, ""):
            return value
    return default


def _read_int_env(name: str, default: int) -> int:
    raw = os.environ.get(name)
    if raw in (None, ""):
        return default
    try:
        value = int(raw)
    except (TypeError, ValueError):
        return default
    return value if value > 0 else default


def provider_config_from_env(*, include_secret: bool = True) -> ProviderConfig:
    mode = (
        _env_first(
            "RAWFISH_LLM_PROVIDER_MODE",
            "LLM_PROVIDER_MODE",
            default="local_ollama",
        )
        or "local_ollama"
    ).strip().lower()
    env_base_url = _env_first("RAWFISH_LLM_BASE_URL", "LLM_BASE_URL")
    base_url = env_base_url
    if base_url is None and mode == "local_ollama":
        base_url = "http://localhost:11434"

    env_model = _env_first("RAWFISH_LLM_MODEL", "LLM_MODEL_NAME")
    default_model = "" if mode == "external" else "qwen3-coder:30b"

    return ProviderConfig(
        mode=mode,
        model=env_model if env_model is not None else default_model,
        provider=_env_first("RAWFISH_LLM_PROVIDER", "LLM_PROVIDER"),
        base_url=base_url,
        api_key=(
            _env_first("RAWFISH_LLM_API_KEY", "LLM_API_KEY")
            if include_secret else None
        ),
    )


def provider_config_from_payload(
    payload: Optional[Dict[str, Any]],
    *,
    include_runtime_secret: bool = True,
) -> ProviderConfig:
    base = provider_config_from_env(
        include_secret=include_runtime_secret,
    ).model_dump()
    if isinstance(payload, dict):
        for key in ("mode", "model", "provider", "base_url"):
            if key in payload and payload[key] not in ("", None):
                base[key] = payload[key]
        final_mode = str(base.get("mode") or "").strip().lower()
        env_base_url = _env_first("RAWFISH_LLM_BASE_URL", "LLM_BASE_URL")
        if (
            final_mode != "local_ollama"
            and "base_url" not in payload
            and env_base_url is None
        ):
            base["base_url"] = None
        if "api_key" in payload:
            raise ValueError(
                "provider api_key is not accepted in request payloads; configure "
                "RAWFISH_LLM_API_KEY in the backend runtime for external providers"
            )
        if (
            final_mode == "external"
            and "model" not in payload
            and _env_first("RAWFISH_LLM_MODEL", "LLM_MODEL_NAME") is None
        ):
            base["model"] = ""
    return ProviderConfig(**base)


def provider_config_from_state(payload: Optional[Dict[str, Any]]) -> ProviderConfig:
    """Hydrate a persisted per-run provider binding for execution.

    ``state.json`` stores only the public provider choice. Secrets are
    resolved from the current runtime environment at generation time,
    so a stale or malicious ``api_key`` field in persisted state is
    ignored rather than used.
    """
    public_payload = dict(payload) if isinstance(payload, dict) else payload
    if isinstance(public_payload, dict):
        public_payload.pop("api_key", None)
    return provider_config_from_payload(
        public_payload,
        include_runtime_secret=True,
    )


def _import_litellm():
    try:
        import litellm  # type: ignore
    except Exception as exc:  # noqa: BLE001
        return None, exc
    return litellm, None


def _litellm_model(config: ProviderConfig) -> str:
    model = config.model
    if config.mode == "local_ollama":
        if model.startswith(("ollama/", "ollama_chat/")):
            return model
        return f"ollama_chat/{model}"
    if config.mode == "local_openai_compatible":
        if model.startswith("openai/"):
            return model
        return f"openai/{model}"
    if config.provider:
        prefix = f"{config.provider}/"
        if model.startswith(prefix):
            return model
        return f"{config.provider}/{model}"
    return model


def _litellm_api_base(config: ProviderConfig) -> Optional[str]:
    """Return the provider base URL in the shape LiteLLM expects."""

    if not config.base_url:
        return None
    base_url = config.base_url.rstrip("/")
    if config.mode == "local_ollama" and base_url.endswith("/v1"):
        return base_url[:-3].rstrip("/")
    return base_url


def _external_cost_lookup_keys(config: ProviderConfig) -> List[str]:
    """Return model ids accepted by RawFish cost override catalogs."""

    keys: List[str] = []
    litellm_model = _litellm_model(config)
    raw_model = (config.model or "").strip()
    for key in (litellm_model, raw_model):
        if key and key not in keys:
            keys.append(key)
    provider = (config.provider or "").strip()
    if provider and raw_model and not raw_model.startswith(f"{provider}/"):
        provider_model = f"{provider}/{raw_model}"
        if provider_model not in keys:
            keys.append(provider_model)
    return keys


def _read_model_cost_catalog(path: Path) -> Dict[str, Any]:
    parsed = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(parsed, dict):
        raise ValueError("model cost catalog must be a JSON object")
    models = parsed.get("models")
    if models is not None:
        if not isinstance(models, dict):
            raise ValueError("model cost catalog 'models' must be a JSON object")
        return models
    return parsed


def _lookup_override_model_cost(
    config: ProviderConfig,
) -> tuple[Optional[Dict[str, Any]], Optional[str]]:
    """Find a RawFish override cost row, returning an advisory error if any.

    Override catalogs are optional. A missing model entry simply falls through
    to LiteLLM's built-in catalog; a malformed explicitly-configured catalog or
    malformed matching row marks the cost unavailable rather than pretending a
    price exists.
    """

    lookup_keys = _external_cost_lookup_keys(config)
    env_path = _env_first(*_MODEL_COST_OVERRIDE_PATH_ENVS)
    catalog_sources: List[tuple[str, Path, bool]] = []
    if env_path:
        catalog_sources.append(
            ("env model cost override catalog", Path(env_path).expanduser(), True),
        )
    catalog_sources.append(
        (
            "bundled model cost override catalog",
            _BUNDLED_MODEL_COST_OVERRIDES_PATH,
            False,
        ),
    )
    for source, path, required in catalog_sources:
        if not path.exists():
            if required:
                return None, f"{source} not found at {path}"
            continue
        try:
            catalog = _read_model_cost_catalog(path)
        except Exception as exc:  # noqa: BLE001
            return None, f"{source} could not be read: {type(exc).__name__}: {exc}"
        for key in lookup_keys:
            if key not in catalog:
                continue
            entry = catalog[key]
            if not isinstance(entry, dict):
                return None, f"model cost entry for {key!r} must be a JSON object"
            return entry, None
    return None, None


def _coerce_cost_per_token(value: Any, *, field: str) -> Optional[float]:
    if value is None:
        return None
    try:
        numeric = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{field} must be numeric") from exc
    if numeric < 0:
        raise ValueError(f"{field} must be non-negative")
    return numeric


def _estimate_cost_from_row(
    row: Dict[str, Any],
    *,
    model: str,
    token_estimate: int,
) -> Dict[str, Any]:
    input_cost = _coerce_cost_per_token(
        row.get("input_cost_per_token", row.get("prompt_cost_per_token")),
        field="input_cost_per_token",
    )
    output_cost = _coerce_cost_per_token(
        row.get("output_cost_per_token", row.get("completion_cost_per_token")),
        field="output_cost_per_token",
    )
    flat_cost = _coerce_cost_per_token(
        row.get("cost_per_token"),
        field="cost_per_token",
    )
    known_costs = [
        value
        for value in (input_cost, output_cost)
        if value is not None
    ]
    if not known_costs and flat_cost is not None:
        known_costs = [flat_cost]
    if not known_costs:
        return {
            "status": "cost_unavailable",
            "currency": "USD",
            "amount": None,
            "model": model,
            "reason": (
                "model cost entry has no input_cost_per_token, "
                "output_cost_per_token, or cost_per_token"
            ),
        }
    blended = sum(known_costs) / len(known_costs)
    return {
        "status": "estimated",
        "currency": "USD",
        "model": model,
        "amount": round(token_estimate * blended, 6),
    }


def check_provider_readiness(
    config: ProviderConfig,
    *,
    probe: bool = False,
) -> ProviderReadiness:
    mode = (config.mode or "").strip().lower()
    if mode not in VALID_PROVIDER_MODES:
        return ProviderReadiness(
            ready=False,
            status="invalid_mode",
            configured=False,
            probed=False,
            reason=f"unsupported provider mode {config.mode!r}",
        )
    if not (config.model or "").strip():
        return ProviderReadiness(
            ready=False,
            status="missing_model",
            configured=False,
            probed=False,
            reason="provider readiness requires an explicit model id",
        )
    if mode == "external":
        if not (config.provider or "").strip():
            return ProviderReadiness(
                ready=False,
                status="missing_external_provider",
                configured=False,
                probed=False,
                reason="external provider mode requires an explicit provider id",
            )
        if not config.api_key:
            return ProviderReadiness(
                ready=False,
                status="missing_external_key",
                configured=False,
                probed=False,
                reason=(
                    "external provider mode requires RAWFISH_LLM_API_KEY "
                    "in the backend runtime configuration"
                ),
            )
    if mode in {"local_ollama", "local_openai_compatible"} and not config.base_url:
        return ProviderReadiness(
            ready=False,
            status="missing_base_url",
            configured=False,
            probed=False,
            reason="local provider modes require a base_url",
        )

    if not probe:
        return ProviderReadiness(
            ready=True,
            status="configured_unprobed",
            configured=True,
            probed=False,
        )

    litellm, import_error = _import_litellm()
    if litellm is None:
        return ProviderReadiness(
            ready=False,
            status="failed",
            configured=True,
            probed=True,
            reason=f"litellm is not installed: {import_error}",
        )

    started = time.monotonic()
    try:
        kwargs: Dict[str, Any] = {
            "model": _litellm_model(config),
            "messages": [
                {"role": "user", "content": "Return the JSON object {\"ok\": true}."}
            ],
            "max_tokens": 16,
            "temperature": 0,
            "api_key": config.api_key or "local-llm-key",
            "timeout": Config.RAWFISH_LLM_READINESS_TIMEOUT_SEC,
            "num_retries": 0,
            "response_format": {"type": "json_object"},
        }
        api_base = _litellm_api_base(config)
        if api_base:
            kwargs["api_base"] = api_base
        litellm.completion(**kwargs)
    except Exception as exc:  # noqa: BLE001
        return ProviderReadiness(
            ready=False,
            status="failed",
            configured=True,
            probed=True,
            reason=repr(exc)[:240],
            latency_ms=int((time.monotonic() - started) * 1000),
        )
    return ProviderReadiness(
        ready=True,
        status="ready",
        configured=True,
        probed=True,
        latency_ms=int((time.monotonic() - started) * 1000),
    )


def estimate_external_cost(
    config: ProviderConfig,
    *,
    token_estimate: int,
) -> Optional[Dict[str, Any]]:
    if config.mode != "external":
        return None
    model = _litellm_model(config)
    override_row, override_error = _lookup_override_model_cost(config)
    if override_error is not None:
        return {
            "status": "cost_unavailable",
            "currency": "USD",
            "amount": None,
            "model": model,
            "reason": override_error,
        }
    if override_row is not None:
        try:
            return _estimate_cost_from_row(
                override_row,
                model=model,
                token_estimate=token_estimate,
            )
        except ValueError as exc:
            return {
                "status": "cost_unavailable",
                "currency": "USD",
                "amount": None,
                "model": model,
                "reason": str(exc),
            }
    litellm, _import_error = _import_litellm()
    if litellm is None:
        return {
            "status": "cost_unavailable",
            "currency": "USD",
            "amount": None,
            "model": model,
            "reason": "litellm model cost data unavailable because litellm is not installed",
        }
    try:
        cost_per_token = getattr(litellm, "model_cost", {}).get(model, {})
        if not isinstance(cost_per_token, dict) or not cost_per_token:
            return {
                "status": "cost_unavailable",
                "currency": "USD",
                "amount": None,
                "model": model,
            }
        estimated = _estimate_cost_from_row(
            cost_per_token,
            model=model,
            token_estimate=token_estimate,
        )
        if estimated.get("reason"):
            estimated.pop("reason", None)
        return estimated
    except Exception as exc:  # noqa: BLE001
        return {
            "status": "cost_unavailable",
            "currency": "USD",
            "amount": None,
            "model": model,
            "reason": repr(exc)[:160],
        }


def provider_budget_state(
    estimated_external_cost: Optional[Dict[str, Any]],
    *,
    warn_at: Optional[float],
) -> ProviderBudgetState:
    """Map an external-cost estimate to an advisory budget state.

    The cockpit/manual route can call this without importing lane
    manifests into the router. Unknown costs stay advisory instead of
    being treated as zero-cost; known costs at or above ``warn_at`` are
    flagged for UI/operator confirmation by the caller.
    """
    if estimated_external_cost is None:
        return ProviderBudgetState(status="not_applicable")
    currency = str(estimated_external_cost.get("currency") or "USD")
    amount = estimated_external_cost.get("amount")
    status = str(estimated_external_cost.get("status") or "cost_unavailable")
    reason = estimated_external_cost.get("reason")
    if amount is None:
        return ProviderBudgetState(
            status=status,
            currency=currency,
            amount=None,
            warn_at=warn_at,
            warning=False,
            reason=str(reason) if reason else None,
        )
    try:
        numeric_amount = float(amount)
    except (TypeError, ValueError):
        return ProviderBudgetState(
            status="cost_unavailable",
            currency=currency,
            amount=None,
            warn_at=warn_at,
            warning=False,
            reason="estimated_external_cost.amount is not numeric",
        )
    warning = warn_at is not None and numeric_amount >= warn_at
    return ProviderBudgetState(
        status="warn_at_exceeded" if warning else status,
        currency=currency,
        amount=numeric_amount,
        warn_at=warn_at,
        warning=warning,
    )


class RawFishLiteLLMClient:
    """Protocol-compatible JSON chat client backed by LiteLLM."""

    capabilities = LLMCapabilities(supports_json_schema=False)

    def __init__(self, config: ProviderConfig):
        self.config = config
        self.model = _litellm_model(config)
        self.json_mode = (os.getenv("LLM_JSON_MODE") or "loose").strip().lower()
        if self.json_mode not in {"loose", "strict", "off"}:
            self.json_mode = "loose"
        self.policy_max_tokens_report = _read_int_env(
            "POLICY_MAX_TOKENS_REPORT",
            16384,
        )
        self.last_usage: Optional[UsageInfo] = None

    def _parse_json(self, raw: str) -> Dict[str, Any]:
        cleaned = re.sub(r"^```(?:json)?\s*\n?", "", raw.strip(), flags=re.I)
        cleaned = re.sub(r"\n?```\s*$", "", cleaned).strip()
        parsed = json.loads(cleaned)
        if not isinstance(parsed, dict):
            raise ValueError("LLM JSON response must be an object")
        return parsed

    def chat_json(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.3,
        max_tokens: int = 4096,
    ) -> Dict[str, Any]:
        readiness = check_provider_readiness(self.config, probe=False)
        if not readiness.ready:
            raise RuntimeError(readiness.reason or readiness.status)
        litellm, import_error = _import_litellm()
        if litellm is None:
            raise RuntimeError(f"litellm is not installed: {import_error}")

        kwargs: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "api_key": self.config.api_key or "local-llm-key",
            "timeout": Config.RAWFISH_LLM_GENERATION_TIMEOUT_SEC,
            "num_retries": Config.RAWFISH_LLM_MAX_RETRIES,
        }
        api_base = _litellm_api_base(self.config)
        if api_base:
            kwargs["api_base"] = api_base
        if self.json_mode != "off":
            kwargs["response_format"] = {"type": "json_object"}
        response = litellm.completion(**kwargs)
        usage = getattr(response, "usage", None)
        if usage is not None:
            self.last_usage = UsageInfo(
                tokens_in=int(getattr(usage, "prompt_tokens", 0) or 0),
                tokens_out=int(getattr(usage, "completion_tokens", 0) or 0),
            )
        content = response.choices[0].message.content
        return self._parse_json(str(content or ""))

    def chat(
        self,
        messages: List[Dict[str, str]],
        temperature: float = 0.7,
        max_tokens: int = 4096,
        response_format: Optional[Dict[str, Any]] = None,
    ) -> str:
        """Plain chat surface on the provider seam."""
        readiness = check_provider_readiness(self.config, probe=False)
        if not readiness.ready:
            raise RuntimeError(readiness.reason or readiness.status)
        litellm, import_error = _import_litellm()
        if litellm is None:
            raise RuntimeError(f"litellm is not installed: {import_error}")

        kwargs: Dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "api_key": self.config.api_key or "local-llm-key",
            "timeout": Config.RAWFISH_LLM_GENERATION_TIMEOUT_SEC,
            "num_retries": Config.RAWFISH_LLM_MAX_RETRIES,
        }
        api_base = _litellm_api_base(self.config)
        if api_base:
            kwargs["api_base"] = api_base
        if response_format:
            kwargs["response_format"] = response_format
        response = litellm.completion(**kwargs)
        usage = getattr(response, "usage", None)
        if usage is not None:
            self.last_usage = UsageInfo(
                tokens_in=int(getattr(usage, "prompt_tokens", 0) or 0),
                tokens_out=int(getattr(usage, "completion_tokens", 0) or 0),
            )
        content = str(response.choices[0].message.content or "")
        return re.sub(r"<think>[\s\S]*?</think>", "", content).strip()


class RawFishLLMProviderFactory:
    """Factory used by platform dispatch and lane adapters."""

    def __init__(self, config: Optional[ProviderConfig] = None):
        self.config = config

    def build_client(self) -> LLMClientProtocol:
        return RawFishLiteLLMClient(self.config or provider_config_from_env())

    def build_client_for_config(
        self,
        config: ProviderConfig,
    ) -> LLMClientProtocol:
        return RawFishLiteLLMClient(config)


__all__ = [
    "PreflightMeterPayload",
    "ProviderBudgetState",
    "ProviderConfig",
    "ProviderReadiness",
    "RawFishLLMProviderFactory",
    "RawFishLiteLLMClient",
    "check_provider_readiness",
    "estimate_external_cost",
    "provider_budget_state",
    "provider_config_from_env",
    "provider_config_from_payload",
    "provider_config_from_state",
]
