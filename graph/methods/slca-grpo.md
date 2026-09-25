---
id: method:slca-grpo
type: method
title: "SLCA-GRPO"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "folding a long tool trajectory into a small active context"
    reason: "FoldGRPO folds context; SLCA routes segment advantages inside one trajectory"
    use_instead: "method:foldgrpo"
  - when: "variable environment latency / async stragglers"
    reason: "SAO remains async first hop; SLCA is structural credit, not straggler replay"
    use_instead: "method:sao"
  - when: "Actor-then-Critic IS-aligned critic after axiomatic token credit"
    reason: "PACT is token-level critic alignment; SLCA is GRPO segment routing"
    use_instead: "method:pact"
  - when: "diagnose which multi-turn tool calls are trainable"
    reason: "Critical-State RL selects which turn gets gradient; SLCA splits tool vs summary tokens"
    use_instead: "method:critical-state-rl"
  - when: "single-turn math/code Pass@1 RLVR"
    reason: "CISPO remains Pass@1; SLCA hosts GRPO on tool-calling agents"
    use_instead: "method:cispo"
assumptions:
  - "Trajectory splits into a tool/execution segment and a final contiguous summary segment. HierR (or equivalent) supplies separate tool and summary returns. Group size G=16 in the paper."
  - "Paper: Qwen2.5-3B/7B-Instruct and Qwen3-8B-Base; SGLS mocker; Toucan filter 42,423 SFT / 31,818 RL; one RL epoch."
  - "GitHub SLCA-GRPO/SLCA-GRPO 404 as of 2026-09-25. Dataset YanZhanPKU/SLCA-GRPO-Datasets is public."
last_reviewed: "2026-09-25"
papers:
  - paper:slca-grpo
recipes:
  - recipe:slca-grpo
claims:
  - benchmark: "Toucan-Test Success@0.9, Qwen2.5-7B-Instruct, three-run mean"
    metric: "strict Success@0.9"
    value: "79.13%"
    baseline: "matched SFT+GRPO +2.53 pp; also +2.35 pp on 3B, +2.05 pp on 8B"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29050"
    notes: "Table 1. Same SFT, SGLS, HierR, G=16, one RL epoch. Not a FoldGRPO/SAO/CISPO retarget."
  - benchmark: "BFCL V3 / tau2-Bench vs matched GRPO, Qwen2.5-7B-Instruct"
    metric: "mean gap vs GRPO"
    value: "+1.36 pp / +9.15 pp"
    baseline: "matched SFT+GRPO under the same training budget"
    date: "2026-09-25"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.29050"
    notes: "Abstract / §4. Orthogonal to VinePPO/SPO/GiGPO temporal credit."
tags:
  - post-training
  - rl-alignment
  - credit-assignment
  - tool-use
  - slca-grpo
  - active
---

# SLCA-GRPO

## Method Overview
GRPO attaches one group-normalized trajectory advantage to every token. On tool-calling traces that mix \(y_{\mathrm{tool}}\oplus y_{\mathrm{sum}}\), summary variation then contaminates tool-token updates. SLCA keeps the GRPO group and the unified backbone. It normalizes tool and summary returns separately

\[
\hat{A}_i^{\mathrm{tool}}=\frac{R_i^{\mathrm{tool}}-\mu_g^{\mathrm{tool}}}{\sigma_g^{\mathrm{tool}}+\epsilon},\qquad
\hat{A}_i^{\mathrm{sum}}=\frac{R_i^{\mathrm{sum}}-\mu_g^{\mathrm{sum}}}{\sigma_g^{\mathrm{sum}}+\epsilon}
\]

and routes \(\hat{A}^{\mathrm{tool}}\) only onto tool tokens and \(\hat{A}^{\mathrm{sum}}\) only onto summary tokens (zero on environment tokens). No extra intermediate-state rollouts. HierR supplies the two returns; SGLS supplies schema-guided simulated observations. Temporal credit (VinePPO / SPO / GiGPO) is a different axis and can compose inside a segment.

FoldGRPO remains folding. SAO remains async. PACT remains Actor-then-Critic. Critical-State RL remains which-turn trainability. CISPO remains Pass@1.

## When to Use
- On-policy tool-agent RL where one trajectory mixes tool calls and a final NL summary, and you already have (or can add) segment-specific rewards.

## When NOT to Use
- Folding → `method:foldgrpo`. Async stragglers → `method:sao`. Actor-then-Critic token credit → `method:pact`. Which turn is trainable → `method:critical-state-rl`. Pass@1 math → `method:cispo`.

## Relation to Existing SOTA
- Active first hop on `task:tool-agent-segment-credit` only (method status active; listed in that task's `current_sota`; `sota_for` stays empty). Does **not** replace `method:foldgrpo`, `method:sao`, `method:pact`, `method:critical-state-rl`, or `method:cispo`.

## Gotchas & Failure Modes
- Claimed GitHub is 404 as of 2026-09-25. Dataset is on Hugging Face. Reimplement routing; do not invent a SAO/FoldGRPO replacement.
- Routing assumes a single final-answer block. Multi-summary or missing-summary traces need the paper's edge-case rules.
- SLCA does not claim tool calls are causally irrelevant to the final answer. It bets that a dense execution reward is the lower-variance signal for tool tokens.
- ToolPO still lets summary-dependent noise reach tool tokens. RLTR splits planner/summarizer. Neither is this method.
