---
id: task:software-engineering-agent-harness
type: task
title: "Build an Agent (Software Engineering Harness)"
domain: "agents"
summary: "First hop for building an agent: the loop, agent-computer interface, and tools for GitHub-issue-to-patch repo work. Not RL training."
scope: "First hop when you need to build an agent: loop + ACI + tools for repo work. Default is the dumb bash ReAct loop."
out_of_scope:
  - "Training an async agent policy (SAO)"
  - "Math/code RLVR (CISPO)"
  - "GUI / OS desktop computer-use"
  - "Dumped 10M-token corpus prompt offload (RLM)"
  - "Trajectory folding (FoldGRPO)"
  - "Planner-coder-tester multi-agent theater for a single patch"
  - "Meta-agent search as the default design process"
redirects:
  - when: "train asynchronous RL for a tool-use policy"
    to: "task:agentic-async-rl"
  - when: "math-code RLVR with verifiable rewards"
    to: "task:math-code-rl-dense"
  - when: "GUI / OS desktop computer-use"
    to: "task:computer-use-agent"
  - when: "10M-token dumped corpus that does not fit the window"
    to: "task:long-context-prompt-offload"
  - when: "building a production engine (rewind, sandbox, remote, TUI)"
    to: "task:agent-harness-runtime"
last_reviewed: "2026-09-02"
current_sota:
  - method: method:mini-swe-agent
    as_of: "2026-09"
    benchmark: "SWE-bench Pro public (Scale, locked mini) / official Verified JSON / vals.ai locked mini"
    metric: "resolved %"
    value: "Pro Muse Spark 1.1 61.50±3.10 (ranking now); official JSON mini+Claude 4.5 Opus high 76.8% (2026-02-17); vals.ai Claude Opus 5 97.00% / DeepSeek V4 Pro 0813 96.40% (2026-09, different snapshot)"
    notes: "Winning design is the ~100 LOC bash ReAct loop. Do not mix vals.ai 97% with official JSON 79.2%. Do not retarget SAO/CISPO/RLM."
methods:
  - method:mini-swe-agent
  - method:cca
  - method:openhands-codeact
  - method:live-swe-agent
  - method:single-agent-plus-tools
tags:
  - agents
  - agent
  - build
  - agent-harness
  - swe-bench
  - mini-swe-agent
  - react
---

# Build an Agent (Software Engineering Harness)

## Problem Definition
Choose the loop, ACI, and tools for repository-level software engineering (issue → patch). This is **not** training an agent policy. Agents are bad at designing agents (MAC 5/39; prior-design context hurts). First hop is the simple bash ReAct loop, not multi-agent and not SAO. Production engines that must rewind, sandbox, drive remotely, and serve a TUI belong on `task:agent-harness-runtime` (`method:omp2-harness`); this task's current_sota stays mini-SWE-agent.

## Evaluation Protocol & Benchmarks
- **Locked mini harness**: official SWE-bench Verified JSON; Scale SWE-bench Pro public; vals.ai locked mini. Label the board. Do not mix snapshots.
- **Hazards**: mixing vals.ai 97% with official JSON 79.2%; treating OpenHands product numbers as locked-mini; promoting CCA as the default.

## SOTA Landscape
- **Default**: **mini-SWE-agent** (`method:mini-swe-agent`).
- **Active**: CCA when you need notes/context management; OpenHands/CodeAct as production OSS.
- **Niche**: Live-SWE-agent (official JSON 79.2% tie).
- **Not this task**: SAO, CISPO, RLM, FoldGRPO, OSWorld. Production harness kernels (rewind/fork/remote/sandbox/TUI) are `task:agent-harness-runtime`.
