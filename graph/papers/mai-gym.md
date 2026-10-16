---
id: paper:mai-gym
type: paper
title: 'MAI-Gym: An Open All-in-One Platform for GUI Agent Evaluation and RL Training across Mobile and Computer Environments'
authors:
- Panrong Tong
- Quyu Kong
- Pengxiang Li
- Tianyu Xia
- Hanzhang Zhou
- Lei Wang
- Chenglin Cai
- Long Li
- Long Chen
- Jianan Zhang
- Zhengwen Zeng
- Xu Zhang
- Gongjie Zhang
- Yue Wang
- Steven Hoi
year: 2026
month: 10
arxiv_id: '2610.20939'
url: https://arxiv.org/abs/2610.20939
methods:
- method:mai-gym
cites:
- paper:recreationworld
- paper:softwaregym
tags:
- computer-use
- gui
- rl-alignment
---

# MAI-Gym

## Abstract Summary
GUI RL is expensive and short on realistic tasks. MAI-Gym unifies evaluation, data collection, and online RL across mobile, computer, and web, scales to 20k parallel instances, and synthesizes resettable mocked apps with execution-validated verifiers.

## Key Contributions
1. Shared rollout pipeline for eval and train.
2. Mocked-app synthesis plus 2,000 verified tasks.
3. MAI-Gym-9B unified mobile/computer agent.

## Empirical Highlights
- MAI-Gym-9B: MobileWorld 78.4%; OSWorld-Verified 76.2% (not OSWorld 2.0 ranking).
- Mocked train-ticketing app transfers to a physical phone 28.8→48.1.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.20939`
- Code: `https://github.com/Tongyi-MAI/MAI-Gym` (`code_status: released`).

