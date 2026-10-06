---
id: recipe:thundersyncrl
type: recipe
title: "ThunderSyncRL Gradient Streaming"
method: method:thundersyncrl
task: task:agentic-async-rl
target_hardware: "multi-GPU agentic GRPO/OPD; paper: SWE-bench Verified / Terminal Bench 4.0"
framework: "GRPO/OPD host with per-trajectory streaming"
repo_url: none found
code_status: none
pip_dependencies:
  - torch>=2.5.0
tags:
  - recipe
  - thundersyncrl
  - training-systems
---

# ThunderSyncRL Gradient Streaming

## Hardware & Environment Setup
- No official GitHub URL as of 2026-10-06 (`arXiv:2610.05935`). `repo_url: none found`. `code_status: none`.
- Async algorithm stays SAO. Engine stays Miles.

## Quickstart Implementation

```python
from __future__ import annotations

def can_stream_grpo(reward_ready: bool, group_ready: bool) -> bool:
    del group_ready
    return reward_ready
```

When a trajectory reward arrives, compute that trajectory's GRPO score gradient immediately. Do not wait for the rest of the group. For OPD, score completed turns while tools run.

## Critical Hyperparameters & Tuning Advice
- Up to 1.9× vs sync; +2.47pp vs async at fixed budget. Do not retarget SAO or Miles.
