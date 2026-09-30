---
id: recipe:dn-mopd
type: recipe
title: "DN-MOPD Domain-Normalized MOPD Advantages"
method: method:dn-mopd
task: task:student-distillation
target_hardware: "multi-GPU Uni-OPD / verl box; paper: Qwen3.5 2B/4B/9B students with matching domain specialists"
framework: "PyTorch / Uni-OPD (MOPD host)"
repo_url: "https://github.com/LiXin97/DN-MOPD"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - dn-mopd
  - distillation
  - multi-teacher
  - on-policy
---

# DN-MOPD Domain-Normalized MOPD Advantages

## Hardware & Environment Setup
- Official: `https://github.com/LiXin97/DN-MOPD`. `code_status: released`.
- Multi-teacher default stays Open-MOPD. Single-teacher stays OPD. Unlabeled token routing stays MOPD-Router.

```bash
git clone https://github.com/LiXin97/DN-MOPD.git && cd DN-MOPD
```

## Quickstart Implementation

```python
from __future__ import annotations

from math import sqrt


def _pop_std(values: list[float]) -> float:
    n = len(values)
    if n < 2:
        return 0.0
    mean = sum(values) / n
    var = sum((x - mean) ** 2 for x in values) / n
    return sqrt(var)


def domain_multipliers(
    log_ratios_by_domain: dict[str, list[float]],
    lo: float = 0.25,
    hi: float = 4.0,
) -> dict[str, float]:
    if lo <= 0.0 or hi < lo:
        raise ValueError("clip bounds must satisfy 0 < lo <= hi")
    pooled: list[float] = []
    for xs in log_ratios_by_domain.values():
        pooled.extend(xs)
    sigma_all = _pop_std(pooled)
    weights: dict[str, float] = {}
    for domain, xs in log_ratios_by_domain.items():
        sigma_d = _pop_std(xs)
        if sigma_all <= 0.0 or sigma_d <= 0.0:
            weights[domain] = 1.0
            continue
        ratio = sigma_all / sigma_d
        weights[domain] = min(max(ratio, lo), hi)
    return weights


def scale_advantages(
    advantages: list[float],
    domain_ids: list[str],
    weights: dict[str, float],
) -> list[float]:
    if len(advantages) != len(domain_ids):
        raise ValueError("advantages and domain_ids must align")
    out: list[float] = []
    for a, d in zip(advantages, domain_ids):
        w = weights.get(d)
        if w is None:
            raise KeyError(f"missing multiplier for domain {d!r}")
        out.append(w * a)
    return out
```

Detached \(\widetilde{A}_t=w_d A_t\) enters the clipped OPD surrogate. Estimate \(w_d\) from cached rollout log-ratios, not from the actor recomputation.

## Critical Hyperparameters & Tuning Advice
- Clip \([0.25, 4]\). \(w_d=1\) if a domain has fewer than two tokens.
- Paper: independently trained Qwen3.5 math/code/IF specialists; equal prompt counts are not equal gradient share.
- Do not retarget Open-MOPD from the six-task Total lifts.
