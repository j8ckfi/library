---
id: method:rlvr-group-correlation
type: method
title: "RLVR Group Verifier Correlation"
category: "rl-alignment"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense Pass@1 RLVR algorithm"
    reason: "This is an analysis of within-group verifier errors, not a loss"
    use_instead: "method:cispo"
  - when: "group-relative magnitude rewarding lucky guesses"
    reason: "That gotcha is paper:spurious-advantage-grpo; this paper is verifier-error ICC"
    use_instead: "method:cispo"
assumptions:
  - "You already run group RLVR (GRPO/CISPO-family) with an automatic verifier. This node does not change the optimizer."
  - "Headline ρ is a pooled within-group ICC on Qwen2.5-1.5B k=8; it mixes prompt difficulty with shared answer form."
last_reviewed: "2026-09-09"
papers:
  - paper:rlvr-group-correlation
recipes:
  - recipe:rlvr-group-correlation
claims:
  - benchmark: "24,998 k=8 groups, Qwen2.5-1.5B, MATH/GSM8K/DeepMath-103K"
    metric: "pooled within-group verifier-error ICC"
    value: 0.530
    baseline: "independence (ρ=0) would give Kish n_eff=8"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.06386"
    notes: "95% CI [0.500, 0.560]. Kish n_eff=1.70. Not an optimizer."
  - benchmark: "Same corpus, four rule-based verifier configs"
    metric: "groups with at least one GRPO advantage-sign disagreement"
    value: "up to 0.83%"
    baseline: "independent verifier-error analyses"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.06386"
tags:
  - post-training
  - rlvr
  - verifier
  - gotcha
  - rlvr-group-correlation
  - niche
---

# RLVR Group Verifier Correlation

## Method Overview
Not an optimizer. Measure whether verifier errors inside a GRPO group are independent. They are not: pooled ICC ρ≈0.53 on 25k k=8 groups, Kish n_eff≈1.70. Use answer-form-aware analyses instead of a single aggregate error rate. Sibling gotcha: `paper:spurious-advantage-grpo` (lucky-guess magnitude). CISPO remains Pass@1.

## When to Use
- Reporting verifier noise, effective group size, or GRPO advantage robustness on math rollouts.
- Recipe hygiene: do not treat k=8 as eight independent verifier trials.

## When NOT to Use
- Choosing a train kernel → `method:cispo`. Lucky-guess magnitude → `paper:spurious-advantage-grpo`.

## Relation to Existing SOTA
- Niche analysis on `task:math-code-rl-dense`. Does **not** enter `current_sota`. Does **not** supersede CISPO or GRPO's retirement.

## Gotchas & Failure Modes
- ρ is marginal across prompts of varying difficulty; the paper does not separate difficulty from shared form.
- Advantage-sign flips are rare (≤0.83%) in this corpus; do not over-read that as "verifiers are interchangeable."
