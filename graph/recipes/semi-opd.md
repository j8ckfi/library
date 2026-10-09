---
id: recipe:semi-opd
type: recipe
title: "Semi-OPD Offline Initial-Student Rollouts"
method: method:semi-opd
task: task:student-distillation
target_hardware: "OPD host; paper: 1.5B-235B teacher-student pairs"
framework: "PyTorch OPD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - semi-opd
---

# Semi-OPD Offline Initial-Student Rollouts

## Hardware & Environment Setup
- No official GitHub as of 2026-10-09.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def choose_opd_rollout(overlap: float, high_overlap: float = 0.5) -> str:
    if not 0.0 <= overlap <= 1.0:
        raise ValueError("overlap must be in [0, 1]")
    if high_overlap <= 0 or high_overlap > 1:
        raise ValueError("high_overlap must be in (0, 1]")
    return "live" if overlap >= high_overlap else "semi" 
```

Freeze initial-student rollouts unless overlap is already high. Do not retarget OPD.
