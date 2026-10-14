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
  - "Mechanism-first stateful tool envs from solved math dynamics (VHD-Play)"
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
  - when: "mechanism-first stateful tool envs (not OSS source)"
    to: "task:mechanism-grounded-agentic-rl-env"
  - when: "from-scratch program reproduction envs / Program-Agent (not issue-to-patch, not OSS source factory)"
    to: "method:programgym"
  - when: "long-horizon terminal-agent data engine / pre-completed work detection (TerminalHorizon)"
    to: "method:terminalhorizon"
  - when: "fork RL rollouts from the agent's own failure states (ReTerm / recovery training)"
    to: "method:reterm"
current_sota:
  - method: method:codemidas
    as_of: "2026-09-21"
    benchmark: "DeepSWE v1.1 / ProgramBench Almost Solved / Terminal-Bench v2.1, MiMo-V2.5 GRPO"
    metric: "pass rate vs initial MiMo-V2.5"
    value: "DeepSWE 10.0→21.7; ProgramBench AS 4.5→21.5; TB v2.1 +8.5pp (63.7→72.2)"
    notes: "CodeMidas (2609.22068). Active env factory. Method status active (not sota). Does not replace CANOPY / SAO / Miles / mini-SWE-agent."
methods:
  - method:reterm
  - method:terminalhorizon
  - method:t1-terminal-rl
  - method:programgym
  - method:codemidas
  - method:canopy
  - method:sao
  - method:mini-swe-agent
  - method:miles
  - method:category-aware-swe-experts
  - method:vhd-play
last_reviewed: '2026-10-14'
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
- **Not this task (mechanism-first tool envs)**: `method:vhd-play` on `task:mechanism-grounded-agentic-rl-env`. Solved math mechanism → stateful tools. Does not replace CodeMidas.
- **Optional from-scratch program-reproduction gym (not this first hop)**: `method:programgym` (`arXiv:2610.13395`) 1,648 C/C++/Go/Rust envs; Qwen3.8-27B 34.87%→42.84% SFT / Program-Agent 55.71%. `code_status: announced`. Does not replace CodeMidas or mini-SWE-agent.
- **Optional long-horizon terminal data engine (not this first hop)**: `method:terminalhorizon` (`arXiv:2610.13166`) 1,535 envs / 2,852 traj / avg 52.8 turns; detects pre-completed work and rebuilds. SFT Qwen3.5-27B: TB1.0 55.0 (+8.7); TB2.0 55.8 (+14.2); TB2.1 46.82→60.67; AutomationBench Pass 5.5→17.2. Project zs1314.github.io/TerminalHorizon. Does not replace CodeMidas. Related 122B recipe is `method:t1-terminal-rl`.
- **Optional recovery-fork terminal RL (not this env-factory first hop)**: `method:reterm` (`arXiv:2610.18484`). ReTerm-9B TB2.0 Pass@1 34.8 (+14.6); SWE-Verified 58.4%. Code twothsnd/ReTerm. Does not replace CodeMidas, T1, or TerminalHorizon.
