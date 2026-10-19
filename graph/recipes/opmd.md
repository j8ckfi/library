---
id: recipe:opmd
type: recipe
title: 'On-policy mechanism distillation'
method: method:opmd
task: task:student-distillation
target_hardware: 'Paper: three teacher-student settings'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- opmd
---

# On-policy mechanism distillation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def compatible_state(teacher_h: float, student_scale: float) -> float:
    if student_scale <= 0.0:
        raise ValueError('student_scale must be > 0')
    return teacher_h * student_scale
```

Do not retarget locked SOTA from this recipe.
