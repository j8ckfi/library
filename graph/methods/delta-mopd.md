---
id: method:delta-mopd
type: method
title: "Delta-MOPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the multi-teacher distillation algorithm"
    reason: "Delta-MOPD changes the transferred object (shift vs endpoint); Open-MOPD remains token-share / gap-aware budget"
    use_instead: "method:open-mopd"
  - when: "single-teacher matching distillation"
    reason: "Delta-MOPD is multi-teacher composition; OPD remains matching"
    use_instead: "method:opd"
  - when: "lexicographic priority among reward-specialist teachers"
    reason: "LMOPD is priority order; Delta-MOPD is a shift vs endpoint target"
    use_instead: "method:lmopd"
assumptions:
  - "Each teacher has a known base checkpoint. Student init is the re-anchor."
  - "No official GitHub as of 2026-10-09." 
last_reviewed: "2026-10-09"
papers:
  - paper:delta-mopd
recipes:
  - recipe:delta-mopd
claims:
  - benchmark: "Three-teacher common-domain composition vs endpoint MOPD"
    metric: "Math / five-benchmark lift vs endpoint composition"
    value: "+4.11 Math and +1.95 five-benchmark; two-teacher matches endpoint; phased routing order gap 10.50 to 6.42"
    baseline: "endpoint-policy MOPD (copy of each teacher)"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.10460"
    notes: "Paper Open-MOPD numbers are not the library 83.4% bake-off. Does not retarget Open-MOPD." 
tags:
  - post-training
  - distillation
  - mopd
  - delta-mopd
  - active
---

# Delta-MOPD

## Method Overview
For each teacher, take logits(teacher) − logits(teacher-base) and add them to the student's frozen initialization logits. Distill that shift instead of the teacher's endpoint distribution. Teacher selection (common-domain mix vs routed specialist) stays whatever you already use.

## When to Use
- Multi-teacher OPD where teachers do not share a base with the student, so endpoint copy imports the wrong inherited prior.

## When NOT to Use
- Token-share / gap-aware default → `method:open-mopd`. Single teacher → `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Open-MOPD or OPD. Paper Open-MOPD numbers are not the library 83.4% bake-off.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-09.
- Needs each teacher's base checkpoint. Cross-tokenizer needs an overlap projection (paper appendix).
