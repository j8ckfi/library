---
id: recipe:flashmask-3
type: recipe
title: 'Mask-aware distributed attention'
method: method:flashmask-3
task: task:llm-pretraining-optimization
target_hardware: 'Paper: H100; 118B-A14B on 128 H100'
framework: Paddle
repo_url: https://github.com/PaddlePaddle/FlashMask
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- flashmask-3
---

# Mask-aware distributed attention

## Hardware & Environment Setup
- Official: `https://github.com/PaddlePaddle/FlashMask`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def clip_shift_max(lo: int, hi: int, rank_start: int, rank_end: int) -> tuple[int, int]:
    if rank_end <= rank_start:
        raise ValueError("rank window must be positive")
    a = max(lo, rank_start)
    b = min(hi, rank_end)
    return a - rank_start, b - rank_start
```

Do not retarget locked SOTA from this recipe.

