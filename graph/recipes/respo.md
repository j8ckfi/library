---
id: recipe:respo
type: recipe
title: "ReSPO Two-Branch Sequence Kernel"
method: method:respo
task: task:math-code-rl-dense
target_hardware: "Off-policy RLVR host that reuses rollouts"
framework: "PyTorch RLVR host; official ReSPO"
repo_url: "https://github.com/yhangchen/ReSPO-code"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - respo
---

# ReSPO Two-Branch Sequence Kernel

## Hardware & Environment Setup
- Official: `https://github.com/yhangchen/ReSPO-code`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

from math import exp

def respo_weight(ratio: float, positive: bool, alpha: float, tilt: float) -> float:
    if ratio <= 0:
        raise ValueError("importance ratio must be positive")
    if not 0.0 < alpha < 1.0:
        raise ValueError("alpha must be in (0, 1)")
    if positive:
        return (ratio ** (1.0 - alpha)) * exp(-tilt)
    return ratio / (1.0 + ratio ** alpha)
```

Keep rare positives; damp over-generated negatives. Do not retarget CISPO.
