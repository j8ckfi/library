---
id: recipe:nvfp4-pretrain-recipe
type: recipe
title: 'NVFP4 pretrain ingredient stack'
method: method:nvfp4-pretrain-recipe
task: task:fp4-hardware-training
target_hardware: 'Paper: Nemotron 8B dense and 30B-A3B, up to 1T tokens'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- nvfp4-pretrain-recipe
---

# NVFP4 pretrain ingredient stack

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_high_precision_layers(selective: bool) -> bool:
    if not selective:
        raise ValueError('paper: selective high-precision layers are required at this scale')
    return True
```

Do not retarget locked SOTA from this recipe.
