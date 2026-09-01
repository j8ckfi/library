---
id: method:agentfold
type: method
title: "AgentFold"
category: "agent-recursion"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "dumped prompt offload"
    reason: "AgentFold folds web history, not a REPL variable"
    use_instead: "method:rlm"
  - when: "36B-class folded tool RL default"
    reason: "FoldGRPO is current_sota for this task"
    use_instead: "method:foldgrpo"
assumptions:
  - "Web-history fold. AgentFold-30B-A3B."
last_reviewed: "2026-09-01"
papers:
  - paper:agentfold
claims:
  - benchmark: "BrowseComp, AgentFold-30B-A3B"
    metric: "accuracy"
    value: 36.2
    baseline: "web-agent history without fold (paper)"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.24699"
    notes: "Active web-fold alternative. FoldGRPO remains task SOTA."
tags:
  - agents
  - agent-recursion
  - agentfold
  - web-agent
---

# AgentFold

## Method Overview
AgentFold (2510.24699) proactively folds web-agent history. Active on `task:long-horizon-tool-agent`. AgentFold-30B-A3B BrowseComp **36.2%**. FoldGRPO remains current_sota.

## When to Use
- Web browsing trajectories that need history compression.

## When NOT to Use
- Dumped prompt → `method:rlm`. Default folded-tool SOTA → `method:foldgrpo`.
