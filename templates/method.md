---
id: method:template-method
type: method
title: "Method Name"
category: "optimizer" # optimizer | architecture | rl-alignment | quantization | peft | spiking | circuits | codec | servo-control | neural-operator | training-systems | graph-algorithms | data-attribution | agent-harness | agent-protocol | agent-memory | agent-recursion
status: sota # sota | active | superseded | niche | experimental
sota_for:
  - task:template-task
supersedes: []
# superseded_by: method:newer-method # Uncomment if status is superseded
do_not_use_for: []
# - when: "condition where this method is the wrong pick"
#   reason: "why"
#   use_instead: "method:better-method"
assumptions: []
# - "Precondition on hardware scale, data regime, or model family"
last_reviewed: "2026-01-01"
papers:
  - paper:template-paper
recipes:
  - recipe:template-recipe
claims:
  - benchmark: "StandardBenchmark"
    metric: "accuracy"
    value: 92.4
    baseline: "AdamW (88.1)"
    date: "2026-01"
    verified: true
    evidence_level: "preprint" # peer-reviewed | preprint | self-reported | unofficial-repro
    source_url: "https://arxiv.org/abs/XXXX.XXXXX"
    notes: "Verified under standard baseline training run."
tags:
  - optimizer
  - efficiency
---

# Method Name

## Method Overview
Explain the core algorithmic mechanism, mathematical equations, and operational workflow.

## When to Use
- Context 1: When targeting high throughput on large matrix parameters...
- Context 2: When memory constraints prevent full precision optimizer states...

## When NOT to Use
Mirror `do_not_use_for` guards here in prose (agents fuzzy-match prose; validators check YAML).
- Condition: what the reader is actually trying to do -> point to method:<better> or task:<redirect>.

## Gotchas & Failure Modes
- Known stability challenges and hyperparameter sensitivity.
- Incompatibilities with specific layer types (e.g. embeddings vs matrix multiplications).
- Scaling anomalies.
