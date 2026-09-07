---
id: paper:rise
type: paper
title: "RISE: Recursive Improvement via Self-Extrapolating Policy Distillation"
authors:
  - "Yang Li"
  - "Semih Yavuz"
  - "Shafiq Joty"
year: 2026
month: 9
arxiv_id: "2609.05295"
url: "https://arxiv.org/abs/2609.05295"
methods:
  - method:rise
cites:
  - paper:opd
  - paper:grpo
  - paper:vista
  - paper:opsa
tags:
  - post-training
  - distillation
  - rlvr
  - self-extrapolation
  - rise
---

# RISE: Recursive Improvement via Self-Extrapolating Policy Distillation

## Abstract Summary
OPD is dense per-token supervision, but teacher quality is the bottleneck: an external teacher mismatches the student, and privileged self-distillation is capped by in-context learning. RISE builds a synthetic teacher from the model's own RLVR trajectory by extrapolating the displacement between the current checkpoint and a trailing anchor, in parameter space or output logit space. Sparse outcome updates become dense token-level OPD targets with no external model and no gold-solution conditioning. The teacher refreshes every iteration as the student improves, so distillation is a recursive loop rather than one-shot compression. RLVR grounds the extrapolation toward correct reasoning; the extrapolated teacher refines token-level decisions. Experiments on math, STEM, code, and multi-turn agentic tasks beat RLVR-only and on-policy self-distillation. No official GitHub as of 2026-09-07.

## Key Contributions
1. **Self-extrapolated teacher**: $\varphi(\pi_{\mathrm{future}})=\varphi(\pi_{\theta_n})+\beta\cdot(\varphi(\pi_{\theta_{n+1}'})-\varphi(\pi_{\theta_n}))$ with $\beta>1$, in weight space ($\theta_{\mathrm{future}}$) or logit space (token-wise logp displacement).
2. **RLVR + OPD loop**: outcome rewards ground the displacement; reverse-KL / Jensen–Shannon OPD distills $\mathrm{sg}[\pi_{\mathrm{future}}]$ into the student; teacher is non-stationary.
3. **Anchor**: EMA $\eta=0.1$ on Qwen, previous-checkpoint $\eta=1$ on OLMo. $\beta$ linearly decays from $\beta_0=1.2$ to $1$.
4. **Top-$K$ logits**: $K=100$ math/STEM, $K=20$ code, plus a tail bucket, so logit-space teachers do not materialize the full vocab.

## Empirical Highlights
- Qwen3-8B DAPOMath in-domain Math Avg: RISE (weight) 62.7 vs GRPO 60.0 vs GRPO+SDPO 55.9; multi-seed 62.4±0.2 vs GRPO 60.1±0.2.
- Qwen3-1.7B Math Avg: RISE (logit) 50.2 vs GRPO 45.4.
- OLMo3-7B-Instruct-SFT / OpenR1: RISE (logit) Math Avg 56.4 vs GRPO 47.6; AIME24 46.9 vs 30.2.
- Qwen3-4B mixed math+STEM: RISE (weight) Math Avg 44.8 vs GRPO 40.2; STEM Avg 47.5 vs 45.5.
- ALFWorld / WebShop Score / Acc: RISE (weight) 84.4 / 86.3 / 74.2 vs GRPO 75.0 / 79.8 / 63.3.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-07. Training described as VeRL on 8 GPUs, one epoch, AdamW constant LR, GRPO advantages without std normalization, token-IS clip 2.0. Recipe is Algorithms 1–2 in the paper (`recipe:rise`).
