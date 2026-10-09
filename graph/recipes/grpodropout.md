---
id: recipe:grpodropout
type: recipe
title: "GRPODropout Positive-Advantage Rollout Drop"
method: method:grpodropout
task: task:math-code-rl-dense
target_hardware: "GRPO-family host"
framework: "PyTorch GRPO host; official GRPODropout"
repo_url: "https://github.com/hexuandeng/GRPODropout"
code_status: released
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - grpodropout
---

# GRPODropout Positive-Advantage Rollout Drop

## Hardware & Environment Setup
- Official: `https://github.com/hexuandeng/GRPODropout`.
- `code_status: released` as of 2026-10-09.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_after_positive_drop(logp, adv, k: int):
    if k < 0:
        raise ValueError("k must be non-negative")
    pos = [i for i, a in enumerate(adv) if a > 0]
    drop = set(sorted(pos, key=lambda i: logp[i], reverse=True)[: min(k, len(pos))])
    keep = [i for i in range(len(adv)) if i not in drop]
    if not keep:
        raise ValueError("dropped the whole group")
    return keep
```

Drop high-logp positive rollouts, then recenter. Do not retarget CISPO.
