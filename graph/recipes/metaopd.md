---
id: recipe:metaopd
type: recipe
title: "MetaOPD Bilevel Token Weighting"
method: method:metaopd
task: task:student-distillation
target_hardware: "OPD host with a frozen teacher and a held-out reference split; paper: 0.6B / 1.7B students"
framework: "PyTorch OPD host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - metaopd
---

# MetaOPD Bilevel Token Weighting

## Hardware & Environment Setup
- No official GitHub as of 2026-10-09.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

from math import tanh

def unit_mean_residual_weights(scores, mask, rho: float = 0.25):
    if rho <= 0:
        raise ValueError("rho must be positive")
    n = float(sum(mask))
    if n <= 0:
        raise ValueError("no valid tokens")
    mean = sum(s * m for s, m in zip(scores, mask)) / n
    raw = [1.0 + rho * tanh(s - mean) if m else 0.0 for s, m in zip(scores, mask)]
    total = sum(raw)
    if total == 0:
        raise ValueError("weights vanished")
    return [w * n / total for w in raw]
```

Keep reverse-KL matching. Learn the token map from post-update validation loss. Do not retarget OPD.
