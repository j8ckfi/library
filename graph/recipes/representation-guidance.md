---
id: recipe:representation-guidance
type: recipe
title: Representation Guidance Pixel DiT
method: method:representation-guidance
task: task:pixel-diffusion-pretrain
target_hardware: 'Paper: ImageNet-256 XL/16 and ImageNet-512 DiT'
framework: PyTorch flow matching; official RG
repo_url: https://github.com/Pan-Zihao/Representation-Guidance
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- representation-guidance
---

# Representation Guidance Pixel DiT

## Hardware & Environment Setup
- Official: `https://github.com/Pan-Zihao/Representation-Guidance`.
- `code_status: released` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def apply_offset(velocity, offset):
    if offset is None:
        raise ValueError("RG offset is required")
    return velocity + offset
```

Pixel-space DiT. Do not retarget DiffusionOPSD.
