---
id: paper:aqlora
type: paper
title: "AQLoRA: Accurate Quantized Low-Rank Adaptation for Large Language Models"
authors:
  - "Romyull Islam et al."
year: 2026
month: 8
arxiv_id: "2608.23816"
url: "https://arxiv.org/abs/2608.23816"
methods:
  - method:aqlora-q
cites:
  - paper:qlora
tags:
  - peft
  - quantization
  - 4bit
  - aqlora
---

# AQLoRA: Accurate Quantized Low-Rank Adaptation for Large Language Models

## Abstract Summary
AQLoRA-Q introduces high-accuracy 4-bit quantized low-rank adaptation with optimized non-uniform quantization grids and accelerated dequantization kernels, superseding standard QLoRA in throughput and accuracy retention.

## Key Contributions
1. **Accurate 4-Bit Grid**: Minimizes residual quantization distortion on sensitive projection layers.
2. **Speed & Recipe SOTA**: Superior wall-clock training speed and downstream task accuracy on 4-bit GPU stacks.

## Open Source Repository
- Implementation: `https://github.com/Romyull-Islam/AQLoRA`
