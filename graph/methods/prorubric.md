---
id: method:prorubric
type: method
title: ProRubric (Protocol-level Rubrics)
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: programmatic checker exists and sparse outcome RL is the protocol
  reason: CANOPY remains checker-based coverage; ProRubric is rubric structure
  use_instead: method:canopy
- when: learning rubric rewards against vacuous credit
  reason: MetaRubric learns the reward; ProRubric regroups existing criteria
  use_instead: method:metarubric
- when: outcome-blind dynamic rubrics plus closed-form step credit
  reason: DRACO remains the no-checker sibling
  use_instead: method:draco
assumptions:
- Rubric-based RL with multi-criterion scores. Paper: HealthBench 4B/8B plus a seven-bench avg.
- Official repo Estrellajer/ProRubric as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:prorubric
recipes:
- recipe:prorubric
claims:
- benchmark: HealthBench 4B/8B; seven-bench avg at 4B
  metric: appropriateness / coverage vs Rubric-RL
  value: 4B appropriateness 36.8 vs 26.0 (+10.8), coverage 35.0 vs 32.1; 8B 45.8 vs
    29.5; +1.3 seven-bench avg at 4B
  baseline: Rubric-RL; untrained 54.1/26.6 appropriateness/coverage at 4B (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2609.38847
  notes: HF Daily 2026-10-14. Does not retarget CANOPY, DRACO, MetaRubric, or CorrGRPO/DARA.
tags:
- post-training
- rubric-rl
- reward-hacking
- active
---

# ProRubric (Protocol-level Rubrics)

## Method Overview
Group rubric criteria into protocols that must hold together. An additive sum lets a padded criterion compensate for a missed one; the protocol score does not.

## When to Use
- Rubric-RL is being hacked by compensating criteria and you still want a rubric (no programmatic checker).

## When NOT to Use
Checker exists → `method:canopy`. Learned rubric reward → `method:metarubric`. Dynamic rubric + step credit → `method:draco`. Multi-reward GRPO aggregation → `task:multi-reward-rlvr`.

## Relation to Existing SOTA
Active plug-in on `task:outcome-only-long-horizon-agent-rl` (`sota_for: []`). Mention on `task:multi-reward-rlvr`. Does **not** replace CANOPY, DRACO, or MetaRubric.

## Gotchas & Failure Modes
- Untrained HealthBench appropriateness (54.1) is higher than trained ProRubric (36.8) at 4B; read the paper's trained vs untrained split before citing the 54.1 number as a win.
