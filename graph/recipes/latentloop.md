---
id: recipe:latentloop
type: recipe
title: Asymmetric compute looped MoE
method: method:latentloop
task: task:compute-matched-moe-looped-pretrain
target_hardware: 'Paper: 1.3B-7B looped MoE, up to >10^21 FLOPs'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- latentloop
---

# Asymmetric compute looped MoE

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def reallocate_width(saved_frac: float, base_width: int) -> int:
    if saved_frac < 0.0 or base_width < 1:
        raise ValueError("saved_frac >= 0 and base_width >= 1")
    return max(base_width, int(base_width * (1.0 + saved_frac)))
```

Do not retarget locked SOTA from this recipe.
