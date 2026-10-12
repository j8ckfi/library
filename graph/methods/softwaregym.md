---
id: method:softwaregym
type: method
title: SoftwareGym
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: desktop/OS GUI ranking on OSWorld 2.0 paper protocol
  reason: Claude computer-use remains the ranking hop; SoftwareGym is synthesized-env training transfer
  use_instead: method:claude-computer-use
- when: hybrid GUI+code recreation train/eval (RecreationWorld)
  reason: RecreationWorld is reference-as-oracle hybrid CUA; SoftwareGym synthesizes GUI apps
  use_instead: method:recreationworld
- when: data/env construction for coding-agent RL from source code
  reason: CodeMidas starts from OSS source; SoftwareGym synthesizes GUI software
  use_instead: method:codemidas
assumptions:
- 'Need diverse GUI software envs for CUA training. Paper: 182 synthesized apps, 12 categories; SoftwareGym-Bench
  120 tasks.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:softwaregym
recipes:
- recipe:softwaregym
claims:
- benchmark: OSWorld (strictly OOD) Pass@3 after training on SoftwareGym trajectories; SoftwareGym-Bench
  metric: Pass@3 / pass rate
  value: OSWorld Pass@3 41.39%→56.97%; SoftwareGym-Bench 40.0%; synthesized apps mean GUI task pass 91.5%
  baseline: same CUA before SoftwareGym training
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12611
  notes: Transfer number is not OSWorld 2.0 paper-protocol ranking. Does not demote Claude computer-use.
tags:
- agents
- computer-use
- environments
- softwaregym
- active
---

# SoftwareGym

## Method Overview
Generate diverse GUI designs, compile them to runnable apps, and iterate GUI tests until the app is functionally reliable. Collect CUA trajectories in those apps and train. Do not treat the in-domain SoftwareGym-Bench score as an OSWorld 2.0 ranking.

## When to Use
- You need scalable GUI software diversity for CUA training and native-app construction is the bottleneck.

## When NOT to Use
OSWorld 2.0 ranking → `method:claude-computer-use`. Hybrid recreation → `method:recreationworld`. Source-code coding RL envs → `method:codemidas`.

## Relation to Existing SOTA
Active plug-in on `task:hybrid-computer-use-agent-rl` with a mention on `task:computer-use-agent` (`sota_for: []`). Does **not** replace RecreationWorld or Claude computer-use.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- OSWorld Pass@3 here is transfer after training, not the library's OSWorld 2.0 paper protocol.
- Mean GUI pass 91.5% is the synthesized-app checker, not agent success.
