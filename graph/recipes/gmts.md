---
id: recipe:gmts
type: recipe
title: "GMTS Token-Selection Plug-in"
method: method:gmts
task: task:math-code-rl-dense
target_hardware: "8x NVIDIA H100 80GB (host RLVR run)"
framework: "PyTorch / verl"
repo_url: "https://github.com/outongyiLv/GMTS"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
tags:
  - recipe
  - gmts
  - rlvr
  - token-selection
---

# GMTS Token-Selection Plug-in

## Hardware & Environment Setup
- Plug into an existing GRPO/DAPO/CISPO-family trainer. Official code: `https://github.com/outongyiLv/GMTS` (`GMTS-Framework1` / `GMTS-Framework2` verl layouts).
- All score inputs (entropy, ratio, advantage, clip) are already in the RLVR step.

## Quickstart Implementation

```python
import torch


def gmts_keep_mask(
    entropy: torch.Tensor,
    ratio: torch.Tensor,
    advantage: torch.Tensor,
    clip_active: torch.Tensor,
    rho: float = 0.2,
) -> torch.Tensor:
    """Keep top-rho tokens by |entropy * omega|, omega = ratio * adv * clip.

    Shapes: [B, T] or [N]. clip_active is 1 when the PPO clip indicator is on.
    """
    omega = ratio * advantage * clip_active
    score = (entropy * omega).abs()
    keep = torch.zeros_like(score, dtype=torch.bool)
    flat = score.reshape(-1)
    k = max(1, int(flat.numel() * rho))
    thresh = torch.topk(flat, k=k, largest=True).values[-1]
    keep = score >= thresh
    return keep


def gmts_token_loss(token_loss: torch.Tensor, keep: torch.Tensor) -> torch.Tensor:
    if not keep.any():
        return token_loss.new_zeros(())
    return token_loss[keep].mean()
```

## Critical Hyperparameters & Tuning Advice
- Default $\rho=0.2$. Do not train on bottom-$\delta$ tokens.
- Host algorithm stays CISPO for Pass@1 labeled RLVR; this mask does not change that default.
- DAPO: $\omega \approx r A \mathbf{1}_{\mathrm{clip}}$ (no KL). GRPO: include the KL term in $\omega$ if the trainer uses it.
