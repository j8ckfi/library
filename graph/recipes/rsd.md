---
id: recipe:rsd
type: recipe
title: 'Privileged retrospective on-policy self-distill'
method: method:rsd
task: task:privileged-teacher-opsd
target_hardware: 'Paper: Qwen3-8B / 14B, ALFWorld / ScienceWorld / SearchQA'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- rsd
---

# Privileged retrospective on-policy self-distill

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def teacher_context(hindsight: str, lessons: list[str]) -> str:
    if not hindsight:
        raise ValueError('empty hindsight')
    return hindsight + '\n' + '\n'.join(lessons)
```

Do not retarget locked SOTA from this recipe.
