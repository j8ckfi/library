---
id: paper:reharness
type: paper
title: Recurrent Harness for Agentic Continual Learning
authors:
- Yuxin Xiao
- Zhiyun Lu
- Jianyu Wang
- Yangtian Zhang
- Yang Song
- Qifan Wang
- Bailin Wang
year: 2026
month: 10
arxiv_id: '2610.12668'
url: https://arxiv.org/abs/2610.12668
methods:
- method:reharness
cites:
- paper:aclarena
- paper:ace
tags:
- agents
- continual-learning
- harness
- reharness
---

# Recurrent Harness for Agentic Continual Learning

## Abstract Summary
Agent harnesses usually only write forward or need extra replay to optimize. ReHarness is strictly online: after each instance, use the resulting trajectory as feedback to revise the reflections that were retrieved for that instance, sending credit backward through the textual harness state.

## Key Contributions
1. Forward read/write plus backward revision under a streaming protocol.
2. No extra replay or validation set for harness optimization.
3. Wins on three CL benches × three backbones vs memory and prompt-opt baselines.

## Empirical Highlights
- See `method:reharness` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12668`
- Code: `none found` (`code_status: none`).
