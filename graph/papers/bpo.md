---
id: paper:bpo
type: paper
title: "Bellman Policy Optimization"
authors:
  - "Zhuoqing Song"
  - "Haotian Xu"
  - "Xikun Zhang"
  - "Lidong Bing"
year: 2026
month: 9
arxiv_id: "2609.15987"
url: "https://arxiv.org/abs/2609.15987"
methods:
  - method:bpo
cites:
  - paper:minimax-m1
  - paper:dapo
  - paper:gspo
  - paper:bpco
  - paper:grpo
tags:
  - post-training
  - rl-alignment
  - math
  - bpo
---

# Bellman Policy Optimization

## Abstract Summary
RLVR improves LLM reasoning, but common critic-free losses still start from a PPO-style importance-sampling ratio. Bellman Policy Optimization (BPO) starts from Policy Mirror Descent. For autoregressive generation with terminal rewards, Bellman telescoping rewrites PMD as a trajectory-level objective that needs only the verifier reward and the prompt-level expected reward, not intermediate state values. The practical loss keeps group-relative advantages and a GRPO-style clip mask, but replaces the IS ratio with a smoothed complementary-token mismatch weight \(\omega=(1+\varepsilon-\mu)/(1+\varepsilon-\pi)\), capped at \(C\). On Qwen3-30B-A3B-Base trained on DAPO-Math-17k, peak AIME 2024–2026 Avg@32 is 50.5%, beating CISPO, GSPO, DPPO, and GRPO-ClipHigher under matched settings.

## Key Contributions
1. **Critic-free PMD**: Bellman telescoping of token advantages leaves only the terminal reward and the initial value, with the same unique optimum as advantage-based PMD on rollout-reachable states.
2. **Mismatch-correction weight**: complementary-token ratio with additive smoothing \(\varepsilon\) and cap \(C\), in place of the token IS ratio.
3. **Matched math RLVR bake-off**: Qwen3-30B-A3B-Base, DAPO-Math-17k, 400 steps, group 16, max 16384.

## Empirical Highlights
- Peak mean Avg@32 across AIME24–26: BPO 50.5% vs CISPO 47.4% (+3.1), DPPO +4.1, GSPO +7.0, GRPO-ClipHigher 39.5% (+11.0).
- Same rollout batch (256 prompts × 16), eight optimizer updates per step.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.15987`
- No public GitHub as of 2026-09-23 (`recipe:bpo` `code_status: none`). Authors Apodex / Princeton. Same honesty note as Critical-State RL / Cal-OPD.
