---
id: recipe:drmoet
type: recipe
title: "DRMoET Distributionally Robust MoE Objective"
method: method:drmoet
task: task:pretrain-moe-frontier
target_hardware: "MoE NTP box; paper: FLAME-MoE 746M / 10.3B"
framework: "PyTorch MoE trainer; official DRMoET"
repo_url: "https://github.com/MAPS-research/DRMoET"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - drmoet
---

# DRMoET Distributionally Robust MoE Objective

## Hardware & Environment Setup
- Official: `https://github.com/MAPS-research/DRMoET`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def dro_residual(expert_load, target, radius: float):
    if radius < 0:
        raise ValueError("radius must be non-negative")
    gap = expert_load - target
    return gap.clamp(min=-radius, max=radius)
```

Official: MAPS-research/DRMoET. Drop-in vs standard load-balancing. Do not retarget DeepSeek-V4 / Kimi-K3.
