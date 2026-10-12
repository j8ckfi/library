---
id: recipe:cbpo
type: recipe
title: Cross-Behavior Policy Optimization
method: method:cbpo
task: task:math-code-rl-dense
target_hardware: 'Math post-train host with a replay buffer; paper: Qwen3-1.7B'
framework: PyTorch unified regression host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- cbpo
---

# Cross-Behavior Policy Optimization

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def shared_record(source: str, reward: float) -> dict:
    if source not in {"offline", "on_policy", "off_policy", "replay"}:
        raise ValueError("unknown CBPO source")
    return {"source": source, "reward": reward}
```

One target, many sources. Do not retarget CISPO.
