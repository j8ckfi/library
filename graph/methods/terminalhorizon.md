---
id: method:terminalhorizon
type: method
title: TerminalHorizon
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: source-code-only coding RL env factory then GRPO
  reason: CodeMidas remains the source-only env factory first hop; TerminalHorizon
    is a terminal-agent data engine plus SFT
  use_instead: method:codemidas
- when: 122B terminal-MoE RL on slime
  reason: T1 is the terminal-MoE RL recipe; TerminalHorizon is data + SFT of Qwen3.5-27B
  use_instead: method:t1-terminal-rl
- when: GitHub issue to patch / SWE harness
  reason: mini-SWE-agent remains the issue-to-patch loop
  use_instead: method:mini-swe-agent
assumptions:
- 'Terminal / shell agent data. Paper: 1,535 envs, 2,852 traj, avg 52.8 turns. SFT
  Qwen3.5-27B.'
- Project page zs1314.github.io/TerminalHorizon. No public trainer as of 2026-10-13.
last_reviewed: '2026-10-13'
papers:
- paper:terminalhorizon
recipes:
- recipe:terminalhorizon
claims:
- benchmark: 'Qwen3.5-27B SFT: Terminal-Bench 2.1 / AutomationBench Pass / VitaBench'
  metric: resolved / pass / score vs base
  value: TB2.1 46.82→60.67; AutomationBench Pass 5.5→17.2; VitaBench 20.5→31.8
  baseline: same Qwen3.5-27B without TerminalHorizon SFT
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13166
  notes: Also TB1.0 55.0 (+8.7); TB2.0 55.8 (+14.2); tau2 Airline 79.0→84.5 Retail
    84.9→87.5. Does not retarget CodeMidas or T1.
tags:
- post-training
- terminal-agents
- environments
- terminalhorizon
- active
---

# TerminalHorizon

## Method Overview
A terminal-agent data engine. Detect pre-completed work in the sandbox, rebuild the env, expand in stages to ~1.5K environments, then SFT a 27B policy on the collected trajectories.

## When to Use
- Need long-horizon terminal / shell trajectories (tens of turns) and an SFT corpus, not a source-only GRPO factory.

## When NOT to Use
Source-code-only env factory → `method:codemidas`. 122B terminal-MoE RL → `method:t1-terminal-rl`. Issue-to-patch harness → `method:mini-swe-agent`.

## Relation to Existing SOTA
Active plug-in on `task:coding-agent-rl-environment-construction` beside `method:codemidas` (`sota_for: []`). Link `method:t1-terminal-rl`. Does **not** enter `current_sota`. Does **not** replace CodeMidas, T1, or mini-SWE-agent.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-13. Project page only: `https://zs1314.github.io/TerminalHorizon`.
- Numbers are SFT of Qwen3.5-27B, not GRPO on the constructed pool (CodeMidas protocol).
- Pre-completed-work detection is the leak that naive terminal dumps miss.
