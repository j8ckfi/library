---
id: recipe:kv4-rl
type: recipe
title: KV4-RL INT4 KV with INT8 sink/recent protection
method: method:kv4-rl
task: task:fp4-rl-train-rollout-alignment
target_hardware: 'Paper: Qwen3-4B/8B-Base GRPO rollouts'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- kv4-rl
---

# KV4-RL INT4 KV with INT8 sink/recent protection

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def protect_int8(sinks: int, recent: int, budget: int = 144) -> bool:
    if sinks < 0 or recent < 0 or budget < 1:
        raise ValueError("protection sizes must be non-negative")
    return sinks + recent <= budget
```

Do not retarget locked SOTA from this recipe.
