---
id: recipe:traceforge
type: recipe
title: 'Family-native trace regeneration'
method: method:traceforge
task: task:student-distillation
target_hardware: 'Paper: five-benchmark distill when teacher traces are withheld'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- traceforge
---

# Family-native trace regeneration

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def use_trace(context: str, answer: str) -> str:
    if not answer:
        raise ValueError('answer')
    return f'{context}\n{answer}'
```

Do not retarget locked SOTA from this recipe.
