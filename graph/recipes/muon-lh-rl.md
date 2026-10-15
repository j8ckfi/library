---
id: recipe:muon-lh-rl
type: recipe
title: Muon + token-avg + truncated IS for long-horizon SWE RL
method: method:muon-lh-rl
task: task:agentic-async-rl
target_hardware: 'Paper: MiniCPM5-2B / Qwen3.5-4B R2E-Gym'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- muon-lh-rl
---

# Muon + token-avg + truncated IS for long-horizon SWE RL

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def truncated_is(ratio: float, cap: float = 2.0) -> float:
    if cap <= 0.0:
        raise ValueError("cap must be positive")
    return min(max(ratio, 0.0), cap)
```

Do not retarget locked SOTA from this recipe.
