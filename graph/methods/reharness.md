---
id: method:reharness
type: method
title: ReHarness
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: multi-stage agent capability stacking / routed LoRA experts
  reason: ACLArena remains weight-space CL; ReHarness revises a textual harness online
  use_instead: method:aclarena
- when: write-time playbook memory (ACE)
  reason: ACE writes a playbook; ReHarness backward-revises retrieved reflections after each instance
  use_instead: method:ace
- when: production kernel (rewind, sandbox, remote, TUI)
  reason: omp2 remains the kernel; ReHarness is a textual recurrent harness
  use_instead: method:omp2-harness
assumptions:
- 'Online streaming agent CL without extra replay/validation data. Paper: three CL benches × three LM
  backbones.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:reharness
recipes:
- recipe:reharness
claims:
- benchmark: Three continual-learning benchmarks × three language-model backbones
  metric: vs raw-context, memory/reflection, and prompt-optimization baselines
  value: consistently outperforms those baselines; revisions are source-grounded and improve stability
    and plasticity
  baseline: raw-context; memory/reflection methods; prompt optimization
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12668
  notes: Does not retarget ACLArena or ACE. Abstract does not list a single headline number.
tags:
- agents
- continual-learning
- harness
- reharness
- active
---

# ReHarness

## Method Overview
Retrieve reflections, act, then edit those same reflections using the trajectory you just got. The harness state is text; the backward pass is a rewrite, not a weight update.

## When to Use
- Online agent CL where the playbook overgeneralizes and you cannot keep a replay buffer.

## When NOT to Use
Routed LoRA experts → `method:aclarena`. Write-time playbook → `method:ace`. Production kernel → `method:omp2-harness`.

## Relation to Existing SOTA
Active plug-in on `task:agent-continual-learning` with mentions on `task:agent-harness-runtime` and `task:agent-memory` (`sota_for: []`). Does **not** replace ACLArena, ACE, or omp2.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Backward revision is after the instance; it does not change the action you just took.
- Not a weight-space CL method.
