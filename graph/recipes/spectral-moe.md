---
id: recipe:spectral-moe
type: recipe
title: Heterogeneous per-layer expert utilization
method: method:spectral-moe
task: task:dense-to-moe-upcycling
target_hardware: 'Paper: Llama-2-7B / Llama-3-8B / Qwen2.5-7B conversion'
framework: PyTorch
repo_url: https://github.com/ZacharyBroveak/Spectral-MoE
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- spectral-moe
---

# Heterogeneous per-layer expert utilization

## Hardware & Environment Setup
- Official: `https://github.com/ZacharyBroveak/Spectral-MoE`.
- `code_status: announced` (README-only) as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def layer_budget(weights: list[float], total_active: int) -> list[int]:
    if total_active < 1 or not weights:
        raise ValueError("need positive budget and weights")
    s = sum(weights)
    if s <= 0.0:
        raise ValueError("weights must sum > 0")
    raw = [w / s * total_active for w in weights]
    return [max(1, int(round(x))) for x in raw]
```

Do not retarget locked SOTA from this recipe.
