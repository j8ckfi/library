---
id: recipe:ugpc
type: recipe
title: UGPC CoT-SFT Contraction
method: method:ugpc
task: task:student-distillation
target_hardware: 'Paper: Qwen3.5-4B/9B SFT; DAPO-17k teacher pool'
framework: PyTorch SFT; official UGPC
repo_url: https://github.com/Jackbrocp/Learning-More-by-Training-Less
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ugpc
---

# UGPC CoT-SFT Contraction

## Hardware & Environment Setup
- Official: `https://github.com/Jackbrocp/Learning-More-by-Training-Less`.
- `code_status: released` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def pool_ratio(rho: float) -> float:
    if not 0 < rho <= 1:
        raise ValueError("rho must be in (0, 1]")
    return rho
```

Contract then route. Do not retarget OPD.
