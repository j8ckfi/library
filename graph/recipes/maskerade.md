---
id: recipe:maskerade
type: recipe
title: "MASKerade Mask-Expert Upcycling"
method: method:maskerade
task: task:dense-to-moe-upcycling
target_hardware: "Dense FFN checkpoint; official MASKerade"
framework: "PyTorch; official MASKerade"
repo_url: "https://github.com/Ming-K9/MASKerade"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - maskerade
---

# MASKerade Mask-Expert Upcycling

## Hardware & Environment Setup
- Official: `https://github.com/Ming-K9/MASKerade`.
- `code_status: released` as of 2026-10-07.

## Quickstart Implementation

```python
from __future__ import annotations

def top2(mask_logits):
    if mask_logits.numel() < 2:
        raise ValueError("need at least two mask experts")
    return mask_logits.topk(2).indices
```

Official: Ming-K9/MASKerade. Four 2:4 experts, top-2, frozen FFN. Do not retarget DeepSeek-V4.
