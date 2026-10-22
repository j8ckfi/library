---
id: recipe:uni-mem
type: recipe
title: 'Stage-decoupled memory GRPO'
method: method:uni-mem
task: task:agent-memory
target_hardware: 'Paper: long-horizon agent memory manager RL'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- uni-mem
---

# Stage-decoupled memory GRPO

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def stage_group(stage: str, allowed=('construct', 'retrieve')) -> str:
    if stage not in allowed:
        raise ValueError('stage')
    return stage
```

Do not retarget locked SOTA from this recipe.
