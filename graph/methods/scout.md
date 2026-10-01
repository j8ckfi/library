---
id: method:scout
type: method
title: "SCOUT"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "single-teacher matching distillation from a strong frozen teacher (default OPD)"
    reason: "OPD remains student-rollout reverse-KL matching; SCOUT additionally adapts the teacher on student prefixes"
    use_instead: "method:opd"
  - when: "trust-region bounds on student–teacher divergence without teacher adaptation"
    reason: "TrOPD gates the student update; SCOUT trains the teacher with RL on student prefixes"
    use_instead: "method:tropd"
  - when: "maximal-coupling-routed teacher supervision / TRB accept-correction routing"
    reason: "SAKI routes student-side accept/correction events for a frozen teacher; SCOUT is the complementary teacher-side fix"
    use_instead: "method:saki"
  - when: "privileged same-model gold-solution OPSD (teacher already sees the reference)"
    reason: "VISTA adapts a privileged same-size teacher on verified rollouts; SCOUT is frozen-teacher OPD off-policy-teacher RL"
    use_instead: "method:vista"
assumptions:
  - "White-box teacher that can be updated with outcome RL on student prefixes. Paper: Qwen3 teacher–student pairs, math plus a code transfer setting."
  - "Teacher update interval f OPD steps; student-prefix ratio rises linearly. Gradients on teacher-generated continuation tokens only."
  - "No public GitHub as of 2026-10-01."
last_reviewed: "2026-10-01"
papers:
  - paper:scout
recipes:
  - recipe:scout
claims:
  - benchmark: "Math reasoning, three teacher–student pairs vs frozen-teacher OPD"
    metric: "average accuracy lift"
    value: "+1.2 to +2.6"
    baseline: "Standard OPD with a frozen teacher"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.38360"
    notes: "Student-prefix conditioning is load-bearing vs extra teacher RL without it. Not an OPD retarget."
  - benchmark: "Code generation vs frozen-teacher OPD"
    metric: "average score"
    value: "59.7"
    baseline: "Frozen-teacher OPD 56.6 (+3.1)"
    date: "2026-10-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.38360"
    notes: "Transfer beyond math. Complementary to TrOPD / SAKI student-side gating."
tags:
  - post-training
  - distillation
  - on-policy
  - scout
  - active
---

# SCOUT

## Method Overview
OPD trajectories are on-policy for the student and off-policy for the teacher. SCOUT (Student-COnditioned Updates of the Teacher) keeps the student reverse-KL OPD update and, every \(f\) OPD steps, splits a student trajectory at prefix ratio \(k\), samples teacher continuations from that prefix, and updates the teacher with group-relative outcome RL on continuation tokens only. The adapted teacher is synchronized for later OPD steps. Prefix ratio rises over training. Complementary to TrOPD / SAKI, which gate a *frozen* teacher.

## When to Use
- Frozen-teacher OPD where long student prefixes make teacher continuations unreliable, and you can afford periodic teacher RL.

## When NOT to Use
- Default frozen-teacher matching → `method:opd`. Student-side trust-region → `method:tropd`. Coupling-routed teacher modes → `method:saki`. Privileged gold-solution OPSD → `method:vista`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:opd` and `method:tropd`. Does **not** enter `current_sota`. Does **not** replace OPD, TrOPD, SAKI, or VISTA.

## Gotchas & Failure Modes
- No public code as of 2026-10-01.
- Teacher RL *without* student-prefix conditioning is not SCOUT and underperforms in the paper.
- Updating the teacher too often is expensive; too rarely leaves the off-policy gap in place.
- Same-family distilled pairs (Qwen3-8B/1.7B) needed extra teacher task training in the paper notes.
