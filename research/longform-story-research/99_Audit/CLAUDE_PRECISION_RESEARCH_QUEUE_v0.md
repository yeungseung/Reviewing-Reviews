# CLAUDE PRECISION RESEARCH QUEUE v0

> Status: PROVISIONAL EXECUTION PLAN  
> Input: Evidence Coverage Matrix v0 + Audit Log + Research Map v2 Draft  
> Goal: convert the Gemini reconnaissance corpus into a smaller, reliable, testable Story Engine knowledge base.

# 0. Core rule

Claude must **not** continue the old 86-item / 257-Theme queue mechanically.

The current corpus is reconnaissance.

The next phase is precision research.

Every task must distinguish:

1. source identity
2. mechanism evidence
3. direct narrative/media evidence
4. cross-domain bridge evidence
5. quantitative evidence
6. platform evidence
7. Story Engine application
8. remaining uncertainty

A useful mechanism may survive even if:
- a DOI is wrong
- the stored N is wrong
- an effect size is wrong
- a Report formula is unsupported

The task is not to destroy the old corpus.
The task is to **salvage what is real and isolate what was invented.**

---

# 1. Mandatory Claude research process

Each research task must execute in this order.

## Step 1 — Define the construct
- exact term
- competing definitions
- neighboring concepts that must not be conflated

## Step 2 — Verify source identity
For every important source:
- exact title
- authors
- year
- venue
- DOI / stable URL
- source type

If bibliographic identity is unresolved:
- mark UNVERIFIED
- do not extract quantitative claims

## Step 3 — Classify evidence type
Allowed labels:
- META_ANALYSIS
- SYSTEMATIC_REVIEW
- EXPERIMENT
- OBSERVATIONAL
- LONGITUDINAL
- FIELD_STUDY
- REVIEW
- THEORY
- BOOK / CRAFT
- PLATFORM_DATA
- OTHER

Do not call a review or theory paper an experiment.

## Step 4 — Extract only traceable claims
For each claim:
- population
- sample
- manipulation/exposure
- outcome
- effect size if reported
- uncertainty/statistical significance if reported
- exact source location where feasible

Never synthesize a percentage not reported by a source.

## Step 5 — Search counterevidence
Required:
- failures
- null effects
- moderation
- boundary conditions
- alternative explanations

## Step 6 — Separate evidence layers

### Layer A — Direct
Tested in:
- story
- narrative
- film
- television
- video
- reading narrative
- comparable longform media

### Layer B — Bridge
Tested in another domain but theoretically relevant.

### Layer C — Application hypothesis
Story Engine proposal derived from A/B.

Layer C must never be written as if it were Layer A.

## Step 7 — Quantitative calibration
Every numeric rule must be one of:
- VERIFIED_DIRECT
- VERIFIED_BRIDGE
- OBSERVATIONAL_PLATFORM
- TUNABLE_PRIOR
- UNSUPPORTED

## Step 8 — Story Engine implication
Only after Steps 1–7.

Output:
- what mechanism appears reliable
- what the engine may represent
- what the engine should **not** hard-code
- what still needs direct validation

---

# 2. Required output schema per research task

```yaml
research_id:
construct:
research_question:

bibliographic_status:
  verified_sources: []
  corrected_sources: []
  unresolved_sources: []
  rejected_sources: []

evidence_summary:
  direct_story_media:
  bridge_evidence:
  counterevidence:
  boundary_conditions:

confidence:
  source_integrity:
  mechanism_support:
  direct_story_media_support:
  quantitative_support:
  domain_transfer:
  platform_support:

story_engine:
  candidate_state_variables: []
  candidate_rules: []
  tunable_priors: []
  reject_or_remove: []
  unresolved_questions: []

recommended_status:
  - VERIFIED_MECHANISM
  - DIRECT_STORY_EVIDENCE
  - BRIDGE_HYPOTHESIS
  - DESIGN_HEURISTIC
  - TUNABLE_PRIOR
  - UNSUPPORTED_QUANTIFICATION
  - REJECTED
```

---

# 3. Priority logic from Coverage Matrix v0

The Matrix shows:

- A Epistemic Integrity: **5 / 18**
- B Audience Model Construction: **17 / 17**
- C Uncertainty / Curiosity / Narrative Expectation: **24 / 24**
- D Appraisal / Emotion / Value: **39 / 42**
- E Relevance / Scale: **16 / 16**
- F Processing Capacity & Information: **15 / 15**
- G Visual / Multimodal: **9 / 9**
- H Resolution / Payoff / Ending: **10 / 10**
- I Packaging / Platform Contract: **0 / 12**
- J Design Architecture & Instruments: **27 / 61**
- K Empirical Story Engine Validation: **0 / 12**
- L Final Synthesis: **3 / 21**

Interpretation:

High completion does **not** mean "finished."

B/C/F are fully researched in the old taxonomy but contain major:
- construct conflation
- quantification injection
- domain transfer

A/K are under-researched but structurally necessary.

Therefore research order is based on:
**centrality × uncertainty × transfer risk × audit exposure × product need**

not raw Theme completion.

---

# 4. WAVE 0 — Source reconstruction

Priority: **CRITICAL**

Before mechanism synthesis, repair the most important broken source records.

## Q0-01 — Emotional Flow source reconstruction
Targets:
- Nabi 2015
- McAllister-related record

Questions:
- exact paper/document identity
- theoretical vs empirical status
- actual samples/methods
- what emotional-flow claims are directly supported

## Q0-02 — Event segmentation / memory source reconstruction
Targets:
- Swallow/Zacks mixed record
- event-memory papers attached to #45

Goal:
separate:
- event boundary
- prediction error
- memory updating
- later recognition
- longform extrapolation

## Q0-03 — QUEST reconstruction
Targets:
- Graesser / QUEST records

Goal:
identify specific publications and remove conflated DOI/title/venue combinations.

## Q0-04 — Credibility / closure / visual DOI repair
Targets:
- Fogg PIT
- Carroll Narrative Closure
- Groves & Thompson
- Slovic psychic numbing
- Annie Lang visual editing source
- Sinclair 2021 author metadata

Output of Wave 0:
three lists:

### VERIFIED SEED
High-confidence sources allowed as Claude starting points.

### INTERESTING / UNVERIFIED
May guide search, not support conclusions.

### NEGATIVE LIST
Known bad bibliographic combinations / unsupported claims that must not be recycled.

---

# 5. WAVE 1 — Epistemic Integrity

Coverage:
**5 / 18**

Priority:
**P1 — FIRST NEW RESEARCH**

This Track is the clearest structural weakness in the corpus.

## Q1-01 — Evidence taxonomy

Legacy:
#60

Research:
- primary vs secondary
- fact vs interpretation
- anecdote vs population evidence
- causal vs correlational
- inference vs observation
- review/comment/opinion
- forecast/projection

Story Engine goal:
create evidence labels used by all nonfiction scripts.

## Q1-02 — Confidence / uncertainty language

Research:
- calibrated uncertainty
- communicating scientific uncertainty
- risk communication
- confidence intervals
- ambiguity
- trust effects

Story Engine goal:
separate:
- known
- probable
- disputed
- inferred
- unknown

## Q1-03 — Emotional framing and factual judgment

Legacy:
#61

Research separately:
1. empirical framing effects
2. misinformation/selective framing
3. normative journalism/documentary standards

Do not merge ethics and effect size.

## Q1-04 — Counterevidence and alternative explanations

Legacy:
#62–#63

Research:
- two-sided messages
- inoculation
- counterargument
- competing causal explanations
- confirmation bias
- false balance
- motivated reasoning

Candidate output:
**Epistemic Counterpoint Module**

## Q1-05 — Source monitoring / correction

Legacy:
#59 + #60

Research:
- continued influence effect
- correction
- alternative explanations
- source memory
- visual source monitoring
- archive vs reenactment vs stock vs synthetic media

## Q1-06 — Vivid example vs representative evidence

Bridge:
A + E

Research:
- identifiable example
- anecdotal bias
- representativeness
- scope neglect
- base rates

Story Engine goal:
prevent "one emotional case" from silently replacing the dataset.

---

# 6. WAVE 2 — Core cognitive mechanisms

Priority:
**P1**

These appear to be the strongest parent-mechanism candidates.

## Q2-01 — Active causal model construction

Track:
B

Current state:
multiple independent research families survive audit.

Research:
- causal coherence
- causal centrality
- goal inference
- local/global coherence
- situation models
- narrative inference

Do not ask:
"Is Causal Spine correct?"

Ask:
"What established mechanisms explain how audiences build causal and goal-based representations of narrative events?"

Expected Story Engine output:
candidate representation for:
- cause
- goal
- obstacle
- consequence
- unresolved causal gap

## Q2-02 — Event / state updating

Track:
B

Research:
- event segmentation
- event boundaries
- event-index dimensions
- situation model updating
- memory consequences

Do not validate:
- fixed chapter length
- fixed 2-state-change threshold
- 2.4x memory
- 79% continuation

Expected output:
which types of change should the Engine track as state updates.

## Q2-03 — Appraisal → emotion

Track:
D

Research:
- agency
- goal relevance
- certainty
- coping/control
- legitimacy/norm
- situational meaning

Then search separately:
- narrative/media evidence

Expected output:
emotion should be represented as consequence of appraisal/state, not as a manually assigned label.

## Q2-04 — Capacity-limited processing

Track:
F

Research:
- encoding
- storage
- retrieval
- working memory
- media-processing models
- multimedia load
- modality competition
- segmentation

Expected output:
directional constraints.

Do not produce:
- universal seconds
- universal density
- universal ratio

---

# 7. WAVE 3 — Narrative expectation

Track:
C

Priority:
**P1**

The old Prediction Engine must remain split.

## Q3-01 — Narrative suspense

Prioritize direct narrative experiments.

Research:
- restricted solution paths
- outcome concern
- known ending
- rereading/repeated suspense
- character goals

## Q3-02 — Curiosity vs suspense vs surprise

Construct separation required.

Questions:
- unknown outcome
- known outcome / unknown path
- missing information
- event-order manipulation
- surprise after occurrence

## Q3-03 — Prospective narrative inference

Research:
- forward inference
- goal prediction
- expectation strength
- expertise/genre schemas

## Q3-04 — Foreshadowing and fair surprise

Research:
- clue visibility
- retrospectively coherent reveal
- perceived fairness
- schema violation
- surprise vs arbitrariness

## Q3-05 — Mnemonic prediction error

Start from:
Sinclair et al. 2021

Research:
- familiar narrative predictions
- hippocampal representation disruption
- memory updating

Do not interpret as:
dopamine pleasure.

## Q3-06 — Reward prediction error bridge

Goal:
determine whether narrative outcomes actually map to RPE under relevant conditions.

Required:
human entertainment/music/game/narrative bridge evidence.

Schultz primate work alone is insufficient.

## Q3-07 — Predictive processing / FEP boundary

Goal:
decide what FEP legitimately contributes.

Likely status:
theoretical background, not direct audience-retention evidence.

---

# 8. WAVE 4 — Processing / information precision

Track:
F

Priority:
**P1**

Coverage is high but audit exposure is also high.

## Q4-01 — Information density

Research:
- processing load
- structural complexity
- narration
- visual complexity

Goal:
derive variables, not seconds.

## Q4-02 — Segmentation

Research:
- learner-controlled vs system-controlled
- multimedia segmentation
- video segmentation

Goal:
determine which conditions make segmentation helpful.

## Q4-03 — Information + emotion interaction

Research:
- affect and encoding
- mood and judgment
- emotional salience
- attentional capture
- central/peripheral memory

## Q4-04 — Modality competition

Research:
- narration + text
- narration + visual
- music + speech
- split attention
- redundancy

Goal:
what conflicts, under what conditions.

---

# 9. WAVE 5 — Empirical Story Engine infrastructure

Track:
K

Coverage:
**0 / 12**

Priority:
**P1-product**

Do not wait until the very end.

## Q5-01 — Analysis Log schema

Legacy:
#84

Required content annotations:
- state change
- active question
- expectation
- causal reveal
- appraisal change
- emotion
- judgment
- stakes/relevance
- evidence type
- visual function
- payoff/closure

## Q5-02 — Timing annotation

For every event:
- start
- end
- duration
- distance since prior update
- chapter position

## Q5-03 — Audience outcomes

Where available:
- retention
- skip
- replay
- click
- continuation
- comments
- search/discovery

## Q5-04 — Confounds

Track:
- topic strength
- celebrity/product/song strength
- source quality
- channel baseline
- duration
- upload timing
- audience segment

## Q5-05 — Engine prior update

Convert rules like:
- 60–90 sec
- 4–8 sec cuts
- 3–5 min ending
- 70:30
- 80:20

into:

```
prior:
observed_range:
genre:
audience:
confidence:
data_source:
last_update:
```

These should become tunable parameters, not research dogma.

---

# 10. WAVE 6 — Instrument validation

Track:
J

Coverage:
**27 / 61**

Priority:
**P1-method**

Do not ask academia to "prove" a worksheet.

## Q6-01 — Tension Engine taxonomy

Legacy:
#6

Validate:
- coverage
- overlap
- missing types
- inter-rater agreement

## Q6-02 — Opening Engine taxonomy

Legacy:
#18

Same validation method.

## Q6-03 — Reversal taxonomy

Legacy:
#33

Test whether categories are:
- mutually distinguishable
- useful in coding
- predictive of audience interpretation

## Q6-04 — Payoff taxonomy

Legacy:
#51

Current nine types mix dimensions.

Test:
- overlap
- missing categories
- multi-label structure

## Q6-05 — Story Design Sheet

Legacy:
#69–#70

Measure:
- completion time
- redundant fields
- missing fields
- revision usefulness
- expert consistency

## Q6-06 — Audience State Tracking Map

Merge candidate:
#71
#73
#74
#75

Candidate state variables:
- belief/model
- question
- prediction
- appraisal
- emotion
- judgment
- goal/risk
- relevance
- uncertainty

Validate:
whether multiple reviewers can annotate the same script consistently.

## Q6-07 — Anti-pattern registry

Legacy:
#80

Every anti-pattern should indicate:
- experiment-backed
- observational
- craft heuristic
- internal lesson

---

# 11. WAVE 7 — Targeted bridge repair

Priority:
**P2**

## Q7-01 — Relevance / Human Scale

Track:
E

Separate:
- identifiable person
- psychological distance
- psychic numbing
- risk perception
- self relevance

Need direct narrative/media bridge evidence.

## Q7-02 — Media-specific adaptation

Track:
D

Search specifically for:
- within-session emotional habituation
- film/video
- repeated affective cues
- recovery/contrast

Goal:
see whether any practical time-scale findings exist.

## Q7-03 — Narrative payoff / ending

Track:
H

Separate:
- closure
- retrospective evaluation
- promise fulfillment
- ending emotion
- open ending
- moral/actionable resolution

## Q7-04 — Visual / multimodal

Track:
G

Reconstruct:
- edit/resource allocation
- gaze
- multimedia comprehension
- affective film form
- provenance

Do not preserve existing hard timing constants unless independently supported.

---

# 12. WAVE 8 — Packaging / Platform Contract

Track:
I

Coverage:
**0 / 12**

Priority:
**P2 after engine feature definitions stabilize**

Use two evidence lanes.

## Lane 1 — Platform
Need actual:
- thumbnail/title A/B
- CTR
- opening retention
- continuation
- satisfaction
- rewatch
- subscription

## Lane 2 — Psychology
Need:
- expectation
- congruence
- trust
- disappointment
- deception
- curiosity

Hard rule:
Lane 2 cannot manufacture Lane 1 percentages.

Candidate parent model:

```
PRE-CLICK PROMISE
      ↓
OPENING CONFIRMATION
      ↓
NARRATIVE DELIVERY
      ↓
PAYOFF FIDELITY
      ↓
SATISFACTION / TRUST
```

---

# 13. WAVE 9 — Final synthesis

Track:
L

Coverage:
**3 / 21**

Status:
**HOLD**

Do not produce final principles until:
- A evidence rules exist
- B/C/D/F core mechanisms are recalibrated
- K empirical validation pipeline exists
- J tools are validated
- I platform evidence is separated from psychology

Final outputs:
1. Core Mechanisms
2. Optional Modules
3. Directional Rules
4. Quantitative/Tunable Priors
5. Instrument Layer
6. Evidence/Trust Layer
7. Platform Layer
8. Confidence model
9. Master Engine v3
10. final one-sentence model

---

# 14. Immediate Claude batch

If only one Claude research batch is launched next, use exactly this order:

1. **Q1-01 Evidence taxonomy**
2. **Q1-04 Counterevidence and alternative explanations**
3. **Q1-05 Source monitoring / correction**
4. **Q2-01 Active causal model construction**
5. **Q2-02 Event / state updating**
6. **Q2-03 Appraisal → emotion**
7. **Q2-04 Capacity-limited processing**
8. **Q3-01 Narrative suspense**
9. **Q3-02 Curiosity vs suspense vs surprise**
10. **Q3-05 Mnemonic prediction error**

Why this order:

- 1–3 repair the research system's epistemic foundation
- 4–7 test the strongest candidate parent mechanisms
- 8–10 replace the current conflated Prediction Engine with direct narrative evidence

---

# 15. Stop conditions

Claude should stop and flag a task instead of forcing a conclusion when:

- the cited source cannot be located
- DOI/title/author identity conflicts
- only secondary summaries are available for a key quantitative claim
- direct narrative evidence does not exist
- a mechanism can only be supported by distant-domain analogy
- evidence is meaningfully mixed
- the requested number/timing is not established

Allowed output:
**INSUFFICIENT EVIDENCE**

This is a successful research result, not a failure.

---

# 16. Success criterion

The goal is not to maximize the number of "Strong Support" findings.

The goal is to leave the Story Engine with fewer but better rules.

A successful next-stage corpus should contain statements like:

> Event-model updating is well supported in cognitive/narrative research, but no universal chapter interval is established.

rather than:

> Every 8–12 minutes, force a two-variable state change to increase retention by 79%.

The former can become a real adaptive Story Engine.
The latter is a brittle pseudo-formula.
