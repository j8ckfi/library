---
id: recipe:brace
type: recipe
title: 'Bank-calibrated MCP rollout allocation'
method: method:brace
task: task:agentic-async-rl
target_hardware: 'Paper: Qwen3-VL MCP agents; BFCL / NESTFUL'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- brace
---

# Bank-calibrated MCP rollout allocation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def mixed_group_value(p_success: float) -> float:
    if not 0 <= p_success <= 1:
        raise ValueError('p')
    return p_success * (1.0 - p_success)
```

Do not retarget locked SOTA from this recipe.
