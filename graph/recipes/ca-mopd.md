---
id: recipe:ca-mopd
type: recipe
title: 'Capability-aware multi-teacher OPD allocation'
method: method:ca-mopd
task: task:student-distillation
target_hardware: 'Paper: six math/code/IF benches'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ca-mopd
---

# Capability-aware multi-teacher OPD allocation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def gap_scale(teacher_acc: float, student_acc: float) -> float:
    if teacher_acc <= 0:
        raise ValueError('empty teacher')
    return max(0.0, teacher_acc - student_acc)
```

Do not retarget locked SOTA from this recipe.
