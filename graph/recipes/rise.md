---
id: recipe:rise
type: recipe
title: "RISE Self-Extrapolating Distillation Recipe"
method: method:rise
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB (paper: one VeRL node)"
framework: "PyTorch / veRL"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
tags:
  - recipe
  - rise
  - distillation
  - rlvr
---

# RISE Self-Extrapolating Distillation Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-07. Paper trains in VeRL on 8 GPUs, one epoch, AdamW constant LR, no warmup, GRPO advantages without std normalization, token-IS clip 2.0. Prompts 2048, responses 8192.
- Host Pass@1 labeled RLVR stays CISPO. This loop is RLVR + self-extrapolated OPD, not a CISPO replacement and not OPSA.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def logit_extrapolate(logp_now: torch.Tensor, logp_after: torch.Tensor, beta: float) -> torch.Tensor:
    """π_future logps from current vs post-RLVR logps. Shapes: [B, T, V] or [B, T, K+1]."""
    return logp_now + beta * (logp_after - logp_now)


def rise_js_loss(student_logp: torch.Tensor, teacher_logp: torch.Tensor, mask: torch.Tensor) -> torch.Tensor:
    """Jensen–Shannon to a stop-grad teacher. teacher_logp is sg[π_future]."""
    teacher = teacher_logp.detach()
    p = student_logp.exp()
    q = teacher.exp()
    m = 0.5 * (p + q)
    log_m = m.clamp_min(1e-12).log()
    js = 0.5 * (p * (student_logp - log_m) + q * (teacher - log_m)).sum(dim=-1)
    denom = mask.sum().clamp_min(1.0)
    return (js * mask).sum() / denom


def beta_linear(step: int, total: int, beta0: float = 1.2) -> float:
    frac = 1.0 - (step / max(total, 1))
    return 1.0 + (beta0 - 1.0) * frac


def ema_anchor(anchor: dict[str, torch.Tensor], params: dict[str, torch.Tensor], eta: float) -> None:
    for name, p in params.items():
        anchor[name].mul_(1.0 - eta).add_(p.detach(), alpha=eta)
```

## Critical Hyperparameters & Tuning Advice
- $\beta_0=1.2$, linear decay to $1$. Cosine is slightly better in Table 4 (63.0 vs 62.5); do not freeze $\beta$.
- Top-$K=100$ (math/STEM), $K=20$ (code) plus a tail bucket.
- Anchor $\eta=0.1$ (EMA) on Qwen; $\eta=1$ (previous checkpoint) on OLMo.
- Weight-space alternative: $\theta_{\mathrm{future}}=\theta_n+\beta(\theta_{n+1}'-\theta_n)$, then one teacher forward.
- Do not skip the RLVR phase. Extrapolation without outcome grounding is not this method.
