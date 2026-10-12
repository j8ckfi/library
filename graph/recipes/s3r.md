---
id: recipe:s3r
type: recipe
title: Self-Sparse Speculative RL Rollouts
method: method:s3r
task: task:frontier-rl-posttrain-stack
target_hardware: 'Long-context RLVR rollout workers; paper: Qwen3'
framework: PyTorch / speculative-decoding RL host
repo_url: none found
code_status: none
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- s3r
---

# Self-Sparse Speculative RL Rollouts

## Hardware & Environment Setup
- Official: `none found`.
- `code_status: none` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def keep_dense_group(draft_ok: bool, verified: bool) -> bool:
    if not verified:
        raise ValueError("S3R must full-attention verify; sparse groups are not GRPO-legal")
    return draft_ok and verified
```

Verify with the dense policy. Do not retarget Miles or CISPO.
