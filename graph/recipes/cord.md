---
id: recipe:cord
type: recipe
title: 'Conflict-aware RL+distill projection'
method: method:cord
task: task:student-distillation
target_hardware: 'Paper: ALFWorld / WebShop joint RL+OPSD recipes'
framework: PyTorch
repo_url: https://github.com/LvAoAo/CORD-release
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- cord
---

# Conflict-aware RL+distill projection

## Hardware & Environment Setup
- Official: `https://github.com/LvAoAo/CORD-release`.
- `code_status: released` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def project_conflict(g_protect, g_other, fire: bool):
    if not fire:
        return g_protect, g_other
    return g_protect, type(g_other)()
```

Do not retarget locked SOTA from this recipe.
