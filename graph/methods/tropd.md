---
id: method:tropd
type: method
title: "TrOPD (Trust-Region On-Policy Distillation)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "maximal-coupling-routed teacher supervision / TRB accept-correction routing"
    reason: "TrOPD bounds OPD update divergence; SAKI realizes a KL-constrained behavior policy via maximal coupling"
    use_instead: "method:saki"
  - when: "adapting the OPD teacher on student prefixes / off-policy teacher, not frozen-teacher OPD"
    reason: "TrOPD gates a frozen teacher; SCOUT RL-adapts the teacher on student prefixes"
    use_instead: "method:scout"
last_reviewed: "2026-10-01"
papers:
  - paper:tropd
recipes:
  - recipe:tropd
claims:
  - benchmark: "Student Distillation Benchmarks"
    metric: "training stability"
    value: "Trust-region bounded teacher matching"
    baseline: "Standard OPD"
    date: "2026-08-26"
    verified: true
    notes: "Bounds student policy divergence across distillation steps."
tags:
  - post-training
  - distillation
  - tropd
---

# TrOPD (Trust-Region On-Policy Distillation)

## Method Overview
TrOPD incorporates trust-region bounds into on-policy distillation, stabilizing student training trajectories when exploring low-probability teacher branches.

## When to Use
- Distilling long conversational or agentic reasoning traces where student exploration can destabilize.
