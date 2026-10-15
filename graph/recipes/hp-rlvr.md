---
id: recipe:hp-rlvr
type: recipe
title: Single-rollout hindsight JSD token credit
method: method:hp-rlvr
task: task:math-code-rl-dense
target_hardware: 'Paper: Qwen3-1.7B/4B/8B 100-step GRPO pairs'
framework: PyTorch
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- hp-rlvr
---

# Single-rollout hindsight JSD token credit

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-15.

## Quickstart Implementation

```python
from __future__ import annotations

def bounded_jsd_weight(jsd: float, max_jsd: float = 1.0) -> float:
    if jsd < 0.0 or max_jsd <= 0.0:
        raise ValueError("jsd must be >= 0 and max_jsd > 0")
    return min(jsd / max_jsd, 1.0)
```

Do not retarget locked SOTA from this recipe.
