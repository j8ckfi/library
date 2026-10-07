---
id: method:hierarchical-moe-routing-control
type: method
title: "Hierarchical MoE Routing Control"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the MoE/VL RLVR loss"
    reason: "This constrains expert routing by agent operation type; SAPO remains the MoE/VL algorithm"
    use_instead: "method:sapo"
  - when: "rollout-side noisy expert-space exploration"
    reason: "ESRL perturbs routing like temperature; this aligns experts to operation types"
    use_instead: "method:esrl"
  - when: "MoE post-train router soft-anchor to the base prior"
    reason: "RPB anchors the live router; this is hierarchical operation-type control"
    use_instead: "method:rpb"
  - when: "AppWorld coverage / anti-drift rather than MoE routing during RL"
    reason: "CANOPY remains outcome-only coverage"
    use_instead: "method:canopy"
assumptions:
  - "MoE policy under agentic RL. Paper: Qwen3-30B-A3B on AppWorld / AutomationBench. No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:hierarchical-moe-routing-control
recipes:
  - recipe:hierarchical-moe-routing-control
claims:
  - benchmark: "AppWorld / AutomationBench, Qwen3-30B-A3B"
    metric: "success-rate lift vs unconstrained MoE RL"
    value: ">10 points"
    baseline: "unconstrained expert routing during agentic RL"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07332"
    notes: "Align experts with agent operation types; constrain routing during RL. Beside ESRL / RPB. Does not replace SAPO or CANOPY."
tags:
  - post-training
  - moe
  - routing
  - agentic
  - hierarchical-moe-routing-control
  - active
---

# Hierarchical MoE Routing Control

## Method Overview
During agentic RL on an MoE, align experts with operation types (tool call vs plan vs observation) and constrain routing instead of leaving the pretrained router free.

## When to Use
- MoE agent RL where routing ignores operation type.

## When NOT to Use
- MoE/VL loss → `method:sapo`. Rollout exploration → `method:esrl`. Router prior bias → `method:rpb`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
- Active plug-in on `task:math-code-rl-moe` with a mention on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** replace SAPO, ESRL, RPB, or CANOPY.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- >10-point success is not a CANOPY TGC bake-off.
