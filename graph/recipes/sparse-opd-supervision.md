---
id: recipe:sparse-opd-supervision
type: recipe
title: "Sparse OPD Supervision Recipe"
method: method:sparse-opd-supervision
task: task:student-distillation
target_hardware: "same as host sampled-token OPD (paper: veRL 0.8.0, DAPO-Math-17K)"
framework: "PyTorch / veRL"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - sparse-supervision
  - opd
  - distillation
---

# Sparse OPD Supervision Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-08. Add a keep-mask to sampled-token OPD (`method:opd`). Paper: veRL 0.8.0 native OPD, batch 128 prompts, n=1, max response 8192, AdamW $1\times10^{-6}$, clip 0.2.
- Host distill algorithm stays OPD. Pass@1 labeled RLVR stays CISPO.

## Quickstart Implementation

```python
import torch


def opd_token_advantage(teacher_logp: torch.Tensor, student_logp: torch.Tensor) -> torch.Tensor:
    """A_t = log π_T(y_t|h_t) − log π_θ(y_t|h_t). teacher_logp/student_logp: [T]."""
    return teacher_logp - student_logp


def sparse_keep_mask(adv: torch.Tensor, kind: str = "minmaxtok") -> torch.Tensor:
    """Boolean [T] keep-mask. Table 2: mintok = max A_t, maxtok = min A_t."""
    t = adv.numel()
    mask = torch.zeros(t, dtype=torch.bool, device=adv.device)
    if t == 0:
        return mask
    if kind == "rand1tok":
        mask[int(torch.randint(t, (1,), device=adv.device).item())] = True
        return mask
    if kind == "mintok":
        mask[int(adv.argmax().item())] = True
        return mask
    if kind == "maxtok":
        mask[int(adv.argmin().item())] = True
        return mask
    if kind == "minmaxtok":
        mask[int(adv.argmax().item())] = True
        mask[int(adv.argmin().item())] = True
        return mask
    if kind == "pctltail":
        k = max(1, int(round(0.0005 * t)))
        top = torch.topk(adv, k=min(k, t)).indices
        bot = torch.topk(-adv, k=min(k, t)).indices
        mask[top] = True
        mask[bot] = True
        return mask
    raise ValueError(f"unknown sparse OPD kind {kind!r}")
```

## Critical Hyperparameters & Tuning Advice
- Default try `minmaxtok` or `pctltail`. Do not start from `maxtok` on a much-smaller base student.
- Mean-normalize by $|y|$, including dropped tokens, matching Eq. (4.1).
- Does not replace OPD, CISPO, or IDA-OPD.
