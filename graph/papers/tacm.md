---
id: paper:tacm
type: paper
title: "Trained Agentic Context Management"
authors:
  - "Bryce Sandlund"
year: 2026
month: 10
arxiv_id: "2610.02404"
url: "https://arxiv.org/abs/2610.02404"
methods:
  - method:tacm
cites:
  - paper:rlm
tags:
  - agents
  - long-context
  - harness
  - tacm
---

# Trained Agentic Context Management

## Abstract Summary
Instead of native long context or a hand-authored long-context harness, TACM finetunes a model over the simplest harness: a self-call tool (any specified prompt) and a range-read tool over the input. Qwen3.6-35B-A3B is finetuned on synthetic data with an 8K per-agent context and compared to GPT-5.4 at 1M tokens on OOLONG-synth. Active plug-in beside RLM. Code: `https://github.com/brycesandlund/infinite-context`.

## Key Contributions
1. **Self-call + range-read** as the only harness; the model is trained to manage context, not prompted into a REPL.
2. **OOLONG-synth (mean of 3 families), 8K harness vs GPT-5.4 1M**: 40K 0.535 vs 0.600; 80K 0.561 vs 0.539; 160K 0.464 vs 0.556; 320K 0.470 vs 0.479.
3. **RULER** finetuned harness 0.949 / 0.949 / 0.929 / 0.885 / 0.868 / 0.858 through 320K (0.858 at 320K).

## Empirical Highlights
- Base Qwen3.6-35B-A3B full-document OOLONG 40K is 0.388; dashes at 80K+.
- RLM remains the dumped-corpus first hop; TACM is a trained 8K self-call harness, not a REPL over a Python environment.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02404`
- Code: `https://github.com/brycesandlund/infinite-context` (`code_status: released`; HTTP 200 as of 2026-10-05).
