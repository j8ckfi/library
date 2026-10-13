---
id: recipe:branchopd
type: recipe
title: BranchOPD Branch-and-Resample Distill
method: method:branchopd
task: task:student-distillation
target_hardware: Teacher OPD host; paper math + ALFWorld/WebShop
framework: PyTorch OPD; official BranchOPD
repo_url: https://github.com/chendy25/BranchOPD
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- branchopd
---

# BranchOPD Branch-and-Resample Distill

## Hardware & Environment Setup
- Official: `https://github.com/chendy25/BranchOPD`.
- `code_status: announced` as of 2026-10-13. Paper lists chendy25/BranchOPD; the GitHub is an empty stub.

## Quickstart Implementation

```python
from __future__ import annotations

def should_branch(student_logp: float, teacher_logp: float, thresh: float) -> bool:
    if thresh <= 0:
        raise ValueError("disagreement threshold must be positive")
    return abs(student_logp - teacher_logp) >= thresh
```

KL on trunk and branches. Do not retarget OPD.
