---
id: method:treehca
type: method
title: TreeHCA
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: programmatic checker AppWorld coverage / anti-drift
  reason: CANOPY remains that hop; TreeHCA is hindsight-guided tree exploration plus turn-level credit
  use_instead: method:canopy
- when: Actor-then-Critic IS-aligned critic after axiomatic token credit
  reason: PACT is Actor-then-Critic; TreeHCA is tree-backup hindsight
  use_instead: method:pact
- when: structural credit split for tool-call vs natural-language-summary tokens
  reason: SLCA-GRPO splits tool vs summary; TreeHCA revisits histories in a tree
  use_instead: method:slca-grpo
assumptions:
- 'Multi-turn LLM agents with a reference-answer likelihood signal. Paper: seven QA benches, three Qwen
  backbones.'
- 'GitHub TheBlackCat22/TreeHCA 404 as of 2026-10-12 (`code_status: announced`).'
last_reviewed: '2026-10-12'
papers:
- paper:treehca
recipes:
- recipe:treehca
claims:
- benchmark: Seven question-answering benchmarks, three Qwen backbones
  metric: aggregate exact match vs baselines
  value: outperforms all baselines in aggregate exact match
  baseline: outcome-supervised GRPO; hindsight credit without tree exploration
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12828
  notes: Abstract does not list per-bench numbers. Does not retarget CANOPY. Code 404 as of ingest.
tags:
- post-training
- agentic
- credit-assignment
- treehca
- active
---

# TreeHCA

## Method Overview
Watch reference-answer likelihood. When it jumps, branch the history and sample another continuation. Correct the sampling distribution with inverse-hindsight weights. Backup the terminal into turn advantages instead of a trajectory-constant GRPO advantage.

## When to Use
- Multi-turn agent RL where GRPO's uniform trajectory advantage hides which turn mattered, and you can score reference-answer likelihood.

## When NOT to Use
AppWorld coverage → `method:canopy`. Actor-then-Critic → `method:pact`. Tool vs summary split → `method:slca-grpo`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` with a mention on `task:tool-agent-segment-credit` (`sota_for: []`). Does **not** replace CANOPY or PACT.

## Gotchas & Failure Modes
- **code: announced** TheBlackCat22/TreeHCA 404 as of 2026-10-12.
- Exploration changes the continuation distribution; skip the IS correction and the backup is biased.
- Needs a reference-answer likelihood, not only a sparse terminal.
