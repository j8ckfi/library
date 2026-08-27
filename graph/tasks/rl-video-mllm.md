---
id: task:rl-video-mllm
type: task
title: "Reinforcement Learning for Video Multimodal LLMs"
domain: "video-mllm"
summary: "Sample-efficient reinforcement learning and post-training for unified video multimodal large language models without costly chain-of-thought generation."
current_sota:
  - method: method:orarl
    as_of: "2026-08-27"
    benchmark: "TimeLens / GOT-10k / RefCOCO / MeViS / VSI-Bench"
    metric: "perception accuracy & step efficiency"
    value: "Video-ORA-9B achieves 66.0 mIoU, 78.2 AO, 73.1 VSI-Bench at 2.2x SFT step time"
    notes: "OraRL (2608.20492) decouples oracle baseline to prevent advantage inversion and applies sign-balanced pruning."
methods:
  - method:orarl
  - method:sapo
  - method:grpo
tags:
  - video-mllm
  - multimodal-rl
  - post-training
  - reinforcement-learning
---

# Reinforcement Learning for Video Multimodal LLMs

## Problem Definition
Post-training multimodal large language models for fine-grained video perception (temporal grounding, object tracking, spatial segmentation, long-form video QA) is severely sample-starved under standard on-policy group RL. Rollouts rarely generate exact bounding coordinates or timestamps, while chain-of-thought (CoT) expands token length and training latency without proportional precision gains.

## SOTA Recommendation (as of 2026-08-27)
- **Primary Method**: **OraRL** (`method:orarl`, `paper:orarl` `arXiv:2608.20492`) for annotation-as-rollout with decoupled advantage estimation and sign-balanced pruning.
