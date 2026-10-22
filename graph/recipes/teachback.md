---
id: recipe:teachback
type: recipe
title: 'Bidirectional privileged OPSD preference'
method: method:teachback
task: task:privileged-teacher-opsd
target_hardware: 'Paper: math and logical reasoning OPSD'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- teachback
---

# Bidirectional privileged OPSD preference

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def suffix_keep(ref_len: int, max_keep: int) -> int:
    if max_keep <= 0:
        raise ValueError('max_keep')
    return min(ref_len, max_keep)
```

Do not retarget locked SOTA from this recipe.
