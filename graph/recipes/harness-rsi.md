---
id: recipe:harness-rsi
type: recipe
title: 'Formal harness RSI admission'
method: method:harness-rsi
task: task:agent-harness-runtime
target_hardware: 'Paper: framework plus accompanying repo'
framework: PyTorch
repo_url: https://github.com/zgcagi/Harness-RSI
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- harness-rsi
---

# Formal harness RSI admission

## Hardware & Environment Setup
- Official: `https://github.com/zgcagi/Harness-RSI`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def admit(fresh_pass: bool, regression_ok: bool) -> bool:
    return bool(fresh_pass) and bool(regression_ok)
```

Do not retarget locked SOTA from this recipe.

