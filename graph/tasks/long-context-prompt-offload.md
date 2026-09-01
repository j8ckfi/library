---
id: task:long-context-prompt-offload
type: task
title: "Long-Context Prompt Offload"
domain: "agents"
summary: "Dense dumped input much larger than the window. The prompt is sliced outside the transformer, not stuffed or compact-summarized."
scope: "Dumped corpus ≫ context window. RLM REPL offload. Not a SWE harness and not trajectory folding."
out_of_scope:
  - "Ordinary SWE issue-to-patch without a dumped 10M prompt"
  - "Long tool/web trajectory folding (small active context)"
  - "Training SAO"
  - "Recursive summary as the only strategy"
redirects:
  - when: "GitHub issue to patch without a dumped corpus"
    to: "task:software-engineering-agent-harness"
  - when: "long tool/web/SWE trajectory with folding"
    to: "task:long-horizon-tool-agent"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:rlm
    as_of: "2025-12"
    benchmark: "GPT-5 Table 1 OOLONG-Pairs / BrowseComp+ 1K (depth=1)"
    metric: "score"
    value: "OOLONG-Pairs 58.0 vs compaction 0.1 vs Claude Code offload 6.5; BrowseComp+ 1K 91.3 vs compaction 70.5 vs base 0.0 OOM"
    notes: "Depth 1 working setting. Do not cite unofficial BrowseComp+ 47.3. Do not replace mini-SWE-agent."
methods:
  - method:rlm
  - method:coding-agent-file-offload
  - method:lambda-rlm
  - method:rah
tags:
  - agents
  - agent-recursion
  - long-context
  - rlm
---

# Long-Context Prompt Offload

## Problem Definition
The input is a dense dumped string far larger than the model window. Do not compact it (OOLONG-Pairs F1 0.1). Do not treat this as a SWE harness.

## Evaluation Protocol & Benchmarks
- OOLONG-Pairs, BrowseComp+ 1K, paper Table 1. Depth 1.
- Complementary filesystem+grep (2603.20432 / RAH citation 71.75 vs RLM 64.38) is a different shape: files on disk, not a 10M prompt.

## SOTA Landscape
- **current_sota**: RLM (`method:rlm`).
- **Active**: coding-agent file offload.
- **Niche**: λ-RLM, RAH (no public code).
- Recursion depth >1 is not default (3.6s → 344.5s).
