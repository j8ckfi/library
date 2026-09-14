---
id: paper:canvasanneal
type: paper
title: "CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models"
authors:
  - "Blake Olson"
  - "Yuhang Song"
  - "Emmett McQuinn"
  - "Yuan Shangguan"
year: 2026
month: 9
arxiv_id: "2609.13060"
url: "https://arxiv.org/abs/2609.13060"
methods:
  - method:canvasanneal
cites: []
tags:
  - diffusion
  - post-training
  - rl-alignment
  - dlm
  - canvasanneal
---

# CanvasAnneal: Curriculum Reinforcement Learning for Diffusion Language Models

## Abstract Summary
Diffusion language models lag autoregressive models on complex reasoning and tool use. Standard DLM RL hits an exploration bottleneck. CanvasAnneal warm-starts exploration by injecting teacher-generated reasoning traces into the initial diffusion canvas, then anneals that guidance so the model must generate more of the trajectory itself. Host optimizer is diffu-GRPO on LLaDA-7B-A1B-Instruct. Gains over diffu-GRPO on MATH500, Countdown, and Tau2; GSM8K and some tool-use settings remain mixed.

## Key Contributions
1. **Teacher-trace canvas injection** as a training-time prior, not an inference draft.
2. **Curriculum anneal**: remove guidance as reward improves.
3. **Task-dependent DLM RL**: helps MATH500/Countdown/Tau2; not a universal DLM upgrade.

## Empirical Highlights
- MATH500 vs diffu-GRPO: +6.0 / +2.0 / +0.4 at generation lengths 128 / 256 / 512.
- Countdown: +2.73 / +3.91 / +1.96 at those lengths.
- Tau2 average 13.03 vs diffu-GRPO 10.15 (Retail 7.90 vs 6.14, Airline 18.00 vs 12.00, Telecom 13.20 vs 12.30).
- GSM8K: standard diffu-GRPO remains stronger.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-14. TinyZero is a cited Countdown baseline, not this trainer.
