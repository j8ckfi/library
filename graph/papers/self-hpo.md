---
id: paper:self-hpo
type: paper
title: 'Self-Evolving Coding Agents via Harness-Policy Optimization'
authors:
- 'Zhepei Wei'
- 'Wenlin Yao'
- 'Baolin Peng'
- 'Danqing Wang'
- 'Qianhui Wu'
- 'Hao Cheng'
- 'Yu Meng'
- 'Jianfeng Gao'
year: 2026
month: 10
arxiv_id: '2610.22791'
url: https://arxiv.org/abs/2610.22791
methods:
- method:self-hpo
cites:
- paper:harness-playbook
- paper:harness-rsi
tags:
- harness
- rsi
- coding-agent
- active
---

# Self-HPO

## Abstract Summary
Large language model (LLM) agents have shown promising potential in coding tasks, and their performance is jointly determined by the policy model and the harness that mediates their interaction with the environment. Indeed, harness and policy are mutually reinforcing and evolving only one component is suboptimal---a harness tuned for one checkpoint may not target the failure modes of an updated policy, while policy learning remains limited to the trajectories elicited by a fixed harness. In light of this, we propose Self-HPO, a recursive self-improving framework for coding agents that alternates harness and policy optimization, using the evolving policy as its own harness proposer. Specifica

## Key Contributions
1. Self-HPO alternates an H-step where the current policy proposes harness candidates from its failures with a P-step that RL-updates the policy under the selected harness. Hard tasks from training become the next harness search set.

## Empirical Highlights
- 57.8%→64.8%; joint gain exceeds harness-only plus policy-only

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22791`
- Code: `none found` (`code_status: none`).
