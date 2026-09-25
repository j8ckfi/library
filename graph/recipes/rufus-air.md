---
id: recipe:rufus-air
type: recipe
title: "Rufus-Air Open Post-Training Recipe"
method: method:rufus-air
task: task:frontier-rl-posttrain-stack
target_hardware: "SFT: 64x 8xH200 (paper); RL stages 8–32 nodes on GLM-4.5-Air-Base 106B-A12B"
framework: "PyTorch / Slime / SGLang / Megatron"
repo_url: "https://github.com/THUDM/slime"
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
  - "sglang"
tags:
  - recipe
  - rufus-air
  - systems
  - post-training
---

# Rufus-Air Open Post-Training Recipe

## Hardware & Environment Setup
- No dedicated Rufus-Air GitHub as of 2026-09-25 (`arXiv:2609.29421`). `repo_url` is the open host `https://github.com/THUDM/slime`. Pair with SGLang. `code_status: none`.
- Engine default stays Miles. Pass@1 stays CISPO. Async stays SAO.

## Quickstart Implementation

```python
from __future__ import annotations


STAGES = (
    "sft",
    "reasoning_rl",
    "coding_rl",
    "if_rl",
    "general_agent",
    "coding_agent",
    "search_agent",
    "rlhf",
)


def next_stage(done: str | None) -> str | None:
    if done is None:
        return STAGES[0]
    if done not in STAGES:
        raise ValueError(f"unknown stage {done!r}")
    idx = STAGES.index(done)
    if idx + 1 >= len(STAGES):
        return None
    return STAGES[idx + 1]


def keep_prompt(n_correct: int, group_size: int) -> bool:
    if group_size <= 0:
        return False
    if n_correct >= group_size:
        return False
    if n_correct <= 0:
        return False
    return True
```

Train each stage on the previous checkpoint. Drop prompts the policy always solves; in most RL stages also drop prompts it never solves. Keep token-in/token-out multi-turn and Rollout Routing Replay on the slime/SGLang host.

## Critical Hyperparameters & Tuning Advice
- SFT (paper): 3 epochs over 9.01M examples, batch 4096, AdamW peak \(5\times 10^{-5}\) cosine to \(5\times 10^{-6}\), context 128K after packing; carry an early-plateau checkpoint (3799), not the final loss step.
- Order stages by reward reliability, not by reward format. IF RL can sit before agent stages even with a rubric judge.
- Do not retarget Miles from Table 1. This is a recipe on slime, not a new engine.
