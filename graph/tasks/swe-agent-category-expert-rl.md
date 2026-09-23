---
id: task:swe-agent-category-expert-rl
type: task
title: "SWE Agent Category-Expert RL"
domain: "post-training"
summary: "Train repository-level SWE agents when pooled RL on heterogeneous categories produces a see-saw, by developing category experts then integrating them into one student."
scope: "Category-aware expert RL plus label-routed integration inside repository-level SWE. First hop is Category-Aware SWE Experts. Not source-only env construction, not async stragglers, not the issue-to-patch harness loop, not the production engine."
out_of_scope:
  - "Data/env construction for coding-agent RL from source code only (CodeMidas)"
  - "Async tool-latency / straggler RL (SAO)"
  - "GitHub issue → patch harness (mini-SWE-agent)"
  - "Production post-train engine (Miles)"
  - "Single-turn math/code Pass@1 RLVR (CISPO)"
redirects:
  - when: "env construction from source only"
    to: "task:coding-agent-rl-environment-construction"
  - when: "async algorithm"
    to: "task:agentic-async-rl"
  - when: "issue-to-patch harness loop"
    to: "task:software-engineering-agent-harness"
  - when: "production stack"
    to: "task:frontier-rl-posttrain-stack"
current_sota:
  - method: method:category-aware-swe-experts
    as_of: "2026-09-23"
    benchmark: "Pro-618 / SWE-bench Multilingual, Logics-SWE-Qwen3.6-27B line"
    metric: "mean resolution vs base"
    value: "Pro-618 58.04% (+5.39); Multilingual 59.00% (+2.78)"
    notes: "Category-Aware SWE Experts (2609.23377). Active first hop. Method status active (not sota). Does not replace CodeMidas / SAO / mini-SWE-agent / Miles."
methods:
  - method:category-aware-swe-experts
  - method:codemidas
  - method:sao
  - method:mini-swe-agent
  - method:miles
  - method:opd
  - method:open-mopd
last_reviewed: "2026-09-23"
tags:
  - post-training
  - agentic
  - swe
  - experts
---

# SWE Agent Category-Expert RL

## Problem Definition
Repository-level SWE is not one homogeneous RL distribution. Service/data fixes, user-facing changes, and systems/tooling patches differ in trajectory length, reward variance, and frequency. Pooled joint RL can raise the aggregate while one category regresses (the category see-saw). This task is splitting that distribution into operational categories, training specialists, and integrating them into one deployable policy.

This is **not** source-only env construction, not async stragglers, not the SWE start loop, and not the frontier engine.

## Evaluation Protocol
- **Primary Benchmarks**: Pro-618 (audit-filtered SWE-bench Pro with Pro-A/B/C), SWE-bench Multilingual; per-category \(\Delta_c\), \(G_{\mathrm{sim}}=\min_c\Delta_c\), see-saw gap.
- **Evaluation Pitfalls**: Do not mix Pro-618 with official Pro public locked-mini ranking. Do not treat expert training as mini-SWE-agent. Do not treat this as CodeMidas.

## SOTA Recommendation (as of 2026-09-23)
- **Primary Method (this task only)**: **Category-Aware SWE Experts** (`method:category-aware-swe-experts`, `paper:category-aware-swe-experts` `arXiv:2609.23377`). Status `active`. Listed here as first hop; method `sota_for` stays empty. SWE Labeler + RRE experts + label-routed MOPD. No external teacher trajectories.
- **Not This Task**: `method:codemidas` remains source-only env construction; `method:sao` remains async; `method:mini-swe-agent` remains issue-to-patch; `method:miles` remains the engine.
