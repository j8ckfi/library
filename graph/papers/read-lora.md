---
id: paper:read-lora
type: paper
title: "New LoRA Skills Should Read but Never Write"
authors:
  - "Zeyan Li"
  - "Panqi Yang"
  - "Qirong Guo"
  - "Shengda Zhuo"
  - "Siyuan Qiu"
  - "Hu Xu"
  - "Chun Li"
  - "Jianfeng Xu"
year: 2026
month: 9
arxiv_id: "2609.31600"
url: "https://arxiv.org/abs/2609.31600"
methods:
  - method:read-lora
cites:
  - paper:lr-matters-lora
tags:
  - peft
  - lora
  - composition
  - read-lora
---

# New LoRA Skills Should Read but Never Write

## Abstract Summary
Independently trained LoRA adapters are cheap to produce and hard to compose. Weight-space merges interfere; joint retraining is expensive; routers keep extra objects at serve time. READ (Read-only Expansion of Adapter Deltas) fixes two freedoms a lone adapter never exposes: gauge in the \(BA\) factorization, and the direction of cross-skill coupling. Each adapter is rewritten into a balanced canonical form that preserves \(\Delta W\) exactly. A coupling matrix \(G\) joins stacked factors; at each append only the new skill's **read** row is trained, and writes into old output subspaces are hard-zeroed. The product folds into the base weights, so serving has no router and no residual LoRA path. Llama-3.2-3B sequential add: SuperGLUE 0.783 vs 0.605 strongest published same-adapter baseline; Domain 0.887 vs 0.846. Qwen3-4B GLUE 0.838 vs 0.775. Shared 32-lineage mean lift +0.073 (95% CI +0.047–+0.101). SJTU / XJTU / HKUST(GZ) / Jinan University. No public code in the paper as of 2026-09-28.

## Key Contributions
1. **Canonical factors**: thin QR of \(B\) and \(A^\top\), then SVD of \(R_B R_A^\top\), balanced \(\Sigma^{1/2}\) so both factors share the same metric and \(B^c A^c = BA\).
2. **Read-only coupling**: new skill may read old input subspaces; \(G_{\le k,k+1}=0\) so it cannot write old output subspaces. Old blocks and all factors stay frozen.
3. **Fold-in serve**: \(\Delta W=B_{\mathrm{stack}} G A_{\mathrm{stack}}\) is a single rank-\(kr\) update, precomputed into \(W_0\).

## Empirical Highlights
- Llama-3.2-3B terminal suite vs per-lineage strongest foldable alternative: SuperGLUE 0.783 vs 0.605; Domain 0.887 vs 0.846; GLUE 0.823 vs 0.631.
- Qwen3-4B: GLUE 0.838 vs 0.775; SuperGLUE 0.797 vs 0.709; Domain 0.852 vs 0.794.
- 32 lineages (2 models × 4 suites × 2 seeds × 2 orders): mean +0.073, 24 wins; all 8 losses on BBH.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.31600`
- Code: none in the paper as of 2026-09-28 (`recipe:read-lora` `code_status: none`).
