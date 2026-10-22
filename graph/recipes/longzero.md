---
id: recipe:longzero
type: recipe
title: 'Self-proposed long-context RL tasks'
method: method:longzero
task: task:data-free-self-evolution
target_hardware: 'Paper: long-context reasoning RL from zero external data'
framework: PyTorch
repo_url: https://github.com/zhennan1/LongZero
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- longzero
---

# Self-proposed long-context RL tasks

## Hardware & Environment Setup
- Official: `https://github.com/zhennan1/LongZero`.
- `code_status: released` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_task(length: int, min_len: int, verifiable: bool) -> bool:
    if min_len <= 0:
        raise ValueError('min_len')
    return verifiable and length >= min_len
```

Do not retarget locked SOTA from this recipe.
