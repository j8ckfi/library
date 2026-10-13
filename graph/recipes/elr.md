---
id: recipe:elr
type: recipe
title: ELR Mixed-Depth Looped LM
method: method:elr
task: task:elastic-depth-looped-lm
target_hardware: 'Paper: 4B dense and 30B-A3B MoE pretrain'
framework: PyTorch looped LM; no public trainer
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- elr
---

# ELR Mixed-Depth Looped LM

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def mix_loop_counts(max_loops: int) -> list[int]:
    if max_loops < 1:
        raise ValueError("need at least one loop")
    return list(range(1, max_loops + 1))
```

Gate the state update and condition on loop index plus remaining budget. Do not retarget SMELT.
