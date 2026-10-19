---
id: recipe:topa
type: recipe
title: 'Block-wise Toeplitz adaptation'
method: method:topa
task: task:lora-quality-tuning
target_hardware: 'Paper: 21 NLP/CV datasets, 5 architectures'
framework: PyTorch
repo_url: https://github.com/scongl/ToPA
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- topa
---

# Block-wise Toeplitz adaptation

## Hardware & Environment Setup
- Official: `https://github.com/scongl/ToPA`.
- `code_status: released` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def block_count(dim: int, block: int) -> int:
    if block < 1 or dim < 1:
        raise ValueError('dim and block must be >= 1')
    return (dim + block - 1) // block
```

Do not retarget locked SOTA from this recipe.
