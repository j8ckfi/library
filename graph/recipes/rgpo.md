---
id: recipe:rgpo
type: recipe
title: "RGPO Adaptive Rationale Scaffolding"
method: method:rgpo
task: task:math-code-rl-dense
target_hardware: "Sparse-reward RLVR box with GT rationales; official RGPO"
framework: "PyTorch RLVR host; official RGPO"
repo_url: "https://github.com/VietHoang1512/rgpo"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - rgpo
---

# RGPO Adaptive Rationale Scaffolding

## Hardware & Environment Setup
- Official: `https://github.com/VietHoang1512/rgpo`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def guidance_weight(sigma0_sq: float, rmax: float, delta: float, horizon: int) -> float:
    if horizon <= 0 or rmax < 0 or sigma0_sq < 0:
        raise ValueError("horizon, rmax, sigma0_sq must be valid")
    denom = sigma0_sq + (rmax ** 2) * (delta ** 2) * horizon
    if denom == 0:
        raise ValueError("degenerate guidance variance")
    return sigma0_sq / denom
```

Official: VietHoang1512/rgpo. λ* from paper:ga-grpo. Do not retarget CISPO.
