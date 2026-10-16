---
id: paper:sero
type: paper
title: 'SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic Reinforcement Learning'
authors:
- Dingyi Rong
- Yue Shi
- Chaofan Ma
- Zongrui Wang
- Jiezhang Cao
- Yixin Cao
- Liang He
- Ning Liu
year: 2026
month: 10
arxiv_id: '2610.19397'
url: https://arxiv.org/abs/2610.19397
methods:
- method:sero
cites:
- paper:canopy
- paper:opd
- paper:state-opd
tags:
- rl-alignment
- agentic
- oracle
---

# SERO

## Abstract Summary
Long-horizon agentic RL only sees futures the current policy visits. SERO restores a policy-reached state, lets a training-only oracle continue in the real environment, and weights each oracle step by frozen-policy compatibility with the preceding oracle prefix.

## Key Contributions
1. Executable oracle continuations from policy-reached states.
2. Policy-reachability weighting along the oracle branch.
3. Auxiliary oracle loss beside GraphGPO / HGPO; no oracle at inference.

## Empirical Highlights
- 1.5B GraphGPO ALFWorld 90.63/88.02→95.83/91.67; WebShop 87.27/77.93→88.90/79.27.
- 7B GraphGPO ALFWorld unseen 76.30→87.50 (+11.20). Root-only hurts.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19397`
- Code: `none found` (`code_status: none`).

