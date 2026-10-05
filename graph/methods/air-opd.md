---
id: method:air-opd
type: method
title: "Air-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "privileged-teacher OPSD with a matched VISTA-protocol bake-off"
    reason: "VISTA remains this task's first hop; Air-OPD changes the privileged context from a static gold solution to iterative repair guidance"
    use_instead: "method:vista"
  - when: "privileged OPSD gains collapse at scale; verified on-policy scaffolds"
    reason: "OASIS changes the scaffold/context; Air-OPD is multi-round error-to-repair"
    use_instead: "method:oasis"
  - when: "neighborhood expert privileged OPSD (frozen local perturbations)"
    reason: "N-OPSD densifies the teacher pool; Air-OPD synthesizes repair guidance"
    use_instead: "method:n-opsd"
  - when: "root-cause diagnosis of the student's own failed reasoning then differentiated prefix/error distillation"
    reason: "RC-OPD repairs the student's trajectory; Air-OPD iterates error-specific guidance"
    use_instead: "method:rc-opd"
assumptions:
  - "Privileged OPSD host plus a guidance generator (self-policy or a larger external model). Failed rollouts only. Paper: DAPO-Math-17K, Avg@12 on AIME24 / AIME25 / HMMT25."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:air-opd
recipes:
  - recipe:air-opd
claims:
  - benchmark: "Qwen3-4B Math Avg (AIME24 / AIME25 / HMMT25 Avg@12)"
    metric: "Math Avg"
    value: "66.7 External-G / 65.8 Self-G"
    baseline: "OPSD 63.1 / GRPO 62.3 / base 61.2"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02700"
    notes: "Not a VISTA bake-off (64.8→66.9) retarget. Self-G needs no extra model."
  - benchmark: "Qwen3-8B Math Avg (AIME24 / AIME25 / HMMT25 Avg@12)"
    metric: "Math Avg"
    value: "67.4 External-G / 66.9 Self-G"
    baseline: "OPSD 64.7 / GRPO 64.0 / base 61.8"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02700"
    notes: "Self-G +2.1 vs OPSD without an external model."
tags:
  - post-training
  - distillation
  - privileged-teacher
  - air-opd
  - active
---

# Air-OPD

## Method Overview
Vanilla privileged OPSD conditions the teacher on a full reference solution. That target does not say how to leave the student's current error. Air-OPD synthesizes repair guidance for the latest failure, retries on-policy with that guidance, and if the retry fails, writes new guidance. At each round a fixed teacher sees the guidance as privileged context and supervises only the error-aligned span of the failed response. Stage weights favor early rounds and credit stages whose retry verifies.

## When to Use
- Privileged math OPSD where a static gold solution invites a solution-conditioned shortcut, and you can afford multi-round retries.

## When NOT to Use
- Privileged-OPSD first hop → `method:vista`. Scale-collapse scaffolds → `method:oasis`. Frozen neighborhood teachers → `method:n-opsd`. Student-trajectory root-cause repair → `method:rc-opd`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside VISTA / OASIS / N-OPSD (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace VISTA.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Do not cite 66.7 / 67.4 Math Avg as beating the library VISTA bake-off (64.8→66.9).
- Failed-rollout-only OPSD in the ablation is 62.5, 0.6 below standard OPSD. The iterative repair is the method, not the failed-only mask.
