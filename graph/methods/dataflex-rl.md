---
id: method:dataflex-rl
type: method
title: "DataFlex-RL"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the Pass@1 RLVR loss"
    reason: "DataFlex-RL is an evaluation of data policies under GRPO, not a loss"
    use_instead: "method:cispo"
  - when: "cold-start silent-group waste is the metric (not final accuracy)"
    reason: "ThinkPrior cuts early waste without claiming accuracy; DataFlex is the accuracy-null"
    use_instead: "method:thinkprior"
assumptions:
  - "Qwen2.5-7B-Base, 12 seeds, 12-bench domain-balanced summary. GRPO recipe. Llama-3.1-8B-Base extension."
last_reviewed: "2026-09-09"
papers:
  - paper:dataflex-rl
recipes:
  - recipe:dataflex-rl
claims:
  - benchmark: "Qwen2.5-7B-Base, 12 matched seeds, 12-bench domain-balanced average"
    metric: "accuracy delta vs untrained / vs uniform"
    value: "uniform +7.76 pp vs untrained; no selection method 95% CI vs uniform excludes 0"
    baseline: "uniform GRPO"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.06107"
    notes: "Negative result. Math-heavy 6-bench ranking vs 12-bench r=−0.33."
tags:
  - post-training
  - rlvr
  - data-policy
  - dataflex-rl
  - active
---

# DataFlex-RL

## Method Overview
DataFlex-RL is a **negative-result evaluation platform**: under a shared GRPO recipe, RLVR data policies do not beat uniform sampling at 95% CI. Read it next to ThinkPrior (waste, not accuracy) and CircuitLens (regime-dependent selection). Does not replace CISPO.

## When to Use
- Before adopting a clever RLVR data policy as an accuracy win. Demand paired CIs and a domain-balanced summary.

## When NOT to Use
- As a training algorithm. Pass@1 → `method:cispo`. Silent-group waste → `method:thinkprior`.

## Relation to Existing SOTA
- Active note on `task:math-code-rl-dense`. Does **not** supersede anyone. Does not demote ThinkPrior (different metric).

## Gotchas & Failure Modes
- A math-only 6-bench ranking can invert the 12-bench ranking (r=−0.33).
