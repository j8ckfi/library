---
id: paper:thinkprior
type: paper
title: "ThinkPrior: Zero-Rollout Difficulty Priors for Cold-Start Prompt Selection in RLVR"
authors:
  - "Tommy Sha"
  - "Skylar Zhai"
  - "Siqi Zhao"
year: 2026
month: 9
arxiv_id: "2609.09075"
url: "https://arxiv.org/abs/2609.09075"
methods:
  - method:thinkprior
cites:
  - paper:grpo
  - paper:dapo
tags:
  - post-training
  - rlvr
  - data-policy
  - thinkprior
---

# ThinkPrior: Zero-Rollout Difficulty Priors for Cold-Start Prompt Selection in RLVR

## Abstract Summary
Under KL-free GRPO, all-correct or all-wrong groups have identically zero group-relative advantages. Uniform sampling spends 39% of a run's rollouts on these silent groups (37.9% of early prompt groups). History-based selectors must spend target-policy rollouts before they can rank unseen prompts. ThinkPrior builds a zero-rollout difficulty prior from one offline verifier-scored pass of an external anchor, initializes a Beta posterior, selects by expected learnability (with a dispersion penalty that prefers better-known difficulty at equal mean), then updates from training outcomes. Loss and optimizer are unchanged. On Qwen2.5-Math-7B across sixteen seeds, early silent groups fall from 23.8% to 10.6% (55% relative) and wasted rollouts through step 30 fall 19%, with no detected final-accuracy difference (+0.7, interval [-2.2, 3.5]). ThinkPrior+DAPO keeps a 3840-rollout update budget while cutting generated rollouts 10.6% (8256→7381).

## Key Contributions
1. **Silent-group waste**: 39% of uniform GRPO rollouts contribute no KL-free reward-advantage gradient.
2. **Zero-rollout prior**: one external-anchor verifier pass before the first target-policy selection.
3. **Expected-learnability selection** with a dispersion penalty (the reverse of uncertainty sampling).
4. **No loss change**: plug-in on GRPO/DAPO-family trainers.

## Empirical Highlights
- Early silent groups 23.8%→10.6% (16 seeds; 95% interval [-16.4, -9.9], d=-2.95).
- Final accuracy null: +0.7 points, interval [-2.2, 3.5]. Fixed-budget 250-prompt pool reallocates rather than nets (full-run discards 968 vs 885).
- ThinkPrior+DAPO: early waste -65.4%, generated rollouts 8256→7381 at the same 3840 update budget.

## Open Source Repository & Resources
- Project: `https://shatianming5.github.io/thinkprior/`
- No official GitHub as of 2026-09-09.
