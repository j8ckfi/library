---
id: paper:t1-terminal-rl
type: paper
title: "T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks"
authors:
  - "Junyao Yang"
  - "Yucheng Shi"
  - "Zhongzhi Li"
  - "Ruhan Wang"
  - "Zongxia Li"
  - "Haitao Mi"
  - "Leowei Liang"
year: 2026
month: 9
arxiv_id: "2609.11042"
url: "https://arxiv.org/abs/2609.11042"
methods:
  - method:t1-terminal-rl
cites:
  - paper:miles
  - paper:sao
  - paper:canopy
  - paper:grpo
tags:
  - post-training
  - agentic
  - terminal
  - moe
  - slime
---

# T1: Terminal Agent Reinforcement Learning for Long-Horizon Tasks

## Abstract Summary
T1 is a 122B-total MoE terminal agent trained with RL in a real cloud sandbox for 300+ tool-call turns, rewarded by each task's verifier. Recipe: aggressive critic warm-start with a dense process reward (absolute passing-verifier count); TITO (token-in, token-out) construction with drift repair at turn boundaries; rollout routing replay (R3) that records sampler expert choices and replays them at train time. Training data is held out from Terminal-Bench 2.1. TITO + R3 cut train–inference logp gap from 0.021 to 0.013 with zero token drift in the loss region. Host stack is slime v0.3.0 (Miles' ancestor), not a Miles replacement. Terminal-Bench 2.1: 43.8% → 64.0% resolved. Long-Horizon Terminal Bench: 27.9%.

## Key Contributions
1. **122B MoE terminal RL** at 300+ tool turns with per-task verifiers.
2. **TITO + R3** for train–inference token and MoE-routing identity.
3. **OOD training corpus** vs Terminal-Bench 2.1.

## Empirical Highlights
- Terminal-Bench 2.1 resolved: 43.8% → 64.0%.
- Long-Horizon Terminal Bench: 27.9% (paper: surpasses GPT-5.4 and GLM-5.1 under the same harness).
- Train–inference logp gap 0.021 → 0.013.

## Open Source Repository & Resources
- Project: `https://jyyang26.github.io/t1`
- Weights collection: `https://huggingface.co/collections/TberiusJunyao/t1`
- Train host: `https://github.com/THUDM/slime` (v0.3.0; paper cites commit bf14dc21). No dedicated T1 train repo as of 2026-09-11.
