---
id: method:cast
type: method
title: CAST
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: history-adaptive spectral clipping of AdamW gradients (CAST-SSC)
  reason: method:cast is cross-tokenizer OPD credit; CAST-SSC is pretrain spectral clipping (2610.19761)
  use_instead: method:cast-ssc
- when: same-tokenizer single-teacher matching distillation
  reason: CAST is credit alignment after chunk correspondence; OPD remains same-tokenizer matching
  use_instead: method:opd
- when: strict 1:1 coverage / student-selected top-16 shared-vocab reverse-KL without chunk credit
  reason: Cross-Tokenizer OPD owns coverage and top-k shared-vocab reverse-KL; CAST redistributes chunk
    advantage
  use_instead: method:cross-tokenizer-opd
assumptions:
- 'Teacher and student tokenizers may disagree. Paper: Qwen3-8B → Mistral-7B / Llama-3.1-8B and shared-tokenizer
  Qwen3-1.7B.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:cast
recipes:
- recipe:cast
claims:
- benchmark: Six math/science/code benches, cross-tokenizer OPD from Qwen3-8B
  metric: average vs strongest evaluated baseline
  value: +2.45 Mistral-7B / +1.32 Llama-3.1-8B cross-tokenizer; +2.10 shared-tokenizer Qwen3-1.7B
  baseline: strongest evaluated cross-tokenizer / shared-tokenizer OPD baseline in the paper
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13257
  notes: Credit assignment after chunk alignment. Does not retarget Cross-Tokenizer OPD coverage or same-tokenizer
    OPD.
tags:
- post-training
- distillation
- opd
- cross-tokenizer
- cast
- active
---

# CAST

## Method Overview
After chunks are aligned, reweight student tokens inside each chunk so the weights solve a KL-regularized credit problem and sum to the chunk advantage. Unaligned positions get a stay KL to the initial policy rather than unconstrained reverse-KL.

## When to Use
- Cross-tokenizer (or shared-tokenizer chunked) OPD where 1:1 / decoded-text alignment exists but token credit inside chunks is wrong.

## When NOT to Use
Same-tokenizer matching → `method:opd`. Coverage / top-16 shared-vocab reverse-KL without credit split → `method:cross-tokenizer-opd`.

## Relation to Existing SOTA
Active plug-in on `task:cross-tokenizer-opd` beside `method:cross-tokenizer-opd` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Cross-Tokenizer OPD or OPD.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Chunk construction is an input. CAST does not invent the alignment.
- Unaligned tokens must be anchored or they drift.
