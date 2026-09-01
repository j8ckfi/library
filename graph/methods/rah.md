---
id: method:rah
type: method
title: "RAH (Recursive Agent Harnesses)"
category: "agent-recursion"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "you need a runnable dumped-prompt recipe"
    reason: "no public code; RLM has github.com/alexzhang13/rlm"
    use_instead: "method:rlm"
assumptions:
  - "2606.13643. No public code. evidence_level preprint. Status niche."
last_reviewed: "2026-09-01"
papers:
  - paper:coding-agents-long-context
claims:
  - benchmark: "Oolong-Synthetic, GPT-5 Codex no-retriever"
    metric: "score"
    value: 71.75
    baseline: "RLM 64.38"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.13643"
    notes: "No public code. Complementary filesystem offload citation, not a new SOTA method."
tags:
  - agents
  - agent-recursion
  - rah
  - niche
---

# RAH (Recursive Agent Harnesses)

## Method Overview
RAH (Lumer et al., 2606.13643) cites GPT-5 Codex no-retriever Oolong-Synthetic 71.75% vs RLM 64.38%. **No public code.** Niche on `task:long-context-prompt-offload`. Do not replace RLM or mini-SWE-agent.

## When to Use
- Literature pointer for filesystem/no-retriever offload vs RLM.

## When NOT to Use
- Need code → `method:rlm` or `method:coding-agent-file-offload`.
