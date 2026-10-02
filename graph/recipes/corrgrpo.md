---
id: recipe:corrgrpo
type: recipe
title: "CorrGRPO Pearson Multi-Reward Normalization"
method: method:corrgrpo
task: task:multi-reward-rlvr
target_hardware: "GRPO-family box; paper: Qwen2.5-Coder 0.5B–7B coding plus tool-calling / agent-security"
framework: "PyTorch / GRPO-family host"
repo_url: "https://github.com/HKUST-KnowComp/CorrGRPO"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - corrgrpo
  - rlvr
  - multi-reward
---

# CorrGRPO Pearson Multi-Reward Normalization

## Hardware & Environment Setup
- Official: `https://github.com/HKUST-KnowComp/CorrGRPO`. `code_status: released`.
- Pass@1 stays CISPO. Density-aware aggregation stays DARA.

```bash
git clone https://github.com/HKUST-KnowComp/CorrGRPO.git && cd CorrGRPO
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def corrgrpo_advantages(rewards: list[list[float]], eps: float = 1e-8) -> list[float]:
    n = len(rewards)
    if n < 2:
        raise ValueError("need a group of at least two rollouts")
    k = len(rewards[0])
    if k < 1 or any(len(row) != k for row in rewards):
        raise ValueError("reward rows must share a positive width")
    means = [sum(rewards[i][j] for i in range(n)) / n for j in range(k)]
    centered = [[rewards[i][j] - means[j] for j in range(k)] for i in range(n)]
    cov = [[0.0] * k for _ in range(k)]
    for l in range(k):
        for m in range(k):
            cov[l][m] = sum(centered[i][l] * centered[i][m] for i in range(n)) / n
    std = [math.sqrt(max(cov[j][j], 0.0)) for j in range(k)]
    rho_sum = 0.0
    for l in range(k):
        for m in range(k):
            if std[l] < eps or std[m] < eps:
                continue
            rho_sum += cov[l][m] / (std[l] * std[m])
    denom = math.sqrt(max(rho_sum, 0.0)) + eps
    return [sum(centered[i]) / denom for i in range(n)]
```

Keep the GRPO surrogate. Zero-variance components contribute a zero row/column.

## Critical Hyperparameters & Tuning Advice
- Needs more than one reward with nonzero within-group variance.
- Single-reward groups reduce to ordinary GRPO-style std-norm.
