---
id: recipe:n-opsd
type: recipe
title: "N-OPSD Neighborhood Privileged Teachers"
method: method:n-opsd
task: task:privileged-teacher-opsd
target_hardware: "OPSD box that can store a frozen perturbation pool; paper: Qwen3-1.7B/4B/8B Avg@12"
framework: "PyTorch OPSD host plus a frozen neighborhood expert pool"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - n-opsd
  - distillation
  - privileged-teacher
---

# N-OPSD Neighborhood Privileged Teachers

## Hardware & Environment Setup
- No official GitHub as of 2026-10-02 (`arXiv:2609.39687`). `repo_url: none found`. `code_status: none`.
- Privileged-OPSD first hop stays VISTA. Scale-collapse scaffolds stay OASIS. Co-evolving gold teacher stays DCE+SRCL.

## Quickstart Implementation

```python
from __future__ import annotations


def maxpeak_token(expert_logp: list[list[float]]) -> int:
    if not expert_logp or not expert_logp[0]:
        raise ValueError("need at least one expert distribution")
    vocab = len(expert_logp[0])
    if any(len(row) != vocab for row in expert_logp):
        raise ValueError("expert distributions must share a vocabulary")
    peak = -1e30
    token = 0
    for dist in expert_logp:
        for i, p in enumerate(dist):
            if p > peak:
                peak = p
                token = i
    return token


def quantile_expert(expert_logp: list[list[float]], anchor: int, q: float) -> int:
    if not 0.0 <= q <= 1.0:
        raise ValueError("q must be in [0, 1]")
    if not expert_logp:
        raise ValueError("expert pool is empty")
    matched = []
    for i, dist in enumerate(expert_logp):
        top = max(range(len(dist)), key=lambda t: dist[t])
        if top == anchor:
            matched.append((dist[anchor], i))
    if not matched:
        raise ValueError("no expert has the MaxPeak token as top-1")
    matched.sort()
    idx = min(len(matched) - 1, int(q * len(matched)))
    return matched[idx][1]
```

Build the pool offline by greedy filtered reference-token gains. Online, MaxPeak picks the anchor token and the quantile rule chooses among matching experts. Apply clipped forward-KL to the chosen expert's full next-token distribution.

## Critical Hyperparameters & Tuning Advice
- Do not cite +2.75/+1.67/+1.94 vs OPSD as beating the library VISTA bake-off (64.8→66.9).
- Highest-peak expert as a naive target is not the method.
