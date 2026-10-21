---
id: method:self-credit
type: method
title: 'Self-Credit'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'programmatic checker AppWorld coverage / anti-drift'
  reason: 'CANOPY remains coverage; Self-Credit densifies sparse outcome rewards via cited-turn rescaling'
  use_instead: method:canopy
- when: 'train a live-web multi-hop search agent (SFT-RL climbing)'
  reason: 'Iris remains climbing; Self-Credit is intra-group citation credit on a GRPO host'
  use_instead: method:iris
assumptions:
- 'Group-based agentic RL. Policy emits cited summaries; intra-group comparison of cited turns across success/fail; advantage reweight on cited turns.'
- 'Paper: BrowseComp-Plus Qwen3-8B/32B; GAIA; xBench-DeepSearch. No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:self-credit
recipes:
- recipe:self-credit
claims:
- benchmark: 'BrowseComp-Plus Qwen3-8B/32B; GAIA; xBench-DeepSearch'
  metric: 'points vs base and strongest agentic RL baselines'
  value: 'BrowseComp-Plus +37.0 / +36.2 vs base and +8.5 / +5.6 vs strongest agentic RL; GAIA +4.9; xBench-DeepSearch +4.7'
  baseline: 'base models; strongest reported agentic RL baselines'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28388'
  notes: 'Intra-group rescaling on failed rollouts matters across scales. Does not retarget CANOPY or Iris.'
tags:
- agentic-rl
- credit-assignment
- active
---

# Self-Credit

## Method Overview
Self-Credit turns sparse outcome rewards into dense turn credit. The policy cites earlier turns in a summary; intra-group comparison of those citations across success and failure downweights undeserved credit; advantages of cited turns are rescaled.

## When to Use
- Long-horizon agentic RLVR where only the episode outcome is verified and you already run group rollouts.

## When NOT to Use
Checker coverage → `method:canopy`. Search climbing → `method:iris`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:canopy`.

## Gotchas & Failure Modes
- Relies on the policy's own citations; garbage citations poison credit.
- Failed-rollout disagreement is load-bearing.
