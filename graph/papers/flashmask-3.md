---
id: paper:flashmask-3
type: paper
title: 'FlashMask-3: Efficient and Expressive Mask-Aware Distributed Attention'
authors:
- Guoxia Wang
- Qianyue He
- Siming Wu
- Haoyang Xie
- Qiwen Bao
- Jinle Zeng
- Jiabin Yang
- Tian Wu
- Dianhai Yu
year: 2026
month: 10
arxiv_id: '2610.17901'
url: https://arxiv.org/abs/2610.17901
methods:
- method:flashmask-3
cites: []
tags:
- training-systems
- attention
---

# FlashMask-3

## Abstract Summary
Long-context training couples structured masks with multi-node context parallelism. FlashMask-3 adds a Hopper mask-aware kernel on FlashAttention-3's TMA/WGMMA pipeline plus zero-communication mask localization, a sparsity-aware load balancer, and mask-driven communication pruning.

## Key Contributions
1. Clip-shift-max localization of column-wise sparse masks under context parallel.
2. Three-role warp-specialized Hopper kernel.
3. End-to-end 118B-A14B MoE at 128K on 128 H100.

## Empirical Highlights
- Single H100 12 masks 4K-128K: +45-141% TFLOPs vs FlashMask.
- CP 4-32: 1.80-3.71x vs Megatron-Core CP ring.
- 118B-A14B e2e +7.3-11.0% throughput.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.17901`
- Code: `https://github.com/PaddlePaddle/FlashMask` (`code_status: released`). NeurIPS 2026.

