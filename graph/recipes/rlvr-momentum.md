---
id: recipe:rlvr-momentum
type: recipe
title: Scale RLVR EMA beta with learning rate
method: method:rlvr-momentum
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen3-4B-Base GRPO / Qwen2.5-32B AdamW'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- rlvr-momentum
---

# Scale RLVR EMA beta with learning rate

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def beta_for_lr(eta: float, safe_ratio: float, eta_ref: float = 1e-6) -> float:
    if eta <= 0.0 or safe_ratio <= 0.0 or eta_ref <= 0.0:
        raise ValueError("eta, safe_ratio, and eta_ref must be positive")
    beta = 1.0 - (eta / safe_ratio)
    if not 0.0 < beta < 1.0:
        raise ValueError("resulting beta must be in (0, 1)")
    return beta
```

Do not retarget locked SOTA from this recipe.
