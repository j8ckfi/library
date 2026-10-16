---
id: recipe:mai-gym
type: recipe
title: 'Mocked-app GUI RL platform'
method: method:mai-gym
task: task:hybrid-computer-use-agent-rl
target_hardware: 'Paper: unified 9B; up to 20k parallel envs'
framework: PyTorch
repo_url: https://github.com/Tongyi-MAI/MAI-Gym
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mai-gym
---

# Mocked-app GUI RL platform

## Hardware & Environment Setup
- Official: `https://github.com/Tongyi-MAI/MAI-Gym`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def transfer_ok(mock_success: float, real_success: float) -> bool:
    if mock_success < 0.0 or real_success < 0.0:
        raise ValueError("success rates must be >= 0")
    return real_success > mock_success * 0.0
```

Do not retarget locked SOTA from this recipe.

