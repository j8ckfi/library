---
id: method:dial-opd
type: method
title: "DIAL-OPD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the single-teacher distillation algorithm"
    reason: "DIAL-OPD is a keep-mask on sampled-token OPD, not a new distill default"
    use_instead: "method:opd"
  - when: "sparse OPD token selection by gradient-estimation reliability (IER)"
    reason: "IER-OPD ranks gradient SNR; DIAL-OPD downweights low-low probability mass"
    use_instead: "method:ier-opd"
  - when: "usefulness keep-mask of 1-2 tokens per trajectory"
    reason: "Sparse OPD supervision is a usefulness mask; DIAL-OPD is probability-space scoring"
    use_instead: "method:sparse-opd-supervision"
  - when: "bilevel learned token weights from post-update validation loss"
    reason: "MetaOPD learns the map; DIAL-OPD is a closed-form keep-score"
    use_instead: "method:metaopd"
  - when: "verifiable labels exist and the goal is Pass@1 RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Host is sampled-token reverse-KL OPD. Paper: four teacher-student pairs, seven math benchmarks."
  - "Code: EIT-NLP/DIAL-OPD (`code_status: released`)." 
last_reviewed: "2026-10-09"
papers:
  - paper:dial-opd
recipes:
  - recipe:dial-opd
claims:
  - benchmark: "Sampled-token OPD, 40% token budget vs full-token Vanilla OPD"
    metric: "seven-benchmark mean accuracy lift"
    value: "up to +5.25pp at 40% tokens; Pass@16 13.33→26.67"
    baseline: "Vanilla OPD (100% tokens); disagreement keep-masks at matched retention"
    date: "2026-10-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.11659"
    notes: "4B teacher with DIAL-OPD can beat 8B teacher full-token OPD. Does not retarget OPD." 
tags:
  - post-training
  - distillation
  - opd
  - token-selection
  - dial-opd
  - active
---

# DIAL-OPD

## Method Overview
Score each sampled token by |log-ratio reward| times the logarithmic mean of teacher and student probabilities of that token. β interpolates log-space vs probability-space. Keep the top fraction. Drop low-low tokens that inflate log-ratios while carrying no mass.

## When to Use
- Sampled-token OPD where full-token or disagreement-only masks overfit low-low tokens.

## When NOT to Use
- Default matching → `method:opd`. IER SNR mask → `method:ier-opd`. Usefulness 1-token mask → `method:sparse-opd-supervision`. Learned bilevel weights → `method:metaopd`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace OPD, IER-OPD, sparse-opd-supervision, or MetaOPD.

## Gotchas & Failure Modes
- **code: released** EIT-NLP/DIAL-OPD as of 2026-10-09.
- β is a real HP. Reward magnitude alone is not the keep-score.
