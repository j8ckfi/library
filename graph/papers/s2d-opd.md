---
id: paper:s2d-opd
type: paper
title: "Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD"
authors:
  - "Yibo Zhao"
  - "Zixuan Yang"
  - "Yunshi Lan"
  - "Xiang Li"
year: 2026
month: 9
arxiv_id: "2609.29142"
url: "https://arxiv.org/abs/2609.29142"
methods:
  - method:s2d-opd
cites:
  - paper:opd
  - paper:oprd
  - paper:w2s-opd
  - paper:ier-opd
  - paper:cal-opd
tags:
  - post-training
  - distillation
  - on-policy
  - weak-to-strong
  - s2d-opd
---

# Not Every Token Is Worth Distilling: Selective Supervision for Direct-OPD

## Abstract Summary
Direct-OPD transfers an RL-induced policy shift from a small post-RL teacher to a larger student by rewarding every student-sampled state with the teacher–reference token log-ratio. That log-ratio is mass-invariant: it can stay large while teacher–reference JSD (and both KL directions) vanish with the probability mass on the student's candidates. S²D-OPD ranks student states by teacher–reference JSD over the student's top-K plus a residual token, and keeps only the top ~10% per response. Across two teacher pairs and four students (1.7B–8B), it improves held-out Acc over dense Direct-OPD in 7/8 settings and ties the eighth (+0.95 mean; 95% CI 0.40–1.54), with no extra forward passes. Low-JSD bins trained alone can collapse the student. East China Normal University. Review-anonymous code.

## Key Contributions
1. **Mass mismatch**: exact construction where Direct-OPD reward/gradient stay fixed while JSD/KL → 0 with candidate mass \(\epsilon\).
2. **JSD keep-mask**: per-response top-\(\rho\) (\(\rho=0.1\)) on compressed teacher–ref JSD; Direct-OPD update unchanged on kept states.
3. **Bin evidence**: top JSD bin beats random 10%; lowest bins drop below init and can collapse.

## Empirical Highlights
- Eight settings, Avg@32, checkpoint on AIME24/25, held-out AIME26+HMMT: mean 47.31 vs dense Direct-OPD 46.36 (+0.95).
- Qwen3-1.7B + JustRL pair Test Avg. 37.6 vs Direct-OPD 36.4; QuestA pair 38.1 vs 36.5.
- Qwen3-8B + QuestA: 57.1 vs Direct-OPD 55.4 (Direct-OPD was +0.0 vs init).
- R1-Distill-7B + JustRL: tie at 40.5 Test Avg.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.29142`
- Code: `https://anonymous.4open.science/r/S2D-OPD-8868` (review-anonymous as of 2026-09-25; `recipe:s2d-opd` `code_status: announced`).
