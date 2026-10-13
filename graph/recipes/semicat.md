---
id: recipe:semicat
type: recipe
title: SemiCat Continuous Diffusion LM
method: method:semicat
task: task:continuous-diffusion-lm-pretrain
target_hardware: 'Paper: TinyGSM plus 1.7B likelihood evals'
framework: PyTorch continuous diffusion LM; no public trainer
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- semicat
---

# SemiCat Continuous Diffusion LM

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def interpolant_levels(kind: str) -> int:
    if kind not in {"doublecat", "semicat"}:
        raise ValueError("kind must be doublecat or semicat")
    return 2
```

Self-condition or use DoubleCat. Discrete dLLM recycle is A2D, not this recipe.
