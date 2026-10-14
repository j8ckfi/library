---
id: recipe:tppo
type: recipe
title: TPPO Tracking-Value PPO
method: method:tppo
task: task:token-level-critic-rl
target_hardware: 'Paper: Qwen3-4B/8B-Base math'
framework: PyTorch
repo_url: https://github.com/LINs-lab/TPPO
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- tppo
---

# TPPO Tracking-Value PPO

## Hardware & Environment Setup
- Official: `https://github.com/LINs-lab/TPPO`.
- `code_status: released` as of 2026-10-14.

- HF Daily 2026-10-14.

## Quickstart Implementation

```python
from __future__ import annotations

def tracking_value(log_odds: list[float]) -> float:
    if not log_odds:
        raise ValueError("empty log-odds")
    return sum(log_odds)
```

Do not retarget locked SOTA from this recipe.
