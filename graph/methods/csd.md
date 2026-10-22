---
id: method:csd
type: method
title: 'CSD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:cross-tokenizer-opd'
  reason: 'CSD is an active plug-in; method:cross-tokenizer-opd remains the first hop'
  use_instead: method:cross-tokenizer-opd
assumptions:
- 'Teacher and student tokenizers disagree. Dynamic joint training of the common-support map.'
last_reviewed: '2026-10-22'
papers:
- paper:csd
recipes:
- recipe:csd
claims:
- benchmark: 'Llama-3.1-8B and 1B Llama/Gemma students vs X-Token / ALM'
  metric: 'average accuracy vs strongest evaluated baseline'
  value: 'Llama-3.1-8B up to +4.2 vs strongest baseline; highest average vs X-Token 0.66-5.38 and ALM 1.33-3'
  baseline: 'X-Token; ALM; strongest paper baseline (not library Cross-Tokenizer OPD bake-off)'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28895'
  notes: 'Does not retarget method:cross-tokenizer-opd.'
tags:
- distillation
- cross-tokenizer
- active
---

# CSD

## Method Overview
CSD aligns teacher and student next-token distributions on a dynamically constructed common support of chunk continuations instead of restricting to a shared vocabulary subset or a single observed chunk.

## When to Use
- Cross-tokenizer logits distillation when 1:1 coverage or shared-vocab reverse-KL leaves alternative continuations unmatched.

## When NOT to Use
Same-tokenizer matching → `method:opd`. Default cross-tokenizer hop → `method:cross-tokenizer-opd`. Chunk credit after correspondence → `method:cast`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cross-tokenizer-opd`.

## Gotchas & Failure Modes
- Paper baselines are not the library 1:1 / k=16 bake-off.
- Host code is NVIDIA-NeMo/RL, not a dedicated CSD repo.
