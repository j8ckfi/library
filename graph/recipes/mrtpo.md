---
id: recipe:mrtpo
type: recipe
title: 'Reward-specific token credit'
method: method:mrtpo
task: task:multi-reward-rlvr
target_hardware: 'Paper: Qwen2.5-Coder-3B/7B SQL; Qwen3-4B IF; Qwen2.5-3B tool calling'
framework: PyTorch
repo_url: https://github.com/zhaihaotian/MRTPO
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- mrtpo
---

# Reward-specific token credit

## Hardware & Environment Setup
- Official: `https://github.com/zhaihaotian/MRTPO`.
- `code_status: released` as of 2026-10-16.

## Quickstart Implementation

```python
from __future__ import annotations

def reassign(advantage: float, relevance: list[float]) -> list[float]:
    total = sum(max(r, 0.0) for r in relevance)
    if total <= 0.0:
        raise ValueError("relevance must have a positive mass")
    return [advantage * max(r, 0.0) / total for r in relevance]
```

Do not retarget locked SOTA from this recipe.

