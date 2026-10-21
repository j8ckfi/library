---
id: recipe:projected-distillation
type: recipe
title: 'Near-on-policy correction of failed student traces'
method: method:projected-distillation
task: task:student-distillation
target_hardware: 'Paper: Qwen3-8B / OLMo-2-7B, five domains'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- projected-distillation
---

# Near-on-policy correction of failed student traces

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def edit_budget(failed: str, corrected: str) -> int:
    if not failed:
        raise ValueError('empty failed attempt')
    return abs(len(corrected) - len(failed))
```

Do not retarget locked SOTA from this recipe.
