---
id: paper:qwen38-next
type: paper
title: "On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability"
authors:
  - "Qwen Team"
year: 2026
month: 8
arxiv_id: "2608.30320"
url: "https://arxiv.org/abs/2608.30320"
methods:
  - method:qwen38-next
cites:
  - paper:muon2
  - paper:gated-deltanet-2
  - paper:mhc
  - paper:deepseek-v4
tags:
  - architecture
  - moe
  - hybrid-attention
  - gated-residual
  - qwen38-next
---

# On the Design of Qwen3.8-Next Architecture: Evaluation, Efficiency, and Training Stability

## Abstract Summary
Qwen3.8-Flash-Next is a 125B-A6B sparse MoE plus 51B n-gram embedding tables held off the accelerator. On fourteen pretraining benchmarks it leads the 397B-A17B predecessor on eight and trails the rest by at most 2.6 points, at 1/3 the activated parameters, 1/3 the training tokens, and roughly 1/9 the training FLOPs. Token mixing is a GDN–attention hybrid (one full-attention layer in every four), later replaced at CPT by Qwen Sparse Attention (QSA). Residuals use a four-branch Gated Residual (GR). Optimizer is Muon on 2D linear maps and AdamW on embeddings, n-gram tables, lm_head, MoE router, and GR low-rank projections. New LR/batch scaling removes batch warmup.

## Key Contributions
1. **GDN hybrid + QSA CPT**: three GDN layers + one full attention per block of four; FlashQLA kernels 2–3× forward and ~2× backward vs FLA Triton. At 1M context, QSA is 7.6× faster than dense attention in prefill and 4.9× in decode at the kernel level.
2. **Gated Residual**: four-branch residual with elementwise read gate; a stability contributor vs Qwen3.5, adjacent to mHC/AttnRes rather than a replacement.
3. **Coupled optimizer recipe**: Muon+AdamW split, fused parameters split before orthogonalization, Newton–Schulz 8 steps, no batch-size warmup (warmup costs 18.8% more optimizer steps).

## Empirical Highlights
- 25B-A3B ablation avg over nine benches: GDN hybrid 53.81 vs SWA hybrid 51.15 vs full attention 49.87.
- Qwen3.8-Flash-Next-Base vs Qwen3.7-Plus-Base (397B-A17B): leads 8/14, trails remainder by at most 2.6. MMLU 90.36 vs 90.43; MMLU-Pro 73.23 vs 70.90; SuperGPQA 51.36 vs 48.42; MATH 72.78 vs 74.38; MultiPL-E 79.09 vs 81.68.
- Full-scale training reported without a loss spike and without qk-clip / SwiGLU-clip.

## Open Source Repository & Resources
- FlashQLA kernels: `https://github.com/QwenLM/FlashQLA` (`pip install flash-qla`)
- Full model training stack is not released with the paper; document the coupled recipe, do not treat FlashQLA as a complete pretrain codebase.
