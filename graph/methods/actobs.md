---
id: method:actobs
type: method
title: "ActObs (Observation-Token SFT before GRPO)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "variable tool latency / async stragglers is the bottleneck"
    reason: "SAO remains the async algorithm; ActObs is an SFT initialization that changes later GRPO exploration"
    use_instead: "method:sao"
  - when: "build a SWE / issue-to-patch harness rather than train a policy"
    reason: "mini-SWE-agent is the loop; ActObs trains on observation tokens inside traces"
    use_instead: "method:mini-swe-agent"
  - when: "outcome-only long-horizon coverage / anti-drift"
    reason: "CANOPY remains that protocol; ActObs is SFT+GRPO exploration on terminal/code agents"
    use_instead: "method:canopy"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; ActObs is agent-trace SFT"
    use_instead: "method:cispo"
assumptions:
  - "You have agent trajectories that already include environment observation tokens. SFT then GRPO (paper). No extra sequence tokens at train or serve time."
  - "Paper: Qwen3-4B/8B. Terminal-Bench 2.0 and aider-polyglot (the latter unseen in SFT/RL)."
  - "No official GitHub as of 2026-09-18."
last_reviewed: "2026-09-18"
papers:
  - paper:actobs
recipes:
  - recipe:actobs
claims:
  - benchmark: "Terminal-Bench 2.0, Qwen3-4B, GRPO after SFT"
    metric: "pass@k vs action-only SFT then GRPO"
    value: "higher pass@k at every evaluated sampling budget"
    baseline: "action-only SFT (observations as context, loss on actions)"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20715"
    notes: "Abstract. SFT metrics are similar; the split appears after GRPO. Not a SAO bake-off."
  - benchmark: "Terminal-Bench 2.0, Qwen3-8B, GRPO after SFT"
    metric: "pass@16"
    value: "+3.4 pp vs action-only; more distinct tasks"
    baseline: "action-only SFT then GRPO (higher pass@1, lower pass@k)"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20715"
    notes: "Trades some pass@1 reliability for coverage. Entropy stays higher; policy moves less from the SFT init."
  - benchmark: "aider-polyglot, Qwen3-4B (unseen in SFT and RL)"
    metric: "pass@1"
    value: "+4.2 pp vs action-only"
    baseline: "action-only SFT then GRPO"
    date: "2026-09-17"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.20715"
    notes: "Cross-domain code editing transfer."
tags:
  - post-training
  - agentic
  - sft
  - observation
  - actobs
  - active
---

# ActObs (Observation-Token SFT before GRPO)

## Method Overview
ActObs is SFT on the observation tokens that already sit in agent traces, not only on action tokens. The deployed policy still samples actions; predicting observations is a train-time consequence model. After SFT the two inits look similar. After GRPO they do not: ActObs explores more (higher entropy, less policy drift from the SFT checkpoint) and raises pass@k. Action-only SFT leaves a residual observation gradient and can make environment prediction worse than the base model.

## When to Use
- Tool/terminal agents where you already log observations and the next stage is GRPO-family RL.

## When NOT to Use
- Async stragglers → `method:sao`. SWE harness → `method:mini-swe-agent`. AppWorld coverage → `method:canopy`. Pass@1 math → `method:cispo`.

## Relation to Existing SOTA
- Active plug-in on `task:agentic-async-rl`. Mentions on `task:software-engineering-agent-harness` and `task:outcome-only-long-horizon-agent-rl`. Does **not** enter `current_sota`. Does **not** supersede `method:sao`, `method:mini-swe-agent`, or `method:canopy`.

## Gotchas & Failure Modes
- Do not judge the method at the SFT checkpoint. The paper's split is after GRPO.
- Qwen3-8B gives up some pass@1 for pass@k. Measure the budget you actually serve.
- No public trainer as of 2026-09-18.
