---
id: method:dr-grpo
type: method
title: "Dr. GRPO (De-biased Group Relative Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:math-code-rl-dense
  - task:math-code-rl-moe
supersedes:
  - method:grpo
papers:
  - paper:dr-grpo
recipes:
  - recipe:grpo-trl-training
claims:
  - benchmark: "R1-Zero Replication & Mathematical Reasoning"
    metric: "unbiased advantage estimation"
    value: "Eliminates length bias in group advantage estimation"
    baseline: "Vanilla GRPO"
    date: "2025-03"
    verified: true
    notes: "Removes length normalization and sample standard-deviation distortion from group advantage estimates."
tags:
  - rl-alignment
  - reasoning
  - de-biasing
---

# Dr. GRPO (De-biased Group Relative Policy Optimization)

## Method Overview
Dr. GRPO identifies mathematical biases in original GRPO advantage calculations:
1. Standard deviation normalization in small groups skews updates against confident correct answers.
2. Inappropriate length scaling artificially rewards verbose, rambling incorrect responses.
Dr. GRPO removes these distorting normalizations to provide unbiased policy updates.

## Supersession
- Supersedes unpatched GRPO length and standard-deviation normalizations.
