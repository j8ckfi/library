---
id: method:qwen38-next
type: method
title: "Qwen3.8-Next (GDN Hybrid, Gated Residual, QSA, Muon+AdamW Split)"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense pretrain optimizer"
    reason: "Qwen3.8-Next is a coupled production architecture recipe; Muon2 + KL-SOAP remains the 7B optimizer default"
    use_instead: "method:muon2"
  - when: "choosing the frontier MoE architecture template"
    reason: "DeepSeek-V4 + Kimi-K3 remain the MoE architecture co-defaults; this is an adjacent Qwen-style hybrid residual design"
    use_instead: "method:deepseek-v4"
  - when: "NVL72 fused MoE dispatch megakernel"
    reason: "Mixture-of-Kittens is the NVL72 systems first-hop"
    use_instead: "method:mixture-of-kittens"
assumptions:
  - "Production Qwen3.8-Flash-Next is 125B-A6B MoE plus 51B host-memory n-gram tables."
  - "Muon on 2D linear maps; AdamW on embeddings, n-gram tables, lm_head, MoE router, and GR low-rank projections. Split fused parameters before orthogonalization. Newton-Schulz 8 steps."
  - "Public code is FlashQLA GDN kernels only, not a full pretrain stack."
last_reviewed: "2026-09-01"
papers:
  - paper:qwen38-next
recipes:
  - recipe:qwen38-next
claims:
  - benchmark: "Fourteen pretraining benches vs Qwen3.7-Plus 397B-A17B"
    metric: "win count / max trail"
    value: "leads 8 of 14; trails remainder by at most 2.6 points"
    baseline: "Qwen3.7-Plus-Base 397B-A17B at 1/3 activated params, 1/3 tokens, ~1/9 FLOPs"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30320"
    notes: "Abstract and Table 11. MMLU-Pro 73.23 vs 70.90; MATH 72.78 vs 74.38; MultiPL-E 79.09 vs 81.68."
  - benchmark: "25B-A3B nine-bench architecture ablation"
    metric: "unweighted average"
    value: 53.81
    baseline: "Full attention 49.87 / SWA hybrid 51.15"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30320"
    notes: "Table 1. One full-attention layer in every four; remaining layers GDN."
  - benchmark: "FlashQLA GDN kernel vs FLA Triton"
    metric: "forward / backward speedup"
    value: "2-3x forward, ~2x backward"
    baseline: "FLA Triton"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.30320"
    notes: "QSA at 1M context: 7.6x prefill and 4.9x decode vs dense attention at kernel level."
tags:
  - architecture
  - moe
  - hybrid-attention
  - gated-residual
  - qwen38-next
---

# Qwen3.8-Next (GDN Hybrid, Gated Residual, QSA, Muon+AdamW Split)

## Method Overview
Coupled architecture + optimizer recipe from Qwen3.8-Flash-Next:

1. **Token mixing**: layer-wise hybrid of Gated DeltaNet and global attention, one full-attention layer in every four. At continued pretraining, full-attention layers become Qwen Sparse Attention (QSA): micro-block compressed indexer, token budget $K=2048$, compression $r=4$.
2. **Gated Residual (GR)**: residual stream widened to four branches, read through an elementwise gate. Adjacent to mHC/AttnRes (widened residual), not a replacement of mHC's Sinkhorn constraint.
3. **Off-accelerator n-gram embeddings**: 51B parameters prefetched from host memory at layer 2.
4. **Optimizer split**: Muon on 2D linear maps; AdamW on embeddings, n-gram, `lm_head`, MoE router, GR low-rank. Split fused parameters before orthogonalization. Newton–Schulz 8 steps. No batch-size warmup (warmup costs 18.8% more optimizer steps for no gain).

## When to Use
- Reference for Qwen-style hybrid residual / GDN+QSA production pretrain design.
- FlashQLA when training or serving GDN layers on Hopper/Blackwell.

## When NOT to Use
- ~7B dense optimizer default remains `method:muon2` (+ KL-SOAP).
- Frontier MoE architecture default remains `method:deepseek-v4` + `method:kimi-k3`.
- NVL72 megakernel remains `method:mixture-of-kittens`.

## Relation to Existing SOTA
- Active architecture + systems shelf next to mHC / AttnRes / Gated DeltaNet 2. Does **not** overwrite Muon2 or DeepSeek-V4/Kimi-K3.
- Muon here is the production split used by Qwen, not a new optimizer node.

## Gotchas & Failure Modes
- Loss and downstream can disagree (n-gram vocab lowers loss while accuracy saturates).
- Dropping RoPE on full-attention layers looks free in pretrain then causes endless generation after post-train.
- Restricting GR to the two highest-gated branches is almost free in pretrain loss then degrades with further training.
- FlashQLA needs SM90+ and CUDA 12.8 / PyTorch 2.8.
