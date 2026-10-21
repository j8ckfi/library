---
id: method:riseharness
type: method
title: 'RiseHarness'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the kernel; RiseHarness iteratively edits a frozen-weight terminal harness'
  use_instead: method:omp2-harness
- when: 'issue-to-patch / locked eval'
  reason: 'mini-SWE-agent remains the SWE loop'
  use_instead: method:mini-swe-agent
- when: 'regularized harness RSI (annealed edit budget / anti-memorization critic)'
  reason: 'RRSI regularizes harness search; RiseHarness flips mixed-outcome tasks using monitor traces'
  use_instead: method:rrsi
assumptions:
- 'Model weights frozen. Mixed success/fail runs of the same task seed failure analysis.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:riseharness
recipes:
- recipe:riseharness
claims:
- benchmark: 'Long-horizon terminal agents; transfer to unseen benches with the same model'
  metric: 'task success and reliability vs pre-evolution harness; ablation of execution evidence and external research'
  value: 'iteratively folds mechanisms from other harnesses into one harness using mixed success/fail runs and runtime-monitor traces'
  baseline: 'frozen-weight baseline harness; ablations without execution evidence or external research'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27435'
  notes: 'Does not retarget omp2, RRSI, AIDE2, or mini-SWE-agent.'
tags:
- agent-harness
- rsi
- terminal
- active
---

# RiseHarness

## Method Overview
RiseHarness improves a terminal-agent harness with weights frozen. It focuses on tasks that both succeed and fail under the same config, joins agent trajectories with runtime-monitor traces, and searches other harnesses for patches that pass behavioral checks.

## When to Use
- Frozen-weight terminal harness RSI when reliability across repeated runs is the gap, not missing model skill.

## When NOT to Use
Production kernel → `method:omp2-harness`. SWE loop → `method:mini-swe-agent`. Regularized RSI → `method:rrsi`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:omp2-harness`.

## Gotchas & Failure Modes
- Needs mixed-outcome tasks; all-fail or all-success pools give no flip signal.
- Not a production kernel.
