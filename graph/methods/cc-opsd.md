---
id: method:cc-opsd
type: method
title: CC-OPSD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: privileged same-size gold teacher OPSD (scoring teacher)
  reason: VISTA remains scoring-teacher OPSD; CC-OPSD first generates a critique then scores
  use_instead: method:vista
- when: hindsight-to-foresight distillation when verifier groups are silent (SRD)
  reason: SRD is silent-group hindsight; CC-OPSD is critique-conditioned scoring
  use_instead: method:srd
assumptions:
- 'Privileged teacher with a gold solution. Paper: gold error spans in student rollouts; math + cold-start
  GRPO. NeurIPS 2026 FLLMPT oral.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:cc-opsd
recipes:
- recipe:cc-opsd
claims:
- benchmark: Privileged OPSD scoring signals vs gold error spans; critique-conditioned teacher; cold-start
    GRPO
  metric: error localization / corrective credit / advantage on otherwise-silent prompts
  value: scoring-only KL and token log-ratio neither localize errors nor push mass off erroneous tokens;
    critique-conditioned scoring does, and also yields GRPO advantage on prompts with no verifier signal
  baseline: scoring-only privileged OPSD; outcome-only GRPO
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13744
  notes: Does not retarget VISTA. Critique is also useful at test time by resuming a wrong rollout.
tags:
- post-training
- distillation
- opsd
- cc-opsd
- active
---

# CC-OPSD

## Method Overview
Do not distill log-ratios from a gold-conditioned scorer alone. First sample a critique of the current rollout. Condition the scorer on that critique. Distill the resulting shift.

## When to Use
- Privileged OPSD where token KL/log-ratio does not sit on the actual error span.

## When NOT to Use
Scoring-teacher OPSD default → `method:vista`. Silent-group hindsight distill → `method:srd`.

## Relation to Existing SOTA
Active plug-in on `task:privileged-teacher-opsd` (`sota_for: []`). Does **not** replace VISTA or SRD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- NeurIPS 2026 FLLMPT oral; still a preprint evidence_level.
- Critique generation is extra teacher compute per rollout.
