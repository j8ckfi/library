---
id: recipe:vrsd
type: recipe
title: VRSD verbal regularization of privileged OPSD
method: method:vrsd
task: task:privileged-teacher-opsd
target_hardware: 'Paper: Qwen3-4B/8B and OLMo-3-7B'
framework: PyTorch
repo_url: https://github.com/lijiazheng99/VRSD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- vrsd
---

# VRSD verbal regularization of privileged OPSD

## Hardware & Environment Setup
- Official: `https://github.com/lijiazheng99/VRSD`.
- `code_status: released` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def verbal_regularize(system_prompt: str) -> str:
    if not system_prompt.strip():
        raise ValueError("system prompt must be non-empty")
    return system_prompt.strip()
```

Do not retarget locked SOTA from this recipe.
