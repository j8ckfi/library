---
id: method:reapo
type: method
title: 'ReAPO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:math-code-rl-dense'
  reason: 'ReAPO is an active plug-in; method:cispo remains the first hop'
  use_instead: method:cispo
assumptions:
- 'Failed attempts stay in context for later retries. Code Nghi-Dao/ReAPO.'
last_reviewed: '2026-10-22'
papers:
- paper:reapo
recipes:
- recipe:reapo
claims:
- benchmark: 'Qwen3 / OLMo-2 0.6B-4B; eight math and science benches vs GRPO'
  metric: 'first-attempt accuracy; tokens to GRPO peak on Qwen3-0.6B'
  value: 'beats GRPO and recent retry baselines on first-attempt; Qwen3-0.6B reaches 2x-group / 2x-step GRPO peaks with 39% / 31% fewer generated tokens'
  baseline: 'GRPO; GRPO with 2x group size or 2x steps'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28770'
  notes: 'Does not retarget method:cispo.'
tags:
- rlvr
- exploration
- active
---

# ReAPO

## Method Overview
ReAPO treats verified success as an SSP terminal and serializes failed GRPO attempts so a later success is credited without reinforcing the preceding failures.

## When to Use
- RLVR where independent group rollouts resample the same failed strategy and retry-in-context needs attempt-level credit.

## When NOT to Use
Default dense Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cispo`.

## Gotchas & Failure Modes
- Not a CISPO replacement.
- Serial retries change the token budget relative to independent groups.
