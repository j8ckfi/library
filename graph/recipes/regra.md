---
id: recipe:regra
type: recipe
title: Two-stage residual-gradient LoRA
method: method:regra
task: task:lora-quality-tuning
target_hardware: 'Paper: RoBERTa GLUE / Llama-3-8B math'
framework: PyTorch
repo_url: https://github.com/Fanyao-Li/ReGRA
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- regra
---

# Two-stage residual-gradient LoRA

## Hardware & Environment Setup
- Official: `https://github.com/Fanyao-Li/ReGRA`.
- `code_status: released` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def residual_grad(grad: float, proj_on_stage1: float) -> float:
    return grad - proj_on_stage1
```

Do not retarget locked SOTA from this recipe.
