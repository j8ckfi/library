---
id: recipe:criticopd
type: recipe
title: Critique-guided OPD rewrite then score
method: method:criticopd
task: task:student-distillation
target_hardware: 'Paper: Qwen3-0.6B/1.7B math OPD'
framework: PyTorch
repo_url: https://github.com/kzhao5/CriticOPD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- criticopd
---

# Critique-guided OPD rewrite then score

## Hardware & Environment Setup
- Official: `https://github.com/kzhao5/CriticOPD`.
- `code_status: released` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def student_train_trace(rewrite: str, critique: str) -> str:
    if not rewrite:
        raise ValueError("empty rewrite")
    _ = critique
    return rewrite
```

Do not retarget locked SOTA from this recipe.
