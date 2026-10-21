---
id: method:e8-qat
type: method
title: 'E8-QAT'
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'deployed checkpoint must stay NF4/INT4/MXFP4 with no high-precision adapter'
  reason: 'GradCodeS remains code-space FT; E8-QAT is 2-bit QAT with an implicit E8 lattice codebook'
  use_instead: method:gradcodes
- when: 'ultra-low-bit QAT recovery via on-policy reverse-KL (OnlineQAT)'
  reason: 'OnlineQAT recovers W3/W2 with reverse-KL; E8-QAT is lattice QAT'
  use_instead: method:onlineqat
- when: 'native FP4 forward/backward hardware training from scratch'
  reason: 'Quartet-II remains NVFP4 hardware training'
  use_instead: method:quartet-ii
assumptions:
- '2-bit QAT with E8 lattice projection, no explicit codebook search in the train forward.'
- 'Code lxy2137/E8_QAT as of 2026-10-21. Paper: Qwen3.6-35B-A3B.'
last_reviewed: '2026-10-21'
papers:
- paper:e8-qat
recipes:
- recipe:e8-qat
claims:
- benchmark: 'Qwen3.6-35B-A3B four-task average; IFEval; LiveCodeBench; decode vs BF16'
  metric: 'task average vs BF16; IFEval / LiveCodeBench vs SOTA 2-bit; peak mem / decode'
  value: 'matches BF16 four-task average; +2.03% IFEval / +1.51% LiveCodeBench vs SOTA 2-bit at same data/schedule/bitwidth; 80% peak-mem cut; 1.97x BF16 decode at max batch'
  baseline: 'full-precision; prior 2-bit QAT/PTQ at matched bit width'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27699'
  notes: 'Implicit E8 codebook. Does not retarget GradCodeS, OnlineQAT, or Quartet-II.'
tags:
- quantization
- qat
- 2bit
- lattice
- active
---

# E8-QAT

## Method Overview
E8-QAT quantizes 8-dimensional weight groups onto the E8 lattice by arithmetic projection, with a 2-bit core encoding plus a sparse extension, avoiding explicit codebook storage or search in the training forward pass.

## When to Use
- 2-bit QAT of an existing LLM when scalar 2-bit collapses and an explicit codebook is too expensive.

## When NOT to Use
Code-space FT → `method:gradcodes`. Reverse-KL recovery → `method:onlineqat`. NVFP4 from scratch → `method:quartet-ii`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:gradcodes`.

## Gotchas & Failure Modes
- Not GradCodeS (weights leave a discrete NF4/INT4/MXFP4 code search).
- Sparse extension adds <0.1% index storage.
