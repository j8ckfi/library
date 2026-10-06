---
id: method:oppd
type: method
title: "OPPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher token-level matching algorithm"
    reason: "OPPD trains against a sequence-level power distribution via SMC, not reverse-KL OPD"
    use_instead: "method:opd"
  - when: "labeled dense Pass@1 RLVR"
    reason: "CISPO remains Pass@1; OPPD uses no reference answers in the GRPO comparison"
    use_instead: "method:cispo"
assumptions:
  - "Frozen teacher whose sequence-level power distribution you can weight. Paper: math benches plus a HumanEval transfer."
  - "Code: ArminAzizi98/OPPD (`code_status: released`)."
last_reviewed: "2026-10-06"
papers:
  - paper:oppd
recipes:
  - recipe:oppd
claims:
  - benchmark: "MATH500 / GSM8K single-generation vs untrained (same temperature)"
    metric: "accuracy lift"
    value: "+23.0 MATH500 / +27.3 GSM8K"
    baseline: "untrained model at the same temperature"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06804"
    notes: "Vs GRPO +3.8 / +4.0 / +5.4 on MATH500 / GSM8K / AIME. Does not retarget OPD or CISPO."
tags:
  - post-training
  - distillation
  - oppd
  - active
---

# OPPD

## Method Overview
OPPD (on-policy power distillation) runs SMC where the student proposes and a frozen teacher's sequence-level power distribution weights complete answers, then does weighted MLE so one generation matches that sharpened distribution.

## When to Use
- You want power-sampling quality in one generation from a frozen teacher, without verifier labels.

## When NOT to Use
- Token-level reverse-KL matching → `method:opd`. Verifiable Pass@1 RLVR → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:opd` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: released** ArminAzizi98/OPPD as of 2026-10-06.
- Complementary to GRPO, not a CISPO retarget.
- One loss coefficient moves the absorbed exponent between 1.19 and 2.02 vs 1.14 for ordinary OPD.
