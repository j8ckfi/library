---
id: method:rewardverse
type: method
title: "RewardVerse (RGPO)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "aligning the video/image generator policy itself"
    reason: "DiffusionOPSD / Self-OPD remain generator post-train defaults"
    use_instead: "method:diffusion-opsd"
  - when: "video MLLM perception RL / annotation-as-rollout"
    reason: "OraRL"
    use_instead: "method:orarl"
assumptions:
  - "Train a video reward model, not the generator. Dynamic rubric (themes/weights/tips) then multi-theme soft-logits scoring. RGPO is two-stage GRPO."
  - "Paper: Qwen2.5-VL-7B RM; 30 preference pairs per EvalVerse dimension (480 total). Downstream GRPO of Wan-2.2-A14B is a use of the RM, not a DiffusionOPSD replacement."
  - "Code: 2kxx/RewardVerse."
last_reviewed: "2026-09-24"
papers:
  - paper:rewardverse
recipes:
  - recipe:rewardverse
claims:
  - benchmark: "EvalVerse 16-dimension pointwise, Joint RGPO"
    metric: "mean PLCC / SRCC"
    value: "0.554 / 0.446"
    baseline: "highest PLCC on 14/16 dimensions; Logic 0.750 vs next-best 0.593"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22947"
    notes: "Table 1. Not a DiffusionOPSD / Self-OPD generator bake-off."
  - benchmark: "VGRB pairwise Acc w/o Tie"
    metric: "accuracy without ties"
    value: "TA 0.623 / VQ 0.660"
    baseline: "VisionReward 0.611 / 0.590; VideoReward is an oracle upper bound (0.722 / 0.756)"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.22947"
    notes: "Table 2. TA is unseen at train time. 30 pairs per dimension."
tags:
  - diffusion
  - video
  - reward-model
  - rewardverse
  - active
---

# RewardVerse (RGPO)

## Method Overview
Unconstrained video RMs map a clip to one scalar and drift: scores pile into a high band or move when the prompt is paraphrased. RewardVerse splits evaluation into rubric generation and scoring. The generator emits query-adaptive themes, weights, and tips without seeing the candidate video. The scorer then reads multi-theme soft-logits against that rubric.

RGPO is two-stage GRPO: warm up the scorer on self-evolving seed rubrics, then jointly train generator and scorer from 30 preference pairs per dimension. DiffusionOPSD / Self-OPD remain generator-policy alignment. OraRL remains video MLLM perception RL.

## When to Use
- You need a stable pointwise video reward model for later generator RL, and unconstrained scalar RMs are collapsing or shifting.

## When NOT to Use
- Aligning the generator policy → `method:diffusion-opsd` / `method:self-opd`. Video MLLM annotation-as-rollout → `method:orarl`.

## Relation to Existing SOTA
- Active video-RM plug-in on `task:posttrain-diffusion`. Does **not** enter `current_sota`. Does **not** replace `method:diffusion-opsd` or `method:self-opd`. Does **not** retarget `task:rl-video-mllm` / `method:orarl`.

## Gotchas & Failure Modes
- Pairwise A/B of two videos is order-sensitive even with a rubric (flip rate 0.562). Deploy pointwise soft-logits.
- VideoReward on VGRB is an oracle upper bound (trained on that set), not a fair baseline.
- Downstream GRPO of Wan-2.2-A14B is evidence that the RM is usable, not a new generator SOTA.
