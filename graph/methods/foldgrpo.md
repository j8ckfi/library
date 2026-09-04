---
id: method:foldgrpo
type: method
title: "Context-Folding + FoldGRPO"
category: "agent-recursion"
status: sota
sota_for:
  - task:long-horizon-tool-agent
supersedes: []
do_not_use_for:
  - when: "dumped corpus ≫ window"
    reason: "this folds trajectories, not a stuffed prompt"
    use_instead: "method:rlm"
  - when: "SWE harness without folding"
    reason: "ordinary issue-to-patch is mini-SWE-agent"
    use_instead: "method:mini-swe-agent"
  - when: "training async agent RL without folding"
    reason: "SAO is the train-policy default; FoldGRPO is folded long-horizon RL"
    use_instead: "method:sao"
  - when: "outcome-only long-horizon agent RL (signal starvation / drift or no checker)"
    reason: "FoldGRPO folds context; CANOPY/DRACO own that RL shelf"
    use_instead: "task:outcome-only-long-horizon-agent-rl"
  - when: "frontier-model SOTA vs GPT-5 ReAct"
    reason: "GPT-5 ReAct still ahead (0.793 / 0.718); this is 36B-class SOTA"
    use_instead: "method:foldgrpo"
  - when: "multi-agent as the long-horizon strategy"
    reason: "single folded agent, not MAS"
    use_instead: "method:single-agent-plus-tools"
assumptions:
  - "Seed-OSS-36B, 32K×10. Long tool/web/SWE trajectory, small active context."
  - "Open reimplementation: sunnweiwei/FoldAgent (may differ from paper train code)."
last_reviewed: "2026-09-01"
papers:
  - paper:foldgrpo
recipes:
  - recipe:foldgrpo
claims:
  - benchmark: "BrowseComp-Plus, Seed-OSS-36B, 32K×10"
    metric: "score"
    value: 0.620
    baseline: "ReAct 327K+GRPO 0.540 / ReAct 32K 0.286 / GPT-5 ReAct 0.793"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.11967"
    notes: "36B-class SOTA, not frontier-model SOTA. GPT-5 ReAct 0.793 still ahead."
  - benchmark: "SWE-Bench Verified, Seed-OSS-36B, 32K×10"
    metric: "resolved rate"
    value: 0.580
    baseline: "ReAct 327K+GRPO 0.574 / GPT-5 ReAct 0.718"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.11967"
    notes: "Folding vs huge ReAct context, not a mini-SWE-agent harness comparison."
tags:
  - agents
  - agent-recursion
  - foldgrpo
  - context-folding
  - sota
---

# Context-Folding + FoldGRPO

## Method Overview
Fold completed sub-trajectories so a long tool/web/SWE run keeps a 32K active window (Sun et al. 2510.11967). FoldGRPO is RL on that folded agent. Code: `https://github.com/sunnweiwei/FoldAgent`. This is **not** RLM (dumped prompt) and **not** the SWE harness default.

## When to Use
- Long horizon of tool calls with a small active context, 36B-class trained agent.

## When NOT to Use
- Dumped prompt → `method:rlm`. SWE loop without folding → `method:mini-swe-agent`. Async RL without folding → `method:sao`.

## Gotchas & Failure Modes
- GPT-5 ReAct still ahead (BrowseComp-Plus 0.793 / SWE-Bench Verified 0.718). Do not claim frontier-model SOTA.
- Open FoldAgent is a verl reimplementation and may differ from the paper's train code.
