---
id: method:topa
type: method
title: 'ToPA'
category: peft
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'quality LoRA / rsLoRA + LR sweep rather than stacking adapters'
  reason: 'Quality default remains vanilla LoRA + rsLoRA + LR sweep; ToPA is block-wise Toeplitz PEFT'
  use_instead: method:lr-matters-lora
- when: 'dynamic tangent LoRA branch via residual-gradient SVD'
  reason: 'DT-LoRA is a tangent branch; ToPA is Toeplitz structure'
  use_instead: method:dt-lora
assumptions:
- 'Reparameterized PEFT via products of block-wise Toeplitz factors. Paper: 21 NLP/CV datasets, 5 architectures. Code: scongl/ToPA.'
last_reviewed: '2026-10-19'
papers:
- paper:topa
recipes:
- recipe:topa
claims:
- benchmark: '21 NLP and CV datasets across 5 architectures vs low-rank and sparse PEFT'
  metric: 'whether ToPA is more expressive / stronger empirically than low-rank and sparse parameterizations'
  value: 'products of block-wise Toeplitz matrices approximate arbitrary matrices at shorter chain length; consistently validates vs low-rank and sparse PEFT'
  baseline: 'low-rank LoRA-style / sparsity PEFT / full FT (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22883'
  notes: 'Does not retarget vanilla LoRA + rsLoRA + LR sweep. Long multiplicative Toeplitz chains are unstable; block-wise is the fix.'
tags:
- peft
- toeplitz
- lora
- active
---

# ToPA

## Method Overview
ToPA replaces long products of Toeplitz matrices with block-wise Toeplitz factors so each factor has more capacity, the chain is shorter, and training stays stable while remaining more expressive than low-rank or sparse PEFT.

## When to Use
- PEFT when low-rank updates underfit full-FT high-rank structure and sparse masks break connectivity, and you can use a Toeplitz parameterization.

## When NOT to Use
24GB quality default → `method:lr-matters-lora`.

## Relation to Existing SOTA
Active plug-in on `task:lora-quality-tuning` (`sota_for: []`). Does **not** replace vanilla LoRA + rsLoRA + LR sweep.

## Gotchas & Failure Modes
- Naive long Toeplitz products are RNN-like unstable.
- Not an MMLU/GSM8k LoRA-quality bake-off against the LR sweep.
