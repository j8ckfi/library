# Graph Change Log

Audit log for all mutations to the knowledge graph: new nodes, supersessions, status changes, and
staleness reviews. One entry per mutation, newest first. Reverts append a reversion receipt — never
rewrite history. Format: [docs/ingestion-guide.md](../docs/ingestion-guide.md) §5.

---

### 2026-09-04 — ingest 2026-09-04 weekday SOTA sweep (OPD-II, Cliff, CANOPY, DIEM, IDA-OPD, Self-Routing, DRACO, spurious-advantage gotcha)
- Added task:outcome-only-long-horizon-agent-rl (CANOPY current_sota; DRACO active sibling). Plug-ins wired beside CISPO/OPD/VeriGate without stealing current_sota. `paper:spurious-advantage-grpo` is a gotcha only (no new method). Per-method receipts follow.
- Does not supersede method:cispo, method:opd, method:sao, method:opsa, method:mini-swe-agent, method:verigate, method:foldgrpo, method:open-mopd, method:ra-opd, or method:omp2-harness.
- Scope checks: new agent-RL task redirects async → agentic-async-rl, folding → long-horizon-tool-agent, dense math/code → math-code-rl-dense, harness → software-engineering-agent-harness, kernel → agent-harness-runtime. Reverse redirects added on those tasks.

### 2026-09-04 — ingest method:opd-one-example (niche; does not supersede method:opd)
- Added paper:opd-one-example (2609.04172), method:opd-one-example, recipe:opd-one-example. Wired to task:student-distillation; Part-II pointer on method:opd / recipe:opd.
- Status niche. OPD is data-overfed but algorithm-starved: one query recovers most full-data gain; ~16 semantically diverse queries match full-data / MOPD.
- Evidence: R1-Distill-1.5B math avg@16 one-shot 68.5 vs full-data 69.8 at step 300; state coverage 71.5% / 98.9% at 1 / 16 queries (arXiv:2609.04172); verified: true; evidence_level: preprint. Code: Thinking-Space/One-Shot-OPD.
- Scope checks: does not supersede method:opd, method:cispo, method:opsa, method:open-mopd, or method:ra-opd.

### 2026-09-04 — ingest method:cliff (active plug-in; does not supersede method:cispo)
- Added paper:cliff (2609.02817), method:cliff, recipe:cliff. Wired to task:math-code-rl-dense, task:reasoning-rl-alignment, task:all-zero-verifier-groups.
- Status active. First-mistake Pitfall Step → token advantages on GRPO/DAPO-style trainers. Not a PRM. Default λ=0. No public code.
- Evidence: Qwen3-4B math avg Cliff 65.66 vs GRPO 61.68 vs OPD 58.17; abstract +15% vs OPD / +7% vs GRPO across 12 scenarios (arXiv:2609.02817); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; VeriGate remains gated-PRM default; OPD remains distill default.

### 2026-09-04 — ingest method:canopy (new task:outcome-only-long-horizon-agent-rl)
- Added paper:canopy (2609.01245), method:canopy, recipe:canopy, task:outcome-only-long-horizon-agent-rl.
- Status sota for outcome-only long-horizon agent RL when a programmatic checker exists. Code listed: AlibabaResearch/SignalCoverageRL.
- Evidence: AppWorld Feb 2026 leaderboard Qwen3-14B TGC 86.9 / 67.6; SWE-bench Verified Qwen3.5-9B mean@4 31.3 → 47.9 (+16.6) (arXiv:2609.01245); verified: true; evidence_level: preprint.
- Scope checks: does not supersede method:sao, method:foldgrpo, method:cispo, method:mini-swe-agent, method:omp2-harness, or method:draco.

### 2026-09-04 — ingest method:diem (active example-reweight; does not supersede method:cispo)
- Added paper:diem (2608.29252), method:diem, recipe:diem. Wired to task:math-code-rl-dense / task:reasoning-rl-alignment.
- Status active. Gradient-alignment importance + constrained batch reweight. Like GMTS: optional. Code: hrtan/DIEM.
- Evidence: Qwen3-4B five-bench avg 40.66 vs GRPO 37.30; Qwen2.5-VL-7B six-bench 61.8 vs RFT 59.1 (arXiv:2608.29252); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; GMTS remains the token-filter plug-in.

### 2026-09-04 — ingest method:ida-opd (niche sampled-token entropy plug-in; does not supersede method:opd)
- Added paper:ida-opd (2608.29846), method:ida-opd, recipe:ida-opd. Wired to task:student-distillation beside ra-opd / opsa / opd.
- Status niche. Keep entropy-expanding A_y; shrink I_H(y)<0 by |q-p|/(q+p). No public code.
- Evidence: Qwen3-8B pass@16 AIME24/25 83.3/76.7 vs OPD 79.1/70.7; Qwen3-4B AIME24 pass@16 83.3 vs OPD 78.7 (arXiv:2608.29846); verified: true; evidence_level: preprint.
- Scope checks: does not replace CISPO or OPD.

### 2026-09-04 — ingest method:self-routing (active recipe router; does not supersede method:cispo or method:opsa)
- Added paper:self-routing (2609.01422), method:self-routing, recipe:self-routing. Wired to task:math-code-rl-dense / task:reasoning-rl-alignment / task:teacher-free-on-policy-self-adaptation (neighbor only).
- Status active. Sample-level GRPO / OPSD / REG / skip from rollout correctness+confidence. No external teacher. ms-swift code planned, not released.
- Evidence: Qwen3-4B six-bench avg 73.7 vs GRPO 66.8 vs OPSD 70.4; Qwen3.5-4B 86.6 vs 79.8 / 83.0 (arXiv:2609.01422); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; OPSA remains teacher-free unlabeled default (Self-Routing's OPSD branch needs gold answers).

### 2026-09-04 — ingest method:draco (active outcome-blind sibling; does not supersede method:canopy)
- Added paper:draco (2609.04094), method:draco, recipe:draco. Wired to task:outcome-only-long-horizon-agent-rl beside CANOPY.
- Status active. Dynamic rubrics + closed-form step credit when no programmatic checker. Code: IBM/draco.
- Evidence: Qwen3.6-27B AppWorld TN TGC p^1 85.3 vs base 69.4 vs outcome-reward GRPO 80.0; τ-bench SR 20.4 vs base 15.8 (arXiv:2609.04094); verified: true; evidence_level: preprint.
- Scope checks: does not supersede method:sao, method:cispo, method:canopy, or method:foldgrpo. Different backbone/protocol than CANOPY's 86.9; not a bake-off.

### 2026-09-04 — ingest paper:spurious-advantage-grpo (gotcha only; no new method)
- Added paper:spurious-advantage-grpo (2609.04063). Updated Gotchas on method:grpo, method:cispo, recipe:cispo, recipe:grpo-trl-training.
- SignBalance is documented in the paper node and is **not** a library method. current_sota unchanged (CISPO).
- Evidence: Qwen2.5-0.5B Avg-8 SignBalance 36.61 vs GRPO 34.24, lift on bounded-answer benches; MATH-7.5K 55.95% bounded answer shapes (arXiv:2609.04063); verified: true; evidence_level: preprint.

### 2026-09-02 — ingest method:omp2-harness (new task:agent-harness-runtime)
- Added paper:harness-playbook (Stencil blog, Can Bölük; no arXiv), method:omp2-harness, recipe:omp2-harness, task:agent-harness-runtime.
- Status sota for production harness-runtime architecture only. Does not supersede method:mini-swe-agent, method:cca, method:openhands-codeact, method:sao, method:foldgrpo, method:rlm, method:magic, method:cispo, method:muon2, method:mcp, or method:ace. omp/Pi are informal predecessors, not library nodes.
- Evidence: Pi official examples 2/78 correct (Appendix A); 5-tool median wall 36.6s vs Codex 42.2s vs Pi 37.0s on task sol (6-run median); renderer 267s → 90ms; speculative compaction ~10% before limit. verified: false; evidence_level: self-reported.
- Scope checks: new agents-shelf task; redirects issue-to-patch/locked eval → software-engineering-agent-harness, train agent RL → agentic-async-rl, dumped long prompt → long-context-prompt-offload, tool protocol → agent-communication. Reverse redirect on the SWE harness task for production engines; that task's current_sota stays mini-swe-agent.

### 2026-09-01 — ingest Agents shelf (harness, RLM, comms)
- Added domain `agents` and method categories `agent-harness`, `agent-protocol`, `agent-memory`, `agent-recursion`.
- New tasks: software-engineering-agent-harness (mini-swe-agent), long-context-prompt-offload (rlm), long-horizon-tool-agent (foldgrpo), agent-communication (mcp), agent-memory (ace), computer-use-agent (claude-computer-use / OSWorld 2.0 paper protocol), multi-agent-orchestration (single-agent-plus-tools; default do not).
- Evidence: official SWE-bench Verified JSON mini+Claude 4.5 Opus (high) 76.8% (2026-02-17); vals.ai locked mini Claude Opus 5 97.00% / DeepSeek V4 Pro 0813 96.40% (2026-09, different snapshot); RLM GPT-5 OOLONG-Pairs d=1 58.0 vs compaction 0.1 (2512.24601); FoldGRPO Seed-OSS-36B BrowseComp-Plus 0.620 vs ReAct 327K+GRPO 0.540 (2510.11967); ACE AppWorld 59.4 vs ReAct 42.4 (2510.04618); OSWorld 2.0 Opus 4.8 20.6% binary / 54.8% partial (2606.29537). Do not mix vals.ai 97% with official JSON 79.2%; do not mix OSWorld 2.0 paper 20.6% with aggregator 70.6%.
- Scope checks: does not retarget CISPO, Muon2, OPD, OLMo-3, poolside-model-factory, BMSSP, OPSA, SAE, MAGIC/Bergson, or SAO (`task:agentic-async-rl` remains SAO). AutoMixer `sota_for` empty. `task:agentic-async-rl` gained a redirect to the harness task for build-not-train; current_sota unchanged.

### 2026-09-01 — ingest method:bergson shelf (new task:training-data-attribution)
- Added task:training-data-attribution; paper:bergson (2606.11660), paper:magic (2504.16430), paper:trackstar (2410.17413), paper:source-tda (2405.12186), paper:ek-fac (2308.03296); method:bergson (active, sota_for empty), method:magic (sota for the new task only), method:trackstar (active), method:ek-fac (active), method:source-unrolling (niche); recipe:bergson-magic-gpt2-wikitext, recipe:bergson-trackstar.
- MAGIC is current_sota for training-data-attribution only (GPT-2 WikiText LDS 0.983). Bergson does not supersede MAGIC (library vs algorithm). No method in this shelf supersedes another. Training defaults unchanged: CISPO, Muon2, OPD family, OLMo-3, factory process, BMSSP, OPSA, SAE (sasa/circuitsteer/fega). AutoMixer pattern: optional factory component, not mix/kernel SOTA.
- Evidence: Bergson Table 1 GPT-2 WikiText FT LDS (50 queries, N=400, Adam) MAGIC 0.983 ± 0.005 vs SOURCE 0.387 vs EK-FAC 0.257 vs TrackStar 0.184; sorted-subset MAGIC 1.000 / EK-FAC 0.865 / TrackStar 0.803; Appendix C 8×A100 grad-dot 72B / EK-FAC 7B (Kronfluence EK-FAC 14B); WMDP bio token reweight +4.61 pp vs unweighted FT +3.11 pp. verified: true; evidence_level: preprint.
- Scope checks: new diagnostic task in interpretability / category data-attribution; redirects mix search → open-data-recipe, SAE → mechanistic-interpretability-dictionaries, factory → industrial-model-building. 405B intro scale recorded as design, not verified.

### 2026-09-01 — receipt: OPSA sweep #12 (4a8406e1)
- Squash-merged ingest of OPSA, NoRA, GMTS, RA-OPD, Qwen3.8-Next, CE-MoE, and GradCodeS, plus new tasks `task:teacher-free-on-policy-self-adaptation` (OPSA) and `task:full-lowbit-finetune` (GradCodeS). Training defaults unchanged: CISPO, Muon2, OPD family, OLMo-3, factory process, BMSSP. Per-method receipts follow.

### 2026-09-01 — integrity: mirror supersedes for method:muon-optimizer
- `method:muon-scalable.supersedes` now includes `method:muon-optimizer` so the existing `superseded_by` pointer is bidirectional. No SOTA retarget.

### 2026-09-01 — ingest method:opsa (new task:teacher-free-on-policy-self-adaptation)
- Added paper:opsa, method:opsa, recipe:opsa, task:teacher-free-on-policy-self-adaptation.
- Status sota for teacher-free / label-free on-policy self-adaptation only. Does not supersede method:cispo, method:opd, method:u-opsd, method:ttpo, method:self-opd, method:vista, or method:j-zero.
- Evidence: Qwen3-1.7B AIME24 Avg@32 48.85 vs base 13.44 vs OPD 32.08 (arXiv:2608.31046); verified: true; evidence_level: preprint.
- Scope checks: new niche; redirects for labeled RLVR, teacher distillation, consensus unlabeled, test-time, data-free, and flow matching.

### 2026-09-01 — ingest method:nora (active; does not supersede method:lr-matters-lora)
- Added paper:nora, method:nora, recipe:nora. Wired to task:parameter-efficient-fine-tuning and task:lora-quality-tuning.
- Status active. Recommended RLVR-stable LoRA upgrade. 24GB quality default remains vanilla LoRA + rsLoRA + LR sweep.
- Evidence: Llama-3.2-3B SFT avg 43.37 vs LoRA 37.93 vs RSLoRA 41.28; RLVR avg 44.4 vs LoRA 42.8 with PiSSA/MiLoRA collapse (arXiv:2608.31036); verified: true; evidence_level: preprint.
- Scope checks: PEFT shelf; no supersession because the paper does not rerun the library LR-sweep protocol of 2602.04998.

### 2026-09-01 — ingest method:gmts (niche token-filter; does not supersede method:cispo)
- Added paper:gmts, method:gmts, recipe:gmts. Wired to task:math-code-rl-dense.
- Status niche. Optional plug-in for GRPO/DAPO/CISPO-family token truncation via |E·ω|.
- Evidence: Qwen2.5-Math-7B DAPO+GMTS 50.14 vs DAPO+ETS 48.81; Qwen3-8B DAPO+GMTS 56.08 vs 53.71 (arXiv:2608.30632); verified: true; evidence_level: preprint.
- Scope checks: in-scope as train-rlvr add-on; CISPO remains Pass@1 default.

### 2026-09-01 — ingest method:ra-opd (niche teacher-OPD filter; does not supersede method:opd or method:opsa)
- Added paper:ra-opd, method:ra-opd, recipe:ra-opd. Wired to task:student-distillation.
- Status niche. Keep trajectories with (2R−1)G≥0; no extra rollouts.
- Evidence: Qwen3-8B-Base math avg@k 49.43 vs OPD 44.34 vs ExOPD 46.95; DeepSeek-R1-Distill-Qwen-7B 69.34 vs OPD 64.43 (arXiv:2608.27960); verified: true; evidence_level: preprint.
- Scope checks: modular filter on teacher OPD; tension with OPSA teacher-noise finding documented, not a supersession.

### 2026-09-01 — ingest method:qwen38-next (active architecture recipe; does not supersede method:muon2 or method:deepseek-v4)
- Added paper:qwen38-next, method:qwen38-next, recipe:qwen38-next. Wired to task:pretrain-moe-frontier, task:pretrain-dense-7b, task:linear-time-sequence-modeling.
- Status active. GDN hybrid + Gated Residual + QSA CPT + off-accelerator n-gram + Muon/AdamW split. Public code is FlashQLA.
- Evidence: 125B-A6B leads 397B-A17B on 8/14 benches at ~1/9 FLOPs; GDN hybrid avg 53.81 vs full attn 49.87; FlashQLA 2–3× forward (arXiv:2608.30320); verified: true; evidence_level: preprint.
- Scope checks: adjacent mHC/AttnRes/GDN; Muon2 and DeepSeek-V4/Kimi-K3 defaults unchanged.

### 2026-09-01 — ingest method:ce-moe (niche MoE layout; does not supersede method:deepseek-v4)
- Added paper:ce-moe, method:ce-moe. No public code; no recipe.
- Status niche. Concentrate experts in fewer routed layers.
- Evidence: 2B–31.5B matched params; 33.3% fewer GPU-hours at 31.5B with better downstream and throughput (arXiv:2608.28511 abstract); verified: true; evidence_level: preprint.
- Scope checks: optional train-moe layout; DeepSeek-V4 / Kimi-K3 remain architecture defaults.

### 2026-09-01 — ingest method:gradcodes (new task:full-lowbit-finetune)
- Added paper:gradcodes, method:gradcodes, recipe:gradcodes, task:full-lowbit-finetune.
- Status sota for fully low-bit code-space fine-tune only. Does not supersede method:aqlora-q or method:quartet-ii.
- Evidence: Llama-3.2-1B-Instruct GSM8K fully 4-bit GradCodeS Full 41.63 vs PV-Tuning 36.92 vs QLoRA-4Merge 24.79 (arXiv:2608.30908); verified: true; evidence_level: preprint.
- Scope checks: new niche; redirects for mixed-precision 4-bit PEFT, native FP4 hardware train, and 24GB quality LoRA.
