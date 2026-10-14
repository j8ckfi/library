---
id: method:vrsd
type: method
title: VRSD (Self-Distillation with Verbal Regularization)
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: privileged-teacher OPSD with teacher adaptation on verified rollouts
  reason: VISTA remains the privileged-teacher first hop
  use_instead: method:vista
- when: anti-collapse by diverging from a self-generated negative condition
  reason: NSD remains the negative-condition trainer
  use_instead: method:nsd
assumptions:
- Privileged teacher can be steered by a system prompt. Paper: Qwen3-4B/8B and OLMo-3-7B.
- Official repo lijiazheng99/VRSD as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:vrsd
recipes:
- recipe:vrsd
claims:
- benchmark: Qwen3-4B / OLMo-3-7B / Qwen3-8B Pass@1; Qwen3-4B SQL
  metric: Pass@1 delta vs OPSD; SQL accuracy
  value: avg +3.9pp (7.2 / 2.8 / 1.6); 11/12 settings; SQL OPSD 69.8 vs VRSD 81.0
  baseline: privileged OPSD without verbal regularization (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.16354
  notes: Does not retarget VISTA or NSD.
tags:
- distillation
- privileged-opsd
- verbal-regularization
- active
---

# VRSD (Self-Distillation with Verbal Regularization)

## Method Overview
Keep the privileged OPSD student update. Soften the teacher's use of gold/privileged tokens with a system prompt so the student cannot shortcut by copying privileged cues.

## When to Use
- Privileged OPSD is collapsing entropy or copying the gold trace too literally.

## When NOT to Use
VISTA teacher adaptation → `method:vista`. Negative-condition divergence → `method:nsd`. Frozen larger teacher OPD → `method:opd`.

## Relation to Existing SOTA
Active plug-in on `task:privileged-teacher-opsd` (`sota_for: []`). Does **not** replace VISTA or NSD.

## Gotchas & Failure Modes
- Prompt-side regularizer; not a replacement for VISTA's teacher update.
