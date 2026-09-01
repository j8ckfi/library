---
id: method:live-swe-agent
type: method
title: "Live-SWE-agent"
category: "agent-harness"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "default SWE harness"
    reason: "self-evolving is niche; mini remains the locked design"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Self-evolving SWE agent. Official JSON 79.2% is a tie with Claude 4.5 Opus, not mini's 76.8% and not vals.ai 97%."
last_reviewed: "2026-09-01"
papers:
  - paper:live-swe-agent
claims:
  - benchmark: "SWE-bench Verified (official JSON)"
    metric: "resolved %"
    value: 79.2
    baseline: "tie with Claude 4.5 Opus on official JSON; not vals.ai 97%"
    date: "2025-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2511.13646"
    notes: "Do not mix 79.2% with mini 76.8% or vals.ai 97.00%."
tags:
  - agents
  - agent-harness
  - live-swe-agent
  - niche
---

# Live-SWE-agent

## Method Overview
Self-evolving software-engineering agent (2511.13646). Niche on `task:software-engineering-agent-harness`. Ties official JSON 79.2% with Claude 4.5 Opus. Default remains mini-SWE-agent.

## When to Use
- Research on on-the-fly SWE-agent self-evolution.

## When NOT to Use
- Default harness / locked board → `method:mini-swe-agent`.
