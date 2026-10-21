---
id: method:rsd
type: method
title: 'RSD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-size teacher privileged with a gold solution and a deterministic verifier (VISTA)'
  reason: 'VISTA remains privileged-teacher first hop; RSD uses retrospective context without GT or verifier rewards'
  use_instead: method:vista
- when: 'unlabeled existing math problems with majority-vote pseudo-solutions'
  reason: 'u-OPSD is unlabeled math consensus; RSD is agent trajectory retrospective self-distill'
  use_instead: method:u-opsd
assumptions:
- 'Same model as student and teacher; privileged context is hindsight plus cross-task lessons, not gold solutions.'
- 'Paper: ALFWorld / ScienceWorld / SearchQA, Qwen3-8B / 14B. No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:rsd
recipes:
- recipe:rsd
claims:
- benchmark: 'ALFWorld / ScienceWorld / SearchQA; Qwen3-8B / 14B'
  metric: 'relative gain vs base; extra gain from frontier-guided context-policy edits'
  value: 'up to +59.7% relative vs base; frontier-guided context policy adds up to +44.7% relative over a fixed context policy'
  baseline: 'base model; fixed retrospective context policy'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27495'
  notes: 'No GT trajectories or verifier rewards for the core update. Does not retarget VISTA.'
tags:
- distillation
- opsd
- privileged
- agentic
- active
---

# RSD

## Method Overview
Retrospective Self-Distillation (RSD) re-scores the student's realized actions with privileged hindsight, turn-level reflection, and cross-task lessons, then distills that teacher distribution back on-policy. An optional frontier model edits how privileged context is built.

## When to Use
- Self-evolving agents with trajectories but no gold solutions or verifier rewards.

## When NOT to Use
Gold solution + verifier → `method:vista`. Unlabeled math consensus → `method:u-opsd`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:vista`.

## Gotchas & Failure Modes
- Teacher sees the completed trajectory; leakage into the student update must stay out of the student context.
- Not VISTA (no gold solution / verifier).
