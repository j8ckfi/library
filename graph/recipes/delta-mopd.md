---
id: recipe:delta-mopd
type: recipe
title: "Delta-MOPD Teacher-Minus-Base Logit Shifts"
method: method:delta-mopd
task: task:student-distillation
target_hardware: "MOPD host with teacher bases and a frozen student init"
framework: "PyTorch MOPD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - delta-mopd
---

# Delta-MOPD Teacher-Minus-Base Logit Shifts

## Hardware & Environment Setup
- No official GitHub as of 2026-10-09.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def shift_target_logits(teacher_logits, teacher_base_logits, student_init_logits):
    if len(teacher_logits) != len(teacher_base_logits) or len(teacher_logits) != len(student_init_logits):
        raise ValueError("logit vectors must align")
    return [s + (t - b) for s, t, b in zip(student_init_logits, teacher_logits, teacher_base_logits)]
```

Transfer the teacher-minus-base shift, not the endpoint. Do not retarget Open-MOPD.
