---
id: method:ap-opd
type: method
title: 'AP-OPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; AP-OPD rescales supervision after penalty jumps'
  use_instead: method:opd
- when: 'sampled-token OPD entropy plug-in (IDA-OPD)'
  reason: 'IDA-OPD keeps entropy-expanding tokens; AP-OPD pullbacks block-level penalty jumps'
  use_instead: method:ida-opd
assumptions:
- 'Sampled-token student-teacher log-ratios with consecutive token blocks. Math and code OPD.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:ap-opd
recipes:
- recipe:ap-opd
claims:
- benchmark: 'Mathematical reasoning and code generation OPD'
  metric: 'task performance vs ordinary OPD after pullback at penalty jumps'
  value: 'improves math and code OPD by scaling post-jump coefficients so the next block matches the previous block mean penalty'
  baseline: 'ordinary sampled-token OPD'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28194'
  notes: 'Penalty jumps persist on held-out tokens and coincide with falling teacher confidence. Does not retarget OPD.'
tags:
- distillation
- opd
- reweight
- active
---

# AP-OPD

## Method Overview
Adaptive Pullback OPD (AP-OPD) detects abrupt increases in average student-teacher penalty, then uniformly scales later-block coefficients so the weighted penalty matches the previous block, without an extra strength hyperparameter.

## When to Use
- Sampled-token OPD where penalties spike mid-response while teacher confidence drops.

## When NOT to Use
Uniform matching → `method:opd`. Entropy keep-mask → `method:ida-opd`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Jump detection is block-wise; short responses have few blocks.
- Does not replace token keep-masks.
