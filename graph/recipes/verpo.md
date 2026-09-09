---
id: recipe:verpo
type: recipe
title: "VERPO Evidence-Regularized PO"
method: method:verpo
task: task:privileged-teacher-opsd
target_hardware: "same as host RLVR (paper: Qwen3-4B/8B, Llama-3.2-1B)"
framework: "PyTorch / host RLVR trainer"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - verpo
  - opsd
  - privileged-teacher
---

# VERPO Evidence-Regularized PO

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Host Pass@1 algorithm stays CISPO. Privileged-teacher OPSD default stays VISTA.
- Keep an evidence-free restoration term independent of the ZPD acceptance gate.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def fisher_evidence_contrast(
    correction: torch.Tensor,
    evidence_dir: torch.Tensor,
    eps: float = 1e-8,
) -> torch.Tensor:
    """Attenuate token corrections along an estimated evidence-presence direction."""
    u = F.normalize(evidence_dir.reshape(1, -1), dim=-1, eps=eps).reshape_as(evidence_dir)
    parallel = (correction * u).sum() * u
    return correction - parallel


def zpd_accept(
    reward_align: torch.Tensor,
    fisher_cost: torch.Tensor,
    tau: float = 1.0,
) -> torch.Tensor:
    """Stopped scalar in [0, 1]. Does not backprop into the gate."""
    raw = torch.sigmoid((reward_align - fisher_cost) / tau)
    return raw.detach()


def verpo_token_term(
    student_logp: torch.Tensor,
    reference_logp: torch.Tensor,
    evidence_logp: torch.Tensor,
    advantage: torch.Tensor,
    evidence_dir: torch.Tensor,
    fisher_cost: torch.Tensor,
) -> torch.Tensor:
    """Outcome term + ungated restoration + gated signed evidence correction."""
    restore = student_logp - reference_logp.detach()
    signed = (evidence_logp.detach() - student_logp) * advantage
    signed = fisher_evidence_contrast(signed, evidence_dir)
    gate = zpd_accept(advantage, fisher_cost)
    return -(advantage * student_logp + restore + gate * signed).sum()
```

## Critical Hyperparameters & Tuning Advice
- Do not let the evidence channel overwrite the outcome advantage.
- Reference restoration stays ungated. Only the signed correction uses ZPD.
