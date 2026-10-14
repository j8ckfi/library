---
id: recipe:vsr
type: recipe
title: VSR Neyman prefix resampling
method: method:vsr
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen2.5-7B math; Qwen2.5-1.5B BabyAI/Sokoban'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- vsr
---

# VSR Neyman prefix resampling

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def neyman_mass(occupancy: float, residual_std: float) -> float:
    if occupancy < 0 or residual_std < 0:
        raise ValueError("occupancy and std must be non-negative")
    return occupancy * residual_std
```

Do not retarget locked SOTA from this recipe.
