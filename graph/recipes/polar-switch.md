---
id: recipe:polar-switch
type: recipe
title: 'Polar-circuit Muon orthogonalization'
method: method:polar-switch
task: task:llm-pretraining-optimization
target_hardware: 'Paper: Modded-NanoGPT #91, Qwen3-0.6B, Gemma 3-1B'
framework: PyTorch
repo_url: https://github.com/zhehangdu/polar-switch
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- polar-switch
---

# Polar-circuit Muon orthogonalization

## Hardware & Environment Setup
- Official: `https://github.com/zhehangdu/polar-switch`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def circuit_degree(k_products: int) -> int:
    if k_products < 0:
        raise ValueError('k_products must be >= 0')
    return 2 ** (k_products + 1) + 1
```

Do not retarget locked SOTA from this recipe.
