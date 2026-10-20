---
id: method:loop-opd
type: method
title: 'LOOP'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'LOOP uses OPD to recover after iterative layer prune, not as the distill default'
  use_instead: method:opd
- when: 'fully low-bit code-space fine-tune'
  reason: 'GradCodeS is the low-bit FT first hop'
  use_instead: method:gradcodes
assumptions:
- 'Iterative layer prune + OPD recovery. Paper: Qwen3-1.7B to 8B, 15-25% layer drop.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:loop-opd
recipes:
- recipe:loop-opd
claims:
- benchmark: 'Qwen3-4B-Instruct math avg at 15/20/25% layer prune; 1.7B-8B at 20%'
  metric: 'avg mathematical reasoning vs strongest one-shot prune+recover baseline'
  value: '+7.37 / +9.10 / +6.34 pp at 15/20/25% on Qwen3-4B-Instruct; wins at 20% on 1.7B-8B'
  baseline: 'one-shot prune then recover'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.25679'
  notes: 'Recovery-oriented layer importance (reasoning contribution × recovery sensitivity). Does not replace OPD.'
tags:
- distillation
- opd
- pruning
- active
---

# LOOP

## Method Overview
LOOP iteratively drops layers using a recovery-aligned importance score (reasoning contribution fused with recovery sensitivity), then runs OPD recovery before the next drop. One-shot prune-to-target makes later recovery harder.

## When to Use
- Shrinking a dense LLM by whole layers and you can afford interleaved OPD recovery.

## When NOT to Use
Default distill → `method:opd`. Quantized FT → `method:gradcodes`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Not a student-distill first hop.
- Importance fusion is a hyperparameter.
