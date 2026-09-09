# Graph Change Log

Audit log for all mutations to the knowledge graph: new nodes, supersessions, status changes, and
staleness reviews. One entry per mutation, newest first. Reverts append a reversion receipt — never
rewrite history. Format: [docs/ingestion-guide.md](../docs/ingestion-guide.md) §5.

---

### 2026-09-09 — ingest 2026-09-09 weekday SOTA sweep (Miles, NeoHorse-1, ThinkPrior, RouteOPD, TV-OPD, DATPO, OPRD + optionals)
- Added two new first-hop tasks (`task:frontier-rl-posttrain-stack`, `task:agentic-rsi-routing-posttrain`) plus fifteen methods. No false supersessions of CISPO / Muon2 / OPD / OPSA / CANOPY / Poolside / SAO / ES-reasoning / mini-SWE-agent / Iris / Uno / W2S-OPD.
- MUST: Miles, NeoHorse-1, ThinkPrior, RouteOPD, TV-OPD, DATPO, OPRD. OPTIONAL (all landed): ACE MoE PEFT, AnLR-LoRA, KBBQ, AF1, CircuitLens, Online Draft Co-Training, DataFlex-RL, MoE sparsity HP scaling. Skipped none of the requested optionals. Already-in-library items (TGOPD, Uno, FlowBalance, Iris, sparse-OPD, OPD-then-RLVR, GAPO, RISE, layer-dropout) were not re-ingested.
- Scope checks: CISPO, Muon2, OPD, OPSA, CANOPY remain first hops on their tasks. Miles is sota only for the new frontier stack. NeoHorse-1 is sota only for the new RSI routing-harness task.

### 2026-09-09 — ingest method:miles (new task:frontier-rl-posttrain-stack)
- Added paper:miles (2609.08368), method:miles, recipe:miles, task:frontier-rl-posttrain-stack. Reverse redirects on task:industrial-model-building, task:agentic-async-rl, task:software-engineering-agent-harness, task:outcome-only-long-horizon-agent-rl.
- Status sota for the production post-train engine only. Code: radixark/miles.
- Evidence: GLM-5.2 744B-A40B Terminal-bench-2 64× GB300 median 263s (first 30 steps); KL 0.0369; reward 0.438→0.556 single run (Table 9 / Figure 5, arXiv:2609.08368); verified: true; evidence_level: preprint.
- Scope checks: Poolside remains factory process; SAO remains async algorithm; CISPO remains Pass@1; Muon2 remains 7B optimizer; mini-SWE-agent remains the harness.

### 2026-09-09 — ingest method:neohorse-1 (new task:agentic-rsi-routing-posttrain)
- Added paper:neohorse-1 (2609.08183), method:neohorse-1, recipe:neohorse-1, task:agentic-rsi-routing-posttrain. Reverse redirects on SWE harness, SAO, CANOPY, Iris, CISPO, OPD shelves.
- Status sota for routing-harness RSI post-train only. Code: TokenRhythm/NeoHorse. Weights: TokenRhythm/neohorse-1.
- Evidence: 4B 58.94→64.87 and 9B 65.60→69.04 ten-bench macro vs Qwen3.5 same size (Table 1, arXiv:2609.08183); verified: true; evidence_level: preprint.
- Scope checks: mini-SWE-agent remains the harness; SAO remains async; CANOPY remains AppWorld; Iris remains search-agent climbing; CISPO remains Pass@1; OPD remains text distill.

### 2026-09-09 — ingest method:thinkprior (active RLVR data-policy plug-in; does not supersede method:cispo / method:gapo / method:verigate)
- Added paper:thinkprior (2609.09075), method:thinkprior, recipe:thinkprior (stub; project page only). Wired to task:math-code-rl-dense; mention on task:all-zero-verifier-groups.
- Status active. Zero-rollout Beta difficulty prior for GRPO cold-start prompt selection. Loss/optimizer unchanged.
- Evidence: silent groups 23.8%→10.6%; ThinkPrior+DAPO 8256→7381 generated rollouts at 3840-update budget; accuracy +0.7 with CI crossing 0 (arXiv:2609.09075); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; GAPO remains clip-width; VeriGate remains PRM gating; DataFlex-RL is the accuracy-null cousin.

### 2026-09-09 — ingest method:routeopd (active OPD plug-in; does not supersede method:opd)
- Added paper:routeopd (2609.08337), method:routeopd, recipe:routeopd (stub; no official code). Wired to task:student-distillation.
- Status active. Pairwise log-odds transport vs sampled reverse-KL OPD.
- Evidence: four settings macro +2.70 Avg@16 vs sampled-RKL; JustRL-DeepSeek 65.53 vs 63.34 (Table 1, arXiv:2609.08337); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; RA-OPD / IDA-OPD / TGOPD remain sibling plug-ins.

### 2026-09-09 — ingest method:tv-opd (active OPD stability plug-in; does not supersede method:opd / method:ra-opd / method:tropd / method:stable-opd)
- Added paper:tv-opd (2609.08341), method:tv-opd, recipe:tv-opd (stub; no official code). Wired to task:student-distillation.
- Status active. Sign of token advantages ≈ full OPD; TV-shaped shared scale for late training.
- Evidence: late AIME24 49.58 vs Raw 46.11; LateMean 43.06 vs 40.87 (Table 2, arXiv:2609.08341); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; RA-OPD remains trajectory mask; TrOPD remains trust-region matching; Stable-OPD remains control variates.

### 2026-09-09 — ingest method:datpo (active Pass@K sibling; does not supersede method:es-reasoning / method:cispo)
- Added paper:datpo (2609.08650), method:datpo, recipe:datpo (GRPO-Zero host). Wired to task:passk-reasoning-coverage; mention on task:math-code-rl-dense.
- Status active. Difficulty-adaptive sentence-entropy tree-structured PO.
- Evidence: Qwen2.5-3B 22.4/54.9 avg@k/pass@k vs GRPO 20.7/48.2; Qwen3-4B 31.3/60.4 vs GRPO 30.1/58.3 (Table 2, arXiv:2609.08650); verified: true; evidence_level: preprint.
- Scope checks: ES-reasoning remains Pass@K / no-backward first hop; CISPO remains Pass@1.

### 2026-09-09 — ingest method:oprd (active reverse distill; does not supersede method:w2s-opd / method:opd / method:cispo)
- Added paper:oprd (2609.08798), method:oprd, recipe:oprd (stub; no official code). Wired to task:student-distillation. Updated method:w2s-opd differentiation / do_not_use_for.
- Status active. Weak-to-strong: amplify verifier-supported student gradient along teacher policy-shift. Not matching.
- Evidence: 4B→8B math avg 51.91 vs KDRL 43.99 / OPD 39.44; multi-teacher 58.77 vs Mix-RL 47.68 (Tables 1/3, arXiv:2609.08798); verified: true; evidence_level: preprint.
- Scope checks: W2S-OPD remains matching; OPD remains distill default; CISPO remains Pass@1. Table 3 vs W2S-OPD is differentiation, not a graph supersession.

### 2026-09-09 — ingest method:ace-moe-peft (active MoE PEFT; does not supersede method:lr-matters-lora or method:ace)
- Added paper:ace-moe-peft (2609.06072, EMNLP 2026), method:ace-moe-peft, recipe:ace-moe-peft. Wired to task:parameter-efficient-fine-tuning. Slug avoids collision with method:ace (Agentic Context Engineering).
- Status active. Expert-adapter consolidation. Code: UbiquitousAILab/ACE.
- Evidence: best mean on 3/4 MoE backbones; 1.31×–1.48× faster vs expert-wise LoRA (arXiv:2609.06072); verified: true; evidence_level: peer-reviewed.
- Scope checks: lr-matters-lora remains 24GB quality default; method:ace remains agent memory.

### 2026-09-09 — ingest method:anlr-lora (active LoRA LR plug-in; does not supersede method:lr-matters-lora / method:nora)
- Added paper:anlr-lora (2609.05885), method:anlr-lora, recipe:anlr-lora (stub). Wired to task:lora-quality-tuning and task:parameter-efficient-fine-tuning.
- Status active. Anisotropic per-rank learning rates, mean-normalized so the global LR is unchanged.
- Evidence: lift vs uniform-LR LoRA on commonsense / NLG / visual instruction-tuning (arXiv:2609.05885); verified: true; evidence_level: preprint.
- Scope checks: quality default remains vanilla LoRA + rsLoRA + LR sweep; NoRA remains rank-normalize A.

### 2026-09-09 — ingest method:kbbq (active W4A4 niche; does not supersede method:quartet-ii / method:mxfp4-mi355x)
- Added paper:kbbq (2609.08135), method:kbbq, recipe:kbbq (stub). Wired to task:fp4-hardware-training as a mention only.
- Status active. Predictive noise law / spectrum-flattening limits for FP4 W4A4.
- Evidence: outperforms prior flatten SOTA with no extra deploy-time compute (arXiv:2609.08135); verified: true; evidence_level: preprint.
- Scope checks: Quartet-II / MXFP4 remain native FP4 hardware-training current_sota.

### 2026-09-09 — ingest method:af1 (active 1-bit PTQ; does not supersede method:sparse-bitnet)
- Added paper:af1 (2609.06161, EMNLP 2026 Main), method:af1, recipe:af1. Wired to task:1bit-extreme-quantization. Claimed GitHub Kishon-zzx/AF1 was 404 at ingest.
- Status active. Genuine 1-bit PTQ of existing LLMs under a 1.0-BPW budget.
- Evidence: best among compared binarization PTQ; ~2.5× inference vs BF16 (arXiv:2609.06161); verified: true; evidence_level: peer-reviewed.
- Scope checks: Sparse-BitNet remains native 1.58-bit pretrain; ScaleQ-1.58 remains ternary post-train.

### 2026-09-09 — ingest method:circuitlens (active RLVR data-selection signal; does not supersede method:cispo)
- Added paper:circuitlens (2609.07183, EMNLP 2026 Findings), method:circuitlens, recipe:circuitlens (stub). Wired to task:math-code-rl-dense.
- Status active. CRS circuit-engagement ranking; low-engagement decile wins on 7B medium math.
- Evidence: lowest-CRS decile +2.0 / +1.6 / +2.9 pp vs random on GSM8K / OlympiadBench / Minerva (arXiv:2609.07183); verified: true; evidence_level: peer-reviewed.
- Scope checks: CISPO remains Pass@1; ThinkPrior remains silent-group prior; DataFlex-RL remains the accuracy-null.

### 2026-09-09 — ingest method:online-draft-cotrain (niche; does not supersede method:miles / method:uno)
- Added paper:online-draft-cotrain (2609.07108), method:online-draft-cotrain, recipe:online-draft-cotrain. Wired to task:frontier-rl-posttrain-stack; mention + redirect from task:diffusion-augmented-ar.
- Status niche. Speculative decoding co-train for long-context RL. Code: NVIDIA-NeMo/RL#3698.
- Evidence: drafts track the policy through 122B / 256K CP with rollout and e2e speedups (arXiv:2609.07108); verified: true; evidence_level: preprint.
- Scope checks: Miles remains the frontier stack; Uno remains diffusion-augmented AR serving; CISPO remains Pass@1.

### 2026-09-09 — ingest method:dataflex-rl (active negative result; does not supersede method:cispo / method:thinkprior)
- Added paper:dataflex-rl (2609.06107), method:dataflex-rl, recipe:dataflex-rl (stub). Wired to task:math-code-rl-dense.
- Status active. Controlled finding: RLVR data policies do not beat uniform GRPO at 95% CI.
- Evidence: uniform +7.76 pp vs untrained on Qwen2.5-7B-Base 12-bench; no selection method 95% CI vs uniform excludes 0 (arXiv:2609.06107); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; ThinkPrior remains the waste-cut prior (not an accuracy claim).

### 2026-09-09 — ingest method:moe-sparsity-hp-scaling (active MoE HP guidance; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:moe-sparsity-hp-scaling (2609.08690), method:moe-sparsity-hp-scaling, recipe:moe-sparsity-hp-scaling (stub). Wired to task:pretrain-moe-frontier.
- Status active. LR/batch vs activation-ratio transfer laws.
- Evidence: ~1,800 MoE pretrain runs; held-out 12B 1/64 predicted HPs close to observed optima (arXiv:2609.08690); verified: true; evidence_level: preprint.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain architecture current_sota; Muon2 remains dense optimizer.

### 2026-09-08 — catch-up ingest method:iris / method:sparse-opd-supervision / method:opd-then-rlvr (completes the weekday sweep to seven)
- Completes the 2026-09-08 weekday sweep. Original four (FlowBalance, TGOPD, OT optimizer schedules, Uno) unchanged. Added Iris (new `task:web-search-agent-rl`), sparse OPD supervision, and OPD-then-RLVR. No false supersessions of CISPO / Muon2 / OPD / OPSA / CANOPY / RISE / GAPO / OPDVR / SAO / mini-SWE-agent / FoldGRPO.
- Still skipped (WATCH): FactoSR, Refuse-without-Refusal, over-editing, CoSkill, ConsensusBench, Multi-Harness RL, Scale-QLoRA, Train-What-You-Deploy, OPSD survey 2608.25936, EmbodiedSkills, ENEAS, revision-propagation, 2609.04575, 2609.04453, 2609.05309, 2609.05274.
- Scope checks: CISPO, Muon2, OPD, CANOPY, SAO remain first hops on their tasks. Uno remains sota only for `task:diffusion-augmented-ar`. Iris is sota only for the new search-agent task.

### 2026-09-08 — ingest method:iris (new task:web-search-agent-rl)
- Added paper:iris (2609.04304), method:iris, recipe:iris, task:web-search-agent-rl. Reverse redirects on task:agentic-async-rl, task:outcome-only-long-horizon-agent-rl, task:long-horizon-tool-agent, task:software-engineering-agent-harness, task:math-code-rl-dense.
- Status sota for live-web search-agent training only. Code/weights: AllSpark-Research/Iris.
- Evidence: Iris-mini 82.2/84.8/86.9/52.3 and Iris-pro 88.6/85.1/92.9/56.4 on BrowseComp / BrowseComp-ZH / DeepSearchQA / HLE-text with discard-all CM (Table 1); no-CM BrowseComp 64.7 / 72.6 (Table 2, arXiv:2609.04304); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld; SAO remains async; mini-SWE-agent remains the harness; FoldGRPO remains folding; CISPO remains Pass@1.

### 2026-09-08 — ingest method:sparse-opd-supervision (active OPD plug-in; does not supersede method:opd / method:cispo)
- Added paper:sparse-opd-supervision (2609.04565), method:sparse-opd-supervision, recipe:sparse-opd-supervision (stub; no official code). Wired to task:student-distillation; optional mention on task:math-code-rl-dense.
- Status active. Keep-mask on sampled-token OPD: 1–2 tokens (~0.05%) can match/beat full-token OPD.
- Evidence: Family 8 avg@8 mean pctltail 0.05% 30.1 vs plain OPD 27.5; Family 9 minmaxtok 49.3 vs plain 47.5 vs teacher 46.8 (Tables 3/5, arXiv:2609.04565); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1; IDA-OPD remains the entropy-shrink plug-in.

### 2026-09-08 — ingest method:opd-then-rlvr (active stacking order; does not supersede method:opd / method:cispo / method:opdvr)
- Added paper:opd-then-rlvr (2609.04108), method:opd-then-rlvr, recipe:opd-then-rlvr. Wired to task:student-distillation and task:math-code-rl-dense; related mention on task:distill-reasoner-verifier. Code: StringNLPLAB/opd-rlvr.
- Status active. OPD then RL beats pure OPD, pure GRPO, and joint one-step fusion. Not a graph supersession of the algorithms.
- Evidence: logic pass@1 mean 80.6 vs GRPO 49.4 vs OPD 53.9 vs KDRL 62.8; math 31.8 vs OPD 31.0 vs GRPO 28.4 (Table 2, arXiv:2609.04108); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1 RLVR (paper RL stage is GRPO); OPDVR remains single-step gated OPD+RLVR.

### 2026-09-08 — ingest 2026-09-08 weekday SOTA sweep (FlowBalance, TGOPD, OT optimizer schedules, Uno)
- Added four methods without stealing CISPO / Muon2 / OPD / OPSA / CANOPY / RISE / GAPO current_sota. Uno is sota only for the new `task:diffusion-augmented-ar`. Per-method receipts follow.
- Skipped (WATCH only): 2608.25936 OPSD critical review; EmbodiedSkills; ENEAS; revision-propagation; training-free MoE expert halving (2609.04575); expert pruning under over-dispersion (2609.04453); mHC residual analysis (2609.05309); Speculative Uncertainty draft-gate (2609.05274). Tue arXiv /new still showed Mon 7 Sep listings at sweep time; HF Daily Papers 2026-09-08 used as extra signal.
- Scope checks: no half supersessions; CISPO, Muon2, OPD remain first hops on their tasks.

### 2026-09-08 — ingest method:flowbalance (active; does not supersede method:cispo / method:opsa / method:opd / method:vista / method:u-opsd / method:rise / method:canopy)
- Added paper:flowbalance (2609.03241), method:flowbalance, recipe:flowbalance. Wired to task:math-code-rl-dense; related mentions on task:teacher-free-on-policy-self-adaptation and task:privileged-teacher-opsd.
- Status active. Privileged same-model token logp-gains aggregated to trajectory self-guidance, sign-gated by verifier group advantage, fitted by profiled trajectory balance. Code: alexhuang13/FlowBalance.
- Evidence: Qwen3-4B five-bench avg 64.26 vs FlowRL 63.22 vs GRPO 62.31; Qwen3-8B 67.61 vs 65.85 / 65.49; AIME24@16 89.33 vs FlowRL 86.67 (Table 1, arXiv:2609.03241); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1 default; OPSA remains supervision-free; VISTA remains privileged-teacher adaptation.

### 2026-09-08 — ingest method:tgopd (active OPD plug-in; does not supersede method:opd / method:cispo / method:opsa / method:open-mopd)
- Added paper:tgopd (2609.02998), method:tgopd, recipe:tgopd (stub; no official code). Wired to task:student-distillation; optional mention on task:math-code-rl-dense.
- Status active. Prompt-level teacher probes then exclusive dense OPD vs GRPO. Sibling of RA-OPD / IDA-OPD / VISTA.
- Evidence: 4B LCB Vanilla OPD 42.3 closes 21% of 39.4→53.3 gap, TGOPD 47.1 closes 55%; 35B LCB TGOPD 64.0 vs base 61.0 vs teacher 62.7 (only positive transfer); 4B SOPD teacher GPU 9.8%→78.9% (Table 1/3, arXiv:2609.02998); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1 RLVR; Open-MOPD remains multi-teacher.

### 2026-09-08 — ingest method:optimizer-memory-schedules (active; does not supersede method:muon2) and thin method:adana
- Added paper:optimizer-memory-schedules (2609.04577), method:optimizer-memory-schedules, recipe:optimizer-memory-schedules (stub; no official code). Wired to task:llm-pretraining-optimization and task:pretrain-dense-7b. Thin method:adana + paper:adana (2602.05298) as the primary ADANA cite; `sota_for: []`.
- Status active. OT horizon changes optimizer rank and optimal LR/WD/memory. WD $\sim\sqrt{\mathrm{OT}}$; LR schedule ranking reverses; longer OT favors longer fixed memory.
- Evidence: 51M $1\times$ linear LR vs $8\times$/$32\times$ cosine; $c_{\mathrm{uniform}}=8\sqrt{f}$; Muon token multiplier vs AdamW $\sim 1.4\times$–$1.7\times$; ADANA equivalent-OT exponent 1.15–1.20 vs AdamW (arXiv:2609.04577); verified: true; evidence_level: preprint. 51M–253M only — not a 7B bake-off.
- Scope checks: Muon2 remains ~7B optimizer; Puro-2B remains consumer ~2B.

### 2026-09-08 — ingest method:uno (new task:diffusion-augmented-ar)
- Added paper:uno (2609.04010), method:uno, recipe:uno, task:diffusion-augmented-ar. Reverse redirects on task:posttrain-diffusion and task:llm-pretraining-optimization.
- Status sota for diffusion-augmented AR serving/train-addon only. Code: ifm-ai/uno.
- Evidence: 8B Uno SWE-Verified 68.4 vs DiffusionGemma 18.7; system throughput 5255 vs 1136 / 1197 tok/s; Uno Qwen 1.6× vs base AR at max H200 batch, >5700 tok/s (Table 1 / §5.2, arXiv:2609.04010); verified: true; evidence_level: preprint.
- Scope checks: does not supersede method:diffusion-opsd, method:self-opd, method:muon2, or method:cispo.

### 2026-09-07 — ingest 2026-09-07 weekday SOTA sweep (GAPO, RISE, layer-dropout, OPD hard-CoT, PTA)
- Added five active/niche methods without stealing current_sota. CISPO, OPD, OPSA, Muon2, CANOPY, SAO, and FoldGRPO remain first hops. Per-method receipts follow.
- Skipped (WATCH only): Iris 2609.04304 (search-agent SFT-RL climbing recipe; domain-specific); ACE expert skipping 2609.05228 (training-free MoE inference); MaxKernel 2609.04523 (TPU kernel agents); mHC residual analysis 2609.05309 (interpretability of existing mHC).
- Scope checks: no half supersessions; cheat-sheet first hops unchanged.

### 2026-09-07 — ingest method:pta (active; does not supersede method:opd / method:cispo / method:canopy / method:sao / method:foldgrpo)
- Added paper:pta (2609.04773, EMNLP 2026 Main), method:pta, recipe:pta. Wired to task:student-distillation; related mentions on task:long-horizon-tool-agent and task:agentic-async-rl.
- Status active. OPKD for tool-using agents: student-induced but teacher-committed rollouts; chunk-level verification + turn-level commitment; persistent lookahead. No official GitHub.
- Evidence: Search-R1 PTA+RL macro best@4 34.59 vs OPKD+RL 32.07; DeepEyes 70.00 vs 67.20; lookahead 0.644 vs 0.519 samples/s (arXiv:2609.04773); verified: true; evidence_level: preprint (EMNLP accept noted).
- Scope checks: OPD remains text distill; CISPO remains Pass@1 RLVR; CANOPY remains outcome-only agent RL; SAO remains async policy train; FoldGRPO remains folding.

### 2026-09-07 — ingest method:gapo (active plug-in; does not supersede method:cispo)
- Added paper:gapo (2609.00444, EMNLP 2026 Main), method:gapo, recipe:gapo. Wired to task:math-code-rl-dense.
- Status active. Adapts GRPO/GSPO IS-ratio clip to rollout advantage (reverse-KL trust-region). No reward shaping. Code: Sheng-J/GAPO.
- Evidence: R1-Distill-Qwen-1.5B AIME24 Pass@1/16 GAPO 44.0/76.7 vs GSPO 41.3/73.3; DeepCoder LCB-v5 24.8 vs 22.4 (arXiv:2609.00444); verified: true; evidence_level: preprint (EMNLP accept noted).
- Scope checks: CISPO remains Pass@1 default; OPD / OPSA / CANOPY unchanged.

### 2026-09-07 — ingest method:rise (active; does not supersede method:opd / method:cispo / method:opsa)
- Added paper:rise (2609.05295), method:rise, recipe:rise. Wired to task:student-distillation; related mentions on task:math-code-rl-dense and task:teacher-free-on-policy-self-adaptation.
- Status active. Synthetic teacher from the model's own RLVR trajectory via param/logit extrapolation. No official GitHub.
- Evidence: Qwen3-8B Math Avg RISE (weight) 62.7 vs GRPO 60.0; OLMo3-7B 56.4 vs 47.6; ALFWorld 84.4 vs 75.0 (arXiv:2609.05295); verified: true; evidence_level: preprint.
- Scope checks: OPD remains single-teacher distill; CISPO remains labeled RLVR; OPSA remains supervision-free; VISTA remains privileged-gold OPSD.

### 2026-09-07 — ingest method:layer-dropout (active; does not supersede method:muon2)
- Added paper:dont-drop-dropout (2609.05275, ICML 2026 extended), method:layer-dropout, recipe:layer-dropout. Wired to task:llm-pretraining-optimization, task:pretrain-dense-7b; optional note on task:budget-consumer-pretrain.
- Status active. Structured layer dropout with $r_{\mathrm{train}}=1/\rho$. Practical code: torchtune layer_dropout.py / fairseq LayerDrop (override residual scale).
- Evidence: 1.8B val 1.836 vs dense 1.849 at 15% FLOP save; 8.2B 25% FLOP save; ~1.5× self-speculative inference (arXiv:2609.05275); verified: true; evidence_level: peer-reviewed.
- Scope checks: Muon2 remains ~7B optimizer; Puro-2B remains consumer ~2B recipe.

### 2026-09-07 — ingest method:opd-hard-cot-selection (niche; does not supersede method:opd or method:opd-one-example)
- Added paper:opd-hard-cot-selection (2609.05198), method:opd-hard-cot-selection, recipe:opd-hard-cot-selection. Wired to task:student-distillation; cross-linked with method:opd-one-example.
- Status niche. Hard/long-CoT selection on OPD (not high token entropy); 8 hard examples match 17K. Sibling to OPD-II's diversity-vs-volume finding.
- Evidence: R1-Distill-Qwen-1.5B 8-hard avg 53.6 vs 17K 53.7; 7B 8-shot 59.5 vs 59.6 (arXiv:2609.05198); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; OPD-II remains the diversity/volume note.

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
