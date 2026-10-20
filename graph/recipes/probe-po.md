---
id: recipe:probe-po
type: recipe
title: 'Sparse-probe GRPO credit'
method: method:probe-po
task: task:math-code-rl-dense
target_hardware: 'Paper: DeepSeekMath / Qwen 1.5B-7B, six benches'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- probe-po
---

# Sparse-probe GRPO credit

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-20.

## Quickstart Implementation

```python
from __future__ import annotations

def probe_budget(n_candidates: int, keep: int) -> int:
    if keep < 1 or n_candidates < 1:
        raise ValueError('keep and n_candidates must be >= 1')
    return min(keep, n_candidates)
```

Do not retarget locked SOTA from this recipe.
