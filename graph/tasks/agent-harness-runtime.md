---
id: task:agent-harness-runtime
type: task
title: "Agent Harness Runtime"
domain: "agents"
summary: "Architecture of a production coding-agent harness that must survive multiplexed local workspaces, remote drivers, spectators, and untrusted autonomous factory jobs."
scope: "Architecture of a production coding-agent harness that must survive multiplexed local workspaces, remote drivers, spectators, and untrusted autonomous factory jobs (the four envelope tests in the Stencil Harness Playbook)."
out_of_scope:
  - "SWE-bench eval loops and issue-to-patch start loops"
  - "Training an agent policy (SAO)"
  - "Outcome-only long-horizon agent RL (CANOPY / DRACO)"
  - "Dumped 10M-token prompts (RLM)"
  - "MCP as the product protocol (MCP stays agent-communication)"
  - "Recurrent CED-style architecture (RLT)"
  - "Harness distillation into weights under a fixed target harness (Harness-Zero)"
  - "Recursive self-rewrite of a research-agent harness (AIDE2)"
  - "Harness curriculum as a non-stationary bandit over failure-pattern arms (ActiveSaddler)"
redirects:
  - when: "harness self-evolution for long-horizon terminal agents (RiseHarness)"
    to: "method:riseharness"
  - when: "MaD-RSI model-as-data harness RSI across heterogeneous LLMs"
    to: "method:mad-rsi"
  - when: "harness optimization elicitation vs expansion"
    to: "paper:harness-elicitation-expansion"
  - when: "just-in-time rubric training harness co-evolving with the policy (HarnessRL)"
    to: "method:harnessrl"
  - when: "alternating harness+policy optimization (Self-HPO)"
    to: "method:self-hpo"
  - when: "hypothesis-tree recursive scientific RSI (DiscoveryRSI)"
    to: "method:discoveryrsi"
  - when: "terminal-agent RSR + RPR recursive self-improve (TB-GAE / FDR / SPR)"
    to: "method:terminal-rsi"
  - when: "formal Harness RSI framework + PAC admission bounds (frozen weights)"
    to: "method:harness-rsi"
  - when: "issue-to-patch / locked eval"
    to: "task:software-engineering-agent-harness"
  - when: "train agent RL"
    to: "task:agentic-async-rl"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit)"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "dumped long prompt"
    to: "task:long-context-prompt-offload"
  - when: "how to talk to tools/agents as a protocol"
    to: "task:agent-communication"
  - when: "recurrent CED-style architecture, not a harness kernel"
    to: "task:recurrent-encoder-decoder-lm"
  - when: "regularized harness RSI (annealed edit budget / anti-memorization critic)"
    to: "method:rrsi"
  - when: "distill optimized-harness behaviors into weights under a fixed target harness"
    to: "task:harness-distillation"
  - when: "recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)"
    to: "method:aide2"
  - when: "harness curriculum as a non-stationary bandit over failure-pattern arms"
    to: "method:activesaddler"
  - when: "recurrent textual harness for agentic continual learning (not the production kernel)"
    to: "method:reharness"
last_reviewed: '2026-10-20'
current_sota:
  - method: method:omp2-harness
    as_of: "2026-09-02"
    benchmark: "Pi official extension examples (Appendix A) + four envelope tests"
    metric: "journal-honest stateful examples / architecture envelope"
    value: "2 correct of 78 Pi examples (60 stateless, 17 stateful); journal covering message tree only ⇒ rewind/fork/resume lie"
    notes: "Self-reported blog architecture, not a SWE-bench number. Does not replace mini-SWE-agent, CCA, OpenHands, SAO, FoldGRPO, RLM, MAGIC, CISPO, Muon2, MCP, or ACE."
methods:
  - method:riseharness
  - method:mad-rsi
  - method:harnessrl
  - method:self-hpo
  - method:discoveryrsi
  - method:terminal-rsi
  - method:harness-rsi
  - method:reharness
  - method:omp2-harness
  - method:harness-onpolicy-correction
  - method:sol-pi
  - method:rrsi
  - method:harness-zero
  - method:aide2
  - method:activesaddler
tags:
  - agents
  - agent-harness
  - harness
  - omp
  - omp2
  - stencil
---

# Agent Harness Runtime

## Problem Definition
Build the **harness kernel** for a durable coding-agent engine: one authoritative session, a trusted control plane, bounded cancellable work, explicit model/provider compatibility, and views that are projections. The four envelope tests (Stencil Harness Playbook, 2026-09-02) are the architecture bar: multiplexed local workspace, remote driver, spectator, and untrusted autonomous factory (Factorio).

This is **not** the SWE-bench start/eval loop. Issue → patch / locked mini harness remains `task:software-engineering-agent-harness` (`method:mini-swe-agent`).

## Evaluation Protocol & Benchmarks
- **Envelope tests**, not SWE-bench: multiplexed workspace, remote driver, spectator, Factorio. A design that only works for the first case smuggles the controller into the TUI.
- **Journal honesty**: rewind, fork, resume, replication, and inspection must derive from one journaled session. Pi official examples: 78 total, 60 stateless, 17 stateful, 2 correct (Appendix A).
- **Hazards**: treating this card as a SWE-bench ranking scaffold; stuffing MCP into the permanent tool grammar; copying Pi's three-callback tool API (`renderCall` / `execute` / `renderResult`) or dual authorities.

## SOTA Landscape
- **Default (this task)**: **omp² harness** (`method:omp2-harness`, `paper:harness-playbook`). Spec for a production engine still being built; start with journal → session DOM.
- **Not this task**: mini-SWE-agent (issue → patch / locked eval), CCA (equal-model Pro scaffold), OpenHands/CodeAct (production OSS SWE agent), SAO (train a policy), FoldGRPO (trajectory folding), RLM (dumped long prompt), MCP (agent↔tool protocol), ACE (agent memory), MAGIC / CISPO / Muon2 (training/eval kernels).
- **Gotcha (evolved-harness SFT)**: `method:harness-onpolicy-correction` (`arXiv:2609.09134`). Does not replace omp2.
- **Active token-efficient Pi sibling (not this first hop)**: `method:sol-pi` (`arXiv:2609.20519`). Harness-layer RSI → Action Fusion / ObservationPack / Evidence-Preserving Reducer / Online Context Compact. EdgeBench parity at −44.7–49% token traffic. Does not replace omp2, mini-SWE-agent, or NeoHorse-1.
- **Active regularized harness RSI (not this first hop)**: `method:rrsi` (`arXiv:2609.24972`). Annealed edit budget, unexplored-trajectory proposer, critic+pruner against evolve-set memorization. Up to +14.1 evolve / +4.7 OOD, ~30% fewer policy tokens. Frozen backbone. Does not replace omp2, NeoHorse-1, SoL-Pi, mini-SWE-agent, or harness-onpolicy-correction.
- **Not this task (harness distillation into weights)**: `method:harness-zero` on `task:harness-distillation`. Agent-as-harness SFT so specialized-harness gains survive under a fixed target harness.
- **Active recursive harness RSI (not this first hop)**: `method:aide2` (`arXiv:2609.26457`). Outer-loop research agent rewrites its own harness; accepted rewrite becomes the next incumbent. 8-day run, 7 accepted improvements; eventually beats AIDE_human on the selection benchmark. No public GitHub. Distinct from RRSI (frozen-backbone search) and NeoHorse-1 (routing-guided weight post-train). Does not replace omp2, RRSI, NeoHorse-1, SoL-Pi, or Harness-Zero.
- **Active harness curriculum (not this first hop)**: `method:activesaddler` (`arXiv:2610.00906`). Non-stationary bandit over failure-pattern arms; +4.4 GAIA2 / +7.5 TB2.0 vs the same optimizer with a frozen scenario order. Curriculum dimension, not a new kernel. Does not replace omp2, RRSI, AIDE2, Harness-Zero, or NeoHorse-1.
- Related workflow, not this architecture: [prewalk](https://stencil.so/blog/prewalk) is a workflow on omp, not current_sota here.
- **Not this task (recurrent textual CL harness)**: `method:reharness` (`arXiv:2610.12668`) on `task:agent-continual-learning`. Backward-revises retrieved reflections; not rewind/sandbox/TUI. Does not replace omp2, ACE, or ACLArena.

- **Optional terminal-agent RSI**: `method:terminal-rsi` (`arXiv:2610.22192`). RSR + RPR; TB4.0 19.84% / TB2.1 86.52%. No public code. Does not replace omp2 or RRSI.
- **Optional formal Harness RSI**: `method:harness-rsi` (`arXiv:2610.18813`). PAC admission bounds. Code zgcagi/Harness-RSI. Does not replace omp2 or RRSI.
- **Optional alternating harness-policy RSI**: `method:self-hpo` (`arXiv:2610.22791`). Qwen3.5-35B-A3B 57.8→64.8. Does not replace omp2 or Harness-RSI.
- **Optional scientific hypothesis RSI**: `method:discoveryrsi` (`arXiv:2610.23839`). DFM-Bench 4.86→5.39; code Gen-Verse/DiscoveryRSI. Does not replace omp2 or Terminal-RSI.
- **Optional just-in-time rubric harness**: `method:harnessrl` (`arXiv:2610.26426`). Qwen3.5-4B Rubric-Mix-10k 64.5 / 49.8 OOD. Code Tongyi-ConvAI/Qwen-Character/HarnessRL. Does not replace omp2, Self-HPO, or CANOPY.
