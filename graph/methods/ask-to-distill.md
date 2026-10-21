---
id: method:ask-to-distill
type: method
title: 'Ask-to-Distill'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation on an existing prompt bank'
  reason: 'OPD remains matching; Ask-to-Distill synthesizes the prompt bank'
  use_instead: method:opd
- when: 'OPD data-efficiency on one or a few real queries (OPD-II / hard-CoT)'
  reason: 'Ask-to-Distill generates questions; OPD-one-example / hard-CoT select from existing data'
  use_instead: method:opd-one-example
assumptions:
- 'Frozen student-teacher pair; synthesizer optimized without reference answers.'
- 'Code GasolSun36/Ask_to_Distill as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:ask-to-distill
recipes:
- recipe:ask-to-distill
claims:
- benchmark: 'Math / code / agentic OPD vs unoptimized student prompts and KL-filtered real questions'
  metric: 'average performance and teacher-gap recovery vs unoptimized / KL-filtered / real-bank OPD'
  value: 'improves over unoptimized student prompts and KL-filtered real questions; matches or exceeds real-bank OPD in evaluated settings'
  baseline: 'unoptimized student-generated prompts; KL-filtered real questions; real-bank OPD'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27450'
  notes: 'Distributional surrogate from disagreement plus teacher mass on student support. Code GasolSun36/Ask_to_Distill.'
tags:
- distillation
- opd
- synthetic-data
- active
---

# Ask-to-Distill

## Method Overview
Ask-to-Distill treats synthetic questions as distribution elicitors. A student-initialized synthesizer is scored by teacher-student disagreement and teacher mass on the student's support, without answers or per-candidate student updates; the bank then feeds ordinary OPD.

## When to Use
- OPD when you can generate prompts but lack labels, and you want denser teacher supervision than a raw question dump.

## When NOT to Use
Existing labeled bank → `method:opd`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Synthesizer reward uses a frozen pair; stale students change which questions look valuable.
- Still runs ordinary OPD after the bank is built.
