---
id: recipe:csd
type: recipe
title: 'Common-support cross-tokenizer distill'
method: method:csd
task: task:cross-tokenizer-opd
target_hardware: 'Paper: Llama / Gemma 1B-8B cross-tokenizer students'
framework: PyTorch
repo_url: https://github.com/NVIDIA-NeMo/RL
code_status: announced
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- csd
---

# Common-support cross-tokenizer distill

## Hardware & Environment Setup
- Official: `https://github.com/NVIDIA-NeMo/RL`.
- `code_status: announced` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def common_support(teacher_ids, student_ids):
    shared = set(teacher_ids) & set(student_ids)
    if not shared:
        raise ValueError('empty support')
    return shared
```

Do not retarget locked SOTA from this recipe.
