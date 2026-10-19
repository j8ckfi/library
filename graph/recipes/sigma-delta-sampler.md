---
id: recipe:sigma-delta-sampler
type: recipe
title: 'Ising-style Sigma-Delta discrete-weight training'
method: method:sigma-delta-sampler
task: task:1bit-extreme-quantization
target_hardware: 'Paper: MatMul-free discrete nets to 2.7B'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- sigma-delta-sampler
---

# Ising-style Sigma-Delta discrete-weight training

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def sigma_delta_quant(residual: float, threshold: float) -> int:
    if threshold <= 0.0:
        raise ValueError('threshold must be > 0')
    if residual > threshold:
        return 1
    if residual < -threshold:
        return -1
    return 0
```

Do not retarget locked SOTA from this recipe.
