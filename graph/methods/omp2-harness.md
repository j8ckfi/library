---
id: method:omp2-harness
type: method
title: "omp² Harness (Stencil Harness Playbook)"
category: "agent-harness"
status: sota
sota_for:
  - task:agent-harness-runtime
supersedes: []
do_not_use_for:
  - when: "SWE-bench start/eval loop or GitHub issue → patch"
    reason: "mini-SWE-agent is the locked ranking scaffold and first hop for starting a loop"
    use_instead: "method:mini-swe-agent"
  - when: "equal-model Pro scaffold vs SWE-agent"
    reason: "CCA is the equal-model notes/context alternative on the SWE harness task"
    use_instead: "method:cca"
  - when: "training an async agent policy"
    reason: "this is a harness kernel, not an RL optimizer"
    use_instead: "method:sao"
  - when: "stuffing MCP into the permanent tool grammar"
    reason: "playbook: MCP is long-tail behind dyn/Bash; MCP remains the agent↔tool protocol, not a harness primitive"
    use_instead: "method:mcp"
assumptions:
  - "You are implementing a harness kernel, not wrapping a 100-line ReAct loop."
  - "The four envelope tests must hold: multiplexed workspace, remote driver, spectator, untrusted factory."
last_reviewed: "2026-09-02"
papers:
  - paper:harness-playbook
recipes:
  - recipe:omp2-harness
claims:
  - benchmark: "Pi official extension examples (Appendix A)"
    metric: "journal-honest stateful examples"
    value: "2 correct of 78 (60 stateless, 17 stateful)"
    baseline: "Pi journal covering message tree only"
    date: "2026-09"
    verified: false
    evidence_level: "self-reported"
    source_url: "https://stencil.so/blog/harness-playbook"
    notes: "Journal covering message tree only ⇒ rewind/fork/resume lie. Self-reported blog audit, not independently reproduced."
  - benchmark: "task sol, median of 6 runs, fresh session (playbook figure)"
    metric: "median wall-clock seconds"
    value: 36.6
    baseline: "Codex 42.2s; Pi 37.0s"
    date: "2026-09"
    verified: false
    evidence_level: "self-reported"
    source_url: "https://stencil.so/blog/harness-playbook"
    notes: "Five essential tools. Tool grammar tax on token generation, not just prefix tokens."
  - benchmark: "Pi TUI renderer profile (playbook figure)"
    metric: "render wall / wrapAnsi / image-line check"
    value: "267s → 90ms one-pass RichText; wrapAnsi 98.7s; .includes 13% CPU; 0 images"
    baseline: "Pi string[] render() pipeline"
    date: "2026-09"
    verified: false
    evidence_level: "self-reported"
    source_url: "https://stencil.so/blog/harness-playbook"
    notes: "One-pass RichText pipeline. Profiled session contained 0 images."
  - benchmark: "context compaction scheduling (playbook)"
    metric: "kickoff before context limit"
    value: "~10% before limit, splice onto live branch"
    baseline: "naive block-at-limit compaction"
    date: "2026-09"
    verified: false
    evidence_level: "self-reported"
    source_url: "https://stencil.so/blog/harness-playbook"
    notes: "Speculative compaction on a journal snapshot; commit only if the snapshot still describes the live branch."
tags:
  - harness
  - omp
  - pi
  - stencil
  - directors
  - session-dom
  - agent-harness
  - sota
---

# omp² Harness (Stencil Harness Playbook)

## Method Overview
Production harness-runtime architecture for omp² (successor to omp/Pi). One authoritative session DOM plus a property-change journal is the Source Engine lesson: rewind, fork, resume, replication, and inspection are the same fold. omp/Pi are informal predecessors, not library nodes.

Mechanism (faithful to the playbook, not a novel):

1. **One authoritative session DOM + property-change journal.** Runtime objects may cache; they must not become a second truth.
2. **Host owns policy / inference / journal; sandbox is a bandwidth-bounded execution stub.** Subagents get copy-on-write worktrees (`pi-iso`: APFS, btrfs, ZFS, overlayfs, ProjFS, or copy fallback).
3. **Tool call = cancellable state stream** (element with `input` / `result` / `diag` / `usage`), not `renderCall` / `execute` / `renderResult`.
4. **Jobs share one stdio-shaped primitive** (bash, subagent, daemon, over-budget call) with central output and time bounds.
5. **Convars** for settings; **Director stack** for loop ownership (`Pass` / `Continue` / `Yield` / `Push` / `Done` / `Fail`). `ForceTool` is semantic; inference translates.
6. **Inference compatibility as compiled taxonomy / classes / providers** (unknown ≠ false; ambiguous overlap errors). Forced tools: soft prompt always, native flag if free, escalate on non-compliance.
7. **Tiny permanent roster**; long tail via `dyn` CLI synthesized from JSON schema plus deep Read/Bash builtins. MCP is not a permanent-grammar tool.
8. **Views are projections.** TUI transcript protocol modeled in TLA+ (Elastic Speculative Slots, Appendix B).
9. **Language: Rust engine + embedded Python extensions** (`@remote`, dependable `Eval`). TypeScript as the default harness language is argued against for agent-generated code.

Does **not** supersede `method:mini-swe-agent`, `method:cca`, `method:openhands-codeact`, `method:sao`, `method:foldgrpo`, `method:rlm`, `method:magic`, `method:cispo`, `method:muon2`, `method:mcp`, or `method:ace`.

## When to Use
- Building a durable coding-agent engine that must rewind, fork, resume, sandbox, drive remotely, and serve a TUI/web spectator.
- Implementing the harness kernel rather than wrapping a 100-line ReAct loop.
- The four envelope tests are in scope.

## When NOT to Use
- SWE-bench start/eval loop or issue → patch → `method:mini-swe-agent` / `task:software-engineering-agent-harness`.
- Equal-model Pro scaffold vs SWE-agent → `method:cca`.
- Training an agent policy → `method:sao`.
- Dumped 10M-token prompt → `method:rlm`.
- How to talk to tools as a protocol → `method:mcp` (keep MCP off the permanent roster; discover via `dyn`/Bash).
- Agent memory playbooks → `method:ace`. Trajectory folding → `method:foldgrpo`.

## Gotchas & Failure Modes
- Dual authorities (message tree plus closures / Maps) make rewind/fork/resume lie even if the JSONL looks complete.
- Pi's three-callback tool API duplicates I/O and has no authoritative lifecycle object.
- Per-tool truncation, backgrounding, and cancellation cannot be optional helpers; Factorio requires a kill boundary that cannot take session authority with it.
- Unknown capability must stay unknown; file-order precedence and `unknown = false` recreate provider-name branch spaghetti.
- omp² is still being built against the playbook; this card is the spec, not a downloadable engine.
- [prewalk](https://stencil.so/blog/prewalk) is an omp workflow, not this architecture.
