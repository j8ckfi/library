---
id: recipe:epic
type: recipe
title: 'Prefix reverse-KL clip'
method: method:epic
task: task:math-code-rl-dense
target_hardware: 'Paper: off-policy RL on a sparse MoE reasoner'
framework: PyTorch
repo_url: https://github.com/LiChengxi666/EPIC
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- epic
---

# Prefix reverse-KL clip

## Hardware & Environment Setup
- Official: `https://github.com/LiChengxi666/EPIC`.
- `code_status: released` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

import math

def prefix_rkld_coord(r: float) -> float:
    if r <= 0:
        raise ValueError('r')
    return r - 1.0 - math.log(r)
```

Do not retarget locked SOTA from this recipe.
