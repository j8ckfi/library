---
id: recipe:agentic-rl-data-scaling
type: recipe
title: 'Compute-optimal agentic RL data split'
method: method:agentic-rl-data-scaling
task: task:coding-agent-rl-environment-construction
target_hardware: 'Paper: Qwen3-8B GRPO isoFLOP splits'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- agentic-rl-data-scaling
---

# Compute-optimal agentic RL data split

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def axis_exponent(axis: str) -> float:
    table = {'environment': 0.34, 'task': 0.27, 'trajectory': 0.13, 'model': 0.26}
    if axis not in table:
        raise KeyError(axis)
    return table[axis]
```

Do not retarget locked SOTA from this recipe.
