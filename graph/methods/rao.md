---
id: method:rao
type: method
title: "Recursive Agent Optimization (RAO)"
category: "agent-recursion"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "drop-in RLM replacement for dumped prompts"
    reason: "RAO trains root+children recursion; RLM is inference REPL offload"
    use_instead: "method:rlm"
  - when: "SWE harness"
    reason: "not a bash loop"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Trained recursion (root + children). TextCraft-Synth 8K numbers only."
last_reviewed: "2026-09-01"
papers:
  - paper:rao
claims:
  - benchmark: "TextCraft-Synth 8K"
    metric: "success %"
    value: 95
    baseline: "single-agent 24%"
    date: "2026-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2605.06639"
    notes: "Trained recursion, not inference RLM."
tags:
  - agents
  - agent-recursion
  - rao
---

# Recursive Agent Optimization (RAO)

## Method Overview
RAO (2605.06639) *trains* a recursive agent (root + children). TextCraft-Synth 8K: single-agent 24% vs recursive 95%. Active on `task:long-horizon-tool-agent`. Not a drop-in RLM replacement.

## When to Use
- You will train recursive root/child agents on a synthetic environment like TextCraft.

## When NOT to Use
- Dumped prompt → `method:rlm`. SWE loop → `method:mini-swe-agent`.
