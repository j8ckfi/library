---
id: method:hive-synth
type: method
title: "Hive Declarative Synthetic Pipelines"
category: "training-systems"
status: active
sota_for: []
supersedes: []
papers:
  - paper:laguna-m1-xs2
claims:
  - benchmark: "Laguna XS.2 synthetic share"
    metric: "fraction of pretrain mix / generated pool"
    value: "~13% of mix from a ~4.4T generated-token pool"
    baseline: "organic sources only, or one-off synth jobs as a new job type"
    date: "2026-08"
    verified: true
    notes: "Laguna M.1/XS.2 §3.2.2. Pipelines (form-rewrite, cascade, multi-turn) are Hive configs, not new orchestrator job types."
tags:
  - systems
  - training-systems
  - synthetic-data
  - hive
  - factory-component
---

# Hive Declarative Synthetic Pipelines

## Method Overview
Hive is the Model Factory's declarative synthetic-data component. Every pipeline is configuration, not a new job type:

\[
P = \mathrm{post}_H \circ H_T \circ \mathrm{pre}_H
\]

where \(H_T\) is an agent-interaction loop over orchestrators, generators, judges, and per-step early-exit gates. A spec \((\mathcal{S},\mathcal{M},G,f,V)\) compiles into that loop. Reported shapes (Laguna Table 2):

- **Form-rewrite**: single-call rephrase conditioned on metadata (~1e12 tokens).
- **Cross-domain transducer**: modality cast (math↔code, language port) (~1e10).
- **Multi-stage cascade**: chained generators with verifier gates (~1e11).
- **Multi-turn rollout**: closed-loop orchestrated chats (~1e10).

Principles: match pipeline complexity to teacher capability; pass known metadata into \(G\) so the generator is not guessing structure. On Laguna XS.2, synth carried ~13% of the mix from a ~4.4T generated pool. Hive has no public package; do not invent one.

## When to Use
- When synth work is currently a one-off script that cannot be reused as a config on the same DAG as train/eval.
- Form-rewrite, cascade, or multi-turn generation that should share generators/filters with later runs.

## Scale-down (few-GPU / small lab)
**Keep** the idea: one generator+filter DAG, pipelines as config, registered as versioned assets. A single local generator and a filter step on Dagster (or equivalent) is the small-lab Hive.

**Skip** Hive's closed runtime, multi-teacher orchestrators, and trillion-token rewrite farms.

## Gotchas & Failure Modes
- Standing up a new job type per synth idea destroys the "config not rewrite" property.
- Teachers that cannot solve the task in one shot need decomposition; otherwise you bake biased generations into the mix.

## Supersession
Active component of `method:poolside-model-factory`. Does not supersede open instruct/data recipes.
