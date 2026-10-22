---
id: method:pace
type: method
title: 'PACE'
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:linear-time-sequence-modeling'
  reason: 'PACE is an active plug-in; method:mamba-2 remains the first hop'
  use_instead: method:mamba-2
assumptions:
- 'Fixed-size recurrent state. Periodic rounding plus a short token buffer. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:pace
recipes:
- recipe:pace
claims:
- benchmark: '4B-35B linear-attention decode vs 8-bit DAMP / Q-Mamba'
  metric: 'quality vs memory vs 8-bit DAMP and Q-Mamba'
  value: 'mixed 4/8-bit heads competitive with 8-bit DAMP at about two thirds the memory on the three larger models; 4-bit throughout beats Q-Mamba at equal memory'
  baseline: 'per-token 4-bit rounding; 8-bit DAMP; Q-Mamba'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29545'
  notes: 'Does not retarget method:mamba-2.'
tags:
- ssm
- quantization
- active
---

# PACE

## Method Overview
PACE stores linear-attention recurrent state in four bits but rounds only every few generated tokens, keeping the intervening tokens in a small buffer the way chunked prefill kernels already do.

## When to Use
- Linear-attention / SSM decode where KV-free state still dominates batch memory and per-token 4-bit rounding loses accuracy.

## When NOT to Use
Architecture from scratch → `method:mamba-2`. Hybrid SSM decode buffer → `method:replayssm`. INT4 KV async RLVR → `method:kv4-rl`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:mamba-2`.

## Gotchas & Failure Modes
- Post-hoc; no fine-tune required in the paper.
- No public code.
- Not an LLM KV-cache method.
