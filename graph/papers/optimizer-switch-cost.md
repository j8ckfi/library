---
id: paper:optimizer-switch-cost
type: paper
title: 'The Ephemeral Cost of Switching Optimizers Across LLM Training Stages'
authors:
- 'Xinyu Zhao'
- 'Davis Wertheimer'
- 'Ashutosh Sharma'
- 'Rameswar Panda'
- 'Paul Pu Liang'
year: 2026
month: 10
arxiv_id: '2610.22650'
url: https://arxiv.org/abs/2610.22650
methods:
- method:muon2
cites:
- paper:muon2
tags:
- optimizer
- muon2
- gotcha
---

# The Ephemeral Cost of Switching Optimizers Across LLM Training Stages

## Abstract Summary
1.2B Llama-3 models pretrained from scratch while interpolating AdamW and Muon across pretrain, continued pretrain, and SFT. Final performance is largely explained by the independent effects of the pretraining and post-training optimizers; downstream gains from switching to Muon for SFT persist even after full AdamW pretraining. Little evidence of a meaningful optimizer-mismatch penalty.

## Key Contributions
1. Systematic AdamW↔Muon interpolations at 1.2B across pretrain / CPT / SFT.
2. Mismatch cost is small relative to each stage's optimizer choice.
3. NeurIPS 2026 Transitioning from Pre-Training to Post-Training workshop.

## Empirical Highlights
- Do not treat optimizer-stage matching as a hard constraint on a Muon2 pretrain plus AdamW SFT (or the reverse) without measuring it.
- Does not retarget Muon2.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22650`
- Code: `none found` (`code_status: none`).
