---
id: recipe:reapo
type: recipe
title: 'Retry-aware GRPO credit'
method: method:reapo
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen3 / OLMo-2 0.6B-4B, eight math/science benches'
framework: PyTorch
repo_url: https://github.com/Nghi-Dao/ReAPO
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- reapo
---

# Retry-aware GRPO credit

## Hardware & Environment Setup
- Official: `https://github.com/Nghi-Dao/ReAPO`.
- `code_status: released` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def retry_mask(successes):
    if not successes:
        raise ValueError('empty')
    return [i for i, ok in enumerate(successes) if ok]
```

Do not retarget locked SOTA from this recipe.
