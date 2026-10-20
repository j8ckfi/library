---
id: method:arctic-swe
type: method
title: 'Arctic-SWE'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'variable environment latency / async straggler algorithm'
  reason: 'SAO remains the async algorithm first hop; Arctic-SWE is a SWE co-design baseline'
  use_instead: method:sao
- when: 'GitHub issue to patch / locked SWE harness'
  reason: 'mini-SWE-agent remains the issue-to-patch loop'
  use_instead: method:mini-swe-agent
- when: 'production post-train engine'
  reason: 'Miles remains the engine'
  use_instead: method:miles
assumptions:
- 'Fully async RL on Prime-RL. Overfit-on-small-pool stress test then raw R2E-Gym then curated mix.'
- 'No dedicated public trainer repo as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:arctic-swe
recipes:
- recipe:arctic-swe
claims:
- benchmark: 'SWE-bench Verified / Pro-v1 / Pro-v2, Qwen3.5-4B and 9B'
  metric: 'pass@1'
  value: 'raw R2E-Gym 4B Verified 62.0%; curated 4B 65.0/38.3/59.7 vs 47.4/25.0/37.9; 9B 65.7/39.6/70.2 vs 56.2/31.9/48.8'
  baseline: 'under-tuned async SWE RL on the same models; unsealed eval hacking audit'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24914'
  notes: 'Gated reward, IS control, aligned train/infer engines. CISPO-form token mask. Does not replace SAO, Miles, or mini-SWE-agent.'
tags:
- rl-alignment
- swe
- async-rl
- active
---

# Arctic-SWE

## Method Overview
Arctic-SWE is a model-system co-design baseline for long-horizon SWE RL: gated reward, importance-weight control, aligned train and inference engines, and execution-grounded test repair. Overfitting a small pool is the diagnostic. The 62.0% Verified number is raw R2E-Gym without new algorithms.

## When to Use
- Training a SWE agent with async RL and you need a strong, auditable baseline before claiming an algorithmic win.

## When NOT to Use
Async straggler algorithm → `method:sao`. Issue-to-patch harness → `method:mini-swe-agent`. Engine → `method:miles`.

## Relation to Existing SOTA
Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Does **not** replace SAO, Miles, or mini-SWE-agent.

## Gotchas & Failure Modes
- Unsealed sandboxes inflate eval.
- 65% Verified is not a mini-SWE-agent ranking.
