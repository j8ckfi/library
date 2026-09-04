---
id: recipe:ida-opd
type: recipe
title: "IDA-OPD Entropy-Shrinkage Recipe"
method: method:ida-opd
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB (same as host sampled-token OPD)"
framework: "PyTorch / vLLM"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - ida-opd
  - distillation
  - on-policy
---

# IDA-OPD Entropy-Shrinkage Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-04. Add the $\mathcal{I}_H$ gate to an existing sampled-token OPD loop (student rollout + teacher logp on the emitted token + student full next-token distribution).
- Host distill algorithm stays `method:opd`.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def entropy_direction(probs: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """D_y from the student's next-token distribution. probs: [B, V], y: [B]."""
    logp = (probs.clamp_min(1e-12)).log()
    entropy = -(probs * logp).sum(dim=-1)
    p2 = probs.square()
    s2_term = (p2 * (logp + entropy.unsqueeze(-1))).sum(dim=-1)
    p_y = probs.gather(-1, y.unsqueeze(-1)).squeeze(-1)
    logp_y = logp.gather(-1, y.unsqueeze(-1)).squeeze(-1)
    return s2_term - p_y * (logp_y + entropy)


def ida_opd_advantage(teacher_logp_y: torch.Tensor, student_logp_y: torch.Tensor, probs: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """Keep A_y when I_H >= 0; else shrink by |q-p|/(q+p)."""
    a = teacher_logp_y - student_logp_y
    influence = a * entropy_direction(probs, y)
    q = teacher_logp_y.exp()
    p = student_logp_y.exp()
    w = (q - p).abs() / (q + p).clamp_min(1e-12)
    return torch.where(influence >= 0, a, w * a)


def ida_opd_loss(student_logits: torch.Tensor, y: torch.Tensor, teacher_logp_y: torch.Tensor) -> torch.Tensor:
    logp = F.log_softmax(student_logits, dim=-1)
    probs = logp.exp()
    student_logp_y = logp.gather(-1, y.unsqueeze(-1)).squeeze(-1)
    adv = ida_opd_advantage(teacher_logp_y, student_logp_y, probs, y)
    return -(adv.detach() * student_logp_y).mean()
```

## Critical Hyperparameters & Tuning Advice
- Do not apply $w_y$ at entropy-expanding positions. The sign of $\mathcal{I}_H$ is the gate.
- Needs student softmax, not just the sampled log-prob.
- Does not replace CISPO or unfiltered OPD.
