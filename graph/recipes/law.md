---
id: recipe:law
type: recipe
title: 'Expected-embedding self-conditioning'
method: method:law
task: task:continuous-diffusion-lm-pretrain
target_hardware: 'Paper: Sudoku / Maze / TinyGSM continuous DLM'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- law
---

# Expected-embedding self-conditioning

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def mix_embed(prev, expected, gate: float):
    if not 0 <= gate <= 1:
        raise ValueError('gate')
    return (1.0 - gate) * prev + gate * expected
```

Do not retarget locked SOTA from this recipe.
