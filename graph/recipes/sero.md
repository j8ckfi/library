---
id: recipe:sero
type: recipe
title: 'Executable oracle continuations'
method: method:sero
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: Qwen2.5-1.5B/7B ALFWorld/WebShop'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- sero
---

# Executable oracle continuations

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def reachability(prefix_compat: list[float]) -> list[float]:
    if not prefix_compat:
        raise ValueError("prefix_compat must be non-empty")
    w = 1.0
    out = []
    for z in prefix_compat:
        w *= z
        out.append(w)
    return out
```

Do not retarget locked SOTA from this recipe.

