---
id: recipe:hymuon
type: recipe
title: 'Hybrid-momentum Muon orthogonalization'
method: method:hymuon
task: task:llm-pretraining-optimization
target_hardware: 'Paper: IWSLT14; GPT-2 124M; LLaMA-1.3B C4'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- hymuon
---

# Hybrid-momentum Muon orthogonalization

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def hybrid_mom(linear_avg, ema, mix: float = 0.5):
    if not 0 <= mix <= 1:
        raise ValueError('mix')
    return mix * linear_avg + (1 - mix) * ema
```

Do not retarget locked SOTA from this recipe.
