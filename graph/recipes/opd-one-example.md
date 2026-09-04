---
id: recipe:opd-one-example
type: recipe
title: "One-Shot OPD Query-Set Recipe"
method: method:opd-one-example
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB (same as host OPD)"
framework: "PyTorch / veRL"
repo_url: "https://github.com/Thinking-Space/One-Shot-OPD"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
  - "transformers>=4.51.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - opd
  - distillation
  - data-efficiency
---

# One-Shot OPD Query-Set Recipe

## Hardware & Environment Setup
- Official code: `https://github.com/Thinking-Space/One-Shot-OPD` (veRL). Same student-rollout + teacher-logprob loop as `recipe:opd`.
- Paper: batch of 64 rollouts, AdamW 1e-6, temperature 1.0, grad clip 1.0. Math used top-k advantage with k=16; code / IF / agent used sampled-token advantage.

## Quickstart Implementation

```python
import torch


def sampled_token_opd_advantage(teacher_logp: torch.Tensor, student_logp: torch.Tensor) -> torch.Tensor:
    """A_i = log pi_T(y_i|s) - log pi_theta(y_i|s). Shapes: [B, T]."""
    return teacher_logp - student_logp


def topk_opd_advantage(
    student_probs: torch.Tensor,
    teacher_logp: torch.Tensor,
    student_logp: torch.Tensor,
    k: int = 16,
) -> torch.Tensor:
    """Truncate reverse KL to the student's top-k tokens (paper Eq. 3).

    student_probs, teacher_logp, student_logp: [B, T, V]
    """
    topk_idx = student_probs.topk(k, dim=-1).indices
    p = student_probs.gather(-1, topk_idx)
    p = p / p.sum(dim=-1, keepdim=True).clamp_min(1e-12)
    t_lp = teacher_logp.gather(-1, topk_idx)
    s_lp = student_logp.gather(-1, topk_idx)
    return (p * (t_lp - s_lp)).sum(dim=-1)
```

## Critical Hyperparameters & Tuning Advice
- Prefer ~16 semantically diverse queries per domain over the full prompt dump. Cluster with BGE-M3 (or equivalent) and take one representative per cluster.
- Host algorithm stays `method:opd`. This recipe only changes the query set.
- If 16-shot already matches full-data OPD, spend GPU-weeks on absorption / step-efficiency, not more prompts.
