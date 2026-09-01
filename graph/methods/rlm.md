---
id: method:rlm
type: method
title: "Recursive Language Models (RLM)"
category: "agent-recursion"
status: sota
sota_for:
  - task:long-context-prompt-offload
supersedes: []
do_not_use_for:
  - when: "GitHub-issue-to-patch / SWE harness"
    reason: "RLM is dumped-prompt REPL offload, not a bash coding loop"
    use_instead: "method:mini-swe-agent"
  - when: "long tool/web/SWE trajectory with folding"
    reason: "trajectory folding is FoldGRPO, not prompt-as-REPL"
    use_instead: "method:foldgrpo"
  - when: "training an async agent policy"
    reason: "RLM is inference offload"
    use_instead: "method:sao"
  - when: "multi-agent orchestration as the long-context strategy"
    reason: "auto MAS is not long-context offload"
    use_instead: "method:single-agent-plus-tools"
  - when: "recursion depth > 1 as default"
    reason: "depth 1 is the working setting; depth 2 overthinks (3.6s → 344.5s)"
    use_instead: "method:rlm"
  - when: "corpus already on a filesystem you can grep"
    reason: "give them a filesystem, not a 10M prompt"
    use_instead: "method:coding-agent-file-offload"
assumptions:
  - "Dense dumped input ≫ window. Prompt is a REPL variable. Depth 1 default."
  - "No 405B-style claims. Do not cite unofficial BrowseComp+ 47.3; paper Table 1 is 91.3."
last_reviewed: "2026-09-01"
papers:
  - paper:rlm
recipes:
  - recipe:rlm-repl
claims:
  - benchmark: "OOLONG-Pairs, GPT-5, RLM depth=1"
    metric: "F1 / score"
    value: 58.0
    baseline: "compaction 0.1 / Claude Code offload 6.5"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.24601"
    notes: "Table 1. Compaction is not a long-context strategy (F1 0.1)."
  - benchmark: "BrowseComp+ 1K, GPT-5, RLM depth=1"
    metric: "accuracy"
    value: 91.3
    baseline: "compaction 70.5 / base 0.0 (OOM)"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.24601"
    notes: "Table 1. Do not cite unofficial 47.3."
  - benchmark: "GPT-5 median vs alternatives"
    metric: "relative gain"
    value: "+26% vs compaction / +130% vs CodeAct+subcalls / +13% vs Claude Code"
    baseline: "compaction / CodeAct+subcalls / Claude Code"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.24601"
    notes: "Paper median summary."
  - benchmark: "RLM-Qwen3-8B SFT (sub-claim)"
    metric: "median relative"
    value: "+28.3%"
    baseline: "untrained RLM-Qwen3-8B"
    date: "2025-12"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2512.24601"
    notes: "1k trajectories, 48 H100-h. Sub-claim on this card, not a new SOTA method."
tags:
  - agents
  - agent-recursion
  - long-context
  - rlm
  - sota
---

# Recursive Language Models (RLM)

## Method Overview
RLM (Zhang, Kraska, Khattab; 2512.24601) replaces `llm.completion(prompt)` with a REPL: the prompt is a variable the model slices in code, with recursive sub-LM calls. Code: `https://github.com/alexzhang13/rlm`, `pip install rlms`. **Depth 1 is the working setting.** Depth 2 overthinks (Wang 2603.02615: 3.6s → 344.5s).

## When to Use
- Dense dumped input much larger than the window.
- Need to programmatically peek/slice rather than compact or stuff.

## When NOT to Use
- SWE harness → `method:mini-swe-agent`.
- Trajectory folding → `method:foldgrpo`.
- Filesystem already available → `method:coding-agent-file-offload`.
- Train SAO → `method:sao`. Multi-agent → do not.

## Gotchas & Failure Modes
- Recursive summary / compaction as the only strategy: OOLONG-Pairs F1 0.1.
- RAH (2606.13643, no public code) cites GPT-5 Codex no-retriever Oolong-Synthetic 71.75% vs RLM 64.38%; complementary file offload, not a replacement of this SOTA.
- λ-RLM (2603.20105) is niche on this task.
