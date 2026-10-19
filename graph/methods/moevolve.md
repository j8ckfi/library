---
id: method:moevolve
type: method
title: 'MoEvolve'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'MoE/VL RLVR loss (SAPO default)'
  reason: 'SAPO remains MoE RLVR; MoEvolve is high-k then distill-back OPD'
  use_instead: method:sapo
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; MoEvolve uses the model''s own expanded-k teacher'
  use_instead: method:opd
assumptions:
- 'MoE with a controllable activation budget k. Recovery-then-improvement: restore high-k, strengthen, distill back to original k.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:moevolve
recipes:
- recipe:moevolve
claims:
- benchmark: 'Diverse MoE models vs initial low-k and same-budget RLVR'
  metric: 'domain-average points'
  value: 'up to +22.2 vs initial; up to +6.5 vs same-budget RLVR; final low-k often beats the expanded teacher'
  baseline: 'same-budget RLVR / naive high-k expansion (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23185'
  notes: 'Does not retarget SAPO or OPD. Naive expansion without recovery degrades.'
tags:
- moe
- opd
- rlvr
- active
---

# MoEvolve

## Method Overview
MoEvolve first restores an activation-expanded high-k MoE and strengthens it, then reverse-distills those capabilities into the original low-k routing so inference keeps the original activation budget.

## When to Use
- MoE RLVR or OPD when you can temporarily raise k to build a stronger in-family teacher, then return to the deployed activation budget.

## When NOT to Use
Default MoE/VL RLVR → `method:sapo`. Dense Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-moe` with a mention on `task:student-distillation` (`sota_for: []`). Does **not** replace SAPO or OPD.

## Gotchas & Failure Modes
- Naive high-k expansion without the recovery stage hurts.
- Not a CISPO/SAPO bake-off on MATH-500.
