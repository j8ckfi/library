---
id: recipe:ra-opd
type: recipe
title: "RA-OPD Reward-Aligned Trajectory Filter"
method: method:ra-opd
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB (same as host OPD)"
framework: "PyTorch / vLLM"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - ra-opd
  - distillation
  - on-policy
---

# RA-OPD Reward-Aligned Trajectory Filter

## Hardware & Environment Setup
- No official GitHub as of 2026-09-01. Add the mask to an existing reverse-KL OPD loop (student rollout + teacher logprobs + outcome verifier).
- Paper trains two epochs, one on-policy response per prompt via vLLM.

## Quickstart Implementation

```python
import torch


def ra_opd_keep(teacher_logp: torch.Tensor, student_logp: torch.Tensor, reward: int) -> bool:
    """Keep a trajectory iff (2R-1) * G >= 0.

    teacher_logp, student_logp: [T] sampled-token log-probs. reward in {0, 1}.
    """
    g = (teacher_logp - student_logp).mean()
    return bool(((2 * reward - 1) * g) >= 0)


def ra_opd_batch_loss(
    teacher_logps: list[torch.Tensor],
    student_logps: list[torch.Tensor],
    rewards: list[int],
) -> torch.Tensor:
    kept_terms = []
    for t_lp, s_lp, r in zip(teacher_logps, student_logps, rewards):
        if not ra_opd_keep(t_lp.detach(), s_lp.detach(), r):
            continue
        g = (t_lp.detach() - s_lp.detach()).mean()
        kept_terms.append(-(g.detach() * s_lp).sum())
    if not kept_terms:
        return student_logps[0].new_zeros(())
    denom = sum(int(x.numel()) for x in student_logps)
    return torch.stack(kept_terms).sum() / max(denom, 1)
```

## Critical Hyperparameters & Tuning Advice
- Only change vs OPD is the mask. Do not add Uni-OPD's four-rollout groups.
- If every trajectory in the batch is dropped, skip the update (zero distillation gradient).
- Needs a binary verifier. Without $R$, this is ordinary OPD.
