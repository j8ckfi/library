---
id: task:instruct-sft-alignment
type: task
title: "Chat / Instruct SFT & General Alignment"
domain: "post-training"
summary: "Curated supervised fine-tuning, direct preference optimization, and verifiable reward alignment for instruction-following models."
current_sota:
  - method: method:tulu3-rlvr
    as_of: "2026-08-26"
    benchmark: "AlpacaEval 2 / Arena-Hard / IFEval"
    metric: "win rate & constraint satisfaction"
    value: "Open SOTA Stack"
    notes: "Tülu-3 stack: curated SFT -> on-policy DPO -> RLVR (verifiable rewards, no learned RM). Code: allenai/open-instruct."
methods:
  - method:tulu3-rlvr
  - method:simpo
  - method:dpo
tags:
  - post-training
  - instruct
  - alignment
  - rlvr
---

# Chat / Instruct SFT & General Alignment

## Problem Definition
Transforming base pre-trained models into safe, capable, instruction-following conversational assistants without degrading core knowledge.

## SOTA Recommendation (as of 2026-08-26)
- **Tülu-3 Stack**: Curated SFT → on-policy DPO → **RLVR** (Reinforcement Learning with Verifiable Rewards, no learned RM).
- **Implementation**: `allenai/open-instruct`.
- Prefer decontaminated, skill-specific data mixes over generic web scrapes like "just ShareGPT."
- If limited to a single 24GB card over a weekend, skip base pretraining and apply QLoRA/DoRA on a strong instruct checkpoint.
