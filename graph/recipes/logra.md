---
id: recipe:logra
type: recipe
title: "LoGRA Low-Rank RL Sketches"
method: method:logra
task: task:full-param-memory-efficient-pretrain
target_hardware: "RL post-train node; paper: 27B on 8 GPUs, 1100+ steps"
framework: "PyTorch RL host with sketched gradients"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - logra
  - optimizer
---

# LoGRA Low-Rank RL Sketches

## Hardware & Environment Setup
- No official GitHub URL as of 2026-10-06 (`arXiv:2610.06647`). `repo_url: none found`. `code_status: none`.
- Pass@1 stays CISPO. Pretrain memory stays SCALE.

## Quickstart Implementation

```python
from __future__ import annotations

def predicted_kl_scale(pred_kl: float, cap: float) -> float:
    if cap <= 0:
        raise ValueError("cap must be positive")
    if pred_kl < 0:
        raise ValueError("predicted KL must be non-negative")
    if pred_kl == 0:
        return 1.0
    return min(1.0, cap / pred_kl)
```

Keep a low-rank sketch of the RL gradient. Before the step, estimate KL and multiply the update by `predicted_kl_scale`.

## Critical Hyperparameters & Tuning Advice
- Up to 45.7% RL memory. Do not retarget CISPO or SCALE.
