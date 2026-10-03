---
id: recipe:self-play-pretraining
type: recipe
title: "Self-Play Pretraining Zero-Data Loop"
method: method:self-play-pretraining
task: task:zero-natural-data-self-play-pretrain
target_hardware: "Small-model box; paper scale <25M, context 4096, max 34.36B tokens"
framework: "PyTorch"
repo_url: "https://github.com/nourya-aliz/self_play_pretraining"
code_status: released
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - self-play-pretraining
  - pretraining
  - zero-data
---

# Self-Play Pretraining Zero-Data Loop

## Hardware & Environment Setup
- Official: `https://github.com/nourya-aliz/self_play_pretraining` (acowsik/self_play_pretraining redirects). `code_status: released`.
- Post-train data-free self-evolution stays J-Zero. Wikipedia-seeded synthetic pretrain stays SYNTH.

```bash
git clone https://github.com/nourya-aliz/self_play_pretraining.git
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def gradient_alignment_reward(grad: list[float], lookback: list[float], adam_v: list[float], eps: float = 1e-8) -> float:
    if not grad or len(grad) != len(lookback) or len(grad) != len(adam_v):
        raise ValueError("grad, lookback, and adam_v must be nonempty and aligned")
    num = 0.0
    den_g = 0.0
    den_m = 0.0
    for g, m, v in zip(grad, lookback, adam_v):
        scale = 1.0 / math.sqrt(max(v, 0.0) + eps)
        gs = g * scale
        ms = m * scale
        num += gs * ms
        den_g += gs * gs
        den_m += ms * ms
    denom = math.sqrt(den_g * den_m)
    if denom <= eps:
        return 0.0
    return num / denom
```

Learner: mean NTP on UTM output bytes. Generator: GRPO-style policy gradient on this reward, plus SFT on high-reward / mutated / replay programs. Do not train on natural text inside the self-play loop.

## Critical Hyperparameters & Tuning Advice
- Context 4096. Paper searches learner LR, generator-to-learner LR ratio, batch size, and generator KL coefficient β. Max budget 34.36B tokens.
- Difficulty-only rewards are the wrong ablation.
- Scale in the paper is below 25M. This is not a 7B pretrain recipe.
