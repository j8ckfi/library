# Graph Change Log

Audit log for all mutations to the knowledge graph: new nodes, supersessions, status changes, and
staleness reviews. One entry per mutation, newest first. Reverts append a reversion receipt — never
rewrite history. Format: [docs/ingestion-guide.md](../docs/ingestion-guide.md) §5.

---

### 2026-10-20 — weekday SOTA sweep (Polar Switch, miniTE, SPOD, Arctic-SWE, TAR, ToolOPD, HarnessRL; secondaries T-MUON, AdamPM, NVFP4 recipe, PACT NVFP4 LoRA, Agentic RL Data Scaling, CD-OPD, LOOP, ECHO, FrameGRPO, EG-GRPO, DFR, Bridged Self-Distillation, ProbePO; notes OPDArena, What RL Brings, GRPO vs RFT, Off-Policy PG Anatomy)
- Twenty active plug-ins and four paper-only notes. No current_sota retarget (Muon2 / CISPO / OPD / Open-MOPD / SAPO / SAO / CANOPY / SCALE / Quartet-II / AQLoRA-Q / Iris / Uno / OraRL / omp2 / RecreationWorld / Claude computer-use / Miles / mini-SWE-agent / DiffusionOPSD / Self-OPD / CodeMidas / BPCO).
- Window: 2026-10-20 Librarian weekday sweep after merged PR 47 (watermark 2610.23839, 1514 nodes, b8430c0). arXiv cs.LG/cs.CL/cs.AI new listing Tue 2026-10-20 (2610.23857-2610.26863) plus HF Daily 2026-10-19 and 2026-10-20. New high id 2610.26863.
- SKIP (already skipped 2026-10-19): LEV 2610.20951; Embeddings Are Overpriced 2610.22428.
- SKIP (considered, not ingested): Muon EoS 2610.24305 (CIFAR-10); statistical Adam/Shampoo/Muon 2610.24839; DP-Muon 2610.24736; LIRQuant 2610.25675; 2-bit n-gram 2610.21810; protein LMs 2610.26651 / 2610.26747; CoworkEnv 2610.24960 (WIP env); TokenGate 2610.26754 (serving); Nash-MOPD 2610.26124; AsyncOPSD 2610.25880; RARE 2610.25434 (HarnessRL covers); LIFT 2610.24229; CSPO 2610.25092; Aperture 2610.25325; RIDGE 2610.25330; C-OPSD 2610.25842; DeGMatch 2610.24963; KronLSTM 2610.26834; RoAR-VAE 2610.26216; GCD SFT 2610.25497; DisaggKD 2610.17644; Halcyon T2I 2610.26863; BatchParScale 2610.25254; TamedFlow 2610.26025; Frechet Forcing 2610.25666; PEFT-MoE empirical 2610.26370; Cache2LoRA 2610.24107; UC-RAMP 2610.25717; WSR-Tune 2610.26443; Codpula 2610.25723; PRECOCIAL 2610.24970; safety mid-training 2610.26809; looped BPTT 2610.26030; internalizing CoT looped 2610.25998; curriculum implicit reasoning 2610.25612; data selection context extension 2610.24469; productive state-space 2610.25957; adaptive decoding RL 2610.25860; targeted CPT 2610.25836; RSRL 2610.25850; PGB 2610.25704; FRDA 2610.26685; Dynalize 2610.26496; visual OPSD 2610.26856; Fisher MOPD 2610.26525; APSD 2610.25973.


### 2026-10-20 — ingest method:polar-switch (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:polar-switch , method:polar-switch, recipe:polar-switch (`code_status: released`).
- Status active (`sota_for: []`). 15.5-18.7% lower Polar Express runtime; code zhehangdu/polar-switch.

### 2026-10-20 — ingest method:t-muon (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:t-muon , method:t-muon, recipe:t-muon (`code_status: none`).
- Status active (`sota_for: []`). head-wise identity t-Muon lowest FineWeb val PPL 51M-1.3B.

### 2026-10-20 — ingest method:adampm (active on task:full-param-memory-efficient-pretrain; does not supersede method:scale / method:muon2)
- Added paper:adampm , method:adampm, recipe:adampm (`code_status: released`).
- Status active (`sota_for: []`). second-moment memory 1/s of Adam; code jixiaowei95/AdamPM.

### 2026-10-20 — ingest method:minite (active on task:fp4-rl-train-rollout-alignment; does not supersede method:quartet-ii / method:trace / method:triage)
- Added paper:minite , method:minite, recipe:minite (`code_status: none`).
- Status active (`sota_for: []`). 33540 tok/s; 1.39x BF16 on Qwen3-30B-A3B NVFP4 RL.

### 2026-10-20 — ingest method:nvfp4-pretrain-recipe (active on task:fp4-hardware-training; does not supersede method:quartet-ii)
- Added paper:nvfp4-pretrain-recipe , method:nvfp4-pretrain-recipe, recipe:nvfp4-pretrain-recipe (`code_status: none`).
- Status active (`sota_for: []`). stacked NVFP4 recipe vs NVIDIA 2025 / Quartet-II / TetraJet at 8B and 30B-A3B.

### 2026-10-20 — ingest method:pact-nvfp4-lora (active on task:4bit-peft-quantization; does not supersede method:aqlora-q / method:pact)
- Added paper:pact-nvfp4-lora , method:pact-nvfp4-lora, recipe:pact-nvfp4-lora (`code_status: none`).
- Status active (`sota_for: []`). NVFP4 GEMMs ~6-7x BF16 on 16 GB RTX 5080; name collides with Actor-then-Critic PACT.

### 2026-10-20 — ingest method:agentic-rl-data-scaling (active on task:coding-agent-rl-environment-construction; does not supersede method:codemidas / method:canopy)
- Added paper:agentic-rl-data-scaling , method:agentic-rl-data-scaling, recipe:agentic-rl-data-scaling (`code_status: none`).
- Status active (`sota_for: []`). D_E* ∝ C^0.34; D_T* ∝ C^0.27; D_τ* ∝ C^0.13; N* ∝ C^0.26.

### 2026-10-20 — ingest method:tar-rlvr (active on task:math-code-rl-dense; does not supersede method:cispo / method:expdis)
- Added paper:tar-rlvr , method:tar-rlvr, recipe:tar-rlvr (`code_status: released`).
- Status active (`sota_for: []`). adaptive replay of undersampled correct RLVR modes; code wenzhilics/tar.

### 2026-10-20 — ingest method:spod (active on task:student-distillation; does not supersede method:opd / method:canopy)
- Added paper:spod , method:spod, recipe:spod (`code_status: released`).
- Status active (`sota_for: []`). +15.2 pp vs OPD; ALFWorld 16.5→82.8 peak; code Jike338/SPOD.

### 2026-10-20 — ingest method:toolopd (active on task:student-distillation; does not supersede method:opd / method:slca-grpo)
- Added paper:toolopd , method:toolopd, recipe:toolopd (`code_status: released`).
- Status active (`sota_for: []`). outcome-asymmetric action-token OPD; code MagicAgent-Search/ToolOPD.

### 2026-10-20 — ingest method:cd-opd (active on task:student-distillation; does not supersede method:opd / method:branchopd)
- Added paper:cd-opd , method:cd-opd, recipe:cd-opd (`code_status: none`).
- Status active (`sota_for: []`). +1.32 to +7.05 pp; CFR -27.4% to -56.4%.

### 2026-10-20 — ingest method:arctic-swe (active on task:agentic-async-rl; does not supersede method:sao / method:miles / method:mini-swe-agent)
- Added paper:arctic-swe , method:arctic-swe, recipe:arctic-swe (`code_status: none`).
- Status active (`sota_for: []`). Qwen3.5-4B SWE-bench Verified 62.0% raw / 65.0 curated.

### 2026-10-20 — ingest method:harnessrl (active on task:agent-harness-runtime; does not supersede method:omp2-harness / method:canopy)
- Added paper:harnessrl , method:harnessrl, recipe:harnessrl (`code_status: released`).
- Status active (`sota_for: []`). Qwen3.5-4B Rubric-Mix-10k 64.5 / 49.8 OOD; code Tongyi-ConvAI/Qwen-Character/HarnessRL.

### 2026-10-20 — ingest method:echo-mtp (active on task:diffusion-augmented-ar; does not supersede method:uno)
- Added paper:echo-mtp , method:echo-mtp, recipe:echo-mtp (`code_status: none`).
- Status active (`sota_for: []`). ECHO-1.5(3) matches ECHO-3 at half MTP overhead.

### 2026-10-20 — ingest method:framegrpo (active on task:rl-video-mllm; does not supersede method:orarl)
- Added paper:framegrpo , method:framegrpo, recipe:framegrpo (`code_status: none`).
- Status active (`sota_for: []`). complementary frame-set GRPO plus gated temporal credit.

### 2026-10-20 — ingest method:eg-grpo (active on task:web-search-agent-rl; does not supersede method:iris / method:gca)
- Added paper:eg-grpo , method:eg-grpo, recipe:eg-grpo (`code_status: none`).
- Status active (`sota_for: []`). evidence-claim step rewards mixed with GRPO.

### 2026-10-20 — ingest method:loop-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:loop-opd , method:loop-opd, recipe:loop-opd (`code_status: none`).
- Status active (`sota_for: []`). Qwen3-4B-Instruct +7.37 / +9.10 / +6.34 pp at 15/20/25% prune.

### 2026-10-20 — ingest method:dfr (active on task:posttrain-diffusion; does not supersede method:diffusion-opsd / method:self-opd / method:mend)
- Added paper:dfr , method:dfr, recipe:dfr (`code_status: none`).
- Status active (`sota_for: []`). up to +29% diversity; 36-41x vs Flow-GRPO on SD3.5-M.

### 2026-10-20 — ingest method:bridged-self-distill (active on task:student-distillation; does not supersede method:opd / method:cross-tokenizer-opd)
- Added paper:bridged-self-distill , method:bridged-self-distill, recipe:bridged-self-distill (`code_status: released`).
- Status active (`sota_for: []`). trace-conditioned self-teacher without teacher logp; code TUMLegalTech/Bridged-Self-Distillation.

### 2026-10-20 — ingest method:probe-po (active on task:math-code-rl-dense; does not supersede method:cispo / method:bpco)
- Added paper:probe-po , method:probe-po, recipe:probe-po (`code_status: none`).
- Status active (`sota_for: []`). 16/18 wins; 76% less time vs VinePPO.

### 2026-10-20 — ingest paper:opdarena (note on task:student-distillation; does not retarget method:opd)
- Added paper:opdarena (methods: [method:opd]). RLVR teachers retain prior skills; SFT teachers forget more; code StellarCurtain/OPDArena.

### 2026-10-20 — ingest paper:what-rl-brings (note on task:math-code-rl-dense; does not retarget method:cispo)
- Added paper:what-rl-brings (methods: [method:cispo]). ~4% greedy disagreements recover 90.5% of GRPO pass@1; code CyrusZhang04/WhatRLBrings.

### 2026-10-20 — ingest paper:grpo-vs-rft (note on task:math-code-rl-dense; does not retarget method:cispo)
- Added paper:grpo-vs-rft (methods: [method:cispo]). GRPO beats 27-run-tuned RFT on a procedural counting task.

### 2026-10-20 — ingest paper:off-policy-pg-anatomy (note on task:math-code-rl-dense; does not retarget method:cispo)
- Added paper:off-policy-pg-anatomy (methods: [method:cispo]). off-policy PG consistency via trajectory IS or KL plus optimal-soft-value baseline.

### 2026-10-19 — weekday SOTA sweep (GR-OPD, TreeOPSD, MoEvolve, Self-HPO; secondaries BMuon, CCR, SimOPD, OPMD, MultiAgent-OPD, GCA, DiscoveryRSI, Ori, LED, MetaCurate, OpenMobile-2, MLExpert, Sigma-Delta, Lean4AgenticRL, Schedule-Free Diffusion, ToPA, MPT)
- Twenty-one active plug-ins, five paper-only notes, and a Part I paper on Looped Models Done Right. No current_sota retarget (Muon2 / CISPO / OPD / Open-MOPD / SAPO / SAO / CANOPY / SCALE / Iris / omp2 / RecreationWorld / Claude computer-use / Sparse-BitNet / Representation Guidance / vanilla LoRA+rsLoRA+LR sweep / VISTA / OLMo-3 / A2D / single-agent-plus-tools).
- Window: 2026-10-19 Librarian weekday sweep after merged PR 46 (watermark 2610.22282, ~1445 nodes, 187c774). arXiv cs.LG/cs.CL new listing Mon 2026-10-19 plus HF Daily 2026-10-16 tail and 2026-10-19. New high id 2610.23839.
- SKIP (duplicates, already skipped 2026-10-16): FDE-Gym 2610.22350; CoDA 2610.22362.
- SKIP (considered, not ingested): ReDiST 2610.23831 (student-conditioned traces, not a new distill kernel); BayesianPRM 2610.23223; MTEdit 2610.23751; Causal Latent Workspaces 2610.22796; LEV 2610.20951; Local proxies 2610.23145; Embeddings Are Overpriced 2610.22428; Region-Inhomogeneous 2610.22380; CADENCE 2610.22788; FrankenMerging 2610.22999; DP-μP 2610.22976; Speculative Forcing 2610.22347; SAGA 2610.22439; Finite-rank LoRA 2610.23343; Deep lifts 2610.23009; LeMA 2610.22925; inference-only DLite 2610.23787, SPOT 2610.22543, ReaDy 2610.20503, length inflation 2610.23818, Prism 2610.22985.

### 2026-10-19 — ingest method:gr-opd (active on task:student-distillation; does not supersede method:opd / method:ier-opd)
- Added paper:gr-opd (2610.23042), method:gr-opd, recipe:gr-opd (`code_status: none`).
- Status active (`sota_for: []`). Wins every setting; +10.9 / +11.5 pp with matched thinking; vanilla OPD collapses on mismatched thinking.

### 2026-10-19 — ingest method:treeopsd (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:treehca)
- Added paper:treeopsd (2610.23181), method:treeopsd, recipe:treeopsd (`code_status: none`).
- Status active (`sota_for: []`). Average accuracy +4.97 vs GRPO.

### 2026-10-19 — ingest method:moevolve (active on task:math-code-rl-moe; does not supersede method:sapo / method:opd)
- Added paper:moevolve (2610.23185), method:moevolve, recipe:moevolve (`code_status: none`). Mention on task:student-distillation.
- Status active (`sota_for: []`). Up to +22.2 vs initial / +6.5 vs same-budget RLVR; final low-k often beats the expanded teacher.

### 2026-10-19 — ingest method:self-hpo (active on task:agent-harness-runtime; does not supersede method:omp2-harness / method:harness-rsi / method:aide2)
- Added paper:self-hpo (2610.22791), method:self-hpo, recipe:self-hpo (`code_status: none`). Mention on task:agentic-rsi-routing-posttrain.
- Status active (`sota_for: []`). Average resolve 57.8%→64.8%; joint gain exceeds harness-only plus policy-only.

### 2026-10-19 — ingest method:bmuon (active on task:llm-pretraining-optimization; does not supersede method:muon2 / method:scale)
- Added paper:bmuon (2610.23571), method:bmuon, recipe:bmuon (`code_status: none`).
- Status active (`sota_for: []`). Beats Muon under post-training MLP channel pruning (1B) and gradual structured MLP prune (ViT-S/16).

### 2026-10-19 — ingest method:ccr (active on task:math-code-rl-dense; does not supersede method:cispo / method:es-reasoning)
- Added paper:ccr (2610.22887), method:ccr, recipe:ccr (`code_status: none`).
- Status active (`sota_for: []`). 8k CCR vs GRPO 32k: 4B 975464→174957 (−82.1%); 8B 793832→165788 (−79.1%) tokens/step.

### 2026-10-19 — ingest method:simopd (active on task:student-distillation; does not supersede method:opd / method:ride)
- Added paper:simopd (2610.23306), method:simopd, recipe:simopd (`code_status: none`).
- Status active (`sota_for: []`). +2.6 same-arch / +3.1 cross-arch vs strongest paper OPD/hidden-state baselines.

### 2026-10-19 — ingest method:opmd (active on task:student-distillation; does not supersede method:opd / method:ride / method:latent-mopd)
- Added paper:opmd (2610.14022), method:opmd, recipe:opmd (`code_status: none`). HF Daily 2026-10-16 tail.
- Status active (`sota_for: []`). Highest average in all three teacher-student settings; generalizes to multi-teacher and cross-family SFT.

### 2026-10-19 — ingest method:multiagent-opd (active on task:student-distillation; does not supersede method:opd / method:single-agent-plus-tools)
- Added paper:multiagent-opd (2610.23234), method:multiagent-opd, recipe:multiagent-opd (`code_status: none`). Mention on task:multi-agent-orchestration.
- Status active (`sota_for: []`). Macro avg@4 38.68%; +4.06 vs Prompted Critic; +2.61 vs C-MAS + RL.

### 2026-10-19 — ingest method:gca (active on task:web-search-agent-rl; does not supersede method:iris / method:canopy)
- Added paper:gca (2610.23148), method:gca, recipe:gca (`code_status: none`).
- Status active (`sota_for: []`). +5.7 EM Qwen2.5-3B / +6.3 EM Qwen3-30B-A3B vs Search-R1; evidence-supported share 76.9%→93.4%.

### 2026-10-19 — ingest method:discoveryrsi (active on task:agent-harness-runtime; does not supersede method:omp2-harness / method:terminal-rsi / method:harness-rsi)
- Added paper:discoveryrsi (2610.23839), method:discoveryrsi, recipe:discoveryrsi (`code_status: released`; Gen-Verse/DiscoveryRSI).
- Status active (`sota_for: []`). Hypothesis quality 4.86→5.39 after two rounds; DiscoveryRSI-27B 6.3% vs GPT-6 2.5% / Opus 5 2.3%.

### 2026-10-19 — ingest method:ori (active on task:full-param-memory-efficient-pretrain; does not supersede method:scale / method:pmrc)
- Added paper:ori (2610.22794), method:ori, recipe:ori (`code_status: none`).
- Status active (`sota_for: []`). Up to 69.3% gap cut vs prior GaLore-family on 1B; best on 10/16 RoBERTa-Base scenarios. No SCALE bake-off.

### 2026-10-19 — ingest method:led (active on task:diffusion-lm-ar-delta-recycle; does not supersede method:a2d / method:justopd / method:canvasanneal)
- Added paper:led (2610.23122), method:led, recipe:led (`code_status: none`).
- Status active (`sota_for: []`). +11.4 (7B) / +7.7 (8B) vs MDM SFT; LED-8B SFT-only beats LLaDA2.1-16B Q-mode (CPT+SFT+RL).

### 2026-10-19 — ingest method:metacurate (active on task:coding-agent-rl-environment-construction; does not supersede method:olmo-3 / method:autosft / method:swe-at-scale)
- Added paper:metacurate (2610.23134), method:metacurate, recipe:metacurate (`code_status: none`). Mention on task:instruct-sft-alignment.
- Status active (`sota_for: []`). Highest mean SWE-Verified among compared SFT filters, including hand-authored and a 3.5x-cost training-loop baseline.

### 2026-10-19 — ingest method:openmobile-2 (active on task:hybrid-computer-use-agent-rl; does not supersede method:recreationworld / method:claude-computer-use / method:mai-gym)
- Added paper:openmobile-2 (2610.14157), method:openmobile-2, recipe:openmobile-2 (`code_status: none`). HF Daily 2026-10-16 tail.
- Status active (`sota_for: []`). AndroidWorld 79.9; MobileWorld 50.4; SPA-Bench 31.9→59.6. OSWorld ranking is not this card.

### 2026-10-19 — ingest method:mlexpert (active on task:agentic-async-rl; does not supersede method:sao / method:canopy)
- Added paper:mlexpert (2610.22344), method:mlexpert, recipe:mlexpert (`code_status: released`; InternScience/MLExpert).
- Status active (`sota_for: []`). MLE-Bench Lite average medal rate 37.9%→72.7%.

### 2026-10-19 — ingest method:sigma-delta-sampler (active on task:1bit-extreme-quantization; does not supersede method:sparse-bitnet / method:scaleq-158)
- Added paper:sigma-delta-sampler (2610.22621), method:sigma-delta-sampler, recipe:sigma-delta-sampler (`code_status: none`).
- Status active (`sota_for: []`). MatMul-free discrete-weight training to 2.7B.

### 2026-10-19 — ingest method:lean4-agentic-rl (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:terminal-rsi)
- Added paper:lean4-agentic-rl (2610.22448), method:lean4-agentic-rl, recipe:lean4-agentic-rl (`code_status: none`).
- Status active (`sota_for: []`). TB2.1 77.3%; +9.89 vs base; +5.07 vs second-best same-size.

### 2026-10-19 — ingest method:schedule-free-diffusion (active on task:pixel-diffusion-pretrain; does not supersede method:representation-guidance / method:diffusion-opsd)
- Added paper:schedule-free-diffusion (2610.22945), method:schedule-free-diffusion, recipe:schedule-free-diffusion (`code_status: none`). Mention on task:posttrain-diffusion.
- Status active (`sota_for: []`). Schedule-Free beats constant-LR EMA across stages; LR decay+EMA is complementary.

### 2026-10-19 — ingest method:topa (active on task:lora-quality-tuning; does not supersede method:lr-matters-lora / method:dt-lora)
- Added paper:topa (2610.22883), method:topa, recipe:topa (`code_status: released`; scongl/ToPA).
- Status active (`sota_for: []`). Block-wise Toeplitz products vs low-rank and sparse PEFT.

### 2026-10-19 — ingest method:market-posttrain (active on task:multi-agent-orchestration; does not supersede method:single-agent-plus-tools / method:sao)
- Added paper:market-posttrain (2610.22322), method:market-posttrain, recipe:market-posttrain (`code_status: released`; Embodied-Minds-Lab/MPT).
- Status active (`sota_for: []`). Joint action+bidding co-adapts capabilities and participation vs fixed orchestration.

### 2026-10-19 — update method:looped-models-done-right (Part I paper:looped-models-done-right-i; does not retarget method:recurrent-looped-transformer / method:smelt)
- Added paper:looped-models-done-right-i (2610.23036) onto the existing Huginn-style card. Same code ifm-ai/xllm-loop.
- 730M/336B Huginn beats Ouro on all ten benches; 8BA0.8B/500B Huginn beats Ouro on nearly all; 75% fewer resident params than 112-layer FF MoE at matched FLOPs.

### 2026-10-19 — note paper:optimizer-switch-cost (gotcha on task:llm-pretraining-optimization; does not retarget method:muon2)
- Added paper:optimizer-switch-cost (2610.22650). 1.2B AdamW↔Muon interpolations: mismatch cost is small vs each stage's optimizer choice.

### 2026-10-19 — note paper:rank-noise-baseline (gotcha on task:lora-quality-tuning; does not retarget method:lr-matters-lora)
- Added paper:rank-noise-baseline (2610.22438). Direction-counting ranks sit near noise; stable rank sits far below; instruct vs non-instruct updates look the same.

### 2026-10-19 — note paper:progressive-misalignment (gotcha on task:privileged-teacher-opsd; does not retarget method:vista / method:opd / method:rrsi)
- Added paper:progressive-misalignment (2610.22467). Recursive self-distillation can progressively misalign even when every generation is safe.

### 2026-10-19 — note paper:posttrain-cue-routing (gotcha on task:instruct-sft-alignment; does not retarget method:olmo-3)
- Added paper:posttrain-cue-routing (2610.22937). Post-training tunes a pretrained cue-routing mechanism rather than installing a new bias circuit.

### 2026-10-19 — note paper:privileged-pi-effectiveness (gotcha on task:privileged-teacher-opsd; does not retarget method:vista / method:privileged-context-drift)
- Added paper:privileged-pi-effectiveness (2610.22512). Predict privileged-information effectiveness before OPSD rather than assuming gold context always helps.

### 2026-10-16 — weekday SOTA sweep (Waypoint-OPD, Mosaic, MRTPO, MMSearch-OPD, SCOPE-T2I, Terminal-RSI, RPO, Training-Free OPD, SCOPED, AutoSFT, SERO, EDEN; secondaries MAI-Gym, OpenGCUA, Harness-RSI, FlashMask-3, LCT, score-centering, SWE-at-Scale, OS-Helix)
- Nineteen active plug-ins and one paper-only note. No current_sota retarget (OPD / Open-MOPD / CISPO / SAO / CANOPY / CorrGRPO+DARA / Iris / omp2 / RRSI / Claude computer-use / RecreationWorld / SCALE / Muon2 / DiffusionOPSD+Self-OPD / JustOPD).
- Window: 2026-10-16 Librarian weekday sweep after merged PR 45 (watermark 2610.20607, 1387 nodes, dcaf314). New high id 2610.22282.
- SKIP (considered, not ingested): benchmarks-only (OmniCompass, RoTA-Bench, FDE-Gym, WorldMemBench, MFVSR); pure 3D/video gen without train recipe change; robot personalization CarryOn; CoDA robot sim; Minecraft / driving-only.

### 2026-10-16 — ingest method:waypoint-opd (active on task:student-distillation; does not supersede method:opd / method:open-mopd / method:justopd / method:rpd-opd)
- Added paper:waypoint-opd (2610.21601), method:waypoint-opd, recipe:waypoint-opd (`code_status: released`; hhhbxloveai/WaypointOPD). Mention on task:privileged-teacher-opsd.
- Status active (`sota_for: []`). Math +2.18/+1.59/+1.89 vs Direct-OPD; code +2.66/+1.52/+1.19; 8B math Avg 56.14 vs no-gate 53.50.

### 2026-10-16 — ingest method:mosaic (active on task:agentic-async-rl; does not supersede method:sao)
- Added paper:mosaic (2610.22174), method:mosaic, recipe:mosaic (`code_status: released`; LARK-AI-Lab/Mosaic).
- Status active (`sota_for: []`). BrowseComp Qwen3.5-4B compaction 38.86 vs 35.31 (sessions 3.17→2.35); subagent 32.46 vs 31.44.

### 2026-10-16 — ingest method:mrtpo (active on task:multi-reward-rlvr; does not supersede method:corrgrpo / method:dara)
- Added paper:mrtpo (2610.21439), method:mrtpo, recipe:mrtpo (`code_status: released`; zhaihaotian/MRTPO).
- Status active (`sota_for: []`). Qwen2.5-Coder-7B SQL avg 73.15 vs GDPO 71.55 / GRPO 70.93; MRTPO+SAW 73.41.

### 2026-10-16 — ingest method:mmsearch-opd (active on task:web-search-agent-rl; does not supersede method:iris / method:opd)
- Added paper:mmsearch-opd (2610.22240), method:mmsearch-opd, recipe:mmsearch-opd (`code_status: none`). Mention on task:student-distillation.
- Status active (`sota_for: []`). 9B avg 60.2 vs Qwen3.5-9B workflow 44.9 (+15.3); vs DeepVoyager-VL-8B +9.6.

### 2026-10-16 — ingest method:scope-t2i (active on task:posttrain-diffusion; does not supersede method:diffusion-opsd / method:self-opd / method:scope-opsd)
- Added paper:scope-t2i (2610.22264), method:scope-t2i, recipe:scope-t2i (`code_status: released`; MAC-AutoML/SCOPE). Distinct from method:scope-opsd.
- Status active (`sota_for: []`). +9.48% GeneVal / +7.62% T2I-CompBench vs vanilla GRPO.

### 2026-10-16 — ingest method:terminal-rsi (active on task:agent-harness-runtime; does not supersede method:omp2-harness / method:rrsi)
- Added paper:terminal-rsi (2610.22192), method:terminal-rsi, recipe:terminal-rsi (`code_status: none`).
- Status active (`sota_for: []`). TB4.0 19.84%; TB2.1 86.52%; TB3.0 16.95%; TB Hard 79.00%; LHTB 0.21→0.37.

### 2026-10-16 — ingest method:rpo (active on task:posttrain-diffusion; does not supersede method:diffusionart / method:mend)
- Added paper:rpo (2610.22282), method:rpo, recipe:rpo (`code_status: none`). Distinct from skipped root-token RPO 2610.17767.
- Status active (`sota_for: []`). Nearly 4× vs Flow-GRPO-style; dense attention restored at inference.

### 2026-10-16 — ingest method:training-free-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:training-free-opd (2610.22236), method:training-free-opd, recipe:training-free-opd (`code_status: none`).
- Status active (`sota_for: []`). Forward-only same-base specialist fusion; AIME25 rises from task-arithmetic to specialist after dropping looped answers.

### 2026-10-16 — ingest method:scoped (active on task:student-distillation; does not supersede method:opd / method:open-mopd)
- Added paper:scoped (2610.22217), method:scoped, recipe:scoped (`code_status: released`; NEUIR/SCOPED).
- Status active (`sota_for: []`). Qwen3-VL-8B +5.83 vs backbone / +3.82 vs Mix-RL.

### 2026-10-16 — ingest method:autosft (active on task:instruct-sft-alignment; does not supersede method:olmo-3)
- Added paper:autosft (2610.22194), method:autosft, recipe:autosft (`code_status: released`; Thinking-Space/AutoSFT).
- Status active (`sota_for: []`). Analysis +6.5 IFEval; synthesis +3.4 IFEval / +2.9 IFBench; code +3.7 MBPP+.

### 2026-10-16 — ingest method:sero (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy)
- Added paper:sero (2610.19397), method:sero, recipe:sero (`code_status: none`).
- Status active (`sota_for: []`). 1.5B GraphGPO ALFWorld 90.63/88.02→95.83/91.67; 7B unseen +11.20.

### 2026-10-16 — ingest method:eden (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:eden (2610.16105), method:eden, recipe:eden (`code_status: none`).
- Status active (`sota_for: []`). Pass@256 avg +6.67 vs GRPO; 7B AIME25 Pass@256 +13.33.

### 2026-10-16 — ingest method:mai-gym (active on task:hybrid-computer-use-agent-rl; does not supersede method:recreationworld / method:claude-computer-use)
- Added paper:mai-gym (2610.20939), method:mai-gym, recipe:mai-gym (`code_status: released`; Tongyi-MAI/MAI-Gym). Mention on task:computer-use-agent.
- Status active (`sota_for: []`). MobileWorld 78.4%; OSWorld-Verified 76.2% is not OSWorld 2.0; real phone 28.8→48.1.

### 2026-10-16 — ingest method:opengcua (active on task:computer-use-agent; does not supersede method:claude-computer-use)
- Added paper:opengcua (2610.22200), method:opengcua, recipe:opengcua (`code_status: released`; Tongyi-MAI/OpenGCUA).
- Status active (`sota_for: []`). OSWorld-v2 +19.6 partial / −53% steps vs batched GUI-only.

### 2026-10-16 — ingest method:harness-rsi (active on task:agent-harness-runtime; does not supersede method:omp2-harness / method:rrsi / method:aide2)
- Added paper:harness-rsi (2610.18813), method:harness-rsi, recipe:harness-rsi (`code_status: released`; zgcagi/Harness-RSI).
- Status active (`sota_for: []`). Formal Harness RSI + PAC admission bounds.

### 2026-10-16 — ingest method:flashmask-3 (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:flashmask-3 (2610.17901), method:flashmask-3, recipe:flashmask-3 (`code_status: released`; PaddlePaddle/FlashMask).
- Status active (`sota_for: []`). +45–141% TFLOPs vs FlashMask; 118B-A14B e2e +7.3–11.0%.

### 2026-10-16 — ingest method:lct (active on task:full-param-memory-efficient-pretrain; does not supersede method:scale)
- Added paper:lct (2610.22179), method:lct, recipe:lct (`code_status: none`).
- Status active (`sota_for: []`). NanoGPT −24.6% mem / +7.2% step-time; Qwen3-4B −23.8% peak.

### 2026-10-16 — note paper:score-centering-pg (gotcha on task:math-code-rl-dense; does not retarget method:cispo)
- Added paper:score-centering-pg (2610.22263). Token-level regularized IS plus group-mean baseline is biased without score centering.

### 2026-10-16 — ingest method:swe-at-scale (active on task:coding-agent-rl-environment-construction; does not supersede method:codemidas / method:mini-swe-agent)
- Added paper:swe-at-scale (2610.21359), method:swe-at-scale, recipe:swe-at-scale (`code_status: released`; cslsolow/SWE-at-scale). Mention on task:software-engineering-agent-harness.
- Status active (`sota_for: []`). Invert historical fixes into executable SWE issues.

### 2026-10-16 — ingest method:os-helix (active on task:hybrid-computer-use-agent-rl; does not supersede method:recreationworld / method:claude-computer-use / method:opengcua)
- Added paper:os-helix (2610.22234), method:os-helix, recipe:os-helix (`code_status: released`; os-copilot/OS-Helix). Mention on task:computer-use-agent.
- Status active (`sota_for: []`). 27B-RL OSWorld-Verified 66.44% is not OSWorld 2.0; Step-balanced GSPO.

### 2026-10-15 — weekday SOTA sweep (CAST-SSC, Muon LH-RL, RLVR Momentum, PMRC, PA1-OPD, Road MOPD, CriticOPD, ActionOPD, LatentLoop, HP-RLVR, Spectral-MoE, ReGRA, ForkGRPO)
- Thirteen active plug-ins and three paper-only notes. No current_sota retarget (Muon2 / CISPO / OPD / Open-MOPD / VISTA / SAO / CANOPY / OLMo-3 / Quartet-II / vanilla LoRA+rsLoRA+LR sweep / SCALE / MASKerade / SMELT / A2D).
- Window: 2026-10-15 Librarian weekday sweep after merged PR 44 (watermark 2610.18874, 1345 nodes, 352f2f9). arXiv cs.LG/cs.CL/cs.AI new listing Thu 2026-10-15 (2610.18877–2610.20607) plus HF Daily 2026-10-14 and 2026-10-15. New high id 2610.20607.
- SKIP (considered, not ingested): Tev 2610.18868 and DeltaTTG 2610.17666 (already skipped 2026-10-14); UltraBERT 2610.15028 (encoder recipe, not LLM train default); LLM-jp-4 2610.19331 (sovereign report, no reusable kernel); AFCS 2610.20086 (synthesis pipeline, not SYNTH); Vision-as-anchors 2610.19443 (ablation); multilingual MoE repetition law 2610.20247 (not OLMo-3 / moe-data-repetition overturn); data-density image SD 2610.19013 (vision, not LLM); COUNT 2610.20456 (n-gram host-memory niche); DTDD 2610.19302 (BranchOPD-adjacent takeover); token-utility 2610.18883 (another OPD keep-mask vs IER/IDA); RM-OPD 2610.20174 (GRM Mix-RL); VASPO 2610.20516 (PPO privileged-value); FSPO 2610.19687 (privileged temporal); SMD/Pivot 2610.18472 (few-step diffusion matching, not Self-OPD); MIPS 2610.19457 (large-outcome IPS); CCPO 2610.19103 (MCGPO/AdaStep-adjacent); Guide Assisted GRPO 2610.19349 (prefix replay vs VSR/RetireOPD); Explorer-Zero 2610.19868 (self-play env vs J-Zero); Agent-Reflex 2610.17953; WorkRover 2610.18067; reward hacking IF 2610.19525; fail gracefully 2610.20401; Advantage Guidance 2610.19783; Inverse Reasoning 2610.18878; textual critiques 2610.19367; cross-interface 2610.20576; policy-verified 2610.19372; Many Right Answers 2610.17771 (recommenders); Outcome-routed dLLM 2610.19271; verifier-reward flow 2610.19080; SALD 2610.01496; rank-one LoRA 2610.19033; Selective margin SFT 2610.19685; LayerTrim 2610.19121; Elastic Transformer 2610.20588 (vs ELR/ShellElastic); SpectrumQuant 2610.20303; NatScale 2610.20353; Titan-Llama 2610.19210; Cortex 2610.20399.

### 2026-10-15 — ingest method:cast-ssc (active on task:llm-pretraining-optimization; does not supersede method:muon2 / method:musec)
- Added paper:cast-ssc (2610.19761), method:cast-ssc, recipe:cast-ssc (`code_status: none`). Distinct from method:cast (cross-tokenizer OPD 2610.13257).
- Status active (`sota_for: []`). 19.08B MoE, 83.89B tokens, 5000 steps: mean val 1.26e-2 below SSC-constant, 2.10e-2 below SSC-cosine; AdaGC loss at step 4639 (7.2% fewer); 5.5% less time vs 5000 ClipByValue.

### 2026-10-15 — ingest method:muon-lh-rl (active on task:agentic-async-rl; does not supersede method:sao)
- Added paper:muon-lh-rl (2610.20256), method:muon-lh-rl, recipe:muon-lh-rl (`code_status: none`).
- Status active (`sota_for: []`). Async single-rollout: Muon + token-avg loss + truncated IS (C=2). MiniCPM5-2B / Qwen3.5-4B, R2E-Gym, Claude Code harness 2.1.118.

### 2026-10-15 — ingest method:rlvr-momentum (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:rlvr-momentum (2610.20413), method:rlvr-momentum, recipe:rlvr-momentum (`code_status: none`).
- Status active (`sota_for: []`). Scale β with η so η/(1-β) stays in the safe regime; Qwen2.5-32B AdamW +~2pp val by increasing β1. Beside adam-beta-cubic.

### 2026-10-15 — ingest method:pmrc (active on task:full-param-memory-efficient-pretrain; does not supersede method:scale)
- Added paper:pmrc (2610.19844), method:pmrc, recipe:pmrc (`code_status: none`; host gist OptimAI-Lab/Minimalist_LLM_Pretraining).
- Status active (`sota_for: []`). LLaMA C4 1.3B train 2.500 vs Fira 2.657 vs GaLore 2.842; val 2.570 vs 2.730 vs 2.875. No SCALE bake-off.

### 2026-10-15 — ingest method:pa1-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:pa1-opd (2610.19601), method:pa1-opd, recipe:pa1-opd (`code_status: none`). Mention on task:pretrain-dense-7b.
- Status active (`sota_for: []`). One-step prefix-augmented OPD for continued pretrain. Stage2 Top10 surprisal adds 48.85% to KD Macro CE gain vs NTP.

### 2026-10-15 — ingest method:road-mopd (active on task:student-distillation; does not supersede method:open-mopd)
- Added paper:road-mopd (2610.13521), method:road-mopd, recipe:road-mopd (`code_status: none`). HF Daily 2026-10-15 top paper.
- Status active (`sota_for: []`). Cross-Teacher Guarding. High-conflict Medical +5.6–8.8pp vs Vanilla MOPD. Qwen3-4B 11-task 47.92 vs ExOPD 45.53.

### 2026-10-15 — ingest method:criticopd (active on task:student-distillation; does not supersede method:opd / method:cc-opsd)
- Added paper:criticopd (2610.20572), method:criticopd, recipe:criticopd (`code_status: released`; kzhao5/CriticOPD).
- Status active (`sota_for: []`). Critique, rewrite, then score. Qwen3-1.7B 50.08→54.65 (+4.57); 0.6B 34.80→38.86; AIME24/25/AMC +6.01/+7.36/+6.94. Distinct from CC-OPSD.

### 2026-10-15 — ingest method:actionopd (active on task:student-distillation; does not supersede method:opd / method:canopy)
- Added paper:actionopd (2610.19820), method:actionopd, recipe:actionopd (`code_status: released`; thu-nics/ActionOPD). Mention on task:outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). Action-level OPD without teacher token probs / tokenizer match. Qwen3-4B/8B +3.3–6.9pp OOD.

### 2026-10-15 — ingest method:latentloop (active on task:compute-matched-moe-looped-pretrain; does not supersede method:smelt)
- Added paper:latentloop (2610.19975), method:latentloop, recipe:latentloop (`code_status: none`).
- Status active (`sota_for: []`). Compress first visit, full-res second, reallocate to width. NLL 1.988: 19.0% vs MoE Base, 7.9% vs MoE Loop. Downstream +0.73–1.18 5-shot vs Loop.

### 2026-10-15 — ingest method:hp-rlvr (active on task:math-code-rl-dense; does not supersede method:cispo / method:hdl)
- Added paper:hp-rlvr (2610.20497), method:hp-rlvr, recipe:hp-rlvr (`code_status: none`). Mention on task:outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). G=1 token credit via causal vs hindsight JSD. Qwen3-8B 1.21×/1.46×/2.30× vs G=8 GRPO math/code/ALFWorld; math 65.73 vs 63.07. Distinct from HDL.

### 2026-10-15 — ingest method:spectral-moe (active on task:dense-to-moe-upcycling; does not supersede method:maskerade)
- Added paper:spectral-moe (2610.19232), method:spectral-moe, recipe:spectral-moe (`code_status: announced`; ZacharyBroveak/Spectral-MoE README-only).
- Status active (`sota_for: []`). Dynamic 25% FFN: WikiText-2 PPL −1.04/−2.96/−2.71 on Llama-2-7B/Llama-3-8B/Qwen2.5-7B. Six-task +1.5/+4.2/+3.6 at 12.5/25/50%.

### 2026-10-15 — ingest method:regra (active on task:lora-quality-tuning; does not supersede method:lr-matters-lora / method:dt-lora)
- Added paper:regra (2610.19700), method:regra, recipe:regra (`code_status: released`; Fanyao-Li/ReGRA).
- Status active (`sota_for: []`). Two-stage residual-gradient LoRA. RoBERTa-base GLUE 84.74 vs LoRA r=8 83.21 / r=16 83.97; Llama-3-8B math 72.14 vs 70.83.

### 2026-10-15 — ingest method:forkgrpo (active on task:diffusion-lm-ar-delta-recycle; does not supersede method:a2d / method:justopd / method:canvasanneal)
- Added paper:forkgrpo (2610.19408), method:forkgrpo, recipe:forkgrpo (`code_status: none`). Mention on task:posttrain-diffusion.
- Status active (`sota_for: []`). dLLM RL fork from high-entropy states. GSM8K/MATH-500/HumanEval/MBPP 90.4/46.6/51.8/49.0 vs JustGRPO +0.8/+0.6/+1.2/+0.4; ForkGRPO-fast 2.49×.

### 2026-10-15 — note paper:muon-ns-bias (gotcha on task:llm-pretraining-optimization; does not retarget method:muon2)
- Added paper:muon-ns-bias (2610.20112). Finite Newton-Schulz + ε sends practical Muon onto Frobenius max-margin; log-growing NS recovers spectral. Theory on linear classification, not a 7B bake-off.

### 2026-10-15 — note paper:agentic-self-distill-reality (gotcha on task:outcome-only-long-horizon-agent-rl; does not retarget method:canopy)
- Added paper:agentic-self-distill-reality (2610.19789). 10 self-distill methods vs GRPO, 132 runs, 12124.4 H800-h; no method consistently beats GRPO.

### 2026-10-15 — note paper:opd-teacher-advantage (gotcha on task:student-distillation; does not retarget method:opd)
- Added paper:opd-teacher-advantage (2610.19145). Teacher advantage lives in repeated token-level corrections, not a single flip. Repeated 28.4%→74.5% vs teacher 76.9%.

### 2026-10-14 — weekday SOTA sweep (KV4-RL, TPPO, ProRubric, Monarch-Muon, PR-OPD, Mixed Precision Scaling, Multimodal Mixtures, Scaling Repeated-Data, ShellElastic, TETPO, VSR, ReTerm, JustOPD, VRSD, DT-LoRA)
- Fifteen active plug-ins and five paper-only notes. No current_sota retarget (Muon2 / CISPO / OPD / Open-MOPD / VISTA / SAO / CANOPY / OLMo-3 / Quartet-II / vanilla LoRA+rsLoRA+LR sweep / A2D / SemiCat / TRACE/TRIAGE / CodeMidas / TerminalHorizon / Repeated-Token Worth).
- Window: 2026-10-14 Librarian weekday sweep after merged PR 43 (watermark 2610.13948, 1295 nodes, a58446e). arXiv had no Tue 2026-10-13 listing; Wed 2026-10-14 listing (cs.LG/cs.CL/cs.AI new+cross) covers both days. New high id 2610.18874. HF Daily 2026-10-13 and 2026-10-14.
- SKIP (considered, not ingested): Echo 2610.14277 (TP comm systems; revisit), ObsSpec 2610.15246, RAD 2610.14572, LEAD 2610.18256, VH-GPO 2610.14000, PreSO 2610.14001 (mentioned under PR-OPD related work only), PEARL 2610.14636, PTGPO 2610.14737, ProAS 2610.18683, DeltaTTG 2610.17666, RELAY 2610.17623, CoCA 2610.17733, Ares spectral-rank RLVR optimizer 2610.16533 (repo stub), Tev 2610.18868, Long-CoT behavioral distillation 2610.17607, Taming Softmax/Muon 2610.17588, LatentMoE shape 2610.14644, VHA 2610.17959, RPO root-token 2610.17767, dLLM RL (RePara 2610.18200, PACT-dLLM 2610.17266; `method:pact` already exists), Apertus 1.5 2610.15542.

### 2026-10-14 — ingest method:mixed-precision-scaling (active on task:fp4-hardware-training; does not supersede method:quartet-ii)
- Added paper:mixed-precision-scaling (2610.17637), method:mixed-precision-scaling, recipe:mixed-precision-scaling (`code_status: none`). Mention on task:full-param-memory-efficient-pretrain.
- Status active (`sota_for: []`). 430M Qwen3 @ 12.8B: bwd-only +0.32–0.72%, fwd-only +0.94–1.22%; law up to 11× lower MSE. Single-paper baselines.

### 2026-10-14 — ingest method:multimodal-data-mixtures (active on task:open-data-recipe; does not supersede method:olmo-3)
- Added paper:multimodal-data-mixtures (2610.14423, NeurIPS 2026 spotlight, `evidence_level: peer-reviewed`), method:multimodal-data-mixtures, recipe:multimodal-data-mixtures (`code_status: none`). Mention on task:pretrain-moe-frontier.
- Status active (`sota_for: []`). 268 MoE runs 457M–8.3B; vision α=0.50 β=0.51, text α=β=0.34, audio α=0.32; saturate ~2×.

### 2026-10-14 — ingest method:scaling-repeated-data (active on task:data-constrained-pretrain; does not supersede method:repeated-token-worth / method:repetition-count-selection)
- Added paper:scaling-repeated-data (2610.15965), method:scaling-repeated-data, recipe:scaling-repeated-data (`code_status: none`).
- Status active (`sota_for: []`). U-shaped loss vs batch size; B=64 vs 512 1.5B CE 3.124→2.977; tying+emb WD 2.971→2.946.

### 2026-10-14 — ingest method:monarch-muon (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:monarch-muon (2610.17429), method:monarch-muon, recipe:monarch-muon (`code_status: none`). Mention on task:full-param-memory-efficient-pretrain.
- Status active (`sota_for: []`). 3.06 vs 3.09 (257M vs Monarch-AdamW; dense Muon 2.99 is better); 1B MoE 2.68 vs 2.77; 6.89B peak mem −23% / opt step 1288.3→304.4 ms.

### 2026-10-14 — ingest method:shell-elastic (active on task:llm-pretraining-optimization; does not supersede method:muon2 / method:elr)
- Added paper:shell-elastic (2610.15124), method:shell-elastic, recipe:shell-elastic (`code_status: released`; jincan333/ShellElastic). Mention on task:elastic-depth-looped-lm.
- Status active (`sota_for: []`). Mean val loss 0.028/0.005/0.018 nats below best baseline; best/tied 12/15 val-loss, 14/15 5-shot. HF Daily 2026-10-14.

### 2026-10-14 — ingest method:kv4-rl (active on task:fp4-rl-train-rollout-alignment; does not supersede method:trace / method:triage)
- Added paper:kv4-rl (2610.14448), method:kv4-rl, recipe:kv4-rl (`code_status: none`). Mention on task:agentic-async-rl.
- Status active (`sota_for: []`). Qwen3-8B-Base GRPO 1.80× rollout / MATH-500 87.68 vs BF16 88.16; plain INT4 −5.24pp even with TIS.

### 2026-10-14 — ingest method:tetpo (active on task:agentic-async-rl; does not supersede method:sao / method:cispo)
- Added paper:tetpo (2610.14440), method:tetpo, recipe:tetpo (`code_status: none`). Mention on task:math-code-rl-dense.
- Status active (`sota_for: []`). Qwen3-Base-1.7B k=32 avg@16 44.4 vs M2PO 42.3 / GSPO 39.0; Llama-3.2-3B-Instruct 18.5 vs GEPO 16.2.

### 2026-10-14 — ingest method:tppo (active on task:token-level-critic-rl; does not supersede method:bpco / method:pact)
- Added paper:tppo (2610.16794), method:tppo, recipe:tppo (`code_status: released`; LINs-lab/TPPO).
- Status active (`sota_for: []`). Qwen3-4B/8B-Base math 41.6 vs PPO 34.6 / 45.9 vs 37.5. HF Daily 2026-10-14.

### 2026-10-14 — ingest method:vsr (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:vsr (2610.15888), method:vsr, recipe:vsr (`code_status: none`). Mention on task:outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). Qwen2.5-7B 37.6 vs GRPO 36.1; Llama-3.2-3B 19.1 vs 15.4; GiGPO+VSR BabyAI 47.6 vs 30.4. Distinct from NGU / ThinkPrior.

### 2026-10-14 — ingest method:prorubric (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:draco / method:metarubric)
- Added paper:prorubric (2609.38847), method:prorubric, recipe:prorubric (`code_status: released`; Estrellajer/ProRubric). Mention on task:multi-reward-rlvr.
- Status active (`sota_for: []`). HealthBench 4B appropriateness 36.8 vs Rubric-RL 26.0 (untrained 54.1 is not a win). HF Daily 2026-10-14.

### 2026-10-14 — ingest method:reterm (active on task:coding-agent-rl-environment-construction; does not supersede method:codemidas / method:t1-terminal-rl / method:terminalhorizon)
- Added paper:reterm (2610.18484), method:reterm, recipe:reterm (`code_status: released`; twothsnd/ReTerm). Mention on task:outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). ReTerm-9B Qwen3.5-9B TB2.0 Pass@1 34.8 (+14.6); SWE-Verified 58.4%.

### 2026-10-14 — ingest method:justopd (active on task:diffusion-lm-ar-delta-recycle; does not supersede method:a2d / method:opd)
- Added paper:justopd (2610.17397), method:justopd, recipe:justopd (`code_status: none`). Mentions on task:student-distillation / task:continuous-diffusion-lm-pretrain.
- Status active (`sota_for: []`). Dream-7B + Qwen3-14B L=256 GSM8K 77.03→81.80 / MATH500 31.80→39.60.

### 2026-10-14 — ingest method:pr-opd (active on task:privileged-teacher-opsd; does not supersede method:vista)
- Added paper:pr-opd (2609.36642), method:pr-opd, recipe:pr-opd (`code_status: released`; balibata/PR-OPD). Mention on task:outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). WebShop skill 42.2→56.2; after GRPO Qwen2.5-3B-Instruct +4.7 ALFWorld / +11.7 WebShop. PreSO 2610.14001 related work only.

### 2026-10-14 — ingest method:vrsd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:nsd)
- Added paper:vrsd (2610.16354), method:vrsd, recipe:vrsd (`code_status: released`; lijiazheng99/VRSD).
- Status active (`sota_for: []`). 11/12 settings; avg +3.9pp Pass@1; SQL OPSD 69.8 vs VRSD 81.0.

### 2026-10-14 — ingest method:dt-lora (active on task:lora-quality-tuning; does not supersede method:lr-matters-lora)
- Added paper:dt-lora (2610.17730), method:dt-lora, recipe:dt-lora (`code_status: announced`; Snipine/DT-LoRA README-only).
- Status active (`sota_for: []`). VTAB-1K 76.2 vs LoRA 75.7; COCO r=16 avg 46.6 (+8.2).

### 2026-10-14 — note paper:dlm-ar-compute-gap (gotcha on task:continuous-diffusion-lm-pretrain / task:diffusion-lm-ar-delta-recycle; does not retarget method:semicat / method:a2d)
- Added paper:dlm-ar-compute-gap (2610.17590). Project guanghanwang.com/dlm-scaling. ELBO MDM 17.8×; DUEL 12.8×; E2D2 b=32/8/4 = 7.8/4.6/3.0×; BD3LM 32/16/8/4 = 9.6/7.8/5.9/4.1 DUEL. Older 16× claims used ELBO/full-sequence protocol.

### 2026-10-14 — note paper:two-clocks-rlvr (gotcha on task:math-code-rl-dense; does not retarget method:cispo)
- Added paper:two-clocks-rlvr (2610.18853). WinstonLiyt/two-clocks-rlvr 404 (`code_status` announced/none). Qwen2.5-Math-1.5B 4096 fails 56–80 steps / 512 after 648, both 30–50k samples.

### 2026-10-14 — note paper:self-distillation-ood (gotcha on task:privileged-teacher-opsd; does not retarget method:vista)
- Added paper:self-distillation-ood (2610.18613). Code sleepypandu/does-sd-improve-reasoning. SDPO LCB test_unseen Qwen3-8B −2.5 vs GRPO +3.7; science OOD −7.1 to −16.6.

### 2026-10-14 — note paper:opd-failure-problems (gotcha on task:student-distillation; does not retarget method:opd)
- Added paper:opd-failure-problems (2610.18011). 8/8 fail-set configs degrade (p=0.0078) while KL drops; same pipeline +4.6pp on non-failure mix (Qwen2.5-0.5B GSM8K 43.6→48.2).

### 2026-10-14 — note paper:thinking-leakage (gotcha on task:reasoning-rl-alignment; does not retarget method:cispo)
- Added paper:thinking-leakage (2610.14270). Mention on task:math-code-rl-dense. Qwen3-8B AIME no-think 0.17→0.43 vs think-mode 0.74; 8D subspace G=0.222 removes 75%.

### 2026-10-13 — weekday SOTA sweep (ELR, MSAR, BranchOPD, SemiCat, TerminalHorizon, UGPC, SAVER, D2R, Representation Guidance, ReplaySSM, Specialists Learn Faster, LatentGRM)
- Twelve active plug-ins, three new tasks (`elastic-depth-looped-lm`, `continuous-diffusion-lm-pretrain`, `pixel-diffusion-pretrain`), three paper-only notes. No current_sota retarget of existing tasks (Muon2 / OPD / Open-MOPD / CANOPY / CodeMidas / OraRL / EfficientTDMPC / Mamba-2 / OLMo-3 / CISPO / A2D / SMELT / Looped Models Done Right). New tasks seed first hops with method `sota_for: []`.
- Window: 2026-10-13 Librarian weekday sweep after merged PR 42 (watermark 2610.13767, 1253 nodes, 14c9b58). New high id 2610.13948. HF Daily 2026-10-12 and partial 2026-10-13.

### 2026-10-13 — ingest method:elr (first hop on task:elastic-depth-looped-lm; does not supersede method:looped-models-done-right / method:smelt)
- Added paper:elr (2610.12582), method:elr, recipe:elr (`code_status: none`), task:elastic-depth-looped-lm. Mentions on task:recurrent-encoder-decoder-lm and task:compute-matched-moe-looped-pretrain.
- Status active (`sota_for: []`). Mixed-depth looped LM. 4B dense 1 loop −0.52 / 4 loops +7.25; 30B-A3B +1.04 / +4.75 (10-task avg).

### 2026-10-13 — ingest method:msar (active on task:llm-pretraining-optimization; does not supersede method:attnres / method:mhc / method:muon2)
- Added paper:msar (2610.13630), method:msar, recipe:msar (`code_status: released`; jianke0604/MSAR).
- Status active (`sota_for: []`). Beats vanilla/mHC/AttnRes on 12 benches at 18B and 28B MoE; iso-loss 1.58× vs 1.35× AttnRes, 1.30× mHC. Single-paper baselines.

### 2026-10-13 — ingest method:branchopd (active on task:student-distillation; does not supersede method:opd / method:canopy)
- Added paper:branchopd (2610.13481), method:branchopd, recipe:branchopd (`code_status: announced`; chendy25/BranchOPD empty stub). Mention on task:outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). +18.55pp math avg@16, +13.8pp ALFWorld vs vanilla OPD; ~19%/31% fewer student tokens vs n=7.

### 2026-10-13 — ingest method:semicat (first hop on task:continuous-diffusion-lm-pretrain; does not supersede method:a2d / method:canvasanneal)
- Added paper:semicat (2610.13834), method:semicat, recipe:semicat (`code_status: none`), task:continuous-diffusion-lm-pretrain. Mentions on task:diffusion-lm-ar-delta-recycle and task:posttrain-diffusion.
- Status active (`sota_for: []`). SemiCat 49.94% TinyGSM; 1.7B beats discrete diffusion on 4/6 likelihood evals. Experimental evidence.

### 2026-10-13 — ingest method:terminalhorizon (active on task:coding-agent-rl-environment-construction; does not supersede method:codemidas / method:t1-terminal-rl)
- Added paper:terminalhorizon (2610.13166), method:terminalhorizon, recipe:terminalhorizon (`code_status: none`; project zs1314.github.io/TerminalHorizon).
- Status active (`sota_for: []`). 1,535 envs / 2,852 traj. SFT Qwen3.5-27B TB1.0 55.0 (+8.7); TB2.1 46.82→60.67.

### 2026-10-13 — ingest method:ugpc (active on task:student-distillation; does not supersede method:opd)
- Added paper:ugpc (2610.12933), method:ugpc, recipe:ugpc (`code_status: released`; Jackbrocp/Learning-More-by-Training-Less).
- Status active (`sota_for: []`). CoT-SFT contraction. Matches/beats full-data reasoning SFT at 0.22–1.91% of the optimization budget.

### 2026-10-13 — ingest method:saver (active on task:rl-video-mllm; does not supersede method:orarl)
- Added paper:saver (2610.10893), method:saver, recipe:saver (`code_status: released`; lmsdss/SAVER).
- Status active (`sota_for: []`). Dense/sparse paired-view video RL. Qwen3.5-2B 0.1fps mIoU 18.4→30.0; QA 45.9→50.8.

### 2026-10-13 — ingest method:d2r (active on task:continuous-control-world-model; does not supersede method:efficienttdmpc)
- Added paper:d2r (2610.13816), method:d2r, recipe:d2r (`code_status: none`).
- Status active (`sota_for: []`). Frozen-policy continual RL via world-model imagination. CALVIN 8 tasks 63.7%→74.8% vs LoRA FT 11.7%.

### 2026-10-13 — ingest method:representation-guidance (first hop on task:pixel-diffusion-pretrain; does not supersede method:diffusion-opsd / method:self-opd)
- Added paper:representation-guidance (2610.12978), method:representation-guidance, recipe:representation-guidance (`code_status: released`; Pan-Zihao/Representation-Guidance), task:pixel-diffusion-pretrain.
- Status active (`sota_for: []`). ImageNet-256 XL/16 FID 1.55; IN-512 FID 1.74; GenEval 0.89.

### 2026-10-13 — ingest method:replayssm (active on task:linear-time-sequence-modeling; does not supersede method:mamba-2 / method:deepseek-v41-flash)
- Added paper:replayssm (2610.13778), method:replayssm, recipe:replayssm (`code_status: released`; Johnny-Liou/ReplaySSM). Mention on task:input-heavy-agentic-moe-serving.
- Status active (`sota_for: []`). vLLM Mamba-2 / Gated DeltaNet 1.20–1.47× decode at batch 256; ~1.8× vs vLLM spec decoding on 120B-class.

### 2026-10-13 — ingest method:specialists-learn-faster (active on task:open-data-recipe; does not supersede method:olmo-3 / method:aclarena)
- Added paper:specialists-learn-faster (2610.13835), method:specialists-learn-faster, recipe:specialists-learn-faster (`code_status: none`; project horizon-lab.org/specialist/). Mention on task:agent-continual-learning.
- Status active (`sota_for: []`). Chronological specialists need fewer update steps. Data-ordering gotcha.

### 2026-10-13 — ingest method:latentgrm (active on task:reasoning-rl-alignment; does not supersede method:cispo / method:sapo)
- Added paper:latentgrm (2610.09788), method:latentgrm, recipe:latentgrm (`code_status: released`; EADMO/LatentGRM).
- Status active (`sota_for: []`). Latent-space generative RM. ~9× shorter eval trajectories; 6–7× faster at vote@5.

### 2026-10-13 — note paper:massive-activation-lifecycle (gotcha on task:llm-pretraining-optimization; does not retarget method:muon2)
- Added paper:massive-activation-lifecycle (2610.00423). Code apd-smcclendon/massive_activations_2. Weight decay causally controls massive-activation magnitude.

### 2026-10-13 — note paper:llm-abstention (gotcha on task:reasoning-rl-alignment; does not retarget method:cispo)
- Added paper:llm-abstention (2610.13821). RL variants did not consistently improve abstention on Qwen3-14B; learned selector TriviaQA coverage 20.2%→30.9%, error 23.0%→14.5%.

### 2026-10-13 — note paper:randomized-momentum-transport (gotcha on task:llm-pretraining-optimization; does not retarget method:muon2)
- Added paper:randomized-momentum-transport (2610.13789). Theory O(T^{-1/3}) for Muon/sign updates; MNIST1D / CIFAR-10 only.

### 2026-10-12 — weekday SOTA sweep (DiffusionART, CAST, State-OPD, RPD-OPD, SynthSelf, S3R, MCGPO, SoftwareGym, ProgramGym, AgentTune, TAPO, GPPO, DualQuant, STAPLE, TreeHCA, CV-OPD, CC-OPSD, ReHarness, CBPO, MagicBeanStalk, PPO-FP16, SoloQ, TIPS)
- Twenty-three active plug-ins. No current_sota retarget of DiffusionOPSD / Self-OPD / Cross-Tokenizer OPD / CANOPY / OPD / Open-MOPD / ACLArena / Miles / CISPO / RecreationWorld / Claude computer-use / CodeMidas / SAO / Quartet-II / MASKerade / VISTA / ACE / omp2 / VeriGate / EfficientTDMPC / A2D / SLCA-GRPO.
- Window: 2026-10-12 Librarian weekday sweep covering arXiv Mon cs.LG/CL/AI + HF Daily 2026-10-12 after merged PR 41 (watermark 2610.12444, 1184 nodes, 0149ebd). New high id 2610.13767.

### 2026-10-12 — ingest method:diffusionart (active on task:posttrain-diffusion; does not supersede method:diffusion-opsd / method:self-opd / method:mend)
- Added paper:diffusionart (2610.12572), method:diffusionart, recipe:diffusionart (`code_status: released`; vanzll/DiffusionART).
- Status active (`sota_for: []`). Aggregation-first reward tilting. HunyuanVideo-13B ~12× fewer GPU-hrs vs DiffusionNFT / Flow-GRPO-Fast.

### 2026-10-12 — ingest method:cast (active on task:cross-tokenizer-opd; does not supersede method:cross-tokenizer-opd)
- Added paper:cast (2610.13257), method:cast, recipe:cast (`code_status: none`).
- Status active (`sota_for: []`). Chunk-credit alignment after correspondence. +2.45 Mistral-7B / +1.32 Llama-3.1-8B vs strongest evaluated baseline.

### 2026-10-12 — ingest method:state-opd (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:opd / method:pivotopd)
- Added paper:state-opd (2610.13238), method:state-opd, recipe:state-opd (`code_status: none`). Mention on task:student-distillation.
- Status active (`sota_for: []`). State-grounded multi-turn OPD. Qwen3-4B macro 31.74 vs 26.07.

### 2026-10-12 — ingest method:rpd-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:rpd-opd (2610.13205), method:rpd-opd, recipe:rpd-opd (`code_status: none`).
- Status active (`sota_for: []`). Relative Δπ transfer via expert-minus-reference log-ratios. Task-specific residuals transfer; scale-only residuals do not.

### 2026-10-12 — ingest method:synthself (active on task:agent-continual-learning; does not supersede method:aclarena / method:opd)
- Added paper:synthself (2610.13113), method:synthself, recipe:synthself (`code_status: none`). Mention on task:student-distillation.
- Status active (`sota_for: []`). Same-family aligner rewrite + rejection sampling then off-policy train of a small student.

### 2026-10-12 — ingest method:s3r (active on task:frontier-rl-posttrain-stack; does not supersede method:miles / method:cispo)
- Added paper:s3r (2610.13202), method:s3r, recipe:s3r (`code_status: none`). Mention on task:math-code-rl-dense.
- Status active (`sota_for: []`). Same-policy sparse-draft / dense-verify RL rollouts. 1.39×–1.35× vs dense AR.

### 2026-10-12 — ingest method:mcgpo (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:sao)
- Added paper:mcgpo (2610.13755), method:mcgpo, recipe:mcgpo (`code_status: none`).
- Status active (`sota_for: []`). Matched-context pairwise credit. +3.96 / +5.16pp WebShop Qwen3-4B/8B vs GraphGPO.

### 2026-10-12 — ingest method:softwaregym (active on task:hybrid-computer-use-agent-rl; does not supersede method:recreationworld / method:claude-computer-use)
- Added paper:softwaregym (2610.12611), method:softwaregym, recipe:softwaregym (`code_status: none`). Mention on task:computer-use-agent.
- Status active (`sota_for: []`). Synthesized GUI apps. OSWorld Pass@3 41.39%→56.97% is transfer, not paper-protocol ranking.

### 2026-10-12 — ingest method:programgym (active on task:coding-agent-rl-environment-construction; does not supersede method:codemidas / method:mini-swe-agent)
- Added paper:programgym (2610.13395), method:programgym, recipe:programgym (`code_status: announced`).
- Status active (`sota_for: []`). From-scratch program reproduction. Qwen3.8-27B 34.87%→42.84% SFT / Program-Agent 55.71%.

### 2026-10-12 — ingest method:agenttune (active on task:agentic-async-rl; does not supersede method:sao / method:miles)
- Added paper:agenttune (2610.13335), method:agenttune, recipe:agenttune (`code_status: released`; Lexsi-Labs/AgentTune). Mention on task:frontier-rl-posttrain-stack.
- Status active (`sota_for: []`). Two-tier EventLog lifecycle. No Pass@1 bake-off vs SAO.

### 2026-10-12 — ingest method:tapo (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:tapo (2610.13020), method:tapo, recipe:tapo (`code_status: none`).
- Status active (`sota_for: []`). Trajectory state-distribution correction. Up to +48% math / +12% coding vs GRPO, not CISPO.

### 2026-10-12 — ingest method:gppo (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:gppo (2610.13015), method:gppo, recipe:gppo (`code_status: none`).
- Status active (`sota_for: []`). f-divergence PPO geometry. Up to +50% math / +14% coding vs GRPO. Sibling of TAPO.

### 2026-10-12 — ingest method:dualquant (active on task:fp4-hardware-training; does not supersede method:quartet-ii / method:kbbq)
- Added paper:dualquant (2610.13767), method:dualquant, recipe:dualquant (`code_status: none`).
- Status active (`sota_for: []`). Dual-scale calibration-free W+A PTQ. Packed W4A4 up to 2.61× memory cut.

### 2026-10-12 — ingest method:staple (active on task:dense-to-moe-upcycling; does not supersede method:maskerade)
- Added paper:staple (2610.12599), method:staple, recipe:staple (`code_status: none`).
- Status active (`sota_for: []`). Token-indexed embedding residuals, not routed experts. OLMo-2 1B +4.27 HumanEval vs continued dense.

### 2026-10-12 — ingest method:treehca (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:pact)
- Added paper:treehca (2610.12828), method:treehca, recipe:treehca (`code_status: announced`; TheBlackCat22/TreeHCA 404). Mention on task:tool-agent-segment-credit.
- Status active (`sota_for: []`). Hindsight-guided tree exploration plus turn-level backup.

### 2026-10-12 — ingest method:cv-opd (active on task:student-distillation; does not supersede method:opd / method:where-opd)
- Added paper:cv-opd (2610.13264), method:cv-opd, recipe:cv-opd (`code_status: none`).
- Status active (`sota_for: []`). Contrastive crop teachers plus visual-token gate against VLM shortcuts.

### 2026-10-12 — ingest method:cc-opsd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:srd)
- Added paper:cc-opsd (2610.13744), method:cc-opsd, recipe:cc-opsd (`code_status: none`).
- Status active (`sota_for: []`). Critique then score. Scoring-only KL does not sit on gold error spans.

### 2026-10-12 — ingest method:reharness (active on task:agent-continual-learning; does not supersede method:aclarena / method:ace / method:omp2-harness)
- Added paper:reharness (2610.12668), method:reharness, recipe:reharness (`code_status: none`). Mentions on task:agent-harness-runtime and task:agent-memory.
- Status active (`sota_for: []`). Backward-revises retrieved reflections. Text harness, not weight-space CL.

### 2026-10-12 — ingest method:cbpo (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:cbpo (2610.12830), method:cbpo, recipe:cbpo (`code_status: none`).
- Status active (`sota_for: []`). Unified reward-vs-reference regression across gold, negatives, live, and replay. +2.33 avg@32 / +4.44 pass@32 vs SFT then DAPO.

### 2026-10-12 — ingest method:magicbeanstalk (active on task:math-code-rl-dense; does not supersede method:cispo / method:verigate / method:srd)
- Added paper:magicbeanstalk (2610.12659), method:magicbeanstalk, recipe:magicbeanstalk (`code_status: none`). Mention on task:all-zero-verifier-groups.
- Status active (`sota_for: []`). Recursive calibrated children from always-fail seeds. gpt-oss-120b 61.2→69.8; DeepSeek v4Flash 72.4→77.9.

### 2026-10-12 — ingest method:ppo-fp16 (active on task:continuous-control-world-model; does not supersede method:efficienttdmpc)
- Added paper:ppo-fp16 (2610.13306), method:ppo-fp16, recipe:ppo-fp16 (`code_status: none`).
- Status active (`sota_for: []`). Residual-protected FP16 PPO for continuous control, not LLM RL. Optimizer state −71.7–74.9%.

### 2026-10-12 — ingest method:soloq (active on task:fp4-hardware-training; does not supersede method:quartet-ii / method:a2d)
- Added paper:soloq (2610.07121), method:soloq, recipe:soloq (`code_status: announced`; Intelligent-Computing-Lab-Panda/SoloQ 404). Mention on task:diffusion-lm-ar-delta-recycle. HF Daily 2026-10-12.
- Status active (`sota_for: []`). Calibration-free dLLM PTQ. NVFP4 up to 2.61× peak-memory / 2.24× e2e.

### 2026-10-12 — ingest method:tips (active on task:all-zero-verifier-groups; does not supersede method:verigate / method:srd / method:cispo)
- Added paper:tips (2609.36641), method:tips, recipe:tips (`code_status: released`; RUCBM/TIPS). Mention on task:math-code-rl-dense. HF Daily 2026-10-12.
- Status active (`sota_for: []`). Outcome-only RL inducing a generative PRM. ProcessBench F1 85.2.

### 2026-10-09 — weekday SOTA sweep (MetaOPD, DIAL-OPD, Semi-OPD, Delta-MOPD, GRPODropout, ExpDis, SCAPO, ReSPO, SRD, KLPO, COPC, ZIP-SR, Spectrally Targeted Muon, SAPD, OnlineQAT, MiMo-V2.6, OPD vanishing-signals, OPD skill-not-knowledge)
- Sixteen active plug-ins and two paper-only notes. No current_sota retarget of OPD / Open-MOPD / CISPO / SAO / Muon2 / GradCodeS / VISTA / Miles / VeriGate / SCALE.
- Window: 2026-10-09 Librarian weekday sweep covering arXiv + HF Daily 2026-10-08 and 2026-10-09 after a failed 10-08 pass; watermark was 2610.08624 (PR 40, 1134 nodes). New high id 2610.12444.

### 2026-10-09 — ingest method:metaopd (active on task:student-distillation; does not supersede method:opd)
- Added paper:metaopd (2610.11989), method:metaopd, recipe:metaopd (`code_status: none`).
- Status active (`sota_for: []`). Bilevel token weights from post-update validation NLL. Avg@8/Pass@8 +1.99/+5.97 (0.6B), +2.25/+6.41 (1.7B) vs uniform OPD.

### 2026-10-09 — ingest method:dial-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:dial-opd (2610.11659), method:dial-opd, recipe:dial-opd (`code_status: released`; EIT-NLP/DIAL-OPD).
- Status active (`sota_for: []`). Probability-space keep-mask. Up to +5.25pp at 40% tokens; Pass@16 13.33→26.67.

### 2026-10-09 — ingest method:semi-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:semi-opd (2610.11291), method:semi-opd, recipe:semi-opd (`code_status: none`).
- Status active (`sota_for: []`). Freeze rollouts at the initial student. 14/17 pairs; up to +13.6% / 11.4× vs live OPD when overlap is low.

### 2026-10-09 — ingest method:delta-mopd (active on task:student-distillation; does not supersede method:open-mopd)
- Added paper:delta-mopd (2610.10460), method:delta-mopd, recipe:delta-mopd (`code_status: none`).
- Status active (`sota_for: []`). Teacher-minus-base logit shifts. +4.11 Math / +1.95 five-benchmark. Paper Open-MOPD numbers are not the library 83.4% bake-off.

### 2026-10-09 — ingest method:grpodropout (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:grpodropout (2610.11854), method:grpodropout, recipe:grpodropout (`code_status: released`; hexuandeng/GRPODropout).
- Status active (`sota_for: []`). Drops high-probability positive-advantage traces. Abstract-backed accuracy/entropy claims only.

### 2026-10-09 — ingest method:expdis (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:expdis (2610.10536), method:expdis, recipe:expdis (`code_status: released`; SaifPunjwani/Exploration-Distillation).
- Status active (`sota_for: []`). Novelty-rewarded explorers distilled into a student without novelty. Beats DAPO at matched wall-clock.

### 2026-10-09 — ingest method:scapo (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:scapo (2609.40360), method:scapo, recipe:scapo (`code_status: released`; DtYXs/SCAPO). HF Daily 2026-10-08.
- Status active (`sota_for: []`). Semifactual token credit. Qwen3-4B/1.7B AIME +5.63/+4.17 vs GRPO.

### 2026-10-09 — ingest method:respo (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:respo (2609.35433), method:respo, recipe:respo (`code_status: released`; yhangchen/ReSPO-code). HF Daily 2026-10-09. Mention on task:frontier-rl-posttrain-stack.
- Status active (`sota_for: []`). Two-branch alpha-divergence sequence kernel instead of IS clip.

### 2026-10-09 — ingest method:srd (active on task:math-code-rl-dense; does not supersede method:cispo / method:verigate / method:vista)
- Added paper:srd (2610.08077), method:srd, recipe:srd (`code_status: released`; SalesforceAIResearch/SRD). HF Daily 2026-10-08. Mentions on task:all-zero-verifier-groups and task:privileged-teacher-opsd.
- Status active (`sota_for: []`). Hindsight-to-foresight when groups are silent. Up to +24.2pp; 2B all-fail 0.0% vs 60.6%.

### 2026-10-09 — ingest method:klpo (active on task:agentic-async-rl; does not supersede method:sao)
- Added paper:klpo (2610.08963), method:klpo, recipe:klpo (`code_status: released`; yifanzhang-pro/KLPO).
- Status active (`sota_for: []`). Sampler-anchored KL least-squares; one rollout; no IS clip. No numeric bake-off in the abstract.

### 2026-10-09 — ingest method:copc (active on task:agentic-async-rl; does not supersede method:sao)
- Added paper:copc (2610.09597), method:copc, recipe:copc (`code_status: none`).
- Status active (`sota_for: []`). Coupled policy-side IS and advantage-staleness TD correction. 1.7× vs sync PPO; 64-step staleness.

### 2026-10-09 — ingest method:zip-sr (active on task:llm-pretraining-optimization; does not supersede method:muon2 / method:scale)
- Added paper:zip-sr (2610.12444), method:zip-sr, recipe:zip-sr (`code_status: none`). Mention on task:full-param-memory-efficient-pretrain.
- Status active (`sota_for: []`). 4-bit AdamW second-moment codebook with preconditioner-space SR. Up to 70% TorchAO gap cut.

### 2026-10-09 — ingest method:spectrally-targeted-muon (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:spectrally-targeted-muon (2610.10965), method:spectrally-targeted-muon, recipe:spectrally-targeted-muon (`code_status: none`).
- Status active (`sota_for: []`). Thresholded orthogonalization: small singular values carry the Muon gain. Not a 7B bake-off.

### 2026-10-09 — ingest method:sapd (active on task:privileged-teacher-opsd; does not supersede method:vista)
- Added paper:sapd (2610.09665), method:sapd, recipe:sapd (`code_status: released`; Miaow-Lab/SAPD). Mention on task:student-distillation.
- Status active (`sota_for: []`). Rollout-free step-aligned privileged distillation. ~2× vs on-policy.

### 2026-10-09 — ingest method:onlineqat (active on task:full-lowbit-finetune; does not supersede method:gradcodes)
- Added paper:onlineqat (2610.09346), method:onlineqat, recipe:onlineqat (`code_status: none`). Mention on task:student-distillation.
- Status active (`sota_for: []`). Block-wise QAT then on-policy reverse-KL. Qwen3-1.7B 57.28 W3A16 / 32.52 W2A16.

### 2026-10-09 — ingest method:mimo-v26 (active on task:frontier-rl-posttrain-stack; does not supersede method:miles)
- Added paper:mimo-v26 (2610.11959), method:mimo-v26, recipe:mimo-v26 (`code_status: announced`).
- Status active (`sota_for: []`). Omni-modal scaled-RL playbook: router freeze, groupwise agentic grading, 1568 samples / 2.7–3.7B tokens/step.

### 2026-10-09 — claim note paper:opd-vanishing-signals (no new method)
- Added paper:opd-vanishing-signals (2610.11247) on method:opd. Larger-scale teachers 25.1% vs self-RL 96.2% loss reduction after 200 updates. Code leizhao7/opd-learning-signals. Does not retarget OPD.

### 2026-10-09 — claim note paper:opd-skill-not-knowledge (no new method)
- Added paper:opd-skill-not-knowledge (2610.09639) on method:opd. Reverse-KL OPD transfers compositional skill, not new facts. Does not retarget OPD.


### 2026-10-07 — weekday SOTA sweep (Cross-Tokenizer OPD, TRACE, TRIAGE, NeMo-DCR, NP-OPD, Adam shared-β cubic, BulkBoost, DRMoET, Hierarchical MoE routing, FC-SWE, RGPO, GA-GRPO, Privileged Context as Drift, OPD-safety backdoor, A2D, MASKerade, DART-ES)
- Four new tasks (`task:cross-tokenizer-opd`, `task:fp4-rl-train-rollout-alignment` dual-active TRACE+TRIAGE, `task:diffusion-lm-ar-delta-recycle`, `task:dense-to-moe-upcycling`), fifteen active/niche methods, two paper-only notes (`paper:ga-grpo`, `paper:opd-safety-backdoor`). No current_sota retarget of CISPO / VISTA / OPD / Muon2 / AdamW / Miles / Quartet-II / ES-reasoning / Category-Aware SWE Experts / SAPO / DeepSeek-V4 / Kimi-K3 / CanvasAnneal / DiffusionOPSD.
- Window: 2026-10-07 Librarian weekday sweep after PR 39; watermark was 2610.06833. New arXiv 2610.08448, 2610.07767, 2610.07043, 2610.08430, 2610.07874, 2610.08624, 2610.07497, 2610.07207, 2610.07332, 2610.07898, 2610.07342, 2610.06861, 2610.07842, 2610.07654, 2610.08108, 2610.07809, 2610.06993.

### 2026-10-07 — ingest method:cross-tokenizer-opd (active first hop on task:cross-tokenizer-opd; does not supersede method:opd)
- Added paper:cross-tokenizer-opd (2610.08448), method:cross-tokenizer-opd, recipe:cross-tokenizer-opd (`code_status: none`). Reverse redirect from student-distillation.
- Status active (`sota_for: []`). Strict 1:1 covers 85.57–96.98% of student tokens; k=16 retains ≥96% of full shared-vocab OPD.
- Evidence: arXiv:2610.08448; verified: true; evidence_level: preprint. Top HF Daily paper 2026-10-07.

### 2026-10-07 — ingest method:trace / method:triage (dual-active on task:fp4-rl-train-rollout-alignment; does not supersede method:quartet-ii)
- Added paper:trace (2610.07767), method:trace, recipe:trace (`code_status: none`). Rollout-guided QAT; up to 5.4× rollout.
- Added paper:triage (2610.07043), method:triage, recipe:triage (`code_status: none`). Direction-aware NVFP4 mismatch; up to 2.3× rollout vs BF16.
- Status active (`sota_for: []`). No head-to-head. Reverse redirect from fp4-hardware-training.

### 2026-10-07 — ingest method:nemo-dcr (active on task:frontier-rl-posttrain-stack; does not supersede method:miles)
- Added paper:nemo-dcr (2610.08430), method:nemo-dcr, recipe:nemo-dcr (`code_status: released`; NVIDIA-NeMo/RL PR #2444).
- Status active (`sota_for: []`). Bit-exact delta-compressed refit; ~1% of BF16 weights change per step; 1T 150s vs 87.5 min.

### 2026-10-07 — ingest method:np-opd (active on task:student-distillation; does not supersede method:opd / method:nsd)
- Added paper:np-opd (2610.07874), method:np-opd, recipe:np-opd (`code_status: released`; `repo_url: https://github.com/naver-ai/np-opd`).
- Status active (`sota_for: []`). Negative-policy rollouts when teacher/student overlap is low.

### 2026-10-07 — ingest method:adam-beta-cubic (active on task:llm-pretraining-optimization; does not supersede method:muon2 / method:adamw-optimizer)
- Added paper:adam-beta-cubic (2610.08624), method:adam-beta-cubic, recipe:adam-beta-cubic (`code_status: released`; AlbertoFdezHdez/Adam_beta_rule_cubic).
- Status active (`sota_for: []`). 40.7% lower mean relative val gap vs β=0.95 on 11 workloads.

### 2026-10-07 — ingest method:bulkboost (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:bulkboost (2610.07497), method:bulkboost, recipe:bulkboost (`code_status: none`).
- Status active (`sota_for: []`). Two-band MP-calibrated spectral reweight; 0.073–0.147% loss reduction vs Muon flat.

### 2026-10-07 — ingest method:drmoet (active on task:pretrain-moe-frontier; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:drmoet (2610.07207), method:drmoet, recipe:drmoet (`code_status: released`; MAPS-research/DRMoET). NeurIPS 2026.
- Status active (`sota_for: []`). FLAME-MoE 10.3B seven-task avg 0.6767 vs 0.6625.

### 2026-10-07 — ingest method:hierarchical-moe-routing-control (active on task:math-code-rl-moe; does not supersede method:sapo / method:esrl / method:rpb)
- Added paper:hierarchical-moe-routing-control (2610.07332), method:hierarchical-moe-routing-control, recipe:hierarchical-moe-routing-control (`code_status: none`).
- Status active (`sota_for: []`). >10-point AppWorld / AutomationBench. Mention on outcome-only agent RL.

### 2026-10-07 — ingest method:fc-swe (active on task:swe-agent-category-expert-rl; does not supersede method:category-aware-swe-experts)
- Added paper:fc-swe (2610.07898), method:fc-swe, recipe:fc-swe (`code_status: none`).
- Status active (`sota_for: []`). SWE-bench Verified 500 Resolved@1 41.7 vs GRPO 38.9.

### 2026-10-07 — ingest method:rgpo (active on task:math-code-rl-dense; does not supersede method:cispo) + claim note paper:ga-grpo
- Added paper:rgpo (2610.07342), method:rgpo, recipe:rgpo (`code_status: released`; VietHoang1512/rgpo). NeurIPS 2026.
- Added paper:ga-grpo (2610.06861) theory/evidence on RGPO / MInTRL / CISPO. λ*=σ0²/(σ0²+Rmax²δ²T). No new method.
- Status active (`sota_for: []`). Adaptive GT rationale scaffolding.

### 2026-10-07 — ingest method:privileged-context-drift (niche on task:privileged-teacher-opsd; does not supersede method:vista)
- Added paper:privileged-context-drift (2610.07842), method:privileged-context-drift, recipe:privileged-context-drift (`code_status: none`).
- Status niche (`sota_for: []`). Content drives KL 5.1× more than source.

### 2026-10-07 — claim note paper:opd-safety-backdoor (no new method)
- Added paper:opd-safety-backdoor (2610.07654) on method:opd. 3% poison → up to 70% ASR. Warning on OPD used for safety alignment. Does not retarget OPD.

### 2026-10-07 — ingest method:a2d (active first hop on task:diffusion-lm-ar-delta-recycle; does not supersede method:diffusion-opsd / method:canvasanneal)
- Added paper:a2d (2610.08108), method:a2d, recipe:a2d (`code_status: none`). Reverse redirect from posttrain-diffusion.
- Status active (`sota_for: []`). AR delta on converted dLLM approaches direct diffusion PT.

### 2026-10-07 — ingest method:maskerade (active first hop on task:dense-to-moe-upcycling; does not supersede method:deepseek-v4)
- Added paper:maskerade (2610.07809), method:maskerade, recipe:maskerade (`code_status: released`; Ming-K9/MASKerade). Reverse redirect from pretrain-moe-frontier.
- Status active (`sota_for: []`). Four 2:4 mask experts, top-2, frozen FFN.

### 2026-10-07 — ingest method:dart-es (active on task:passk-reasoning-coverage; does not supersede method:es-reasoning / method:cispo)
- Added paper:dart-es (2610.06993), method:dart-es, recipe:dart-es (`code_status: released`; szs777/DART-ES-Code).
- Status active (`sota_for: []`). GSM8K 73.53 vs ES 72.07 vs GRPO 73.26.

### 2026-10-06 — weekday SOTA sweep (ORCA, ExpertMuon-Compass, Clean, DGA-Muon, Repeated-Token Worth, Repetition-Count Selection, Looped Models Done Right, ResOPD, Flash-OPD, Prep-OPD, DiffGate, OPPD, E2-OPSD, OG-OPSD, off-policy grafting, ThunderSyncRL, LoGRA, ExPPO, MEND, OnePO)
- Twenty active plug-ins, one new dual-active task (`task:data-constrained-pretrain`), and one claim-note paper (`paper:rethink-mopd`). No current_sota retarget of muon2 / CISPO / VISTA / OPD / Open-MOPD / SAO / Miles / ACLArena / Self-OPD / OLMo-3 / RLT / SMELT.
- Window: 2026-10-06 Librarian weekday sweep after PR 38; watermark was 2610.03702. New arXiv 2610.06116, 2610.04140, 2610.04204, 2610.06578, 2610.05591, 2610.05126, 2610.06833, 2610.04882, 2610.06105, 2610.04950, 2610.04596, 2610.06804, 2610.05048, 2610.05070, 2610.04272, 2610.05872, 2610.05935, 2610.06647, 2610.04011, 2610.05954, 2610.05966.

### 2026-10-06 — claim note paper:rethink-mopd (no new method)
- Added paper:rethink-mopd (2610.04272) on method:open-mopd and siblings (sf-mopd / mopd-router / dn-mopd / pmopd / latent-mopd). Tuned SFT/Soft-KD ≈ MOPD after matching HPs; MOPD 14.8–23.1× SFT GPU-h. Announced GitHub apple-aiml-research/ml-rethink-mopd 404 as of 2026-10-06. Does not retarget Open-MOPD.

### 2026-10-06 — ingest method:onepo (active on task:instruct-sft-alignment; does not supersede method:olmo-3 / method:cispo)
- Added paper:onepo (2610.05966), method:onepo, recipe:onepo (`code_status: released`; `repo_url: https://github.com/FreedomIntelligence/HuatuoGPT-3`). Reverse redirect for SFT-free RL-only domain adaptation.
- Status active (`sota_for: []`). OnePO Adaptive Objective Evolution + Teacher Retirement; HuatuoGPT-3 27B.
- Evidence: HealthBench Total 67.2 / 20K, +2.7 vs SFT+RL / +7.4 vs pure RL; 27B 70.1 Total / 71.4 Professional (arXiv:2610.05966); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains instruct default; CISPO remains Pass@1.

### 2026-10-06 — ingest method:mend (active on task:posttrain-diffusion; does not supersede method:diffusion-opsd / method:self-opd)
- Added paper:mend (2610.05954), method:mend, recipe:mend (`code_status: none`; `repo_url: none found`). Reverse redirect for proximal velocity matching.
- Status active (`sota_for: []`). ~100 updates vs Flow-GRPO ~4k.
- Evidence: 5/6 evaluators at matched distance to base images; beats ReFL and DiffusionNFT under equal budget (arXiv:2610.05954); verified: true; evidence_level: preprint.
- Scope checks: DiffusionOPSD / Self-OPD remain diffusion post-train defaults.

### 2026-10-06 — ingest method:exppo (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:exppo (2610.04011), method:exppo, recipe:exppo (`code_status: released`; `repo_url: https://github.com/jinhangzhan/ExPPO`). Reverse redirect for surprisal+pass-rate advantage shaping.
- Status active (`sota_for: []`). Exploration-preserving advantage on an existing group reward.
- Evidence: abstract has no numeric table (arXiv:2610.04011); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1.

### 2026-10-06 — ingest method:logra (active on task:math-code-rl-dense / task:full-param-memory-efficient-pretrain; does not supersede method:cispo / method:scale)
- Added paper:logra (2610.06647), method:logra, recipe:logra (`code_status: none`; `repo_url: none found`). Reverse redirects for RL memory sketches.
- Status active (`sota_for: []`). Low-rank gradient sketches + predicted-KL step control.
- Evidence: up to 45.7% RL memory reduction; 27B 1100+ steps on 8 GPUs (arXiv:2610.06647); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SCALE remains full-param pretrain memory.

### 2026-10-06 — ingest method:thundersyncrl (active on task:agentic-async-rl; does not supersede method:sao / method:miles)
- Added paper:thundersyncrl (2610.05935), method:thundersyncrl, recipe:thundersyncrl (`code_status: none`; `repo_url: none found`). Reverse redirects from agentic-async-rl and frontier-rl-posttrain-stack.
- Status active (`sota_for: []`). Lossless no-staleness overlap of gradient with GRPO/OPD rollout.
- Evidence: 1.9× vs sync; +2.47pp vs async (arXiv:2610.05935); verified: true; evidence_level: preprint.
- Scope checks: SAO remains async stragglers; Miles remains the production engine.

### 2026-10-06 — ingest method:off-policy-grafting (active on task:agent-continual-learning; does not supersede method:aclarena)
- Added paper:off-policy-grafting (2610.05872), method:off-policy-grafting, recipe:off-policy-grafting (`code_status: none`; `repo_url: none found`). Reverse redirect against OPSD for continual learning.
- Status active (`sota_for: []`). Donor-checkpoint SFT then scaled merge. Distinct from method:graft (all-fail salvage).
- Evidence: off-policy merging beats on-policy self-distillation for CL in the paper (arXiv:2610.05872); verified: true; evidence_level: preprint.
- Scope checks: ACLArena remains the agent continual-learning first hop.

### 2026-10-06 — ingest method:e2-opsd / method:og-opsd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:u-opsd)
- Added paper:e2-opsd (2610.05048), method:e2-opsd, recipe:e2-opsd (`code_status: none`). Entropy-overshoot fix; up to +4.3 mean@16 vs OPSD.
- Added paper:og-opsd (2610.05070), method:og-opsd, recipe:og-opsd (`code_status: none`). Outcome-guided FKL/RKL + entropy prefix cutoff; improves vanilla OPSD on Qwen3 1.7B/4B/8B and Qwen3-VL-2B (no numeric table in abstract).
- Linked from method:opsd-collapse-review. Status active (`sota_for: []`).
- Scope checks: VISTA remains privileged-OPSD first hop.

### 2026-10-06 — ingest method:oppd (active on task:student-distillation; does not supersede method:opd / method:cispo)
- Added paper:oppd (2610.06804), method:oppd, recipe:oppd (`code_status: released`; `repo_url: https://github.com/ArminAzizi98/OPPD`).
- Status active (`sota_for: []`). SMC against a frozen teacher's sequence-level power distribution.
- Evidence: MATH500 +23.0 / GSM8K +27.3 vs untrained; +3.8 / +4.0 / +5.4 vs GRPO on MATH500 / GSM8K / AIME (arXiv:2610.06804); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:diffgate (active on task:student-distillation; does not supersede method:opd / method:opd-then-rlvr / method:cispo)
- Added paper:diffgate (2610.04596), method:diffgate, recipe:diffgate (`code_status: none`; verl cited, no dedicated repo).
- Status active (`sota_for: []`). Difficulty-gated OPD+GRPO on failed trajectories.
- Evidence: Qwen3-0.6B/1.7B code avg@8 +1.7/+1.8, pass@8 +1.6/+5.7 vs GRPO (arXiv:2610.04596); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:prep-opd (active on task:student-distillation; does not supersede method:opd / method:scout)
- Added paper:prep-opd (2610.04950), method:prep-opd, recipe:prep-opd (`code_status: none`). Prepare-then-freeze vs SCOUT interleaved teacher RL.
- Status active (`sota_for: []`).
- Evidence: 4B→1.7B +8.28 vs OPD, +2.30 vs Relay-OPD (arXiv:2610.04950); verified: true; evidence_level: preprint. Relay-OPD is a paper baseline, not a library method.

### 2026-10-06 — ingest method:flash-opd (active on task:student-distillation; does not supersede method:opd)
- Added paper:flash-opd (2610.06105), method:flash-opd, recipe:flash-opd (`code_status: released`; `repo_url: https://github.com/Onedean/Flash-OPD`).
- Status active (`sota_for: []`). First-passage adaptive rollout horizon.
- Evidence: 2.2×–7.5× vs OPD (arXiv:2610.06105); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:resopd (active on task:student-distillation; does not supersede method:opd / method:sparse-opd-supervision)
- Added paper:resopd (2610.04882), method:resopd, recipe:resopd (`code_status: announced`; InternLM/ResOPD HTTP 404 as of 2026-10-06).
- Status active (`sota_for: []`). Tail residualization for sparse reverse-KL OPD.
- Evidence: unbiased full-vocab reverse KL and substantial variance reduction (abstract; no numeric table) (arXiv:2610.04882); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:looped-models-done-right (active on task:recurrent-encoder-decoder-lm; does not supersede method:recurrent-looped-transformer / method:smelt)
- Added paper:looped-models-done-right (2610.06833), method:looped-models-done-right, recipe:looped-models-done-right (`code_status: released`; `repo_url: https://github.com/ifm-ai/xllm-loop`). Reverse redirect from compute-matched-moe-looped-pretrain.
- Status active (`sota_for: []`). Huginn-style fixed-point loops; learned depth prior + terminal KV sharing.
- Evidence: 1.6B 3× smaller KV matches fixed-depth full-cache average; prefill distill up to 1.79×; RL saved-state grads 2× (arXiv:2610.06833); verified: true; evidence_level: preprint.
- Scope checks: RLT remains the CED experimental hop (no measurements); SMELT remains MoE looping.

### 2026-10-06 — ingest task:data-constrained-pretrain (dual-active method:repeated-token-worth + method:repetition-count-selection; does not supersede method:olmo-3 / method:moe-data-repetition)
- Added paper:repeated-token-worth (2610.05591) and paper:repetition-count-selection (2610.05126) with methods/recipes (`code_status: none`). New task current_sota lists both; method `sota_for` stays empty.
- Evidence: second epoch nearly as valuable as fresh; ~15 epochs at 127M to ~4 at 2B; consecutive shard replay up to +0.46 bits/byte (2610.05591). 520M Proof-Pile-2 r=8 beats r=16 with fewer tokens (2610.05126); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains the open mix; MoE data-repetition remains the sparsity gotcha.

### 2026-10-06 — ingest method:dga-muon (active on task:llm-pretraining-optimization; does not supersede method:muon2 / method:sf-normuon)
- Added paper:dga-muon (2610.06578), method:dga-muon, recipe:dga-muon (`code_status: none`).
- Status active (`sota_for: []`). Decoupled geometry-aligned scaling; NorMuon adaptivity is mostly orthogonalization geometry.
- Evidence: empirical superiority over NorMuon (abstract; no numeric table) (arXiv:2610.06578); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:clean (active on task:llm-pretraining-optimization; does not supersede method:soap / method:soap-muon-scale / method:muon2)
- Added paper:clean (2610.04204), method:clean, recipe:clean (`code_status: none`). Nyström SOAP + Q-Clean.
- Status active (`sota_for: []`).
- Evidence: Q-Clean >50% optimizer memory vs Muon on LLaMA-1.3B; Clean 26% faster wall-clock to AdamW final quality; 13B on one 80GB GPU (arXiv:2610.04204); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:expertmuon-compass (active on task:llm-pretraining-optimization / task:pretrain-moe-frontier; does not supersede method:muon2 / method:muonclip-kimi-k2)
- Added paper:expertmuon-compass (2610.04140), method:expertmuon-compass, recipe:expertmuon-compass (`code_status: none`).
- Status active (`sota_for: []`). Per-expert Muon step multipliers from update–gradient alignment.
- Evidence: FineWeb-Edu; strongest on blocked multilingual (arXiv:2610.04140); verified: true; evidence_level: preprint.

### 2026-10-06 — ingest method:orca (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:orca (2610.06116), method:orca, recipe:orca (`code_status: none`). Temporary soft-orthogonality then remove.
- Status active (`sota_for: []`).
- Evidence: LLaMA / Qwen3 / fine-grained MoE 130M–8B; lower final val loss than Muon; Muon-relative drop matches or exceeds Muon's vs Adam (arXiv:2610.06116); verified: true; evidence_level: preprint. Do not invent 0.02–0.04 or 60k-vs-100k.

### 2026-10-05 — weekday SOTA sweep (MuonIO, SF-MOPD, LMOPD, Latent-MOPD, RP-OPD, Air-OPD, RC-OPD, AdaStep, FTW, SCAD, Mesh Learning, TACM, LESSER, OPSFT, MetaRubric)
- Fifteen active plug-ins plus four claim-note papers. No current_sota retarget of muon2 / CISPO / VISTA / OPD / Open-MOPD / CANOPY / SLCA-GRPO / CorrGRPO / DARA / RLM / SAO / Miles.
- Window: 2026-10-05 Librarian weekday sweep after PR 37; watermark was 2610.02199 from PR 36. New arXiv 2610.02705, 2610.02324, 2610.02359, 2610.02381, 2610.02781, 2610.02700, 2610.03515, 2610.03223, 2610.03361, 2610.03372, 2610.02835, 2610.02404, 2610.03702, 2609.36659, 2610.02824. Claim notes 2610.03185, 2609.35259, 2610.03529, 2610.02911.

### 2026-10-05 — claim notes paper:opd-gains-collapse / paper:on-policy-or-off-policy / paper:divergence-entropy-distillation / paper:probe-the-harness (no new methods)
- Added paper:opd-gains-collapse (2610.03185) on method:opd. Teacher as implicit reward; masking 4B→Base avg 10.16→13.24. Code HancCui/opd_hacking (`code_status: released`).
- Added paper:on-policy-or-off-policy (2609.35259) on method:opd. KL direction dominates rollout on-policyness. No code.
- Added paper:divergence-entropy-distillation (2610.03529) on method:opd. Forward KL inflates student entropy; reverse KL deflates. Code NicolasZucchet/Entropy-in-distillation (`code_status: released`).
- Added paper:probe-the-harness (2610.02911) on method:cis-rl / method:carm / method:sao. TIS vs SAN ranking reversals in verl. SAN is not a library method. No code.

### 2026-10-05 — ingest method:metarubric (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:draco)
- Added paper:metarubric (2610.02824), method:metarubric, recipe:metarubric (`code_status: released`; `repo_url: https://github.com/metarubric/metarubric`). Reverse redirect for learned rubric rewards.
- Status active (`sota_for: []`). Learns rubric rewards against Vacuous Credit.
- Evidence: Qwen3-4B PubMedQA 78.40 vs GRPO 72.40 (+6.00); Gemma-e2b 72.00 vs 51.60; HealthBench-Hard 4B 13.02 vs 10.56 (arXiv:2610.02824); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains checker coverage; DRACO remains outcome-blind dynamic rubrics.

### 2026-10-05 — ingest method:opsft (active on task:instruct-sft-alignment; does not supersede method:olmo-3 / method:cispo)
- Added paper:opsft (2609.36659), method:opsft, recipe:opsft (`code_status: released`; `repo_url: https://github.com/ssfgunner/OPSFT`). Reverse redirects from instruct-sft-alignment and math-code-rl-dense.
- Status active (`sota_for: []`). Projects SFT onto the on-policy parameter-update direction.
- Evidence: Qwen3-4B DeepMath mean 40.11 vs GRPO 38.96 vs SFT 34.22 (6.4h vs 16.5h); Qwen3-8B 41.67 vs GRPO 40.31 vs SFT 38.41; post-GRPO continue 38.96→41.36 vs SFT drop 36.25 (arXiv:2609.36659); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains instruct default; CISPO remains Pass@1.

### 2026-10-05 — ingest method:lesser (active on task:training-data-attribution; does not supersede method:magic)
- Added paper:lesser (2610.03702), method:lesser, recipe:lesser (`code_status: none`; `repo_url: none found`). Reverse redirect for output-layer-gradient SFT/RL selection.
- Status active (`sota_for: []`). Cheaper gradient features for selection wrappers.
- Evidence: 9.7× SFT / 3.0× RL vs 4-ckpt LESS on Llama-2-7B; Jaccard 0.53 vs random 0.075; same final RL acc as GradAlign (arXiv:2610.03702); verified: true; evidence_level: preprint.
- Scope checks: MAGIC remains peak-LDS first hop.

### 2026-10-05 — ingest method:tacm (active on task:long-context-prompt-offload; does not supersede method:rlm)
- Added paper:tacm (2610.02404), method:tacm, recipe:tacm (`code_status: released`; `repo_url: https://github.com/brycesandlund/infinite-context`). Reverse redirect for trained self-call + range-read harness.
- Status active (`sota_for: []`). 8K context matching a 1M baseline on OOLONG-synth at some lengths.
- Evidence: Qwen3.6-35B-A3B 8K vs GPT-5.4 1M OOLONG-synth 40K 0.535 vs 0.600, 80K 0.561 vs 0.539, 160K 0.464 vs 0.556, 320K 0.470 vs 0.479 (arXiv:2610.02404); verified: true; evidence_level: preprint.
- Scope checks: RLM remains dumped-prompt first hop.

### 2026-10-05 — ingest method:mesh-learning (active on task:math-code-rl-dense; does not supersede method:cispo)
- Added paper:mesh-learning (2610.02835), method:mesh-learning, recipe:mesh-learning (`code_status: released`; `repo_url: https://github.com/Ayanami-0123/Open-Mesh-Learning`). Reverse redirect for catastrophic strategy collapse.
- Status active (`sota_for: []`). Coach Prompting + strategy-balancing regularization.
- Evidence: Qwen3-4B m=4 AIME26 56.7 vs GRPO 43.3; Qwen2.5-7B m=4 AIME26 13.3 vs GRPO 9.2 (arXiv:2610.02835); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1.

### 2026-10-05 — ingest method:scad (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:pivotopd)
- Added paper:scad (2610.03372), method:scad, recipe:scad (`code_status: none`; `repo_url: none found`). Reverse redirect for structured planning/subtask credit.
- Status active (`sota_for: []`). Local-context distillation for long-horizon agents.
- Evidence: Qwen3-4B text Avg 46.10 vs ATOD 41.62 / HiPER 41.49 / FoldGRPO 39.60 (+4.48); multimodal +4.19 (arXiv:2610.03372); verified: true; evidence_level: preprint. ATOD/HiPER are paper baselines, not library methods.
- Scope checks: CANOPY remains checker coverage; PivotOPD remains pivotal-mistake OPD.

### 2026-10-05 — ingest method:ftw (active on task:agentic-async-rl; does not supersede method:sao)
- Added paper:ftw (2610.03361), method:ftw, recipe:ftw (`code_status: none`; `repo_url: none found`). Reverse redirect for CEM-style critic-free RFT from replay.
- Status active (`sota_for: []`). NeurIPS 2026. Use when group rollouts are impractical.
- Evidence: Search-R1 Qwen2.5-3B-Instruct FTW-K1-C4 35.46±0.15 vs GRPO 33.6 vs PPO 32.5; Sokoban is curves only (arXiv:2610.03361); verified: true; evidence_level: peer-reviewed.
- Scope checks: SAO remains async straggler replay.

### 2026-10-05 — ingest method:adastep (active on task:tool-agent-segment-credit; does not supersede method:slca-grpo / method:canopy)
- Added paper:adastep (2610.03223), method:adastep, recipe:adastep (`code_status: none`; `repo_url: none found`). Reverse redirects from tool-agent-segment-credit and outcome-only-long-horizon-agent-rl.
- Status active (`sota_for: []`). Per-state shrinkage of step-level advantage.
- Evidence: Qwen3-4B 93.01/86.58/88.76/80.27/48.70 vs GiGPO 88.02/83.07/87.34/78.28/46.67; Qwen3-1.7B Δ vs GiGPO +2.60/+1.73/+0.75/+0.66/+9.36 (arXiv:2610.03223); verified: true; evidence_level: preprint. GiGPO is a paper baseline, not a library method.
- Scope checks: SLCA-GRPO remains segment-credit first hop; CANOPY remains checker coverage.

### 2026-10-05 — ingest method:rc-opd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:oasis)
- Added paper:rc-opd (2610.03515), method:rc-opd, recipe:rc-opd (`code_status: released`; `repo_url: https://github.com/Starrylay/RC-OPD`). Reverse redirect for root-cause-guided OPD.
- Status active (`sota_for: []`). Diagnoses the student's own failed reasoning then differentiates prefix/error distillation.
- Evidence: Table 1 Avg@4 Qwen3-1.7B/4B/8B 44.17/66.11/66.94 vs OPSD 40.28/62.50/63.33; 8B AIME25 76.67 vs OPSD 64.17 (arXiv:2610.03515); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-OPSD SOTA (64.8→66.9 bake-off unchanged).

### 2026-10-05 — ingest method:air-opd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:oasis)
- Added paper:air-opd (2610.02700), method:air-opd, recipe:air-opd (`code_status: none`; `repo_url: none found`). Reverse redirect for adaptive iterative error-to-repair OPSD.
- Status active (`sota_for: []`). Iterates error-specific repair guidance.
- Evidence: Qwen3-4B Math Avg External-G 66.7 / Self-G 65.8 vs OPSD 63.1 / GRPO 62.3 / base 61.2; 8B 67.4 / 66.9 vs OPSD 64.7 (arXiv:2610.02700); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains first hop; OASIS remains scale-collapse scaffolds.

### 2026-10-05 — ingest method:rp-opd (active on task:student-distillation; does not supersede method:opd / method:opd-then-rlvr)
- Added paper:rp-opd (2610.02781), method:rp-opd, recipe:rp-opd (`code_status: none`; `repo_url: none found`). Reverse redirects from student-distillation; do_not_use_for on opd-then-rlvr.
- Status active (`sota_for: []`). NeurIPS 2026. Rubric-privileged OPD warm start then rubric RL.
- Evidence: Qwen2.5-7B HealthBench/ResearchQA/RubricHub 0.673/0.797/0.829 vs SFT+RL 0.607/0.721/0.815; 3B 0.632/0.776/0.735; Llama-3.1-8B HealthBench 0.634 vs 0.526 (arXiv:2610.02781); verified: true; evidence_level: peer-reviewed.
- Scope checks: OPD remains matching distillation; OPD-then-RLVR remains verifiable OPD then labeled RLVR.

### 2026-10-05 — ingest method:latent-mopd (active on task:student-distillation; does not supersede method:open-mopd)
- Added paper:latent-mopd (2610.02381), method:latent-mopd, recipe:latent-mopd (`code_status: released`; `repo_url: https://github.com/fangzy96/Latent-MOPD`). Reverse redirect for hidden-state multi-teacher OPD.
- Status active (`sota_for: []`). Representation-level specialist matching.
- Evidence: same-family 1.5B last-3 Norm 1.05 vs token-only 0.90 vs uniform 0.79; GYM 52.4 / BBH 66.3 / AIME24 50.8 vs 51.8/65.4/46.0; cross-family last-1 Linear Norm 0.26 vs 0.16 (arXiv:2610.02381); verified: true; evidence_level: preprint.
- Scope checks: Open-MOPD remains token-share / gap-aware budget.

### 2026-10-05 — ingest method:lmopd (active on task:student-distillation; does not supersede method:open-mopd / method:corrgrpo / method:dara)
- Added paper:lmopd (2610.02359), method:lmopd, recipe:lmopd (`code_status: none`; `repo_url: none found`). Reverse redirects from student-distillation and multi-reward-rlvr.
- Status active (`sota_for: []`). Lexicographic priority among reward-specialist teachers.
- Evidence: 30B-A3B two-expert retained-gain pass@1 102.9 / RQ 103.3 / Conc 46.9 avg 84.4 vs Rewarded Soup 67.1 / GDPO(25,1,1) 18.9; four-expert avg 39.6 vs gated RLVR 34.4; raw pass@1 0.7450 vs base 0.7109 (arXiv:2610.02359); verified: true; evidence_level: preprint. GDPO is prior art, not a library method.
- Scope checks: Open-MOPD remains multi-teacher default; CorrGRPO/DARA remain scalarized multi-reward RL.

### 2026-10-05 — ingest method:sf-mopd (active on task:student-distillation; does not supersede method:open-mopd)
- Added paper:sf-mopd (2610.02324), method:sf-mopd, recipe:sf-mopd (`code_status: none`; `repo_url: none found`). Reverse redirect for slow/fast EMA student coupling.
- Status active (`sota_for: []`). Capability preservation in multi-teacher OPD.
- Evidence: Qwen3-VL All Avg 8B 67.7 vs MOPD 65.5 vs Open-MOPD 64.2; 4B 64.8 vs 63.6; 2B 54.2 vs 53.3 (arXiv:2610.02324); verified: true; evidence_level: preprint. Paper Open-MOPD 64.2 is not the library 83.4% bake-off.
- Scope checks: Open-MOPD remains token-share / gap-aware budget.

### 2026-10-05 — ingest method:muonio (active on task:llm-pretraining-optimization; does not supersede method:muon2)
- Added paper:muonio (2610.02705), method:muonio, recipe:muonio (`code_status: none`; `repo_url: none found`). Reverse redirects from llm-pretraining-optimization and pretrain-dense-7b.
- Status active (`sota_for: []`). Muon-style \(1\to 2\) embeddings and \(2\to\infty\) LM head instead of AdamW.
- Evidence: C4 val PPL 60M/130M/1B 28.366/23.617/14.374 vs Muon Tuned 28.502/24.238/14.527; Polar Express IO 1B 14.160 vs PE Tuned 14.361; I/O FLOPs 7Vd+3V vs AdamW 13Vd; state Vd vs 2Vd (arXiv:2610.02705); verified: true; evidence_level: preprint.
- Scope checks: Muon2 remains the hidden-layer / 7B default.

### 2026-10-03 — ingest method:sampling-sft (active on task:math-code-rl-dense; does not supersede method:cispo / method:vista)
- Added paper:sampling-sft (2610.02140), method:sampling-sft, recipe:sampling-sft (`code_status: none`; `repo_url: none found`; project https://aakaran.github.io/finetuning_with_sampling/). Reverse redirects from math-code-rl-dense and privileged-teacher-opsd.
- Status active (`sota_for: []`). MCMC / Metropolis–Hastings projection sampling rewrites off-policy expert traces toward the base model, then ordinary SFT. Vanilla SFT still loses to GRPO; do not headline “SFT beats GRPO.” Sampling SFT then GRPO is best in the math table.
- Evidence: Qwen2.5-3B MATH(3,4,5) 0.495 vs GRPO 0.457 vs UFT 0.470 vs vanilla SFT 0.243 vs base 0.315; MATH500 0.582 vs GRPO 0.313; Sampling SFT+RL 0.545 / 0.652. Chemistry 0.660 vs OPSD 0.618. Medical 0.458 vs OPSD 0.466, prior avg 0.516 vs 0.501 (arXiv:2610.02140); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; VISTA remains privileged-teacher OPSD; OPD remains matching distillation.

### 2026-10-03 — ingest task:zero-natural-data-self-play-pretrain (experimental first hop method:self-play-pretraining; does not supersede method:j-zero)
- Added task:zero-natural-data-self-play-pretrain, paper:self-play-pretraining (2609.30063), method:self-play-pretraining (`status: experimental`, `sota_for: []`, listed in the new task `current_sota`), recipe:self-play-pretraining (`code_status: released`; `repo_url: https://github.com/nourya-aliz/self_play_pretraining`). Reverse redirects from data-free-self-evolution, open-data-recipe, llm-pretraining-optimization, pretrain-dense-7b, teacher-free-on-policy-self-adaptation.
- Title confirmed from arXiv: “Self-Play Pretraining with Zero Data.” This is pretraining from random init with zero natural text (UTM generator + byte NTP), not a J-Zero post-train sibling, so it gets its own task rather than an active plug-in on task:data-free-self-evolution. J-Zero `current_sota` is unchanged.
- Evidence: DCLM exponent b=0.123 vs literature 0.048–0.099; CIFAR-10 image bytes b=0.145; Fibonacci discovery round 512 vs E[first]>53,000; 24.4M warm start ESC-50 320M vs 496M, CIFAR-10 421M vs 588M (arXiv:2609.30063); verified: true; evidence_level: preprint. Scale <25M.
- Scope checks: J-Zero remains post-train Challenger–Solver–Judge; SYNTH remains Wikipedia-seeded synthetic pretrain; OLMo-3 remains the open mix; OPSA remains unlabeled-prompt self-adaptation.

### 2026-10-03 — ingest task:synthetic-single-stage-pretrain (first hop method:synth; does not supersede method:olmo-3 / method:muon2)
- Added task:synthetic-single-stage-pretrain, paper:synth (2609.37891), method:synth (`status: sota`, `sota_for: [task:synthetic-single-stage-pretrain]`), recipe:synth (`code_status: partial`; dataset `PleIAs/SYNTH` / `SYNTH-Initiative/SYNTH`; HF `PleIAs/Baguettotron` is the 321M/200B card, not the 594M FActScore run). Reverse redirects from open-data-recipe, llm-pretraining-optimization, pretrain-dense-7b.
- Seed-grounded synthetic pretraining (58,698 Wikipedia articles + Wikibooks), not self-play and not a Dolma-3 replacement. No separate SFT/RL. Distinct from `method:hive-synth`.
- Evidence: Baguettotron-600M (594M, 158B tokens) Table 1 S/(S+C) 79.3%±2.1 / macro 41.7%±2.2 vs Qwen3-0.6B 65.7%/31.6% (~36T) and Phi-4-mini 77.4%/29.5% (~5T); iso-compute +16–17 MC / +11–14 open-ended vs FineWiki/FinePDFs-Edu; TeleQnA 41.6→56.7, 3GPP FactScore 21.5→38.8; held-out abstain 67% vs 20% in-seed (arXiv:2609.37891); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains the open mix; Muon2 remains the ~7B optimizer; Puro-2B remains consumer-GPU open-mix ~2B. Locked method files were not edited.

### 2026-10-02 — weekday SOTA sweep (CorrGRPO, DARA, TACO, Where-OPD, ActiveSaddler, CARM, N-OPSD)
- Seven active plug-ins plus new `task:multi-reward-rlvr` (dual-active CorrGRPO + DARA). No current_sota retarget of CISPO / VISTA / muon2 / omp2-harness / SCALE / Miles / SAPO / ES-reasoning / NeoHorse-1 / Vision-RL2.
- Window: 2026-10-02 Librarian weekday sweep after PR 35 watermark 2609.40285. New arXiv 2609.36820, 2610.00574, 2610.02199, 2610.02117, 2610.00906, 2610.02039, 2609.39687. Optional claim notes: Sharpening Tax 2610.01509, OPD same-family scaling 2609.32722.

### 2026-10-02 — ingest task:multi-reward-rlvr (dual-active method:corrgrpo + method:dara; does not supersede method:cispo)
- Added task:multi-reward-rlvr with current_sota CorrGRPO + DARA (methods stay `status: active`, `sota_for: []`). Reverse redirects from math-code-rl-dense / math-code-rl-moe.
- No head-to-head. CorrGRPO Pearson-normalizes summed GRPO covariances; DARA inverse-sqrt density on GDPO-style advantages. GDPO is prior art, not a library node.

### 2026-10-02 — ingest method:corrgrpo (active on task:multi-reward-rlvr; does not supersede method:cispo)
- Added paper:corrgrpo (2609.36820), method:corrgrpo, recipe:corrgrpo (`code_status: released`; `repo_url: https://github.com/HKUST-KnowComp/CorrGRPO`). Reverse redirect for Pearson-normalize multi-reward GRPO covariances.
- Status active (`sota_for: []`). Dual-active first hop with DARA. Plug-in mention on math-code-rl-dense / GRPO family.
- Evidence: Qwen2.5-Coder-7B-Instruct coding Avg Pass@1 51.49 vs GRPO 47.28 / GDPO 48.88 / base 47.64 (arXiv:2609.36820); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; DARA remains density-energy; SAPO remains MoE/VL; CARM remains off-policy sequence masking.

### 2026-10-02 — ingest method:dara (active on task:multi-reward-rlvr; does not supersede method:cispo / method:corrgrpo)
- Added paper:dara (2610.00574), method:dara, recipe:dara (`code_status: released`; `repo_url: https://github.com/zhaihaotian/DARA`). Reverse redirect for density-aware multi-reward aggregation.
- Status active (`sota_for: []`). Dual-active first hop with CorrGRPO. Default DARA-Asym.
- Evidence: up to 26% fewer steps to high tool-format compliance / 65% fewer steps to near-saturated math length compliance vs GDPO (arXiv:2610.00574); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; CorrGRPO remains Pearson scale; GDPO is not a library method.

### 2026-10-02 — ingest method:taco (active on task:full-param-memory-efficient-pretrain; does not supersede method:scale / method:muon2)
- Added paper:taco (2610.02199), method:taco, recipe:taco (`code_status: released`; `repo_url: https://github.com/Jichao2357/TACO_optimizer`). Reverse redirects from full-param-memory-efficient-pretrain and llm-pretraining-optimization for ternary column-wise one-sparse FT.
- Status active (`sota_for: []`). FT-axis plug-in beside SCALE. Not a pretrain-from-scratch recipe.
- Evidence: OPT-13B SST-2 94.22% at 27.5 GB peak / 0.16 GB optimizer state vs AdamW8bit 80.6 / 27.7 GB (174× state, 2.9× peak); OPT-30B / Qwen3-32B fit on one 80 GB H100 (arXiv:2610.02199); verified: true; evidence_level: preprint.
- Scope checks: SCALE remains the subspace first hop; Muon2 remains the ~7B pretrain optimizer; Quartet-II remains FP4 hardware; lr-matters-lora remains quality LoRA.

### 2026-10-02 — ingest method:where-opd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:oasis / method:vision-rl2)
- Added paper:where-opd (2610.02117), method:where-opd, recipe:where-opd (`code_status: released`; `repo_url: https://github.com/sirkosophia/Where-OPD`). Reverse redirects from privileged-teacher-opsd and mllm-finegrained-perception-rl for textual spatial-hint MLLM OPSD.
- Status active (`sota_for: []`). Teacher gets object/coord hints from synthetic scenes; student sees the same image.
- Evidence: Qwen3.5-4B real-world avg +3.23; ChartQA / EvoChart +7.20 / +10.11 (arXiv:2610.02117); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains text-math privileged-OPSD SOTA; Vision-RL2 remains region-level RL; OASIS remains scale-collapse scaffolds; u-OPSD remains no-GT.

### 2026-10-02 — ingest method:activesaddler (active on task:agent-harness-runtime; does not supersede method:omp2-harness / method:rrsi / method:aide2)
- Added paper:activesaddler (2610.00906), method:activesaddler, recipe:activesaddler (`code_status: released`; `repo_url: https://github.com/microsoft/AutoSaddler`). Reverse redirects from agent-harness-runtime and agentic-rsi-routing-posttrain for harness curriculum as a non-stationary bandit.
- Status active (`sota_for: []`). Curriculum dimension; harness-update operator unchanged.
- Evidence: GAIA2 +4.4 pp / Terminal-Bench 2.0 +7.5 pp vs the same optimizer with a frozen scenario order (arXiv:2610.00906); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains the kernel; RRSI remains frozen-backbone RSI; AIDE2 remains recursive rewrite; Harness-Zero remains distill-into-weights; NeoHorse-1 remains routing-guided weight post-train.

### 2026-10-02 — ingest method:carm (active on task:frontier-rl-posttrain-stack; does not supersede method:cispo / method:cis-rl / method:miles)
- Added paper:carm (2610.02039), method:carm, recipe:carm (`code_status: none`; `repo_url: none found`). Reverse redirects from frontier-rl-posttrain-stack, math-code-rl-dense, and math-code-rl-moe for cancellation-aware off-policy sequence masking.
- Status active (`sota_for: []`). Averages absolute token log-ratios before the threshold. Token PPO/GRPO clipping unchanged.
- Evidence: math mean@16 up to +3.13 pp vs GeoMean; four-code pass@1 +2.88 pp vs strongest baseline (arXiv:2610.02039); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; CIS-RL remains per-token train–infer IS; Miles remains the engine; SAPO remains MoE/VL.

### 2026-10-02 — ingest method:n-opsd (active on task:privileged-teacher-opsd; does not supersede method:vista / method:oasis / method:dce-srcl)
- Added paper:n-opsd (2609.39687), method:n-opsd, recipe:n-opsd (`code_status: none`; `repo_url: none found`). Reverse redirect for neighborhood-expert privileged OPSD.
- Status active (`sota_for: []`). Offline greedy frozen perturbation pool; online MaxPeak + quantile routing.
- Evidence: Avg@12 +2.75 / +1.67 / +1.94 vs OPSD on Qwen3-1.7B/4B/8B, three independent runs (arXiv:2609.39687); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains first hop (64.8→66.9 bake-off unchanged); OASIS remains scaffolds; DCE+SRCL remains co-evolution; u-OPSD remains no-GT.

### 2026-10-02 — claim notes paper:sharpening-tax / paper:opd-same-family-scaling (no new methods)
- Added paper:sharpening-tax (2610.01509) on method:es-reasoning / method:cispo / task:passk-reasoning-coverage. Coverage diagnostic; PTGS is not a library method.
- Added paper:opd-same-family-scaling (2609.32722) on method:opd. Early useful-transfer linear in \(\sqrt{\mathrm{KL}}\); peak gold score saturates near student scale.

### 2026-10-01 — weekday SOTA sweep (SCOUT, PivotOPD, OASIS, LSD, HDL, RIDE, DuoOPD, ActFirst-OPD)
- Eight active plug-ins. No new task. No current_sota retarget of OPD / Open-MOPD / VISTA / CISPO / Miles / CANOPY / mini-SWE-agent / SAPO / VeriGate / u-OPSD / TrOPD / GRAFT / PMOPD.
- Window: 2026-10-01 Librarian weekday sweep after PR 34 watermark 2609.37868. New arXiv 2609.38360, 2609.40285, 2609.37915, 2609.38854, 2609.36864, 2609.36484, 2609.33711, 2609.36608. HDL 2609.36864 was SKIP on 2026-09-30 and is ingested here.

### 2026-10-01 — ingest method:scout (active on task:student-distillation; does not supersede method:opd / method:tropd)
- Added paper:scout (2609.38360), method:scout, recipe:scout (`code_status: none`; `repo_url: none found`). Reverse redirect for adapting the OPD teacher on student prefixes / off-policy teacher.
- Status active (`sota_for: []`). Keeps student reverse-KL OPD; periodically RL-adapts the teacher on student-generated prefixes. Complementary to TrOPD / SAKI student-side gating.
- Evidence: +1.2–2.6 math / +3.1 code (56.6→59.7) over frozen-teacher OPD (arXiv:2609.38360); verified: true; evidence_level: preprint.
- Scope checks: OPD remains frozen-teacher matching; TrOPD remains student-side trust-region; SAKI remains coupling-routed frozen-teacher modes; VISTA remains privileged-OPSD.

### 2026-10-01 — ingest method:pivotopd (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:opd)
- Added paper:pivotopd (2609.40285), method:pivotopd, recipe:pivotopd (`code_status: announced`; project https://research.nvidia.com/labs/lpr/pivotopd/). Reverse redirect for multi-turn agent OPD at pivotal early mistakes. Soft SWE-Bench Verified mention on task:software-engineering-agent-harness.
- Status active (`sota_for: []`). Reverse-KL prevent + forward-KL recovery at teacher-named pivotal turns.
- Evidence: strongest average on ALFWorld/WebShop/Search-QA; ALFWorld +5.5 vs strongest of 13 baselines (Qwen3-1.7B); +3.2 SWE-Bench Verified vs OPD +0.2 (arXiv:2609.40285); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld TGC; OPD remains matching; mini-SWE-agent remains the harness. SWE +3.2 is distill transfer, not a loop ranking.

### 2026-10-01 — ingest method:oasis (active on task:privileged-teacher-opsd; does not supersede method:vista / method:u-opsd)
- Added paper:oasis (2609.37915), method:oasis, recipe:oasis (`code_status: none`; `repo_url: none found`). Reverse redirect for privileged OPSD gains collapsing at scale / verified on-policy scaffolds.
- Status active (`sota_for: []`). Supervise shortest verified on-policy scaffolds; teacher context is another same-problem rollout (answer labels only).
- Evidence: vs base +3.2 to +3.8 at 1.7B/4B/8B while OPSD vs base collapses +3.05 / +1.98 / +0.14; OASIS vs OPSD +3.05 at 8B (arXiv:2609.37915); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-OPSD SOTA. Not a VISTA bake-off (64.8→66.9) retarget. u-OPSD remains unlabeled/no-GT.

### 2026-10-01 — ingest method:lsd (active on task:math-code-rl-dense; does not supersede method:cispo / method:miles)
- Added paper:lsd (2609.38854), method:lsd, recipe:lsd (`code_status: none`; `repo_url: none found`). Reverse redirects from math-code-rl-dense and frontier-rl-posttrain-stack for length-scaling tax / EMA OPD on solved groups.
- Status active (`sota_for: []`). Route solved prompt groups to on-policy distillation against an EMA of the online policy; keep RLVR on unsolved groups.
- Evidence: single-turn LST 19.0%→−3.7%; agentic LST 31.4%→13.7% without sacrificing accuracy (arXiv:2609.38854); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; Miles remains the engine; When2Think remains offline Think/NoThink IDAC.

### 2026-10-01 — ingest method:hdl (active on task:math-code-rl-dense; does not supersede method:cispo / method:graft)
- Added paper:hdl (2609.36864), method:hdl, recipe:hdl (`code_status: none`; slime host `https://github.com/THUDM/slime`). Reverse redirects from math-code-rl-dense and outcome-only-long-horizon-agent-rl for hindsight-divergence prefix reuse.
- Status active (`sota_for: []`). Branch GRPO groups at hindsight logp-change positions; reuse prefixes, train suffixes. Previously SKIP on 2026-09-30.
- Evidence: up to 2.5× fewer tokens / 1.8× faster rollouts vs GRPO; agent gains including ScienceWorld up to +12.5 (arXiv:2609.36864); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; GRAFT remains peer all-fail salvage; CANOPY remains AppWorld TGC. GRPO stays retired as Pass@1.

### 2026-10-01 — ingest method:ride (active on task:student-distillation; does not supersede method:opd / method:s2d-opd)
- Added paper:ride (2609.36484), method:ride, recipe:ride (`code_status: released`; `repo_url: https://github.com/xixixixixxxx/RIDE`). Reverse redirect for distilling RL gains via representation residuals rather than logits.
- Status active (`sota_for: []`). Layerwise hidden-state residual extrapolation from frozen RL teacher vs pre-RL reference. Same-init required.
- Evidence: only RIDE's mean meets or exceeds the RL teacher across four base/RL-teacher pairs on AIME24/AIME25/AIMO Avg@16; output-space extrapolation stays below the teacher (arXiv:2609.36484); verified: true; evidence_level: preprint.
- Scope checks: OPD remains reverse-KL matching; S2D-OPD remains Direct-OPD JSD keep-mask; OPRD remains reverse distill.

### 2026-10-01 — ingest method:duoopd (active on task:student-distillation; does not supersede method:open-mopd / method:pmopd)
- Added paper:duoopd (2609.33711), method:duoopd, recipe:duoopd (`code_status: released`; `repo_url: https://github.com/YongYuanDeAo/DuoOPD`). Reverse redirect for multi-task OPD when the teacher can be wrong on some tasks.
- Status active (`sota_for: []`). One teacher; student outcome sets direction, joint teacher–student outcome sets support. Not Open-MOPD token-share.
- Evidence: Qwen3 / Llama mean macro +2.58 / +5.98 vs OPD (arXiv:2609.33711); verified: true; evidence_level: preprint.
- Scope checks: Open-MOPD remains multi-teacher default; PMOPD remains subspace cycling; OPD remains matching; OPDVR remains student-only ReLU gate.

### 2026-10-01 — ingest method:actfirst-opd (active on task:outcome-only-long-horizon-agent-rl; does not supersede method:canopy / method:opd)
- Added paper:actfirst-opd (2609.36608), method:actfirst-opd, recipe:actfirst-opd (`code_status: announced`; `repo_url: https://anonymous.4open.science/r/ActFirst-OPD`). Reverse redirect for act-first / reason-later multi-turn OPD.
- Status active (`sota_for: []`). Inverse-dynamics acting from reference next observations; async full think-then-act reverse-KL distill.
- Evidence: 2.3× / 1.8× / 4.9× wall-clock vs Vanilla OPD on ALFWorld / WebShop / ScienceWorld; 8/9 settings match or beat compared OPD baselines (arXiv:2609.36608); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld TGC; OPD remains matching; PivotOPD remains pivotal-mistake prevent/recover.

### 2026-09-30 — weekday SOTA sweep (DN-MOPD, CIS-RL, LSPD, EAPO, SAKI, GRAFT, PMOPD)
- MUST 1–4 plus in-scope 5–7. No new task. No current_sota retarget of OPD / Open-MOPD / VISTA / lr-matters-lora / CISPO / Miles / SAPO / VeriGate.
- Window: 2026-09-30 Librarian weekday sweep after PR 33 watermark 2609.31600. New arXiv 2609.35347, 2609.32444, 2609.35505, 2609.33781, 2609.36601, 2609.37868, 2609.34605. SKIP HDL 2609.36864, KL-free OPD 2609.33791.

### 2026-09-30 — ingest method:dn-mopd (active on task:student-distillation; does not supersede method:open-mopd / method:mopd-router)
- Added paper:dn-mopd (2609.35347), method:dn-mopd, recipe:dn-mopd (`code_status: released`; `repo_url: https://github.com/LiXin97/DN-MOPD`). Reverse redirect from student-distillation for domain-feedback-scale calibration of labeled MOPD advantages.
- Status active (`sota_for: []`). Keeps label routing; rescales each domain's OPD advantages by batch log-ratio std (clip 0.25–4). IF log-ratios 2.3–4.4× pooled; 94% of 4B combined gradient.
- Evidence: Qwen3.5 9B/4B/2B six-task Total 59.6/52.5/29.0 vs label MOPD 58.4/50.3/26.6; 16K +1.17–2.36, 8K +2.47–3.08 (arXiv:2609.35347); verified: true; evidence_level: preprint.
- Scope checks: Open-MOPD remains multi-teacher default; MOPD-Router remains unlabeled token routing; OPD remains single-teacher.

### 2026-09-30 — ingest method:cis-rl (active on task:math-code-rl-moe; does not supersede method:cispo / method:sapo / method:miles)
- Added paper:cis-rl (2609.32444), method:cis-rl, recipe:cis-rl (`code_status: released`; `repo_url: https://github.com/kzhao5/CIS-RL`). Reverse redirects from math-code-rl-dense / math-code-rl-moe / frontier-rl-posttrain-stack for MoE train–infer mismatch.
- Status active (`sota_for: []`). Truncates log-odds displacement, mapping to confidence-dependent cap \(k\le 1+\lambda(1-p)\). Slug `cis-rl` avoids CISPO collision.
- Evidence: Qwen1.5-MoE 5-bench avg 34.78 vs IcePop 34.18 / TIS 31.40; Qwen3-30B-A3B 69.88 vs IcePop 68.99 / GSPO 69.23 (arXiv:2609.32444); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL loss; Miles remains the engine; GAPO remains scarcity clip width.

### 2026-09-30 — ingest method:lspd (active on task:student-distillation; does not supersede method:opd)
- Added paper:lspd (2609.35505), method:lspd, recipe:lspd (`code_status: released`; `repo_url: https://github.com/UNCSciML/LSPD`). Reverse redirect for sample-efficient / off-policy OPD.
- Status active (`sota_for: []`). Reverse-KL OPD as KL-regularized RL; Huber quadratic student–teacher logp matching + entropy; LSPD-RB replay.
- Evidence: Avg@16 31.60 (+1.59 vs baselines); LSPD-RB 31.51 Avg@16 / 54.86 Pass@16 at ~10 steps / ~25% rollouts (arXiv:2609.35505); verified: true; evidence_level: preprint.
- Scope checks: OPD remains matching default; Open-MOPD remains multi-teacher; CISPO remains Pass@1.

### 2026-09-30 — ingest method:eapo (active on task:math-code-rl-dense; does not supersede method:cispo / method:cliff)
- Added paper:eapo (2609.33781), method:eapo, recipe:eapo (`code_status: released`; `repo_url: https://github.com/wgcyeo/EAPO`; project https://eapo-explore.github.io). Reverse redirect for asymmetric entropy×sign exploration credit.
- Status active (`sota_for: []`). Reinforce high-entropy tokens on success, penalize low-entropy on failure; no auxiliary model.
- Evidence: Qwen3-4B-Base mean Avg@32 31.0 (+5.6 vs EntropyAdv); 8B-Base 34.0 (+4.3 vs 80/20) (arXiv:2609.33781); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; Cliff remains first-mistake teacher credit; VeriGate remains PRM gating.

### 2026-09-30 — ingest method:saki (active on task:student-distillation; does not supersede method:opd / method:tropd / method:routeopd)
- Added paper:saki (2609.36601), method:saki, recipe:saki (`code_status: none`; `repo_url: none found`). Reverse redirect for maximal-coupling-routed teacher supervision.
- Status active (`sota_for: []`). TRB + maximal coupling: accept keeps reverse-KL, correction is teacher top-1 NLL. Meituan / KTH.
- Evidence: 1.7B Mean@8/Pass@8 29.0/47.5 vs TRB 27.9/44.6; 4.22× speculative throughput (arXiv:2609.36601); verified: true; evidence_level: preprint.
- Scope checks: OPD remains student-rollout matching; TrOPD remains update trust-region; RouteOPD remains log-odds transport.

### 2026-09-30 — ingest method:graft (active on task:math-code-rl-dense; does not supersede method:cispo / method:verigate / method:miles)
- Added paper:graft (2609.37868), method:graft, recipe:graft (`code_status: none`; `repo_url: none found`). Reverse redirects from math-code-rl-dense and all-zero-verifier-groups for peer all-fail salvage.
- Status active (`sota_for: []`). Replace receiver all-fail groups with mixed peer groups; source advantages + compatibility / token IS clip. Distinct from VeriGate.
- Evidence: +2.1 avg over GRPO n=8 (SmolLM3 32.60→37.06; Qwen3-1.7B 31.20→33.44); stored peer +1.8 (arXiv:2609.37868); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; VeriGate remains PRM gating; Miles remains the engine.

### 2026-09-30 — ingest method:pmopd (active on task:student-distillation; does not supersede method:open-mopd / method:dn-mopd)
- Added paper:pmopd (2609.34605), method:pmopd, recipe:pmopd (`code_status: none`; `repo_url: none found`). Reverse redirect for multi-teacher OPD subspace protection / cycling.
- Status active (`sota_for: []`). Dual projection of gradients and Adafactor updates out of protected task SVD bases; conflict probe + cycling. Ant Group.
- Evidence: Qwen2.5-7B 66.97 vs MOPD 64.43 (+2.54) vs paper Open-MOPD 63.54; Llama-3.1-8B 41.04 vs 38.95 (arXiv:2609.34605); verified: true; evidence_level: preprint.
- Scope checks: Open-MOPD remains multi-teacher default. Paper Open-MOPD 63.54 is NOT the library 83.4% headroom-recovery bake-off. DN-MOPD remains domain-scale calibration.

### 2026-09-28 — weekday SOTA sweep (MOPD-Router, DCE+SRCL, READ)
- MUST 1–3. One new task (`task:lora-skill-composition`). No current_sota retarget of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / ACE / BPCO / CodeMidas / DiffusionOPSD / Self-OPD / mini-SWE-agent / Muon2 / NeoHorse-1 / Claude computer-use / RecreationWorld / Harness-Zero / Jev-Mem / RRSI / IER-OPD / Critical-State RL / PACT / JitMem / VHD-Play / RewardVerse / BPO / ACLArena / Category-Aware SWE / AIDE2 / Rufus-Air / LastOPD / SLCA-GRPO / S2D-OPD / lr-matters-lora / AQLoRA-Q.
- Window: America/Denver 2026-09-28 Librarian weekday sweep. New arXiv 2609.30837, 2609.30652, 2609.31600.

### 2026-09-28 — ingest method:mopd-router (active on task:student-distillation; does not supersede method:open-mopd / method:opd / method:s2d-opd / method:cal-opd / method:ier-opd / method:lastopd)
- Added paper:mopd-router (2609.30837), method:mopd-router, recipe:mopd-router (`code_status: released`; `repo_url: https://github.com/TURLEing/MOPD-Router`; verl/, benchmarks/, run.sh). Reverse redirect from Open-MOPD for token-level ExpertAlign routing over unlabeled multi-teacher pools; reverse from mopd-router back to Open-MOPD for gap-aware budget / token-share balancing defaults.
- Status active (`sota_for: []`). Token-level routing over the full teacher pool (no domain labels, no separate router train). ExpertAlign scores whether a teacher's local correction expresses that teacher's post-train specialty. SJTU / GAIR / Alibaba.
- Evidence: unlabeled mixtures +5.88 / +12.3% overall vs Mean aggregation; labeled +3.95 / +7.8% vs standard MOPD without using domain labels; strong-to-weak + same-size (arXiv:2609.30837); verified: true; evidence_level: preprint.
- Scope checks: Open-MOPD remains multi-teacher default; OPD remains single-teacher; S2D-OPD / Cal-OPD / IER-OPD / LastOPD remain their own axes.

### 2026-09-28 — ingest method:dce-srcl (active on task:privileged-teacher-opsd; does not supersede method:vista)
- Added paper:dce-srcl (2609.30652), method:dce-srcl, recipe:dce-srcl (`code_status: none`; `repo_url: none found`; reproducibility promised, no public repo as of 2026-09-28). Reverse redirect from privileged-teacher-opsd for DCE co-evolution + SRCL concise rewrites.
- Status active (`sota_for: []`). Dynamic Co-Evolution lets the privileged teacher co-evolve with the student (attacks frozen privileged-teacher OPSD); SRCL adds shorter verified rewrites of on-policy responses. Meta AI / UCR.
- Evidence: Qwen3-8B 65.97% Average@12 on four math contests; +35.62 pp vs their OPSD baseline (~30%); −7.80% mean output length vs DCE alone (arXiv:2609.30652); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-OPSD SOTA. This paper's OPSD baseline is NOT comparable to the library VISTA bake-off (~64.8→66.9). Bake before any future retarget. OPD / Self-OPD / LastOPD / S2D-OPD / Open-MOPD remain their own axes.

### 2026-09-28 — ingest method:read-lora (new task:lora-skill-composition; does not supersede method:lr-matters-lora / method:aqlora-q)
- Added paper:read-lora (2609.31600), method:read-lora, recipe:read-lora (`code_status: none`; no code in paper), task:lora-skill-composition. New task first hop; method status active with `sota_for: [task:lora-skill-composition]`. Reverse redirects from task:parameter-efficient-fine-tuning / task:lora-quality-tuning when stacking independently trained adapters / sequential skill add.
- Status active. Canonicalize LoRA factors + read-only coupling (new skill may read old input subspaces, must not write old output subspaces); fold into base weights. No routing / no inference overhead.
- Evidence: Llama-3.2-3B SuperGLUE 0.783 vs 0.605 strongest published same-adapter baseline; Domain 0.887 vs 0.846; Qwen3-4B GLUE 0.838 vs 0.775; shared 32-lineage mean lift +0.073 (95% CI +0.047–+0.101) (arXiv:2609.31600); verified: true; evidence_level: preprint.
- Scope checks: lr-matters-lora remains 24GB quality; AQLoRA-Q remains 4-bit PEFT. No locked current_sota retarget.

### 2026-09-25 — weekday SOTA sweep (Rufus-Air, LastOPD, SLCA-GRPO, S2D-OPD)
- MUST 1–4. One new task (`task:tool-agent-segment-credit`). No current_sota retarget of Miles / OPD / Open-MOPD / CISPO / CANOPY / SAO / ACE / omp2 / TTPO / FoldGRPO / PACT / Cal-OPD / IER-OPD.
- Window: America/Denver 2026-09-25 Librarian weekday sweep after 2609.27334 / HF Daily through 09-24. New arXiv 2609.28845, 2609.29050, 2609.29142, 2609.29421.

### 2026-09-25 — ingest method:rufus-air (active on task:frontier-rl-posttrain-stack; does not supersede method:miles)
- Added paper:rufus-air (2609.29421), method:rufus-air, recipe:rufus-air (`code_status: none`; `repo_url: https://github.com/THUDM/slime`; no dedicated Rufus-Air GitHub). Reverse redirect from Miles for full open post-train recipe / stage order / agentic RL infra playbook.
- Status active (`sota_for: []`). 8-stage serial pipeline on GLM-4.5-Air-Base (106B-A12B): SFT → Reasoning RL → Coding RL → IF RL → General Agent → Coding Agent → Search Agent → RLHF. Amazon.
- Evidence: vs GLM-4.5-Air IFBench 76.9 vs 33.6, LCB v6 76.4 vs 59.6, TB2.1 42.7 vs 24.7, SWE-Verified 65.6 vs 50.6 (arXiv:2609.29421); verified: true; evidence_level: preprint.
- Scope checks: Miles remains the engine; SAO remains async; CISPO remains Pass@1.

### 2026-09-25 — ingest method:lastopd (active on task:student-distillation; does not supersede method:opd / method:open-mopd / method:cal-opd / method:oprd)
- Added paper:lastopd (2609.28845), method:lastopd, recipe:lastopd (`code_status: announced`; Muyiiiii/LastOPD 404 as of 2026-09-25). Reverse redirect for latent OPD collapse / last-layer crossfade.
- Status active (`sota_for: []`). Last-layer pre-LM-head latent loss, then ~10-step crossfade into reverse top-k token OPD. Visa Research.
- Evidence: Qwen3-4B/8B → 1.7B-Base MATH-500 +5.55 / +4.02 vs token-only OPD; ~half the steps to token-OPD final score (arXiv:2609.28845); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; Open-MOPD remains multi-teacher; Cal-OPD remains TSD calibration; same-lineage latent-only stays OPRD-Vanilla.

### 2026-09-25 — ingest method:slca-grpo (new task:tool-agent-segment-credit; does not supersede method:foldgrpo / method:sao / method:pact / method:critical-state-rl / method:cispo)
- Added paper:slca-grpo (2609.29050), method:slca-grpo, recipe:slca-grpo (`code_status: announced`; SLCA-GRPO/SLCA-GRPO 404 as of 2026-09-25; HF YanZhanPKU/SLCA-GRPO-Datasets). New task first hop; method status active (`sota_for: []`). Reverse redirects from long-horizon-tool-agent / agentic-async-rl / math-code-rl-dense / token-level-critic-rl.
- Status active. Segment-locked GRPO: tool advantages to tool tokens, summary advantages to summary tokens. SGLS + HierR. Tencent PCG / PKU.
- Evidence: Qwen2.5-7B matched GRPO +2.53 pp Toucan Success@0.9 / +1.36 pp BFCL / +9.15 pp τ²-Bench (arXiv:2609.29050); verified: true; evidence_level: preprint.
- Scope checks: FoldGRPO remains folding; SAO remains async; PACT remains Actor-then-Critic; Critical-State RL remains which-turn trainability; CISPO remains Pass@1.

### 2026-09-25 — ingest method:s2d-opd (active Direct-OPD plug-in on task:student-distillation; does not supersede method:opd)
- Added paper:s2d-opd (2609.29142), method:s2d-opd, recipe:s2d-opd (`code_status: announced`; review-anonymous `anonymous.4open.science/r/S2D-OPD-8868`). Reverse redirect for Direct-OPD JSD keep-mask.
- Status active (`sota_for: []`). Direct-OPD log-ratio is mass-invariant; keep top ~10% student states by teacher–reference JSD. ECNU.
- Evidence: +0.95 mean held-out Acc over dense Direct-OPD (7/8 settings; 95% CI 0.40–1.54); no extra forwards (arXiv:2609.29142); verified: true; evidence_level: preprint.
- Scope checks: OPD remains strong-teacher matching; Cal-OPD / IER-OPD / LastOPD are different axes; OPRD remains reverse distill.

### 2026-09-24 — weekday SOTA sweep (PACT, JitMem, VHD-Play, RewardVerse)
- MUST 1–4. One new task. No current_sota retarget of CISPO / CANOPY / SAO / OPD / omp2 / TTPO / Miles / ACE / BPCO / CodeMidas / DiffusionOPSD / Self-OPD.
- Window: HF Daily 2026-09-23/24 + arXiv ≳2609.26800. FLAG: UECR-GRPO, RL-Starts-before-RL, AEWM, MemoryAthena, Agensh, JEV-as-a-Judge, EmbodiedSWE, LatentPort, WhatWorkedBench, GeoPair, FLEET.

### 2026-09-24 — ingest method:pact (active on task:token-level-critic-rl; does not supersede method:bpco / method:cispo / method:sao)
- Added paper:pact (2609.26355), method:pact, recipe:pact (`code_status: announced`; AllSpark-Research/PACT empty stub).
- Evidence: agentic-math avg 72.87% (+8.80 GRPO / +13.16 PPO); SWE-Verified 67.4% (+3.8 SAO); verified: true; preprint.

### 2026-09-24 — ingest method:jitmem (active on task:agent-memory; does not supersede method:ace)
- Added paper:jitmem (2609.27334), method:jitmem, recipe:jitmem (`code_status: none`).
- Evidence: ALFWorld/WebShop/τ² +16.2/+16.3/+3.9 abs vs strongest write-time baseline; verified: true; preprint.

### 2026-09-24 — ingest method:vhd-play (new task:mechanism-grounded-agentic-rl-env; does not supersede method:codemidas)
- Added paper:vhd-play (2609.27321), method:vhd-play, recipe:vhd-play (`code_status: none`), task:mechanism-grounded-agentic-rl-env.
- Evidence: 0.204→0.815 five-family diagnostic; E-Commerce Bench > Qwen3.7-Max; verified: true; preprint.

### 2026-09-24 — ingest method:rewardverse (active video-RM plug-in on task:posttrain-diffusion; does not supersede method:diffusion-opsd / method:self-opd)
- Added paper:rewardverse (2609.22947), method:rewardverse, recipe:rewardverse (`code_status: released`; 2kxx/RewardVerse).
- Evidence: EvalVerse SOTA pointwise/pairwise; rubric mitigates scalar drift; verified: true; preprint.

### 2026-09-23 — weekday SOTA sweep (BPO, FP8 Calibrated Clipping, ACLArena, Category-Aware SWE Experts, AIDE2)
- MUST 1–5. Two new tasks (`task:agent-continual-learning`, `task:swe-agent-category-expert-rl`). No `current_sota` retargets of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / Claude computer-use / ACE / mini-SWE-agent / Muon2 / NeoHorse-1 / Code2Skill / Cal-OPD / RecreationWorld / CodeMidas / Vision-RL2 / EPS / Harness-Zero / Jev-Mem / RRSI / IER-OPD / sol-pi / Critical-State RL.
- Window: America/Denver 2026-09-23 Librarian weekday sweep. SKIP: Tasteful Agent / Taste-Bench, RULER SVG, Flash-dLLM, Agensh, JEV-as-a-Judge, onPanda, EDGEGEN, SkillSpec, LatentPort, ALPINE, collusion study, StableVQ, VideoGen-Agent, already-ingested PR29 set (IER-OPD / RRSI / Harness-Zero / Jev-Mem / Critical-State RL).

### 2026-09-23 — ingest method:bpo (active critic-free PMD candidate; does not supersede method:cispo / method:sapo / method:sao)
- Added paper:bpo (2609.15987), method:bpo, recipe:bpo (`code_status: none`; `repo_url: none found`). Wired to task:math-code-rl-dense. Reverse redirect from CISPO for Bellman telescoping vs Pass@1 default.
- Status active (`sota_for: []`). Not dense Pass@1 SOTA. Practical loss replaces the IS ratio with a smoothed complementary-token mismatch weight (ε, C). Authors Apodex / Princeton.
- Evidence: Qwen3-30B-A3B-Base + DAPO-Math-17k peak AIME24–26 Avg@32 50.5% vs CISPO 47.4% (+3.1), GRPO-ClipHigher 39.5% (+11.0); also beats GSPO/DPPO under matched settings (arXiv:2609.15987); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; SAO remains async.

### 2026-09-23 — ingest method:fp8-calibrated-clipping (active FP8 clip plug-in; does not supersede method:miles / method:cispo)
- Added paper:fp8-calibrated-clipping (2609.22870), method:fp8-calibrated-clipping, recipe:fp8-calibrated-clipping (`code_status: none`; `repo_url: none found`; VeRL experiments). Wired to task:frontier-rl-posttrain-stack beside Miles. Reverse redirect from Miles for full-pipeline FP8 clip calibration.
- Status active (`sota_for: []`). Match FP8 lower-bound clipping quantile to BF16 and rebalance the upper bound. ByteDance Seed / UW–Madison.
- Evidence: restores BF16-level quality; tensorwise up to ~1.5× BF16 throughput; blockwise ~10–20%; GRPO/DAPO, 8B–32B, VeRL + vLLM + TorchAO (arXiv:2609.22870); verified: true; evidence_level: preprint.
- Scope checks: Miles remains the engine; CISPO remains Pass@1; skip on BF16-only stacks.

### 2026-09-23 — ingest method:aclarena (new task:agent-continual-learning; does not supersede method:cispo / method:sao / method:canopy / method:miles / method:mini-swe-agent)
- Added paper:aclarena (2609.23989), method:aclarena, recipe:aclarena (`code_status: released`; WillDreamer/ACLArena; HF willhx/aclarena). New task first hop; method status active (`sota_for: []`). Reverse redirects from task:math-code-rl-dense / task:agentic-async-rl / task:outcome-only-long-horizon-agent-rl / task:frontier-rl-posttrain-stack / task:software-engineering-agent-harness / task:student-distillation.
- Status active. Offline replay of high-quality trajectories plus routed LoRA experts specialized via RL. Built on slime.
- Evidence: MLE AIME26 21.04 / NQ 49.7 / τ³-Retail 32.9 / IF-Eval 85.0 vs Seq-Final 10.21 / 33.5 / 29.6 / 84.8 (arXiv:2609.23989); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAO remains async; CANOPY remains AppWorld TGC; Miles remains the engine; mini-SWE-agent remains the loop; OPD / Open-MOPD remain text distill defaults.

### 2026-09-23 — ingest method:category-aware-swe-experts (new task:swe-agent-category-expert-rl; does not supersede method:codemidas / method:sao / method:mini-swe-agent / method:miles)
- Added paper:category-aware-swe-experts (2609.23377), method:category-aware-swe-experts, recipe:category-aware-swe-experts (`code_status: released`; alibaba/AgenticBigBang). New task first hop; method status active (`sota_for: []`). Reverse redirects from task:coding-agent-rl-environment-construction / task:agentic-async-rl / task:software-engineering-agent-harness / task:frontier-rl-posttrain-stack / task:student-distillation. SKIP'd 2026-09-22 for no public code; repo is live.
- Status active. SWE Labeler + RRE experts + label-routed MOPD (ReLU-gated reward extrapolation). No external teacher trajectories. Alibaba Logics-SWE-Qwen3.6-27B line.
- Evidence: Pro-618 58.04% (+5.39 vs base); SWE-bench Multilingual 59.00% (+2.78) (arXiv:2609.23377); verified: true; evidence_level: preprint.
- Scope checks: CodeMidas remains source-only env construction; SAO remains async; mini-SWE-agent remains issue-to-patch; Miles remains the engine.

### 2026-09-23 — ingest method:aide2 (active recursive harness RSI; does not supersede method:omp2-harness / method:rrsi / method:neohorse-1 / method:harness-zero)
- Added paper:aide2 (2609.26457), method:aide2, recipe:aide2 (`code_status: none`; `repo_url: none found`). Mention on task:agent-harness-runtime and task:agentic-rsi-routing-posttrain. Reverse redirects from both tasks, task:harness-distillation, and sibling methods. Authors Weco AI.
- Status active (`sota_for: []`). Outer-loop research agent rewrites its own harness; accepted rewrite becomes the next incumbent.
- Evidence: 8-day autonomous run, 7 accepted improvements, incumbent grade 0.703→0.778 vs AIDE_human 0.749; reward hacking 55%→32% vs human 39% (arXiv:2609.26457); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains kernel spec; RRSI remains regularized frozen-backbone search; NeoHorse-1 remains routing-harness weight post-train; Harness-Zero remains harness-behavior SFT.

### 2026-09-22 — weekday SOTA sweep (IER-OPD, RRSI, Harness-Zero, Jev-Mem, Critical-State RL)
- MUST 1–5. One new task (`task:harness-distillation`). No `current_sota` retargets of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / Claude computer-use / ACE / mini-SWE-agent / Muon2 / NeoHorse-1 / Code2Skill / Cal-OPD / RecreationWorld / CodeMidas / Vision-RL2 / EPS / sol-pi.
- Window: America/Denver 2026-09-22 Librarian weekday sweep. SKIP: OSWorld-Pro, onPanda, Complex KDA, VideoGen-Agent, EDGEGEN, IncLoRA+Muon, iSDFT, InfoPPO, Category-Aware SWE 2609.23377 (no public code).

### 2026-09-22 — ingest method:ier-opd (active sparse-OPD reliability plug-in; does not supersede method:opd / method:cispo / method:sparse-opd-supervision / method:ida-opd / method:cal-opd)
- Added paper:ier-opd (2609.24432), method:ier-opd, recipe:ier-opd (`code_status: released`; BruceSheng1202/IER-OPD). Wired to task:student-distillation beside sparse-opd-supervision and ida-opd. Reverse redirects from student-distillation and sibling methods.
- Status active (`sota_for: []`). Not distill SOTA. IER = teacher-gradient SNR under an optimal scalar baseline; candidate-set ranking fused with usefulness (IER-OR / IER-AND); keep sampled reverse-KL OPD.
- Evidence: 0.1%–1% token budgets match/exceed full OPD on math + HealthBench (JustRL-Qwen3-4B→1.7B Bayes@32 AIME25 15.8 vs full OPD 14.4; HealthBench TIP+IER-OR 46.08 vs 45.77) (arXiv:2609.24432); verified: true; evidence_level: preprint.
- Scope checks: OPD remains distill default; CISPO remains Pass@1; sparse-opd-supervision remains usefulness keep-mask; IDA-OPD remains entropy A_y reweight; Cal-OPD remains TSD calibration.

### 2026-09-22 — ingest method:rrsi (active regularized harness RSI; does not supersede method:omp2-harness / method:neohorse-1 / method:sol-pi / method:mini-swe-agent / method:harness-onpolicy-correction)
- Added paper:rrsi (2609.24972), method:rrsi, recipe:rrsi (`code_status: released`; google-research/rrsi). Mention on task:agent-harness-runtime and task:agentic-rsi-routing-posttrain. Reverse redirects from both tasks and sibling methods.
- Status active (`sota_for: []`). Frozen-backbone harness search with annealed edit budget, unexplored-component proposer, critic+pruner against evolve-set memorization.
- Evidence: Terminal-Bench 2.1 evolve 64.6→78.7 (+14.1) Gemini 3.5 Flash; up to +4.7 on five OOD benches; ~30% fewer policy tokens vs unregularized; 8 benches (arXiv:2609.24972); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains kernel spec; NeoHorse-1 remains routing-harness weight post-train; SoL-Pi remains Pi token-efficiency; mini-SWE-agent remains issue-to-patch; harness-onpolicy-correction remains the evolved-harness SFT gotcha.

### 2026-09-22 — ingest method:harness-zero (new task:harness-distillation; does not supersede method:omp2-harness / method:neohorse-1 / method:opd / method:open-mopd / method:sao / method:canopy)
- Added paper:harness-zero (2609.24974), method:harness-zero, recipe:harness-zero (`code_status: released`; metaevo-ai/harness-zero). New task first hop; method status active (`sota_for: []`). Reverse redirects from task:agent-harness-runtime / task:agentic-rsi-routing-posttrain / task:student-distillation / task:software-engineering-agent-harness / task:agentic-async-rl.
- Status active. Agent-as-harness corrects student replies into the target action space before execution, then SFT; drop the specialized harness at deploy.
- Evidence: Qwen3.5-9B macro success 23.3%→44.3% without specialized harness (vs 41.7% with harness); agent-as-harness 81.1% vs code-as-harness 78.1%; 82.3% recovery of 28 patterns (arXiv:2609.24974); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains kernel; NeoHorse-1 remains routing RSI post-train; OPD / Open-MOPD remain text distill; mini-SWE-agent remains the loop (used here as target harness h); SAO remains async; CANOPY remains AppWorld TGC.

### 2026-09-22 — ingest method:jev-mem (active on task:agent-memory; does not supersede method:ace / method:code2skill)
- Added paper:jev-mem (2609.23986), method:jev-mem, recipe:jev-mem (`code_status: released`; libingzheren/Jev-Mem). Wired to task:agent-memory alongside ACE and Code2Skill. Redirect when System-One control of memory ops.
- Status active. Not memory SOTA. Typed System-One control plane (typing, routing, budget, traversal, scoring, stop) plus multi-relational store; System Two only for hard reasoning.
- Evidence: LoCoMo judge 0.777 vs MAGMA 0.700 (+11% rel); construction 158 s (6.6× vs Nemori 1,044 s); query 0.93 s (−36.7% vs MAGMA 1.47 s) (arXiv:2609.23986); verified: true; evidence_level: preprint.
- Scope checks: ACE remains playbook/memory default; Code2Skill remains repository-grounded skills.

### 2026-09-22 — ingest method:critical-state-rl (active multi-turn trainability diagnostic; does not supersede method:sao / method:canopy / method:cispo / method:foldgrpo)
- Added paper:critical-state-rl (2609.24985), method:critical-state-rl, recipe:critical-state-rl (`code_status: none`; `repo_url: none found`). Wired to task:agentic-async-rl. Reverse redirect for nested-sampling diagnostic vs straggler replay.
- Status active (`sota_for: []`). Diagnose which multi-turn calls are trainable (action-sufficiency, headroom, nested sampling vs continuation noise), then contextual-bandit at selected states.
- Evidence: BFCL v4 miss_func Gemma-4-26B-A4B 0.14→0.283±0.015 (~+14 pp); alternatives flat/worse (arXiv:2609.24985); verified: true; evidence_level: preprint.
- Scope checks: SAO remains async first hop; CANOPY remains AppWorld coverage; CISPO remains Pass@1; FoldGRPO remains folding.

### 2026-09-21 — weekday SOTA sweep (Cal-OPD, CodeMidas, RecreationWorld, Code2Skill, Vision-RL2)
- MUST 1–5. Three new tasks. No `current_sota` retargets of CISPO / CANOPY / SAO / OPD / Open-MOPD / VISTA / omp2-harness / TTPO / Miles / Claude computer-use / ACE / mini-SWE-agent / Muon2 / EPS.
- Window: HF Daily 2026-09-19/20 empty weekend; 2026-09-21 + arXiv ~2609.20800–2609.22086. WATCH/SKIP: GraphSkillEvo 2609.21749, IntBMoE 2609.21346, λ-Controlled GRPO 2609.22041, Matrix AdaGrad 2609.21815, Abstention and Noise Filtering 2609.22005.

### 2026-09-21 — ingest method:cal-opd (active TSD-calibration plug-in; does not supersede method:opd / method:vista / method:retireopd)
- Added paper:cal-opd (2609.21619), method:cal-opd, recipe:cal-opd (`code_status: none`; `repo_url: none found`; verl reimplementation, λ=5, 8×H20). Wired to task:student-distillation; mention on task:privileged-teacher-opsd. Reverse redirect from privileged-teacher-opsd for TSD calibration vs teacher update.
- Status active. Not distill SOTA. Probes teacher self-deviation with positive+negative privileged interventions; residual discrepancy (~52–65%) is the OPD advantage. Differentiates from RetireOPD (retirement timing).
- Evidence: Qwen3-4B→1.7B Avg@16 53.1 vs OPD 50.8; Qwen3-30B-A3B→4B 69.0 vs OPD 65.9 (arXiv:2609.21619); verified: true; evidence_level: preprint.
- Scope checks: OPD remains student distill; VISTA remains privileged-teacher adaptation; RetireOPD remains agent-RL retirement.

### 2026-09-21 — ingest method:codemidas (new task:coding-agent-rl-environment-construction; does not supersede method:canopy / method:sao / method:miles / method:mini-swe-agent)
- Added paper:codemidas (2609.22068), method:codemidas, recipe:codemidas (`code_status: none`; project `https://mimo.xiaomi.com/rl/`; no public GitHub as of 2026-09-21). New task first hop; method status active (`sota_for: []`). Mentions and reverse redirects from task:outcome-only-long-horizon-agent-rl / task:agentic-async-rl / task:software-engineering-agent-harness.
- Status active. Source-code-only env factory (explore → specs → execution-grounded tests → filter) then GRPO. 5,545 tasks / 3,185 repos / 23 languages.
- Evidence: MiMo-V2.5 GRPO DeepSWE 10.0→21.7, ProgramBench Almost Solved 4.5→21.5, Terminal-Bench v2.1 +8.5pp (arXiv:2609.22068); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld coverage; SAO remains async; Miles remains the engine; mini-SWE-agent remains the loop.

### 2026-09-21 — ingest method:recreationworld (new task:hybrid-computer-use-agent-rl; does not demote method:claude-computer-use)
- Added paper:recreationworld (2609.22000), method:recreationworld, recipe:recreationworld (`code_status: released`; QwenLM/RecreationWorld; RecreationBench 250; HF `Qwen/RecreationBench`). New task first hop; method status active. Reverse redirect from task:computer-use-agent for hybrid GUI+code training.
- Status active. Hybrid CUA train/eval (GUI + code interleaved) across Ubuntu/macOS/Windows/Android/Web; reference-as-oracle rewards; OOD transfer.
- Evidence: GPT-6 Astra RecreationBench 58.1% overall / 2.8% full programmatic; OOD up to +17.9 pp (arXiv:2609.22000); verified: true; evidence_level: preprint.
- Scope checks: Claude computer-use remains OSWorld 2.0 ranking; mini-SWE-agent remains issue-to-patch; CANOPY remains AppWorld.

### 2026-09-21 — ingest method:code2skill (active on task:agent-memory; does not supersede method:ace)
- Added paper:code2skill (2609.05571), method:code2skill, recipe:code2skill (`code_status: partial`; ant-intl/Code2Skill pre-release; HF `ant-intl/DeveloperSkills-Code2Skill`). Wired to task:agent-memory alongside ACE. Redirect when repository-grounded skills before interaction.
- Status active. Not memory SOTA. Pipeline lifts code units into verified atomic/composite/pattern skills; CodeSkillBank ~1.0M from 19,769 repos.
- Evidence: +11.7% avg over matched baselines across 72 evals / 8 benches (42.90→47.90, 57/72); vs Trace2Skill 31.0 / ExpeL 27.9 / SkillRL-Bank 32.8, Code2Skill 49.5 (arXiv:2609.05571); verified: true; evidence_level: preprint.
- Scope checks: ACE remains playbook/memory default; mini-SWE-agent remains the loop with no bank.

### 2026-09-21 — ingest method:vision-rl2 (new task:mllm-finegrained-perception-rl; does not supersede method:eps-prompt-scaffolding)
- Added paper:vision-rl2 (2609.19745), method:vision-rl2, recipe:vision-rl2 (`code_status: released`; YuHengsss/VisionRL2). New task first hop; method status active. Reverse redirects from task:mllm-rl-prompt-curriculum / task:rl-video-mllm.
- Status active. Region-level RL on a lightweight RoI proposal network; frozen MLLM reader scores leave-one-out likelihood; sparse encoding cuts visual tokens ~4×.
- Evidence: Qwen3.5-9B six-bench avg 80.1 vs base 74.6 / Vision-OPD-9B 78.7; 4B aligned 71.1 vs SD-RPN 66.6 with 4.2× fewer tokens (arXiv:2609.19745); verified: true; evidence_level: preprint.
- Scope checks: EPS remains prompt-curriculum first hop; OraRL remains video annotation-as-rollout; CISPO remains Pass@1.

### 2026-09-18 — weekday SOTA sweep (RetireOPD, When2Think, ActObs, OPD-EOS, SoL-Pi, bias-only TTRL)
- MUST 1–6. Active/niche only. No new tasks. No false supersessions of CISPO / CANOPY / SAO / VISTA / OPD / OPSA / TTPO / omp2-harness / mini-swe-agent / NeoHorse-1 / Muon2.
- Housekeeping: `paper:deepseek-v41-flash` `arxiv_id` set to 2609.19969.

### 2026-09-18 — ingest method:retireopd (active Adaptive Retirement; does not supersede method:canopy / method:sao / method:opd / method:vista / method:opsa)
- Added paper:retireopd (2609.20784), method:retireopd, recipe:retireopd (`code_status: none`; `repo_url: none found`). Wired to task:outcome-only-long-horizon-agent-rl; mention on task:agentic-async-rl / task:student-distillation / task:privileged-teacher-opsd. Reverse redirect from agentic-async-rl for privileged self-OPD then retire to RL.
- Status active. Not AppWorld TGC SOTA. Drop the privileged teacher when discrepancy stops shrinking and the student hits a fraction of teacher success, then pure RL.
- Evidence: Qwen2.5 1.5B–7B ALFWorld SR +14.1–18.8% vs RL; WebShop +11.8–19.0%; student beats its skill-conditioned teacher in every reported setting (arXiv:2609.20784); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains checker protocol; SAO remains async; OPD remains student distill; VISTA remains privileged math OPSD.

### 2026-09-18 — ingest method:when2think (active IDAC Think/NoThink plug-in; does not supersede method:cispo)
- Added paper:when2think (2609.19671), method:when2think, recipe:when2think (`code_status: partial`; GitHub JJunShim/When2Think stub README). Wired to task:math-code-rl-dense as an efficiency plug-in.
- Status active. Not Pass@1 SOTA. Offline reference accuracy/token stats shape Think vs NoThink.
- Evidence: AIME24 Pass@3 +10.0% with tokens −27.9% vs base; AIME25 Pass@3 40.0% over compression/routing-only (arXiv:2609.19671); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; ES-reasoning remains Pass@K / no-backward.

### 2026-09-18 — ingest method:actobs (active observation-token SFT; does not supersede method:sao / method:mini-swe-agent / method:canopy)
- Added paper:actobs (2609.20715), method:actobs, recipe:actobs (`code_status: none`; `repo_url: none found`). Wired to task:agentic-async-rl; mention on task:software-engineering-agent-harness / task:outcome-only-long-horizon-agent-rl. Reverse redirect from the SWE harness for observation-token SFT before GRPO.
- Status active. SFT looks similar; GRPO exploration changes.
- Evidence: Qwen3-4B Terminal-Bench 2.0 higher pass@k at every budget vs action-only; Qwen3-8B +3.4 pp pass@16; aider-polyglot +4.2 pp pass@1 at 4B (arXiv:2609.20715); verified: true; evidence_level: preprint.
- Scope checks: SAO remains async stragglers; mini-SWE-agent remains the loop; CANOPY remains coverage.

### 2026-09-18 — ingest paper:opd-eos / method:opd-eos (niche gotcha + semantic-class stop; does not supersede method:opd)
- Added paper:opd-eos (2609.20511), method:opd-eos (status niche), recipe:opd-eos. Code: UNCSciML/opd-eos. Wired to task:student-distillation. Gotchas added on method:opd and recipe:opd (same pattern as paper:spurious-advantage-grpo).
- Teacher/student EOS mismatch inflates length under OPD; decoding-stop alignment is insufficient; semantic-class stop is the fix. Late K2-Horizon inflation can remain.
- Evidence: Qwen stop-mass → ~0 by step 150 without the fix; Gemma 7168-clip ~100% → mean ~2000 tokens (arXiv:2609.20511); verified: true; evidence_level: preprint.
- Scope checks: OPD remains student-distill default.

### 2026-09-18 — ingest method:sol-pi (active Pi token-efficiency sibling; does not supersede method:omp2-harness / method:mini-swe-agent / method:neohorse-1)
- Added paper:sol-pi (2609.20519), method:sol-pi, recipe:sol-pi. Code: NVlabs/SoL-Pi. Wired to task:agent-harness-runtime; mention on task:agentic-rsi-routing-posttrain. Reverse redirect from NeoHorse's task for Pi harness mechanisms vs routing-guided OPD.
- Status active. Action Fusion / ObservationPack / Evidence-Preserving Reducer / Online Context Compact. Opt-in, default off.
- Evidence: EdgeBench 51-task Pi parity at −44.7–49.0% token traffic / ~−1/3 API cost (arXiv:2609.20519); verified: true; evidence_level: preprint.
- Scope checks: omp2 remains the kernel spec; mini-SWE-agent remains issue-to-patch; NeoHorse-1 remains routing-harness post-train.

### 2026-09-18 — ingest method:bias-only-ttrl (niche bias-subspace TTRL; does not supersede method:ttpo)
- Added paper:bias-only-ttrl (2609.18587), method:bias-only-ttrl, recipe:bias-only-ttrl (`code_status: none`; `repo_url: none found`). Wired to task:label-free-test-time-reasoner beside TTPO.
- Status niche. Majority-vote rewards on ~100K bias params; backbone frozen.
- Evidence: MATH-500 76.67%; ~76,000× fewer trainable params than full TTRL (arXiv:2609.18587); verified: true; evidence_level: preprint.
- Scope checks: TTPO remains label-free TTT; u-OPSD remains train-time unlabeled; CISPO remains Pass@1.

### 2026-09-16 — weekday SOTA sweep (NGU, DCO)
- MUST 1–2. Active plug-ins only. No new tasks. No false supersessions of CISPO / SAPO / GRPO / ThinkPrior / DIEM / GMTS / DataFlex-RL / NoRA / Iso-LoRA / lr-matters-lora / OLMo-3 / Delta Learning / Open-MOPD.

### 2026-09-16 — ingest method:ngu (active async sampler; does not supersede method:cispo / method:sapo / method:grpo / method:thinkprior / method:diem / method:gmts / method:dataflex-rl / method:sao)
- Added paper:ngu (2609.13443), method:ngu, recipe:ngu (`code_status: partial`; `repo_url: none found`; claimed `mnoukhov/never-give-up` HTTP 404 on 2026-09-16; blog `mnoukhov.github.io/posts/ngu`). Wired to task:math-code-rl-dense; mention on task:agentic-async-rl / task:reasoning-rl-alignment. Reverse redirect from agentic-async-rl for math/code until-correct sampling.
- Status active. Not Pass@1 SOTA. Keep sampling a prompt until ≥1 correct; reallocates async compute off easy prompts onto hard ones (Matthew Effect / signal efficiency).
- Evidence: Deepscaler Qwen3-4B-Base NGU p=0.875 avg pass@1 26.5±0.6 vs GRPO K=16 24.8±1.0, hard-subset Δ 4.3±1.2 vs 1.6±0.3; Manufactoria GRPO+NGU reaches all-tests solves where GRPO stalls (arXiv:2609.13443); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; GRPO stays retired as the loss; ThinkPrior remains cold-start prompt select; DIEM/GMTS remain example/token reweight; DataFlex-RL remains the accuracy-null; SAO remains async stragglers.

### 2026-09-16 — ingest method:dco (active drift-budget instruct FT; does not supersede method:olmo-3 / method:lr-matters-lora / method:nora / method:iso-lora / method:delta-learning / method:open-mopd)
- Added paper:dco (2609.13680), method:dco, recipe:dco. Code: CONE-MT/DCO (LLaMA-Factory freeze LST; confirmed). HF collection LLaMAX/dco. Wired to task:instruct-sft-alignment; mention on task:parameter-efficient-fine-tuning. Cross-redirects PEFT ↔ instruct for drift-budget vs LoRA quality.
- Status active. Not instruct SOTA. Optimize update direction (coarse layer-selective probe) under an anchored-KL budget; reverses QA-only FT failure while keeping reasoning; stronger RL init.
- Evidence: Qwen3-8B LST b4t16 FLORES-101 xCOMET 52.66/55.60 vs ref 47.07/51.40 and Seed-X-PPO-7B 47.76/51.31; SmolInstruct FFT 59.65 dumps general avg 42.22→33.60 while LST b4t16 29.61 / 44.03 (arXiv:2609.13680); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains open instruct; lr-matters-lora remains 24GB LoRA quality; NoRA / Iso-LoRA remain LoRA-geometry; Delta Learning remains activation-space deltas; Open-MOPD remains multi-teacher distill.

### 2026-09-15 — weekday SOTA sweep (EPS prompt scaffolding)
- Ingested arXiv:2609.15051 (EMNLP 2026 main). New narrow task `task:mllm-rl-prompt-curriculum`. No false supersessions of CISPO / SAPO / OraRL / DataFlex / GRPO / CANOPY / DIEM.

### 2026-09-15 — ingest method:eps-prompt-scaffolding (new task:mllm-rl-prompt-curriculum; does not supersede method:orarl / method:dataflex-rl / method:cispo / method:sapo / method:grpo / method:canopy / method:diem)
- Added paper:eps-prompt-scaffolding (2609.15051), method:eps-prompt-scaffolding, recipe:eps-prompt-scaffolding (`code_status: partial`; `repo_url: none found`; project page only). Reverse redirects from task:rl-video-mllm / task:math-code-rl-dense. DataFlex mention: static-policy null vs online adaptive scaffolding.
- Status sota for the multimodal prompt-curriculum task only. EPS from on-policy GRPO rewards; teacher task-preserving rewrites; dynamic pool.
- Evidence: Qwen3-VL-4B Geo3K 65.39 vs GRPO 60.57; MMK12 71.15 vs 68.05; 2B MMK12 relatives +9.7% in-domain / +11.5% MathVision / +11.1% MMMU-Pro (arXiv:2609.15051); verified: true; evidence_level: peer-reviewed.
- Scope checks: OraRL remains video annotation-as-rollout; CISPO remains Pass@1; SAPO remains MoE/VL loss; DataFlex remains the static-policy null; GRPO stays the host; CANOPY remains outcome-only agents; DIEM remains example-reweight.

### 2026-09-14 — weekday SOTA sweep (SCOPE-OPSD, MInTRL, ESRL, PLC-DPO, SAS, Tiny Aya L2-Thinker, CanvasAnneal, EvoRS, DDO, Iso-LoRA)
- MUST 1–6 plus optional 7–10. Two new narrow tasks (`task:posttrain-attention-sparsification`, `task:multilingual-l2-reasoning-sft`). No false supersessions of CISPO / SAPO / OLMo-3 / SimPO / VISTA / OPSA / Muon2 / Miles / DeepSeek-V4 / Kimi-K3.
- Skipped: DataFlex-RL (already ingested), NSD / Musec / Nemotron IMO Gold / NCP / RLT / SMELT / V4.1-Flash (already in), COBRA-Skills, HyQuant, Thai TTS/OCR, robotics LIT. Weekend HF Daily 09-12/13 empty.

### 2026-09-14 — ingest method:iso-lora (active optimizer-shape LoRA note; does not supersede method:lr-matters-lora / method:nora / method:anlr-lora)
- Added paper:iso-lora (2609.12123), method:iso-lora, recipe:iso-lora (`code_status: partial`; `repo_url: none found`). Wired to task:lora-quality-tuning / task:parameter-efficient-fine-tuning.
- Status active. Nominal LoRA rank is capacity; AdamW vs Muon shapes effective rank. Iso-LoRA spectrally couples BA updates.
- Evidence: LLaMA-2-7B GSM8K rank-128 EM 61.87 vs Full FT 59.52 / LoRA-Pro 59.20 (arXiv:2609.12123); verified: true; evidence_level: preprint.
- Scope checks: lr-matters-lora remains the 24GB quality default; NoRA remains RLVR-stable A; AnLR remains per-rank LR.

### 2026-09-14 — ingest method:ddo (active successful-strategy coverage; does not supersede method:olmo-3 / method:simpo / method:canopy / method:draco)
- Added paper:ddo (2609.10052), method:ddo, recipe:ddo. Code: koguma00/direct_diverse_optimization. Wired to task:direct-preference-alignment; mention on task:outcome-only-long-horizon-agent-rl.
- Status active. DTC branch sets + RTO odds matching over successful alternatives.
- Evidence: strongest among DPO / DivFreq / DivProb / TieDPO on BabyAI / BabaIsAI / WebShop (arXiv:2609.10052); verified: true; evidence_level: preprint.
- Scope checks: Dolci / SimPO remain preference defaults; CANOPY / DRACO remain outcome-only first hops.

### 2026-09-14 — ingest method:evors (active Reward-DAG evolution; does not supersede method:canopy / method:draco)
- Added paper:evors (2609.12459), method:evors, recipe:evors (`code_status: partial`; `repo_url: none found`). Wired to task:outcome-only-long-horizon-agent-rl.
- Status active. On-policy designer edits an executable Reward-DAG under success / anti-hack / health / informativeness guards. Writing/roleplay domain, not AppWorld TGC.
- Evidence: WritingBench + CoSER three-judge average vs static and dynamic rubric RL (arXiv:2609.12459); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains checker protocol; DRACO remains frozen-judge step credit.

### 2026-09-14 — ingest method:canvasanneal (active discrete-DLM curriculum; does not supersede method:diffusion-opsd / method:self-opd / method:uno)
- Added paper:canvasanneal (2609.13060), method:canvasanneal, recipe:canvasanneal (`code_status: partial`; `repo_url: none found`). Wired to task:posttrain-diffusion; reverse redirect from task:diffusion-augmented-ar.
- Status active. Teacher-trace canvas anneal on LLaDA-7B-A1B-Instruct + diffu-GRPO.
- Evidence: MATH500 +6.0 / +2.0 / +0.4 vs diffu-GRPO at gen 128/256/512; GSM8K mixed (arXiv:2609.13060); verified: true; evidence_level: preprint.
- Scope checks: DiffusionOPSD / Self-OPD remain image/flow defaults; Uno remains AR serving.

### 2026-09-14 — ingest method:tiny-aya-l2-thinker (new task:multilingual-l2-reasoning-sft; does not supersede method:olmo-3 / method:cispo)
- Added paper:multilingual-bridges (2609.10445), method:tiny-aya-l2-thinker, recipe:tiny-aya-l2-thinker (`code_status: partial`; HF weights CohereLabs/tiny-aya-l2-thinker, no train GitHub), task:multilingual-l2-reasoning-sft. Reverse redirects from task:open-data-recipe / task:instruct-sft-alignment / task:math-code-rl-dense.
- Status sota for the L2-fidelity task only. MR+NR+English reasoning mix; >93% L2 rate across 60 languages at 3.35B.
- Evidence: L2 rate >93% on 6 benchmarks; PolyMath 11.1 vs Qwen3.5-4B 40.3 is a gotcha, not Pass@1 SOTA (arXiv:2609.10445); verified: true; evidence_level: preprint.
- Scope checks: OLMo-3 remains open instruct / Dolma-3; CISPO remains Pass@1.

### 2026-09-14 — ingest method:sas (new task:posttrain-attention-sparsification; does not supersede method:rlm / method:mamba-2 / method:uno)
- Added paper:sas (2609.13141), method:sas, recipe:sas. Code: Tencent-Hunyuan/Simple-Attention-Sparsification (branch `release`); HF tencent/Simple-Attention-Sparsification. Reverse redirects from task:long-context-prompt-offload / task:linear-time-sequence-modeling / task:software-engineering-agent-harness.
- Status sota for the narrow budgeted-selector task only. End-to-end LM-loss gates vs Top-K + dense-attention distillation.
- Evidence: +6.0–7.7 MATH500 and +10.6–15.5 GPQA-Diamond vs SeerAttention-R at budget 1024 on Qwen3-4B/8B/14B (arXiv:2609.13141); verified: true; evidence_level: preprint.
- Scope checks: RLM remains dumped-prompt offload; Mamba-2 remains SSM pretrain; Uno remains diffusion-augmented AR serving.

### 2026-09-14 — ingest method:plc-dpo (active noisy-label DPO; does not supersede method:olmo-3 / method:simpo)
- Added paper:plc-dpo (2608.30597), method:plc-dpo, recipe:plc-dpo. Code: VennTum99/PLC-DPO. Wired to task:direct-preference-alignment.
- Status active. Routes each pair as clean / flip / tie from a calibrated policy-reference margin. EMNLP 2026 Findings.
- Evidence: mean win rate 60.5 vs next-best 55.5 across 57 cells (arXiv:2608.30597); verified: true; evidence_level: peer-reviewed.
- Scope checks: OLMo-3 Dolci remains the open stack; SimPO remains the clean reference-free baseline.

### 2026-09-14 — ingest method:esrl (active MoE routing exploration; does not supersede method:sapo)
- Added paper:esrl (2609.13058), method:esrl, recipe:esrl. Code: strawberrymaster111/ESRL-Release (slime + SGLang patches). Wired to task:math-code-rl-moe.
- Status active. Anchored noisy expert sampling + entropy-adaptive noise + rollout expert-ID replay (R3).
- Evidence: Qwen3-30B-A3B MATH avg Pass@1/Pass@8 42.1/64.2 vs GRPO 38.9/59.7 (arXiv:2609.13058); verified: true; evidence_level: preprint. Not a SAPO bake-off.
- Scope checks: SAPO remains the MoE/VL loss default; RPB remains the router soft-anchor; CISPO remains dense Pass@1.

### 2026-09-14 — ingest method:mintrl (active sparse-intervention RLVR plug-in; does not supersede method:cispo / method:sapo / method:sao)
- Added paper:mintrl (2609.12419), method:mintrl, recipe:mintrl (`code_status: partial`; `repo_url: none found`). Wired to task:math-code-rl-dense.
- Status active. Judge Keep/Revise on short suffixes inside otherwise on-policy rollouts; sequence-level advantage regression (no IS). Paper lists long-horizon agentic eval as future work.
- Evidence: Qwen3-1.7B MInTRL-Const 35.45 math / 61.95 code vs stronger of GRPO and OPD (arXiv:2609.12419); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; SAPO remains MoE/VL; SAO remains async stragglers; CANOPY remains outcome-only agents.

### 2026-09-14 — ingest method:scope-opsd (active Fisher-subspace OPSD auxiliary; does not supersede method:vista / method:nsd / method:opsa / method:opd / method:cispo)
- Added paper:scope-opsd (2609.12579), method:scope-opsd, recipe:scope-opsd (`code_status: partial`; `repo_url: none found`). Wired to task:privileged-teacher-opsd beside VISTA / NSD.
- Status active. Projects the privileged teacher-student residual onto a frozen rank-64 Fisher-sensitive factor; matched Random control; reuses OPSD forwards.
- Evidence: Qwen3-1.7B/4B/8B step-75 Macro Avg@12 43.33 / 63.80 / 65.28 vs Pure OPSD 41.48 / 62.13 / 64.45 (arXiv:2609.12579); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-teacher first hop; NSD remains anti-collapse; OPSA remains teacher-free; OPD remains matching distill; CISPO remains Pass@1.

### 2026-09-12 — ingest method:recurrent-looped-transformer (experimental; does not supersede method:muon2 / method:deepseek-v4 / method:deepseek-v41-flash / method:ncp-archpreview)
- Added paper:recurrent-looped-transformer (tech report 2026-09-12, no arXiv), method:recurrent-looped-transformer, recipe:recurrent-looped-transformer (`code_status: partial`; GitHub yifanzhang-pro/recurrent-looped-tranformer, note spelling), task:recurrent-encoder-decoder-lm. Reverse redirects from task:latent-space-lm-pretrain / task:pretrain-moe-frontier / task:software-engineering-agent-harness / task:agent-harness-runtime.
- Status experimental. Causal encoder KV + all-token recurrent decoder; shared pretrain/SFT/sample/current-policy replay; 48+48 reference; no measured efficiency or scaling.
- Evidence: mechanisms only; verified: false; evidence_level: self-reported.
- Scope checks: Muon2 remains ~7B optimizer; NCP remains latent-space; DeepSeek-V4 / Kimi-K3 remain MoE pretrain; V4.1-Flash remains CED serving; mini-SWE-agent remains the harness.

### 2026-09-12 — ingest method:smelt (active looped-MoE recipe; does not supersede method:deepseek-v4 / method:kimi-k3 / method:ce-moe)
- Added paper:smelt (2609.01343), method:smelt, recipe:smelt (`repo_url: none found`), task:compute-matched-moe-looped-pretrain. Wired as sibling of method:ce-moe on task:pretrain-moe-frontier with reverse redirect.
- Status active. Loop middle 50% of MoE layers twice; narrow width; raise experts; residual scale 1/2; match FLOPs / non-embedding params / KV. Scales to 54B non-embedding.
- Evidence: 6.8–18.0% training FLOPs saved on the compute-optimal sparse-grid frontier; DCLM Completion 96/96; Code largest; second visit reduces attention sink (arXiv:2609.01343); verified: true; evidence_level: preprint.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain MoE architecture co-defaults; CE-MoE remains the communication-layout niche.

### 2026-09-12 — ingest method:deepseek-v41-flash (new task:input-heavy-agentic-moe-serving; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:deepseek-v41-flash (HF tech report, no arXiv), method:deepseek-v41-flash, recipe:deepseek-v41-flash (`code_status: partial`; HF weights + inference/ + deepseek-ai/deepseek-recipe). Reverse redirect on task:pretrain-moe-frontier. Cross-link method:mhc (Single-Pass mHC) and method:recurrent-looped-transformer (experimental conceptual sibling). No prior method:deepseek-v4-flash node.
- Status sota for the serving task only. 552B CED 20+20; 8B prefill / 16B decode; CSA2; FP4 main KV ~890 B/token (~1/4 V4-Flash); SWA Bounded Replay (~1/8 persistent KV); Engram; DSpark. API news: V4-Flash / V4-Flash-Vision-Exp retired; V4-Pro routing to V4.1-Flash from 2026-09-14.
- Evidence: vendor card Terminal-Bench 2.1 90.6 / DeepSWE v1.1 74.2 / 890 B/token (HF model card + DeepSeek_V41_Tech_Report.pdf); verified: true; evidence_level: self-reported.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain pretrain co-defaults. CISPO / Muon2 / OPD / VISTA / OPSA / CANOPY / SAO / Miles / NeoHorse-1 / mini-SWE-agent / Iris / Poolside / MAGIC / Nemotron IMO Gold / NCP-ArchPreview first hops unchanged.

### 2026-09-11 — wire verified artifact pointers on the 2026-09-11 sweep (no first-hop retarget)
- NSD: collection slug is `PassionPrc/nsd-negative-self-distillation` (not bare `PassionPrc/nsd`); train/eval stay in-repo verl at Prongcan/NSD (`scripts/4B_NSD/`, `scripts/eval/`).
- Nemotron IMO Gold: collection `nvidia/nemotron-labs-imo-2026`; dataset `nvidia/Nemotron-IMO-Bench`; Skills `recipes/nemotron-imo-tts`; NeMo-RL `imo-26-ultra-v3` guide; SFT/RL ckpts and Math-Proofs datasets already named.
- NCP: `ArchSpace-Collection/NCP_ArchPreview_*`; eval LUMIA-Group/ncp_olmo_eval; serving LuckySJTU/vllm_ncp_archpreview (obsolete fork; successor LuckySJTU/vllm `dev/ncp-archpreview`). `recipe:ncp-archpreview` `code_status: partial` (no official train GitHub).
- Revisiting traces: `https://github.com/naver-ai/revisiting-trace` confirmed. Harness on-policy correction stays niche stub (`repo_url: none found`).
- First hops unchanged: VISTA / CISPO / Muon2 / OLMo-3 / mini-SWE-agent. Skipped AgentGrad / HyQuant / AdamX / OPD-gating-TweetEval.

### 2026-09-11 — ingest 2026-09-11 weekday SOTA sweep (NSD, Musec, Nemotron IMO Gold, NCP, harness on-policy correction, partial traces, MoE repetition, T1)
- MUST 1–6 plus optional 7–8. Two new narrow tasks (`task:latent-space-lm-pretrain`, `task:olympiad-math-posttrain`). No false supersessions of CISPO / Muon2 / OPD / OPSA / VISTA / CANOPY / SAO / ES-reasoning / Miles / NeoHorse-1 / mini-SWE-agent / Iris / Poolside.
- Skipped WATCH: AdamX 2609.11867, unified per-token OPD gating 2609.11768, AgentGrad, HyQuant, LILA, TF-IDF CE.

### 2026-09-11 — ingest method:nsd (active sibling; does not supersede method:vista / method:cispo / method:opd / method:opsa)
- Added paper:nsd (2609.11699), method:nsd, recipe:nsd. Code: Prongcan/NSD. Wired to task:privileged-teacher-opsd; mention on task:teacher-free-on-policy-self-adaptation and method:opsd-collapse-review.
- Status active. Diverges from a self-generated negative condition instead of imitating privileged traces.
- Evidence: Qwen3-1.7B/4B/8B ΔAvg +2.3 / +7.5 / +6.0 vs OPSD/Intuitor/TTRL (Table 1, arXiv:2609.11699); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-teacher first hop; CISPO remains Pass@1; OPD remains matching distill; OPSA remains teacher-free; opsd-collapse-review stays the niche survey.

### 2026-09-11 — ingest method:musec (active Muon stability plug-in; does not supersede method:muon2 / method:muonclip-kimi-k2)
- Added paper:musec (2609.11655), method:musec, recipe:musec (Soft Musec stub on kellerjordan/modded-nanogpt). Wired to task:llm-pretraining-optimization; mention on task:pretrain-dense-7b.
- Status active. Spectral clip of momentum singular values vs Muon flattening.
- Evidence: Soft Musec stays stable where Muon variants diverge on modded-nanogpt; matches them when already well-tuned (arXiv:2609.11655); verified: true; evidence_level: preprint.
- Scope checks: Muon2 remains ~7B optimizer; MuonClip remains trillion-scale MoE recipe.

### 2026-09-11 — ingest method:nemotron-imo-gold (new task:olympiad-math-posttrain; does not supersede method:cispo / method:nemotron-3-ultra)
- Added paper:nemotron-imo-gold (2609.10712), method:nemotron-imo-gold, recipe:nemotron-imo-gold, task:olympiad-math-posttrain. Reverse redirect on task:math-code-rl-dense. Cross-link method:nemotron-3-ultra.
- Status active. SFT+RL specialists + NL generate–verify–refine TTC. Artifacts: NVIDIA-NeMo/Skills recipes/nemotron-imo-tts; NeMo-RL imo-26-ultra-v3 guide; nvidia/Nemotron-3-Labs-Ultra-Math-{SFT,RL}.
- Evidence: IMO 2026 30/42 gold threshold (arXiv:2609.10712); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; Ultra remains the base architecture; OLMo-3 remains instruct SFT.

### 2026-09-11 — ingest method:ncp-archpreview (new task:latent-space-lm-pretrain; experimental; does not supersede method:muon2 / method:olmo-3)
- Added paper:ncp-archpreview (2609.10715), method:ncp-archpreview, recipe:ncp-archpreview, task:latent-space-lm-pretrain. Reverse redirects on task:llm-pretraining-optimization / task:pretrain-dense-7b / task:open-data-recipe.
- Status experimental. Joint NTP + Next Concept Prediction; 8.9B on 5.73T Dolma-3. Weights: ArchSpace-Collection/ncp-archpreview. Eval: LUMIA-Group/ncp_olmo_eval.
- Evidence: 51.3% tokens to match OLMo-3-7B Stage-1 loss; +2.45 macro; +5.99 GSM8K (arXiv:2609.10715); verified: true; evidence_level: preprint.
- Scope checks: Muon2 remains the optimizer; OLMo-3 remains the open mix.

### 2026-09-11 — ingest method:harness-onpolicy-correction (niche gotcha; does not supersede method:mini-swe-agent / method:miles / method:neohorse-1)
- Added paper:harness-onpolicy-correction (2609.09134), method:harness-onpolicy-correction, recipe:harness-onpolicy-correction (stub; no official code). Wired to task:software-engineering-agent-harness / task:agent-harness-runtime / task:agentic-rsi-routing-posttrain.
- Status niche. Full expert-trajectory LoRA-SFT after model-specific harness evolution regresses (−4 to −30 pts); on-policy failing-turn rewrite is the fix.
- Evidence: all seven enterprise tasks, Qwen3-Coder and Gemma 4 (arXiv:2609.09134); verified: true; evidence_level: preprint.
- Scope checks: mini-SWE-agent remains the harness; Miles remains the stack; NeoHorse-1 remains RSI routing post-train.

### 2026-09-11 — ingest method:partial-reasoning-traces (active SFT-data plug-in; does not supersede method:olmo-3 / method:nemotron-cascade-2)
- Added paper:partial-reasoning-traces (2609.07103), method:partial-reasoning-traces, recipe:partial-reasoning-traces. Code: naver-ai/revisiting-trace. Wired to task:instruct-sft-alignment; mention on task:math-code-rl-dense.
- Status active. Full long CoT SFT is overfed; partial/truncated traces work; intermediate tokens contribute little.
- Evidence: EMNLP 2026 Findings; attention + token-removal studies (arXiv:2609.07103); verified: true; evidence_level: peer-reviewed.
- Scope checks: OLMo-3 / Nemotron-Cascade 2 remain instruct defaults; CISPO remains Pass@1.

### 2026-09-11 — ingest method:moe-data-repetition (niche gotcha; does not supersede method:deepseek-v4 / method:kimi-k3)
- Added paper:moe-data-repetition (2609.11917), method:moe-data-repetition, recipe:moe-data-repetition (no code). Wired to task:pretrain-moe-frontier / task:train-moe-nvl72.
- Status niche. MoEs degrade from ~4× repeats; dense 80M tolerated 8×; effect scales with total params.
- Evidence: 80M–1B active / 8.5B total (arXiv:2609.11917); verified: true; evidence_level: preprint.
- Scope checks: DeepSeek-V4 / Kimi-K3 remain MoE architecture defaults.

### 2026-09-11 — ingest method:t1-terminal-rl (active; does not supersede method:canopy / method:sao / method:miles)
- Added paper:t1-terminal-rl (2609.11042), method:t1-terminal-rl, recipe:t1-terminal-rl. Host: THUDM/slime v0.3.0. Project: jyyang26.github.io/t1. Wired as mention on task:outcome-only-long-horizon-agent-rl / task:frontier-rl-posttrain-stack / task:agentic-async-rl.
- Status active. 122B MoE terminal RL, TITO + R3. Not a new first hop.
- Evidence: Terminal-Bench 2.1 43.8%→64.0%; Long-Horizon Terminal Bench 27.9% (arXiv:2609.11042); verified: true; evidence_level: preprint.
- Scope checks: CANOPY remains AppWorld coverage; SAO remains async algorithm; Miles remains the production stack.

### 2026-09-09 — refine 2026-09-09 sweep (OPRD code, VERPO, RPB, group-correlation, OPSD collapse review)
- Corrections on the open PR: OPRD recipe now points at raymin0223/on_policy_reverse_distillation. ACE MoE PEFT was already ingested (`method:ace-moe-peft`, UbiquitousAILab/ACE). No CISPO / Muon2 / OPD / OPSA / CANOPY retarget.
- Added method:verpo (2609.06100), method:rpb (2609.08115), method:rlvr-group-correlation (2609.06386), method:opsd-collapse-review (2608.25936). WATCH skipped: FEE EnvAsScaffold 2609.08404. AnLR-LoRA / MoE HP scaling / AF1 / DataFlex-RL already landed in the first commit.
- Scope checks: VISTA remains privileged-teacher first hop; SAPO remains MoE/VL RLVR; CISPO remains Pass@1.

### 2026-09-09 — ingest method:verpo (active; does not supersede method:vista / method:cispo)
- Added paper:verpo (2609.06100), method:verpo, recipe:verpo (stub; no official code). Wired to task:privileged-teacher-opsd; mention on task:math-code-rl-dense.
- Status active. Privileged evidence as a proposal (Fisher contrast + ZPD gate) on an outcome objective.
- Evidence: five scientific/tool tasks, best-variant averages Qwen3-4B 0.6857 vs 0.6826, Qwen3-8B 0.7058 vs 0.6895, Llama-3.2-1B 0.5657 vs 0.4751 (arXiv:2609.06100); verified: true; evidence_level: preprint.
- Scope checks: VISTA remains privileged-teacher SOTA; CISPO remains Pass@1.

### 2026-09-09 — ingest method:rpb (active MoE routing candidate; does not supersede method:sapo)
- Added paper:rpb (2609.08115), method:rpb, recipe:rpb. Wired to task:math-code-rl-moe. Claimed GitHub naver-ai/rpb was 404 at ingest.
- Status active. Soft router anchoring vs re-applied LBL or unanchored FT.
- Evidence: Moonlight-16B-A3B in-domain 45.77 vs LBL 31.91 vs unanchored 29.44 (arXiv:2609.08115); verified: true; evidence_level: preprint.
- Scope checks: SAPO remains MoE/VL current_sota.

### 2026-09-09 — ingest method:rlvr-group-correlation (niche analysis; does not supersede method:cispo)
- Added paper:rlvr-group-correlation (2609.06386), method:rlvr-group-correlation, recipe:rlvr-group-correlation. Code: ethxin0011/rlvr_group_correlation. Wired as gotcha on task:math-code-rl-dense / method:grpo / method:cispo.
- Status niche. Within-group verifier-error ICC, not an optimizer.
- Evidence: ρ=0.530 [0.500, 0.560] on 24,998 k=8 groups; Kish n_eff=1.70; advantage-sign disagreement ≤0.83% (arXiv:2609.06386); verified: true; evidence_level: preprint.
- Scope checks: CISPO remains Pass@1; sibling gotcha remains paper:spurious-advantage-grpo.

### 2026-09-09 — ingest method:opsd-collapse-review (niche playbook; does not supersede method:vista / method:opsa / method:cispo)
- Added paper:opsd-collapse-review (2608.25936), method:opsd-collapse-review, recipe:opsd-collapse-review (no code). Wired to task:privileged-teacher-opsd and task:teacher-free-on-policy-self-adaptation.
- Status niche. Three levers for OPSD collapse (where / what / when). Survey; no new experiments.
- Evidence: structural review only (arXiv:2608.25936); verified: true; evidence_level: preprint.
- Scope checks: VISTA / OPSA / CISPO first hops unchanged.

### 2026-09-09 — OPRD recipe code pointer (method:oprd already ingested)
- Set recipe:oprd repo_url to https://github.com/raymin0223/on_policy_reverse_distillation. Repo is an early stub at ingest; algorithm snippet unchanged. Does not retarget OPD or CISPO.

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
