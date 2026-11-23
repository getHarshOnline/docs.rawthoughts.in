"""Scale-guard mechanics for the simulation platform.

A pure, side-effect-free evaluator for the canonical scale formula
``ensemble_n * len(stakeholders) * drift_horizon_rounds`` against the
two caps published by :mod:`app.policy.schema`
(:data:`SCALE_CAP_POC` / :data:`SCALE_CAP_LARGE`).

The :class:`ScaleGuardExceeded` exception type and the
:func:`evaluate_scale_guard` helper live here so any use case (not
just policy) can reuse the same admission gate. The HTTP boundary reads
``POLICY_ALLOW_EXPENSIVE`` from the process environment and passes the
resolved boolean down -- this module never touches the environment or emits log records, which
keeps it deterministic and easy to test.

The two enforcement sites (schema validator + runtime guard) MUST
share this single formula; if either side drifts, a scenario admitted
at create-time could be rejected at start-time for a different reason
(or vice versa). The schema validator continues to enforce its own
copy directly because Pydantic validation context is the natural
home for the override flag there; this module is the runtime SSoT
shared by anything outside Pydantic.
"""

from __future__ import annotations

from typing import Dict, Optional, Tuple

from .scale_caps import SCALE_CAP_LARGE, SCALE_CAP_POC


class ScaleGuardExceeded(Exception):
    """Raised when the scale product strictly exceeds the active cap.

    Carries the inputs and the resolved cap so callers can render
    a structured error payload without recomputing anything.
    """

    def __init__(
        self,
        *,
        stakeholders: int,
        rounds: int,
        ensemble_n: int,
        product: int,
        cap: int,
    ) -> None:
        super().__init__(
            f"Scale guard exceeded: ensemble_n={ensemble_n} * "
            f"stakeholders={stakeholders} * rounds={rounds} = {product} > {cap}"
        )
        self.stakeholders = stakeholders
        self.rounds = rounds
        self.ensemble_n = ensemble_n
        self.product = product
        self.cap = cap

    def to_details(self) -> Dict[str, int]:
        return {
            "stakeholders": self.stakeholders,
            "rounds": self.rounds,
            "ensemble_n": self.ensemble_n,
            "product": self.product,
            "cap": self.cap,
        }


class PlatformScaleGuardRefused(Exception):
    """Lane-agnostic scale-guard refusal carrying a (message, details) pair.

    Lanes that wrap their own scale-guard exception type (e.g. the
    policy lane's ``PolicyScaleGuardExceeded`` in
    :mod:`app.services.policy.policy_runner_service`) re-raise as this
    platform-level exception when their adapter is invoked through the
    generic dispatch surface. The generic ``POST .../start`` route in
    :mod:`app.api.use_cases` catches this exception BEFORE its broad
    ``except Exception`` and maps it to a structured
    ``400 SCALE_GUARD_EXCEEDED`` envelope whose ``message`` and
    ``details`` preserve the lane's structured refusal payload.

    The two-field shape (``message`` + ``details``) mirrors the policy
    lane wrapper's; the lane's exception carries the structured
    payload via :meth:`ScaleGuardExceeded.to_details` so the platform
    surface re-emits exactly the same dict.
    """

    def __init__(self, *, message: str, details: Dict[str, int]) -> None:
        super().__init__(message)
        self.message = message
        self.details = details


def evaluate_scale_guard(
    *,
    ensemble_n: int,
    stakeholders: int,
    rounds: int,
    allow_expensive_env: bool = False,
) -> Tuple[bool, int, Optional[Dict[str, int]]]:
    """Evaluate the canonical scale formula against the active cap.

    Pure: no env read, no logging, no side effects. The override
    flag must be resolved by the caller (the HTTP boundary reads
    ``POLICY_ALLOW_EXPENSIVE``).

    Args:
      ensemble_n: per-call ensemble fan-out.
      stakeholders: count of stakeholder segments (equals OASIS
        ``agents`` at the canonical POC; lane-specific multipliers should
        be applied before calling this pure guard).
      rounds: drift-horizon round count.
      allow_expensive_env: when ``True``, raise the ceiling to
        :data:`SCALE_CAP_LARGE`; default :data:`SCALE_CAP_POC`.
        The override raises the ceiling, it does NOT remove it.

    Returns:
      ``(ok, cap_value, error_payload)`` where ``ok`` is ``True``
      when ``product <= cap_value``; ``error_payload`` is ``None``
      on admit and the structured details dict on reject.
    """
    product = max(1, stakeholders) * max(1, rounds) * max(1, ensemble_n)
    cap = SCALE_CAP_LARGE if allow_expensive_env else SCALE_CAP_POC
    if product > cap:
        payload = {
            "stakeholders": stakeholders,
            "rounds": rounds,
            "ensemble_n": ensemble_n,
            "product": product,
            "cap": cap,
        }
        return False, cap, payload
    return True, cap, None


__all__ = ["ScaleGuardExceeded", "evaluate_scale_guard"]
