---
id: recipe:synth
type: recipe
title: "SYNTH Baguettotron Single-Stage Pretrain"
method: method:synth
task: task:synthetic-single-stage-pretrain
target_hardware: "16× H100 64GB (torchtitan FSDP); early Nanotron on H100"
framework: "PyTorch / torchtitan FSDP (Nanotron for Monad and 350M)"
repo_url: "https://huggingface.co/datasets/PleIAs/SYNTH"
code_status: partial
pip_dependencies:
  - "torch>=2.5.0"
tags:
  - recipe
  - synth
  - baguettotron
  - pretraining
  - synthetic-data
---

# SYNTH Baguettotron Single-Stage Pretrain

## Hardware & Environment Setup
- Dataset: `https://huggingface.co/datasets/PleIAs/SYNTH` (also `SYNTH-Initiative/SYNTH`). Weights: `https://huggingface.co/PleIAs/Baguettotron` is the 321M / ~200B card, not the 594M / 158B FActScore run.
- Paper training code is not released (`code_status: partial`). Configs: sequence 2048, AdamW weight decay 0.01, grad clip 1.0, 16.6% linear decay tail to 0.2% of peak LR, 16×H100 FSDP.
- Open mix stays OLMo-3. 7B optimizer stays Muon2. UTM self-play stays `method:self-play-pretraining`.

```bash
huggingface-cli download PleIAs/SYNTH --repo-type dataset
huggingface-cli download PleIAs/Baguettotron
```

## Quickstart Implementation

```python
from __future__ import annotations

import math


def adamw_decayed_lr(step: int, peak_lr: float, total_steps: int, warmup: int = 10000, tail_frac: float = 0.166) -> float:
    if total_steps <= 0 or peak_lr <= 0.0:
        raise ValueError("total_steps and peak_lr must be positive")
    if step < 0:
        raise ValueError("step must be nonnegative")
    if step < warmup:
        return peak_lr * (step + 1) / warmup
    tail_start = int((1.0 - tail_frac) * total_steps)
    if step < tail_start:
        return peak_lr
    remaining = max(1, total_steps - tail_start)
    progress = min(1.0, (step - tail_start) / remaining)
    return peak_lr * (1.0 - 0.998 * progress)
```

Train ordinary NTP on SYNTH. Do not add an SFT or RL stage for the paper recipe. Baguettotron-600M is 594M / 48 layers / d=1024 / 158B tokens in Table 1.

## Critical Hyperparameters & Tuning Advice
- Sequence 2048 for the main dense/MoE runs. Monad used 1024 then a 2048 extension.
- Knowledge is capped by ~58k Wikipedia seeds; do not expect web-scale coverage.
- Do not confuse HF `PleIAs/Baguettotron` (321M) with the 594M FActScore checkpoint.
