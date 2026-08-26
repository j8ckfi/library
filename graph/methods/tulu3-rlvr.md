---
id: method:tulu3-rlvr
type: method
title: "Tülu-3 Stack (SFT -> On-Policy DPO -> RLVR)"
category: "rl-alignment"
status: sota
sota_for:
  - task:instruct-sft-alignment
supersedes:
  - method:ppo-rlhf
papers:
  - paper:tulu3-rlvr
recipes:
  - recipe:simpo-alignment
claims:
  - benchmark: "AlpacaEval 2 / Arena-Hard / IFEval / GSM8k"
    metric: "open instruction benchmark average"
    value: "Leading Open Post-Training Stack"
    baseline: "RM-only RLHF / Llama 3.1 Post-Training"
    date: "2024-11"
    verified: true
    notes: "Curated SFT -> on-policy DPO -> RLVR (verifiable rewards without learned reward model noise)."
tags:
  - post-training
  - alignment
  - rlvr
  - tulu3
---

# Tülu-3 Stack (SFT -> On-Policy DPO -> RLVR)

## Method Overview
The Tülu-3 post-training pipeline is the state-of-the-art open-source recipe for creating high-capability chat and instruct models:
1. **Curated SFT**: High-quality, decontaminated skill mixes (math, coding, IFEval constraint following, multi-turn chat).
2. **On-Policy DPO**: Preference pairs generated directly from the fine-tuned model checkpoint.
3. **RLVR (Reinforcement Learning with Verifiable Rewards)**: Scaling RL with deterministic ground-truth checkers (test cases, format parsers, exact answers) rather than noisy learned reward models.

## Supersession
- Supersedes learned-RM-only RLHF as the standard open alignment path.
