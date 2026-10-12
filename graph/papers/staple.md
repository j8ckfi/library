---
id: paper:staple
type: paper
title: 'STAPLE: Static Sparse Upcycling of Pretrained Checkpoints via Embedding Modules'
authors:
- Ranajoy Sadhukhan
- Euijin Hong
- Sheng Cao
- Zechun Liu
- Shuowei Jin
- Sha Li
- Changlong Yu
- Xin Liu
- Qin Lu
- Zhenyu Shi
- Priyanka Nigam
- Beidi Chen
year: 2026
month: 10
arxiv_id: '2610.12599'
url: https://arxiv.org/abs/2610.12599
methods:
- method:staple
cites:
- paper:maskerade
- paper:deepseek-v4
tags:
- pretraining
- sparsity
- upcycling
- staple
---

# STAPLE: Static Sparse Upcycling of Pretrained Checkpoints via Embedding Modules

## Abstract Summary
STEM replaces FFN up-projections with token-indexed embeddings and trains poorly as a drop-in. STAPLE keeps the pretrained FFN and adds embeddings as a residual pathway. Host-offload keeps train/gen throughput within 3%/1.5% of dense while caching ~5% hottest embeddings on GPU. Beats STEM, Engram-style, and an MoE upcycle on average with faster decode.

## Key Contributions
1. Residual static sparse memory instead of replacing FFN up-projections.
2. Host-offload with ~5% GPU cache; near-dense throughput.
3. OLMo-2 1B/7B quality lifts vs continued dense and vs MoE upcycle at 2× decode.

## Empirical Highlights
- See `method:staple` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12599`
- Code: `none found` (`code_status: none`).
