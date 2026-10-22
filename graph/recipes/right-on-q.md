---
id: recipe:right-on-q
type: recipe
title: 'On-policy QAT trajectory recovery'
method: method:right-on-q
task: task:full-lowbit-finetune
target_hardware: 'Paper: Qwen3 2-bit QAT on reasoning benches'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- right-on-q
---

# On-policy QAT trajectory recovery

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def kl_gate(student_logp: float, teacher_logp: float) -> float:
    return max(0.0, teacher_logp - student_logp)
```

Do not retarget locked SOTA from this recipe.
