---
id: method:flash-opd
type: method
title: "Flash-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "Flash-OPD shortens OPD rollouts; OPD remains the matching default"
    use_instead: "method:opd"
  - when: "sparse OPD token keep-mask, not rollout horizon"
    reason: "Sparse OPD drops tokens; Flash-OPD stops trajectories early"
    use_instead: "method:sparse-opd-supervision"
assumptions:
  - White-box teacher OPD where teacher–student compatibility can be checked during generation.
  - "Code: Onedean/Flash-OPD (`code_status: released`)."
last_reviewed: "2026-10-06"
papers:
  - paper:flash-opd
recipes:
  - recipe:flash-opd
claims:
  - benchmark: "Flash-OPD vs standard OPD wall-clock / accuracy"
    metric: "speedup vs OPD at maintained or improved accuracy"
    value: "2.2×–7.5× vs standard OPD"
    baseline: "standard full-horizon OPD"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06105"
    notes: "Does not retarget OPD."
tags:
  - post-training
  - distillation
  - flash-opd
  - active
---

# Flash-OPD

## Method Overview
Flash-OPD stops each student trajectory when low teacher–student compatibility events first accumulate past a threshold. Verification points are scheduled from the recent event rate; the stop itself uses the exact cumulative count so estimation errors cannot cut a trajectory early.

## When to Use
- Frozen-teacher OPD where long rollouts dominate cost and reliable prefixes vary by trajectory.

## When NOT to Use
- Default matching OPD → `method:opd`. Token keep-mask → `method:sparse-opd-supervision`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:opd` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: released** Onedean/Flash-OPD as of 2026-10-06.
- Do not use the event-rate schedule as the stop rule; that is only the next-check time.
