---
id: recipe:harness-scaling
type: recipe
title: 'Factorial harness RL subset'
method: method:harness-scaling
task: task:agentic-rsi-routing-posttrain
target_hardware: 'Paper: multi-scale agentic RL across harness configurations'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- harness-scaling
---

# Factorial harness RL subset

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def factorial_cover(factors, k: int):
    if k <= 0:
        raise ValueError('k')
    return list(factors)[:k]
```

Do not retarget locked SOTA from this recipe.
