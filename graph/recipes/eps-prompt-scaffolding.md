---
id: recipe:eps-prompt-scaffolding
type: recipe
title: "EPS Prompt Scaffolding on GRPO"
method: method:eps-prompt-scaffolding
task: task:mllm-rl-prompt-curriculum
target_hardware: "8-GPU FSDP box for Qwen3-VL-2B/4B GRPO (paper); teacher API for Qwen-VL-Max"
framework: "PyTorch GRPO host (FSDP) + async teacher rewrite worker"
repo_url: none found
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - eps
  - grpo
  - multimodal-rl
---

# EPS Prompt Scaffolding on GRPO

## Hardware & Environment Setup
- No official GitHub as of 2026-09-15 (`arXiv:2609.15051`). `repo_url: none found`. Project page: `https://mqleet.github.io/EPS-ProjectPage/`. Loop is Appendix A.
- Paper: Qwen3-VL-2B/4B, Geometry3K + MMK12, 3000 GRPO steps, 8 rollouts/prompt, batch 16, 8-GPU FSDP, lr 1e-6, clip 0.2, KL 0.01, max response 3072. Teacher Qwen-VL-Max. Default \(\tau=0\).
- Dense Pass@1 stays CISPO. MoE/VL loss stays SAPO. Video stays OraRL.

## Quickstart Implementation

```python
import torch


def exploration_potential_score(rewards: torch.Tensor, beta: float) -> torch.Tensor:
    """Ê(x) = Σ r_i · softmax(r_i / β) − mean(r). rewards: (N,) or (B, N)."""
    shifted = rewards - rewards.amax(dim=-1, keepdim=True)
    weights = torch.softmax(shifted / beta, dim=-1)
    weighted = (weights * rewards).sum(dim=-1)
    return weighted - rewards.mean(dim=-1)


def partition_prompts(eps: torch.Tensor, tau: float = 0.0):
    """Keep ℰ̂(x) > τ for GRPO; route ℰ̂(x) ≤ τ to the teacher."""
    keep = eps > tau
    return keep, ~keep


def refresh_pool(active, refresh_buffer, reserve, tau: float = 0.0):
    """Reinject scaffolded prompts; reactivate reserved originals once EPS rises."""
    if refresh_buffer:
        active.extend(refresh_buffer)
        refresh_buffer.clear()
    revived = [p for p in reserve if p.get("eps", tau) > tau]
    for prompt in revived:
        reserve.remove(prompt)
        active.append(prompt)
    return active
```

## Critical Hyperparameters & Tuning Advice
- Host remains GRPO. Do not swap CISPO/SAPO for this loop.
- \(\tau=0\) is the paper default (idealized EPS is non-negative; negatives are noise or currently-hard prompts).
- Teacher rewrite must preserve the task and not dump the answer. Paper scaffolds are answer-aware.
- Stabilized softmax (subtract max) is required for small \(\beta\).
