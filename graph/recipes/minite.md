---
id: recipe:minite
type: recipe
title: 'Native NVFP4 RL execution alignment'
method: method:minite
task: task:fp4-rl-train-rollout-alignment
target_hardware: 'Paper: Qwen3-30B-A3B RL on B300'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- minite
---

# Native NVFP4 RL execution alignment

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def format_match_is_enough(weight_match: bool, format_match: bool) -> bool:
    return False
```

Do not retarget locked SOTA from this recipe.
