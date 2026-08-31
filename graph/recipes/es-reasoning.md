---
id: recipe:es-reasoning
type: recipe
title: "ES-Reasoning One-Point Evolution Strategies Recipe"
method: method:es-reasoning
task: task:passk-reasoning-coverage
target_hardware: "8x single-GPU vLLM workers (paper Easy/Hard comparisons)"
framework: "PyTorch / vLLM (forward-only; no backward)"
repo_url: "https://github.com/yunpengba7/understanding-es"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - evolution-strategies
  - passk
  - es-reasoning
---

# ES-Reasoning One-Point Evolution Strategies Recipe

## Hardware & Environment Setup
- Paper layout: eight single-GPU vLLM engines, one perturbation direction group per engine. No backward state.
- Official code: `https://github.com/yunpengba7/understanding-es`.
- FLOP-match versus GRPO: $N=32$ directions vs $G=8$ responses.

## Quickstart Implementation

```python
import torch


def zscore(rewards: torch.Tensor, eps: float = 1e-8) -> torch.Tensor:
    """Population z-score. Required; raw rewards underperform."""
    centered = rewards - rewards.mean()
    denom = torch.sqrt((centered.square().mean()) + eps)
    return centered / denom


def es_center_update(
    epsilon: torch.Tensor,
    rewards: torch.Tensor,
    alpha: float = 2.5e-4,
) -> torch.Tensor:
    """One-point ES: theta <- theta + (alpha / N) * sum z_i epsilon_i.

    Args:
        epsilon: Perturbation directions [N, ...param].
        rewards: Verifier rewards per direction [N].
        alpha: Update scale (paper 2.5e-4). Perturbations are theta + sigma * epsilon
            with sigma=1.5e-3 at evaluation time; alpha absorbs 1/sigma in the paper's
            practical estimator.
    """
    z = zscore(rewards)
    n = float(epsilon.size(0))
    weights = (z / n).view(-1, *([1] * (epsilon.ndim - 1)))
    return alpha * (weights * epsilon).sum(dim=0)
```

At each step: draw $N$ seeds, add $\sigma\epsilon_i$ in place, generate one response per prompt, restore the center, z-score $R_i$, apply the update. Do not use two-point/antithetic ZO for regenerated CoT rewards.

## Critical Hyperparameters & Tuning Advice
- $\sigma=1.5\times 10^{-3}$, $\alpha=2.5\times 10^{-4}$. Must z-score.
- $N=32$ to FLOP-match GRPO $G=8$. 0.5B needs $N\approx 32$ versus $N=64$; 1.5B/3B can use $N=16$.
- Sequential ES then GRPO under a shared update budget if Pass@1 and Pass@32 both matter. That does not revive GRPO as this library's RLVR default (`method:cispo`).
