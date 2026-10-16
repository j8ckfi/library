---
id: recipe:rpo
type: recipe
title: 'Attention-routing diffusion RL'
method: method:rpo
task: task:posttrain-diffusion
target_hardware: 'Paper: text-to-image and text-to-video online RL'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- rpo
---

# Attention-routing diffusion RL

## Hardware & Environment Setup
- Official: `none found`. Project: `https://velox-world.com/rpo`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def route_keep(attn_mass: float, keep_self: bool) -> str:
    if attn_mass < 0.0:
        raise ValueError("attn_mass must be >= 0")
    if keep_self:
        return "dense"
    return "sample"
```

Do not retarget locked SOTA from this recipe.

