---
id: recipe:doobpo
type: recipe
title: 'Doob-ratio then drift distill'
method: method:doobpo
task: task:posttrain-diffusion
target_hardware: 'Paper: diffusion/flow robot and sequential-decision policies'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- doobpo
---

# Doob-ratio then drift distill

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def ratio_clip(r: float, cap: float) -> float:
    if cap <= 0:
        raise ValueError('cap')
    return min(max(r, 0.0), cap)
```

Do not retarget locked SOTA from this recipe.
