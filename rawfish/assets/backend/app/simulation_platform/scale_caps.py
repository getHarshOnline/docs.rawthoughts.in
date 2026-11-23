"""Platform-level cost-ceiling constants.

Two ``int`` constants any use-case lane's admission gate consults
before approving a simulation request. Kept in their own leaf module
(no imports) so any of the platform's lane-agnostic modules
(``scale_guard``, future ``runner_adapter``) can read them without
pulling in the heavy ``app.policy.schema`` graph.

``app.policy.schema`` re-exports these names verbatim so existing
``from app.policy.schema import SCALE_CAP_POC, SCALE_CAP_LARGE``
imports remain valid -- the canonical home is here, but the policy
schema is the historical entry point.
"""
from __future__ import annotations


# Default cost ceiling. Caps total LLM-call products
# (ensemble_n * stakeholders * drift_horizon_rounds). Applies unless
# the request opts into the expensive tier via the
# ``allow_expensive=True`` validation context (env override:
# ``POLICY_ALLOW_EXPENSIVE=true``). 500 keeps the POC loop inside a
# few-minute budget even on a slow provider.
SCALE_CAP_POC: int = 500


# Relaxed ceiling when the expensive-tier override is enabled. Set
# to 10x the default cap so an accidental opt-in still cannot
# green-light a production-scale spend without being noticed in cost
# summaries.
SCALE_CAP_LARGE: int = 5000


__all__ = ["SCALE_CAP_POC", "SCALE_CAP_LARGE"]
