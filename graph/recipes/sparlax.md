---
id: recipe:sparlax
type: recipe
title: 'Sparse-relaxed soft-CoT RL'
method: method:sparlax
task: task:math-code-rl-dense
target_hardware: 'Paper: nine reasoning benchmarks'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- sparlax
---

# Sparse-relaxed soft-CoT RL

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def entmax_keep(p, k: int) -> int:
    if k <= 0:
        raise ValueError('k')
    return min(k, len(p))
```

Do not retarget locked SOTA from this recipe.
