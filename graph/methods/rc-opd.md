---
id: method:rc-opd
type: method
title: "RC-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD with a matched VISTA-protocol bake-off"
    reason: "VISTA remains this task's first hop; RC-OPD repairs the student's own failed reasoning"
    use_instead: "method:vista"
  - when: "privileged OPSD gains collapse at scale; verified on-policy scaffolds"
    reason: "OASIS changes the scaffold/context; RC-OPD diagnoses the student's error stage"
    use_instead: "method:oasis"
  - when: "adaptive iterative error-to-repair guidance for OPSD"
    reason: "Air-OPD synthesizes evolving repair guidance; RC-OPD locally repairs the student trajectory"
    use_instead: "method:air-opd"
  - when: "neighborhood expert privileged OPSD (frozen local perturbations)"
    reason: "N-OPSD densifies the teacher pool; RC-OPD is diagnosis of one trajectory"
    use_instead: "method:n-opsd"
assumptions:
  - "Privileged OPSD host that can diagnose an Error Stage, repair an Anchor Stage, and continue the same student policy. Paper: Qwen3-1.7B/4B/8B, Avg@4."
  - "Official code Starrylay/RC-OPD released as of 2026-10-05."
last_reviewed: "2026-10-05"
papers:
  - paper:rc-opd
recipes:
  - recipe:rc-opd
claims:
  - benchmark: "Qwen3-1.7B / 4B / 8B Avg@4 (Table 1)"
    metric: "Avg@4"
    value: "44.17 / 66.11 / 66.94"
    baseline: "OPSD 40.28 / 62.50 / 63.33"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03515"
    notes: "Not a VISTA bake-off (64.8→66.9) retarget."
  - benchmark: "Qwen3-8B AIME25 Avg@4"
    metric: "AIME25"
    value: "76.67"
    baseline: "OPSD 64.17"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03515"
    notes: "Same Table 1 8B block."
tags:
  - post-training
  - distillation
  - privileged-teacher
  - rc-opd
  - active
---

# RC-OPD

## Method Overview
Reference-conditioned OPSD can borrow a correct conclusion without repairing the student's derivation, and can over-constrain valid prefixes. RC-OPD finds the earliest substantive error, locally repairs it into an anchor, and tests the repair by letting the same student continue. Successful chains distill Failure Reason & Goal on the error span and COT-to-Anchor on the valid prefix. Exhausted budgets fall back to reference-conditioned OPSD.

## When to Use
- Privileged math OPSD where the student fails with a salvageable prefix and you can diagnose the first error.

## When NOT to Use
- Privileged-OPSD first hop → `method:vista`. Scale-collapse scaffolds → `method:oasis`. Iterative synthesized repair guidance → `method:air-opd`. Frozen neighborhood teachers → `method:n-opsd`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside VISTA / OASIS / N-OPSD / Air-OPD (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace VISTA.

## Gotchas & Failure Modes
- Do not cite 44.17 / 66.11 / 66.94 vs OPSD as beating the library VISTA bake-off (64.8→66.9).
- ROSD / DASH / PW-OPSD / AVSD / EOPD are paper baselines, not library methods.
