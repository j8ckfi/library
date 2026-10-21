---
id: method:kronlstm
type: method
title: 'KronLSTM'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'linear-time architecture from scratch (SSM / Mamba)'
  reason: 'Mamba-2 remains the architecture default; KronLSTM is xLSTM-family linear attention with a Kronecker delta memory revision'
  use_instead: method:mamba-2
- when: 'checkpoint + recent-input buffer for hybrid SSM decode (ReplaySSM)'
  reason: 'ReplaySSM is a serving buffer; KronLSTM is a memory-update rule'
  use_instead: method:replayssm
assumptions:
- 'Associative matrix memory revised along a single matrix-space direction. xLSTM family.'
- 'Code NX-AI/KronLSTM as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:kronlstm
recipes:
- recipe:kronlstm
claims:
- benchmark: 'Linear-attention language modeling and long-context benches vs (Gated) DeltaNet family'
  metric: 'quality vs DeltaNet-family linear attention; memory-norm stability without extra normalizers'
  value: 'competitive with and often better than (Gated) DeltaNet-family models, especially on long context; expected memory norm stays uniformly bounded'
  baseline: '(Gated) DeltaNet-family linear attention'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26834'
  notes: 'Re-ingest: skipped 2026-10-20 as KronLSTM-the-LSTM. It is linear attention. Does not retarget Mamba-2.'
tags:
- linear-attention
- xlstm
- long-context
- active
---

# KronLSTM

## Method Overview
KronLSTM applies the Kronecker Delta Rule: a targeted association is revised by a rank-structured update along one matrix-space direction, reducing interference versus delta-rule memory writes and keeping the expected memory norm bounded without extra stabilizers.

## When to Use
- xLSTM / linear-attention long-context LM when delta-rule updates overwrite too much stored content.

## When NOT to Use
SSM default → `method:mamba-2`. Hybrid SSM decode buffer → `method:replayssm`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:mamba-2`.

## Gotchas & Failure Modes
- Not an LSTM trainer and not Mamba-2.
- Open weights on Hugging Face NX-AI/kronlstm.
