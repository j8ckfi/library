---
id: task:coding-agent-rl-environment-construction
type: task
title: "Coding-Agent RL Environment Construction"
domain: "post-training"
summary: "Turn implemented OSS functionality into executable coding-agent RL environments using source code as the only task-specific input, then filter for leak-resistant verifiers."
scope: "Data and environment factories for coding-agent RL (explore → behavioral specs → execution-grounded tests → filter). First hop is CodeMidas. Not the SWE loop, not AppWorld coverage, not async stragglers, not a production trainer."
out_of_scope:
  - "Programmatic-checker outcome-only agent RL (CANOPY / AppWorld TGC)"
  - "Variable tool latency / async stragglers (SAO)"
  - "GitHub issue → patch harness (mini-SWE-agent)"
  - "Production post-train engine (Miles)"
  - "Single-turn math/code Pass@1 RLVR (CISPO)"
  - "Live-web multi-hop search-agent training (Iris)"
  - "Category-aware SWE expert RL on already-executable tasks (Category-Aware SWE Experts)"
redirects:
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "variable environment latency / async stragglers"
    to: "task:agentic-async-rl"
  - when: "GitHub issue to patch / SWE harness"
    to: "task:software-engineering-agent-harness"
  - when: "production post-train stack rather than env construction"
    to: "task:frontier-rl-posttrain-stack"
  - when: "single-turn math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "category see-saw on heterogeneous SWE RL (already-executable tasks)"
    to: "task:swe-agent-category-expert-rl"
current_sota:
  - method: method:codemidas
    as_of: "2026-09-21"
    benchmark: "DeepSWE v1.1 / ProgramBench Almost Solved / Terminal-Bench v2.1, MiMo-V2.5 GRPO"
    metric: "pass rate vs initial MiMo-V2.5"
    value: "DeepSWE 10.0→21.7; ProgramBench AS 4.5→21.5; TB v2.1 +8.5pp (63.7→72.2)"
    notes: "CodeMidas (2609.22068). Active env factory. Method status active (not sota). Does not replace CANOPY / SAO / Miles / mini-SWE-agent."
methods:
  - method:codemidas
  - method:canopy
  - method:sao
  - method:mini-swe-agent
  - method:miles
  - method:category-aware-swe-experts
last_reviewed: "2026-09-23"
tags:
  - post-training
  - agentic
  - coding-rl
  - environments
  - codemidas
---

# Coding-Agent RL Environment Construction

## Problem Definition
Coding-agent RL needs diverse tasks with leak-resistant verifiers. Most pipelines seed those tasks from issues, PRs, commits, existing tests, or documentation. This task is the factory that starts from source code alone: explore implemented functionality, write a behavioral specification, build tests whose expected values come from executing the original code, then filter.

This is **not** the SWE loop, not AppWorld coverage, and not an async trainer.

## Evaluation Protocol
- **Primary Benchmarks**: DeepSWE, ProgramBench Almost Solved, Terminal-Bench v2.1, SWE-bench Pro, RepoZero C2Rust after training on the constructed pool.
- **Evaluation Pitfalls**: Do not treat a DeepSWE lift as an AppWorld TGC result. Unfiltered scale can lose to a smaller cleaned pool.

## SOTA Recommendation (as of 2026-09-21)
- **Primary Method (this task only)**: **CodeMidas** (`method:codemidas`, `paper:codemidas` `arXiv:2609.22068`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:canopy` remains checker-protocol outcome-only RL; `method:sao` remains async stragglers; `method:mini-swe-agent` remains the issue-to-patch loop; `method:miles` remains the frontier post-train engine; `method:cispo` remains Pass@1.
- **Not this task (category-aware SWE expert RL)**: `method:category-aware-swe-experts` on `task:swe-agent-category-expert-rl`. Trains experts on already-executable SWE tasks; not a source-only env factory.
