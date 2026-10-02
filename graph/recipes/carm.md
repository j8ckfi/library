---
id: recipe:carm
type: recipe
title: "CARM Cancellation-Aware Response Mask"
method: method:carm
task: task:frontier-rl-posttrain-stack
target_hardware: "GRPO/PPO box with a separate rollout engine; paper: AIME mean@16 and four code benches"
framework: "PyTorch / GRPO-family host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - carm
  - rlvr
  - off-policy
---

# CARM Cancellation-Aware Response Mask

## Hardware & Environment Setup
- No official GitHub as of 2026-10-02 (`arXiv:2610.02039`). `repo_url: none found`. `code_status: none`.
- Pass@1 stays CISPO. Per-token train–infer IS stays CIS-RL. Engine stays Miles.

## Quickstart Implementation

```python
from __future__ import annotations

import math


def carm_score(token_ratios: list[float], eps: float = 1e-12) -> float:
    if not token_ratios:
        raise ValueError("need at least one token ratio")
    acc = 0.0
    for r in token_ratios:
        if r <= 0.0:
            raise ValueError("token ratios must be positive")
        acc += abs(math.log(max(r, eps)))
    return math.exp(acc / len(token_ratios))


def keep_response(score: float, threshold: float) -> bool:
    if threshold <= 1.0:
        raise ValueError("threshold must be greater than 1")
    return score <= threshold
```

Compute \(r_t=\pi_\theta(y_t\mid x,y_{<t})/\pi_{\mathrm{rollout}}(y_t\mid x,y_{<t})\). Average absolute log-ratios before the threshold. Token PPO/GRPO clipping is unchanged.

## Critical Hyperparameters & Tuning Advice
- Match filtering rates when comparing masks. More masking is not uniformly better.
- Complements CIS-RL rather than replacing it.
