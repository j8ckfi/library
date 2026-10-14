---
id: recipe:justopd
type: recipe
title: JustOPD AR-to-dLLM on-policy distillation
method: method:justopd
task: task:diffusion-lm-ar-delta-recycle
target_hardware: 'Paper: Dream-7B student / Qwen3-14B teacher'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- justopd
---

# JustOPD AR-to-dLLM on-policy distillation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def length_ok(gen_len: int) -> bool:
    if gen_len < 1:
        raise ValueError("generation length must be positive")
    return gen_len in (256, 512, 1024)
```

Do not retarget locked SOTA from this recipe.
