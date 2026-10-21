---
id: recipe:dstill
type: recipe
title: 'One-step block-diffusion drafter distillation'
method: method:dstill
task: task:diffusion-augmented-ar
target_hardware: 'Paper: three model families, reasoning/math/code'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- dstill
---

# One-step block-diffusion drafter distillation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def mask_frac(step: int, n: int) -> float:
    if n <= 0:
        raise ValueError('n')
    return min(1.0, step / n)
```

Do not retarget locked SOTA from this recipe.
