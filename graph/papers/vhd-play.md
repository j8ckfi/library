---
id: paper:vhd-play
type: paper
title: "Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms"
authors:
  - "Xinjie Shen"
  - "Wei Fan"
  - "Xudong Guo"
  - "Jianhong Tu"
  - "Yang Su"
  - "Chuqiao Kuang"
  - "Yinger Zhang"
  - "Dayiheng Liu"
year: 2026
month: 9
arxiv_id: "2609.27321"
url: "https://arxiv.org/abs/2609.27321"
methods:
  - method:vhd-play
cites:
  - paper:codemidas
  - paper:canopy
  - paper:sao
  - paper:grpo
tags:
  - post-training
  - agentic
  - environments
  - vhd-play
---

# Verifiable Hidden Dynamics Play: Generating Agentic RL Environments from Solved Mechanisms

## Abstract Summary
Scaling long-horizon agent RL needs diverse environments with dependable outcome signals. Environment-first generators build the sandbox before fixing the scoring rule, then align dynamics and evaluation after the fact. VHD-Play reverses that order: sample and solve a mathematical mechanism first, then a corpus-grounded setter renders the decision process as stateful tools whose dynamics and verifiers are inherited from the same solution. The player sees neither parameters nor the solution and must recover them through interaction. The pipeline admits 3,300 environments at a few cents each. Training Qwen3.6-35B-A3B on three families raises mean agentic score 0.204→0.815 on a five-family diagnostic, transfers to held-out and unseen mechanism families, and beats Qwen3.7-Max on a 365-day E-Commerce Bench with zero bankruptcy. Most of the learnable gap is stateful interaction, not the written problem. Qwen Technical Report.

## Key Contributions
1. **Mechanism-first construction**: \(M(\theta)\to z_\theta\to\mathcal{R}_\theta\) before wrapping executable dynamics as \(E(\theta)\).
2. **Cheap diverse substrate**: 3,300 admitted envs; frozen 35B setter; information-asymmetric probe/decision tools.
3. **Stateful interaction is the gap**: written-out vs hidden-parameter agentic forms of the same problem.

## Empirical Highlights
- Five-family diagnostic mean agentic score 0.204→0.815 after training on three families.
- Held-out instances of trained families plus eight unseen mechanism families improve.
- E-Commerce Bench: every run completes without bankruptcy; exceeds Qwen3.7-Max; 3.4× base ending balance.
- BFCL V4 interaction-focused cells +2.84; written-out problem solving is preserved.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.27321`
- No public GitHub found as of 2026-09-24 (`recipe:vhd-play` `code_status: none`).
