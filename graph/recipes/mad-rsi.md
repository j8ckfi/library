---
id: recipe:mad-rsi
type: recipe
title: 'Shared harness RSI across heterogeneous LLMs'
method: method:mad-rsi
task: task:agent-harness-runtime
target_hardware: 'Paper: multiple datasets and LLMs'
framework: PyTorch
repo_url: https://github.com/cuiyu-ai/MaD-RSI
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mad-rsi
---

# Shared harness RSI across heterogeneous LLMs

## Hardware & Environment Setup
- Official: `https://github.com/cuiyu-ai/MaD-RSI`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def shared_harness_batch(models: list[str]) -> int:
    if len(models) < 2:
        raise ValueError('need heterogeneous models')
    return len(models)
```

Do not retarget locked SOTA from this recipe.
