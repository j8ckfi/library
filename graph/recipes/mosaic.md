---
id: recipe:mosaic
type: recipe
title: 'Session-aware agentic RL advantages'
method: method:mosaic
task: task:agentic-async-rl
target_hardware: 'Paper: Qwen3.5-4B BrowseComp ReAct'
framework: PyTorch
repo_url: https://github.com/LARK-AI-Lab/Mosaic
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mosaic
---

# Session-aware agentic RL advantages

## Hardware & Environment Setup
- Official: `https://github.com/LARK-AI-Lab/Mosaic`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def session_tax(reward: float, n_sessions: int, mean_sessions: float) -> float:
    if n_sessions <= 0 or mean_sessions <= 0:
        raise ValueError("session counts must be positive")
    sign = 1.0 if reward > 0.0 else -1.0
    return reward - sign * (n_sessions - mean_sessions) / mean_sessions
```

Do not retarget locked SOTA from this recipe.

