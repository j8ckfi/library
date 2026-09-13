---
id: paper:smelt
type: paper
title: "SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers"
authors:
  - "Shaowen Wang"
  - "Ge Zhang"
  - "Kairong Luo"
  - "Yuhao Wu"
  - "Shaofan Liu"
  - "Jiaheng Liu"
  - "Wenhao Huang"
  - "Shen Yan"
  - "Jian Li"
year: 2026
month: 9
arxiv_id: "2609.01343"
url: "https://arxiv.org/abs/2609.01343"
methods:
  - method:smelt
cites: []
tags:
  - architecture
  - moe
  - looped-transformer
  - smelt
  - scaling-laws
---

# SMELT: Scaling Laws for Compute-Matched MoE Looped Transformers

## Abstract Summary
Looped Transformers raise effective depth by repeating a shared block, but most comparisons hold parameter count fixed and let FLOPs and KV grow. SMELT (Sparse MoE Transformer, middle layers Loop Twice) loops the middle half of MoE layers twice while matching an unlooped Baseline on per-token FLOPs, total non-embedding parameters, and KV cache (narrow the hidden size, raise expert count, adjust GQA/head size; scale looped residuals by \(1/2\)). Separate Chinchilla-style surfaces on a sparse-grid ladder up to 54B non-embedding parameters show SMELT's loss dropping faster with compute, saving 6.8–18.0% of training FLOPs on the compute-optimal frontier. Downstream gains exceed what validation loss predicts, are largest on Code, and grow with sample length and in-context examples. A second visit reduces the attention sink and redirects mass toward content tokens.

## Key Contributions
1. **Three-budget matching** on MoE: FLOPs, non-embedding params, and KV simultaneously.
2. **Locked recipe**: middle 50% span, two visits, larger effective depth-to-width than the Baseline.
3. **Scaling laws** on a 100M–1.6B active / up to 54B non-embedding ladder with compute-equivalent sparsity \(S \approx 85\%, 95\%, 97\%\).
4. **Mechanistic note**: second visit amplifies residual updates and reduces attention-sink mass.

## Empirical Highlights
- CE Gain 6.8–10.0% at \(10^{20}\) FLOPs and 14.7–18.0% at \(10^{21}\) FLOPs across the three sparse levels (cell-bootstrap intervals in the paper).
- DCLM Completion wins 96/96 matched pairs; DCLM Core 83/96; MMLU 29/30 pairs with Baseline \(\geq 10\) pp above chance.
- Affiliations: Tsinghua, ByteDance Seed, M-A-P, TokenWave.AI.

## Open Source Repository & Resources
- arXiv HTML/PDF: `https://arxiv.org/abs/2609.01343`
- No official training code as of 2026-09-12 (`recipe:smelt` `repo_url: none found`). Unrelated GitHub projects share the SMELT name.
