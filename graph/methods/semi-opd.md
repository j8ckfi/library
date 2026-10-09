---
id: method:semi-opd
type: method
title: "Semi-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "teacher and student already share high output-token overlap and live prefixes help"
    reason: "Semi-OPD is for misaligned pairs; live OPD remains matching when overlap is high"
    use_instead: "method:opd"
  - when: "sample-efficient / off-policy OPD (Huber quadratic matching + replay)"
    reason: "LSPD is a loss/replay change; Semi-OPD only freezes the rollout policy at init"
    use_instead: "method:lspd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Same reverse-KL OPD loss. Only the rollout policy is frozen at the initial student."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:semi-opd
recipes:
  - recipe:semi-opd
claims:
  - benchmark: "17 teacher-student pairs, 1.5B-235B"
    metric: "pairs where Semi-OPD beats live OPD; max accuracy / speedup"
    value: "14/17 win; up to +13.6% accuracy and 11.4x training speedup"
    baseline: "live on-policy OPD"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.11291"
    notes: "Live OPD remains better when initial output-token overlap is high. Does not retarget OPD." 
tags:
  - post-training
  - distillation
  - opd
  - semi-opd
  - offline-rollout
  - active
---

# Semi-OPD

## Method Overview
Generate rollouts once from the initial student. Distill with the usual reverse-KL teacher signal on those frozen prefixes. Skip regenerating on-policy traces every step unless overlap with the teacher is already high.

## When to Use
- Teacher/student overlap is low or unknown and live OPD rollouts dominate the wall-clock.

## When NOT to Use
- High initial overlap → `method:opd`. Huber off-policy matching → `method:lspd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- Frozen init rollouts go stale if the student moves far; re-check overlap.
