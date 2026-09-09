---
id: recipe:routeopd
type: recipe
title: "RouteOPD Probability Transport"
method: method:routeopd
task: task:student-distillation
target_hardware: "same as host sampled-token OPD (paper tables on 1.5B–4B students)"
framework: "PyTorch / host OPD trainer"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - routeopd
  - distillation
  - on-policy
---

# RouteOPD Probability Transport

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Add routing on top of sampled-token OPD (`method:opd`).
- Defaults: k=32, m=2, Bmin=log 1.2, Bmax=log 1.5, Huber κ=1.0, probability floor 1e-8.
- Host distill algorithm stays OPD. Pass@1 labeled RLVR stays CISPO.

## Quickstart Implementation

```python
import math

import torch
import torch.nn.functional as F


def herfindahl_concentration(deficit: torch.Tensor) -> torch.Tensor:
    """c_t in [0, 1] from positive deficit mass on the union."""
    pos = deficit.clamp(min=0.0)
    mass = pos.sum()
    if float(mass) <= 0.0:
        return deficit.new_tensor(0.0)
    q = pos / mass
    n = int((q > 0).sum().item())
    if n <= 1:
        return deficit.new_tensor(1.0)
    h = (q * q).sum()
    return (n * h - 1.0) / (n - 1)


def bounded_potential(x: torch.Tensor, budget: float) -> torch.Tensor:
    """φ_B(x) = (B/2) tanh(2x/B), range (-B/2, B/2)."""
    b = max(float(budget), 1e-8)
    return (b / 2.0) * torch.tanh(2.0 * x / b)


def pair_target(g_src: torch.Tensor, g_dst: torch.Tensor, budget: float) -> torch.Tensor:
    return bounded_potential(g_dst, budget) - bounded_potential(g_src, budget)


def huber(resid: torch.Tensor, kappa: float = 1.0) -> torch.Tensor:
    abs_r = resid.abs()
    quad = 0.5 * resid * resid
    lin = kappa * (abs_r - 0.5 * kappa)
    return torch.where(abs_r <= kappa, quad, lin)


def routeopd_loss(
    delta_logodds: torch.Tensor,
    target: torch.Tensor,
    mismatch_mass: torch.Tensor,
    kappa: float = 1.0,
) -> torch.Tensor:
    """Mean Huber on m routes, scaled by mismatch mass M_t."""
    return mismatch_mass * huber(delta_logodds - target, kappa).mean()


def adaptive_budget(concentration: torch.Tensor, b_min: float, b_max: float) -> torch.Tensor:
    return b_min + (b_max - b_min) * concentration


B_MIN = math.log(1.2)
B_MAX = math.log(1.5)
```

## Critical Hyperparameters & Tuning Advice
- Detach routing statistics. Do not backprop through the coupling.
- Shared potential, not independent edge clipping.
- k=32, m=2 is the measured Pareto knee. Do not jump to full-vocabulary routing for +0.08 Avg@16.
