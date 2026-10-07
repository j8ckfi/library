---
id: recipe:a2d
type: recipe
title: "A2D AR-Delta Recycle onto a Converted dLLM"
method: method:a2d
task: task:diffusion-lm-ar-delta-recycle
target_hardware: "Converted dLLM plus an AR post-training delta"
framework: "PyTorch dLLM host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - a2d
---

# A2D AR-Delta Recycle onto a Converted dLLM

## Hardware & Environment Setup
- No official GitHub as of 2026-10-07.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def apply_ar_delta(dllm_base, ar_delta, scale: float = 1.0):
    if scale < 0:
        raise ValueError("scale must be non-negative")
    return dllm_base + scale * ar_delta
```

Add the AR post-training delta to the converted dLLM. Composes with later diffusion PT. Do not retarget CanvasAnneal.
