---
id: method:opsft
type: method
title: "OPSFT"
category: "data-curriculum"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "general chat / instruct SFT without an on-policy update-direction constraint"
    reason: "OLMo-3 Dolci remains the instruct default; OPSFT projects SFT onto the on-policy parameter direction"
    use_instead: "method:olmo-3"
  - when: "single-turn dense math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; OPSFT is cheaper SFT that can match or beat GRPO on DeepMath, not a CISPO replacement"
    use_instead: "method:cispo"
  - when: "MCMC projection sampling of expert traces then ordinary SFT"
    reason: "Sampling SFT rewrites traces then does vanilla SFT; OPSFT changes the SFT update direction"
    use_instead: "method:sampling-sft"
assumptions:
  - "SFT host that can compute an on-policy gradient (current-model NLL on its own samples or a projection of the SFT step onto that direction). Paper: Qwen3-4B/8B DeepMath."
  - "Official code ssfgunner/OPSFT released as of 2026-10-05."
last_reviewed: "2026-10-05"
papers:
  - paper:opsft
recipes:
  - recipe:opsft
claims:
  - benchmark: "Qwen3-4B DeepMath mean"
    metric: "mean score"
    value: "40.11"
    baseline: "GRPO 38.96 / SFT 34.22 (6.4 h vs GRPO 16.5 h)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36659"
    notes: "Not a CISPO Pass@1 retarget. Post-GRPO continue 38.96→41.36 vs SFT drop 36.25."
  - benchmark: "Qwen3-8B DeepMath mean"
    metric: "mean score"
    value: "41.67"
    baseline: "GRPO 40.31 / SFT 38.41"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.36659"
    notes: "Same DeepMath table."
tags:
  - post-training
  - sft
  - opsft
  - active
---

# OPSFT

## Method Overview
The paper's claim is that post-training generalization follows the *parameter update direction* relative to the on-policy gradient, not whether the tokens were sampled on-policy. OPSFT is the usable SFT variant: take a supervised step, then keep the component aligned with the current model's on-policy gradient (or train SFT under that constraint). Vanilla SFT after GRPO can drop; OPSFT can continue.

## When to Use
- Instruct or math SFT where vanilla SFT generalizes worse than GRPO and you can afford an on-policy gradient projection.

## When NOT to Use
- Instruct default → `method:olmo-3`. Pass@1 RLVR → `method:cispo`. MCMC trace projection then vanilla SFT → `method:sampling-sft`.

## Relation to Existing SOTA
- Active plug-in on `task:instruct-sft-alignment` beside OLMo-3, with a mention on `task:math-code-rl-dense` (`sota_for: []`). Does **not** enter either `current_sota`. Does **not** replace OLMo-3 or CISPO.

## Gotchas & Failure Modes
- Do not headline “SFT beats GRPO” without the on-policy-direction constraint. Vanilla SFT is 34.22 vs GRPO 38.96 on Qwen3-4B DeepMath.
- Sampling SFT is a different projection (traces, not parameter steps).
