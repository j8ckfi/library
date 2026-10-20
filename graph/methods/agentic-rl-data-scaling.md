---
id: method:agentic-rl-data-scaling
type: method
title: 'Agentic RL Data Scaling'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'source-code coding RL env factory'
  reason: 'CodeMidas constructs envs; this card allocates synthesis budget across axes'
  use_instead: method:codemidas
- when: 'outcome-only AppWorld coverage'
  reason: 'CANOPY remains coverage first hop'
  use_instead: method:canopy
assumptions:
- 'Agentic RL data is a tensor over environment, task, and trajectory plus a reward-density control. NeurIPS 2026.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:agentic-rl-data-scaling
recipes:
- recipe:agentic-rl-data-scaling
claims:
- benchmark: 'Compute-optimal agentic RL allocation; Qwen3-8B GRPO isoFLOP splits'
  metric: 'fitted exponents of env/task/trajectory/model vs compute C'
  value: 'D_E* ∝ C^0.34; D_T* ∝ C^0.27; D_τ* ∝ C^0.13; N* ∝ C^0.26'
  baseline: 'scalar token-count scaling; matched-token GRPO with a different axis split'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23946'
  notes: 'Environment axis outpaces trajectories. Does not replace CodeMidas or CANOPY.'
tags:
- rl-alignment
- scaling-laws
- agentic-rl
- active
---

# Agentic RL Data Scaling

## Method Overview
Fits per-axis scaling laws for agentic RL data: environment, task, and trajectory cardinalities plus a reward-density control. The compute-optimal recipe spends more of a synthesis budget on environments than on extra trajectories.

## When to Use
- Allocating a synthesis budget across env generators, task generators, and extra rollouts.

## When NOT to Use
Building the env factory → `method:codemidas`. Sparse-outcome coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:coding-agent-rl-environment-construction` (`sota_for: []`). Does **not** replace CodeMidas, CANOPY, or SAO.

## Gotchas & Failure Modes
- Exponents are fitted on the paper's testbeds; world vs structure diversity changes the environment axis.
- Not a new RL loss.
