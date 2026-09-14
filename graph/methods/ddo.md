---
id: method:ddo
type: method
title: "DDO (Direct Diversity Optimization)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "open instruct / Dolci preference stack"
    reason: "DDO is successful-strategy coverage for sequential agents, not chat alignment"
    use_instead: "method:olmo-3"
  - when: "noisy pairwise chat preferences"
    reason: "PLC-DPO routes clean/flip/tie on DPO pairs; DDO needs divergence trees"
    use_instead: "method:plc-dpo"
  - when: "outcome-only long-horizon RL with a programmatic checker"
    reason: "CANOPY remains that first hop; DDO is offline preference coverage"
    use_instead: "method:canopy"
  - when: "labeled Pass@1 math/code RLVR"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Offline post-train. DTC collects state-aligned successful branches. RTO matches reference-relative target odds. Paper: BabyAI, BabaIsAI, WebShop. LoRA adapters."
  - "Code: koguma00/direct_diverse_optimization. Nine released DDO adapters. Base models from Hugging Face."
last_reviewed: "2026-09-14"
papers:
  - paper:ddo
recipes:
  - recipe:ddo
claims:
  - benchmark: "BabyAI / BabaIsAI / WebShop task success and successful-strategy coverage"
    metric: "success and coverage vs DPO / DivFreq / DivProb / TieDPO"
    value: "strongest among compared post-training methods"
    baseline: "DPO and decoding-time diversification; successful-only imitation"
    date: "2026-09-14"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.10052"
    notes: "Also highest recovery after local action replacement. Offline preference method, not CANOPY."
tags:
  - post-training
  - preference-alignment
  - diversity
  - agent
  - ddo
  - active
---

# DDO (Direct Diversity Optimization)

## Method Overview
Trajectory-level success labels collapse agents onto one working branch. DDO first builds Divergence-Tree Collection (DTC) branch sets at shared decision states, then trains with a Reference-Relative Target-Odds (RTO) objective so remaining successful alternatives keep probability mass.

## When to Use
- Sequential agents (web, grid, rule-worlds) where you care about covering multiple successful strategies under a fixed eval budget.

## When NOT to Use
- Chat stack → `method:olmo-3`. Noisy DPO pairs → `method:plc-dpo`. Checker long-horizon RL → `method:canopy`. Math Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- Active on `task:direct-preference-alignment` with a mention on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace OLMo-3, SimPO, CANOPY, or DRACO.

## Gotchas & Failure Modes
- Needs DTC artifacts (or `start_from: scratch` to collect them). Released ZIPs are separate from the git repo.
- Decoding-time diversification is a control, not a substitute for RTO.
