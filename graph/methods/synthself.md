---
id: method:synthself
type: method
title: SynthSelf
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: multi-stage agent capability stacking / routed LoRA experts (ACLArena)
  reason: SynthSelf is small-model synthetic SDFT; ACLArena remains sequential agent CL
  use_instead: method:aclarena
- when: single-teacher matching distillation from a strong frozen teacher
  reason: OPD remains that hop; SynthSelf outsources in-distribution rewrite to a same-family aligner
  use_instead: method:opd
assumptions:
- 'Small on-device student that fails SDFT''s ICL rewrite. Paper: 3 small scales, 4 acquisition sets,
  14 retention benches.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:synthself
recipes:
- recipe:synthself
claims:
- benchmark: 4 acquisition datasets (incl. a mixture) and 14 retention benchmarks, 3 small-model scales
  metric: acquisition and retention vs 6 methods including off- and on-policy distillation
  value: consistently outperforms the 6 compared methods at all 3 scales
  baseline: SDFT; off-policy distillation; on-policy distillation
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13113
  notes: Does not retarget ACLArena or OPD. Abstract does not list per-bench numbers.
tags:
- post-training
- distillation
- continual-learning
- synthself
- active
---

# SynthSelf

## Method Overview
Have a slightly larger same-family model rewrite new-task traces into the small student's distribution. Keep those traces with rejection sampling. Train the small model off-policy on the kept set so it does not leave its original mass.

## When to Use
- Continual post-train of a small / on-device model where SDFT's ICL rewrite fails.

## When NOT to Use
Sequential agent LoRA experts → `method:aclarena`. Strong-teacher OPD → `method:opd`.

## Relation to Existing SOTA
Active plug-in on `task:agent-continual-learning` with a mention on `task:student-distillation` (`sota_for: []`). Does **not** replace ACLArena or OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- The aligner must stay same-family and only slightly larger or the rewrite leaves-distribution.
- Off-policy + rejection sampling is load-bearing; naive SFT on the rewrite forgets.
