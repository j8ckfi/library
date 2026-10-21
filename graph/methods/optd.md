---
id: method:optd
type: method
title: 'OPTD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains final-layer matching; OPTD also matches layer-to-layer logp increments'
  use_instead: method:opd
- when: 'on-policy mechanism distillation beyond output supervision (OPMD)'
  reason: 'OPMD transfers intermediate computation; OPTD aligns depthwise prediction transitions'
  use_instead: method:opmd
assumptions:
- 'Student rollouts plus teacher/student intermediate layer pairs. Paper: three backbones, eight benches, dual- and three-domain.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:optd
recipes:
- recipe:optd
claims:
- benchmark: 'Three backbones; eight math/code/IF benches; dual- and three-domain distillation'
  metric: 'teacher-student capability-gap recovery vs OPD'
  value: 'three-domain recovers ~90% of the overall teacher-student gap vs ~75% for OPD; best or tied-best overall in dual- and three-domain'
  baseline: 'final-layer OPD'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28048'
  notes: 'Correct responses show lower mean transition KL at intermediate layer pairs. Does not retarget OPD.'
tags:
- distillation
- opd
- transitions
- active
---

# OPTD

## Method Overview
On-Policy Transition Distillation (OPTD) keeps final-layer OPD and adds alignment of layer-to-layer log-probability increments on student rollouts.

## When to Use
- OPD when intermediate prediction transitions correlate with correctness and you can afford extra teacher/student layer reads.

## When NOT to Use
Final-layer matching → `method:opd`. Mechanism-level intermediates → `method:opmd`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Needs comparable intermediate layers; tokenizer/arch mismatch is out of scope.
- Extra forward cost vs final-layer OPD.
