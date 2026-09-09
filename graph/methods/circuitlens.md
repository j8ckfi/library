---
id: method:circuitlens
type: method
title: "CircuitLens"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the dense Pass@1 RLVR default"
    reason: "CRS is a data-selection signal; CISPO remains the loss"
    use_instead: "method:cispo"
  - when: "zero-rollout difficulty prior for silent GRPO groups"
    reason: "ThinkPrior is a Beta learnability prior, not circuit engagement"
    use_instead: "method:thinkprior"
  - when: "you need a data policy that beats uniform GRPO at 95% CI"
    reason: "DataFlex-RL finds no such policy in its controlled setting"
    use_instead: "method:dataflex-rl"
assumptions:
  - "Paper: Qwen2.5-Math-7B, 46 contrastive-ablation heads, one frozen forward. EMNLP 2026 Findings."
  - "Low-engagement is the 7B medium-math finding, not a universal ranking."
last_reviewed: "2026-09-09"
papers:
  - paper:circuitlens
recipes:
  - recipe:circuitlens
claims:
  - benchmark: "Qwen2.5-Math-7B, lowest-CRS decile vs random"
    metric: "pp vs random on GSM8K / OlympiadBench / Minerva"
    value: "+2.0 / +1.6 / +2.9"
    baseline: "random selection; highest-engagement decile ≈ middle"
    date: "2026-09-09"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.07183"
    notes: "EMNLP 2026 Findings. Counterintuitive. Fails to separate on a domain-curated pool; 1.5B reverses direction."
tags:
  - post-training
  - rlvr
  - interpretability
  - circuitlens
  - active
---

# CircuitLens

## Method Overview
CircuitLens ranks RLVR problems by Circuit Reasoning Score from a small set of reasoning-sensitive heads on the frozen base. On 7B medium math, **low** engagement wins. This is not ThinkPrior (pass-rate prior) and not a CISPO replacement. DataFlex-RL is the reminder that data policies often fail to beat uniform.

## When to Use
- Exploring model-conditioned data selection on Qwen2.5-Math-7B-class models.

## When NOT to Use
- Pass@1 kernel → `method:cispo`. Silent-group prior → `method:thinkprior`.
- Do not ship "always take the top CRS decile."

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-dense`. Does **not** supersede CISPO, ThinkPrior, or DataFlex-RL.

## Gotchas & Failure Modes
- 1.5B scale flips the useful direction. Domain-curated pools: no method separates.
- Lowest-reward training condition generalized best in the paper — another warning against a static ranking.
