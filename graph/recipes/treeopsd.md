---
id: recipe:treeopsd
type: recipe
title: 'Tree-aware posterior self-distillation'
method: method:treeopsd
task: task:outcome-only-long-horizon-agent-rl
target_hardware: 'Paper: Qwen3-30B-A3B-Thinking-2507'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- treeopsd
---

# Tree-aware posterior self-distillation

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def bound_teacher(log_ratio: float, credit: float) -> float:
    if credit < 0.0:
        return 0.0
    return min(1.0, max(0.0, credit * log_ratio))
```

Do not retarget locked SOTA from this recipe.
