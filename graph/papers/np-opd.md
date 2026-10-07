---
id: paper:np-opd
type: paper
title: "On-Policy Distillation with Negative-Policy Rollouts"
authors:
  - Jaehui Hwang
  - Dongyoon Han
  - Sangdoo Yun
  - Byeongho Heo
year: 2026
month: 10
arxiv_id: "2610.07874"
url: "https://arxiv.org/abs/2610.07874"
methods:
  - method:np-opd
cites:
  - paper:opd
  - paper:nsd
tags:
  - post-training
  - distillation
  - opd
  - np-opd
---

# On-Policy Distillation with Negative-Policy Rollouts

## Abstract Summary
Teacher OPD starves when teacher/student overlap is low. NP-OPD adds negative-policy rollouts that complement teacher supervision instead of imitating a privileged gold trace. Combines with ExOPD / OPD2. Related to NSD (diverge from a negative condition) but stays on the frozen-teacher OPD shelf. Code naver-ai/np-opd. Does not replace OPD or NSD.

## Key Contributions
1. **Negative-policy rollouts** fill the overlap gap in teacher OPD.
2. **Composes** with ExOPD / OPD2.
3. **Released code** at naver-ai/np-opd.

## Empirical Highlights
- Helps when teacher/student overlap is low; do not treat as a CISPO Pass@1 bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07874`
- Code: `https://github.com/naver-ai/np-opd` (`code_status: released`; HTTP 200 as of 2026-10-07).
