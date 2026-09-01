---
id: paper:gradcodes
type: paper
title: "Fine-Tuning Low-Bit Models with Gradient in Quantized Code Space"
authors:
  - "Shiguang Wu"
  - "Zhouchen Lin"
  - "Quanming Yao"
year: 2026
month: 8
arxiv_id: "2608.30908"
url: "https://arxiv.org/abs/2608.30908"
methods:
  - method:gradcodes
cites:
  - paper:qlora
  - paper:aqlora
tags:
  - quantization
  - peft
  - low-bit
  - gradcodes
---

# Fine-Tuning Low-Bit Models with Gradient in Quantized Code Space

## Abstract Summary
Fully low-bit fine-tuning keeps targeted weights in NF4, INT4, or MXFP4 at every accepted checkpoint, with only datatype-permitted scales and no high-precision residual adapter. Continuous methods are distorted by STE or a post-quantize gap; discrete search is faithful but slow. GradCodeS builds a code-coordinate surrogate gradient by codebook continuation (effective-step correction for group scales and non-uniform gaps), uses it to center a candidate set, and accepts an update only by realized deployed loss. Every selected iterate is a valid low-bit checkpoint.

## Key Contributions
1. **Code-space surrogate gradient** $\nabla_Z L=\nabla_{\widehat W}L\odot D$, where $D$ is the descent-aligned local codebook gap times group scale.
2. **Guide–sample–evaluate–select**: one backward pass to propose, then loss-based selection over deployable candidates.
3. **Datatype-agnostic**: NF4, INT4, MXFP4; full-matrix or LoRA code parameterization.

## Empirical Highlights
- Llama-3.2-1B-Instruct GSM8K fully 4-bit: GradCodeS Full 41.63 vs PV-Tuning 36.92 vs QLoRA-4Merge 24.79 vs Base-4 25.85. QLoRA mixed adapter is a different deployment regime; merging it back to 4-bit loses 13.4 points in the paper's GSM8K example.
- Qwen3-0.6B GSM8K fully 4-bit: GradCodeS LoRA 45.72 vs PV-Tuning 38.70 vs 16-bit SFT 39.65.
- MASSIVE EM Llama-3.2-1B: GradCodeS Full 69.17 vs PV-Tuning 64.50.
- Datatype sweep on Llama-3.2-1B GSM8K: NF4 41.6, MXFP4 41.1, INT4 38.9 vs PV-Tuning 36.9.

## Open Source Repository & Resources
- Code: `https://github.com/ovo67/GradCodes`
