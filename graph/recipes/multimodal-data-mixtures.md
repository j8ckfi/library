---
id: recipe:multimodal-data-mixtures
type: recipe
title: Multimodal Data-Mixture Scaling Laws
method: method:multimodal-data-mixtures
task: task:open-data-recipe
target_hardware: 'Paper: 268 MoE runs, 457M–8.3B, up to 150B tokens'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- multimodal-data-mixtures
---

# Multimodal Data-Mixture Scaling Laws

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def nontext_repeats_ok(repeats: float) -> bool:
    if repeats < 1:
        raise ValueError("repetition ratio must be >= 1")
    return repeats <= 2.0
```

Do not retarget locked SOTA from this recipe.
