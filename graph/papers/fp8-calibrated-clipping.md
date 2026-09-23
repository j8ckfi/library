---
id: paper:fp8-calibrated-clipping
type: paper
title: "Towards Full Pipeline FP8 Reinforcement Learning for LLMs"
authors:
  - "Fanchao Chen"
  - "Ziheng Jiang"
  - "Ziyun Wei"
  - "Zheng Zhong"
  - "Du Li"
  - "Chi Zhang"
  - "Haibin Lin"
  - "Shivaram Venkataraman"
year: 2026
month: 9
arxiv_id: "2609.22870"
url: "https://arxiv.org/abs/2609.22870"
methods:
  - method:fp8-calibrated-clipping
cites:
  - paper:dapo
  - paper:grpo
  - paper:miles
tags:
  - systems
  - post-training
  - fp8
  - clipping
---

# Towards Full Pipeline FP8 Reinforcement Learning for LLMs

## Abstract Summary
FP8 can accelerate RL, but a full rollout-and-train FP8 pipeline still entropy-surges. Train–inference mismatch corrections such as TIS are not enough: compounded FP8 quantization noise distorts the importance ratio, pushing negative-advantage tokens outside the trust region and zeroing their gradients, so pathological outputs are not penalized. Calibrated Clipping matches the FP8 lower-bound clipping quantile to a BF16 reference and rebalances the upper bound so the positive-to-negative update ratio is restored. Across GRPO and DAPO, 8B–32B models, and several FP8 scaling granularities in VeRL + vLLM + TorchAO, the method eliminates entropy surges and restores BF16-level quality, with up to about 1.5× BF16 training throughput.

## Key Contributions
1. **Failure mode**: compounded FP8 noise over-clips negative-advantage tokens via a distorted IS ratio.
2. **Calibrated Clipping**: match the FP8 lower-bound clip quantile to BF16, then rebalance the upper bound.
3. **Systems evidence**: GRPO/DAPO, 8B–32B, tensorwise/blockwise FP8, VeRL + vLLM + TorchAO (ByteDance Seed / UW–Madison).

## Empirical Highlights
- Eliminates mid-training entropy surges and garbled outputs that persist under TIS-style mismatch correction.
- Restores BF16-level quality. Tensorwise FP8 typically up to ~1.5× BF16 training throughput; blockwise ~10–20%.
- Sequence lengths 4K / 8K / 16K on 8B, 14B, and 32B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.22870`
- No public standalone GitHub as of 2026-09-23 (`recipe:fp8-calibrated-clipping` `code_status: none`). Implemented in VeRL experiments; FlashRL FP8 rollout patch is used in the paper. Do not invent a Miles replacement.
