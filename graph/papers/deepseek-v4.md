---
id: paper:deepseek-v4
type: paper
title: "DeepSeek-V4: Frontier Sparse Mixture-of-Experts Architecture"
authors:
  - "DeepSeek-AI Team"
year: 2026
month: 6
arxiv_id: "2606.19348"
url: "https://arxiv.org/abs/2606.19348"
methods:
  - method:deepseek-v4
cites:
  - paper:deepseek-v3
  - paper:mhc
tags:
  - architecture
  - moe
  - frontier
  - deepseek-v4
---

# DeepSeek-V4: Frontier Sparse Mixture-of-Experts Architecture

## Abstract Summary
DeepSeek-V4 establishes the mid-2026 state-of-the-art sparse Mixture-of-Experts architecture, advancing Multi-Head Latent Attention (MLA), dynamic multi-token prediction heads, and ultra-fine-grained expert routing.

## Key Contributions
1. **Next-Generation MLA**: Enhanced latent projection compression for reduced KV cache footprint.
2. **Fine-Grained Expert Routing**: Expanded expert pool with auxiliary-loss-free load balancing.
3. **Multi-Token Prediction**: Speculative multi-token generation heads integrated natively into pretraining.
4. **Manifold-Constrained Hyper-Connections (mHC)**: Residual stream expanded to \(n \times d\) (\(n=4\)) with Sinkhorn doubly-stochastic projection preserving identity mapping.

## Open Source Repository
- Implementation: `none found`
