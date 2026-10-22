---
id: recipe:spare-moe
type: recipe
title: 'Routing-entropy MoE prune allocation'
method: method:spare-moe
task: task:pretrain-moe-frontier
target_hardware: 'Paper: Mixtral / Qwen3 / DeepSeek calibration prune'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- spare-moe
---

# Routing-entropy MoE prune allocation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

import math

def routing_entropy(weights):
    s = sum(weights)
    if s <= 0:
        raise ValueError('weights')
    p = [w / s for w in weights]
    return -sum(x * math.log(x) for x in p if x > 0)
```

Do not retarget locked SOTA from this recipe.
