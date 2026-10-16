---
id: recipe:scoped
type: recipe
title: 'Skill-decoupled VLM expert OPD'
method: method:scoped
task: task:student-distillation
target_hardware: 'Paper: Qwen3-VL-8B/4B A800; EasyR1 + veRL'
framework: PyTorch
repo_url: https://github.com/NEUIR/SCOPED
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- scoped
---

# Skill-decoupled VLM expert OPD

## Hardware & Environment Setup
- Official: `https://github.com/NEUIR/SCOPED`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def student_prompt(image_query: str, skill: str | None) -> str:
    if not image_query:
        raise ValueError("image_query must be non-empty")
    if skill:
        raise ValueError("student inference must not see skills")
    return image_query
```

Do not retarget locked SOTA from this recipe.

