---
id: recipe:simopd
type: recipe
title: 'Relational similarity OPD'
method: method:simopd
task: task:student-distillation
target_hardware: 'Paper: same- and cross-architecture OPD'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- simopd
---

# Relational similarity OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def match_similarity(student_sim: list[float], teacher_sim: list[float]) -> float:
    if len(student_sim) != len(teacher_sim) or not student_sim:
        raise ValueError('similarity banks must align')
    return sum((s - t) ** 2 for s, t in zip(student_sim, teacher_sim)) / len(student_sim)
```

Do not retarget locked SOTA from this recipe.
