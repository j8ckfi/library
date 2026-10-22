---
id: recipe:bird-rl
type: recipe
title: 'Trajectory-scoped SQL replica reuse'
method: method:bird-rl
task: task:agentic-async-rl
target_hardware: 'Paper: 7B / 14B on BIRD-CRITIC-SQLite'
framework: PyTorch
repo_url: https://github.com/bird-bench/BIRD-RL
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- bird-rl
---

# Trajectory-scoped SQL replica reuse

## Hardware & Environment Setup
- Official: `https://github.com/bird-bench/BIRD-RL`.
- `code_status: released` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def replica_key(traj_id: str, turn: int) -> str:
    if not traj_id:
        raise ValueError('traj_id')
    return f'{traj_id}:{turn}'
```

Do not retarget locked SOTA from this recipe.
