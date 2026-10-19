---
id: recipe:moevolve
type: recipe
title: 'MoE bidirectional on-policy distillation'
method: method:moevolve
task: task:math-code-rl-moe
target_hardware: 'Paper: MoE models with expandable k'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- moevolve
---

# MoE bidirectional on-policy distillation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def activation_budget(train_k: int, infer_k: int, stage: str) -> int:
    if stage not in {'expand', 'distill'}:
        raise ValueError(stage)
    return train_k if stage == 'expand' else infer_k
```

Do not retarget locked SOTA from this recipe.
