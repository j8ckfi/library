---
id: recipe:monitorability-trainable
type: recipe
title: 'CoT-output mutual information stage'
method: method:monitorability-trainable
task: task:math-code-rl-dense
target_hardware: 'Paper: three CoT-degraded model organisms plus undegraded policies'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- monitorability-trainable
---

# CoT-output mutual information stage

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-22.

## Quickstart Implementation

```python
from __future__ import annotations

def mi_keep(cot_logp: float, out_logp: float) -> float:
    return cot_logp + out_logp
```

Do not retarget locked SOTA from this recipe.
