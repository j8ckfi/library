---
id: method:programgym
type: method
title: ProgramGym
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: data/env construction for coding-agent RL from source code (issue-free factory then GRPO)
  reason: CodeMidas starts from implemented OSS; ProgramGym is from-scratch program reproduction
  use_instead: method:codemidas
- when: GitHub issue to patch / SWE harness
  reason: mini-SWE-agent remains the issue-to-patch loop
  use_instead: method:mini-swe-agent
assumptions:
- 'From-scratch program reproduction with black-box tests. Paper: 1,648 envs in C/C++/Go/Rust; ProgramBench;
  Qwen3.8-27B.'
- 'Release promised (`code_status: announced`). No public URL as of 2026-10-12.'
last_reviewed: '2026-10-12'
papers:
- paper:programgym
recipes:
- recipe:programgym
claims:
- benchmark: ProgramBench, Qwen3.8-27B SFT on ProgramGym trajectories then Program-Agent
  metric: program-reproduction success
  value: base 34.87% → SFT 42.84%; Program-Agent 55.71% / 56.25% on base and SFT
  baseline: Qwen3.8-27B without ProgramGym
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13395
  notes: Does not retarget CodeMidas or mini-SWE-agent. Not issue-to-patch.
tags:
- agents
- coding-rl
- environments
- programgym
- active
---

# ProgramGym

## Method Overview
Build a runtime-verified sandbox and black-box tests from a reference repo. Train on trajectories that must discover requirements by exploring the reference, then implement. At inference, isolate analysis / implementation / review with compile-and-recover revisions.

## When to Use
- You want coding-agent RL/SFT for from-scratch program reproduction rather than issue-to-patch.

## When NOT to Use
Source-only env factory → `method:codemidas`. Issue-to-patch harness → `method:mini-swe-agent`.

## Relation to Existing SOTA
Active plug-in on `task:coding-agent-rl-environment-construction` (`sota_for: []`). Does **not** replace CodeMidas or mini-SWE-agent.

## Gotchas & Failure Modes
- **code: announced** as of 2026-10-12; paper says the release is coming.
- Black-box tests hide the reference; leaking the repo into the prompt collapses the task.
- Not SWE-Bench issue-to-patch.
