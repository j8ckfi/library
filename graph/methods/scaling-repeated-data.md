---
id: method:scaling-repeated-data
type: method
title: Scaling Repeated-Data Pretraining
category: data-curriculum
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: unique-token epoch pricing rather than batch/regularization under repeats
  reason: Repeated-Token Worth remains the dual-active first hop for epoch value
  use_instead: method:repeated-token-worth
- when: open web / Dolma-3 mix with unique data not binding
  reason: OLMo-3 remains the open mix
  use_instead: method:olmo-3
assumptions:
- Finite unique-token dense NTP. Paper reports 153M and 1.5B multi-epoch runs.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:scaling-repeated-data
recipes:
- recipe:scaling-repeated-data
claims:
- benchmark: 1.5B and 153M dense multi-epoch CE
  metric: val CE; useful epochs before overfitting
  value: 1.5B B=64 vs 512 CE 3.124→2.977; tying+emb WD 2.971→2.946 at B=64; epochs
    20→32 (1.5B) and 112→240 (153M)
  baseline: large-batch multi-epoch without packing/tying/emb WD (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.15965
  notes: Does not retarget Repeated-Token Worth / Repetition-Count Selection / OLMo-3.
tags:
- pretraining
- data-constrained
- batch-size
- active
---

# Scaling Repeated-Data Pretraining

## Method Overview
Under multi-epoch replay, increase the number of optimizer steps per unique token by shrinking batch size, and delay overfitting with per-epoch packing, weight tying, and positive embedding weight decay.

## When to Use
- Unique data is binding and you are already in the multi-epoch regime; pick batch size and regularization, not only r.

## When NOT to Use
Open unique-rich mix → `method:olmo-3`. Epoch-value pricing → `method:repeated-token-worth`. Repetition-count shortlist → `method:repetition-count-selection`.

## Relation to Existing SOTA
Active plug-in on `task:data-constrained-pretrain` (`sota_for: []`). Does **not** replace Repeated-Token Worth or Repetition-Count Selection.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Smaller batches raise GPU-time; the paper's packing recovers some wall-clock, not all.
- U-shape is multi-epoch; do not import a single-epoch large-batch default.
