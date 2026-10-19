---
id: method:sigma-delta-sampler
type: method
title: 'Sigma-Delta Sampler'
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'native 1.58-bit pretrain from scratch (Sparse-BitNet)'
  reason: 'Sparse-BitNet remains the 2026 BitNet line; Sigma-Delta Sampler is an Ising/ΣΔ discrete-weight trainer'
  use_instead: method:sparse-bitnet
- when: 'post-training ternarization of existing LLMs'
  reason: 'ScaleQ-1.58 remains PTQ ternarization'
  use_instead: method:scaleq-158
assumptions:
- 'Binary/ternary nets as hierarchical high-order Ising models. ΣΔ noise-shaped sampler as a noisy quantizer inside a first-order loop. Paper reports MatMul-free training to 2.7B.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:sigma-delta-sampler
recipes:
- recipe:sigma-delta-sampler
claims:
- benchmark: 'On-the-edge binary/ternary training; MatMul-free scale'
  metric: 'trainable scale without dense MatMul'
  value: 'MatMul-free discrete-weight training to 2.7B'
  baseline: 'Ising ground-state solvers / standard discrete-weight QAT (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22621'
  notes: 'Does not retarget Sparse-BitNet. Generalization, not ground-state search, is the training objective.'
tags:
- quantization
- ternary
- ising
- active
---

# Sigma-Delta Sampler

## Method Overview
Sigma-Delta Sampler treats discrete-weight training loss as a high-order Ising energy and embeds stochastic sampling-and-annealing as a noise-shaped quantizer inside a first-order loop so the solver generalizes instead of only seeking a ground state.

## When to Use
- Binary/ternary on-device training where an Ising solver would overfit a fixed energy and you need MatMul-free updates.

## When NOT to Use
Native 1.58-bit LLM pretrain → `method:sparse-bitnet`. Existing-LLM ternarization → `method:scaleq-158`.

## Relation to Existing SOTA
Active plug-in on `task:1bit-extreme-quantization` (`sota_for: []`). Does **not** replace Sparse-BitNet.

## Gotchas & Failure Modes
- Not a Sparse-BitNet 3B/7B Commonsense bake-off.
- Annealing must stay noisy enough to generalize.
