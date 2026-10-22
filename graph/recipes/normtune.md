---
id: recipe:normtune
type: recipe
title: 'Norm-guided PEFT scale'
method: method:normtune
task: task:lora-quality-tuning
target_hardware: 'Paper: LoRA / Bone / MoRA on AIME MATH GPQA'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- normtune
---

# Norm-guided PEFT scale

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def layer_boost(update_norm: float, full_ft_norm: float) -> float:
    if full_ft_norm <= 0:
        raise ValueError('full_ft_norm')
    return max(1.0, full_ft_norm / max(update_norm, 1e-8))
```

Do not retarget locked SOTA from this recipe.
