---
id: recipe:mmsearch-opd
type: recipe
title: 'Multimodal search Refine plus decaying OPD'
method: method:mmsearch-opd
task: task:web-search-agent-rl
target_hardware: 'Paper: Qwen3.5-9B student; 27B SFT teacher'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mmsearch-opd
---

# Multimodal search Refine plus decaying OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations
import math

def opd_coeff(step: int, half_life: int) -> float:
    if step < 0 or half_life <= 0:
        raise ValueError("step must be >= 0 and half_life > 0")
    return math.exp(-step / float(half_life))
```

Do not retarget locked SOTA from this recipe.

