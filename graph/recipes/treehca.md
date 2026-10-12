---
id: recipe:treehca
type: recipe
title: TreeHCA Hindsight Tree Credit
method: method:treehca
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Multi-turn agent RL host; paper: three Qwen backbones'
framework: PyTorch agent RL host
repo_url: https://github.com/TheBlackCat22/TreeHCA
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- treehca
---

# TreeHCA Hindsight Tree Credit

## Hardware & Environment Setup
- Official: `https://github.com/TheBlackCat22/TreeHCA`.
- `code_status: announced` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def should_branch(prev_ref_logp: float, cur_ref_logp: float, min_delta: float) -> bool:
    if min_delta < 0:
        raise ValueError("min_delta must be non-negative")
    return abs(cur_ref_logp - prev_ref_logp) >= min_delta
```

Branch on hindsight likelihood jumps. Do not retarget CANOPY.
