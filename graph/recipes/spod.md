---
id: recipe:spod
type: recipe
title: 'Success-preserving agentic OPD'
method: method:spod
task: task:student-distillation
target_hardware: 'Paper: two families, three agentic benches'
framework: PyTorch
repo_url: https://github.com/Jike338/SPOD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- spod
---

# Success-preserving agentic OPD

## Hardware & Environment Setup
- Official: `https://github.com/Jike338/SPOD`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def mask_teacher(student_ok: bool, teacher_conflicts: bool) -> bool:
    return student_ok and teacher_conflicts
```

Do not retarget locked SOTA from this recipe.
