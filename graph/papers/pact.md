---
id: paper:pact
type: paper
title: "PACT: From Credit Assignment to Critic Alignment"
authors:
  - "Jiayan Fu"
  - "Hang Xu"
  - "Yong Zhang"
  - "Zhaokai Luo"
  - "Yao Hu"
  - "Dongyan Zhao"
  - "Mu Chuan"
year: 2026
month: 9
arxiv_id: "2609.26355"
url: "https://arxiv.org/abs/2609.26355"
methods:
  - method:pact
cites:
  - paper:opd
  - paper:grpo
  - paper:sao
  - paper:bpco
  - paper:ppo-paper
tags:
  - post-training
  - rl-alignment
  - actor-critic
  - credit-assignment
  - pact
---

# PACT: From Credit Assignment to Critic Alignment

## Abstract Summary
Token-level credit in LLM RL lacks a generally accepted definition. Completeness, Prefix Consistency, and Neutrality uniquely determine token-level credit as consecutive differences of the reward martingale \(C_i=\mathbb{E}[R\mid\mathcal{F}_i]-\mathbb{E}[R\mid\mathcal{F}_{i-1}]\). Under an ideal teacher, OPD is an implicit critic whose expected policy gradient is proportional to that credit. Response-level RLOO matches the expected policy-gradient contribution despite coarser granularity. Approximate sparsity under bounded outcome rewards shows how GAE critic errors can swamp the credit signal. Policy Aligned Critic Training (PACT) therefore updates the actor first, then trains the critic with importance-sampling correction (and BCE instead of MSE) so the critic tracks the updated policy. AllSpark Team.

## Key Contributions
1. **Unique token-credit axioms**: Completeness, Prefix Consistency, and Neutrality pin \(C_i=V_i-V_{i-1}\).
2. **OPD / RLOO as credit**: ideal-teacher OPD is an implicit critic; RLOO matches expected token-credit gradients.
3. **Actor-then-Critic PACT**: IS correction on critic training after the actor step.

## Empirical Highlights
- Agentic math Avg@16 (AIME 2025 / AIME 2026 / BeyondAIME / HMMT Nov. 2025): 72.87% average, +8.80 vs GRPO, +13.16 vs PPO.
- SWE-bench Verified pass@1 on Qwen3.6-35B-A3B: 67.4%, +2.0 GRPO, +2.4 PPO, +3.8 SAO.
- Figure 1 math uses Qwen3.5-4B with OpenCode; coding uses Qwen3.6-35B-A3B with Codex. Not a CISPO / SAO / BPCO retarget.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.26355`
- Claimed code: `https://github.com/AllSpark-Research/PACT` (empty stub as of 2026-09-24; `recipe:pact` `code_status: announced`).
