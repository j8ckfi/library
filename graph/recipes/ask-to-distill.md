---
id: recipe:ask-to-distill
type: recipe
title: 'Synthesize OPD questions without answers'
method: method:ask-to-distill
task: task:student-distillation
target_hardware: 'Paper: math / code / agentic OPD'
framework: PyTorch
repo_url: https://github.com/GasolSun36/Ask_to_Distill
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ask-to-distill
---

# Synthesize OPD questions without answers

## Hardware & Environment Setup
- Official: `https://github.com/GasolSun36/Ask_to_Distill`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def question_value(disagree: float, teacher_mass: float) -> float:
    if teacher_mass < 0:
        raise ValueError('mass')
    return disagree * teacher_mass
```

Do not retarget locked SOTA from this recipe.
