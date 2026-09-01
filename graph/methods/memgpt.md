---
id: method:memgpt
type: method
title: "MemGPT"
category: "agent-memory"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "SWE patch loops"
    reason: "OS-style paging is for long-lived persona agents, not mini-SWE-agent"
    use_instead: "method:mini-swe-agent"
  - when: "incremental playbook with execution feedback"
    reason: "ACE is the memory SOTA"
    use_instead: "method:ace"
  - when: "recursive summary as long-context"
    reason: "compaction fails; use RLM"
    use_instead: "method:rlm"
assumptions:
  - "Hierarchical main/archival memory. Long-lived persona agents."
last_reviewed: "2026-09-01"
papers:
  - paper:memgpt
claims:
  - benchmark: "DMR document QA, GPT-4"
    metric: "accuracy"
    value: 92.5
    baseline: "GPT-4 32.1%"
    date: "2023-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2310.08560"
    notes: "32.1% → 92.5%."
  - benchmark: "sleep-time compute (2504.13171)"
    metric: "test-time compute"
    value: "~5× less"
    baseline: "test-time-only memory assembly"
    date: "2025-04"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2504.13171"
    notes: "Complementary: precompute memory offline."
tags:
  - agents
  - agent-memory
  - memgpt
---

# MemGPT

## Method Overview
MemGPT (2310.08560) pages context like an OS. Active on `task:agent-memory` for long-lived persona agents. ACE is current_sota for incremental playbooks. Sleep-time compute (2504.13171) is ~5× less test-time.

## When to Use
- Long-lived persona / OS-style memory.

## When NOT to Use
- SWE patches → `method:mini-swe-agent`. Playbook with feedback → `method:ace`. Dumped prompt → `method:rlm`.
