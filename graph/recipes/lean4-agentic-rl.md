---
id: recipe:lean4-agentic-rl
type: recipe
title: 'Lean4 multi-level process rewards for agentic RL'
method: method:lean4-agentic-rl
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: LAR-9B/27B terminal/SWE RL'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- lean4-agentic-rl
---

# Lean4 multi-level process rewards for agentic RL

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def stage_norm(reward: float, stage_mean: float) -> float:
    return reward - stage_mean
```

Do not retarget locked SOTA from this recipe.
