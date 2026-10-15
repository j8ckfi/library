---
id: recipe:pmrc
type: recipe
title: PMRC projected Muon with residual correction
method: method:pmrc
task: task:full-param-memory-efficient-pretrain
target_hardware: 'Paper: LLaMA 1.3B on 8x H20; 60M/150M on 2x RTX PRO 6000'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- pmrc
---

# PMRC projected Muon with residual correction

## Hardware & Environment Setup
- Official dedicated repo: `none found`. Experiments used `https://github.com/OptimAI-Lab/Minimalist_LLM_Pretraining`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def residual_update(projected: float, residual: float) -> float:
    return projected + residual
```

Do not retarget locked SOTA from this recipe.
