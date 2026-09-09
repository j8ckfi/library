---
id: method:neohorse-1
type: method
title: "NeoHorse-1"
category: "rl-alignment"
status: sota
sota_for:
  - task:agentic-rsi-routing-posttrain
supersedes: []
do_not_use_for:
  - when: "build a SWE / issue-to-patch harness rather than post-train from routing traces"
    reason: "NeoHorse is a routing-harness post-train recipe, not the bash ReAct SWE loop"
    use_instead: "method:mini-swe-agent"
  - when: "async stragglers / tool-latency replay is the bottleneck"
    reason: "SAO remains the async-algorithm default"
    use_instead: "method:sao"
  - when: "outcome-only long-horizon agent RL (AppWorld coverage / anti-drift)"
    reason: "Coverage / anti-drift is CANOPY"
    use_instead: "method:canopy"
  - when: "train a live-web multi-hop search agent (SFT-RL climbing)"
    reason: "Iris remains the search-agent first hop"
    use_instead: "method:iris"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "Labeled dense RLVR stays CISPO"
    use_instead: "method:cispo"
  - when: "single-teacher text distillation without a routing harness"
    reason: "Routing-guided OPD is a curriculum on OPD, not a new distill default"
    use_instead: "method:opd"
assumptions:
  - "A deployed routing harness over a heterogeneous model pool that logs predicted demand, selected tier, and the interaction."
  - "Paper: 4B and 9B agent-native models; SGLang v0.5.17; thinking mode; eval on ten harness/tool/code/IF benches."
  - "RSI here is one evaluation–selection–update prototype, not an automated research loop."
last_reviewed: "2026-09-09"
papers:
  - paper:neohorse-1
recipes:
  - recipe:neohorse-1
claims:
  - benchmark: "NeoHorse-1-4B vs Qwen3.5-4B ten-bench macro"
    metric: "macro-average"
    value: 64.87
    baseline: "Qwen3.5-4B 58.94 / Spark-X2.5-4B 62.22 / Nanbeige-4.2-3B 62.31 / Agents-A1-4B 61.46"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08183"
    notes: "Table 1. τ²-Bench 88.46 vs 84.29; PinchBench 77.33 vs 71.19; WorkBuddy 34.41 vs 24.62; HumanEval 96.95 vs 87.20."
  - benchmark: "NeoHorse-1-9B vs Qwen3.5-9B ten-bench macro"
    metric: "macro-average"
    value: 69.04
    baseline: "Qwen3.5-9B 65.60"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08183"
    notes: "Table 2 / abstract. Post-trained 4B narrows the aggregate gap to the 9B base."
tags:
  - post-training
  - agentic
  - rsi
  - routing
  - neohorse
  - sota
---

# NeoHorse-1

## Method Overview
NeoHorse-1 post-trains an agent-native model from a **routing harness**. Each user turn logs predicted capability demand, the selected service tier, and the interaction. Traces become user-turn examples that keep interleaved reasoning, tool calls, and harness context. Admission is structural validation, six-dimensional semantic evaluation, and subscene labels. Routing scores organize SFT into a three-stage curriculum and the same scores condition **routing-guided OPD** (teacher on student-generated prefixes). Capability-guided allocation maps eval feedback into the next mixture, closing an evaluation–selection–update loop.

This is not mini-SWE-agent, SAO, CANOPY, Iris, CISPO, or OPD.

## When to Use
- You already route over a model pool and can turn those logs into a curriculum.
- Goal is harness-mediated RSI post-train at ~4B/9B, not a SWE loop.

## When NOT to Use
- SWE harness → `method:mini-swe-agent`.
- Async stragglers → `method:sao`. AppWorld coverage → `method:canopy`.
- Live-web search climbing → `method:iris`. Pass@1 RLVR → `method:cispo`.
- Text distill without routing → `method:opd`.

## Relation to Existing SOTA
- First hop for `task:agentic-rsi-routing-posttrain` only. Does **not** supersede `method:mini-swe-agent`, `method:sao`, `method:canopy`, `method:iris`, `method:cispo`, or `method:opd`.
- Routing-guided OPD is a data/curriculum construction on OPD, not a new distill kernel.

## Gotchas & Failure Modes
- Prototype of one RSI cycle, not a claim that successive iterations compound indefinitely.
- Eval uses official harnesses (OpenSquilla, native WorkBuddy / VitaBench / τ²). VitaBench judge is DeepSeek-V4-Flash because the original recommended models were unavailable.
- Thinking-mode SGLang settings are load-bearing for the reported numbers.
