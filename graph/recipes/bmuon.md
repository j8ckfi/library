---
id: recipe:bmuon
type: recipe
title: 'Budgeted Muon spectral geometry'
method: method:bmuon
task: task:llm-pretraining-optimization
target_hardware: 'Paper: ViT-S/16; 1B LLaMA-style FineWeb'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- bmuon
---

# Budgeted Muon spectral geometry

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def channel_budget(block_mass: list[float], budget: float) -> list[float]:
    total = sum(block_mass) or 1.0
    scale = min(1.0, budget / total)
    return [m * scale for m in block_mass]
```

Do not retarget locked SOTA from this recipe.
