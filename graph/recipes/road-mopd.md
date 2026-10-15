---
id: recipe:road-mopd
type: recipe
title: Cross-teacher guarding for multi-teacher OPD
method: method:road-mopd
task: task:student-distillation
target_hardware: 'Paper: Qwen3-4B / 1.7B MOPD'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- road-mopd
---

# Cross-teacher guarding for multi-teacher OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def agreement_keep(routed_sign: int, aux_sign: int) -> float:
    if routed_sign not in (-1, 1) or aux_sign not in (-1, 1):
        raise ValueError("signs must be +/-1")
    return 1.0 if routed_sign == aux_sign else 0.0
```

Do not retarget locked SOTA from this recipe.
