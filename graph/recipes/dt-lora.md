---
id: recipe:dt-lora
type: recipe
title: DT-LoRA dynamic tangent branch
method: method:dt-lora
task: task:lora-quality-tuning
target_hardware: 'Paper: VTAB-1K and COCO r=16'
framework: PyTorch
repo_url: https://github.com/Snipine/DT-LoRA
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- dt-lora
---

# DT-LoRA dynamic tangent branch

## Hardware & Environment Setup
- Official: `https://github.com/Snipine/DT-LoRA`.
- `code_status: announced` as of 2026-10-14.

- Stub repo (README/hashes) as of 2026-10-14.

## Quickstart Implementation

```python
from __future__ import annotations

def split_rank(rank: int, dynamic: int) -> tuple[int, int]:
    if rank < 2 or dynamic < 1 or dynamic >= rank:
        raise ValueError("need rank >= 2 and 1 <= dynamic < rank")
    return rank - dynamic, dynamic
```

Do not retarget locked SOTA from this recipe.
