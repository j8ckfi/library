---
id: recipe:arctic-swe
type: recipe
title: 'Async SWE RL co-design baseline'
method: method:arctic-swe
task: task:agentic-async-rl
target_hardware: 'Paper: Qwen3.5-4B/9B on Prime-RL, R2E-Gym / SWE-rebench / Scale-SWE'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- arctic-swe
---

# Async SWE RL co-design baseline

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def sealed_eval(network_open: bool, history_leaked: bool) -> bool:
    return not network_open and not history_leaked
```

Do not retarget locked SOTA from this recipe.
