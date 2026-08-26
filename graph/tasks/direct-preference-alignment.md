---
id: task:direct-preference-alignment
type: task
title: "Direct Preference Alignment & Offline Post-Training"
domain: "post-training"
summary: "Offline instruction tuning and preference alignment without online policy rollouts or separate reference model inference."
current_sota:
  - method: method:tulu3-rlvr
    as_of: "2026-08-26"
    benchmark: "AlpacaEval 2 / Arena-Hard"
    metric: "length-controlled win rate"
    value: "Tülu-3 Open Stack"
    notes: "Tülu-3 on-policy DPO + RLVR supersedes standalone offline DPO."
methods:
  - method:tulu3-rlvr
  - method:simpo
  - method:dpo
tags:
  - post-training
  - preference-alignment
---

# Direct Preference Alignment & Offline Post-Training

## Problem Definition
Offline preference optimization trains models to prefer human-chosen responses over rejected alternatives given pairs \((y_w, y_l)\). Standard DPO requires computing forward passes through both the active policy model and a frozen reference model to calculate implicit reward logits, doubling GPU memory usage and leading to length exploitation where verbose answers receive artificially high rewards.

## Evaluation Protocol & Benchmarks
- **Standard Benchmarks**: AlpacaEval 2 (Length-Controlled Win Rate), Arena-Hard-Auto, MT-Bench.
- **Evaluation Hazards**: Verbosity bias and length gaming in standard LLM-as-a-judge evaluators.

## SOTA Landscape
SimPO (Simple Preference Optimization) introduces a length-normalized implicit reward margin directly into the objective, eliminating the need for a frozen reference model during training and surpassing DPO on leaderboards.
