---
id: method:toolopd
type: method
title: 'ToolOPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains text matching; ToolOPD reweights action-token OPD with GRPO'
  use_instead: method:opd
- when: 'structural tool vs summary GRPO credit without a teacher'
  reason: 'SLCA-GRPO is the segment-credit first hop'
  use_instead: method:slca-grpo
assumptions:
- 'Long-horizon tool-use OPD + GRPO. Paper: ALFWorld / WebShop / FTRL-style tool benches.'
- 'Code MagicAgent-Search/ToolOPD as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:toolopd
recipes:
- recipe:toolopd
claims:
- benchmark: 'ALFWorld / WebShop / tool-use agent benches vs GRPO and uniform OPD'
  metric: 'success vs outcome RL and general (self-)distillation'
  value: 'credit-aware action-token OPD jointly optimized with GRPO; trajectory credit concentrates on a few critical actions'
  baseline: 'GRPO; uniform OPD; skill-conditioned self-distillation'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.25693'
  notes: 'Outcome-conditioned hindsight skill induction plus outcome-asymmetric skill relevance. Does not replace OPD, SLCA-GRPO, or CANOPY.'
tags:
- distillation
- opd
- tool-use
- active
---

# ToolOPD

## Method Overview
ToolOPD assigns OPD credit to tool-use actions using outcome-conditioned hindsight skills and outcome-asymmetric relevance, then jointly optimizes action-token reverse-KL with GRPO. Uniform OPD over a long trajectory is the wrong credit assumption.

## When to Use
- Distilling a tool-use student where most tokens are not the credit-bearing actions.

## When NOT to Use
Text OPD → `method:opd`. Tool vs summary GRPO without a teacher → `method:slca-grpo`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD, SLCA-GRPO, or CANOPY.

## Gotchas & Failure Modes
- Reversing only the final outcome changes credit on multiple turns.
- Joint GRPO weight is a hyperparameter.
