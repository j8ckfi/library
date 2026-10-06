---
id: task:data-constrained-pretrain
type: task
title: "Data-Constrained Pretraining (Epoch / Repetition Geometry)"
domain: "pretraining"
summary: "How many times to replay a finite unique-token budget during dense NTP pretraining: token-value vs fresh data, and which repetition counts transfer across model scales."
scope: "Unique-data-constrained dense pretrain epoch/repetition schedules. Dual-active first hops are Repeated-Token Worth (pricing / critical epoch) and Repetition-Count Selection (r shortlists that reverse with scale). Not the open mix, not the 7B optimizer, not the MoE sparsity×repeat gotcha."
out_of_scope:
  - "Open multi-trillion-token web / Dolma mix when unique data are not binding (OLMo-3)"
  - "~7B dense NTP optimizer (Muon2)"
  - "MoE sparsity × data-repetition overfit (MoE data-repetition)"
  - "Fully synthetic single-stage pretrain from Wikipedia/Wikibooks seeds (SYNTH)"
  - "Zero-natural-data self-play pretrain (UTM programs)"
redirects:
  - when: "open pretrain mix / Dolma-3 recipe rather than unique-token epoch geometry"
    to: "task:open-data-recipe"
  - when: "choosing the ~7B dense pretrain optimizer"
    to: "task:llm-pretraining-optimization"
  - when: "MoE sparsity × data-repetition overfit (not dense epoch pricing)"
    to: "method:moe-data-repetition"
  - when: "fully synthetic single-stage LLM pretraining from Wikipedia/Wikibooks seeds"
    to: "task:synthetic-single-stage-pretrain"
  - when: "zero-natural-data self-play pretraining (generator proposes UTM programs)"
    to: "task:zero-natural-data-self-play-pretrain"
current_sota:
  - method: method:repeated-token-worth
    as_of: "2026-10-06"
    benchmark: "multi-epoch dense pretrain, unique data fixed"
    metric: "repeated-token value vs fresh; epochs at 127M vs 2B"
    value: "second epoch nearly as valuable as fresh; ~15 epochs at 127M to ~4 at 2B"
    notes: "Repeated-Token Worth (2610.05591). Dual-active with repetition-count-selection. Method status active. Does not replace OLMo-3 / Muon2 / MoE data-repetition."
  - method: method:repetition-count-selection
    as_of: "2026-10-06"
    benchmark: "520M Proof-Pile-2 repetition-count ranking"
    metric: "loss at r=8 vs r=16"
    value: "r=8 beats r=16 with fewer training tokens"
    notes: "Repetition-Count Selection (2610.05126). Rankings reverse with scale. Dual-active with repeated-token-worth. Method status active. Does not replace OLMo-3."
methods:
  - method:repeated-token-worth
  - method:repetition-count-selection
  - method:olmo-3
  - method:moe-data-repetition
  - method:muon2
last_reviewed: "2026-10-06"
tags:
  - pretraining
  - data-curriculum
  - data-repetition
  - data-constrained
---

# Data-Constrained Pretraining (Epoch / Repetition Geometry)

## Problem Definition
When unique pretrain tokens are the bottleneck, extra epochs and a chosen repetition count `r` change loss as much as the mix recipe. This task owns **how to price and select repeats**, not which web mix to use and not the 7B optimizer.

This is **not** OLMo-3 / Dolma-3, not Muon2, and not the MoE sparsity × repetition gotcha.

## Evaluation Protocol
- **Primary Benchmarks**: multi-epoch NTP loss vs one epoch on the same data and vs fresh data at equal compute; target-corpus `r` rankings that reverse with model scale (Proof-Pile-2 / Wikipedia-derived / PubMed / Caselaw).
- **Evaluation Pitfalls**: Consecutive shard replay is not shuffled repeats (up to +0.46 bits/byte). Do not copy a single small-model `r` to a larger model. The two first hops have **no head-to-head**; they fix different residuals (token-value geometry vs scale-dependent `r` shortlists).

## SOTA Recommendation (as of 2026-10-06)
- **Primary (token value / critical epoch, this task only)**: **Repeated-Token Worth** (`method:repeated-token-worth`, `paper:repeated-token-worth` `arXiv:2610.05591`). Status `active`. Dual-active with Repetition-Count Selection.
- **Primary (r shortlist across scales, this task only)**: **Repetition-Count Selection** (`method:repetition-count-selection`, `paper:repetition-count-selection` `arXiv:2610.05126`). Status `active`. Dual-active with Repeated-Token Worth.
- **Not This Task**: `method:olmo-3` remains the open mix; `method:muon2` remains the 7B optimizer; `method:moe-data-repetition` remains the MoE sparsity gotcha.
