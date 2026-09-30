---
id: recipe:eapo
type: recipe
title: "EAPO Entropy-Guided Advantage Redistribution"
method: method:eapo
task: task:math-code-rl-dense
target_hardware: "8x H100 80GB host RLVR box (paper: Qwen3-4B/8B-Base and reasoning backbones)"
framework: "PyTorch / GRPO-family host"
repo_url: "https://github.com/wgcyeo/EAPO"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - eapo
  - rlvr
  - exploration
---

# EAPO Entropy-Guided Advantage Redistribution

## Hardware & Environment Setup
- Official: `https://github.com/wgcyeo/EAPO`. Project: `https://eapo-explore.github.io`. `code_status: released`.
- Pass@1 default stays CISPO. First-mistake teacher credit stays Cliff.

```bash
git clone https://github.com/wgcyeo/EAPO.git && cd EAPO
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def _percentile(sorted_vals: list[float], q: float) -> float:
    if not sorted_vals:
        raise ValueError("empty entropy batch")
    if not 0.0 <= q <= 1.0:
        raise ValueError("percentile must be in [0, 1]")
    if len(sorted_vals) == 1:
        return sorted_vals[0]
    pos = q * (len(sorted_vals) - 1)
    lo = int(math.floor(pos))
    hi = int(math.ceil(pos))
    if lo == hi:
        return sorted_vals[lo]
    w = pos - lo
    return sorted_vals[lo] * (1.0 - w) + sorted_vals[hi] * w


def normalize_entropy(values: list[float], eps: float = 1e-8) -> list[float]:
    ordered = sorted(values)
    q_lo = _percentile(ordered, 0.10)
    q_hi = _percentile(ordered, 0.90)
    span = q_hi - q_lo + eps
    return [min(max((h - q_lo) / span, 0.0), 1.0) for h in values]


def eapo_weights(adv: float, entropy_norm: list[float], kappa: float) -> list[float]:
    if kappa < 0.0:
        raise ValueError("kappa must be non-negative")
    n = len(entropy_norm)
    if n == 0:
        raise ValueError("empty response")
    if adv == 0.0 or kappa == 0.0:
        return [1.0] * n
    sign = 1.0 if adv > 0.0 else -1.0
    scores = [math.exp(kappa * sign * h) for h in entropy_norm]
    mean = sum(scores) / n
    if mean <= 0.0:
        raise ValueError("weight mean must be positive")
    return [s / mean for s in scores]
```

Token advantage is \(\hat{A}^i w_{i,t}\). Entropies are stop-grad from \(\pi_{\mathrm{old}}\). Percentiles are batch-wide over completion tokens.

## Critical Hyperparameters & Tuning Advice
- \(\kappa>0\) is the method; \(\kappa=0\) is GRPO. Ratio of any two in-response weights is at most \(e^\kappa\).
- 10th/90th percentile clip is the paper default.
- All-zero groups still have zero advantage; EAPO does not replace VeriGate or GRAFT.
