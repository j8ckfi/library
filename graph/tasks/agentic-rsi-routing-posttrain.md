---
id: task:agentic-rsi-routing-posttrain
type: task
title: "Agentic RSI Routing-Harness Post-Training"
domain: "post-training"
summary: "Post-train an agent-native model from routing-harness traces: capability-demand curriculum, routing-guided OPD, and evaluation-selection-update loops toward recursive self-improvement. Not a SWE harness, not SAO, not CANOPY, not Iris."
scope: "Agentic post-training that converts routing-harness records (predicted demand, selected tier, interaction) into SFT curriculum and routing-guided OPD, then reallocates the next mix from capability feedback."
out_of_scope:
  - "SWE issue-to-patch harness (mini-SWE-agent)"
  - "Async tool-latency / straggler RL (SAO)"
  - "AppWorld outcome-only coverage / anti-drift (CANOPY)"
  - "Live-web multi-hop search-agent climbing (Iris)"
  - "Single-turn dense math/code RLVR (CISPO)"
  - "Text-only single-teacher distillation default (OPD)"
redirects:
  - when: "build a SWE / issue-to-patch harness rather than post-train from routing traces"
    to: "task:software-engineering-agent-harness"
  - when: "variable environment latency / async stragglers, not RSI routing post-train"
    to: "task:agentic-async-rl"
  - when: "outcome-only long-horizon agent RL (AppWorld coverage / anti-drift or rubric credit)"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "train a live-web multi-hop search agent (SFT-RL climbing)"
    to: "task:web-search-agent-rl"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "single-teacher text distillation without a routing harness"
    to: "task:student-distillation"
current_sota:
  - method: method:neohorse-1
    as_of: "2026-09-09"
    benchmark: "10-bench macro (agentic / coding / IF) vs Qwen3.5 same size"
    metric: "macro-average"
    value: "4B 58.94→64.87; 9B 65.60→69.04"
    notes: "NeoHorse-1 (2609.08183). First hop for routing-harness RSI post-train only. Does not replace mini-SWE-agent, SAO, CANOPY, Iris, CISPO, or OPD."
methods:
  - method:neohorse-1
  - method:mini-swe-agent
  - method:sao
  - method:canopy
  - method:iris
  - method:opd
  - method:harness-onpolicy-correction
last_reviewed: "2026-09-11"
tags:
  - post-training
  - agentic
  - rsi
  - routing
  - neohorse
---

# Agentic RSI Routing-Harness Post-Training

## Problem Definition
Recursive self-improvement needs a concrete loop: observe capability demand from a deployed routing harness, convert traces into training examples, admit them, curriculum-train, then reallocate the next mix from evaluation. Nearby shelves (SWE harness, async stragglers, AppWorld coverage, live-web search, Pass@1 RLVR, plain OPD) do not own this loop.

## Evaluation Protocol
- **Primary Benchmarks**: harness agents (QwenClawBench, PinchBench, WorkBuddy, VitaBench, τ²-Bench), tool use (BFCL v4), coding (HumanEval, LiveCodeBench v6), instruction following (IFBench, IFEval). Macro-average vs same-size base.
- **Evaluation Pitfalls**: Do not mix this with SWE-bench harness choice. Routing-guided OPD is a curriculum on OPD, not a replacement of `method:opd`.

## SOTA Recommendation (as of 2026-09-09)
- **Primary Method**: **NeoHorse-1** (`method:neohorse-1`, `paper:neohorse-1` `arXiv:2609.08183`). Code: TokenRhythm/NeoHorse. Weights: hf.co/collections/TokenRhythm/neohorse-1.
- **Not This Task**: `method:mini-swe-agent` remains the SWE harness; `method:sao` remains async; `method:canopy` remains AppWorld; `method:iris` remains search-agent climbing; `method:cispo` remains Pass@1; `method:opd` remains text distill.
- **Gotcha (evolved-harness full-traj SFT)**: `method:harness-onpolicy-correction` (`arXiv:2609.09134`). Does not replace NeoHorse-1.
