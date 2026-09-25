---
id: recipe:slca-grpo
type: recipe
title: "SLCA-GRPO Segment-Locked Credit"
method: method:slca-grpo
task: task:tool-agent-segment-credit
target_hardware: "GRPO tool-agent box; paper: Qwen2.5-3B/7B-Instruct and Qwen3-8B-Base, G=16, one RL epoch"
framework: "PyTorch GRPO host plus schema-guided tool simulator"
repo_url: "https://github.com/SLCA-GRPO/SLCA-GRPO"
code_status: announced
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - slca-grpo
  - credit-assignment
  - tool-use
---

# SLCA-GRPO Segment-Locked Credit

## Hardware & Environment Setup
- Claimed repo: `https://github.com/SLCA-GRPO/SLCA-GRPO`. 404 as of 2026-09-25. `code_status: announced`.
- Dataset: `https://huggingface.co/datasets/YanZhanPKU/SLCA-GRPO-Datasets`.
- Folding stays FoldGRPO. Async stays SAO. Pass@1 stays CISPO. Actor-then-Critic stays PACT.

## Quickstart Implementation

```python
from __future__ import annotations

from statistics import mean, pstdev


def group_zscore(rewards: list[float], eps: float = 1e-8) -> list[float]:
    if not rewards:
        return []
    mu = mean(rewards)
    sigma = pstdev(rewards) if len(rewards) > 1 else 0.0
    denom = sigma + eps
    return [(r - mu) / denom for r in rewards]


def slca_token_advantage(
    is_tool: bool,
    is_summary: bool,
    a_tool: float,
    a_sum: float,
    lam_tool: float = 1.0,
    lam_sum: float = 1.0,
) -> float:
    if is_tool and is_summary:
        raise ValueError("a token cannot be both tool and summary")
    if is_tool:
        return lam_tool * a_tool
    if is_summary:
        return lam_sum * a_sum
    return 0.0
```

Normalize tool returns and summary returns in separate `group_zscore` calls on the same GRPO group. Attach `slca_token_advantage` per token from the segment mask. Do not broadcast \(R_{\mathrm{tool}}+R_{\mathrm{sum}}\).

## Critical Hyperparameters & Tuning Advice
- Matched GRPO comparison in the paper shares SFT, SGLS, HierR, \(G=16\), one epoch. Change only the advantage routing.
- Presence-filter and omission-penalty routing are in the paper appendix; skip them only if every rollout has both segments.
- Do not retarget SAO, FoldGRPO, PACT, or CISPO from the +2.53 / +1.36 / +9.15 numbers.
