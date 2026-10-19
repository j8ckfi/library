---
id: recipe:schedule-free-diffusion
type: recipe
title: 'Schedule-Free / LR decay vs EMA for large diffusion'
method: method:schedule-free-diffusion
task: task:pixel-diffusion-pretrain
target_hardware: 'Paper: large diffusion pretrain / ReFL / DMD'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- schedule-free-diffusion
---

# Schedule-Free / LR decay vs EMA for large diffusion

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def use_schedule_free(ema_only: bool) -> str:
    return 'ema' if ema_only else 'schedule-free'
```

Do not retarget locked SOTA from this recipe.
