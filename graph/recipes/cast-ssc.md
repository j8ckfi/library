---
id: recipe:cast-ssc
type: recipe
title: CAST history-adaptive spectral clipping
method: method:cast-ssc
task: task:llm-pretraining-optimization
target_hardware: 'Paper: 19.08B MoE, 5000 steps, 64 devices ~0.6x H100'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- cast-ssc
---

# CAST history-adaptive spectral clipping

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def ema_threshold(h_old: float, spectral_norm: float, decay: float = 0.99) -> float:
    if not 0.0 < decay < 1.0:
        raise ValueError("decay must be in (0, 1)")
    if spectral_norm < 0.0:
        raise ValueError("spectral norm must be non-negative")
    return decay * h_old + (1.0 - decay) * spectral_norm
```

Do not retarget locked SOTA from this recipe.
