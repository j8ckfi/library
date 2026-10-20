---
id: paper:tar-rlvr
type: paper
title: 'Preserving Reasoning Diversity in Reinforcement Learning with Verifiable Rewards via Adaptive Replay'
authors:
- 'Wen-Zhi Li'
- 'Sainyam Galhotra'
- 'Claire Cardie'
year: 2026
month: 10
arxiv_id: '2610.24236'
url: https://arxiv.org/abs/2610.24236
methods:
- method:tar-rlvr
cites:
- paper:minimax-m1
- paper:expdis
tags:
- rl-alignment
- rlvr
- active
---

# TAR

## Abstract Summary
On-policy RLVR can suppress equally rewarded reasoning modes that finite groups undersample. TAR stores diverse correct base traces and adaptively replays them. Across six math benches and two Qwen2.5 scales it balances accuracy and diversity better than evaluated diversity methods.

## Key Contributions
1. Memory-bank targeted adaptive replay with a soft rollout gate and a token gate.

## Empirical Highlights
- Reduces forgetting of correct base-model solutions.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24236`
- Code: `https://github.com/wenzhilics/tar` (`code_status: released`).
