---
id: paper:programgym
type: paper
title: 'ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents'
authors:
- Chengyi Yang
- Renxu Bao
- Jue Hou
- Zongpei Teng
- Ziheng Wang
- Yujie Lin
- Chengsong Huang
- Junnan Zhu
- Delai Qiu
- Yining Wang
- Shengping Liu
- Fei Long
- Jinsong Su
year: 2026
month: 10
arxiv_id: '2610.13395'
url: https://arxiv.org/abs/2610.13395
methods:
- method:programgym
cites:
- paper:codemidas
- paper:mini-swe-agent
tags:
- agents
- coding-rl
- environments
- programgym
---

# ProgramGym: Scaling Training Environments for Long-Horizon Program Reproduction Agents

## Abstract Summary
Coding agents that build programs from scratch lack scalable verifiable envs that force requirement discovery and design. ProgramGym's Program-Env repairs sandbox builds and black-box tests from repositories (1,648 C/C++/Go/Rust envs). Program-Agent is a role-isolated analysis/implementation/review workflow with revision management. SFT on those trajectories then the agent raises ProgramBench well above the 27B base.

## Key Contributions
1. Feedback-driven env factory from repositories with black-box tests (1,648 envs).
2. Program-Agent role-isolated long-horizon workflow.
3. Qwen3.8-27B 34.87→42.84 SFT; agent 55.71/56.25.

## Empirical Highlights
- See `method:programgym` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13395`
- Code: `announced` (`code_status: announced`).
