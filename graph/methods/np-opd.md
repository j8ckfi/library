---
id: method:np-opd
type: method
title: "NP-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "NP-OPD complements teacher OPD when overlap is low; OPD remains matching"
    use_instead: "method:opd"
  - when: "anti-collapse privileged OPSD that diverges from a negative condition"
    reason: "NSD is the negative-condition trainer on privileged OPSD; NP-OPD stays on frozen-teacher OPD"
    use_instead: "method:nsd"
  - when: "labeled Pass@1 math/code RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Frozen-teacher OPD where teacher/student token overlap is low. Combines with ExOPD / OPD2 in the paper."
  - "Code: naver-ai/np-opd (`code_status: released`)."
last_reviewed: "2026-10-07"
papers:
  - paper:np-opd
recipes:
  - recipe:np-opd
claims:
  - benchmark: "On-policy distillation with negative-policy rollouts vs teacher-only OPD"
    metric: "gain when teacher/student overlap is low"
    value: "negative-policy rollouts complement teacher supervision"
    baseline: "teacher-only OPD (ExOPD / OPD2 hosts in the paper)"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07874"
    notes: "Related to NSD but not a privileged-teacher trainer. Does not replace OPD or NSD."
tags:
  - post-training
  - distillation
  - opd
  - np-opd
  - active
---

# NP-OPD

## Method Overview
When teacher/student overlap is low, teacher OPD starves. NP-OPD samples negative-policy rollouts that complement teacher supervision instead of imitating a gold trace. Distinct from NSD, which diverges from a self-generated negative condition on privileged OPSD.

## When to Use
- Frozen-teacher OPD with low overlap. Compose with ExOPD / OPD2 if already on that host.

## When NOT to Use
- Default matching → `method:opd`. Privileged negative-condition anti-collapse → `method:nsd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD or NSD.

## Gotchas & Failure Modes
- **code: released** naver-ai/np-opd as of 2026-10-07.
- Do not confuse with NSD's negative condition.
