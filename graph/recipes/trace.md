---
id: recipe:trace
type: recipe
title: "TRACE Rollout-Guided FP4 QAT"
method: method:trace
task: task:fp4-rl-train-rollout-alignment
target_hardware: "MoE RL box with a separate FP4 rollout engine; paper: Qwen3.5-35B-A3B class"
framework: "PyTorch RL host + FP4 rollout engine"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - trace
---

# TRACE Rollout-Guided FP4 QAT

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def cache_rollout_qparams(mantissa, scale):
    if scale is None or mantissa is None:
        raise ValueError("rollout mantissa and scale are required")
    return {"mantissa": mantissa, "scale": scale}
```

Align train-side FP4 rounding to cached rollout qparams. Up to 5.4× rollout. Do not retarget Quartet-II.
