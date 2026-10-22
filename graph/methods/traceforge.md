---
id: method:traceforge
type: method
title: 'TraceForge'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:student-distillation'
  reason: 'TraceForge is an active plug-in; method:opd remains the first hop'
  use_instead: method:opd
assumptions:
- 'Teacher answer is available. Two-stage generator+critic. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:traceforge
recipes:
- recipe:traceforge
claims:
- benchmark: 'Five-benchmark SFT; coding HumanEval+ / MBPP+ vs teacher-hidden traces'
  metric: 'pass@1 vs Fable-5 own-thinking content; authenticity score'
  value: 'generated family-native traces beat Fable 5''s own thinking on coding; authenticity 0.68 vs real traces 0.66 (critic-selected 0.82)'
  baseline: 'teacher answer without a reasoning trace; encrypted-block replay (ToS-breaking)'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29680'
  notes: 'Does not retarget method:opd.'
tags:
- distillation
- traces
- active
---

# TraceForge

## Method Overview
TraceForge trains a generator to write student-family reasoning traces from context plus a teacher answer, then a critic picks authentic-looking traces. Training is SFT then adversarial; it does not replay encrypted teacher blocks.

## When to Use
- Distillation when the teacher returns an answer (or short summary) but withholds the reasoning trace, and breaking ToS to recover hidden tokens is not an option.

## When NOT to Use
Teacher logp available → `method:opd`. Missing logp but an external trace exists → `method:bridged-self-distill`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Authenticity is not correctness.
- No public code.
- General-task corpora looked similar; coding is where family-native traces moved the needle.
