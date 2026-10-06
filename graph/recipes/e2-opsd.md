---
id: recipe:e2-opsd
type: recipe
title: "E2-OPSD Entropy-Overshoot Fix"
method: method:e2-opsd
task: task:privileged-teacher-opsd
target_hardware: "OPSD host with a retrieval pool of solved neighbors"
framework: "PyTorch privileged-OPSD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - e2-opsd
  - distillation
---

# E2-OPSD Entropy-Overshoot Fix

## Hardware & Environment Setup
- No official GitHub as of 2026-10-06 (`arXiv:2610.05048`). `repo_url: none found`. `code_status: none`.
- Privileged first hop stays VISTA.

## Quickstart Implementation

```python
from __future__ import annotations

def entropy_gap(student_h: float, teacher_h: float) -> float:
    return student_h - teacher_h
```

Retrieve a solved neighbor for the teacher context. Scale each token's distillation by `entropy_gap` (overshoot → pull back). Do not condition the teacher on the current gold answer.

## Critical Hyperparameters & Tuning Advice
- Up to +4.3 mean@16 vs OPSD. Do not retarget VISTA.
