---
id: task:mechanism-grounded-agentic-rl-env
type: task
title: "Mechanism-Grounded Agentic RL Environment Synthesis"
domain: "post-training"
summary: "Synthesize diverse long-horizon agentic RL environments by solving a mathematical mechanism first, then rendering stateful tools whose dynamics and verifiers are inherited from that solution."
scope: "Env factories that start from solved mechanisms / hidden dynamics (VHD-Play). Not source-code coding env factories (CodeMidas), not AppWorld coverage, not async trainers."
out_of_scope:
  - "Source-code-only coding-agent RL env construction (CodeMidas)"
  - "AppWorld TGC / programmatic checker coverage (CANOPY)"
  - "Async straggler replay (SAO)"
  - "SWE issue→patch harness (mini-SWE-agent)"
redirects:
  - when: "source-code coding RL envs"
    to: "task:coding-agent-rl-environment-construction"
  - when: "AppWorld coverage"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "async stragglers"
    to: "task:agentic-async-rl"
current_sota:
  - method: method:vhd-play
    as_of: "2026-09-24"
    benchmark: "five-family agentic diagnostic / E-Commerce Bench"
    metric: "mean agentic score; bankruptcy-free completion"
    value: "0.204→0.815 on diagnostic; exceeds Qwen3.7-Max on E-Commerce Bench"
    notes: "VHD-Play (2609.27321). Method status active. Does not replace CodeMidas."
methods:
  - method:vhd-play
  - method:codemidas
  - method:canopy
  - method:sao
  - method:mini-swe-agent
last_reviewed: "2026-09-24"
tags:
  - post-training
  - agentic
  - environments
  - vhd-play
---

# Mechanism-Grounded Agentic RL Environment Synthesis

## Problem Definition
Long-horizon agent RL needs diverse interactive environments with dependable outcome signals. This task is the factory that starts from a solved mathematical mechanism, then renders stateful tools whose dynamics and verifiers are inherited from that solution. The player recovers hidden parameters through interaction.

This is **not** a source-code coding env factory, not AppWorld coverage, and not an async trainer.

## Evaluation Protocol
- **Primary Benchmarks**: five-family agentic diagnostic (train three, eval five), held-out and unseen mechanism families, E-Commerce Bench, BFCL V4 interaction cells.
- **Evaluation Pitfalls**: Do not treat written-out accuracy on \(M(\theta)\) as the agentic score. Do not treat a DeepSWE / CodeMidas lift as this task.

## SOTA Recommendation (as of 2026-09-24)
- **Primary Method (this task only)**: **VHD-Play** (`method:vhd-play`, `paper:vhd-play` `arXiv:2609.27321`). Status `active`. Listed here as first hop; method `sota_for` stays empty.
- **Not This Task**: `method:codemidas` remains source-code coding-agent RL env construction; `method:canopy` remains checker-protocol outcome-only RL; `method:sao` remains async stragglers; `method:mini-swe-agent` remains the issue-to-patch loop.
