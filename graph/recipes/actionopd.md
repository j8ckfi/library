---
id: recipe:actionopd
type: recipe
title: Action-level OPD without teacher token probs
method: method:actionopd
task: task:student-distillation
target_hardware: 'Paper: Qwen3-4B/8B tool-use distill'
framework: PyTorch
repo_url: https://github.com/thu-nics/ActionOPD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- actionopd
---

# Action-level OPD without teacher token probs

## Hardware & Environment Setup
- Official: `https://github.com/thu-nics/ActionOPD`.
- `code_status: released` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def action_agreement(student_action: str, teacher_action: str) -> float:
    if not student_action or not teacher_action:
        raise ValueError("empty action")
    return 1.0 if student_action.strip() == teacher_action.strip() else 0.0
```

Do not retarget locked SOTA from this recipe.
