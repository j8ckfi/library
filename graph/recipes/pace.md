---
id: recipe:pace
type: recipe
title: 'Periodic 4-bit recurrent-state round'
method: method:pace
task: task:linear-time-sequence-modeling
target_hardware: 'Paper: linear-attention LMs 4B-35B decode'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- pace
---

# Periodic 4-bit recurrent-state round

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def should_round(step: int, period: int) -> bool:
    if period <= 0:
        raise ValueError('period')
    return step % period == 0
```

Do not retarget locked SOTA from this recipe.
