---
id: paper:saki
type: paper
title: "SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation"
authors:
  - "Miteto Wei"
  - "Xiaohan Wang"
  - "Zehao Chen"
  - "Jiajun Chai"
  - "Sichao Liu"
  - "Li Wang"
  - "Haoyuan Xu"
  - "Zhaoyu Hu"
  - "Wei Lin"
  - "Guojun Yin"
year: 2026
month: 9
arxiv_id: "2609.36601"
url: "https://arxiv.org/abs/2609.36601"
methods:
  - method:saki
cites:
  - paper:opd
  - paper:tropd
tags:
  - post-training
  - distillation
  - on-policy
  - saki
---

# SAKI: Maximal-Coupling-Routed Teacher Supervision for On-Policy Distillation

## Abstract Summary
Teacher-guided OPD (TRB) interpolates a behavior policy \(q_t\) inside a student-centered KL trust region, but still applies the same reverse-KL objective at every prefix. SAKI (Supervision Allocation with KL-constrained Interpolation) realizes \(q_t\) by maximal coupling with the student: accepted student proposals keep sampled reverse-KL; correction events switch to NLL on the teacher's top-1 token. Correction probability is exactly \(\mathrm{TV}(p_t,q_t)\le\sqrt{\epsilon/2}\) under the trust region. An engine-resident speculative verifier preserves the exact-\(q\) trajectory and coupling semantics at 4.22× matched-workload throughput. Improves Mean@8 / Pass@8 vs matched teacher-guided OPD on 1.7B and 0.6B students. Meituan / KTH. No public GitHub as of 2026-09-30.

## Key Contributions
1. **Endogenous router**: reuse accept/correction events; not equal-budget random or TV-weighted placement.
2. **Minimal intervention**: maximal coupling; residual token continues the rollout, teacher mode trains the correction position.
3. **Exact-\(q\) speculative verifier**: first-rejection commit/rollback; 4.22× vs external-loop teacher calls.

## Empirical Highlights
- 1.7B Mean@8 / Pass@8 29.0 / 47.5 vs TRB 27.9 / 44.6. 0.6B 18.4 / 35.6 vs 17.2 / 33.6. Seven math benches.
- Correction-triggered routing beats count-matched random and TV-weighted placement. Fixed-prefix analysis: larger gaps vs random at higher initial student–teacher disagreement.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.36601`
- Code: none found as of 2026-09-30 (`code_status: none`).
