---
id: recipe:tetpo
type: recipe
title: TETPO target-ESS tempering
method: method:tetpo
task: task:agentic-async-rl
target_hardware: 'Paper: Qwen3-Base-1.7B and Llama-3.2-3B-Instruct k=32'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- tetpo
---

# TETPO target-ESS tempering

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def temper_is(rho: float, alpha: float) -> float:
    if rho < 0:
        raise ValueError("IS ratio must be non-negative")
    return rho ** alpha
```

Do not retarget locked SOTA from this recipe.
