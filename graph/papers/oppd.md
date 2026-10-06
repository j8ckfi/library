---
id: paper:oppd
type: paper
title: "Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution"
authors:
  - Erfan Baghaei Potraghloo
  - Seyedarmin Azizi
  - Arya Fayyazi
  - Saeid Shokoufa
  - Mehdi Kamal
  - Souvik Kundu
  - Massoud Pedram
year: 2026
month: 10
arxiv_id: "2610.06804"
url: "https://arxiv.org/abs/2610.06804"
methods:
  - method:oppd
cites:
  - paper:opd
  - paper:grpo
tags:
  - post-training
  - distillation
  - opd
  - oppd
---

# Sharpen Without Search: On-Policy Distillation of Sequence-Level Power Distribution

## Abstract Summary
Sequence-level power distributions sharpen a frozen teacher's answers but usually need many scored candidates. OPPD trains the student with an SMC sampler whose weights come from that frozen power distribution, then maximum-likelihood on the same weights so one generation matches power sampling. MATH500 +23.0 and GSM8K +27.3 vs untrained at the same temperature; one generation scores +2.4 / +3.5 vs published 64-candidate power sampling. Vs GRPO from the same checkpoint/budget: +3.8 / +4.0 / +5.4 on MATH500 / GSM8K / AIME with no reference answers; OPPD after GRPO adds up to 9.3. HumanEval +5.3 after math-only training. Code: https://github.com/ArminAzizi98/OPPD. Beside OPD.

## Key Contributions
1. **SMC on a frozen teacher's sequence-level power distribution**, then weighted MLE.
2. **One generation** recovers most of multi-candidate power sampling.
3. **Complementary to GRPO**: OPPD after GRPO adds up to 9.3 points.

## Empirical Highlights
- MATH500 +23.0 / GSM8K +27.3 vs untrained at the same temperature.
- +2.4 / +3.5 vs published 64-candidate power sampling; 94% of the untrained 16-candidate gain.
- Vs GRPO: +3.8 / +4.0 / +5.4 on MATH500 / GSM8K / AIME; after GRPO up to +9.3.
- HumanEval +5.3 after math-only training. Already-RL'd model: +4.4 MATH500 where lowering temperature gives nothing.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06804`
- Code: `https://github.com/ArminAzizi98/OPPD` (`code_status: released`; HTTP 200 as of 2026-10-06).
