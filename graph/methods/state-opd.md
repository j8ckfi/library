---
id: method:state-opd
type: method
title: State-OPD
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-teacher text distillation without a multi-turn interaction state
  reason: State-OPD grounds teacher targets in matched interaction states, not frozen-teacher OPD
  use_instead: method:opd
- when: programmatic checker AppWorld coverage / anti-drift
  reason: CANOPY remains outcome-only coverage; State-OPD is multi-turn agent OPD
  use_instead: method:canopy
- when: multi-turn agent OPD at pivotal early mistakes (prevent reverse-KL + recover forward-KL)
  reason: PivotOPD is reverse-KL prevent / forward-KL recover; State-OPD is state-grounded sampling
  use_instead: method:pivotopd
assumptions:
- 'Multi-turn tool/agent env with interaction states. Paper: ALFWorld, ScienceWorld, WebShop; Qwen3-1.7B/4B
  students.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:state-opd
recipes:
- recipe:state-opd
claims:
- benchmark: ALFWorld / ScienceWorld / WebShop, Qwen3-1.7B and Qwen3-4B students
  metric: macro-average success vs strongest baseline
  value: Qwen3-4B 31.74 vs 26.07; highest macro-average among evaluated methods at both sizes; Qwen3-4B
    surpasses Qwen3-32B teacher on ALFWorld Seen
  baseline: strongest evaluated multi-turn OPD / agent baseline in the paper
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13238
  notes: Does not retarget CANOPY, OPD, PivotOPD, or ActFirst-OPD.
tags:
- post-training
- distillation
- opd
- agentic
- state-opd
- active
---

# State-OPD

## Method Overview
Match teacher continuation on the objective interaction state (task + action-observation record), not on the student's private CoT. Spend extra samples on high-entropy states as full reasoning-action responses rather than action-only resamples under a frozen trace.

## When to Use
- Multi-turn agent OPD where teacher targets are poisoned by the student's prior CoT, and you can identify high-entropy interaction states.

## When NOT to Use
Text OPD → `method:opd`. AppWorld coverage → `method:canopy`. Pivotal-mistake reverse/forward KL → `method:pivotopd`. Act-first inverse dynamics → `method:actfirst-opd`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` with a mention on `task:student-distillation` (`sota_for: []`). Does **not** replace CANOPY, OPD, PivotOPD, or ActFirst-OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Removing prior student reasoning at matched states is the teacher-target fix; do not distill the student's CoT as if it were the state.
- Entropy-triggered resampling is a budget split, not extra environment steps for free.
