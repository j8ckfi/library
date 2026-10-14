---
id: method:reterm
type: method
title: ReTerm (Recovery Training)
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: source-code-only coding-agent RL env factory
  reason: CodeMidas remains the env-construction first hop
  use_instead: method:codemidas
- when: long-horizon terminal-agent data engine / pre-completed work detection
  reason: TerminalHorizon remains the data-engine plug-in
  use_instead: method:terminalhorizon
- when: 122B terminal-MoE RL on slime
  reason: T1 remains that recipe
  use_instead: method:t1-terminal-rl
assumptions:
- Terminal / SWE agent with stored failure states. Paper: Qwen3.5-9B ReTerm-GRPO.
- Official repo twothsnd/ReTerm as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:reterm
recipes:
- recipe:reterm
claims:
- benchmark: ReTerm-9B Qwen3.5-9B Terminal-Bench 2.0; SWE-bench Verified
  metric: Pass@1; resolve rate
  value: TB2.0 Pass@1 34.8 (+14.6); SWE-Verified 58.4%
  baseline: paper's Qwen3.5-9B without recovery training (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.18484
  notes: Does not retarget CodeMidas, TerminalHorizon, T1, or CANOPY.
tags:
- post-training
- terminal-agent
- recovery
- active
---

# ReTerm (Recovery Training)

## Method Overview
Store failure states from rollouts and fork new GRPO groups from those states so the policy practices recovery rather than only full-episode success.

## When to Use
- Terminal / SWE agent keeps dying in the same states and you can checkpoint those states for forked RL.

## When NOT to Use
Env factory from source → `method:codemidas`. Terminal data engine → `method:terminalhorizon`. 122B slime recipe → `method:t1-terminal-rl`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:coding-agent-rl-environment-construction` (`sota_for: []`). Mention on `task:outcome-only-long-horizon-agent-rl`. Does **not** replace CodeMidas, T1, or TerminalHorizon.

## Gotchas & Failure Modes
- Recovery data (ReTerm-10K) is not a substitute for leak-resistant env construction.
