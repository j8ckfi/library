---
id: recipe:ase
type: recipe
title: 'Activation-space RLVR rollout steering'
method: method:ase
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen3-1.7B-Base / 8B-Base, DAPO-Math-17k'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ase
---

# Activation-space RLVR rollout steering

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def steer(h, v, alpha: float = 1.0):
    if v is None:
        raise ValueError('empty steering vector')
    return h + alpha * v
```

Do not retarget locked SOTA from this recipe.
