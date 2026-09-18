---
id: recipe:actobs
type: recipe
title: "ActObs Observation-Token SFT"
method: method:actobs
task: task:agentic-async-rl
target_hardware: "SFT then GRPO box for Qwen3-4B/8B agent traces"
framework: "PyTorch SFT + GRPO-family host"
repo_url: none found
code_status: none
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - actobs
  - sft
  - agentic
---

# ActObs Observation-Token SFT

## Hardware & Environment Setup
- No official GitHub as of 2026-09-18 (`arXiv:2609.20715`). `repo_url: none found`. `code_status: none`.
- Async default stays SAO. SWE loop stays mini-SWE-agent. This recipe only changes which tokens in a trace get SFT loss.

## Quickstart Implementation

```python
from __future__ import annotations

import torch
import torch.nn.functional as F


def actobs_sft_loss(
    logits: torch.Tensor,
    labels: torch.Tensor,
    is_action: torch.Tensor,
    is_observation: torch.Tensor,
) -> torch.Tensor:
    """Loss on action and observation tokens; ignore prompt/padding."""
    n, t, v = logits.shape
    logp = F.log_softmax(logits, dim=-1)
    token_nll = F.nll_loss(logp.reshape(n * t, v), labels.reshape(n * t), reduction="none").view(n, t)
    mask = (is_action | is_observation).to(token_nll.dtype)
    denom = mask.sum().clamp_min(1.0)
    return (token_nll * mask).sum() / denom
```

## Critical Hyperparameters & Tuning Advice
- Observations are already in the sequence. Do not add a second forward pass or extra parameters.
- Keep the GRPO stage. Comparing SFT-only checkpoints hides the paper's result.
- Action-only masking is the ablation, not a recommended default once RL starts.
