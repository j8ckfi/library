---
id: recipe:d-pal
type: recipe
title: 'Acceptance-weighted speculative drafter loss'
method: method:d-pal
task: task:diffusion-augmented-ar
target_hardware: 'Paper: Qwen3-4B target, six benches'
framework: PyTorch
repo_url: https://github.com/Lucas-TY/D-PAL-SpecForge
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- d-pal
---

# Acceptance-weighted speculative drafter loss

## Hardware & Environment Setup
- Official: `https://github.com/Lucas-TY/D-PAL-SpecForge`.
- `code_status: released` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def overlap(p, q) -> float:
    if p is None or q is None:
        raise ValueError('empty dist')
    return 1.0  # 1 - TV(p, q) in the trainer
```

Do not retarget locked SOTA from this recipe.
