---
id: task:web-search-agent-rl
type: task
title: "Web Search Agent Training"
domain: "post-training"
summary: "Train a live-web multi-hop search policy: reverse-constructed hyperlink tasks, filtered SFT, live-search RL, and SFT-RL climbing. Not AppWorld coverage, not async stragglers, not a SWE harness."
scope: "Policy training for ReAct search agents (search/scrape against the live web) with synthetic multi-hop tasks, trajectory/turn filtering, in-cluster judge/summarizer, and iterative SFT-RL climbing."
out_of_scope:
  - "AppWorld / outcome-only long-horizon coverage and anti-drift (CANOPY / DRACO)"
  - "Async tool-latency / straggler RL (SAO)"
  - "SWE issue-to-patch harness (mini-SWE-agent)"
  - "Folding a long tool trajectory into a small active context (FoldGRPO)"
  - "Single-turn dense math/code RLVR (CISPO)"
redirects:
  - when: "outcome-only long-horizon agent RL (AppWorld coverage / anti-drift or rubric credit)"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "variable environment latency / async stragglers, not search-agent climbing"
    to: "task:agentic-async-rl"
  - when: "build a SWE / issue-to-patch harness rather than train a search policy"
    to: "task:software-engineering-agent-harness"
  - when: "the problem is context folding of a long tool trajectory, not the search train recipe"
    to: "task:long-horizon-tool-agent"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
current_sota:
  - method: method:iris
    as_of: "2026-09-08"
    benchmark: "BrowseComp / BrowseComp-ZH / DeepSearchQA / HLE-text, discard-all CM, open-source same-size"
    metric: "accuracy / F1 (DeepSearchQA)"
    value: "Iris-mini 82.2/84.8/86.9/52.3; Iris-pro 88.6/85.1/92.9/56.4"
    notes: "Iris (2609.04304). Strongest overall among reported open-source search agents in the 30-35B and ~400B ranges with CM. Does not replace CANOPY, SAO, mini-SWE-agent, FoldGRPO, or CISPO. DeepSearchQA mini loses to Aquila-mini 89.5. Frontier (Kimi-K3 91.2 BrowseComp) still ahead."
methods:
  - method:iris
  - method:sao
  - method:canopy
  - method:foldgrpo
  - method:mini-swe-agent
  - method:cispo
last_reviewed: "2026-09-08"
tags:
  - post-training
  - agentic
  - web-search
  - sft-rl-climbing
  - iris
---

# Web Search Agent Training

## Problem Definition
Train a single ReAct search agent that must decide what to search, how to read retrieved pages, when to continue, and when evidence is enough. Tasks are hard multi-hop web questions (often reverse-constructed from a hyperlink graph). Failure modes of nearby shelves: AppWorld coverage RL, async straggler replay, SWE harness choice, or trajectory folding without a search data recipe.

## Evaluation Protocol
- **Primary Benchmarks**: BrowseComp, BrowseComp-ZH (accuracy); DeepSearchQA (F1); HLE text-only (accuracy). Pass@1, one rollout, official LLM judge.
- **Evaluation Pitfalls**: Report with and without context management under a fixed tool set / context / judge. Do not mix discard-all + retry with the default discard-all table. Do not mix frontier heavy-compute (Apodex-H, Kimi-K3) with same-size open-source. DeepSearchQA is F1, not accuracy.

## SOTA Recommendation (as of 2026-09-08)
- **Primary Method**: **Iris** (`method:iris`, `paper:iris` `arXiv:2609.04304`) reverse-constructed tasks → traj/turn filter → SFT → live-search RL → SFT-RL climbing. Code/weights: AllSpark-Research/Iris.
- **Not This Task**: `method:canopy` remains AppWorld outcome-only; `method:sao` remains async stragglers; `method:mini-swe-agent` remains the SWE harness; `method:foldgrpo` remains folding; `method:cispo` remains dense Pass@1 RLVR.
