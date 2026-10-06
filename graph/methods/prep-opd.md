---
id: method:prep-opd
type: method
title: "Prep-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "Prep-OPD prepares the teacher, then runs ordinary OPD"
    use_instead: "method:opd"
  - when: "interleaved teacher RL during student OPD (off-policy teacher)"
    reason: "SCOUT updates the teacher every f OPD steps; Prep-OPD prepares then freezes"
    use_instead: "method:scout"
assumptions:
  - "You can RL-train the teacher on frozen student prefixes before distillation. Paper: Qwen3-4B-Instruct-2507 teacher, Qwen3-0.6B/1.7B students, eight math benches."
  - "No public code as of 2026-10-06 (`code_status: none`). Relay-OPD is a paper baseline, not a library method."
last_reviewed: "2026-10-06"
papers:
  - paper:prep-opd
recipes:
  - recipe:prep-opd
claims:
  - benchmark: "Qwen3-4B-Instruct-2507 → Qwen3-1.7B, eight math benchmarks vs OPD / Relay-OPD"
    metric: "average accuracy lift"
    value: "+8.28 vs OPD / +2.30 vs Relay-OPD"
    baseline: "standard OPD / Relay-OPD (paper baseline, not a library method)"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04950"
    notes: "Prepare-then-freeze, not SCOUT's interleaved teacher RL. Does not retarget OPD or SCOUT."
tags:
  - post-training
  - distillation
  - prep-opd
  - active
---

# Prep-OPD

## Method Overview
Prep-OPD first RL-trains the teacher to continue fixed student prefixes under a final-answer reward, then freezes that teacher and runs ordinary trajectory OPD. Complementary to SCOUT, which keeps adapting the teacher during student OPD.

## When to Use
- Frozen-teacher OPD where the teacher is weak on student prefixes, and you can afford a separate teacher-RL stage before distillation.

## When NOT to Use
- Default OPD → `method:opd`. Interleaved teacher RL during OPD → `method:scout`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:scout` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD or SCOUT.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Relay-OPD is a paper baseline, not a library method.
- Problem-start teacher RL is not Prep-OPD.
