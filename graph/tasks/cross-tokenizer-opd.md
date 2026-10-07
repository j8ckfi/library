---
id: task:cross-tokenizer-opd
type: task
title: "Cross-Tokenizer On-Policy Distillation"
domain: "post-training"
summary: "OPD when the teacher and student tokenizers disagree: how much of the student sequence is already covered by a strict 1:1 alignment, and whether reverse-KL needs the full shared vocabulary."
scope: "Cross-tokenizer student distillation (different vocabularies). First hop is Cross-Tokenizer OPD: strict 1:1 coverage plus student-selected top-k reverse-KL on the shared vocab. Not same-tokenizer OPD, not privileged-teacher OPSD, not safety-alignment OPD."
out_of_scope:
  - "Same-tokenizer single-teacher matching (OPD)"
  - "Privileged same-size gold teacher (VISTA)"
  - "Multi-teacher capability merging (Open-MOPD)"
  - "OPD used as a safety-alignment trainer (backdoor risk note)"
redirects:
  - when: "same-tokenizer single-teacher matching distillation"
    to: "task:student-distillation"
  - when: "privileged same-size gold teacher OPSD"
    to: "task:privileged-teacher-opsd"
  - when: "OPD used for safety alignment / backdoor transfer risk"
    to: "paper:opd-safety-backdoor"
current_sota:
  - method: method:cross-tokenizer-opd
    as_of: "2026-10-07"
    benchmark: "Qwen3 / Llama / Gemma cross-tokenizer OPD, shared-vocab reverse-KL"
    metric: "fraction of full shared-vocab OPD gain retained at k=16"
    value: "strict 1:1 covers 85.57–96.98% of student tokens; k=16 retains ≥96% of full shared-vocab OPD"
    notes: "Cross-Tokenizer OPD (2610.08448). Method status active. Does not replace OPD on same-tokenizer student distillation."
methods:
  - method:cross-tokenizer-opd
  - method:opd
  - method:sparse-opd-supervision
  - method:np-opd
last_reviewed: "2026-10-07"
tags:
  - post-training
  - distillation
  - opd
  - tokenizer
  - cross-tokenizer
---

# Cross-Tokenizer On-Policy Distillation

## Problem Definition
Teacher and student vocabularies only partially overlap. Agents often assume a full shared-vocab reverse-KL or a learned span alignment. This task owns **how much of the student sequence a strict 1:1 map already covers**, and whether reverse-KL on a small student-selected shared-vocab subset matches full shared-vocab OPD.

This is **not** same-tokenizer OPD and not privileged-teacher OPSD.

## Evaluation Protocol
- **Primary Benchmarks**: cross-family teacher–student pairs (Qwen3 / Llama / Gemma) with Jaccard overlap in the 39–65% range; token-coverage of 1:1 maps; downstream accuracy vs full shared-vocab OPD.
- **Evaluation Pitfalls**: Span-level MSE alignment can hurt. Do not treat this as a retarget of `method:opd` on same-tokenizer distillation.

## SOTA Recommendation (as of 2026-10-07)
- **Primary (this task only)**: **Cross-Tokenizer OPD** (`method:cross-tokenizer-opd`, `paper:cross-tokenizer-opd` `arXiv:2610.08448`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:opd` remains same-tokenizer matching; `method:vista` remains privileged-teacher OPSD.
