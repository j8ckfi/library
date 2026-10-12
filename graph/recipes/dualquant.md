---
id: recipe:dualquant
type: recipe
title: DualQuant Calibration-Free W+A PTQ
method: method:dualquant
task: task:fp4-hardware-training
target_hardware: 'W4A4 PTQ; paper: Llama-3.1-8B RTX 4090 packed path'
framework: PyTorch PTQ
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- dualquant
---

# DualQuant Calibration-Free W+A PTQ

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def dual_scale_ok(weight_scale: float, act_scale: float) -> bool:
    if weight_scale <= 0 or act_scale <= 0:
        raise ValueError("DualQuant scales must be positive")
    return True
```

No calibration set. Do not retarget Quartet-II.
