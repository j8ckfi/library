---
id: recipe:multiagent-opd
type: recipe
title: 'Leader-Searcher-Answerer OPD'
method: method:multiagent-opd
task: task:student-distillation
target_hardware: 'Paper: hierarchical search team, seven datasets'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- multiagent-opd
---

# Leader-Searcher-Answerer OPD

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def team_roles(n_searchers: int) -> list[str]:
    if n_searchers < 1:
        raise ValueError('need at least one searcher')
    return ['leader'] + ['searcher'] * n_searchers + ['answerer']
```

Do not retarget locked SOTA from this recipe.
