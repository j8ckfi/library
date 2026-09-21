---
id: recipe:vision-rl2
type: recipe
title: "Vision-RL2 Region-Level RL"
method: method:vision-rl2
task: task:mllm-finegrained-perception-rl
target_hardware: "1–4 GPUs depending on backbone (paper reports RTX A6000 latency; 4B/9B Qwen3.5, 7B Qwen2.5-VL, 12B Gemma-4)"
framework: "PyTorch / transformers / lmms-eval / DeepSpeed (Qwen); sdpa-only for Gemma-4"
repo_url: "https://github.com/YuHengsss/VisionRL2"
code_status: released
pip_dependencies:
  - "torch>=2.4.0"
  - "transformers>=4.51.0"
  - "lmms-eval"
tags:
  - recipe
  - vision-rl2
  - multimodal-rl
  - finegrained-perception
---

# Vision-RL2 Region-Level RL

## Hardware & Environment Setup
- Official: `https://github.com/YuHengsss/VisionRL2`
- Project: `https://yuhengsss.github.io/VisionRL2/`
- Weights/data: Hugging Face collection `YuhengSSS/visionrl2`
- One conda env per backbone family (`requirements.txt`, `requirements_qwen2_5vl.txt`, `requirements_gemma4.txt`).
- EPS prompt scaffolding stays the multimodal prompt-curriculum first hop. OraRL stays video.

## Quickstart Implementation

```bash
hf download YuhengSSS/VisionRL2-data --repo-type dataset --local-dir data/VisionRL2-data
MODEL=qwen3_5-4b DATASET_ROOT=datasets bash scripts/train_sdrpn_online.sh
PHASE_A_CKPT=output/sdrpn/qwen3_5-4b-sdrpn-K21T3 DATASET_ROOT=datasets \
  bash scripts/train_rl_qwen3_5_4b.sh
```

Leave-one-out reader sketch:

```python
from __future__ import annotations

import math


def leave_one_out_delta(h_full: float, h_without: float, clip: float = 5.0) -> float:
    delta = h_full - h_without
    return max(-clip, min(clip, delta))


def subtractive_advantage(delta: float, margin: float, scale: float) -> float:
    return (margin - delta) / (scale + 1.0)
```

## Critical Hyperparameters & Tuning Advice
- Train only the RoI predictor. Freeze the MLLM reader.
- Stage 1 is SD-RPN; stage 2 is region-level RL from that checkpoint. Qwen2.5-VL-7B ships a stage-1 checkpoint so only stage 2 is required.
- Default batch 32, lr \(1.5\times 10^{-5}\), one epoch, 576-token source limit during RL.
- Keep subtractive noise margin and the additive recovery group. Dropping either costs ~1 point.
- Do not replace the functional score with binary generation accuracy.
