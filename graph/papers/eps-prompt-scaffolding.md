---
id: paper:eps-prompt-scaffolding
type: paper
title: "Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal Reinforcement Post-Training"
authors:
  - "Yuanhao Yue"
  - "Qianli Ma"
  - "Chengyu Wang"
  - "Haoting Wang"
  - "Lei Shen"
  - "Jun Huang"
year: 2026
month: 9
arxiv_id: "2609.15051"
url: "https://arxiv.org/abs/2609.15051"
methods:
  - method:eps-prompt-scaffolding
cites:
  - paper:grpo
tags:
  - post-training
  - multimodal-rl
  - prompt-curriculum
  - eps
  - emnlp
---

# Not All Prompts Are Equal: Exploration-Guided Prompt Scaffolding for Multimodal Reinforcement Post-Training

## Abstract Summary
Training prompts in online RL are not equally informative for the current policy: some are saturated, others too hard to yield a reliable learning signal, yet both get the same rollout budget. The paper introduces an exploration-guided prompt scaffolding loop for MLLM RL post-training. The Exploration Potential Score (EPS) is a KL-regularized policy-improvement proxy computed from on-policy rollout rewards with no extra rollouts. Low-EPS prompts are rewritten by a teacher that preserves task intent instead of asking the student to imitate answers. Integrated with GRPO on Geometry3K and MMK12, the method beats GRPO in-domain and on OOD multimodal reasoning benches.

## Key Contributions
1. **EPS**: \(\hat{\mathcal{E}}(x)=\sum_i r_i\cdot\mathrm{softmax}(r_i/\beta)-\bar{r}\) from GRPO rewards; default \(\tau=0\).
2. **Teacher scaffolding as data refinement**, not output imitation (Qwen-VL-Max; answer-aware hints that must not reveal the answer).
3. **Dynamic prompt pool**: keep / rewrite / reserve / reactivate as the policy moves.

## Empirical Highlights
- Qwen3-VL-4B Geometry3K: 65.39 vs GRPO 60.57; OOD avg 49.75 vs 48.54.
- Qwen3-VL-4B MMK12: 71.15 vs GRPO 68.05; MathVision 44.41 vs 41.78.
- Qwen3-VL-2B MMK12 relatives vs GRPO: +9.7% in-domain, +11.5% MathVision, +11.1% MMMU-Pro.
- Setup: GRPO 3000 steps, 8 rollouts/prompt, 8-GPU FSDP, batch 16, lr \(1\times10^{-6}\), clip 0.2, KL 0.01. Reward: MathRuler. OOD judge: Qwen3-VL-Plus via LMMs-Eval.
- EMNLP 2026 main. Alibaba Cloud Computing / SJTU / Fudan / XJTU.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.15051`
- Project page: `https://mqleet.github.io/EPS-ProjectPage/`
- No official public training repo as of 2026-09-15. Pseudocode in Appendix A. Project page lists "Code (coming soon)".
