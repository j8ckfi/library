---
id: recipe:latentgrm
type: recipe
title: LatentGRM Latent Judge
method: method:latentgrm
task: task:reasoning-rl-alignment
target_hardware: 'Paper: Qwen3-4B/8B; vLLM vote@5'
framework: PyTorch / vLLM; official LatentGRM
repo_url: https://github.com/EADMO/LatentGRM
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- latentgrm
---

# LatentGRM Latent Judge

## Hardware & Environment Setup
- Official: `https://github.com/EADMO/LatentGRM`.
- `code_status: released` as of 2026-10-13.

## Quickstart Implementation

```python
from __future__ import annotations

def votes_ok(k: int) -> int:
    if k < 1:
        raise ValueError("need at least one vote")
    return k
```

Judge in latent space. Do not retarget CISPO.
