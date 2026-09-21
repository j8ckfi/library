---
id: recipe:codemidas
type: recipe
title: "CodeMidas Coding RL Environments"
method: method:codemidas
task: task:coding-agent-rl-environment-construction
target_hardware: "multi-GPU GRPO box for MiMo-V2.5-class coding-agent rollouts"
framework: "GRPO host with binary execution rewards and containerized verifiers"
repo_url: "https://mimo.xiaomi.com/rl/"
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - codemidas
  - coding-rl
  - environments
---

# CodeMidas Coding RL Environments

## Hardware & Environment Setup
- Project page `https://mimo.xiaomi.com/rl/` is a live MiMo RL dashboard as of 2026-09-21. It is not a public trainer, dataset, or GitHub release. `code_status: none`. Do not invent a GitHub URL.
- Paper: 5,545 tasks from 3,185 repos, GRPO, binary execution rewards, batch 32, 32 rollouts per task, MiMo-V2.5.
- Outcome-only first hop stays CANOPY. Async stays SAO. SWE loop stays mini-SWE-agent. Production engine stays Miles.

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ConsistencyResult:
    start_fails: int
    reference_passes: int


def keep_after_consistency(result: ConsistencyResult) -> bool:
    return result.start_fails >= 2 and result.reference_passes >= 4


def keep_after_rollout_screen(n_pass: int, n_fail: int) -> bool:
    return n_pass > 0 and n_fail > 0
```

## Critical Hyperparameters & Tuning Advice
- Verifier stays outside the solver environment until grading. Residual compiled artifacts and caches are leakage; reject the task.
- Scale the *cleaned* pool. A vanilla 8k unfiltered set lost to high-quality 3k in the paper.
- GRPO here is the inner optimizer, not the library's math/code RLVR default.
