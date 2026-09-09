---
id: recipe:circuitlens
type: recipe
title: "CircuitLens CRS Data Selection"
method: method:circuitlens
task: task:math-code-rl-dense
target_hardware: "1x GPU for frozen-base CRS scoring + host RLVR"
framework: "PyTorch"
repo_url: "none found"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.51.0"
tags:
  - recipe
  - circuitlens
  - rlvr
---

# CircuitLens CRS Data Selection

## Hardware & Environment Setup
- No official GitHub as of 2026-09-09. Score prompts with a frozen base in one forward; train with the host GRPO/CISPO loop.
- Paper uses 46 contrastive-ablation heads. Re-identify heads if the base model changes.

## Quickstart Implementation

```python
import torch


def circuit_reasoning_score(head_acts: torch.Tensor, head_index: torch.Tensor) -> torch.Tensor:
    """Mean absolute activation on selected reasoning heads. head_acts: [H, T], head_index: [K]."""
    selected = head_acts.index_select(0, head_index)
    return selected.abs().mean()


def lowest_decile_mask(scores: torch.Tensor) -> torch.Tensor:
    """Keep the lowest-engagement 10% (7B medium-math finding, not universal)."""
    thresh = torch.quantile(scores.float(), 0.1)
    return scores <= thresh
```

## Critical Hyperparameters & Tuning Advice
- Re-validate direction at each scale. Do not copy the 7B low-decile rule to 1.5B.
- Host algorithm stays CISPO. This only ranks prompts.
