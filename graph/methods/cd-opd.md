---
id: method:cd-opd
type: method
title: 'CD-OPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; CD-OPD is takeover OPD with a contextual digest'
  use_instead: method:opd
- when: 'branch-and-resample at disagreement tokens'
  reason: 'BranchOPD is a different repair'
  use_instead: method:branchopd
assumptions:
- 'Teacher-takeover OPD on math. Paper: Qwen3-1.7B student, Qwen3-4B-Instruct teacher, eight benches.'
- 'Anonymous code dump; no GitHub as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:cd-opd
recipes:
- recipe:cd-opd
claims:
- benchmark: 'Eight math benches vs takeover OPD; Collaboration Failure Rate'
  metric: 'avg accuracy; CFR vs vanilla/Relay takeover'
  value: '+1.32 to +7.05 pp vs representative OPD; CFR -27.4% to -56.4% vs takeover OPD'
  baseline: 'vanilla prefix takeover; Relay-OPD'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.25359'
  notes: 'Teacher takeover can fail even when both models are independently correct. Does not replace OPD.'
tags:
- distillation
- opd
- takeover
- active
---

# CD-OPD

## Method Overview
CD-OPD (Contextual Digest for On-Policy Distillation) structures earlier teacher-guidance into a dependency-graph digest of required conditions and preceding reasoning, then continues the student. Online meta-reweighting compares digest-segment gradients to an independent-student task gradient. Collaboration Failure Rate measures takeover producing a wrong answer when both models were independently correct.

## When to Use
- Teacher-takeover OPD where independent student and teacher are both correct but the joined trajectory is not.

## When NOT to Use
Default matching → `method:opd`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Lengthening takeover does not monotonically cut CFR.
- Digest construction is teacher-generated.
