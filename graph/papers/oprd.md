---
id: paper:oprd
type: paper
title: "Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation"
authors:
  - "Youngrok Park"
  - "Sangmin Bae"
  - "Hojung Jung"
  - "Jongwoo Ko"
  - "Yunseon Choi"
  - "Young Jin Kim"
  - "Pashmina Cameron"
  - "Aaron Courville"
  - "Se-Young Yun"
year: 2026
month: 9
arxiv_id: "2609.08798"
url: "https://arxiv.org/abs/2609.08798"
methods:
  - method:oprd
cites:
  - paper:opd
  - paper:grpo
  - paper:w2s-opd
tags:
  - post-training
  - distillation
  - weak-to-strong
  - oprd
---

# Eliciting Weak-to-Strong Generalization with On-Policy Reverse Distillation

## Abstract Summary
Weak-to-strong generalization asks whether a stronger student can learn from a weaker supervisor and surpass it. Conventional distillation treats the weak teacher as an optimization target and can impose its ceiling. On-Policy Reverse Distillation (OPRD) evaluates the teacher's policy shift relative to its reference on student rollouts and amplifies the component of the student's verifier-driven policy gradient along that direction. Only verifier-supported updates are rescaled, so the stationary points of policy optimization are preserved while learning can continue past the teacher. On successive 4B→8B transfer, multi-teacher consolidation, and even strong-to-weak distillation, OPRD beats GRPO, OPD, KDRL, MOPD, and the paper's W2S-OPD reimplementation, with fewer student updates to GRPO's end-of-training level.

## Key Contributions
1. **Reverse distillation**: teacher shift as a direction for the student's verifier gradient, not a matching target.
2. **Verifier gate**: amplify only reward-supported components; stationary points of RLVR stay.
3. **Works across capacity order**: weak-to-strong, multi-teacher, and strong-to-weak.
4. **Distinct from W2S-OPD**: Table 3 compares OPRD 60.81 vs W2S-OPD 49.22 on the paper's 4B→8B mix.

## Empirical Highlights
- 4B→8B math Mean@16 avg: OPRD 51.91 vs KDRL 43.99 vs OPD 39.44 vs GRPO 39.38 vs teacher 38.66 (Table 1). AIME'24 66.92 vs KDRL 53.46.
- Reasoning Gym Pass@1 avg: OPRD 55.18 vs KDRL 44.38 vs OPD 42.83.
- Multi-teacher 4×4B→8B: OPRD 58.77 vs Mix-RL 47.68 vs specialist mean 44.65 (Table 2).
- Strong-to-weak avg: OPRD 41.49 vs KDRL 29.52 vs OPD 25.00.

## Open Source Repository & Resources
- Code: `https://github.com/raymin0223/on_policy_reverse_distillation`
