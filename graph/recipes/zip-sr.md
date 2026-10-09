---
id: recipe:zip-sr
type: recipe
title: "ZIP-SR Preconditioner-Space Stochastic Rounding"
method: method:zip-sr
task: task:llm-pretraining-optimization
target_hardware: "AdamW pretrain/SFT; paper: 130M-2.7B"
framework: "PyTorch AdamW host"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - zip-sr
---

# ZIP-SR Preconditioner-Space Stochastic Rounding

## Hardware & Environment Setup
- No official GitHub as of 2026-10-09.
- `repo_url: none found`. `code_status: none`.

## Quickstart Implementation

```python
from __future__ import annotations

def include_zero(codebook):
    if 0.0 not in codebook:
        raise ValueError("ZIP-SR second-moment codebook must include zero")
    return list(codebook)
```

Round the second moment in preconditioner space. Do not retarget Muon2.
