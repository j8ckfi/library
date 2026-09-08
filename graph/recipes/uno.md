---
id: recipe:uno
type: recipe
title: "Uno Diffusion Distillation Recipe"
method: method:uno
task: task:diffusion-augmented-ar
target_hardware: "1x NVIDIA H200 (paper throughput); 1x GPU with grad-accum 16 for Qwen3-8B adapter train (global batch 128)"
framework: "PyTorch 2.11 / Nano-vLLM / DeepSpeed ZeRO-2"
repo_url: "https://github.com/ifm-ai/uno"
pip_dependencies:
  - "torch==2.11.0"
  - "flash-attn==2.8.3"
tags:
  - recipe
  - uno
  - diffusion
  - speculative-decoding
---

# Uno Diffusion Distillation Recipe

## Hardware & Environment Setup
- Official code: `https://github.com/ifm-ai/uno`. Project: `https://s-sahoo.com/uno/`.
- Install: Python 3.10, `torch==2.11.0` (cu128), FlashAttention-2 wheel, `pip install -e '.[eval,train]'`. Tree verification additionally needs FlashAttention-3 (`flash-attention/hopper`).
- Checkpoints: `IFM/K2-Horizon-7B-Uno`, `IFM/K2-Horizon-0.9B-Uno`, `s-sahoo/uno-qwen3-8B`.
- Host pretrain optimizer stays Muon2 for ~7B. Host Pass@1 RLVR stays CISPO. This recipe is Diffusion Distillation + $\Psi$-Spec decode.

## Quickstart Implementation

```python
# Linear sampler (system throughput): B=4
# Tree sampler (batch-1): B=16, K=32, V=32 (paper Table 1 TPF 2)
# Public inference wrapper:
#   bash examples/uno_qwen3_8B/run_inference.sh --prompt "..."
# Tree:
#   ATTENTION_BACKEND=fa3 bash examples/uno_qwen3_8B/run_inference.sh \
#     --diffusion-block-size 16 --tree-candidate-top-k 32 --tree-verify-size 60

def psi_spec_linear_accept(ar_verify_prefix_ok: list[bool]) -> int:
    """Accept the longest AR-verified prefix; sample a replacement at the first failure."""
    for i, ok in enumerate(ar_verify_prefix_ok):
        if not ok:
            return i
    return len(ar_verify_prefix_ok)
```

Train adapters (single GPU, global batch 128 via accum):

```bash
python -m training.prepare_openthoughts --output /data/openthoughts-uno-4095 --num-proc 32
python -m training.train \
  --dataset-path /data/openthoughts-uno-4095 \
  --curriculum training/configs/uno_3epoch_curriculum.yaml \
  --deepspeed training/configs/deepspeed_zero2.json \
  --per-device-batch-size 8 \
  --gradient-accumulation-steps 16 \
  --learning-rate 1e-5 \
  --warmup-steps 562 \
  --lora-target all \
  --lora-rank 128 \
  --lora-alpha 2048 \
  --ce-alpha 0 \
  --kl-beta 0 \
  --tv-gamma 1
```

## Critical Hyperparameters & Tuning Advice
- System throughput: Linear $B=4$. Per-request: tree $(16,32,32)$. Larger $V$ can lose tok/s to verify cost.
- Keep AR weights as the quality path. Do not train a d-LLM substitute if lossless AR law is the point.
- Does not replace DiffusionOPSD / Self-OPD (image/flow post-train) or CISPO / Muon2.
