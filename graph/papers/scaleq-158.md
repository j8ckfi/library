---
id: paper:scaleq-158
type: paper
title: "ScaleQ-1.58: Post-Training Ternary Quantization for Existing SOTA LLMs"
authors:
  - "Intel China AI Team"
year: 2026
month: 8
arxiv_id: "2608.01078"
url: "https://arxiv.org/abs/2608.01078"
methods:
  - method:scaleq-158
cites:
  - paper:bitnet-b158
tags:
  - quantization
  - ptq
  - ternary
  - scaleq-158
---

# ScaleQ-1.58: Post-Training Ternary Quantization for Existing SOTA LLMs

## Abstract Summary
ScaleQ-1.58 achieves post-training ternarization of existing pre-trained foundation LLMs into ternary {-1, 0, +1} representations using scale-compensated integer optimization without requiring pretraining from scratch.

## Key Contributions
1. **Post-Training Ternarization**: Converts existing FP16 checkpoints into ternary 1.58-bit models with minimal calibration tokens.
2. **Inference Acceleration**: Directly compatible with addition-only BitLinear kernels.

## Open Source Repository
- Implementation: `https://github.com/IntelChina-AI/BitTern` (claimed)
