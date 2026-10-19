---
id: recipe:mlexpert
type: recipe
title: 'Windowed Interaction RL for MLE agents'
method: method:mlexpert
task: task:agentic-async-rl
target_hardware: 'Paper: 35B MoE MLExpert; Kaggle-MLE Factory'
framework: PyTorch
repo_url: https://github.com/InternScience/MLExpert
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mlexpert
---

# Windowed Interaction RL for MLE agents

## Hardware & Environment Setup
- Official: `https://github.com/InternScience/MLExpert`.
- `code_status: released` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def window_reward(experiment_ok: bool) -> float:
    return 1.0 if experiment_ok else 0.0
```

Do not retarget locked SOTA from this recipe.
