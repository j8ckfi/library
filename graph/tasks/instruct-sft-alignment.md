---
id: task:instruct-sft-alignment
type: task
title: "Chat / Instruct SFT & General Alignment"
domain: "post-training"
summary: "Curated supervised fine-tuning, direct preference optimization, and verifiable reward alignment for instruction-following models."
current_sota:
  - method: method:olmo-3
    as_of: "2026-08-26"
    benchmark: "AlpacaEval 2 / Arena-Hard / IFEval"
    metric: "win rate & constraint satisfaction"
    value: "Open SOTA Stack"
    notes: "OLMo-3 Dolci (2512.13961); industrial alt Nemotron-Cascade 2 (2603.19220)."
  - method: method:nemotron-cascade-2
    as_of: "2026-08-26"
    benchmark: "Arena-Hard / Multi-Stage SFT"
    metric: "instruction compliance"
    value: "Industrial SOTA Alt"
    notes: "Nemotron-Cascade-2 (2603.19220) for industrial multi-stage SFT."
methods:
  - method:olmo-3
  - method:nemotron-cascade-2
  - method:tulu3-rlvr
  - method:delta-learning
  - method:nemotron-cascade
  - method:simpo
  - method:dpo
  - method:partial-reasoning-traces
last_reviewed: "2026-09-11"
tags:
  - post-training
  - instruct
  - alignment
  - sft
  - dolci
---

# Chat / Instruct SFT & General Alignment

## Problem Definition
Transforming base pre-trained models into safe, capable, instruction-following conversational assistants without degrading core knowledge.

## SOTA Recommendation (as of 2026-09-11)
- **Primary Open Stack**: **OLMo-3 Dolci** (`method:olmo-3`, 2512.13961).
- **Industrial Alternative**: **Nemotron-Cascade-2** (`method:nemotron-cascade-2`, 2603.19220).
- **Optional reasoning-trace shaping**: `method:partial-reasoning-traces` (`arXiv:2609.07103`). Prefer partial/truncated CoT over dumping complete traces. Does not replace OLMo-3 / Cascade.
