---
id: method:af1
type: method
title: "AF1"
category: "quantization"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "native 1.58-bit pretraining from scratch"
    reason: "AF1 is genuine 1-bit PTQ of an existing LLM; Sparse-BitNet remains the 2026 BitNet pretrain line"
    use_instead: "method:sparse-bitnet"
  - when: "post-training ternarization of a pretrained LLM at 1.58-bit"
    reason: "ScaleQ-1.58 is the ternary post-train default"
    use_instead: "method:scaleq-158"
assumptions:
  - "PTQ on LLaMA/Qwen/Gemma-class checkpoints under a strict 1.0-BPW budget. EMNLP 2026 Main."
last_reviewed: "2026-09-09"
papers:
  - paper:af1
recipes:
  - recipe:af1
claims:
  - benchmark: "LLaMA / Qwen / Gemma PTQ vs prior 1-bit PTQ"
    metric: "PPL / zero-shot; speed vs BF16"
    value: "best among compared binarization PTQ; ~2.5× inference, >90% memory cut"
    baseline: "prior binarization PTQ (hidden overhead >1 BPW); BF16"
    date: "2026-09-09"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.06161"
    notes: "EMNLP 2026 Main. Does not replace Sparse-BitNet pretrain."
tags:
  - quantization
  - 1bit
  - ptq
  - af1
  - active
---

# AF1

## Method Overview
AF1 is genuine **1.0-BPW PTQ** (NABF + HiSA). Active beside Sparse-BitNet (native 1.58-bit pretrain) and ScaleQ-1.58 (ternary post-train). Does not replace either.

## When to Use
- Deploy an existing dense LLM at a true 1-bit storage budget.

## When NOT to Use
- Train 1.58-bit from scratch → `method:sparse-bitnet`. Ternarize a pretrained LLM → `method:scaleq-158`.

## Relation to Existing SOTA
- Active on `task:1bit-extreme-quantization`. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- GitHub URL in the paper 404'd at ingest (2026-09-09). Confirm the repo before depending on it.
