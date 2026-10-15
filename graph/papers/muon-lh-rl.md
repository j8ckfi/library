---
id: paper:muon-lh-rl
type: paper
title: Long-Horizon RL Needs Muon
authors:
- Kai Ruan
- Jinghao Lin
- Tao Chen
- Ziqi Zhou
- Qianshan Wei
- Zihe Huang
year: 2026
month: 10
arxiv_id: '2610.20256'
url: https://arxiv.org/abs/2610.20256
methods:
- method:muon-lh-rl
cites:
- paper:sao
- paper:muon2
tags:
- post-training
- muon
- async-rl
- swe
---

# Long-Horizon RL Needs Muon

## Abstract Summary
Long-horizon SWE agents need an optimizer recipe that weights variable-length traces and updates while rollouts are still collecting. The paper's async single-rollout mix is Muon, token-averaged loss, truncated IS, and length/tool-error penalties on an SPO/SPO++ host.

## Key Contributions
1. Muon vs Adam inside single-stream policy optimization for issue resolution.
2. Ablations on token-avg loss, TIS, length penalty, and tool-error penalty.
3. MiniCPM5-2B and Qwen3.5-4B on R2E-Gym with Claude Code harness 2.1.118.

## Empirical Highlights
- Full recipe reports higher training success than SPO baselines in the selected runs from both families.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.20256`
- Code: `none found` (`code_status: none`).
