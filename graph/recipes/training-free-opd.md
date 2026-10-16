---
id: recipe:training-free-opd
type: recipe
title: 'Forward-only specialist fusion'
method: method:training-free-opd
task: task:student-distillation
target_hardware: 'Paper: Olmo 3 7B specialists; a few GPU-hours of forwards'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- training-free-opd
---

# Forward-only specialist fusion

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def fused_weight(xtx: list[list[float]], xty: list[list[float]]) -> str:
    if not xtx or not xty:
        raise ValueError("second-moment blocks must be non-empty")
    return "solve X^T X W = X^T Y"
```

Do not retarget locked SOTA from this recipe.

