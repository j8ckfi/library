---
id: recipe:ssr
type: recipe
title: 'Successive-scale harness evidence race'
method: method:ssr
task: task:agent-harness-runtime
target_hardware: 'Paper: agentic harness evolution over expanding task pools'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- ssr
---

# Successive-scale harness evidence race

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def evidence_budget(n_tasks: int, cap: int) -> int:
    if cap <= 0:
        raise ValueError('cap')
    return min(n_tasks, cap)
```

Do not retarget locked SOTA from this recipe.
