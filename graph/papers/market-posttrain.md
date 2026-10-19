---
id: paper:market-posttrain
type: paper
title: 'Learning Self-Orchestration in Decentralized Agent Swarms'
authors:
- 'Guowei Xu'
- 'Zhenting Qi'
- 'Amani Kiruga'
- 'Himabindu Lakkaraju'
- 'Yilun Du'
year: 2026
month: 10
arxiv_id: '2610.22322'
url: https://arxiv.org/abs/2610.22322
methods:
- method:market-posttrain
cites: []
tags:
- multi-agent
- swarm
- post-training
- active
---

# MPT

## Abstract Summary
The capabilities of an agent swarm depend on both its individual members and how they coordinate. Yet existing multi-agent systems often train agents within fixed orchestration structures, separating the learning of individual capabilities from the organization of collective behavior. We introduce market-based post-training (MPT), a framework for jointly learning action policies and self-orchestration in decentralized agent swarms. Agents express their willingness to participate through bids, which determine who acts and how collective outcomes provide local training credit. Learning both action and bidding behavior allows individual capabilities and patterns of participation to adapt togeth

## Key Contributions
1. Market-based post-training (MPT) lets swarm agents bid for participation so action policies and orchestration are learned together; bids both select who acts and assign local credit from collective outcomes.

## Empirical Highlights
- joint action+bidding lets individual capabilities and participation patterns adapt together, vs training inside a fixed orchestration structure

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22322`
- Code: `https://github.com/Embodied-Minds-Lab/MPT` (`code_status: released`).
