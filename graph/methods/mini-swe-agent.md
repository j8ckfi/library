---
id: method:mini-swe-agent
type: method
title: "mini-SWE-agent"
category: "agent-harness"
status: sota
sota_for:
  - task:software-engineering-agent-harness
supersedes: []
do_not_use_for:
  - when: "training an async agent policy (tool-use RL)"
    reason: "mini-SWE-agent is a harness, not an RL optimizer"
    use_instead: "method:sao"
  - when: "train outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit)"
    reason: "mini-SWE-agent is the eval harness CANOPY used on SWE-bench; it is not the train protocol"
    use_instead: "task:outcome-only-long-horizon-agent-rl"
  - when: "dumped corpus much larger than the context window"
    reason: "bash ReAct does not slice a 10M-token prompt"
    use_instead: "method:rlm"
  - when: "long tool/web trajectory with a small active context"
    reason: "this is trajectory folding, not a SWE loop"
    use_instead: "method:foldgrpo"
  - when: "planner-coder-tester multi-agent theater for a single patch"
    reason: "MAC: successful artifacts are simple ReAct; auto MAS is theater"
    use_instead: "method:single-agent-plus-tools"
  - when: "GUI / OS desktop computer-use"
    reason: "repo patching is not OSWorld"
    use_instead: "method:claude-computer-use"
  - when: "notes/context management beyond bash on a hard repo"
    reason: "CCA is the equal-model alternative when you need notes"
    use_instead: "method:cca"
  - when: "building a durable coding-agent engine (rewind/fork/remote/sandbox/TUI)"
    reason: "mini-SWE-agent is the SWE-bench start/eval loop, not a production harness kernel"
    use_instead: "method:omp2-harness"
assumptions:
  - "Locked SWE-bench mini harness; bash-only ReAct; linear history; independent subprocess.run actions."
  - "Model quality, not scaffold complexity, is the ranking variable on official boards."
last_reviewed: "2026-09-02"
papers:
  - paper:mini-swe-agent
  - paper:mac-meta-agent
recipes:
  - recipe:mini-swe-agent
claims:
  - benchmark: "SWE-bench Verified (official JSON, locked mini harness)"
    metric: "resolved %"
    value: 76.8
    baseline: "author mini >74%; OpenHands+GPT-5 official JSON 71.8"
    date: "2026-02"
    verified: true
    evidence_level: "unofficial-repro"
    source_url: "https://www.swebench.com/"
    notes: "mini + Claude 4.5 Opus (high), 2026-02-17. Do not mix with official JSON 79.2% (Live-SWE-agent tie, different row) or vals.ai 97%."
  - benchmark: "vals.ai SWE-bench Verified (locked mini)"
    metric: "resolved %"
    value: 97.0
    baseline: "DeepSeek V4 Pro 0813 96.40 on the same vals.ai locked-mini board"
    date: "2026-09"
    verified: true
    evidence_level: "unofficial-repro"
    source_url: "https://www.vals.ai/"
    notes: "Claude Opus 5 97.00%. Different snapshot/models from official JSON 76.8% / 79.2%. Record both; do not mix."
  - benchmark: "SWE-bench Pro public (Scale, locked mini)"
    metric: "resolved % mean ± std"
    value: "61.50 ± 3.10"
    baseline: "locked mini ranking bench as of 2026-09"
    date: "2026-09"
    verified: true
    evidence_level: "unofficial-repro"
    source_url: "https://scale.com/leaderboard/swe_bench_pro_public"
    notes: "Muse Spark 1.1. Ranking bench now. Not SWE-bench Verified."
tags:
  - agents
  - agent-harness
  - swe-bench
  - mini-swe-agent
  - react
  - sota
---

# mini-SWE-agent

## Method Overview
mini-SWE-agent is a ~100-line bash ReAct loop: no tools except bash, linear message history, each action via independent `subprocess.run` (swap to `docker exec` for sandboxing). It is the 2026 winning *design* for software-engineering agents and the official SWE-bench locked harness. Cite `paper:mini-swe-agent` (SWE-agent 2405.15793) plus `https://github.com/SWE-agent/mini-swe-agent`.

MAC (2606.04455): code agents given 12–24h to write an agent; only 5/39 configs beat a human baseline; winners converge on this kind of simple ReAct loop and still fail to beat Terminus-2 / OpenHands.

## When to Use
- Default first hop for "I need to build an agent" / GitHub-issue-to-patch.
- Locked-harness SWE-bench Verified or SWE-bench Pro model ranking.

## When NOT to Use
- Train async RL → `method:sao` / `task:agentic-async-rl`.
- Dumped 10M-token prompt → `method:rlm`.
- Long tool trajectory folding → `method:foldgrpo`.
- Multi-agent planner-coder-tester for one patch → still this loop, not MAS.
- GUI desktop → `method:claude-computer-use`.
- Need notes/context mgmt beyond bash → `method:cca`.
- Durable production engine (rewind/fork/remote/sandbox/TUI) → `method:omp2-harness` / `task:agent-harness-runtime`.

## Gotchas & Failure Modes
- Do not mix vals.ai 97% with official JSON 79.2% or 76.8% (different snapshots/models).
- Stuffing 40 MCP servers into this loop is not the design. One shell is the point.
- Meta-agent search as default: El et al. 2510.06711, expanding prior designs hurts.
