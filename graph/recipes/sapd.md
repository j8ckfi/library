---
id: recipe:sapd
type: recipe
title: "SAPD Step-Aligned Privileged Distillation"
method: method:sapd
task: task:privileged-teacher-opsd
target_hardware: "Offline distill host with stepwise reference solutions"
framework: "PyTorch distill host; official SAPD"
repo_url: "https://github.com/Miaow-Lab/SAPD"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - sapd
---

# SAPD Step-Aligned Privileged Distillation

## Hardware & Environment Setup
- Official: `https://github.com/Miaow-Lab/SAPD`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

def step_context(solution_steps, t: int) -> list:
    if t < 0 or t >= len(solution_steps):
        raise ValueError("step index out of range")
    return list(solution_steps[t:])
```

Privileged remaining-solution context at the current step only. Do not retarget VISTA.
