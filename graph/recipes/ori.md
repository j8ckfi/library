---
id: recipe:ori
type: recipe
title: 'Drift-aware streaming k-PCA low-rank LLM training'
method: method:ori
task: task:full-param-memory-efficient-pretrain
target_hardware: 'Paper: 1B LLaMA pretrain; RoBERTa-Base FT'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ori
---

# Drift-aware streaming k-PCA low-rank LLM training

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def oja_step(v: float, g: float, lr: float) -> float:
    if lr <= 0.0:
        raise ValueError('lr must be > 0')
    return v + lr * g
```

Do not retarget locked SOTA from this recipe.
