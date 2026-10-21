---
id: recipe:self-credit
type: recipe
title: 'Intra-group citation credit for agentic RL'
method: method:self-credit
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: BrowseComp-Plus Qwen3-8B/32B; GAIA; xBench-DeepSearch'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- self-credit
---

# Intra-group citation credit for agentic RL

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-21.

## Quickstart Implementation

```python
from __future__ import annotations

def rescale(cite_w: float, n_ok: int, n_fail: int) -> float:
    if n_ok + n_fail <= 0:
        raise ValueError('empty group')
    return cite_w * (n_ok / (n_ok + n_fail))
```

Do not retarget locked SOTA from this recipe.
