---
id: recipe:pr-opd
type: recipe
title: PR-OPD privileged representation OPSD
method: method:pr-opd
task: task:privileged-teacher-opsd
target_hardware: 'Paper: Qwen2.5-3B-Instruct ALFWorld/WebShop'
framework: PyTorch
repo_url: https://github.com/balibata/PR-OPD
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- pr-opd
---

# PR-OPD privileged representation OPSD

## Hardware & Environment Setup
- Official: `https://github.com/balibata/PR-OPD`.
- `code_status: released` as of 2026-10-14.


## Quickstart Implementation

```python
from __future__ import annotations

def invisible_advantage(token_frac: float, hidden_frac: float) -> bool:
    if not 0 <= token_frac <= 1 or not 0 <= hidden_frac <= 1:
        raise ValueError("fractions must be in [0, 1]")
    return token_frac < 0.25 and hidden_frac > 0.80
```

Do not retarget locked SOTA from this recipe.
