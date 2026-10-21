---
id: recipe:r2s
type: recipe
title: 'Reward-free teacher-scorer repair then OPD'
method: method:r2s
task: task:student-distillation
target_hardware: 'Paper: three environments, two teachers, four students'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- r2s
---

# Reward-free teacher-scorer repair then OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_state(n_pass: int, n_take: int, k: int = 1) -> bool:
    if n_take <= 0:
        raise ValueError('no takeovers')
    return n_pass >= k
```

Do not retarget locked SOTA from this recipe.
