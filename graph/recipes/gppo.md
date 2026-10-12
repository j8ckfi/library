---
id: recipe:gppo
type: recipe
title: Generalized PPO Divergence View
method: method:gppo
task: task:math-code-rl-dense
target_hardware: PPO-family LLM RL host
framework: PyTorch RLVR host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- gppo
---

# Generalized PPO Divergence View

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def divergence_estimator_cell(divergence: str, estimator: str) -> str:
    if not divergence or not estimator:
        raise ValueError("GPPO cell is Divergence x Estimator")
    return f"{divergence}:{estimator}"
```

Fill both axes. Do not retarget CISPO.
