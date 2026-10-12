---
id: recipe:tapo
type: recipe
title: Trajectory-Aware Policy Optimization
method: method:tapo
task: task:math-code-rl-dense
target_hardware: GRPO/GSPO-family LLM RL host
framework: PyTorch RLVR host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- tapo
---

# Trajectory-Aware Policy Optimization

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

from math import exp, log

def geometric_mean(xs: list[float]) -> float:
    if not xs:
        raise ValueError("empty trajectory")
    if any(x <= 0 for x in xs):
        raise ValueError("geometric mean needs positive weights")
    return exp(sum(log(x) for x in xs) / len(xs))
```

Correct state shift along the trajectory. Do not retarget CISPO.
