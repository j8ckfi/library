---
id: recipe:scope-t2i
type: recipe
title: 'Span-pooled GRPO for T2I prompt rewriting'
method: method:scope-t2i
task: task:posttrain-diffusion
target_hardware: 'Paper: Qwen-Image / SD3 / FLUX.1-dev rewriter'
framework: PyTorch
repo_url: https://github.com/MAC-AutoML/SCOPE
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- scope-t2i
---

# Span-pooled GRPO for T2I prompt rewriting

## Hardware & Environment Setup
- Official: `https://github.com/MAC-AutoML/SCOPE`.
- `code_status: released` as of 2026-10-16. Distinct from `method:scope-opsd`.

## Quickstart Implementation

```python
from __future__ import annotations

def span_coeff(logp_shifts: list[float]) -> float:
    if not logp_shifts:
        raise ValueError("span must be non-empty")
    return sum(logp_shifts) / float(len(logp_shifts))
```

Do not retarget locked SOTA from this recipe.

