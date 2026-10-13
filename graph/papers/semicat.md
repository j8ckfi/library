---
id: paper:semicat
type: paper
title: On the Design Space of Continuous Diffusion Language Models
authors:
- Oscar Davis
- Daan Roos
- Alice Bizeul
- Amitis Shidani
- Victor Turrisi
- Louis Béthune
- Pierre Ablin
- Marco Cuturi
year: 2026
month: 10
arxiv_id: '2610.13834'
url: https://arxiv.org/abs/2610.13834
methods:
- method:semicat
cites:
- paper:a2d
- paper:canvasanneal
tags:
- pretraining
- diffusion-lm
- semicat
---

# On the Design Space of Continuous Diffusion Language Models

## Abstract Summary
Maps the continuous diffusion LM design space. Self-conditioning closes a train/inference mismatch. DoubleCat is a two-level interpolant that gets the same match without an extra forward. SemiCat adds discrete reveals. SemiCat reaches 49.94% TinyGSM (matches discrete diffusion). At 1.7B it beats discrete diffusion on 4/6 likelihood evals. First hop on `task:continuous-diffusion-lm-pretrain`. No public code.

## Key Contributions
1. Self-conditioning as the train/inference mismatch fix for continuous diffusion LMs.
2. DoubleCat two-level interpolant: same match without an extra forward.
3. SemiCat adds discrete reveals on top of DoubleCat.

## Empirical Highlights
- DoubleCat TinyGSM 4.42%→16.00%.
- SemiCat TinyGSM 32.90% / 49.94% with a tuned sampler (matches discrete diffusion).
- 1.7B beats discrete diffusion on 4/6 likelihood evals.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13834`
- Code: `none found` (`code_status: none`).
