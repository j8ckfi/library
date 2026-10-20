---
id: recipe:dfr
type: recipe
title: 'Distributional rewards for diffusion/flow FT'
method: method:dfr
task: task:posttrain-diffusion
target_hardware: 'Paper: SD3.5-M GenEval / OCR vs RAM and Flow-GRPO'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- dfr
---

# Distributional rewards for diffusion/flow FT

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def instantiations() -> tuple[str, ...]:
    return ('mmd', 'frechet', 'dreamsim')
```

Do not retarget locked SOTA from this recipe.
