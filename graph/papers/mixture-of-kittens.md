---
id: paper:mixture-of-kittens
type: paper
title: "Mixture-of-Kittens: MoE Megakernel for NVL72s"
authors:
  - "Stuart H. Sul"
  - "Nash Brown"
  - "Henry Wildermuth"
  - "William Lin"
  - "Federico Cassano"
year: 2026
month: 8
arxiv_id: ""
url: "https://github.com/cursor/mixture-of-kittens"
methods:
  - method:mixture-of-kittens
cites:
  - paper:deepseek-v4
  - paper:kimi-k3
  - paper:nemotron-3-super-latentmoe
tags:
  - systems
  - megakernel
  - moe
  - nvl72
  - blackwell
  - mok
  - mixture-of-kittens
---

# Mixture-of-Kittens: MoE Megakernel for NVL72s

## Overview
Mixture-of-Kittens (MoK) is Cursor Research's open-source (Apache-2.0) deterministic Mixture-of-Experts training megakernel designed from first principles for NVIDIA Blackwell NVL72 rack architectures (GB200/GB300 NVL72). It powers production training of Composer at Cursor.

## Key Technical Contributions
1. **Full Megakernel Fusion**: Fuses MoE token dispatch, expert FFN computation (SwiGLU GEMM), and token combine into a single deterministic GPU kernel.
2. **Pull Dispatch & Push Combine**: Employs fine-grained asynchronous networking reducing signaling latency from 103 µs to 18 µs.
3. **Ring Token Buffer**: Eliminates CPU-GPU synchronization entirely while ensuring zero dropped tokens under severe routing load imbalance.
4. **Dual Precision Paths**: Full support for both BF16 and micro-scaled FP8 (MXFP8) across forward and backward passes.
5. **Hardware Floor**: Targets NVIDIA Blackwell SM100/SM103 hardware using ThunderKittens tile abstractions, PyTorch 2.10+, and CUDA 13+.

## Empirical Highlights
- **Megakernel Speedup vs Fastest Public Baseline (DeepEP / TransformerEngine / HybridEP / NCCL)**:
  - MXFP8: Up to 2.37x forward, 1.78x backward.
  - BF16: Up to 1.92x forward, 1.58x backward.
- **Production End-to-End Scale**:
  - 512-GPU training throughput increased from 760.9 to 1070.2 tokens/sec/GPU (1.41x) compared to the prior DeepEP stack.

## Resources
- GitHub Repository: https://github.com/cursor/mixture-of-kittens
- Technical Blog Post: https://cursor.com/blog/mixture-of-kittens
