---
id: recipe:led
type: recipe
title: 'Lookahead editing SFT for masked dLLMs'
method: method:led
task: task:diffusion-lm-ar-delta-recycle
target_hardware: 'Paper: Qwen2.5-7B / Qwen3-8B MDM SFT'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- led
---

# Lookahead editing SFT for masked dLLMs

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def lookahead_steps(n: int) -> int:
    if n < 1:
        raise ValueError('need at least one lookahead step')
    return n
```

Do not retarget locked SOTA from this recipe.
