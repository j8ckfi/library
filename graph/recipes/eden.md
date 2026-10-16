---
id: recipe:eden
type: recipe
title: 'Anchored embedding-space RLVR exploration'
method: method:eden
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen2.5-0.5B / Math-1.5B / Math-7B, 8x H100, verl'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- eden
---

# Anchored embedding-space RLVR exploration

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def split_group(n: int, n_noise: int) -> tuple[int, int]:
    if n_noise < 0 or n_noise >= n:
        raise ValueError("n_noise must be in [0, n)")
    return n - n_noise, n_noise
```

Do not retarget locked SOTA from this recipe.

