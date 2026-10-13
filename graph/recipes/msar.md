---
id: recipe:msar
type: recipe
title: MSAR Multi-Stream Attention Residuals
method: method:msar
task: task:llm-pretraining-optimization
target_hardware: 'Paper: 18B and 28B MoE pretrain'
framework: PyTorch; official MSAR
repo_url: https://github.com/jianke0604/MSAR
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- msar
---

# MSAR Multi-Stream Attention Residuals

## Hardware & Environment Setup
- Official: `https://github.com/jianke0604/MSAR`.
- `code_status: released` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def n_streams_ok(n: int) -> bool:
    if n < 2:
        raise ValueError("MSAR needs at least two residual streams")
    return True
```

Compose with Muon2. Do not retarget mHC or AttnRes.
