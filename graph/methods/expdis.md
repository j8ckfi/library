---
id: method:expdis
type: method
title: "ExpDis"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense math/code Pass@1 RLVR loss"
    reason: "ExpDis is an explore/distill split; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "exploration-preserving advantage shaping on an existing group reward"
    reason: "ExPPO reshapes advantage; ExpDis trains a separate explorer"
    use_instead: "method:exppo"
  - when: "Pass@K / coverage / no-backward rather than Pass@1"
    reason: "ES-reasoning remains Pass@K"
    use_instead: "task:passk-reasoning-coverage"
assumptions:
  - "A correctness filter exists. Explorers can be cheaper copies of the student."
  - "Code: SaifPunjwani/Exploration-Distillation (`code_status: released`)." 
last_reviewed: "2026-10-09"
papers:
  - paper:expdis
recipes:
  - recipe:expdis
claims:
  - benchmark: "Seven math reasoning benchmarks, two model families, matched wall-clock vs DAPO"
    metric: "whether novelty belongs in the deployed-policy reward"
    value: "ExpDis outperforms DAPO at the same wall-clock; improved pass@k scaling"
    baseline: "DAPO with a novelty bonus on the deployed policy"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.10536"
    notes: "Does not retarget CISPO. Pass@k lift is coverage, not a Pass@1 kernel change." 
tags:
  - post-training
  - rlvr
  - exploration
  - expdis
  - active
---

# ExpDis

## Method Overview
Train one or more explorer policies with a novelty bonus. Keep only traces that pass the verifier and a quality filter. Distill those traces into a student whose reward has no novelty term. Iterate.

## When to Use
- You want new strategies out of RLVR but a novelty bonus on the deployed policy wrecks prior behavior.

## When NOT to Use
- Pass@1 kernel -> `method:cispo`. Advantage shaping on one group -> `method:exppo`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CISPO.

## Gotchas & Failure Modes
- **code: released** SaifPunjwani/Exploration-Distillation as of 2026-10-09.
- Explorer traces that fail the filter must not leak into the student.
