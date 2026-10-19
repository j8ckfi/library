---
id: method:market-posttrain
type: method
title: 'MPT'
category: agents
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'whether to use more than one agent (default: do not)'
  reason: 'single-agent-plus-tools remains the orchestration default; MPT jointly learns action and bidding'
  use_instead: method:single-agent-plus-tools
- when: 'train asynchronous RL for a tool-use policy'
  reason: 'SAO remains async tool RL; MPT is swarm bidding'
  use_instead: method:sao
assumptions:
- 'Decentralized swarm. Agents bid to participate; bids decide who acts and how collective outcomes credit local updates. Code: Embodied-Minds-Lab/MPT.'
last_reviewed: '2026-10-19'
papers:
- paper:market-posttrain
recipes:
- recipe:market-posttrain
claims:
- benchmark: 'Decentralized agent swarms, jointly learned action and bidding'
  metric: 'whether action policies and self-orchestration co-adapt vs fixed orchestration'
  value: 'joint action+bidding lets individual capabilities and participation patterns adapt together, vs training inside a fixed orchestration structure'
  baseline: 'fixed-orchestration multi-agent training (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22322'
  notes: 'Does not retarget single-agent-plus-tools. MAS remains the exception, not the SWE default.'
tags:
- multi-agent
- swarm
- post-training
- active
---

# MPT

## Method Overview
Market-based post-training (MPT) lets swarm agents bid for participation so action policies and orchestration are learned together; bids both select who acts and assign local credit from collective outcomes.

## When to Use
- Decentralized swarms where fixing the orchestration while training skills (or vice versa) is the failure mode.

## When NOT to Use
Default: do not use MAS → `method:single-agent-plus-tools`. SWE issue-to-patch → `method:mini-swe-agent`.

## Relation to Existing SOTA
Active plug-in on `task:multi-agent-orchestration` (`sota_for: []`). Does **not** replace single-agent-plus-tools.

## Gotchas & Failure Modes
- Does not overturn the library do-not-MAS default for SWE.
- Bidding credit is the training signal; a broken market starves skill learning.
