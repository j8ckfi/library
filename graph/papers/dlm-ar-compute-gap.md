---
id: paper:dlm-ar-compute-gap
type: paper
title: Revisiting the 16x Pretraining Compute Gap between Diffusion and Autoregressive Language Models
authors:
- Guanghan Wang
- Bing He
- Zhan Shi
- Benoit Dumoulin
- Hanqing Lu
- Volodymyr Kuleshov
year: 2026
month: 10
arxiv_id: '2610.17590'
url: https://arxiv.org/abs/2610.17590
methods:
- method:semicat
- method:a2d
cites:
- paper:semicat
- paper:a2d
tags:
- diffusion
- pretraining
- scaling-laws
- gotcha
---

# Revisiting the 16x Pretraining Compute Gap

## Abstract Summary
Caution/evidence paper. Older ~16× DLM-vs-AR compute claims used ELBO / full-sequence protocols. Under exact likelihood in decoding order, block diffusion, and encoder-decoder (~1,700 models), the gap shrinks. Discrete MDM/BD3LM/E2D2 vs AR — not SemiCat continuous pretrain, but attached as a gotcha on that task and on AR-delta recycle. Does not retarget SemiCat or A2D.

## Key Contributions
1. Protocol gap: ELBO MDM 17.8× vs exact-likelihood DUEL 12.8×.
2. Architecture shrinks further: E2D2 b=32/8/4 → 7.8× / 4.6× / 3.0×; BD3LM 32/16/8/4 → 9.6 / 7.8 / 5.9 / 4.1 DUEL.
3. ~1,700-model sweep. Project guanghanwang.com/dlm-scaling.

## Empirical Highlights
- ELBO MDM 17.8×; DUEL 12.8×.
- E2D2 b=32 7.8×, b=8 4.6×, b=4 3.0×.
- BD3LM 32/16/8/4 = 9.6/7.8/5.9/4.1 DUEL.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.17590`
- Project: `https://guanghanwang.com/dlm-scaling`
- Code: `none found` (`code_status: none`).
