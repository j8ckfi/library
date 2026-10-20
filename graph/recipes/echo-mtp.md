---
id: recipe:echo-mtp
type: recipe
title: 'Causal self-recursion MTP'
method: method:echo-mtp
task: task:diffusion-augmented-ar
target_hardware: 'Paper: ECHO vs auxiliary MTP pretrain and speculative decode'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- echo-mtp
---

# Causal self-recursion MTP

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def dds_prob(depth: int, decay: float) -> float:
    if depth < 1 or not 0 < decay <= 1:
        raise ValueError('depth >= 1 and decay in (0, 1]')
    return decay ** (depth - 1)
```

Do not retarget locked SOTA from this recipe.
