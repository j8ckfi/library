---
id: recipe:j-zero
type: recipe
title: "J-Zero Data-Free Self-Evolution Recipe"
method: method:j-zero
task: task:data-free-self-evolution
target_hardware: "4x NVIDIA B200 + 4x NVIDIA H200"
framework: "PyTorch / verl (GRPO inner loop)"
repo_url: "https://github.com/GyoukChu/J-Zero"
pip_dependencies:
  - "torch>=2.6.0"
  - "verl>=0.4.0"
  - "transformers>=4.51.0"
  - "vllm>=0.8.0"
tags:
  - recipe
  - self-evolution
  - data-free
  - grpo
  - j-zero
---

# J-Zero Data-Free Self-Evolution Recipe

## Hardware & Environment Setup
- Recommended Hardware: 4x NVIDIA B200 + 4x NVIDIA H200 as in the paper.
- Framework: verl GRPO for Challenger and Solver; Bradley–Terry update for the Judge.
- Official code: `https://github.com/GyoukChu/J-Zero`. Project page: `https://gyoukchu.github.io/projects/j_zero/`.
- Judge init: Skywork-Reward-V2-Llama-3.1-8B. Policies: Qwen3-4B-Base / Qwen3-8B-Base.

## Quickstart Implementation

```python
import torch
import torch.nn.functional as F


def challenger_reward(
    mean_solver_score: torch.Tensor,
    repetition_penalty: torch.Tensor,
    format_ok: torch.Tensor,
) -> torch.Tensor:
    """Challenger composite reward: hard tasks, with repetition and format penalties."""
    difficulty = 1.0 - mean_solver_score
    valid = torch.clamp(difficulty - repetition_penalty, min=0.0)
    invalid = -1.0 - repetition_penalty
    return torch.where(format_ok, valid, invalid)


def judge_bradley_terry_loss(
    judge_chosen_logit: torch.Tensor,
    judge_rejected_logit: torch.Tensor,
) -> torch.Tensor:
    """BT loss on pairs whose order is known from loop structure, not Judge scores.

    Role-asymmetry: Solver answer > Challenger answer on the same task.
    Subtask-amplification: composed divide-and-conquer answer > Solver one-shot.
    """
    return -F.logsigmoid(judge_chosen_logit - judge_rejected_logit).mean()


def select_frontier_tasks(judge_scores: torch.Tensor, top_k: int) -> torch.Tensor:
    """Keep tasks with largest Solver-score dispersion for the Solver GRPO step."""
    dispersion = judge_scores.std(dim=-1)
    k = min(top_k, dispersion.numel())
    return torch.topk(dispersion, k=k, largest=True).indices
```

Each iteration on verl: train Challenger 5 GRPO steps (batch 16, 4 rollouts), Solver 15 GRPO steps on the top-dispersion tasks (batch 128, 5 rollouts), then Judge 8 BT steps (batch 64) on equal parts $\mathcal{D}_{\mathrm{role}}$ and $\mathcal{D}_{\mathrm{amp}}$. GRPO clip $(0.20, 0.28)$, KL coefficient 0.01, Challenger/Solver LR $1\times 10^{-6}$, Judge LR $5\times 10^{-7}$, no weight decay.

## Critical Hyperparameters & Tuning Advice
- **Do not take Judge preference labels from the Judge's own scores.** Chosen/rejected order comes from role asymmetry and subtask amplification.
- Inner GRPO is self-play mechanics. For labeled math/code RLVR, this library still routes to `method:cispo`, not GRPO.
- Frozen-Judge ablations plateau after ~2 iterations; keep Judge co-adaptation enabled if the run must go past that.
