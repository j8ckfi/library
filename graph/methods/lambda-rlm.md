---
id: method:lambda-rlm
type: method
title: "λ-RLM"
category: "agent-recursion"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "default dumped-prompt offload"
    reason: "RLM depth=1 is current_sota"
    use_instead: "method:rlm"
assumptions:
  - "Niche λ-calculus / Y-combinator framing (2603.20105). Recursion depth >1 is still not default."
last_reviewed: "2026-09-01"
papers:
  - paper:lambda-rlm
claims:
  - benchmark: "long-context rot / recursive offload (niche)"
    metric: "status"
    value: "niche alternative to RLM"
    baseline: "RLM depth=1"
    date: "2026-03"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2603.20105"
    notes: "Does not replace method:rlm."
tags:
  - agents
  - agent-recursion
  - lambda-rlm
  - niche
---

# λ-RLM

## Method Overview
Niche recursive offload (2603.20105). RLM remains current_sota for dumped prompts. Depth >1 is still not the working setting.

## When to Use
- Research on λ-calculus-style recursive LM calls.

## When NOT to Use
- Default long-context offload → `method:rlm`.
