---
id: recipe:scaling-repeated-data
type: recipe
title: Scaling Repeated-Data Pretraining
method: method:scaling-repeated-data
task: task:data-constrained-pretrain
target_hardware: 'Paper: 153M and 1.5B dense multi-epoch'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- scaling-repeated-data
---

# Scaling Repeated-Data Pretraining

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def prefer_small_batch(unique_epochs: int, batch: int) -> bool:
    if unique_epochs < 1 or batch < 1:
        raise ValueError("epochs and batch must be positive")
    return unique_epochs >= 2 and batch <= 64
```

Do not retarget locked SOTA from this recipe.
