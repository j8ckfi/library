---
id: recipe:riseharness
type: recipe
title: 'Frozen-weight terminal harness self-evolution'
method: method:riseharness
task: task:agent-harness-runtime
target_hardware: 'Paper: long-horizon terminal agents, frozen weights'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- riseharness
---

# Frozen-weight terminal harness self-evolution

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def is_flip_pool(n_ok: int, n_fail: int) -> bool:
    if n_ok + n_fail <= 0:
        raise ValueError('empty')
    return n_ok > 0 and n_fail > 0
```

Do not retarget locked SOTA from this recipe.
