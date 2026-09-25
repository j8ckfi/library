---
id: recipe:s2d-opd
type: recipe
title: "S2D-OPD Selective Direct-OPD"
method: method:s2d-opd
task: task:student-distillation
target_hardware: "Direct-OPD host with teacher and pre-RL reference forwards; paper: 1.7B–8B students, Avg@32"
framework: "PyTorch Direct-OPD host"
repo_url: "https://anonymous.4open.science/r/S2D-OPD-8868"
code_status: announced
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - s2d-opd
  - distillation
  - on-policy
---

# S2D-OPD Selective Direct-OPD

## Hardware & Environment Setup
- Review-anonymous code as of 2026-09-25: `https://anonymous.4open.science/r/S2D-OPD-8868`. `code_status: announced`. Not a named public GitHub.
- Strong-teacher distill default stays OPD. Cal-OPD / IER-OPD / LastOPD are different axes.

## Quickstart Implementation

```python
from __future__ import annotations

from math import log


def js_divergence(p: list[float], q: list[float], eps: float = 1e-12) -> float:
    if len(p) != len(q) or not p:
        raise ValueError("p and q must be non-empty and aligned")
    acc = 0.0
    for pi, qi in zip(p, q):
        pi = max(pi, 0.0)
        qi = max(qi, 0.0)
        m = 0.5 * (pi + qi)
        if m <= eps:
            continue
        if pi > eps:
            acc += 0.5 * pi * log(pi / m)
        if qi > eps:
            acc += 0.5 * qi * log(qi / m)
    return acc


def keep_top_jsd(scores: list[float], rho: float = 0.1) -> list[bool]:
    n = len(scores)
    if n == 0:
        return []
    k = max(1, int((rho * n) + 0.999999))
    k = min(k, n)
    order = sorted(range(n), key=lambda i: scores[i], reverse=True)
    mask = [False] * n
    for i in order[:k]:
        mask[i] = True
    return mask
```

Build compressed teacher/reference distributions on the student's top-K plus residual mass, score with `js_divergence`, and apply Direct-OPD only where `keep_top_jsd` is true. No extra forwards beyond Direct-OPD.

## Critical Hyperparameters & Tuning Advice
- Default \(\rho=0.1\) per response. Keep at least one state so every rollout appears.
- Adaptive KL coefficient in the paper still uses all valid positions; the mask applies to the Direct-OPD terms.
- Do not retarget OPD from the +0.95 mean. This is a Direct-OPD keep-mask.
