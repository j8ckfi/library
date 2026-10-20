---
id: recipe:t-muon
type: recipe
title: 't-SVD Muon tensor update'
method: method:t-muon
task: task:llm-pretraining-optimization
target_hardware: 'Paper: 51M-1.3B FineWeb GPT-2 / LLaMA-style'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- t-muon
---

# t-SVD Muon tensor update

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def stack_heads(grads: list) -> int:
    if not grads:
        raise ValueError('empty head group')
    return len(grads)
```

Do not retarget locked SOTA from this recipe.
