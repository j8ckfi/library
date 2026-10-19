---
id: recipe:market-posttrain
type: recipe
title: 'Market-based post-training of agent swarms'
method: method:market-posttrain
task: task:multi-agent-orchestration
target_hardware: 'Paper: decentralized agent swarms'
framework: PyTorch
repo_url: https://github.com/Embodied-Minds-Lab/MPT
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- market-posttrain
---

# Market-based post-training of agent swarms

## Hardware & Environment Setup
- Official: `https://github.com/Embodied-Minds-Lab/MPT`.
- `code_status: released` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def bid_select(bids: list[float], k: int) -> list[int]:
    if k < 1 or k > len(bids):
        raise ValueError('k out of range')
    ranked = sorted(range(len(bids)), key=lambda i: bids[i], reverse=True)
    return ranked[:k]
```

Do not retarget locked SOTA from this recipe.
