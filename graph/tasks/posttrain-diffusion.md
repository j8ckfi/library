---
id: task:posttrain-diffusion
type: task
title: "Diffusion Post-Training and Reward Alignment"
domain: "diffusion"
summary: "Aligning text-to-image diffusion and flow models with human preferences and task-specific reward functions using on-policy trajectory guidance."
current_sota:
  - method: method:diffusion-opsd
    as_of: "2026-08-27"
    benchmark: "SD 3.5-M / Z-Image-Turbo (10 Evaluators)"
    metric: "held-out reward score & GPU-hours"
    value: "Best in 19/20 reward-matched settings; 40-63% GPU-hr reduction"
    notes: "DiffusionOPSD (2608.24646) converts image-level rewards into bounded intermediate clean-output targets."
  - method: method:self-opd
    as_of: "2026-08-28"
    benchmark: "Flow Matching Visual Alignment (Single & Mixed Reward Benchmarks)"
    metric: "reward score and multi-objective Pareto front"
    value: "Outperforms Flow-GRPO, Flow-OPD, and DiffusionNFT without external task-specific teachers"
    notes: "Self-OPD (2608.26872) provides teacher-free per-step pull-push distillation for flow matching multi-objective alignment."
methods:
  - method:doobpo
  - method:dfr
  - method:schedule-free-diffusion
  - method:scope-t2i
  - method:rpo
  - method:forkgrpo
  - method:representation-guidance
  - method:semicat
  - method:diffusionart
  - method:mend
  - method:diffusion-opsd
  - method:self-opd
  - method:canvasanneal
  - method:rewardverse
  - method:a2d
redirects:
  - when: "likelihood-free RL fine-tune of diffusion/flow policies (DoobPO)"
    to: "method:doobpo"
  - when: "distributional regularization for diffusion/flow reward FT (DFR)"
    to: "method:dfr"
  - when: "Schedule-Free / LR decay vs EMA (not reward alignment)"
    to: "method:schedule-free-diffusion"
  - when: "semantic-span-bounded GRPO prompt rewriting for T2I (SCOPE)"
    to: "method:scope-t2i"
  - when: "online diffusion RL via attention routing (RPO; not score-function noise)"
    to: "method:rpo"
  - when: "aggregation-first reward tilting for diffusion RL (~12× fewer GPU-hrs vs DiffusionNFT / Flow-GRPO-Fast)"
    to: "method:diffusionart"
  - when: "recycle an AR post-training weight delta onto a converted dLLM (not image/flow alignment)"
    to: "task:diffusion-lm-ar-delta-recycle"
  - when: "flow-model RL via proximal velocity matching (~100 updates vs Flow-GRPO ~4k)"
    to: "method:mend"
  - when: "lossless multi-token / diffusion-augmented AR serving, not image-policy alignment"
    to: "task:diffusion-augmented-ar"
  - when: "training a stable video reward model / rubric-guided RM PO"
    to: "method:rewardverse"
  - when: "pixel-space DiT / flow-matching image pretrain (Representation Guidance)"
    to: "task:pixel-diffusion-pretrain"
  - when: "continuous diffusion language model pretrain (not image/flow alignment)"
    to: "task:continuous-diffusion-lm-pretrain"
  - when: "dLLM RL that forks from high-entropy intermediate states (ForkGRPO)"
    to: "method:forkgrpo"
last_reviewed: '2026-10-22'
tags:
  - diffusion
  - post-training
  - alignment
  - generative-models
---

# Diffusion Post-Training and Reward Alignment

## Problem Definition
Aligning generative diffusion and flow models with downstream reward functions (aesthetic quality, text-image alignment, human preference ratings). Endpoint rewards create a structural mismatch because feedback is only observed on decoded final images, while the model operates across multi-step denoising trajectories.

## SOTA Recommendation (as of 2026-09-14)
- **Primary Method (Reward/Self-Distill with Behavior Policy)**: **DiffusionOPSD** (`method:diffusion-opsd`, `paper:diffusion-opsd` `arXiv:2608.24646`) for on-policy self-distillation with bounded intermediate clean-output targets.
- **Teacher-Free Flow Matching / Multi-Objective Alignment**: **Self-OPD** (`method:self-opd`, `paper:self-opd` `arXiv:2608.26872`) for stochastic SDE branching vs deterministic self-reference and reward-level multi-objective fusion without task-specific teachers.
- **Niche discrete-diffusion-LM curriculum RL (not this first hop)**: `method:canvasanneal` (`arXiv:2609.13060`) anneals a teacher-trace canvas on LLaDA-8B. MATH500 +6.0 / +2.0 / +0.4 vs diffu-GRPO. Does not replace DiffusionOPSD, Self-OPD, or Uno.
- **Active aggregation-first diffusion RL (not this first hop)**: `method:diffusionart` (`arXiv:2610.12572`) ~12× fewer GPU-hrs vs DiffusionNFT / Flow-GRPO-Fast on HunyuanVideo-13B. Code vanzll/DiffusionART. Beside MEND / Flow-GRPO / DiffusionNFT. Does not replace DiffusionOPSD or Self-OPD.
- **Active video-RM / RGPO plug-in (not generator alignment)**: `method:rewardverse` (`arXiv:2609.22947`) dynamic rubric + two-stage RGPO for video reward models. EvalVerse Joint mean PLCC 0.554 / SRCC 0.446. Does not replace DiffusionOPSD or Self-OPD. Does not retarget OraRL.
- **Not This Task (AR-delta recycle onto a converted dLLM)**: `method:a2d` on `task:diffusion-lm-ar-delta-recycle` (`arXiv:2610.08108`). Does not replace DiffusionOPSD / Self-OPD / CanvasAnneal.
- **Not This Task**: lossless AR multi-token serving is `method:uno` on `task:diffusion-augmented-ar`. Does not replace this image/flow post-train default.
- **Not this task (pixel-space DiT pretrain)**: `method:representation-guidance` on `task:pixel-diffusion-pretrain` (`arXiv:2610.12978`). Does not replace DiffusionOPSD / Self-OPD.
- **Not this task (continuous diffusion LM)**: `method:semicat` on `task:continuous-diffusion-lm-pretrain` (`arXiv:2610.13834`). Does not replace DiffusionOPSD / Self-OPD.

- **Optional T2I span-pooled GRPO**: `method:scope-t2i` (`arXiv:2610.22264`). +9.48% GeneVal / +7.62% T2I-CompBench vs GRPO. Code MAC-AutoML/SCOPE. Distinct from `method:scope-opsd`. Does not replace DiffusionOPSD / Self-OPD.
- **Optional attention-routing diffusion RL**: `method:rpo` (`arXiv:2610.22282`). Nearly 4x vs Flow-GRPO-style. Distinct from skipped 2610.17767. Does not replace DiffusionART / MEND.
- **Optional distributional reward FT regularizer**: `method:dfr` (`arXiv:2610.24897`). MMD / Frechet / DreamSim vs reverse-KL velocity penalty. SD3.5-M +29% diversity, 36-41x vs Flow-GRPO. Does not replace DiffusionOPSD, Self-OPD, or MEND.
