---
id: method:mcgpo
type: method
title: MCGPO
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: programmatic checker AppWorld coverage / anti-drift
  reason: CANOPY remains that hop; MCGPO is matched-context pairwise credit on already-collected agent
    rollouts
  use_instead: method:canopy
- when: variable environment latency / async stragglers
  reason: SAO remains async; MCGPO reuses sibling rollouts
  use_instead: method:sao
assumptions:
- 'Long-horizon agent with sparse terminal feedback and sibling rollouts. Paper: ALFWorld / WebShop, Qwen2.5-1.5B/7B
  and Qwen3-4B/8B, three seeds.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:mcgpo
recipes:
- recipe:mcgpo
claims:
- benchmark: ALFWorld and WebShop, six env-backbone settings, three seeds
  metric: mean success vs matched GraphGPO
  value: +0.47–1.46pp ALFWorld/WebShop Qwen2.5-1.5B/7B; +3.96 / +5.16pp WebShop Qwen3-4B/8B
  baseline: matched GraphGPO
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13755
  notes: ALFWorld baseline already >92%. Does not retarget CANOPY. GraphGPO is prior art, not a library
    node.
tags:
- post-training
- agentic
- gpo
- mcgpo
- active
---

# MCGPO

## Method Overview
Summarize pre-action state and rubric progress. Match two-action supports with ordered exact/coarse rules. Score the pair with held-out fold terminals. Add a support-weighted pairwise term next to the usual group task loss.

## When to Use
- Long-horizon agent GRPO/GraphGPO where sibling rollouts exist but token-uniform advantages ignore context.

## When NOT to Use
AppWorld TGC coverage → `method:canopy`. Async stragglers → `method:sao`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Does **not** replace CANOPY or SAO. GraphGPO is not a library node.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- ALFWorld headroom is small once success is already >92%.
- Matching rules are annotated by task rubrics; do not invent them at train time.
