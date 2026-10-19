---
id: recipe:gr-opd
type: recipe
title: 'Group-relative sequence credit OPD'
method: method:gr-opd
task: task:student-distillation
target_hardware: 'Paper: Qwen3 teacher-student math'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- gr-opd
---

# Group-relative sequence credit OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def collective_pressure(group_credit: list[float], keep: float) -> list[float]:
    if not group_credit:
        return []
    mean = sum(group_credit) / len(group_credit)
    return [(c - mean) + keep * mean for c in group_credit]
```

Do not retarget locked SOTA from this recipe.
