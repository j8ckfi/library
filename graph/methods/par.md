---
id: method:par
type: method
title: 'PAR'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'experimental CED all-token recurrence, not mixed-depth looping'
  reason: 'RLT remains the CED-recurrence experimental hop; PAR is progress-aligned state-tracking recurrence'
  use_instead: method:recurrent-looped-transformer
- when: 'Huginn-style dense fixed-point looped LMs (learned depth prior / terminal KV sharing)'
  reason: 'Looped Models Done Right is Huginn-style; PAR is progress-aligned recurrence for state tracking'
  use_instead: method:looped-models-done-right
assumptions:
- 'Sequential state tracking with per-iteration progress targets and first-iteration norm anchoring.'
- 'Paper: Qwen2.5-0.5B swap-S5, train <=32 moves, test 512. No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:par
recipes:
- recipe:par
claims:
- benchmark: 'swap-S5 Qwen2.5-0.5B trained on at most 32 moves, evaluated at 512 moves'
  metric: 'mean full-state accuracy vs RLT / explicit CoT; ablation of norm anchoring and progress targets'
  value: '95.5% at 16x train length vs RLT 55.7% and CoT 0.8%; no norm-anchor <2.2x; final-answer targets at most 8x'
  baseline: 'RLT; explicit chain of thought; ablations without norm anchoring or progress-aligned targets'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27628'
  notes: 'Does not retarget RLT as the CED experimental hop or Looped Models Done Right.'
tags:
- architecture
- looped-lm
- length-generalization
- active
---

# PAR

## Method Overview
Progress-Aligned Recurrence (PAR) trains iteration k to match the state after the first k operations and rescales recurrent states to first-iteration norms so extra test-time loops track longer sequences.

## When to Use
- Looped LMs on sequential state tracking where extra iterations currently fail to length-generalize.

## When NOT to Use
CED experimental hop → `method:recurrent-looped-transformer`. Huginn-style → `method:looped-models-done-right`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:recurrent-looped-transformer`.

## Gotchas & Failure Modes
- Gains are for state-tracking task structure, not generic CED serving.
- Prefix self-distillation is the unlabeled-intermediate fallback.
