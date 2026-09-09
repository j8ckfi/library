---
id: recipe:thinkprior
type: recipe
title: "ThinkPrior Cold-Start Prompt Selection"
method: method:thinkprior
task: task:math-code-rl-dense
target_hardware: "same as host GRPO/DAPO (paper: Qwen2.5-Math-7B)"
framework: "PyTorch / host RLVR trainer"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - thinkprior
  - rlvr
  - data-policy
---

# ThinkPrior Cold-Start Prompt Selection

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Project: `https://shatianming5.github.io/thinkprior/`.
- Add a Beta posterior over pass rate to an existing GRPO/DAPO loop. Host Pass@1 algorithm stays CISPO; ThinkPrior only ranks prompts.
- One offline verifier-scored pass of a cheap external anchor before step 0.

## Quickstart Implementation

```python
from __future__ import annotations

from math import lgamma


def _beta_mean(alpha: float, beta: float) -> float:
    return alpha / (alpha + beta)


def expected_learnability(alpha: float, beta: float, eps: float = 1e-6) -> float:
    """Select by E[p(1-p)] with a dispersion penalty: at equal mean, prefer better-known p.

    Silent groups peak at p in {0,1}. p(1-p) is learnability. Variance of a Beta is
    mu*(1-mu)/(n+1), so a tighter posterior at the same mean is preferred.
    """
    n = alpha + beta
    mu = _beta_mean(alpha, beta)
    learn = mu * (1.0 - mu)
    return learn * (n / (n + 1.0 + eps))


def init_from_anchor(k: int, n: int, prior: float = 1.0) -> tuple[float, float]:
    """Verifier-scored anchor: k correct in n samples. Uniform Beta(1,1) plus counts."""
    return prior + float(k), prior + float(n - k)


def update_from_group(alpha: float, beta: float, correct: int, group_size: int) -> tuple[float, float]:
    return alpha + float(correct), beta + float(group_size - correct)


def log_beta(x: float, y: float) -> float:
    return lgamma(x) + lgamma(y) - lgamma(x + y)
```

## Critical Hyperparameters & Tuning Advice
- Select the prompt with highest expected learnability among unseen / under-observed items at cold start.
- After step 0, update from target-policy group outcomes. Do not keep using only the anchor.
- Do not change the GRPO/CISPO loss. Do not expect a final-accuracy lift on a small exhausted pool.
