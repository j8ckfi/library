---
id: method:gr-opd
type: method
title: 'GR-OPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; GR-OPD aggregates token feedback into sequence credit'
  use_instead: method:opd
- when: 'token keep-mask / sparse OPD budget'
  reason: 'IER/IDA/sparse-OPD select tokens; GR-OPD is sequence-level credit'
  use_instead: method:ier-opd
assumptions:
- 'OPD host with same-prompt rollout groups. Paper: five Qwen3 teacher-student settings, six math benches.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:gr-opd
recipes:
- recipe:gr-opd
claims:
- benchmark: 'Five Qwen3 teacher-student settings, six math benches, macro Avg@K vs vanilla OPD'
  metric: 'macro Avg@K; two matched-thinking settings'
  value: 'wins every setting; +10.9 and +11.5 pp with matched thinking; vanilla OPD collapses on mismatched thinking'
  baseline: 'vanilla OPD (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23042'
  notes: 'Does not retarget OPD. Collective teacher pressure is a hyperparameter.'
tags:
- distillation
- opd
- sequence-credit
- active
---

# GR-OPD

## Method Overview
GR-OPD aggregates token-level teacher feedback into calibrated sequence-level credit, discounts later feedback under distribution shift, and keeps a controlled fraction of the group mean as collective teacher pressure.

## When to Use
- OPD where sampled-token credit is too local, especially mismatched thinking patterns that collapse vanilla OPD.

## When NOT to Use
Default matching distill → `method:opd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Excess collective teacher pressure or an unrestricted feedback horizon destabilizes training.
- No public code.
