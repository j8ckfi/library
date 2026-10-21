---
id: recipe:optd
type: recipe
title: 'Layer-transition OPD on student rollouts'
method: method:optd
task: task:student-distillation
target_hardware: 'Paper: three backbones, eight benches'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- optd
---

# Layer-transition OPD on student rollouts

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def transition_kl(prev_logp, next_logp) -> float:
    if prev_logp is None or next_logp is None:
        raise ValueError('missing layer logp')
    return float((next_logp - prev_logp).abs().mean())
```

Do not retarget locked SOTA from this recipe.
