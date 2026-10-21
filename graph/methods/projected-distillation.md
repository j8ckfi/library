---
id: method:projected-distillation
type: method
title: 'Projected Distillation'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation when some student rollouts succeed'
  reason: 'OPD remains matching on student rollouts; projected distillation edits failed attempts into near-on-policy correct targets'
  use_instead: method:opd
- when: 'outcome-only long-horizon coverage with a checker'
  reason: 'CANOPY remains coverage; this is near-on-policy correction of failed student traces'
  use_instead: method:canopy
assumptions:
- 'Hard problems where all on-policy attempts fail. Paper: Qwen3-8B and OLMo-2-7B, five domains.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:projected-distillation
recipes:
- recipe:projected-distillation
claims:
- benchmark: 'Qwen3-8B / OLMo-2-7B; five domains math/code/science/tool; specialization-retention AUC'
  metric: 'area under specialization-retention frontier vs GRPO / OPD / SPOT / SODA'
  value: 'best on 8 of 9 cells vs GRPO and OPD; 7 of 9 vs SPOT and SODA; retention 0.916 vs 0.744 when replacing minimal edits with gold solutions'
  baseline: 'GRPO; OPD; SPOT; SODA; student-agnostic gold solutions'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27467'
  notes: 'Regret scales linearly with edit size under minimal correction vs quadratic under full-answer replacement. Does not retarget OPD.'
tags:
- distillation
- opd
- hard-problems
- active
---

# Projected Distillation

## Method Overview
Projected distillation minimally edits failed student attempts into correct targets, then uses contrastive updates and refreshed corrections so the student learns near on-policy even when every rollout fails.

## When to Use
- Hard-problem OPD/RL where all student attempts fail and gold solutions would pull the student off-policy.

## When NOT to Use
Working student rollouts → `method:opd`. Checker coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Retention falls as corrections move off-policy.
- Needs an editor that can produce small correct patches.
