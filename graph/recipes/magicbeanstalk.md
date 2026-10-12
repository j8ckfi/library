---
id: recipe:magicbeanstalk
type: recipe
title: MagicBeanStalk Recursive RLVR Data Synthesis
method: method:magicbeanstalk
task: task:math-code-rl-dense
target_hardware: 'RLVR host plus a teacher for recursive synthesis; paper: 16K-token budget'
framework: PyTorch RLVR host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- magicbeanstalk
---

# MagicBeanStalk Recursive RLVR Data Synthesis

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def zero_advantage_trap(pass_rate: float) -> bool:
    if not 0.0 <= pass_rate <= 1.0:
        raise ValueError("pass rate must be in [0, 1]")
    return pass_rate == 0.0 or pass_rate == 1.0
```

Grow mixed-success children of hard seeds. Do not retarget CISPO.
