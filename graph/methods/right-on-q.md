---
id: method:right-on-q
type: method
title: 'Right On Q'
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:full-lowbit-finetune'
  reason: 'Right On Q is an active plug-in; method:gradcodes remains the first hop'
  use_instead: method:gradcodes
assumptions:
- 'Quantized student generates training prefixes. Dynamic KL vs the full-precision teacher. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:right-on-q
recipes:
- recipe:right-on-q
claims:
- benchmark: 'Qwen3-8B 2-bit reasoning vs fixed-response QAT'
  metric: 'average reasoning score vs QAT baselines'
  value: 'beats every 2-bit baseline on every bench and size; Qwen3-8B average +10.26'
  baseline: 'full-precision-supervised QAT on fixed responses'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29378'
  notes: 'Does not retarget method:gradcodes.'
tags:
- quantization
- qat
- active
---

# Right On Q

## Method Overview
Right On Q (OnQ) drops fixed-response QAT and supervises the quantized student on its own generated prefixes with a dynamic KL, so long-horizon reasoning prefixes match decode.

## When to Use
- Low-bit QAT of reasoners that fail to terminate inside the full-precision token budget under fixed-response supervision.

## When NOT to Use
Deployed NF4/INT4/MXFP4 FT with no high-precision adapter → `method:gradcodes`. On-policy reverse-KL QAT recovery → `method:onlineqat`. Native FP4 from scratch → `method:quartet-ii`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:gradcodes`.

## Gotchas & Failure Modes
- No public code.
- On-policy prefixes are the point; replaying teacher traces reopens the mismatch.
