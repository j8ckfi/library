---
id: paper:elr
type: paper
title: 'One Model to Loop Them All: Elastic Latent Recurrence for Language Models'
authors:
- Faisal Ladhak
- Shantanu Acharya
- Santiago Akle Serano
- Simeng Sun
- Boris Ginsburg
- Krishna C Puvvada
year: 2026
month: 10
arxiv_id: '2610.12582'
url: https://arxiv.org/abs/2610.12582
methods:
- method:elr
cites:
- paper:looped-models-done-right
- paper:smelt
tags:
- pretraining
- looped-lm
- elr
- nvidia
---

# One Model to Loop Them All: Elastic Latent Recurrence for Language Models

## Abstract Summary
NVIDIA Elastic Latent Recurrence (ELR) trains one looped LM that can run at variable loop counts. A gated state update uses a learned step size. Mixed loop counts share one optimizer update. Loop-index and remaining-budget conditioning keep the shared weights coherent. Mixed-depth ELR can be added late in pretraining. MoE reuses first-loop routes. KV is last-loop-only. First hop on `task:elastic-depth-looped-lm`. No public code.

## Key Contributions
1. Gated latent recurrence with a learned step size and mixed loop counts per optimizer step.
2. Loop-index / remaining-budget conditioning so one weight set serves 1–K loops.
3. Late mixed-depth conversion, MoE first-loop route reuse (~11.7% faster), last-loop-only KV.

## Empirical Highlights
- 4B dense 10-task avg: 1 loop −0.52 vs matched baseline; 4 loops +7.25.
- 30B-A3B MoE: 1 loop +1.04; 4 loops +4.75.
- Koi-4B AAII ~18 at 1 loop (Qwen3.5-4B class) and 29 at 4 loops.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12582`
- Code: `none found` (`code_status: none`).
