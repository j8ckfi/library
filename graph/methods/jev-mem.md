---
id: method:jev-mem
type: method
title: "Jev-Mem"
category: "agent-memory"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "incremental playbook with execution feedback across tasks"
    reason: "ACE remains the default agent-memory SOTA; Jev-Mem is System-One control of a multi-relational store"
    use_instead: "method:ace"
  - when: "repository-grounded procedural skills before interaction experience"
    reason: "Code2Skill synthesizes verified skill records from source code; Jev-Mem organizes conversational / interaction memory"
    use_instead: "method:code2skill"
  - when: "long-lived persona OS-style paging"
    reason: "MemGPT is the persona/OS memory alternative"
    use_instead: "method:memgpt"
  - when: "dumped corpus much larger than the window"
    reason: "RLM offloads the prompt; Jev-Mem retrieves from a structured store"
    use_instead: "method:rlm"
  - when: "SWE patch loop with no persistent memory"
    reason: "bash ReAct does not need a System-One memory plane"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "System-One controller (Jev / typed Noul and Choice decisions) plus an OpenAI-compatible System-Two answer model. Default paper eval: GPT-4o-mini judge and answer on LoCoMo."
  - "Canonical observations are retained; selectivity is in relation construction and retrieval, not irreversible discard at ingest."
  - "Code: libingzheren/Jev-Mem. Demo runs offline with mock decisions."
last_reviewed: "2026-09-22"
papers:
  - paper:jev-mem
recipes:
  - recipe:jev-mem
claims:
  - benchmark: "LoCoMo LLM-as-a-Judge overall, GPT-4o-mini"
    metric: "judge score"
    value: 0.777
    baseline: "MAGMA 0.700 (+11.0% relative); Nemori 0.590; A-MEM 0.580; MemoryOS 0.553; full context 0.481"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.23986"
    notes: "Table 1. Multi-Hop 0.623 / Open-Domain 0.618 / Single-Hop 0.802 / Adversarial 0.962. Temporal 0.637 vs MAGMA 0.650. ACE stays memory SOTA."
  - benchmark: "LoCoMo memory construction time and query latency"
    metric: "build seconds / query seconds"
    value: "158 s / 0.93 s"
    baseline: "fastest build Nemori 1,044 s (6.6×); fastest query MAGMA 1.47 s (−36.7%)"
    date: "2026-09-22"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.23986"
    notes: "Table 2. A-MEM/MemoryOS construction >3,000 s. Full-context query 1.74 s."
tags:
  - agents
  - agent-memory
  - jev-mem
  - active
---

# Jev-Mem

## Method Overview
Jev-Mem is a System-One / System-Two agentic memory architecture. System One is a typed control plane: memory typing, redundancy, semantic / temporal / causal / entity relations on the write path; query routing, budget allocation, graph traversal, candidate scoring, and adaptive stopping on the read path. The data plane keeps canonical observations plus four relational views and vector/lexical indexes. System Two (an LLM) runs only for hard reasoning and answer synthesis.

Decisions are bounded (propositions or a small choice set), not generated text. ACE remains the playbook/memory default. Code2Skill remains the repository-grounded skill bank. This is the System-One-controlled store.

## When to Use
- Long-horizon conversational / interaction memory where LLM-on-the-critical-path for typing, routing, and stop is the cost, and you can run a typed System-One controller.

## When NOT to Use
- Incremental execution-feedback playbook → `method:ace`. Skills from source code → `method:code2skill`. Persona paging → `method:memgpt`. Dumped prompt → `method:rlm`. SWE bash with no store → `method:mini-swe-agent`.

## Relation to Existing SOTA
- Active on `task:agent-memory` alongside ACE and Code2Skill. Does **not** enter `current_sota`. Does **not** supersede `method:ace` or `method:code2skill`.

## Gotchas & Failure Modes
- LoCoMo + GPT-4o-mini is not AppWorld. Do not retarget ACE from these numbers.
- Live runs need TypeSafe (Jev) and an OpenAI-compatible answer model. The demo uses mock decisions and does not measure judge score.
- Temporal score does not beat MAGMA (0.637 vs 0.650). Overall still leads.
