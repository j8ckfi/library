---
id: recipe:mend
type: recipe
title: "MEND Proximal Velocity Matching"
method: method:mend
task: task:posttrain-diffusion
target_hardware: "flow-model reward box; paper: ~100 updates vs Flow-GRPO ~4k"
framework: "PyTorch flow trainer"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - mend
  - diffusion
---

# MEND Proximal Velocity Matching

## Hardware & Environment Setup
- No official GitHub URL as of 2026-10-06 (`arXiv:2610.05954`). `repo_url: none found`. `code_status: none`.
- Image OPSD stays DiffusionOPSD. Teacher-free flow stays Self-OPD.

## Quickstart Implementation

```python
from __future__ import annotations

def accept_move(reward_gain: float, displacement: float, price: float) -> bool:
    if displacement < 0 or price < 0:
        raise ValueError("displacement and price must be non-negative")
    return reward_gain > price * (displacement ** 2)
```

Cap rewards in the prompt group. Propose a reward-gradient move only below the cap. Accept with `accept_move`. Regress the flow onto the accepted velocity. No KL.

## Critical Hyperparameters & Tuning Advice
- 100 updates vs Flow-GRPO ~4k; 5/6 evaluators. Do not retarget Self-OPD.
