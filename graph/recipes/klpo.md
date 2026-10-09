---
id: recipe:klpo
type: recipe
title: "KLPO Sampler-Anchored Least-Squares Update"
method: method:klpo
task: task:agentic-async-rl
target_hardware: "Async RL host with a known sampler logp"
framework: "PyTorch RL host; official KLPO"
repo_url: "https://github.com/yifanzhang-pro/KLPO"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - klpo
---

# KLPO Sampler-Anchored Least-Squares Update

## Hardware & Environment Setup
- Official: `https://github.com/yifanzhang-pro/KLPO`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

def log_ratio(logp_pi: float, logp_sampler: float) -> float:
    return logp_pi - logp_sampler
```

Fit on sampler trajectories. No IS clip. Do not retarget SAO.
