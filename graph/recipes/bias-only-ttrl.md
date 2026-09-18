---
id: recipe:bias-only-ttrl
type: recipe
title: "Bias-Only Label-Free TTRL"
method: method:bias-only-ttrl
task: task:label-free-test-time-reasoner
target_hardware: "1x GPU for frozen-backbone TTT; optimizer state is ~100K bias params"
framework: "PyTorch TTRL host (majority-vote rewards)"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - ttrl
  - bias-only
  - label-free
---

# Bias-Only Label-Free TTRL

## Hardware & Environment Setup
- No official GitHub as of 2026-09-18 (`arXiv:2609.18587`). `repo_url: none found`. `code_status: none`.
- Label-free TTT default stays TTPO. This recipe only trains bias parameters under majority-vote rewards.

## Quickstart Implementation

```python
from __future__ import annotations

from collections import Counter

import torch


def freeze_except_bias(model: torch.nn.Module) -> list[torch.nn.Parameter]:
    trainable: list[torch.nn.Parameter] = []
    for name, param in model.named_parameters():
        is_bias = name.endswith("bias") or ".bias" in name
        param.requires_grad = is_bias
        if is_bias:
            trainable.append(param)
    if not trainable:
        raise RuntimeError("no bias parameters marked trainable")
    return trainable


def majority_vote_reward(completions: list[str]) -> list[float]:
    if not completions:
        return []
    winner, _ = Counter(completions).most_common(1)[0]
    return [1.0 if c == winner else 0.0 for c in completions]
```

## Critical Hyperparameters & Tuning Advice
- Do not unfreeze the backbone. The paper's compression claim is the bias-only constraint.
- Majority-vote group size is the reliability knob; tiny groups make the reward noise TTPO was designed to split.
- Host TTT algorithm stays TTPO when you want agreeing-rollout OPSD plus disagreeing-rollout Grouped RL.
