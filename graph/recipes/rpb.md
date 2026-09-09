---
id: recipe:rpb
type: recipe
title: "RPB Soft Router Anchoring"
method: method:rpb
task: task:math-code-rl-moe
target_hardware: "MoE post-train box (paper: Moonlight-16B-A3B, Qwen3-30B-A3B-Base)"
framework: "PyTorch"
repo_url: "https://github.com/naver-ai/rpb"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - rpb
  - moe
  - routing
---

# RPB Soft Router Anchoring

## Hardware & Environment Setup
- Claimed code: `https://github.com/naver-ai/rpb` (404 at 2026-09-09 ingest). Host MoE/VL algorithm stays SAPO; RPB only biases the router.
- Snapshot the base router once. Do not re-enable a uniformity load-balancing loss.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def rpb_logit_bias(
    live_logits: torch.Tensor,
    prior_logits: torch.Tensor,
    strength: float,
) -> torch.Tensor:
    """Pull live router logits toward a detached base-router prior."""
    return live_logits + float(strength) * (prior_logits.detach() - live_logits.detach())


def rpb_kl_anchor(
    live_logits: torch.Tensor,
    prior_logits: torch.Tensor,
) -> torch.Tensor:
    """Soft distributional anchor. Weight, logit, and output priors are interchangeable in the paper."""
    live = F.log_softmax(live_logits, dim=-1)
    prior = F.softmax(prior_logits.detach(), dim=-1)
    return F.kl_div(live, prior, reduction="batchmean")
```

## Critical Hyperparameters & Tuning Advice
- Keep the constraint soft. Hard assignment of the same prior preserves communities and loses accuracy.
- Logit, weight, and output-distribution priors are comparable; pick the one that is cheapest to store.
- MoE/VL Pass@1 algorithm stays `method:sapo`.
