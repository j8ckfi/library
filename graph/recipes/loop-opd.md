---
id: recipe:loop-opd
type: recipe
title: 'Iterative layer prune with OPD recovery'
method: method:loop-opd
task: task:student-distillation
target_hardware: 'Paper: Qwen3-1.7B to 8B, 15-25% layer prune'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- loop-opd
---

# Iterative layer prune with OPD recovery

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def fused_importance(reason: float, recover: float) -> float:
    return reason * recover
```

Do not retarget locked SOTA from this recipe.
