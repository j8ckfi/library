---
id: recipe:adampm
type: recipe
title: 'Adam second-moment pooling'
method: method:adampm
task: task:full-param-memory-efficient-pretrain
target_hardware: 'Paper: LLaMA pretrain / GLUE / multimodal'
framework: PyTorch
repo_url: https://github.com/jixiaowei95/AdamPM
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- adampm
---

# Adam second-moment pooling

## Hardware & Environment Setup
- Official: `https://github.com/jixiaowei95/AdamPM`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def pooled_second_moment_numel(n: int, group: int) -> int:
    if group < 1 or n < 1:
        raise ValueError('n and group must be >= 1')
    return (n + group - 1) // group
```

Do not retarget locked SOTA from this recipe.
