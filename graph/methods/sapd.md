---
id: method:sapd
type: method
title: "SAPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged same-size gold teacher OPSD with a live teacher update"
    reason: "VISTA remains the privileged-teacher first hop; SAPD is rollout-free step-aligned distill"
    use_instead: "method:vista"
  - when: "single-teacher student distillation from a larger frozen teacher"
    reason: "OPD remains matching; SAPD uses a reference solution as privileged context"
    use_instead: "method:opd"
  - when: "dense math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "A reference solution with identifiable reasoning steps exists. No live rollouts."
  - "Code: Miaow-Lab/SAPD (`code_status: released`)." 
last_reviewed: "2026-10-09"
papers:
  - paper:sapd
recipes:
  - recipe:sapd
claims:
  - benchmark: "Mathematical reasoning vs SFT / label smoothing / on-policy RL / self-distillation"
    metric: "average math accuracy and training-loop speed vs on-policy baselines"
    value: "beats SFT and label smoothing; competitive with on-policy RL; ~2x training-loop speedup"
    baseline: "SFT; label smoothing; on-policy RL; self-distillation"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.09665"
    notes: "Does not retarget VISTA or CISPO." 
tags:
  - post-training
  - distillation
  - privileged
  - sapd
  - active
---

# SAPD

## Method Overview
Walk a known reference solution step by step. At each student prefix, the remaining solution is privileged context that shapes a distributional target for the current transition only, not the whole gold trace as undifferentiated context.

## When to Use
- You have gold traces with steps and cannot afford on-policy rollouts, but SFT on those traces is too blunt.

## When NOT to Use
- Live privileged teacher update -> `method:vista`. Frozen larger teacher matching -> `method:opd`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` (`sota_for: []`) with a mention on `task:student-distillation`. Does **not** replace VISTA or OPD.

## Gotchas & Failure Modes
- **code: released** Miaow-Lab/SAPD as of 2026-10-09.
- Step alignment is the method; dumping the full gold solution as context is the thing it argues against.
