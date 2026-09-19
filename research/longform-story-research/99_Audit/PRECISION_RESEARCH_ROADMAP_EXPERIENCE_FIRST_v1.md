# PRECISION RESEARCH ROADMAP — EXPERIENCE-FIRST v1

> Status: APPROVED — P0 ACTIVE / E1-01 COMPLETE / E1-02 COMPLETE FOR REVIEW  
> Purpose: redirect Precision Research from evidence-system expansion toward Story State, State Transition, and Story Decision support.  
> Constraint: no new large Precision Research begins from this roadmap until user approval.

---

# 0. Product objective

The project is not building an academic evidence framework.

The product is a Story Engine that helps a frontier model decide:

1. what the audience currently knows, expects, feels, and is trying to resolve,
2. what experience should come next,
3. whether that transition is psychologically and causally plausible,
4. what information should be revealed, delayed, emphasized, contrasted, or withheld,
5. what facts and causal constraints must remain invariant,
6. what Story State should follow.

Core unit:

**STATE → TRANSITION → NEXT STATE**

Research exists to improve that decision.

---

# 1. Evidence layer repositioning

Q1-01 is preserved, but removed from the main research spine.

New role:

**Evidence Firewall / Research Integrity Layer**

Runtime core should consume only a minimal research-confidence payload such as:

```yaml
evidence_quality:
  confidence:
  directness:
  causal_status:
  population_or_domain:
  important_limits:
  source_independence:
```

Detailed evidence taxonomy/source ledger remains available offline for research auditing.

Do not continue expanding:
- universal evidence taxonomy
- exhaustive provenance enums
- annotation science
- GRADE/Cochrane recreation
- evidence-methodology research for its own sake

Source reconstruction becomes **on-demand repair** only when a source is important to an active Story Mechanism.

---

# 2. New prioritization test

Every future research task must answer:

> Does this research directly improve Story Engine judgment about audience state, state transition, information control, causal coherence, or experience design?

Classification:

- **KEEP** — directly supports Story State/Transition decisions
- **MODIFY** — useful, but research question must be rewritten around state/transition decisions
- **MERGE** — better handled as part of another mechanism
- **DEFER** — useful later for implementation/validation/expression
- **DROP** — low product value for current Story Engine core

---

# 3. Current Q-list reclassification

## WAVE 0 — Source reconstruction

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q0-01 | Emotional Flow source reconstruction | DEFER / ON-DEMAND | Repair only when emotional-transition research depends on the source |
| Q0-02 | Event segmentation / memory reconstruction | MODIFY → support State Updating research | Directly relevant to event/state transitions; repair only necessary seed sources |
| Q0-03 | QUEST reconstruction | MODIFY → support Causal Model research | Useful only insofar as it clarifies causal/question-model mechanisms |
| Q0-04 | Credibility/closure/visual DOI repair | DEFER / ON-DEMAND | Mixed targets; no longer a standalone wave |

**Decision:** abolish WAVE 0 as a mandatory precondition.  
Source repair becomes a local gate inside active mechanism research.

---

## WAVE 1 — Epistemic Integrity

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q1-01 | Evidence taxonomy | KEEP AS FIREWALL — COMPLETE | Useful protection layer, not engine core |
| Q1-02 | Confidence / uncertainty language | DEFER / MINIMAL MERGE | Only enough to prevent overstatement; no full language-calibration research now |
| Q1-03 | Emotional framing & factual judgment | MODIFY / MERGE | Move empirical emotional-framing effects into Appraisal/Judgment; keep factual distortion as firewall |
| Q1-04 | Counterevidence / alternative explanations | MODIFY / MERGE | Alternative causal models belong in Causal Model / Reframe research, not an independent epistemology project |
| Q1-05 | Source monitoring / correction | DEFER | Research only when provenance/correction becomes a direct story-state need |
| Q1-06 | Vivid example vs representative evidence | MODIFY → Relevance / Human Scale | Strong direct connection to salience, empathy, scope, judgment |

**Decision:** Track A is no longer the first new-research wave.

---

## WAVE 2 — Core cognitive mechanisms

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q2-01 | Active causal model construction | KEEP — P0 | Central to what audience believes happened and why |
| Q2-02 | Event / state updating | KEEP — P0 | Directly defines State and Transition |
| Q2-03 | Appraisal → emotion | KEEP — P0 | Central bridge from meaning/state change to experience change |
| Q2-04 | Capacity-limited processing | KEEP — P0 #7 | Cross-cutting constraint on what can be processed at a state |

**Decision:** this becomes the new starting research wave.

---

## WAVE 3 — Narrative expectation

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q3-01 | Narrative suspense | KEEP — P1 | Directly models tension under unresolved outcomes |
| Q3-02 | Curiosity vs suspense vs surprise | MODIFY → Uncertainty / Expectation Transition | Research as different state-transition patterns rather than dictionary definitions |
| Q3-03 | Prospective narrative inference | MERGE with Q2-01/Q2-02 + expectation research | Prediction follows current causal/goal model |
| Q3-04 | Foreshadowing and fair surprise | KEEP/MODIFY | Study conditions for expectation violation that remains retrospectively coherent |
| Q3-05 | Mnemonic prediction error | DEFER / MERGE | Useful for memory updating, but secondary to immediate Story State decisions |
| Q3-06 | Reward prediction error bridge | DEFER FROM CORE | Too distant unless a genuine reward/value transition is being modeled |
| Q3-07 | Predictive processing / FEP boundary | DROP FROM ACTIVE ROADMAP | Theoretical background has low direct product value |

---

## WAVE 4 — Processing / information precision

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q4-01 | Information density | KEEP/MODIFY — P1 | Reframe as state-dependent processing constraint |
| Q4-02 | Segmentation | MERGE with Event/State Updating + Capacity | Useful when segmentation corresponds to meaningful model change |
| Q4-03 | Information + emotion interaction | KEEP — P1 | Directly affects reveal timing and experience-state management |
| Q4-04 | Modality competition | DEFER TO EXPRESSION LAYER | Voice/visual/text implementation, not medium-independent core |

---

## WAVE 5 — Empirical infrastructure

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q5-01 | Analysis Log schema | MODIFY → Story State / Decision Log | Keep minimal product loop; do not turn into annotation science |
| Q5-02 | Timing annotation | DEFER | Timing is later empirical prior, not core research target |
| Q5-03 | Audience outcomes | DEFER / SECONDARY | Useful feedback, but not Story Engine objective function |
| Q5-04 | Confounds | DEFER / MINIMAL | Add only when testing a concrete engine hypothesis |
| Q5-05 | Engine prior update | KEEP LATER | Useful once actual content evidence exists |

---

## WAVE 6 — Instrument validation

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q6-01 | Tension taxonomy | DEFER | Do not validate taxonomy before transition mechanisms are understood |
| Q6-02 | Opening taxonomy | DEFER | Opening is a use case of state/expectation mechanisms |
| Q6-03 | Reversal taxonomy | DEFER / MERGE with Reframe | Reversal should emerge from belief/model update research |
| Q6-04 | Payoff taxonomy | DEFER / MERGE with Resolution | Taxonomy is instrument, not core mechanism |
| Q6-05 | Story Design Sheet | DEFER | Product UI after state model stabilizes |
| Q6-06 | Audience State Tracking Map | MODIFY / PROMOTE AS DESIGN OUTPUT | Important as engine representation, but not as inter-rater research project |
| Q6-07 | Anti-pattern registry | DEFER | Build from mechanism failure conditions later |

---

## WAVE 7 — Targeted bridge repair

| Q | Existing task | New disposition | Reason |
|---|---|---|---|
| Q7-01 | Relevance / Human Scale | KEEP — P1/P2 | Changes stakes, empathy, psychological distance, judgment |
| Q7-02 | Media-specific adaptation | MODIFY → Repetition / Adaptation / Contrast | Core question is response change under repeated/sustained state, not media timing |
| Q7-03 | Narrative payoff / ending | KEEP/MODIFY — P1 | Reframe as resolution, closure, expectation fulfillment, open-state transformation |
| Q7-04 | Visual / multimodal | DEFER TO EXPRESSION LAYER | Important later, but not core medium-independent state engine |

---

## WAVE 8 — Packaging / Platform Contract

Disposition: **DEFER AS APPLICATION LAYER**

Packaging affects pre-story expectation and trust, but CTR/retention optimization is not the Story Engine’s primary objective.

Keep only the medium-independent concept:

**pre-experience expectation → delivered experience → fulfillment/violation → satisfaction/trust**

Platform-specific thumbnail/title/CTR research moves later.

---

## WAVE 9 — Final synthesis

Disposition: **HOLD**

No final engine compression until the experience-transition mechanism map stabilizes.

---

# 4. New Experience-First research spine

The new roadmap is organized around the decisions the engine must make, not around academic disciplines.

## PHASE E0 — Evidence Firewall

Status: mostly complete with Q1-01.

Purpose:
Prevent unsupported upgrades from entering the mechanism library.

No further broad evidence-system research.

---

## PHASE E1 — Audience Model & Story State Foundation

### Foundation Pair

E1-01 and E1-02 are separate research tasks but must be treated as one Story Engine **Foundation Pair**:

- **E1-01 — Causal + Goal Model Construction**: what causal/goal model the audience currently holds
- **E1-02 — Event / State Updating**: when incoming change causes that model/state to update

E1-01 must not absorb E1-02, but every E1-01 result should identify handoff points to E1-02.

### Foundation State Separation

All later Story State research must keep three layers distinct:

```text
A. Canonical / World State
   What is actually true in the story world

B. Character State
   What a character actually knows, believes, wants, intends, and is constrained by

C. Audience Model
   What the audience knows, believes, and infers about causes, goals, intentions, and consequences
```

Hard distinctions:

```text
Audience inference ≠ Story fact
Audience belief about character ≠ Character actual belief
Character desire ≠ Character intention
Known information ≠ Currently active information
Known information ≠ Currently causally relevant information
```

Candidate accessibility states such as unknown / known-but-dormant / active / causally-relevant / reactivated / suppressed remain provisional and must be refined by E1-02 rather than frozen now.


### E1-01 — Causal + Goal Model Construction
Former:
- Q2-01
- parts of Q0-03
- Q3-03

Research decision target:

> What does the audience currently believe caused what, who wants what, and what causal/goal gaps remain?

Outputs should support:
- cause
- consequence
- actor/agent
- goal
- obstacle
- dependency
- unresolved causal gap

---

### E1-02 — Event / State Updating
Former:
- Q2-02
- Q4-02
- parts of Q0-02

Research decision target:

> What kinds of change make the audience update its current model of the situation?

Candidate state dimensions:
- goal
- cause
- agent
- location/context
- risk
- relationship
- knowledge
- value/meaning
- control
- outcome probability

No fixed number of state variables or timing rule.

---

### E1-03 — Appraisal → Emotion / Judgment Update
Former:
- Q2-03
- empirical portion of Q1-03

Research decision target:

> Given the current facts and audience model, what appraisal change can plausibly move emotion/judgment from state A to state B?

Candidate appraisal variables:
- goal relevance
- agency/responsibility
- certainty
- controllability/coping
- legitimacy/fairness
- expected outcome
- meaning/value

This is one of the central transition mechanisms.

---

### E1-04 — Processing Capacity as State Constraint

Priority: **P0 #7**
Former:
- Q2-04
- Q4-01
- Q4-02

Research decision target:

> Given current cognitive/emotional load, how much new information or structural change can be processed without losing the active model?

This should produce directional constraints, not seconds or ratios.

---

# 5. PHASE E2 — Uncertainty, Expectation & Information Control

## E2-01 — Information Gap / Curiosity Transition
Former:
- C1
- Q3-02 curiosity portion

Decision target:

> When does missing information create a useful open question rather than confusion or indifference?

Needed outputs:
- preconditions
- information-gap clarity
- relevance
- resolvability
- load sensitivity
- failure conditions

---

## E2-02 — Narrative Expectation / Suspense
Former:
- Q3-01
- Q3-03 relevant portion

Decision target:

> When an outcome matters but is unresolved, what conditions maintain or increase tension/suspense?

Track:
- outcome concern
- solution paths
- character goals
- known outcome / unknown path
- uncertainty level

---

## E2-03 — Expectation Violation → Surprise → Reappraisal / Reframe
Former:
- Q3-04
- B3
- parts of Q1-04

Decision target:

> When incoming information violates an existing expectation, under what conditions does that violation produce surprise and lead to reappraisal/reframe?

Do not presuppose fair/unfair. Perceived fairness, arbitrariness, coherence, and audience judgment are Boundary / Failure outcomes to be investigated.

Research:
- cue visibility
- causal compatibility
- retrospective coherence
- prior belief strength
- responsibility/meaning update

---

## E2-04 — Information Reveal / Delay / Partial Resolution
Derived from:
- C3 Open Question lifecycle
- Q3-02
- Q7-03

Decision target:

> Should the next information unit be revealed now, withheld, partially revealed, or used to transform the active question?

This is a direct Story Decision mechanism.

---

# 6. PHASE E3 — Experience Regulation & Emotional Dynamics

## E3-01 — Tension / Arousal / Relief Transition
Research target:

> How does perceived threat, safety, control, uncertainty, and outcome proximity shift tension and relief?

Focus on transition relations:
- stability → unease
- unease → tension
- tension → relief
- relief → renewed tension

Do not prescribe fixed sensory devices.

---

## E3-02 — Repetition / Habituation / Adaptation / Contrast
Former:
- Q7-02
- D5

Decision target:

> When does maintaining the same experience strengthen it, and when does repetition reduce responsiveness or create fatigue?

Research:
- repetition
- novelty
- contrast
- recovery
- context change
- escalation limits

No universal timing constants.

---

## E3-03 — Emotional Carryover / Mixed States / Contrast
Derived from:
- D4
- Q4-03
- parts of D5

Decision target:

> How does the previous emotional state alter the next appraisal and possible transition?

Examples:
- fear → relief
- hope → disappointment
- sadness → bittersweet satisfaction
- anger → empathy after responsibility reappraisal

---

## E3-04 — Stakes / Relevance / Empathy / Distance
Former:
- Q7-01
- Q1-06
- Track E

Decision target:

> What makes the current unresolved outcome matter to this audience at this moment?

Research:
- self relevance
- human consequence
- psychological distance
- scale
- identifiability
- risk perception

Guard:
more emotional salience does not automatically mean more accurate judgment.

---

# 7. PHASE E4 — Resolution, Closure & Post-Update State

## E4-01 — Closure / Unfinished State
Former:
- Q7-03
- H1
- C3

Decision target:

> Which unresolved questions/causal gaps/goals must close, and which may remain open without producing a broken experience?

---

## E4-02 — Expectation Fulfillment / Disconfirmation
Former:
- H2
- medium-independent part of Packaging Contract

Decision target:

> How does delivering, reframing, exceeding, or violating an established expectation alter satisfaction and trust?

---

## E4-03 — Retrospective Re-evaluation / Ending State
Former:
- H3/H4

Decision target:

> How does the final update change the audience’s interpretation of the whole preceding experience?

This includes:
- reframe
- final emotion
- open ending
- ambiguity
- meaning consolidation

Peak-end is bridge evidence, not a universal law.

---

# 8. PHASE E5 — Engine Representation & Feedback

This phase is product engineering, not a major academic research program.

## E5-01 — Minimal Story State representation

Candidate fields, to be refined from E1–E4 research:

```yaml
story_state:
  factual_constraints:
    known:
    unresolved:

  character_model:
    goals:
    constraints:
    knowledge:

  audience_model:
    known:
    believed:
    expected:
    open_questions:

  experience_state:
    emotion:
    arousal:
    tension:
    curiosity:
    uncertainty:
    cognitive_load:

  narrative_state:
    active_purpose:
    unresolved_causality:
    open_loops:
    required_future_information:

  possible_next_moves:
    maintain:
    intensify:
    reduce:
    contrast:
    transition:
```

This is a working representation, not a fixed ontology.

---

## E5-02 — Story Decision record

For each important step:

```yaml
current_state:
candidate_experience:
required_transition:
supporting_mechanisms:
conditions:
risks:
facts_that_must_not_change:
information_action:
  reveal:
  delay:
  partially_reveal:
  emphasize:
next_state:
confidence:
```

Purpose:
Make the model’s decision context explicit without forcing deterministic output.

---

## E5-03 — Feedback / priors later

Real content data can later adjust:
- timing priors
- genre priors
- transition strength
- audience-specific priors

But these are empirical tuning inputs, not the core theory of storytelling.

---

# 9. Medium-independent Core vs Expression Layers

## Core

Research first:

- causal/goal model
- event/state update
- appraisal
- emotion/judgment
- uncertainty
- expectation
- curiosity
- tension
- relief
- relevance/stakes
- adaptation/contrast
- processing capacity
- closure/reframe

## Expression Layer — later

Text:
- wording
- sentence rhythm
- lexical choice

Voice:
- prosody
- pause
- intensity
- vocal emotion

Visual:
- shot scale
- edit
- gaze
- motion
- evidence visual

Sound/Music:
- musical tension
- release
- contrast
- motif

Platform:
- packaging
- CTR
- retention
- thumbnail/title conventions

Core should specify **desired experience and constraints**; expression layers choose implementation.

---

# 10. New priority order

## P0 — Research first

1. **E1-01 Causal + Goal Model Construction**
2. **E1-02 Event / State Updating**
3. **E1-03 Appraisal → Emotion / Judgment**
4. **E2-01 Information Gap / Curiosity**
5. **E2-02 Narrative Expectation / Suspense**
6. **E2-03 Expectation Violation → Surprise → Reappraisal / Reframe**
7. **E1-04 Processing Capacity**

These define the minimum dynamic Story State engine.

## P1 — Next

8. **E3-01 Tension / Relief**
9. **E3-02 Adaptation / Repetition / Contrast**
10. **E3-04 Relevance / Stakes / Human Scale**
11. **E2-04 Reveal / Delay / Partial Resolution**
12. **E4-01 Closure / Unfinished State**
13. **E4-02 Expectation Fulfillment**
14. **E3-03 Emotional Carryover / Mixed States**

## P2 — After core stabilizes

15. **E4-03 Ending / Retrospective Re-evaluation**
16. Minimal Story State representation
17. Story Decision record
18. empirical priors / feedback loop

## DEFERRED APPLICATION LAYERS

- visual/multimodal craft
- voice/TTS
- music/sound
- platform packaging/CTR
- taxonomy/instrument validation
- detailed annotation reliability
- exact timing/ratio optimization

---

# 11. Revised research output contract

Every new Precision Research should attempt to produce Story-Decision-ready knowledge.

Preferred compressed record:

```yaml
id:

mechanism:

human_effect:
  primary:
  secondary:

trigger_or_input:

preconditions:

likely_transition:
  from:
  to:

moderators:

boundary_conditions:

failure_modes:

countereffects:

evidence_quality:
  confidence:
  directness:
  domain:
  important_limits:

story_engine_use:
  usable:
  possible_functions:
  cautions:

do_not_claim:
```

The schema is a transport format, not the research objective.

---

# 12. Research question template

Future tasks should avoid:

> Is mechanism X true?

Prefer:

> Under what conditions can X move an audience from state A to state B, what input produces that movement, what blocks or reverses it, and what information/causal constraints must remain intact?

Every research task should, whenever the evidence allows, explicitly answer:

1. **FROM state**
2. **TRIGGER / INPUT**
3. **TO state**
4. **PRECONDITIONS**
5. **MODERATORS**
6. **BOUNDARIES**
7. **COUNTEREFFECTS**
8. **POSSIBLE STORY DECISIONS**
9. **DO NOT CLAIM**

---

# 13. Relationship to existing corpus

Existing corpus remains reconnaissance material.

For each recurring mechanism:

## A — Surviving Mechanism
Directly supported qualitative mechanism.

## B — Bridge / Application
Mechanism is established elsewhere and plausibly useful for Story decisions.

Do not discard merely because it is not direct narrative research.

## C — Unsupported Upgrade
Remove or quarantine:
- fabricated numbers
- causal upgrades
- population/domain overreach
- platform KPI injection
- fixed timing formulas
- unsupported adjacent mechanism claims

Precision Research should maximize salvage of A/B while stripping C.

---

# 14. Proposed next action after approval

Do **not** run Q1-04.

E1-01 is complete. The next authorized Precision Research is:

**E1-02 — Event / State Updating**

Its research brief should be redesigned around:

> Given the facts/events already introduced, how does an audience build and update a causal/goal model, what kinds of missing causal links create useful uncertainty versus confusion, and what constraints make a next state feel coherent or arbitrary?

Expected Story Engine contribution:

```text
CURRENT FACTS / EVENTS
      ↓
AUDIENCE CAUSAL + GOAL MODEL
      ↓
UNRESOLVED CAUSAL GAP / GOAL
      ↓
CANDIDATE NEW INFORMATION
      ↓
MODEL UPDATE
      ↓
NEXT QUESTION / EXPECTATION
```

P0 direction is approved. E1-01 and E1-02 are complete for review. E1-03 and later research must not start automatically without user approval.
