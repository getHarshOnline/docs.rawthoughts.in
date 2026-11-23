---
title: "backend/app/simulation_platform/builtin_lanes.py"
noindex: true
---

```py
"""Built-in RawFish lane registration."""

from __future__ import annotations

from typing import Iterable

from .registry import register
from .use_case import SimulationUseCase


def iter_builtin_use_cases() -> Iterable[SimulationUseCase]:
    """Yield the lane adapters shipped with the RawFish product."""

    from app.creator.adapter import CREATOR_USE_CASE
    from app.internal_policy.adapter import INTERNAL_POLICY_USE_CASE
    from app.public_policy.adapter import PUBLIC_POLICY_USE_CASE

    yield CREATOR_USE_CASE
    yield INTERNAL_POLICY_USE_CASE
    yield PUBLIC_POLICY_USE_CASE


def register_builtin_use_cases() -> None:
    """Register every built-in lane with the platform registry."""

    for use_case in iter_builtin_use_cases():
        register(use_case)
```
