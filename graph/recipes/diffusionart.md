---
id: recipe:diffusionart
type: recipe
title: DiffusionART Aggregation-First Reward Tilting
method: method:diffusionart
task: task:posttrain-diffusion
target_hardware: 'Video/image diffusion RL host; paper: HunyuanVideo-13B'
framework: PyTorch diffusion RL; official DiffusionART
repo_url: https://github.com/vanzll/DiffusionART
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- diffusionart
---

# DiffusionART Aggregation-First Reward Tilting

## Hardware & Environment Setup
- Official: `https://github.com/vanzll/DiffusionART`.
- `code_status: released` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def aggregate_prompt_rewards(rewards: list[float]) -> float:
    if not rewards:
        raise ValueError("empty prompt group")
    return sum(rewards) / len(rewards)
```

Tilt reverse-process states with the shared direction. Do not retarget DiffusionOPSD.
