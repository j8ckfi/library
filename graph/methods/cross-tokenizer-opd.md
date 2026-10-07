---
id: method:cross-tokenizer-opd
type: method
title: "Cross-Tokenizer OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "same-tokenizer single-teacher matching distillation"
    reason: "Cross-tokenizer OPD is for disagreeing vocabs; OPD remains same-tokenizer matching"
    use_instead: "method:opd"
  - when: "privileged same-size gold teacher OPSD"
    reason: "VISTA remains privileged-teacher first hop"
    use_instead: "method:vista"
  - when: "OPD used for safety alignment / backdoor transfer risk"
    reason: "A backdoored safety teacher transfers hidden behavior under OPD"
    use_instead: "paper:opd-safety-backdoor"
assumptions:
  - "Teacher and student tokenizers disagree. Paper: Qwen3 / Llama / Gemma pairs, Jaccard 39.49–64.87%."
  - "No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:cross-tokenizer-opd
recipes:
  - recipe:cross-tokenizer-opd
claims:
  - benchmark: "Cross-tokenizer OPD, strict 1:1 coverage vs Jaccard overlap"
    metric: "fraction of student tokens covered by 1:1 alignment"
    value: "85.57–96.98%"
    baseline: "Jaccard overlap 39.49–64.87%"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08448"
    notes: "Does not retarget same-tokenizer OPD."
  - benchmark: "Shared-vocab reverse-KL, student-selected top-k vs full shared vocab"
    metric: "fraction of full shared-vocab OPD gain retained"
    value: "k=16 retains ≥96%"
    baseline: "full shared-vocab reverse-KL OPD"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.08448"
    notes: "Span MSE alignment hurts. Top HF Daily paper 2026-10-07."
tags:
  - post-training
  - distillation
  - opd
  - tokenizer
  - cross-tokenizer-opd
  - active
---

# Cross-Tokenizer OPD

## Method Overview
Keep a strict 1:1 sequence map for the bulk of student tokens. Restrict reverse KL to a student-selected top-k subset of the shared vocabulary (k=16 in the paper). Do not replace 1:1 coverage with span-level MSE.

## When to Use
- Teacher and student tokenizers disagree and a full shared-vocab reverse-KL is expensive.

## When NOT to Use
- Same tokenizer → `method:opd`. Privileged gold teacher → `method:vista`.

## Relation to Existing SOTA
- Active first hop on `task:cross-tokenizer-opd` (`sota_for: []`). Does **not** enter `task:student-distillation` `current_sota`. Does **not** replace OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- Span MSE is the wrong leftover-token fix.
