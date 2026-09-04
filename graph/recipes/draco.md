---
id: recipe:draco
type: recipe
title: "DRACO Rubric Step-Credit Recipe"
method: method:draco
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "8x NVIDIA H100 80GB (paper LoRA GRPO) plus a frozen judge"
framework: "PyTorch / GRPO"
repo_url: "https://github.com/IBM/draco"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - draco
  - agentic
  - rubrics
---

# DRACO Rubric Step-Credit Recipe

## Hardware & Environment Setup
- Official code: `https://github.com/IBM/draco`. Paper: LoRA GRPO, batch 16, group 6, 8x H100. Judge calls are separate from the policy update.
- Ground-truth unit tests are eval-only. Do not wire them into $R_i$ if you are in the outcome-blind setting.

## Quickstart Implementation

```python
def step_advantages(traj_adv: float, n_tokens: list[int], quality: list[float]) -> list[float]:
    """Redistribute GRPO trajectory advantage A_i onto steps. quality Q_j in [0, 1].

    Conserves sum_j n_j * a_j = A_i * N and never flips sign.
    """
    if traj_adv >= 0:
        weights = list(quality)
    else:
        weights = [1.0 - q for q in quality]
    w_sum = sum(weights)
    n_total = sum(n_tokens)
    if w_sum <= 0.0 or n_total <= 0:
        return [traj_adv] * len(n_tokens)
    return [traj_adv * n_total * w / max(n, 1) / w_sum for w, n in zip(weights, n_tokens)]


def rubric_reward(n_pass: int, n_fail: int) -> float:
    denom = n_pass + n_fail
    if denom <= 0:
        return 0.0
    return (n_pass - n_fail) / denom
```

## Critical Hyperparameters & Tuning Advice
- Drop criteria that every group member passed. Shared criterion set, per-trajectory applicability.
- Uncited steps inherit mean Q of cited steps.
- When a verifier exists, prefer CANOPY rather than paying a frontier judge to reconstruct the checker.
- Does not replace SAO, CISPO, CANOPY, or FoldGRPO.
