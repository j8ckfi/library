---
id: recipe:esrl
type: recipe
title: "ESRL Expert-Space Exploration on slime"
method: method:esrl
task: task:math-code-rl-moe
target_hardware: "1x node 8 GPU, Qwen3-30B-A3B (paper example)"
framework: "slime + SGLang + Megatron-LM (official image nightly-dev-20251222b)"
repo_url: "https://github.com/strawberrymaster111/ESRL-Release"
pip_dependencies: []
tags:
  - recipe
  - esrl
  - moe
  - slime
---

# ESRL Expert-Space Exploration on slime

## Hardware & Environment Setup
- Official: `https://github.com/strawberrymaster111/ESRL-Release` (slime patches).
- Image: `slimerl/slime:nightly-dev-20251222b`. Then `bash scripts/apply_image_patches.sh`.
- Host MoE/VL algorithm stays SAPO. ESRL only changes rollout routing.

## Quickstart Implementation

```bash
export HF_CHECKPOINT_DIR=/path/to/huggingface-checkpoint
export REF_CHECKPOINT_DIR=/path/to/megatron-reference-checkpoint
export OUTPUT_DIR=/path/to/training-output
export TRAIN_DATA_PATH=/path/to/train.parquet
export EVAL_DATA_PATH=/path/to/eval.jsonl
bash scripts/Qwen-3-30BA3B-n010-t080-singlenode.sh
```

Essential flags from the repo:

```text
--use-slime-router
--use-rollout-routing-replay
--sglang-use-moe-sampling-routing
--sglang-moe-routing-noise-std 2.0
--sglang-use-adaptive-noise
--sglang-use-partial-safe-noisytopk
--sglang-partial-safe-num-fixed 2
--sglang-partial-safe-num-candidates 32
```

## Critical Hyperparameters & Tuning Advice
- Replay expert IDs, not weights. One routing variant at a time.
- Validated on Qwen3-MoE SGLang non-DeePEP. Add `--eval-disable-routing-noise` for deterministic eval.
- Noise scale: `beta_min + (beta_max - beta_min) * (1 - normalized_entropy)`.
