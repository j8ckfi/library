---
id: method:lct
type: method
title: 'LCT'
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'full-param subspace projections (SCALE)'
  reason: 'SCALE is the mem-efficient pretrain hop; LCT losslessly compresses tensors'
  use_instead: method:scale
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the optimizer'
  use_instead: method:muon2
- when: 'subspace Muon with residual correction (PMRC)'
  reason: 'PMRC is subspace Muon; LCT is Huffman tensors'
  use_instead: method:pmrc
assumptions:
- 'Training where peak memory is dominated by dense tensors and a small step-time tax is acceptable.'
- 'Code: none found as of 2026-10-16.'
last_reviewed: '2026-10-16'
papers:
- paper:lct
recipes:
- recipe:lct
claims:
- benchmark: 'NanoGPT 162M train; Qwen3-4B fine-tune peak memory / context'
  metric: 'memory; step-time; context length'
  value: 'NanoGPT -24.6% mem / +7.2% step-time; Qwen3-4B -23.8% peak, 3.5x context; up to 1.455x compression'
  baseline: 'uncompressed BF16/FP tensors (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22179'
  notes: 'Does not retarget SCALE. No public code as of 2026-10-16.'
tags:
- memory
- training-systems
- active
---

# LCT

## Method Overview
Huffman-code weights, activations, and optimizer states with precomputed GPU codebooks so tensors can be re-encoded every step. Track magnitude shifts so codebooks stay valid.

## When to Use
- Peak-memory bound full-param train/FT when a few percent of step-time can buy ~25% memory.

## When NOT to Use
SCALE subspace hop → `method:scale`. ~7B optimizer → `method:muon2`. Residual-correction subspace → `method:pmrc`.

## Relation to Existing SOTA
Active plug-in on `task:full-param-memory-efficient-pretrain` (`sota_for: []`). Does **not** replace SCALE.

## Gotchas & Failure Modes
- Magnitude shifts can invalidate codebooks; the paper characterizes that cost.
- No public kernels as of 2026-10-16.

