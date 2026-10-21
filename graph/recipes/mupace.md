---
id: recipe:mupace
type: recipe
title: 'Meta-learned Muon step-size for LoRA'
method: method:mupace
task: task:lora-quality-tuning
target_hardware: 'Paper: 64 LoRA FT problems; transfer to 32B / 27B'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mupace
---

# Meta-learned Muon step-size for LoRA

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def bound_scale(raw: float, lo: float = 0.25, hi: float = 4.0) -> float:
    if lo <= 0 or hi <= lo:
        raise ValueError('bounds')
    return min(hi, max(lo, raw))
```

Do not retarget locked SOTA from this recipe.
