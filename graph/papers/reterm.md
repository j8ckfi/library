---
id: paper:reterm
type: paper
title: 'ReTerm: Recovery Training for Self-Improving Terminal Agents'
authors:
- Wei Xie
- Kaituo Feng
- Shiming Fu
- Yong Liu
- Xiangyu Yue
- Shuangjia Zheng
year: 2026
month: 10
arxiv_id: '2610.18484'
url: https://arxiv.org/abs/2610.18484
methods:
- method:reterm
cites:
- paper:codemidas
- paper:terminalhorizon
- paper:t1-terminal-rl
- paper:canopy
tags:
- post-training
- terminal-agent
- recovery
- grpo
---

# ReTerm

## Abstract Summary
Fork RL rollouts from the agent's own failure states (Recovery Training). ReTerm-GRPO plus ReTerm-10K. Qwen3.5-9B Terminal-Bench 2.0 Pass@1 34.8 (+14.6); SWE-Verified 58.4%. Does not replace CodeMidas / T1 / TerminalHorizon.

## Key Contributions
1. Failure-state forking so recovery is on-policy from the agent's own mistakes.
2. ReTerm-10K recovery data plus ReTerm-GRPO.
3. Released github.com/twothsnd/ReTerm.

## Empirical Highlights
- ReTerm-9B (Qwen3.5-9B) TB2.0 Pass@1 34.8 (+14.6) (single-paper).
- SWE-bench Verified 58.4%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.18484`
- Code: `https://github.com/twothsnd/ReTerm` (`code_status: released`).
