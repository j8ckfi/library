---
id: recipe:opd-hard-cot-selection
type: recipe
title: "OPD Hard-CoT Query Selection Recipe"
method: method:opd-hard-cot-selection
task: task:student-distillation
target_hardware: "8x NVIDIA H100 80GB (same as host OPD)"
framework: "PyTorch / veRL"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "verl>=0.4.0"
  - "transformers>=4.51.0"
  - "vllm>=0.7.0"
tags:
  - recipe
  - opd
  - distillation
  - data-selection
---

# OPD Hard-CoT Query Selection Recipe

## Hardware & Environment Setup
- No official GitHub as of 2026-09-07. Host loop is `recipe:opd` (student rollouts + teacher top-$k$ reverse KL). This recipe only ranks the query set.
- Paper: verl, batch and mini-batch 64, 8 responses/prompt, temperature 1.0, max response 7168, top-16 reverse KL, 279 steps, 8x H100.

## Quickstart Implementation

```python
from typing import Sequence


def difficulty_score(student_pass: Sequence[float], teacher_pass: Sequence[float]) -> list[float]:
    """A_i = (S_i + T_i) / 2 from 16-rollout pass rates in [0, 1]."""
    return [0.5 * (s + t) for s, t in zip(student_pass, teacher_pass)]


def select_hard(
    example_ids: Sequence[str],
    scores: Sequence[float],
    k: int = 8,
    hard_threshold: float = 0.1,
) -> list[str]:
    """Keep Hard A_i < 0.1, then take the k hardest (lowest A_i). Tie-break by original id."""
    ranked = sorted(zip(scores, example_ids), key=lambda row: (row[0], row[1]))
    hard = [(score, eid) for score, eid in ranked if score < hard_threshold]
    pool = hard if hard else ranked
    return [eid for _, eid in pool[:k]]
```

## Critical Hyperparameters & Tuning Advice
- Hard band is $A_i<0.1$; easy is $A_i>0.9$. Paper 8-shot uses $\{\pi_{874},\ldots,\pi_{997}\}$ from a 1000-example DAPO-Math pool ranked by $A_i$.
- Host algorithm stays `method:opd`. If the question is diversity vs volume rather than hard vs easy, use `method:opd-one-example`.
- Keep 279-step (or host full-set step) budget; few-shot is fewer prompts, not a shorter run.
- Teacher-unsolvable hard items can stay in the set.
