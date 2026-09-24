---
id: recipe:rewardverse
type: recipe
title: "RewardVerse RGPO Video RM"
method: method:rewardverse
task: task:posttrain-diffusion
target_hardware: "Qwen2.5-VL-7B-class RM box; optional Wan-2.2-A14B GRPO for downstream use of the RM"
framework: "PyTorch / GRPO video reward modeling"
repo_url: "https://github.com/2kxx/RewardVerse"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - rewardverse
  - video
  - reward-model
---

# RewardVerse RGPO Video RM

## Hardware & Environment Setup
- Official: `https://github.com/2kxx/RewardVerse`. README and docs present as of 2026-09-24. `code_status: released`.
- Generator alignment stays DiffusionOPSD / Self-OPD. Video MLLM perception RL stays OraRL.

```bash
git clone https://github.com/2kxx/RewardVerse.git && cd RewardVerse
```

## Quickstart Implementation

```python
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class RubricTheme:
    name: str
    weight: float
    tip: str


def soft_logit_score(token_logps: dict[int, float], rating_ids: list[int]) -> float:
    mass = sum(token_logps.get(i, 0.0) for i in rating_ids)
    if mass <= 0.0:
        return 0.0
    expected = 0.0
    for i, rating in enumerate(rating_ids, start=1):
        expected += i * (token_logps.get(rating, 0.0) / mass)
    return expected


def rubric_weighted_score(theme_scores: list[float], themes: list[RubricTheme]) -> float:
    total_w = sum(t.weight for t in themes)
    if total_w <= 0.0:
        return 0.0
    return sum(s * t.weight for s, t in zip(theme_scores, themes)) / total_w
```

Generate the rubric from the query only. Score each theme with soft-logits, then weight. Do not emit a free-form scalar.

## Critical Hyperparameters & Tuning Advice
- Stage-1 scorer warm-up before joint rubric training. Skipping it dropped EvalVerse PLCC by 0.099 in the paper.
- 30 pairs per dimension is the measured budget. Direct rubric-free training at the same budget lagged Full RGPO.
- Keep the generator on DiffusionOPSD / Self-OPD. This recipe trains the RM.
