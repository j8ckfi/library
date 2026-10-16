---
id: method:mosaic
type: method
title: 'Mosaic'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'variable environment latency / async stragglers'
  reason: 'SAO remains the async algorithm; Mosaic is multi-session credit, not straggler replay'
  use_instead: method:sao
- when: 'live-web multi-hop search-agent SFT-RL climbing (not session credit)'
  reason: 'Iris remains that recipe; Mosaic is evaluated on BrowseComp but owns session-aware advantages'
  use_instead: method:iris
- when: 'outcome-only AppWorld coverage / anti-drift'
  reason: 'CANOPY remains sparse-outcome coverage'
  use_instead: method:canopy
assumptions:
- 'Trajectories that actually split into compaction or subagent sessions. Paper: Qwen3.5-4B ReAct on BrowseComp.'
- 'Code: LARK-AI-Lab/Mosaic (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:mosaic
recipes:
- recipe:mosaic
claims:
- benchmark: 'BrowseComp, Qwen3.5-4B, multi-session compaction / subagent vs broadcasting'
  metric: 'accuracy and mean sessions'
  value: 'compaction 38.86 vs 35.31 (sessions 3.17→2.35, up to 10.1% relative); subagent 32.46 vs 31.44 (4.43→3.77)'
  baseline: 'trajectory-advantage broadcasting; single-session GRPO / IGPO (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22174'
  notes: 'Does not retarget SAO, Iris, or CANOPY. Prefer extending agentic-async-rl redirects over a new first-hop task.'
tags:
- agentic
- multi-session
- rl-alignment
- active
---

# Mosaic

## Method Overview
Treat compaction and subagent forks as sessions inside one trajectory. Estimate a session-aware trajectory advantage (reward stays dominant; extra sessions tax successes and credit exploration on failures), then shape each session by its type-normalized marginal contribution.

## When to Use
- Agentic RL whose inference path actually compact or forks, so broadcasting one advantage across sessions is the failure.

## When NOT to Use
Async stragglers → `method:sao`. Search-agent climbing → `method:iris`. AppWorld coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Multi-session is not a new first-hop task. Does **not** replace SAO.

## Gotchas & Failure Modes
- Single-session GRPO can still win under single-session inference (31.99). Mosaic is for multi-session execution.

