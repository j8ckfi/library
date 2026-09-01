---
id: method:ace
type: method
title: "ACE (Agentic Context Engineering)"
category: "agent-memory"
status: sota
sota_for:
  - task:agent-memory
supersedes: []
do_not_use_for:
  - when: "recursive summary as the only long-context strategy"
    reason: "RLM paper: compaction OOLONG-Pairs F1 0.1"
    use_instead: "method:rlm"
  - when: "SWE patch loop with no persistent playbook"
    reason: "bash ReAct does not need ACE; do not invent a memory theater"
    use_instead: "method:mini-swe-agent"
  - when: "long-lived persona OS-style paging"
    reason: "MemGPT is the persona/OS memory alternative"
    use_instead: "method:memgpt"
assumptions:
  - "Generator / Reflector / Curator. Incremental bullets, not rewrite. Needs execution feedback."
last_reviewed: "2026-09-01"
papers:
  - paper:ace
recipes:
  - recipe:ace
claims:
  - benchmark: "AppWorld, DeepSeek-V3.1"
    metric: "success %"
    value: 59.4
    baseline: "ReAct 42.4 (+17)"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.04618"
    notes: "Incremental playbook vs ReAct."
  - benchmark: "AppWorld adaptation vs GEPA"
    metric: "latency"
    value: "−82%"
    baseline: "GEPA"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.04618"
    notes: "Offline AppWorld −82.3% latency / −75.1% rollouts vs GEPA."
  - benchmark: "Dynamic Cheatsheet context collapse"
    metric: "tokens @ score"
    value: "18282 tok @ 66.7 → 122 tok @ 57.1"
    baseline: "rewrite-based memory"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.04618"
    notes: "Why incremental bullets, not rewrite."
tags:
  - agents
  - agent-memory
  - ace
  - sota
---

# ACE (Agentic Context Engineering)

## Method Overview
ACE (2510.04618, `github.com/ace-agent/ace`) evolves a playbook with Generator / Reflector / Curator. Updates are incremental bullets, not a full rewrite. Default memory method.

Failure: without feedback, ACE/DC can degrade. Recursive summary is not a long-context strategy (use RLM).

## When to Use
- Agent should accumulate strategies across tasks with execution feedback.

## When NOT to Use
- Dumped prompt → `method:rlm`.
- SWE bash loop with no playbook need → `method:mini-swe-agent`.
- Persona OS paging → `method:memgpt`.

## Gotchas & Failure Modes
- No feedback → ACE/DC can degrade.
- Context collapse from rewrite: Dynamic Cheatsheet 18282@66.7 → 122@57.1.
