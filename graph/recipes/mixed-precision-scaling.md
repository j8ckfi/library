---
id: recipe:mixed-precision-scaling
type: recipe
title: Mixed Precision Scaling Laws for Quantized Pretraining
method: method:mixed-precision-scaling
task: task:fp4-hardware-training
target_hardware: 'Paper: Qwen3 up to 0.9B; 430M ablation at 12.8B tokens'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mixed-precision-scaling
---

# Mixed Precision Scaling Laws for Quantized Pretraining

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def keep_forward_high_precision(fwd_gap: float, bwd_gap: float) -> bool:
    if fwd_gap < 0 or bwd_gap < 0:
        raise ValueError("loss gaps must be non-negative")
    return fwd_gap > bwd_gap
```

Do not retarget locked SOTA from this recipe.
