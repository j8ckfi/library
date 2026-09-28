---
id: paper:mopd-router
type: paper
title: "MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation"
authors:
  - "Tianze Xu"
  - "Yanzhao Zheng"
  - "Zhentao Zhang"
  - "Yuanqiang Yu"
  - "Chao Ma"
  - "Jihuai Zhu"
  - "Lelun Wu"
  - "Lyumanshan Ye"
  - "Pengfei Liu"
  - "Baohua Dong"
  - "Hangcheng Zhu"
  - "Ruohui Huang"
  - "Gang Yu"
year: 2026
month: 9
arxiv_id: "2609.30837"
url: "https://arxiv.org/abs/2609.30837"
methods:
  - method:mopd-router
cites:
  - paper:open-mopd
  - paper:opd
tags:
  - post-training
  - distillation
  - multi-teacher
  - on-policy
  - mopd-router
---

# MOPD-Router: Rethinking Teacher Routing in Multi-Teacher On-Policy Distillation

## Abstract Summary
Standard multi-teacher on-policy distillation hard-routes each prompt to one domain-matched teacher for the entire rollout. That needs prompt-level domain labels and leaves complementary signals from the rest of the pool unused. MOPD-Router instead weights the full teacher pool at every token, with no domain labels and no separately trained router. ExpertAlign scores whether a teacher's local correction of the student expresses that teacher's post-training specialty (cosine of the teacher–base expertise vector with the teacher–student teaching vector on the student's top-k support). On unlabeled mixtures ExpertAlign lifts overall score +5.88 / +12.3% vs Mean aggregation; on labeled data it beats standard MOPD by +3.95 / +7.8% without using the available domain labels. Strong-to-weak and same-size. SJTU / GAIR / Alibaba. Code released at `https://github.com/TURLEing/MOPD-Router`.

## Key Contributions
1. **Token-level routing interface**: replace one-teacher-per-prompt assignment with plug-in metrics that select and weight per-teacher sampled-token OPD advantages at each position.
2. **ExpertAlign**: keep a teacher only when its teaching direction aligns with the specialization it acquired relative to the shared pre-RL base; cosine-weight the retained set (uniform ablation is weaker).
3. **Label-free and labeled bake-off**: ExpertAlign is strongest in all four settings (unlabeled / labeled × 1.7B / 4B). Entropy (confidence) is a weak router; Novelty is a useful but weaker reference metric.

## Empirical Highlights
- Unlabeled 60K mix, Qwen3-4B student, overall Avg. of nine math/code/IF metrics: ExpertAlign 53.76 vs Mean 47.88 (+5.88, +12.3%) vs Standard MOPD 48.76 vs Open-MOPD 49.41.
- Labeled MOPD mix, same student: ExpertAlign 54.58 vs Standard MOPD 50.63 (+3.95, +7.8%) vs Open-MOPD 52.37, without using domain labels.
- Strong-to-weak Qwen3-1.7B unlabeled: 38.58 vs Mean 34.49; labeled: 40.19 vs Standard MOPD 37.52.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.30837`
- Code: `https://github.com/TURLEing/MOPD-Router` (`verl/`, `benchmarks/`, `run.sh`; `code_status: released`).
