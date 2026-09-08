---
id: method:iris
type: method
title: "Iris (SFT-RL Climbing Search Agent)"
category: "rl-alignment"
status: sota
sota_for:
  - task:web-search-agent-rl
supersedes: []
do_not_use_for:
  - when: "outcome-only long-horizon agent RL (AppWorld coverage / anti-drift)"
    reason: "Iris is a live-web search train recipe, not sparse-outcome AppWorld coverage"
    use_instead: "method:canopy"
  - when: "variable tool latency / async stragglers is the bottleneck"
    reason: "Partial rollout here is request-level prefix reuse under a co-located schedule, not SAO's async replay"
    use_instead: "method:sao"
  - when: "build a SWE / issue-to-patch harness rather than train a search policy"
    reason: "mini-SWE-agent is the harness first hop"
    use_instead: "method:mini-swe-agent"
  - when: "the problem is folding a long tool trajectory into a small active context"
    reason: "Iris trains the search policy; FoldGRPO folds history"
    use_instead: "method:foldgrpo"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "Dense labeled RLVR stays CISPO"
    use_instead: "method:cispo"
assumptions:
  - "Live search/scrape tools, a unique verifiable answer, and an in-cluster judge. Paper init: Qwen3.6-35B-A3B (mini) / Qwen3.5-397B-A17B (pro), 256K context."
  - "SFT: 2 epochs, global batch 64, max seq 262144. RL: Relax engine; GenRM + summarizer are in-cluster Qwen3.5-397B-A17B FP8. ~2× over-sampling headroom for partial rollout."
  - "Default reported decode uses discard-all CM (DeepSeek-V3.2). Publish no-CM numbers too. Single ReAct, no sub-agents, no test-time verification."
last_reviewed: "2026-09-08"
papers:
  - paper:iris
recipes:
  - recipe:iris
claims:
  - benchmark: "Iris-mini 35B-A3B BrowseComp / BrowseComp-ZH / DeepSearchQA / HLE-text (discard-all CM)"
    metric: "accuracy / F1 (DeepSearchQA)"
    value: "82.2 / 84.8 / 86.9 / 52.3"
    baseline: "XYZ-Aquila-mini 78.8 / 82.9 / 89.5 / 51.1; Agents-A1 BrowseComp 75.5"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04304"
    notes: "Table 1. Best overall in 30-35B open-source on three of four benches. DeepSearchQA loses to Aquila-mini 89.5."
  - benchmark: "Iris-pro 397B-A17B BrowseComp / BrowseComp-ZH / DeepSearchQA / HLE-text (discard-all CM)"
    metric: "accuracy / F1 (DeepSearchQA)"
    value: "88.6 / 85.1 / 92.9 / 56.4"
    baseline: "XYZ-Aquila-pro 84.8 / 85.1 / 92.5 / 53.3; Nex-N2-Pro BrowseComp 83.7"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04304"
    notes: "Table 1. Ties Aquila-pro on BrowseComp-ZH. Frontier Kimi-K3 BrowseComp 91.2 still ahead."
  - benchmark: "Iris-mini / Iris-pro BrowseComp without CM"
    metric: "accuracy"
    value: "64.7 / 72.6"
    baseline: "FORT-Searcher w/o 55.9; OpenSeeker-v2 w/o 46.0; REDSearcher w/o 42.1"
    date: "2026-09-08"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04304"
    notes: "Table 2. discard-all then +17.5 / +16.0 to the Table 1 numbers. CM is load-bearing; do not cite only the managed scores."
tags:
  - post-training
  - agentic
  - web-search
  - sft-rl-climbing
  - iris
  - sota
---

# Iris (SFT-RL Climbing Search Agent)

## Method Overview
End-to-end search-agent recipe, not a new RL kernel. Reverse-construct multi-hop questions from a web hyperlink graph, filter teacher ReAct trajectories (correct / non-degenerate / deep, then turn-level KEEP/MASK), SFT, then live-search group-relative RL with an in-cluster judge and page summarizer. Over-long sessions are aborted at the request level and resumed from the committed prefix (truncated IS). Alternate SFT and RL: from each RL group keep queries with $0 < \bar{R}(q) \le 1/2$, require $\ge K_{\mathrm{rft}}$ tool turns, take the shortest successful trajectory, and SFT on that set (**climbing**).

Default eval is discard-all context management. The policy is a single ReAct loop (SEARCH, SCRAPE). This does not replace CANOPY, SAO, mini-SWE-agent, FoldGRPO, or CISPO.

## When to Use
- Training a live-web multi-hop search agent at tens-to-hundreds of billions of parameters.
- You can host an in-cluster judge/summarizer and live search, and you will report both CM and no-CM.

## When NOT to Use
- AppWorld coverage / anti-drift → `method:canopy`.
- Async stragglers → `method:sao`.
- SWE harness → `method:mini-swe-agent`.
- Trajectory folding → `method:foldgrpo`.
- Dense math/code Pass@1 → `method:cispo`.

## Relation to Existing SOTA
- First hop for `task:web-search-agent-rl` only. Does **not** supersede `method:canopy`, `method:sao`, `method:mini-swe-agent`, `method:foldgrpo`, or `method:cispo`.
- Partial rollout is not SAO. Climbing is not CANOPY group scaling. Observation summaries are not FoldGRPO.

## Gotchas & Failure Modes
- Context management moves BrowseComp by +16 to +21 points. Quote Table 2 alongside Table 1.
- Iris-mini is not best on DeepSearchQA (86.9 vs Aquila-mini 89.5).
- discard-all+retry (Iris-pro BrowseComp 90.3) is extra full attempts, not the default report.
- Hugging Face dataset/space URLs for the benches are blocked at search, scrape, and the tool manager.
- Official BrowseComp-ZH labels can disagree with source material (paper Appendix A, Q85).
