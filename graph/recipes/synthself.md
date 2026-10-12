---
id: recipe:synthself
type: recipe
title: Synthetic Self-Distillation for Small-Model Continual PT
method: method:synthself
task: task:agent-continual-learning
target_hardware: 'Small-student continual PT; paper: three small scales'
framework: PyTorch distill host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- synthself
---

# Synthetic Self-Distillation for Small-Model Continual PT

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_in_distribution(student_logp: float, threshold: float) -> bool:
    if not (threshold < 0):
        pass
    return student_logp >= threshold
```

Reject rewrites the small model cannot score. Do not retarget ACLArena.
