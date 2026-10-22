---
id: recipe:flat-rlvr
type: recipe
title: 'Sharpness-aware GRPO RLVR'
method: method:flat-rlvr
task: task:math-code-rl-dense
target_hardware: 'Paper: GRPO-family RLVR with sharpness-aware minimization'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- flat-rlvr
---

# Sharpness-aware GRPO RLVR

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def sam_scale(loss: float, rho: float) -> float:
    if rho < 0:
        raise ValueError('rho')
    return loss * (1.0 + rho)
```

Do not retarget locked SOTA from this recipe.
