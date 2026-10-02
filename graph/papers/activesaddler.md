---
id: paper:activesaddler
type: paper
title: "ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization"
authors:
  - "Sungho Park"
  - "Wonjoong Kim"
  - "Jue Zhang"
  - "Wook-Shin Han"
  - "Pengfei Gao"
  - "Chanyoung Park"
  - "Yongqiang Yao"
  - "Rao Fu"
  - "Elsie Nallipogu"
  - "Qingwei Lin"
  - "Victor Ruhle"
year: 2026
month: 10
arxiv_id: "2610.00906"
url: "https://arxiv.org/abs/2610.00906"
methods:
  - method:activesaddler
cites:
  - paper:harness-playbook
  - paper:rrsi
tags:
  - agents
  - agent-harness
  - curriculum
  - activesaddler
---

# ActiveSaddler: Automated Curriculum Learning for Agent Harness Optimization

## Abstract Summary
Automated harness optimization usually fixes the scenario set and only evolves prompts, tools, and control. As the harness changes, the useful scenarios change. ActiveSaddler treats the training curriculum as a non-stationary bandit whose arms are failure-pattern clusters instantiated from diagnosed traces. Each iteration either revisits an arm by remaining learning progress or evaluates unseen scenarios. The harness-update operator is unchanged. Microsoft / POSTECH / KAIST. Code host: `https://github.com/microsoft/AutoSaddler`.

## Key Contributions
1. **Curriculum as the missing axis**: scenario selection co-evolves with the harness under a fixed rollout budget.
2. **Failure-pattern arms**: not category labels, not one arm per scenario.
3. **Explore vs revisit**: adaptive balance as unresolved failures shrink.

## Empirical Highlights
- GAIA2 test Pass@1 +4.4 pp vs the same harness optimizer with scenario order fixed before optimization.
- Terminal-Bench 2.0 test Pass@1 +7.5 pp under the same comparison. Ablations: failure-pattern arms, evolving utility, explore-vs-revisit are load-bearing.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.00906`
- Code: `https://github.com/microsoft/AutoSaddler` (`code_status: released`).
- Project: `https://autosaddler-projectpage.github.io/activesaddler/` (aka.ms/ActiveSaddler-website).
