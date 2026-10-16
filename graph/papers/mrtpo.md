---
id: paper:mrtpo
type: paper
title: 'Each Reward to Its Relevant Tokens: Reward-Specific Token-Level Credit Assignment for Multi-Reward RL'
authors:
- Skylar Zhai
- Haonan Wang
- Zhining Liu
- Linxin Song
- Xuwei Ding
- Jingcheng Liang
- Jian Kang
year: 2026
month: 10
arxiv_id: '2610.21439'
url: https://arxiv.org/abs/2610.21439
methods:
- method:mrtpo
cites:
- paper:corrgrpo
- paper:dara
tags:
- rl-alignment
- multi-reward
- credit-assignment
---

# MRTPO

## Abstract Summary
GDPO keeps per-reward advantages distinct but still spreads each advantage over the whole response. MRTPO reassigns each reward's advantage onto tokens whose next-token distribution moves when that verifier's information is ablated.

## Key Contributions
1. Leave-one-out verifier replay to score token relevance without extra models.
2. Reward-specific token credit on a GRPO/GDPO host.
3. Text-to-SQL, multi-constraint IF, and tool calling.

## Empirical Highlights
- Qwen2.5-Coder-7B-Instruct SQL avg 73.15 vs GDPO 71.55 vs GRPO 70.93; MRTPO+SAW 73.41.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.21439`
- Code: `https://github.com/zhaihaotian/MRTPO` (`code_status: released`).

