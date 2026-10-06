---
id: method:diffgate
type: method
title: "DiffGate"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "DiffGate mixes OPD teacher signal into GRPO on failed trajectories; OPD remains matching"
    use_instead: "method:opd"
  - when: "OPD then RLVR as a two-stage schedule"
    reason: "OPD-then-RLVR sequences stages; DiffGate is a per-group mix"
    use_instead: "method:opd-then-rlvr"
  - when: "labeled dense Pass@1 RLVR without a teacher"
    reason: "CISPO remains Pass@1; DiffGate needs a teacher on failed rollouts"
    use_instead: "method:cispo"
assumptions:
  - "GRPO-family host plus a white-box teacher. Paper: Qwen3-0.6B/1.7B students, code and math."
  - "No dedicated GitHub as of 2026-10-06; verl is the cited host (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:diffgate
recipes:
  - recipe:diffgate
claims:
  - benchmark: "Qwen3-0.6B / 1.7B code vs matched GRPO"
    metric: "avg@8 / pass@8 lift"
    value: "avg@8 +1.7 / +1.8; pass@8 +1.6 / +5.7"
    baseline: "matched GRPO"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.04596"
    notes: "Math avg@8 within 0.5 of GRPO; pass@8 +1.1 / +3.9. Does not retarget OPD, OPD-then-RLVR, or CISPO."
tags:
  - post-training
  - distillation
  - diffgate
  - active
---

# DiffGate

## Method Overview
DiffGate keeps GRPO's outcome reward and adds bounded teacher reverse-KL only on failed trajectories, scaled by group difficulty. The verifier gates which rollouts see the teacher; the teacher does not rewrite successful ones.

## When to Use
- Joint OPD+GRPO where all-fail groups and coverage (pass@8) are the complaint, not a two-stage OPD-then-RL schedule.

## When NOT to Use
- Matching OPD → `method:opd`. Two-stage OPD then RLVR → `method:opd-then-rlvr`. Pass@1 without a teacher → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` beside `method:opd-then-rlvr` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD or CISPO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06 (verl host, no dedicated repo).
- Do not apply the teacher to successful trajectories; that is not DiffGate.
