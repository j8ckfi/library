---
id: method:lmopd
type: method
title: "LMOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the multi-teacher student-distillation default"
    reason: "Open-MOPD remains token-share / gap-aware budget; LMOPD is lexicographic priority among reward specialists"
    use_instead: "method:open-mopd"
  - when: "multi-reward GRPO aggregation (Pearson covariance or density-aware)"
    reason: "CorrGRPO/DARA scalarize or density-correct GRPO rewards; LMOPD is priority-ordered teacher OPD"
    use_instead: "task:multi-reward-rlvr"
  - when: "single-turn dense math/code Pass@1 RLVR (one verifier reward)"
    reason: "CISPO remains Pass@1; LMOPD is multi-objective distillation"
    use_instead: "method:cispo"
assumptions:
  - "Reward-specialist teachers exist with an explicit priority order (correctness before quality before conciseness in the paper). 30B-A3B MoE eval."
  - "GDPO / Rewarded Soup are paper baselines, not library methods."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:lmopd
recipes:
  - recipe:lmopd
claims:
  - benchmark: "30B-A3B two-expert retained gain (pass@1 / RQ / Conc)"
    metric: "retained-gain average"
    value: "84.4%"
    baseline: "Rewarded Soup (2:1) 67.1% / GDPO(25,1,1) 18.9%"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02359"
    notes: "pass@1 102.9% / RQ 103.3% / Conc 46.9%. Raw pass@1 0.7450 vs base 0.7109 vs capability expert 0.7440."
  - benchmark: "30B-A3B four-expert retained-gain average"
    metric: "retained-gain average"
    value: "39.6%"
    baseline: "gated RLVR 34.4%"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02359"
    notes: "pass@1 90.6 / RQ-corr 88.6. Not an Open-MOPD 83.4% bake-off retarget."
tags:
  - post-training
  - distillation
  - multi-teacher
  - multi-objective
  - lmopd
  - active
---

# LMOPD

## Method Overview
Scalarized multi-reward RL can buy conciseness by spending correctness. LMOPD keeps a stack of reward-specialist teachers and a priority order. For each student rollout it gates the first deficient objective, then locally projects that specialist's centered log-policy correction so it cannot oppose higher-priority specialists. This is multi-teacher OPD, not CorrGRPO / DARA aggregation.

## When to Use
- Reward-specialist teachers with an asymmetric priority (correctness must not lose to conciseness).

## When NOT to Use
- Multi-teacher default → `method:open-mopd`. Scalarized multi-reward GRPO → `task:multi-reward-rlvr`. Single-reward Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside Open-MOPD (`sota_for: []`). Mention on `task:multi-reward-rlvr` as the priority-ordered OPD alternative. Does **not** enter either `current_sota`. Does **not** replace Open-MOPD, CorrGRPO, or DARA.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Random routing in the paper collapses retained gain (6.8%). The gate is the method.
- GDPO is not a library node.
