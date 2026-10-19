---
id: recipe:discoveryrsi
type: recipe
title: 'Hypothesis-tree recursive scientific RSI'
method: method:discoveryrsi
task: task:agent-harness-runtime
target_hardware: 'Paper: DiscoveryRSI-27B; Harbor tasks'
framework: PyTorch
repo_url: https://github.com/Gen-Verse/DiscoveryRSI
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- discoveryrsi
---

# Hypothesis-tree recursive scientific RSI

## Hardware & Environment Setup
- Official: `https://github.com/Gen-Verse/DiscoveryRSI`.
- `code_status: released` as of 2026-10-19.

## Quickstart Implementation

```python
from __future__ import annotations

def hypothesis_credit(score: float, prior: float) -> float:
    if score < 0.0 or prior < 0.0:
        raise ValueError('scores must be >= 0')
    return score - prior
```

Do not retarget locked SOTA from this recipe.
