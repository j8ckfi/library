---
id: method:repetition-count-selection
type: method
title: "Repetition-Count Selection"
category: "data-curriculum"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "open unique-data mix, not a finite target fraction mixed with generic data"
    reason: "OLMo-3 remains the open mix"
    use_instead: "method:olmo-3"
  - when: "MoE sparsity x data-repetition overfit"
    reason: "That gotcha is moe-data-repetition, not a dense r-shortlist"
    use_instead: "method:moe-data-repetition"
  - when: "pricing a repeated token vs fresh data / critical epoch geometry"
    reason: "That is repeated-token-worth on the same task"
    use_instead: "method:repeated-token-worth"
assumptions:
  - "Finite target corpus mixed with generic data at a fixed target fraction. Paper: Wikipedia-derived, Proof-Pile-2, PubMed, Caselaw; 200M and 520M."
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:repetition-count-selection
recipes:
  - recipe:repetition-count-selection
claims:
  - benchmark: "520M Proof-Pile-2 repetition-count ranking"
    metric: "loss at r=8 vs r=16"
    value: "r=8 beats r=16 with fewer training tokens"
    baseline: "r=16"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05126"
    notes: "Rankings reverse with scale. Dual-active with repeated-token-worth. Does not retarget OLMo-3."
tags:
  - pretraining
  - data-curriculum
  - repetition-count-selection
  - active
---

# Repetition-Count Selection

## Method Overview
When a finite target corpus is mixed with generic data at a fixed fraction, the best repetition count r can reverse as the model grows. Train small proxies, keep a shortlist of r that still look good, and evaluate that shortlist at the target scale rather than transferring a single r.

## When to Use
- Data-constrained pretrain with a finite target source mixed into generic data, and you will train more than one scale.

## When NOT to Use
- Open unique mix → `method:olmo-3`. MoE × repeats → `method:moe-data-repetition`. Token-value / critical-epoch geometry → `method:repeated-token-worth`.

## Relation to Existing SOTA
- Dual-active first hop on `task:data-constrained-pretrain` with `method:repeated-token-worth`. Method `sota_for` stays empty. Does **not** replace OLMo-3.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Do not copy r from a  small run; rankings reverse.
- Candidate retention is not exact point prediction of r.
