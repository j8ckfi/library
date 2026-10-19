---
id: method:lean4-agentic-rl
type: method
title: 'Lean4AgenticRL'
category: rl
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'outcome-only long-horizon agent RL with a programmatic checker (CANOPY)'
  reason: 'CANOPY remains coverage/anti-drift; Lean4AgenticRL adds Lean4-formalized process rewards'
  use_instead: method:canopy
- when: 'terminal-agent RSR + RPR recursive self-improve'
  reason: 'Terminal-RSI is harness RSI on TB; LAR is process-reward RL'
  use_instead: method:terminal-rsi
assumptions:
- 'Problem-specific workflow plus Lean4 formalization of toolcall / workflow-stage / outcome rewards. Workflow-stage-normalized GRPO. Trains LAR-9B/27B.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:lean4-agentic-rl
recipes:
- recipe:lean4-agentic-rl
claims:
- benchmark: 'LAR-27B TerminalBench-2.1; vs base and same-size second-best'
  metric: 'TB2.1; average vs base'
  value: 'TB2.1 77.3%; +9.89 vs base; +5.07 vs second-best same-size'
  baseline: 'base model / same-size SOTA in the paper'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22448'
  notes: 'Does not retarget CANOPY or Terminal-RSI. TB2.1 is not AppWorld TGC.'
tags:
- agent-rl
- lean4
- process-reward
- active
---

# Lean4AgenticRL

## Method Overview
Lean4AgenticRL grounds toolcall, workflow-stage, and outcome rewards in a unified Lean4 schema, then trains with workflow-stage-normalized GRPO so open-ended SWE/terminal agents get verifiable process credit.

## When to Use
- Open-ended SWE/terminal agent RL when outcome-only rewards starve toolcall and workflow-stage credit and you can formalize the workflow in Lean4.

## When NOT to Use
AppWorld coverage → `method:canopy`. Terminal harness RSI → `method:terminal-rsi`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** replace CANOPY.

## Gotchas & Failure Modes
- Needs Lean4 workflow formalization.
- TB2.1 77.3% is below Terminal-RSI's reported TB2.1 86.52% and is a different recipe (process-reward RL vs harness RSI).
