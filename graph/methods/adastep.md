---
id: method:adastep
type: method
title: "AdaStep"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "structural credit split for tool-call vs natural-language-summary tokens"
    reason: "SLCA-GRPO remains that task's first hop; AdaStep shrinks GiGPO-style step advantages, it does not split tool vs summary tokens"
    use_instead: "method:slca-grpo"
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains outcome-only coverage; AdaStep is a step-credit shrink on GiGPO groups"
    use_instead: "method:canopy"
  - when: "variable environment latency / async stragglers, not step-credit noise"
    reason: "SAO remains async RL; AdaStep assumes grouped step returns already exist"
    use_instead: "method:sao"
assumptions:
  - "GiGPO-style grouping of state–action pairs that share an anchor state. Trajectory-level group advantage is kept; only the local correction is shrunk."
  - "Paper: Qwen3-1.7B / 4B and Qwen2.5-7B-Instruct on ALFWorld, WebShop, ScienceWorld."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:adastep
recipes:
  - recipe:adastep
claims:
  - benchmark: "Qwen3-1.7B Δ vs GiGPO (ALFWorld In/Out, WebShop Seen/Unseen, ScienceWorld)"
    metric: "success-rate points"
    value: "+2.60 / +1.73 / +0.75 / +0.66 / +9.36"
    baseline: "GiGPO (Feng et al. 2025)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03223"
    notes: "Paper Δ row. Not a CANOPY AppWorld TGC retarget. Not SLCA-GRPO."
  - benchmark: "Qwen3-4B ALFWorld In / Out / WebShop Seen / Unseen / ScienceWorld"
    metric: "success rate"
    value: "93.01 / 86.58 / 88.76 / 80.27 / 48.70"
    baseline: "GiGPO 88.02 / 83.07 / 87.34 / 78.28 / 46.67 (Δ +4.99 / +3.51 / +1.42 / +1.99 / +2.03)"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03223"
    notes: "Same table. HGPO is not a library method."
tags:
  - post-training
  - rl-alignment
  - agentic
  - adastep
  - active
---

# AdaStep

## Method Overview
GiGPO adds a fixed-weight step-level relative advantage to the trajectory-level group advantage. AdaStep keeps the trajectory term and multiplies the local correction by a per-state shrinkage coefficient: estimated signal variance over total return variance in that step-level group. When later actions or the environment dominate the return, the coefficient goes toward zero; when the chosen action explains the return, it stays near one.

## When to Use
- Agentic RL that already groups shared states (GiGPO-style) and the step correction is noisy.

## When NOT to Use
- Tool vs summary token split → `method:slca-grpo`. Sparse outcome coverage with a checker → `method:canopy`. Async stragglers → `method:sao`.

## Relation to Existing SOTA
- Active plug-in on `task:tool-agent-segment-credit` beside SLCA-GRPO, with a mention on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** enter either `current_sota`. Does **not** replace SLCA-GRPO or CANOPY.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- Needs GiGPO-style grouping; it is not a drop-in on CANOPY same-task groups or SLCA tool/summary masks.
- GiGPO / HGPO are paper hosts/baselines, not library SOTA retargets.
