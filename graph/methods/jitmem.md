---
id: method:jitmem
type: method
title: "JitMem (Just-in-Time Memory)"
category: "agent-memory"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "incremental playbook with execution feedback (write-time bullets)"
    reason: "ACE remains agent-memory SOTA"
    use_instead: "method:ace"
  - when: "System-One typed memory control plane"
    reason: "Jev-Mem"
    use_instead: "method:jev-mem"
  - when: "repository-grounded skills from source before interaction"
    reason: "Code2Skill"
    use_instead: "method:code2skill"
assumptions:
  - "Keep raw trajectories. Curate at read time from the current task plus retrieved traces. Train the curator from immediate task success (GRPO); freeze the executor."
  - "Paper: ALFWorld / WebShop / τ²-bench. Retriever is BM25 over task descriptions. Quality-gated bank updates."
  - "No public GitHub as of 2026-09-24."
last_reviewed: "2026-09-24"
papers:
  - paper:jitmem
recipes:
  - recipe:jitmem
claims:
  - benchmark: "ALFWorld success rate, Qwen3-8B executor"
    metric: "absolute SR vs strongest write-time baseline"
    value: "77.4 (+16.2)"
    baseline: "SkillOS 61.2; ReasoningBank 55.7; no memory 47.9"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.27334"
    notes: "Table 1. ACE stays playbook/memory SOTA. Not AppWorld."
  - benchmark: "WebShop success rate, Qwen3-8B executor"
    metric: "absolute SR vs strongest write-time baseline"
    value: "32.8 (+16.3)"
    baseline: "SkillOS 16.5"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.27334"
    notes: "Table 1. WebShop Score 61.1 vs SkillOS 40.6 (+20.5)."
  - benchmark: "τ²-bench success vs strongest write-time baseline"
    metric: "absolute SR lift"
    value: "+3.9"
    baseline: "strongest write-time baseline in the paper"
    date: "2026-09-24"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.27334"
    notes: "Abstract. Untrained read-time curator is already competitive; training compounds."
tags:
  - agents
  - agent-memory
  - jitmem
  - active
---

# JitMem (Just-in-Time Memory)

## Method Overview
Write-time memory (ACE-style playbooks, skills, reflections) decides what to keep before the future query is known. JitMem stores raw trajectories and curates at read time. Retrieve top-\(k\) traces (BM25 on the task text), then a curator synthesizes a compact payload conditioned on the current task. The payload is consumed immediately, so the curator trains with GRPO against same-task success of a frozen executor. Quality-gated storage keeps only judged-successful traces.

ACE remains the incremental playbook default. Code2Skill remains repository-grounded skills. Jev-Mem remains the System-One control plane.

## When to Use
- Persistent episodic memory where write-time irreversible summaries are the wrong abstraction, and you can train (or even just prompt) a read-time curator from immediate task success.

## When NOT to Use
- Write-time execution-feedback playbook → `method:ace`. Typed System-One memory ops → `method:jev-mem`. Skills from source before interaction → `method:code2skill`.

## Relation to Existing SOTA
- Active on `task:agent-memory` beside ACE / Code2Skill / Jev-Mem. Does **not** enter `current_sota`. Does **not** supersede `method:ace`.

## Gotchas & Failure Modes
- ALFWorld / WebShop / \(\tau^2\) are not AppWorld. Do not retarget ACE from these numbers.
- No public code as of 2026-09-24.
- Untrained read-time curation already carries much of the gain; RL on the curator is compounding, not the whole method.
- The executor stays frozen. Do not backprop through the agent loop "to be safe."
