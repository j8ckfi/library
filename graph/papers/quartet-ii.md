---
id: paper:quartet-ii
type: paper
title: "Quartet-II: Hardware-Aware NVFP4 Training for Deep Networks"
authors:
  - "IST-DASLab Authors"
year: 2026
month: 1
arxiv_id: "2601.22813"
url: "https://arxiv.org/abs/2601.22813"
methods:
  - method:quartet-ii
cites: []
tags:
  - quantization
  - fp4
  - nvfp4
  - hardware-training
  - quartet-ii
---

# Quartet-II: Hardware-Aware NVFP4 Training for Deep Networks

## Abstract Summary
Quartet-II details end-to-end 4-bit floating-point (NVFP4) training protocols for large language models, leveraging NVIDIA Blackwell tensor core architectures with stochastic rounding and scale tracking.

## Key Contributions
1. **NVFP4 Training Pipeline**: Forward and backward passes executed natively in FP4 without loss of gradient dynamics.
2. **Hardware Speedup**: Up to 3.5x training throughput speedup over standard BF16 implementations.

## Open Source Repository
- Implementation: `https://github.com/IST-DASLab/Quartet-II`
