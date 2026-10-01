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
last_reviewed: "2026-10-01"
papers:
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

## When to Use
- When distilling capabilities from multiple specialized expert teachers (e.g., math, code, conversational instruction, tool-use) into a single compact generalist student.
- When standard multi-task or multi-teacher distillation leads to catastrophic forgetting or degradation on concise response tasks.

## Relation to Existing SOTA
- Co-exists with `method:opd` under `task:student-distillation`: `method:opd` is the single-teacher default; `method:open-mopd` is the multi-teacher distillation default as of 2026-08-28. Privileged same-model gold-solution OPSD is `method:vista` and does not replace Open-MOPD.
- Multi-stage agent continual learning (`method:aclarena`) uses MMOPD as a paper baseline, not a retarget of this method. Label-routed MOPD of SWE category experts is `method:category-aware-swe-experts`.
- Token-level ExpertAlign routing over unlabeled multi-teacher pools is `method:mopd-router` (`arXiv:2609.30837`). Active plug-in. Does **not** replace Open-MOPD as the gap-aware budget / token-share balancing default.
- Joint-outcome multi-task gating of one teacher is `method:duoopd` (`arXiv:2609.33711`). Does **not** replace Open-MOPD.
