---
id: recipe:ccr
type: recipe
title: 'Concurrent Constraint Reinforcement short-window RLVR'
method: method:ccr
task: task:math-code-rl-dense
target_hardware: 'Paper: 4B and 8B math RLVR'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ccr
---

# Concurrent Constraint Reinforcement short-window RLVR

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def concurrent_slots(problems: list[str], k: int = 3) -> list[str]:
    if k < 1:
        raise ValueError('k must be >= 1')
    return problems[:k]
```

Do not retarget locked SOTA from this recipe.
