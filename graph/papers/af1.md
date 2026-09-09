---
id: paper:af1
type: paper
title: "All for 1-Bit: Towards Genuine 1-Bit Post-Training Quantization for LLMs"
authors:
  - "Zhixiong Zhao"
  - "Zukang Xu"
  - "Guangyu Sun"
  - "Lifeng Liu"
  - "Dawei Yang"
year: 2026
month: 9
arxiv_id: "2609.06161"
url: "https://arxiv.org/abs/2609.06161"
methods:
  - method:af1
cites: []
tags:
  - quantization
  - 1bit
  - ptq
  - af1
---

# All for 1-Bit: Towards Genuine 1-Bit Post-Training Quantization for LLMs

## Abstract Summary
Existing binarization PTQ methods usually exceed a nominal 1-bit storage target because of hidden overhead. AF1 is a genuine 1.0-BPW PTQ recipe: Null-space-Aware Binary Factorization (NABF) with Hessian-aware surrogate reparameterization, null-space-aware factorization, and scale-only global reconstruction; plus Hierarchical Shapley Allocation (HiSA) for structural capacity. On LLaMA, Qwen, and Gemma, AF1 beats prior binarization PTQ in perplexity and zero-shot accuracy, with ~2.5× inference speedup vs BF16 and >90% memory reduction. EMNLP 2026 Main. Beside Sparse-BitNet (native 1.58-bit *pretrain*), not a pretrain default.

## Key Contributions
1. **Strict 1.0-BPW PTQ** without hidden overhead.
2. **NABF** reconstruction + **HiSA** capacity allocation.

## Empirical Highlights
- Beats existing binarization PTQ on LLaMA / Qwen / Gemma PPL and zero-shot.
- ~2.5× inference vs BF16; >90% memory reduction.

## Open Source Repository & Resources
- Claimed code: `https://github.com/Kishon-zzx/AF1` (404 at ingest time 2026-09-09; keep the paper URL).
