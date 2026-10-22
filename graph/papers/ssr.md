---
id: paper:ssr
type: paper
title: 'Forging More Tasks into Better Harnesses: Agentic Harness Evolution via Successive Scale Racing'
authors:
- 'Jingzhe Liu'
- 'Jiliang Tang'
- 'Tong Zhao'
- 'Neil Shah'
- 'Clark Mingxuan Ju'
year: 2026
month: 10
arxiv_id: '2610.28815'
url: https://arxiv.org/abs/2610.28815
methods:
- method:ssr
cites:
- paper:harness-playbook
tags:
- harness-rsi
- active
---

# SSR

## Abstract Summary
SSR (Successive Scale Racing) treats harness-evolution evidence selection as a search problem: more tasks help only if the optimizer picks the right evidence combination at each step.

## Key Contributions
1. SSR as an active plug-in on `task:agent-harness-runtime`.

## Empirical Highlights
- existing evolution methods degrade as the task pool expands; SSR adaptively searches evidence combinations at each evolution step. Does not retarget `method:omp2-harness`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28815`
- Code: `none found` (`code_status: none`).
