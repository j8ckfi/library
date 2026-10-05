---
id: recipe:metarubric
type: recipe
title: "MetaRubric Evidence-Aware Rubric RL"
method: method:metarubric
task: task:outcome-only-long-horizon-agent-rl
target_hardware: "GRPO host plus an LM rubric judge; paper: Qwen3-4B/8B, Gemma-e2b"
framework: "PyTorch GRPO with a three-score criterion judge"
repo_url: "https://github.com/metarubric/metarubric"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - metarubric
  - rubric
  - rl-alignment
---

# MetaRubric Evidence-Aware Rubric RL

## Hardware & Environment Setup
- Official: `https://github.com/metarubric/metarubric`. Project: `https://metarubric.github.io`. `code_status: released`.
- Outcome-blind rubrics stay DRACO. Checker coverage stays CANOPY.

```bash
git clone https://github.com/metarubric/metarubric.git && cd metarubric
```

## Quickstart Implementation

```python
from __future__ import annotations


def criterion_credit(satisfaction: float, coverage: float, evidence: float) -> float:
    for name, val in (
        ("satisfaction", satisfaction),
        ("coverage", coverage),
        ("evidence", evidence),
    ):
        if not 0.0 <= val <= 1.0:
            raise ValueError(f"{name} must be in [0, 1]")
    return min(satisfaction, coverage, evidence)
```

Judge each criterion with three scores. Credit is the min. Run GRPO on the weighted sum. At stage boundaries, revise criterion text and weights from current-policy errors; keep the original rubric's meaning, including the paired counterfactual prompt.

## Critical Hyperparameters & Tuning Advice
- PubMedQA Qwen3-4B 78.40 vs static-judge GRPO 72.40. Do not retarget DRACO or CANOPY.
