---
id: recipe:empo
type: recipe
title: 'Effect-level IS coupling'
method: method:empo
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: ALFWorld / WebShop / Sokoban multi-turn RL'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- empo
---

# Effect-level IS coupling

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def effect_key(tool_name: str, args) -> tuple:
    if not tool_name:
        raise ValueError('tool')
    return (tool_name, tuple(sorted(args.items())) if isinstance(args, dict) else args)
```

Do not retarget locked SOTA from this recipe.
