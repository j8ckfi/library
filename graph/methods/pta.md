---
id: method:pta
type: method
title: "PTA (Persistent Teacher Anchoring)"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "plain text distillation without tool execution"
    reason: "PTA's load-bearing piece is delaying and correcting tool calls before they hit the environment; OPD remains the text OPKD default"
    use_instead: "method:opd"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "PTA is a pre-RL distill construction for tool-using agents, not the labeled dense RLVR default"
    use_instead: "method:cispo"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift)"
    reason: "PTA does not scale sparse episode-end groups; CANOPY owns that shelf"
    use_instead: "method:canopy"
  - when: "training async agent RL for straggler latency"
    reason: "Lookahead here fills idle distill capacity under a fixed teacher; SAO is the async policy-train default"
    use_instead: "method:sao"
  - when: "folding a long tool trajectory into a small active context"
    reason: "PTA commits turns; it does not fold history. FoldGRPO is the folding default"
    use_instead: "method:foldgrpo"
  - when: "build a SWE / issue-to-patch harness rather than distill a tool policy"
    reason: "mini-SWE-agent is the harness first hop"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "White-box teacher during rollout construction. Retrieval: Qwen3-32B teacher / Qwen3-1.7B student. Perception: Qwen3-VL-32B / Qwen3-VL-2B-Thinking."
  - "Tool interface is Search-R1-style retrieval or DeepEyes-style bbox zoom. Paper does not cover code execution, DBs, or multi-agent."
  - "veRL + SGLang chunk loop. Distill KL only on committed assistant tokens. Downstream RL restores unrestricted student rollouts."
last_reviewed: "2026-09-07"
papers:
  - paper:pta
recipes:
  - recipe:pta
claims:
  - benchmark: "Search-R1 retrieval (NQ / PopQA / HotpotQA / Musique), Qwen3-1.7B after same-budget RL"
    metric: "macro best@4 EM"
    value: 34.59
    baseline: "OPKD+RL 32.07 / Direct RL 32.66 / base 30.77"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04773"
    notes: "Table 2. +2.5 vs OPKD. EMNLP 2026 Main. Weighted best@4 39.92 vs OPKD 37.09."
  - benchmark: "DeepEyes perception (VStar / HRBench4K / HRBench8K), Qwen3-VL-2B after same-budget RL"
    metric: "macro best@4"
    value: 70.00
    baseline: "OPKD+RL 67.20 / Direct RL 68.10 / base 66.96"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04773"
    notes: "Table 3. +2.8 vs OPKD. Pre-RL Table 4 already leads OPKD on all six metrics (HRBench8K best@4 65.00 vs 58.00)."
  - benchmark: "Lookahead scheduler vs synchronous PTA rollouts"
    metric: "throughput (samples/s)"
    value: 0.644
    baseline: "Synchronous 0.519 (24% lift); 20.2 promoted samples/step"
    date: "2026-09-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.04773"
    notes: "Table 5. Fills idle capacity; does not shorten generation or update time."
tags:
  - post-training
  - distillation
  - tool-use
  - opkd
  - pta
  - active
---

# PTA (Persistent Teacher Anchoring)

## Method Overview
PTA is OPKD for tool-using agents. The student proposes a chunk; the teacher verifies it (keep if inside teacher top-$K$, else replace). Verified chunks accumulate in a pending turn $R$. Only after $R$ is finalized is the assistant turn appended to the committed trajectory $\tau$ and a parsed tool call allowed to hit the environment. Observations then join $\tau$. Distillation is reverse-KL on committed assistant positions only.

That turn boundary is also a persistence unit. Persistent lookahead advances future samples in idle rollout slots and carries unfinished prefixes across student updates because the teacher verifier is fixed.

This is not text-only SKD/SWITCH. Those decide which tokens are kept; PTA decides **when a turn may act**. It is a pre-RL distill phase. Downstream RL restores unrestricted student-driven rollouts. It does not replace CISPO, CANOPY, SAO, FoldGRPO, or plain-text OPD.

## When to Use
- Distilling a smaller tool-using student (search / visual zoom) from a white-box teacher **before** Search-R1- or DeepEyes-style RL.
- When vanilla OPKD lets student tool calls execute into teacher-unvisited states and the later prefixes poison the KL target.

## When NOT to Use
- No tools -> `method:opd`.
- Labeled math/code Pass@1 RLVR -> `method:cispo`.
- Sparse episode-end coverage -> `method:canopy`.
- Async stragglers -> `method:sao`.
- Context folding -> `method:foldgrpo`.
- Building a harness -> `method:mini-swe-agent`.

## Relation to Existing SOTA
- Active plug-in on `task:student-distillation`. Related mention on `task:long-horizon-tool-agent` and `task:agentic-async-rl`. Does **not** supersede `method:opd`, `method:cispo`, `method:canopy`, `method:sao`, or `method:foldgrpo`.
- Distinct from `method:vista` (privileged gold OPSD) and `method:rise` (self-extrapolated teacher, no external model).

## Gotchas & Failure Modes
- Safe timing without in-call replacement is not PTA: the ablation that keeps buffering but ships the student's original tool call falls below OPKD.
- Teacher inference is on the rollout path. Lookahead recovers idle slots; it does not remove verifier cost.
- Paper does not cover code execution, databases, or multi-agent interaction.
- Each setting is trained once; significance is evaluation variation, not seed variation.
- Downstream RL must be unrestricted student rollouts. The pre-RL policy never saw the error states the teacher blocked.
