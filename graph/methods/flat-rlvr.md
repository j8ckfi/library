---
id: method:flat-rlvr
type: method
title: 'Flat-RLVR'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:math-code-rl-dense'
  reason: 'Flat-RLVR is an active plug-in; method:cispo remains the first hop'
  use_instead: method:cispo
assumptions:
- 'GRPO-family host. Sharpness-aware search of flat reward regions. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:flat-rlvr
recipes:
- recipe:flat-rlvr
claims:
- benchmark: 'RLVR Pass@K / coverage vs GRPO-family hosts'
  metric: 'sample diversity vs single-attempt accuracy'
  value: 'improved sample diversity while maintaining single-attempt accuracy vs GRPO variants'
  baseline: 'GRPO / GRPO-family RLVR'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29281'
  notes: 'Does not retarget method:cispo.'
tags:
- rlvr
- sharpness
- active
---

# Flat-RLVR

## Method Overview
Flat-RLVR adds sharpness-aware minimization to GRPO-family RLVR so the policy sits in flat-reward regions instead of collapsing onto peaked rare-yet-correct modes.

## When to Use
- RLVR runs that keep Pass@1 while Pass@K / coverage collapse from distribution sharpening.

## When NOT to Use
Default dense Pass@1 → `method:cispo`. Pass@K / no-backward first hop → `method:es-reasoning`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cispo`.

## Gotchas & Failure Modes
- No public code.
- SAM overhead sits on the GRPO host; not a CISPO loss swap.
