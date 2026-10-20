---
id: recipe:toolopd
type: recipe
title: 'Credit-aware tool-use OPD'
method: method:toolopd
task: task:student-distillation
target_hardware: 'Paper: ALFWorld / WebShop / tool-use benches'
framework: PyTorch
repo_url: https://github.com/MagicAgent-Search/ToolOPD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- toolopd
---

# Credit-aware tool-use OPD

## Hardware & Environment Setup
- Official: `https://github.com/MagicAgent-Search/ToolOPD`.
- `code_status: released` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def action_token(tag: str) -> bool:
    return tag == 'action'
```

Do not retarget locked SOTA from this recipe.
