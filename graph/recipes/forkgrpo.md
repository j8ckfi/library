---
id: recipe:forkgrpo
type: recipe
title: Fork dLLM RL from high-entropy states
method: method:forkgrpo
task: task:diffusion-lm-ar-delta-recycle
target_hardware: 'Paper: dLLM GRPO math/code benches'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- forkgrpo
---

# Fork dLLM RL from high-entropy states

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def fork_sites(entropy: list[float], k: int) -> list[int]:
    if k < 1 or not entropy:
        raise ValueError("need entropy and k >= 1")
    ranked = sorted(range(len(entropy)), key=lambda i: entropy[i], reverse=True)
    return ranked[: min(k, len(ranked))]
```

Do not retarget locked SOTA from this recipe.
