---
id: recipe:oprd
type: recipe
title: "OPRD Reverse Distillation Recipe"
method: method:oprd
task: task:student-distillation
target_hardware: "same as host GRPO/OPD (paper: Qwen3 4B teacher / 8B student)"
framework: "PyTorch / host RLVR + teacher logps"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - oprd
  - distillation
  - weak-to-strong
---

# OPRD Reverse Distillation Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Needs student rollouts, a frozen teacher, the teacher's reference policy, and an outcome verifier.
- Host Pass@1 algorithm stays CISPO when you are not using a teacher shift. Matching distill stays OPD. Weak-policy matching stays W2S-OPD.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def teacher_shift_direction(
    teacher_logp: torch.Tensor,
    reference_logp: torch.Tensor,
) -> torch.Tensor:
    """Detached teacher policy-shift on the sampled tokens. [T]."""
    return (teacher_logp - reference_logp).detach()


def verifier_token_grad(student_logp: torch.Tensor, advantage: torch.Tensor) -> torch.Tensor:
    """Verifier-driven per-token term. advantage is outcome group-relative, broadcast to [T]."""
    return student_logp * advantage


def oprd_scale(shift: torch.Tensor, student_term: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Keep the component of the student term along the teacher-shift direction.

    Amplify only when the verifier advantage and the shift agree in sign at the sequence level.
    """
    shift_n = F.normalize(shift.unsqueeze(0), dim=-1, eps=eps).squeeze(0)
    proj = (student_term * shift_n).sum()
    aligned = torch.relu(proj)
    return aligned * shift_n


def oprd_loss(
    student_logp: torch.Tensor,
    teacher_logp: torch.Tensor,
    reference_logp: torch.Tensor,
    advantage: torch.Tensor,
) -> torch.Tensor:
    """Negative aligned projection. advantage is a scalar sequence advantage."""
    shift = teacher_shift_direction(teacher_logp, reference_logp)
    term = verifier_token_grad(student_logp, advantage)
    scaled = oprd_scale(shift, term)
    return -scaled.sum()
```

## Critical Hyperparameters & Tuning Advice
- Rescale verifier-supported updates only. Do not regress the student onto the weak teacher.
- Average several checkpoints when comparing to GRPO/OPD (paper: five equally spaced).
- Multi-teacher: pair each batch item with its specialist; do not match the full specialist policy.
