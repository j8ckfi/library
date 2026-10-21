---
id: recipe:par
type: recipe
title: 'Progress-aligned looped recurrence'
method: method:par
task: task:recurrent-encoder-decoder-lm
target_hardware: 'Paper: Qwen2.5-0.5B swap-S5'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- par
---

# Progress-aligned looped recurrence

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def rescale_to_first(state, first_norm: float):
    n = float(state.abs().mean()) if hasattr(state, 'abs') else float(abs(state))
    if n == 0:
        raise ValueError('zero state')
    return state * (first_norm / n)
```

Do not retarget locked SOTA from this recipe.
