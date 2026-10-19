---
id: method:openmobile-2
type: method
title: 'OpenMobile-2'
category: agents
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'hybrid GUI+code CUA train/eval (RecreationWorld)'
  reason: 'RecreationWorld remains hybrid CUA first hop; OpenMobile-2 is mobile env+RL'
  use_instead: method:recreationworld
- when: 'desktop/OS GUI ranking on OSWorld 2.0 paper protocol'
  reason: 'Claude computer-use remains OSWorld 2.0 ranking'
  use_instead: method:claude-computer-use
- when: 'mocked-app GUI eval+RL platform with real-phone transfer (MAI-Gym)'
  reason: 'MAI-Gym is mocked-app plus real-phone; OpenMobile-2 is MobileGym++'
  use_instead: method:mai-gym
assumptions:
- 'HF Daily tail. MobileGym++ with 2K+ executable tasks and automatic rewards; 300+ app-native tools across 50+ apps.'
- 'No resolvable GitHub as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:openmobile-2
recipes:
- recipe:openmobile-2
claims:
- benchmark: 'AndroidWorld / MobileWorld / SPA-Bench real-device transfer'
  metric: 'success / SPA-Bench'
  value: 'AndroidWorld 79.9; MobileWorld 50.4; SPA-Bench 31.9→59.6'
  baseline: 'prior OpenMobile / SPA-Bench transfer (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.14157'
  notes: 'Does not retarget RecreationWorld or Claude computer-use. Not OSWorld 2.0 ranking.'
tags:
- mobile-agent
- gui
- hybrid-cua
- active
---

# OpenMobile-2

## Method Overview
OpenMobile-2 scales mobile-agent environments (MobileGym++) with automatic rewards and an experimental hybrid GUI plus app-native tool interface, then trains agents that transfer to real devices.

## When to Use
- Mobile GUI/hybrid agents when you need a scalable executable-task gym with automatic rewards, not desktop OSWorld ranking.

## When NOT to Use
Hybrid GUI+code desktop/multi-platform → `method:recreationworld`. OSWorld 2.0 → `method:claude-computer-use`.

## Relation to Existing SOTA
Active plug-in on `task:hybrid-computer-use-agent-rl` (`sota_for: []`). Does **not** replace RecreationWorld or Claude computer-use.

## Gotchas & Failure Modes
- AndroidWorld/MobileWorld numbers are not OSWorld 2.0.
- App-native tools are an experimental setting on a shared task suite.
