---
id: recipe:bridged-self-distill
type: recipe
title: 'Trace-bridged self-distillation'
method: method:bridged-self-distill
task: task:student-distillation
target_hardware: 'Paper: shared-tokenizer, cross-tokenizer, and API teachers'
framework: PyTorch
repo_url: https://github.com/TUMLegalTech/Bridged-Self-Distillation
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- bridged-self-distill
---

# Trace-bridged self-distillation

## Hardware & Environment Setup
- Official: `https://github.com/TUMLegalTech/Bridged-Self-Distillation`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def needs_teacher_logp() -> bool:
    return False
```

Do not retarget locked SOTA from this recipe.
