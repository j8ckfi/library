---
id: method:coding-agent-file-offload
type: method
title: "Coding-agent file offload"
category: "agent-recursion"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "the input is a dumped string with no filesystem"
    reason: "file offload needs files; RLM slices a REPL variable"
    use_instead: "method:rlm"
  - when: "SWE issue-to-patch without a 10M dump"
    reason: "ordinary repo work is mini-SWE-agent"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Corpus lives on disk. Agent uses filesystem + grep. Complementary to RLM."
last_reviewed: "2026-09-01"
papers:
  - paper:coding-agents-long-context
claims:
  - benchmark: "Oolong-Synthetic, GPT-5 Codex no-retriever (RAH citation)"
    metric: "score"
    value: 71.75
    baseline: "RLM 64.38"
    date: "2026-03"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.13643"
    notes: "Cited from RAH 2606.13643 (no public code). Complementary to RLM, not a SWE-harness replacement."
tags:
  - agents
  - long-context
  - file-offload
---

# Coding-agent file offload

## Method Overview
Cao et al. 2603.20432: coding agents are effective long-context processors if you give them a filesystem and grep instead of a 10M-token prompt. Active complementary method on `task:long-context-prompt-offload`. Does not replace RLM (dumped string) or mini-SWE-agent (ordinary repo).

## When to Use
- The corpus can live on disk and be grepped.

## When NOT to Use
- Dumped string, no FS → `method:rlm`.
- Ordinary SWE patch → `method:mini-swe-agent`.
