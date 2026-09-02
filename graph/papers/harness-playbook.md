---
id: paper:harness-playbook
type: paper
title: "The Harness Playbook"
authors:
  - "Can Bölük"
year: 2026
month: 9
arxiv_id: ""
url: "https://stencil.so/blog/harness-playbook"
venue: "blog"
methods:
  - method:omp2-harness
cites: []
tags:
  - agents
  - agent-harness
  - harness
  - omp
  - stencil
  - blog
---

# The Harness Playbook

## Abstract Summary
Can Bölük (Stencil) argues that a production coding-agent harness is systems software, not a while-loop around a fetch. omp and Pi started as the simple version; omp² is the replacement architecture that owns unavoidable complexity so extensions and users do not. Schema requires `arxiv_id`; it is empty because this is a 2026-09-02 blog post (`https://stencil.so/blog/harness-playbook`), not an arXiv preprint. Evidence level is **self-reported**.

The design envelope is four architecture tests: multiplexed local workspace, remote driver, spectator, and untrusted autonomous factory. Those tests force one authoritative session DOM with a property-change journal, host-owned policy with a bandwidth-bounded sandbox stub, cancellable tool/job streams, compiled inference compatibility, a tiny permanent tool roster with `dyn`/Bash for the long tail, and views as projections (TUI transcript protocol modeled in TLA+).

[prewalk](https://stencil.so/blog/prewalk) is a *workflow* on omp, not this architecture, and is not current_sota here.

## Key Contributions
1. **One authority**: session materializes as a DOM; the journal stores property-change patches. Pi's journal covering the message tree only makes rewind/fork/resume lie (78 official Pi examples: 60 stateless, 17 stateful, 2 correct; Appendix A).
2. **Host / sandbox split**: host owns policy, inference, and journal; sandbox is an obedient bounded execution stub. Subagents get copy-on-write worktrees (`pi-iso`).
3. **Tool call as state stream**: an element with `input` / `result` / `diag` / `usage`, not Pi's `renderCall` / `execute` / `renderResult`. Jobs (bash, subagent, daemon, over-budget call) share one stdio-shaped primitive with central output/time bounds.
4. **Control plane**: convars for settings; Director stack for loop ownership (`Pass` / `Continue` / `Yield` / `Push` / `Done` / `Fail`); `ForceTool` is semantic, inference translates (soft prompt always, native flag if free, escalate on non-compliance).
5. **Tiny roster + `dyn`**: five essential tools median wall 36.6s vs Codex 42.2s vs Pi 37.0s on task `sol` (median of 6, fresh session). MCP does not belong in the permanent tool grammar.
6. **Renderer and TUI**: 267s → 90ms one-pass RichText pipeline; TLA+ Elastic Speculative Slots (Appendix B). Language: Rust engine + embedded Python (`@remote`, dependable `Eval`); TypeScript as default harness language is argued against.

## Empirical Highlights
- Pi official examples: 78 total, 60 stateless, 17 stateful, **2 correct** (Appendix A).
- Tool roster tax: 5 essential tools median wall **36.6s** vs Codex **42.2s** vs Pi **37.0s** on task `sol`, median of 6 runs, fresh session.
- Renderer: 267s → 90ms one-pass RichText; `.includes` image-line check 13% CPU / 98.7s wrapAnsi in a profiled session with 0 images.
- Speculative compaction ~10% before the context limit; splice onto the live branch vs naive block-at-limit.
- omp² is still being built against this document; no public omp² repository is linked from the post.
