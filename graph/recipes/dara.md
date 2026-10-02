---
id: recipe:dara
type: recipe
title: "DARA Density-Aware Multi-Reward Aggregation"
method: method:dara
task: task:multi-reward-rlvr
target_hardware: "GDPO-style multi-reward GRPO box; paper: Qwen2.5-1.5B/3B ToolRL and math length+correctness"
framework: "PyTorch / GRPO-family host"
repo_url: "https://github.com/zhaihaotian/DARA"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - dara
  - rlvr
  - multi-reward
---

# DARA Density-Aware Multi-Reward Aggregation

## Hardware & Environment Setup
- Official: `https://github.com/zhaihaotian/DARA`. `code_status: released`.
- Pass@1 stays CISPO. Pearson covariance-norm stays CorrGRPO. GDPO is prior art, not a library node.

```bash
git clone https://github.com/zhaihaotian/DARA.git && cd DARA
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def dara_asym_weights(
    active_density: list[float],
    w_max: float = 8.0,
    eps: float = 1e-8,
) -> list[float]:
    if w_max <= 0.0:
        raise ValueError("w_max must be positive")
    if not active_density:
        raise ValueError("density vector is empty")
    pi_ref = max(active_density)
    if pi_ref <= 0.0:
        raise ValueError("at least one reward must be active")
    weights = []
    for pi in active_density:
        if pi <= 0.0:
            weights.append(0.0)
            continue
        weights.append(min(w_max, math.sqrt(pi_ref / max(pi, eps))))
    return weights


def scale_positive(advantages: list[float], weight: float) -> list[float]:
    if weight < 0.0:
        raise ValueError("weight must be non-negative")
    return [a * weight if a > 0.0 else a for a in advantages]
```

Apply reward-wise group norm first. Then DARA-Asym on positive advantages only. Sum and batch-normalize as in GDPO.

## Critical Hyperparameters & Tuning Advice
- Keep \(w_{\max}\). Uncapped inverse-sqrt explodes when a reward is active in one group.
- DARA-Sym amplifies both signs; the paper default is Asym.
