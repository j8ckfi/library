---
id: task:hybrid-computer-use-agent-rl
type: task
title: "Hybrid Computer-Use Agent RL"
domain: "agents"
summary: "Train and evaluate hybrid computer-use agents that interleave GUI exploration with code/CLI implementation and visually verify their own artifacts."
scope: "Hybrid GUI+code train/eval (recreation tasks, reference-as-oracle rewards, multi-platform harness). First hop is RecreationWorld. Desktop OSWorld 2.0 paper-protocol ranking stays Claude computer-use."
out_of_scope:
  - "Desktop/OS GUI ranking on OSWorld 2.0 paper protocol (Claude computer-use)"
  - "GitHub issue → patch (mini-SWE-agent)"
  - "Programmatic-checker AppWorld coverage (CANOPY)"
  - "Trained mobile-only GUI policy on AndroidWorld (MAI-UI / UI-TARS-2)"
  - "Coding-agent RL env construction from source code (CodeMidas)"
redirects:
  - when: "desktop/OS GUI ranking on OSWorld 2.0 paper protocol"
    to: "task:computer-use-agent"
  - when: "GitHub issue to patch / SWE harness"
    to: "task:software-engineering-agent-harness"
  - when: "programmatic checker AppWorld coverage / anti-drift"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "data/env construction for coding-agent RL from source code"
    to: "task:coding-agent-rl-environment-construction"
current_sota:
  - method: method:recreationworld
    as_of: "2026-09-21"
    benchmark: "RecreationBench 250 (50 per platform), GPT-6 Astra"
    metric: "unweighted mean of programmatic and visual scores"
    value: "58.1% overall; full programmatic pass 2.8%"
    notes: "RecreationWorld (2609.22000). Active hybrid CUA train/eval. Method status active (not sota). Does not demote Claude computer-use on OSWorld 2.0."
methods:
  - method:recreationworld
  - method:claude-computer-use
  - method:ui-tars-2
  - method:mai-ui
  - method:mini-swe-agent
last_reviewed: "2026-09-21"
tags:
  - agents
  - computer-use
  - hybrid-cua
  - recreationworld
---

# Hybrid Computer-Use Agent RL

## Problem Definition
GUI computer-use and terminal/code agents advanced on separate tracks. Hybrid CUAs must explore a running interface, implement software, and visually verify their own artifacts with no prescribed stage order. This task is that train/eval setting: recreation against a running reference, hidden programmatic and visual assertions, five platforms (Ubuntu, macOS, Windows, Android, Web).

OSWorld 2.0 paper-protocol ranking is a different shelf.

## Evaluation Protocol
- **Primary Benchmarks**: RecreationBench (250 tasks, 50 per platform); OOD coding / hybrid CUA transfer after recreation training.
- **Evaluation Pitfalls**: High overall scores can hide near-zero full programmatic pass. Do not mix RecreationBench with OSWorld 2.0 binary/partial.

## SOTA Recommendation (as of 2026-09-21)
- **Primary Method (this task only)**: **RecreationWorld** (`method:recreationworld`, `paper:recreationworld` `arXiv:2609.22000`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:claude-computer-use` remains OSWorld 2.0 paper-protocol ranking; `method:mini-swe-agent` remains issue-to-patch; `method:canopy` remains AppWorld coverage; `method:mai-ui` / `method:ui-tars-2` remain trained GUI-only policies.
