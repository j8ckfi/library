---
id: method:open-mopd
type: method
title: "Open-MOPD (Multi-Teacher On-Policy Distillation)"
category: "distillation"
status: sota
sota_for:
  - task:student-distillation
supersedes: []
do_not_use_for:
  - when: "multi-teacher OPD via teacher-minus-base logit shifts rather than endpoint copy"
    reason: "Open-MOPD remains token-share / gap-aware budget; Delta-MOPD transfers the post-training shift"
    use_instead: "method:delta-mopd"
  - when: "MOPD vs tuned off-policy SFT/Soft-KD after matching training design (GPU-hour confound)"
    reason: "Open-MOPD remains the multi-teacher matching default; rethink-mopd is a caveat that a tuned off-policy baseline may suffice"
    use_instead: "paper:rethink-mopd"
  - when: "token-level ExpertAlign routing over unlabeled multi-teacher pools (no domain labels, no separate router train)"
    reason: "Open-MOPD is gap-aware token-share balancing on labeled domain teachers; MOPD-Router routes the full pool per token"
    use_instead: "method:mopd-router"
  - when: "domain-feedback-scale calibration of labeled MOPD advantages (not token-share budget)"
    reason: "Open-MOPD allocates budget from remaining gap / token share; DN-MOPD rescales log-ratio spread on labeled routing"
    use_instead: "method:dn-mopd"
  - when: "multi-teacher OPD subspace protection / task cycling (not token-share)"
    reason: "Open-MOPD is the multi-teacher default; PMOPD projects interfering update directions"
    use_instead: "method:pmopd"
  - when: "multi-task OPD and teacher can be wrong on some tasks"
    reason: "Open-MOPD is token-share / gap-aware budget across teachers; DuoOPD gates one teacher's weights by joint outcomes"
    use_instead: "method:duoopd"
  - when: "slow (EMA) / fast student coupling in multi-teacher OPD for capability preservation"
    reason: "Open-MOPD remains token-share / gap-aware budget; SF-MOPD is slow/fast EMA coupling"
    use_instead: "method:sf-mopd"
  - when: "lexicographic priority multi-objective OPD from reward-specialist teachers"
    reason: "Open-MOPD remains token-share / gap-aware budget; LMOPD is lexicographic priority among specialists"
    use_instead: "method:lmopd"
  - when: "representation-level (hidden-state) multi-teacher OPD"
    reason: "Open-MOPD remains token-share / gap-aware budget; Latent-MOPD matches specialist hidden states"
    use_instead: "method:latent-mopd"
last_reviewed: "2026-10-09"
papers:
  - paper:delta-mopd
  - paper:open-mopd
recipes:
  - recipe:open-mopd
claims:
  - benchmark: "Multi-Teacher Capability Integration (SmolLM3-3B Benchmark)"
    metric: "oracle ensemble headroom recovery"
    value: "Increases headroom recovery from 35.6% to 83.4% in a single generalist student"
    baseline: "Standard M-OPD / Domain-routed Oracle Ensemble"
    date: "2026-08-28"
    verified: true
    notes: "Token-share balancing, gap-aware dynamic budget allocation, and student reward refresh eliminate multi-teacher imbalance."
tags:
  - post-training
  - distillation
  - multi-teacher
  - open-mopd
  - sota
---

# Open-MOPD (Multi-Teacher On-Policy Distillation)

## Method Overview
Open-MOPD is the state-of-the-art framework for consolidating multiple domain-specialized teachers into a single student policy without capability collapse:
1. **Token-Share Balancing**: Normalizes token-level loss contributions per domain to prevent verbose chain-of-thought teachers (e.g. math/code) from monopolizing gradients over concise instruction-following tasks.
2. **Gap-Aware Dynamic Budget Allocation**: Monitors the capability gap between student and respective domain teachers in real time, dynamically steering the optimization budget to lagging domains.
3. **Student Reward Refresh**: Refreshes on-policy student references and teacher advantage scores to eliminate staleness during asynchronous policy updates.

## Training-design caveat
`paper:rethink-mopd` (`arXiv:2610.04272`) finds that after matching training design and hyperparameters, tuned SFT / Soft-KD can approach MOPD while MOPD costs 14.8–23.1× SFT GPU-hours. That does **not** retarget this card's 83.4% bake-off. Try a tuned off-policy baseline before paying on-policy multi-teacher cost.

## When to Use
- When distilling capabilities from multiple specialized expert teachers (e.g., math, code, conversational instruction, tool-use) into a single compact generalist student.
- When standard multi-task or multi-teacher distillation leads to catastrophic forgetting or degradation on concise response tasks.

## Relation to Existing SOTA
- Co-exists with `method:opd` under `task:student-distillation`: `method:opd` is the single-teacher default; `method:open-mopd` is the multi-teacher distillation default as of 2026-08-28. Privileged same-model gold-solution OPSD is `method:vista` and does not replace Open-MOPD.
- Multi-stage agent continual learning (`method:aclarena`) uses MMOPD as a paper baseline, not a retarget of this method. Label-routed MOPD of SWE category experts is `method:category-aware-swe-experts`.
- Token-level ExpertAlign routing over unlabeled multi-teacher pools is `method:mopd-router` (`arXiv:2609.30837`). Active plug-in. Does **not** replace Open-MOPD as the gap-aware budget / token-share balancing default.
- Joint-outcome multi-task gating of one teacher is `method:duoopd` (`arXiv:2609.33711`). Does **not** replace Open-MOPD.
