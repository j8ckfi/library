---
id: recipe:ap-opd
type: recipe
title: 'Penalty-jump pullback for sampled-token OPD'
method: method:ap-opd
task: task:student-distillation
target_hardware: 'Paper: math and code OPD'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ap-opd
---

# Penalty-jump pullback for sampled-token OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def pullback(prev_mean: float, next_mean: float) -> float:
    if next_mean == 0:
        raise ValueError('empty next block')
    return prev_mean / next_mean
```

Do not retarget locked SOTA from this recipe.
