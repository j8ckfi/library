---
id: recipe:ppo-fp16
type: recipe
title: Structure-Aware Half-Precision PPO
method: method:ppo-fp16
task: task:continuous-control-world-model
target_hardware: 'Commodity GPU PPO; paper: six continuous-control tasks'
framework: PyTorch PPO
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ppo-fp16
---

# Structure-Aware Half-Precision PPO

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def policy_change_residual(logp_now: float, logp_behavior: float) -> float:
    return logp_now - logp_behavior
```

Protect the residual, not the whole graph. Do not retarget EfficientTDMPC.
