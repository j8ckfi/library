---
id: method:mai-gym
type: method
title: 'MAI-Gym'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'desktop/OS GUI ranking on OSWorld 2.0 paper protocol'
  reason: 'OSWorld-Verified is not the locked ranking; Claude remains OSWorld 2.0'
  use_instead: method:claude-computer-use
- when: 'hybrid GUI+code recreation train/eval (RecreationWorld)'
  reason: 'RecreationWorld remains hybrid recreation; MAI-Gym is mocked-app GUI RL'
  use_instead: method:recreationworld
- when: 'synthesized GUI software environments for CUA training transfer'
  reason: 'SoftwareGym is synthesized GUI apps for transfer; MAI-Gym is the train/eval platform'
  use_instead: method:softwaregym
assumptions:
- 'GUI agent RL that can use mocked apps and many parallel envs. Paper: unified 9B mobile/computer agent.'
- 'Code: Tongyi-MAI/MAI-Gym (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:mai-gym
recipes:
- recipe:mai-gym
claims:
- benchmark: 'MobileWorld / OSWorld-Verified / physical-phone ticketing transfer, MAI-Gym-9B'
  metric: 'success; real-phone transfer'
  value: 'MobileWorld 78.4%; OSWorld-Verified 76.2% (NOT OSWorld 2.0); real phone 28.8→48.1'
  baseline: 'open GUI agents under 10B (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.20939'
  notes: 'Does not demote Claude computer-use on OSWorld 2.0. Does not replace RecreationWorld.'
tags:
- computer-use
- gui
- env
- active
---

# MAI-Gym

## Method Overview
One platform for GUI eval, collection, and online RL across mobile/computer/web, with mocked resettable apps and execution-validated tasks. Train on mocks; transfer is measured on a real phone.

## When to Use
- Scaling GUI-agent RL when real apps are too costly and you can mock them.

## When NOT to Use
OSWorld 2.0 ranking → `method:claude-computer-use`. Hybrid recreation → `method:recreationworld`. Synthesized GUI transfer gym → `method:softwaregym`.

## Relation to Existing SOTA
Active plug-in on `task:hybrid-computer-use-agent-rl` with a mention on `task:computer-use-agent` (`sota_for: []`). Does **not** demote Claude computer-use.

## Gotchas & Failure Modes
- OSWorld-Verified is near-saturated and is not the library ranking protocol.

