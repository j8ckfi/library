---
id: method:mrtpo
type: method
title: 'MRTPO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'Pearson covariance-norm multi-reward aggregation (CorrGRPO)'
  reason: 'CorrGRPO rescales correlated totals; MRTPO assigns each reward to tokens'
  use_instead: method:corrgrpo
- when: 'inverse-sqrt density on sparse rewards (DARA)'
  reason: 'DARA is group-density; MRTPO is token relevance'
  use_instead: method:dara
- when: 'single-turn dense math/code Pass@1 with one verifier'
  reason: 'CISPO remains Pass@1'
  use_instead: method:cispo
assumptions:
- 'Several verifiable rewards whose checkers look at different spans. Paper: SQL / IF / tool calling.'
- 'Code: zhaihaotian/MRTPO (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:mrtpo
recipes:
- recipe:mrtpo
claims:
- benchmark: 'Qwen2.5-Coder-7B-Instruct text-to-SQL execution accuracy average'
  metric: 'six-split SQL avg vs GDPO / GRPO'
  value: '73.15 vs GDPO 71.55 / GRPO 70.93; MRTPO+SAW 73.41'
  baseline: 'GDPO; GRPO; OPSD; GDPO+SAW (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.21439'
  notes: 'Does not retarget CorrGRPO/DARA as the multi-reward aggregation hop, or CISPO.'
tags:
- multi-reward
- credit-assignment
- rlvr
- active
---

# MRTPO

## Method Overview
Replay the same response with and without each verifier's information. Per-token Jensen-Shannon distance between those next-token distributions is the relevance weight that redistributes that reward's advantage.

## When to Use
- Multi-reward RLVR where format, executability, and match fire on different tokens.

## When NOT to Use
Correlation-scale aggregation → `method:corrgrpo`. Sparse-reward density → `method:dara`. Single verifier Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:multi-reward-rlvr` (`sota_for: []`). Does **not** replace CorrGRPO / DARA.

## Gotchas & Failure Modes
- Extra forward pass per reward for the leave-one-out replay.
- Orthogonal to SAW; combining them is reported, not a new default aggregator.

