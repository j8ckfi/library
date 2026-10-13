---
id: method:msar
type: method
title: MSAR (Multi-Stream Attention Residuals)
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: choosing the ~7B dense pretrain optimizer
  reason: MSAR is a residual topology; Muon2 remains the optimizer default and composes
    with it
  use_instead: method:muon2
- when: widened Birkhoff residual streams as used in DeepSeek-V4
  reason: mHC remains the Sinkhorn hyper-connection; MSAR is a single-paper residual
    bake-off
  use_instead: method:mhc
assumptions:
- MoE pretrain at 18B and 28B in the paper. Composes with Muon2.
- 'Code: jianke0604/MSAR (code_status: released).'
last_reviewed: '2026-10-13'
papers:
- paper:msar
recipes:
- recipe:msar
claims:
- benchmark: 18B and 28B MoE, 12 downstream benchmarks
  metric: downstream vs vanilla / mHC / AttnRes; iso-loss compute speedup
  value: beats vanilla/mHC/AttnRes; iso-loss 1.58× vs 1.35× AttnRes, 1.30× mHC
  baseline: vanilla residual; mHC; AttnRes (single-paper)
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13630
  notes: '18B train loss 1.750 vs Vanilla 1.799 / mHC 1.776 / AttnRes 1.769. No supersedes
    edge: single-paper baselines.'
tags:
- pretraining
- residuals
- msar
- active
---

# MSAR (Multi-Stream Attention Residuals)

## Method Overview
Split the residual stream and mix streams with attention residuals. Drop-in for standard Pre-LN residuals, mHC, and AttnRes. Composes with Muon2.

## When to Use
- MoE (or dense) pretrain where you want a residual topology bake-off against vanilla / mHC / AttnRes.

## When NOT to Use
Optimizer choice → `method:muon2`. DeepSeek-V4 Stream mixing via Sinkhorn → `method:mhc`. Content-dependent skip over layer history → `method:attnres`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` beside `method:attnres` and `method:mhc` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Muon2, mHC, or AttnRes.

## Gotchas & Failure Modes
- **code: released** jianke0604/MSAR as of 2026-10-13.
- Baselines are this paper's vanilla / mHC / AttnRes reimplementation. No library supersession.
- 28B overhead is small (+0.5% FLOPs / +0.3% activated params) but not free.
