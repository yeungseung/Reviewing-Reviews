# E1-02 — Event / State Updating
## Precision Research Report v0

> Phase: E1 — Audience Model & Story State Foundation  
> Foundation Pair: **E1-01 Causal + Goal Model Construction ↔ E1-02 Event / State Updating**  
> Status: COMPLETE FOR REVIEW  
> Research date: 2026-09-19  
> Scope guard: E1-02 only. E1-03 and later P0 items were not started.

---

# 0. Research purpose

E1-01 established the audience's current causal + goal model.

E1-02 asks:

> When new events, information, or changes arrive, when and how does the audience's current Story Model update, remain stable, become conflicted, or divide into a new event/state?

Core process:

```text
CURRENT STORY MODEL
      ↓
NEW EVENT / INFORMATION
      ↓
CHANGE DETECTION + RELEVANCE / COHERENCE CHECK
      ↓
MAINTAIN
or
INCREMENTALLY UPDATE / ENRICH
or
REACTIVATE / SUPPRESS
or
CONFLICT / REVISE
or
GLOBAL UPDATE / NEW EVENT MODEL
      ↓
NEW STORY STATE
```

The purpose is not to reproduce all of Event Segmentation Theory or all situation-model theory.

Only mechanisms useful for Story Decision are retained.

---

# 1. Foundation State Separation

All findings in E1-02 preserve three layers.

```text
A. CANONICAL / WORLD STATE
   What is actually true in the story world

B. CHARACTER STATE
   What each character actually knows, believes, wants, intends, and is constrained by

C. AUDIENCE MODEL
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

E1-02 adds another important distinction:

```text
Change in World State
≠
Change detected by Audience
≠
Change integrated into Audience Model
≠
Event Boundary / New Event Model
```

---

# 2. Executive findings

## 2.1 State updating is not one operation

The literature supports at least two qualitatively different processes:

### Incremental / local updating
Incoming information is mapped onto the current model.
The ongoing event remains the same broad event.

### Global updating / model construction
At a sufficiently large coherence break or perceived event boundary, the comprehender constructs a new event model / substructure.

Kurby & Zacks (2012) found evidence for both during the same extended narrative:
- changed dimensions were mentioned more even within event middles → incremental updating
- multiple dimensions were mentioned more at perceived event boundaries → broader/global updating

Brich et al. (2024) provided direct visual-narrative evidence that:
- small omissions within an ongoing event can be bridged while preserving/updating the current event model
- larger breaks between events produce model construction / shifting
- event segmentation was much more sensitive to the new-event break than to the within-event omission

### Engine implication

Do not collapse:

```text
information added
model updated
new event begun
```

into one state transition.

---

## 2.2 Situation changes are multi-dimensional, but there is no universal fixed dimension set for all stories

Classic event-indexing work represents narrative events along dimensions such as:
- time
- space/location
- protagonist/character
- causality
- intentionality/goal

Later reading/film studies also found event segmentation related to:
- character changes
- location changes
- goal changes
- causal changes
- object interaction changes
- temporal references/shifts
- character interactions

Speer et al. (2009) additionally coded:
- spatial changes
- object changes
- character changes
- causal changes
- goal changes
- temporal information

### Engine implication

The Story Engine should track **functionally relevant change dimensions**, not freeze the 1995 five dimensions as a complete ontology.

Candidate dimensions from current evidence:

```yaml
change_dimensions:
  causal:
  goal_intention:
  character_agent:
  location_context:
  time:
  object_interaction:
  social_interaction:
```

User-proposed candidates such as:
- knowledge change
- relationship change
- risk change
- control change
- value/meaning change
- outcome probability change

remain plausible Story Engine dimensions but are **not all directly established as event-segmentation dimensions by E1-02 evidence**.

They should be investigated mainly through E1-03 / E2 / later state synthesis.

---

## 2.3 EVENT CHANGE does not automatically create an EVENT BOUNDARY

Event models are relatively stable across moment-to-moment fluctuations.

Zacks et al.'s Event Segmentation Theory proposes that current event models support predictions about the near future. When prediction becomes less accurate, the model may be updated and a subjective boundary may be perceived.

But:
- not every physical change creates a meaningful boundary
- changes can be incorporated incrementally within the same event
- conceptual overlap and coherence matter
- prior knowledge and predictability affect segmentation

### Engine implication

The Engine should ask:

```text
Did something change?
↓
Is the change relevant to the currently active model?
↓
Can the current model absorb it?
↓
Does it change one/few dimensions locally?
or
Does it create a broad coherence break requiring a new event model?
```

---

## 2.4 Event boundary and surprise must remain separate

Pettijohn & Radvansky (2016) showed a key distinction:

- foreshadowing could remove the extra reading-time cost associated with an event shift
- but it did not eliminate identification of the event shift
- memory-probe slowing after the shift remained, suggesting model updating still occurred

Therefore:

```text
EXPECTED EVENT SHIFT
can still be
EVENT BOUNDARY / MODEL UPDATE
without strong SURPRISE
```

### Engine implication

E1-02 owns:
- state shift
- boundary
- model update

E2-03 owns:
- expectation violation
- surprise
- reappraisal / reframe

Do not infer surprise merely because an event model changes.

---

## 2.5 The number and magnitude of situational changes can influence boundary strength, but no threshold should be hard-coded

Huff et al. (2014) studied audiovisual narratives and found:
- boundaries with more situation-dimension changes were associated with stronger recognition
- predictions across those boundaries became less reliable as more dimensions changed
- results were consistent with incremental effects of multiple dimension changes

Other work found segmentation likelihood/magnitude related to situational changes in reading and film.

### Engine implication

Possible directional prior:

```text
more consequential / simultaneous dimension change
→ higher chance of stronger model update / boundary
```

But do not create:

```text
"2 dimensions = boundary"
"3 dimensions = chapter"
```

No universal threshold is established.

---

## 2.6 Local update and global construction can coexist in one narrative

Kurby & Zacks (2012) directly support both:

```text
dimension changes inside an event
→ incremental updating

perceived event boundary
→ broader/global updating
```

Brich et al. (2024) similarly distinguish:
- mapping/updating within an ongoing event
- shifting/laying a new foundation at larger coherence breaks

### Engine implication

The working operations should distinguish at least:

```text
MAINTAIN
LOCAL UPDATE
NEW EVENT MODEL / SEGMENT
```

Other operations such as REVISION, REACTIVATION, SUPPRESSION, and CONFLICT are layered onto this foundation.

---

## 2.7 Boundaries reorganize accessibility; they do not simply "erase" old information

Swallow, Zacks & Abrams (2009) found that perceptual event boundaries affect immediate memory:
- information present at boundaries can be encoded strongly
- information separated from the current event by a boundary can become differently accessible

Doorway/location-updating research similarly shows reduced retrieval for information associated with a prior event/location.

But boundary effects are not simply "memory gets worse":
Pettijohn et al. (2016) found that distributing information across multiple events can improve later memory under some conditions.

### Engine implication

After a boundary:

```text
old information ≠ deleted
```

A better Story State representation is:

```text
currently active
known but less accessible / prior-event
dormant
reactivatable
```

This supports the E1-01 distinction between known and active information.

---

## 2.8 Causal relevance can reactivate dormant information

E1-01 identified evidence that previously available information can be reactivated when later events make it causally relevant.

E1-02 preserves this as a state-update operation:

```text
KNOWN BUT DORMANT
+
NEW CAUSAL NEED
→
REACTIVATED / ACTIVE
```

This is not the same as introducing new information.

### Engine implication

Before repeating a prior fact, the Engine can ask:

> Is the fact absent from memory, or merely dormant and likely to reactivate through causal relevance?

The answer is probabilistic; Story Engine should not assume automatic reactivation.

---

## 2.9 Conflict does not guarantee revision

Narrative inconsistency research shows that:
- inconsistent new information creates processing difficulty
- successful revision is not guaranteed
- prior information may be reactivated and continue influencing comprehension
- sufficient explanation can help revision

O'Brien et al. (1998) found evidence that qualifying information was not always maintained in the active model; earlier information could be reactivated when later actions were processed.

Rapp & Kendeou (2007) found that revising trait-based character models was easier when later refutation contained sufficient explanation; revision was otherwise resistant.

Temporal inconsistency research likewise shows that inconsistent information can impair integration and can be detected indirectly even when people cannot explicitly report the inconsistency.

### Engine implication

The transition:

```text
MODEL CONFLICT
→ REVISED MODEL
```

must not be automatic.

Possible outcomes include:

```text
conflict remains unresolved
old model persists
new information integrated locally
old relation weakened
alternative interpretation added
model revised
new model constructed
comprehension failure
```

Some of these are application-level distinctions rather than separately proven cognitive operations.

---

## 2.10 Update can fail because required information is unavailable or not validated

Inconsistency/comprehension-monitoring research distinguishes at least two possible failures:

1. required prior information is not currently available/reactivated
2. prior information is available, but incoming information is not successfully validated against it

This supports the user's condition:

```text
CHANGE
≠
AUTOMATIC DETECTION
≠
AUTOMATIC UPDATE
```

### Engine implication

When deciding whether a transition is plausible, the Engine may need to test:

```text
PRIOR INFORMATION AVAILABLE?
CHANGE DETECTABLE?
CURRENT MODEL ACTIVE?
NEW INFORMATION COMPATIBLE?
UPDATE LOAD ACCEPTABLE?
```

Detailed processing-capacity mechanisms belong to E1-04.

---

## 2.11 Event structure is hierarchical and multi-scale

Event segmentation research indicates that people segment activity:
- at fine and coarse grains
- simultaneously across multiple timescales
- with smaller units nested into larger meaningful events

Changes in causes, goals, and locations can be more associated with coarse segmentation, while object-level changes can be more associated with finer segmentation in some tasks.

### Engine implication

A Story State system should not assume one global boundary scale.

Possible levels:

```text
micro/local update
event boundary
larger episode/chapter boundary
```

These are provisional product levels, not exact cognitive categories.

---

# 3. Core State Updating Mechanisms

---

## E102-M01 — Incremental Situation-Model Updating

### mechanism
Incremental situation-model updating

### what_it_updates
One or more currently represented situation dimensions while preserving the ongoing event model.

### trigger
Incoming information changes a relevant feature but retains sufficient overlap/coherence with the current event.

### preconditions
- current event model remains usable
- incoming information can be mapped onto it
- coherence break is limited / bridgeable

### from_state
```text
stable current event model
```

### update_operation
```text
maintain + enrich / modify changed dimension
```

### to_state
```text
same broad event model
+
updated local state
```

### moderators
- semantic/conceptual overlap
- causal continuity
- goal continuity
- spatial/temporal continuity
- background knowledge
- attentional focus

### boundary_conditions
A dimension change can occur without creating a new perceived event.

### failure_modes
- treating every change as new event
- failing to update a relevant changed dimension
- overloading the model with obsolete information

### countereffects
Incremental updating still consumes processing and may make old values less accessible.

### relation_to_E1_01
Updates the causal/goal model without necessarily replacing it.

### possible_story_decisions
- KEEP current event if causal/goal continuity remains strong
- ADD new fact to current state
- MODIFY only the changed relation/attribute
- AVOID declaring a new narrative phase for a minor local change

### evidence
- confidence: HIGH
- directness: DIRECT narrative reading + DIRECT visual narrative support
- population_domain: primarily adults
- important_limits: exact internal mechanism remains theoretically debated

### application_status
CORE FOUNDATION MECHANISM

### do_not_claim
- one exact cognitive algorithm for incremental updating
- one fixed amount of change that defines local update

---

## E102-M02 — Global Update / New Event-Model Construction

### mechanism
Global updating / event-model construction

### what_it_updates
The currently active event representation as a broad unit.

### trigger
A large coherence break / event boundary / low overlap with the current model.

### preconditions
- incoming event is not easily mapped onto current structure
- audience perceives a meaningful discontinuity

### from_state
```text
current event model active
```

### update_operation
```text
segment + construct new event model
```

### to_state
```text
new active event model
+
previous model moved to prior-event memory
```

### moderators
- number/magnitude of dimension changes
- causal/goal discontinuity
- spatial/temporal discontinuity
- predictability
- prior knowledge
- attentional focus

### boundary_conditions
A new shot, sentence, location cue, or physical change alone is not sufficient to prove a new event model.

### failure_modes
- segmentation from superficial edit alone
- forcing a new event despite strong continuity
- preserving obsolete active relations across a genuine boundary

### countereffects
Global updates can reduce accessibility of some prior-event information while strengthening boundary encoding.

### relation_to_E1_01
Changes which causal/goal model is currently active; old model may remain retrievable.

### possible_story_decisions
- START new event/state representation after a genuine coherence break
- ARCHIVE but do not delete prior model
- CARRY FORWARD only relations still relevant
- REACTIVATE prior-event facts later when causally needed

### evidence
- confidence: HIGH
- directness: DIRECT narrative + visual narrative + naturalistic activity
- population_domain: mostly adults
- important_limits: no universal boundary threshold

### application_status
CORE FOUNDATION MECHANISM

### do_not_claim
- every boundary fully wipes working memory
- every location/time change creates a new event

---

## E102-M03 — Situation-Dimension Change Monitoring

### mechanism
Monitoring changes in situation dimensions

### what_it_updates
The variables used to represent what is currently happening.

### trigger
Change in one or more relevant dimensions.

### empirically supported candidate dimensions
- causality
- goal / intentionality
- character / protagonist
- location / space
- time
- object interaction
- character interaction

### from_state
```text
dimension values stable
```

### update_operation
```text
local revise
or
contribute to boundary / global update
```

### to_state
```text
dimension value changed
+
possibly altered boundary strength
```

### moderators
- dimension type
- grain of segmentation
- number of co-occurring changes
- salience
- conceptual importance

### boundary_conditions
No evidence supports treating every possible Story State field as an equally strong boundary cue.

### failure_modes
- freezing legacy five dimensions as exhaustive
- treating any value change as equally meaningful

### possible_story_decisions
- DETECT which dimensions changed
- ASK whether changed dimensions are structurally relevant now
- UPDATE only relevant dimensions if event continuity remains
- ESCALATE to boundary evaluation when changes accumulate or reduce coherence

### evidence
- confidence: HIGH
- directness: DIRECT across reading, listening, film
- population_domain: adults; some developmental evidence
- important_limits: relative weights vary by context/task

### application_status
CORE REPRESENTATION SUPPORT

### do_not_claim
- universal dimension weights
- fixed number of dimensions required for boundary

---

## E102-M04 — Prediction-Stability / Boundary Detection

### mechanism
Prediction-stability based event boundary detection

### what_it_updates
The active event model when its near-future predictions become less reliable.

### trigger
Transient increase in prediction error / unexpected situational change.

### preconditions
- audience has an active event model
- model generates near-future expectations

### from_state
```text
stable predictive event model
```

### update_operation
```text
detect mismatch → update / possibly segment
```

### to_state
```text
revised or newly constructed event model
```

### moderators
- predictability
- situational change magnitude
- prior knowledge
- attention

### boundary_conditions
Event boundary perception is related to prediction difficulty, but surprise is not required for all model updates.

Pettijohn & Radvansky show that a foreshadowed shift can still be identified and updated without the same reading-time surprise cost.

### failure_modes
- equating boundary with surprise
- treating prediction error as reward prediction error
- assuming all mismatch triggers a new event

### relation_to_E1_01
Current causal/goal model generates constraints on plausible next events.

### possible_story_decisions
- FLAG candidate boundary when current model no longer predicts the new situation well
- KEEP update separate from surprise judgment
- USE foreshadowing as possible expectation support without assuming it prevents state update

### evidence
- confidence: MODERATE-HIGH
- directness: DIRECT event-perception/narrative evidence; theory component
- population_domain: adult readers/viewers
- important_limits: predictive-error account is a theory, not a complete deterministic rule

### application_status
USABLE AS DIRECTIONAL MECHANISM

### do_not_claim
- event boundary = surprise
- narrative prediction error = dopamine reward signal

---

## E102-M05 — Boundary-Driven Accessibility Redistribution

### mechanism
Event-boundary memory/accessibility redistribution

### what_it_updates
Which information is currently easy to retrieve from the active event representation.

### trigger
Perceived event boundary / new event model construction.

### from_state
```text
current-event information highly accessible
```

### update_operation
```text
deactivate / archive some prior-event contents
+
encode boundary/current information
```

### to_state
```text
new-event information prioritized
prior-event information still stored but variably accessible
```

### moderators
- relationship of information to boundary
- retrieval cue
- integration with current event
- event structure
- memory interval

### boundary_conditions
Boundaries can both impair and improve memory depending on what is measured and how information is distributed.

### failure_modes
- treating boundary as deletion
- assuming all old information becomes inaccessible
- assuming more boundaries always improve memory

### relation_to_E1_01
Supports known vs active vs dormant distinction.

### possible_story_decisions
- DO NOT assume previously presented facts remain active after a strong boundary
- REACTIVATE important prior-event information if next reasoning depends on it
- ALLOW old state information to become dormant without deleting it

### evidence
- confidence: HIGH for accessibility/memory restructuring
- directness: DIRECT naturalistic film/event tasks + narrative/virtual-environment evidence
- population_domain: adults
- important_limits: memory outcome is task-dependent

### application_status
CORE STATE-ACCESSIBILITY SUPPORT

### do_not_claim
- boundary erases prior event memory
- one universal accessibility decay rate

---

## E102-M06 — Causal-Relevance Reactivation

### mechanism
Causal relevance driven reactivation

### what_it_updates
Accessibility status of previously known information.

### trigger
New information makes an older fact/object/location causally relevant.

### from_state
```text
known but dormant / low-accessibility
```

### update_operation
```text
reactivate
```

### to_state
```text
currently active and causally relevant
```

### moderators
- prior encoding
- distance
- causal relevance
- cue overlap

### boundary_conditions
Reactivation is not guaranteed.

### failure_modes
- assuming "shown once" means currently active
- unnecessary repetition of every prior fact
- depending on a weakly encoded fact without cueing it

### relation_to_E1_01
Direct continuation of E101-M07.

### possible_story_decisions
- CUE prior information when next causal inference depends on it
- RELY on natural reactivation only when causal connection is strong enough
- DISTINGUISH information availability from factual existence

### evidence
- confidence: MODERATE-HIGH
- directness: DIRECT narrative reading
- population_domain: adults
- important_limits: narrow stimulus types relative to general Story Engine use

### application_status
FOUNDATION PAIR SHARED MECHANISM

---

## E102-M07 — Model Conflict Detection / Validation Failure

### mechanism
Conflict detection when incoming information is inconsistent with the current model

### what_it_updates
Compatibility status between old model and new information.

### trigger
New information contradicts or poorly fits an active prior relation/state.

### preconditions
- conflicting prior information must be accessible enough to compare
- incoming information must be processed/validated

### from_state
```text
coherent current model
```

### update_operation
```text
conflict detection
→ update not yet resolved
```

### to_state
```text
MODEL_CONFLICT
```

### moderators
- accessibility of prior information
- explanation quality
- contradiction strength
- attention/comprehension monitoring
- task goals

### boundary_conditions
Conflict detection does not guarantee successful revision.

### failure_modes
- prior information unavailable → conflict missed
- validation failure → contradiction missed
- old model persists despite correction
- new claim rejected rather than integrated

### countereffects
Conflict can cause:
- extra processing
- local repair
- unresolved inconsistency
- later revision

Emotional/surprise consequences are outside E1-02.

### relation_to_E1_01
Extends E101-M08's model-conflict intermediate state.

### possible_story_decisions
- ENTER model_conflict rather than immediate reframe
- CHECK whether conflicting prior fact is currently accessible
- ADD explanatory information when revision is required
- PRESERVE unresolved conflict if evidence does not resolve it

### evidence
- confidence: HIGH for inconsistency cost; MODERATE for detailed revision pathways
- directness: DIRECT narrative reading + BRIDGE knowledge-revision evidence
- population_domain: adults plus developmental studies
- important_limits: revision mechanisms vary; no universal path

### application_status
CORE CONFLICT STATE

### do_not_claim
- contradiction automatically revises model
- contradiction automatically creates surprise
- old information is always removed after correction

---

## E102-M08 — Model Revision / Transformation

### mechanism
Revision of an existing model when new information cannot be integrated without changing prior relations.

### what_it_updates
Previously represented traits, relations, temporal order, or explanatory structure.

### trigger
Conflict plus sufficient reason/evidence to alter the existing representation.

### from_state
```text
model_conflict
```

### update_operation
```text
revise / transform
```

### to_state
```text
modified model that incorporates new information
```

### moderators
- explanatory sufficiency
- strength of prior representation
- task goals
- active availability of old information

### boundary_conditions
Revision is effortful and can be incomplete.

Some research supports persistence/reactivation of outdated information.

### failure_modes
- explanation insufficient
- old model remains dominant
- incompatible elements coexist without full integration

### relation_to_E1_01
Changes causal/goal/belief relations established in E1-01.

### possible_story_decisions
- PROVIDE sufficient explanatory bridge when a factual reinterpretation must be understood
- DO NOT assume one contradictory sentence will replace a strong prior model
- KEEP prior model represented as historical/old interpretation when relevant

### evidence
- confidence: MODERATE-HIGH
- directness: DIRECT narrative comprehension for some revision tasks
- population_domain: adults
- important_limits: exact mechanisms differ across paradigms

### application_status
USABLE WITH CAUTION

### do_not_claim
- revision fully deletes old knowledge
- all model conflicts require transformation

---

## E102-M09 — Hierarchical / Multi-Scale Event Segmentation

### mechanism
Hierarchical event segmentation

### what_it_updates
Which temporal/narrative unit is treated as the current meaningful event.

### trigger
Changes can be perceived at fine or coarse grain depending on their structural significance.

### from_state
```text
ongoing activity stream
```

### update_operation
```text
segment at local or broader grain
```

### to_state
```text
nested event representation
```

### moderators
- causal change
- goal change
- spatial change
- object/action change
- task/instructions
- prior event knowledge

### boundary_conditions
Grain is context- and task-dependent.

### failure_modes
- one boundary scale for all narratives
- equating shot/paragraph/chapter boundaries with cognitive event boundaries

### relation_to_E1_01
Larger causal/goal shifts may support coarser segmentation.

### possible_story_decisions
- REPRESENT micro-update separately from major phase/event shift
- ALLOW nested event units
- DO NOT infer chapter boundaries from one low-level change

### evidence
- confidence: HIGH for hierarchical segmentation
- directness: DIRECT everyday event + narrative/film evidence
- population_domain: adult observers/readers
- important_limits: Story Engine mapping to chapter/scene levels remains application hypothesis

### application_status
CORE STRUCTURAL SUPPORT

---

# 4. Update-operation candidates after E1-02

The user-proposed operation list can now be reduced and qualified.

## Strongly supported as useful distinctions

```text
MAINTAIN
INCREMENTAL_UPDATE
REACTIVATE
SUPPRESS / DEACTIVATE
CONFLICT
REVISE
SEGMENT / CONSTRUCT_NEW_MODEL
```

## Useful but should remain implementation-level aliases

### ENRICH
Can be treated as a subtype of INCREMENTAL_UPDATE:
new information added without changing the existing structural relations.

### REPLACE
Global update/new construction can functionally replace the active model, but the old model is not necessarily erased.
Prefer:

```text
SEGMENT + NEW_ACTIVE_MODEL
```

rather than literal memory replacement.

## Not yet strong enough as independent cognitive operation

### REWEIGHT
Useful for competing hypotheses/goals, but direct E1-02 evidence is insufficient to make it a core event-updating operation.

Keep as optional later representation.

### COEXIST
Multiple models/interpretations can functionally coexist, but E1-02 does not establish a single canonical coexistence mechanism.

Keep as a model state, not necessarily an update operation.

---

# 5. Event Boundary vs Local Update

This is the most important E1-02 distinction.

## Local / incremental update

```text
CURRENT EVENT MODEL
+
relevant change with sufficient continuity
↓
changed dimension(s) updated
↓
SAME EVENT MODEL, MODIFIED
```

Characteristics:
- same broad activity/event remains intelligible
- high/moderate overlap
- inference may bridge omitted information
- no robust subjective new-event boundary is required

## Event boundary / global construction

```text
CURRENT EVENT MODEL
+
large coherence break / major multi-dimensional shift
↓
boundary
↓
NEW ACTIVE EVENT MODEL
```

Characteristics:
- broader change
- lower overlap
- old model becomes prior-event representation
- boundary can restructure accessibility and prediction

## Critical caution

The research supports a **continuum plus distinguishable processes**, not a universal binary threshold.

---

# 6. Existing-information lifecycle candidate

E1-01 proposed:

```text
unknown
known but dormant
active
causally relevant
reactivated
suppressed / low-accessibility
```

E1-02 supports keeping the distinctions but not freezing the enum.

A more relational representation may be safer:

```yaml
information_state:
  known: true/false
  accessibility: high | low | unknown
  active_in_current_model: true/false
  causal_relevance_now: true/false
  event_membership: current | prior | cross_event
  suppression_or_deactivation: true/false
```

Why:

```text
CAUSALLY RELEVANT
```

is not necessarily a memory state.

It is a **relationship between information and current model needs**.

Likewise:

```text
REACTIVATED
```

describes a transition/history, not necessarily a stable state.

This is a schema refinement candidate, not final design.

---

# 7. Model conflict processing candidates

Evidence supports the following safe flow:

```text
CURRENT MODEL
+
INCOMPATIBLE INFORMATION
↓
IS PRIOR CONFLICTING INFORMATION AVAILABLE?
↓
IS INCONSISTENCY DETECTED / VALIDATED?
↓
MODEL_CONFLICT
↓
possible outcomes:
  maintain old model
  local repair
  add qualification
  weaken old relation
  revise model
  construct new model
  leave unresolved
  comprehension failure
```

## What is not established enough to hard-code

- exact probability of each path
- one universal revision sequence
- contradiction automatically causing a new event boundary
- contradiction automatically causing surprise
- old information being erased

---

# 8. Candidate Story State schema changes

E1-02 does not finalize the schema.

Suggested additions/modifications:

```yaml
story_reality:
  current_world_state:
  canonical_relations:
  actual_event_changes:

character_state:
  per_character:
    knowledge:
    beliefs:
    desires:
    goals:
    intentions:
    constraints:

audience_model:
  current_event_model:
    active_dimensions:
    causal_goal_model:
    current_event_id_or_scope:

  information_access:
    known_information:
    active_information:
    dormant_or_low_accessibility_information:
    prior_event_information:

  update_status:
    detected_changes:
    local_updates:
    boundary_candidate:
    model_conflicts:
    unresolved_updates:

  prior_models:
    - event_model:
      accessibility:
      still_relevant:
```

## Important structural change

Do not encode:

```text
causally_relevant
```

as a simple permanent property of an information item.

Prefer:

```text
information X
is causally relevant
TO current model/question Y
AT current state
```

---

# 9. FROM → TO transition candidates

## T1 — Stable model → Incrementally updated model

```text
FROM:
current event model coherent

TRIGGER:
one/few relevant situation dimensions change with strong continuity

TO:
same event model with local updates
```

---

## T2 — Stable model → New event model

```text
FROM:
current event model active

TRIGGER:
large coherence break / broad situation change

TO:
new active event model
prior model archived / less accessible
```

---

## T3 — Known dormant information → Reactivated information

```text
FROM:
known but not currently active

TRIGGER:
new event makes information causally useful

TO:
active / causally relevant information
```

---

## T4 — Active old-event information → Prior-event / reduced accessibility

```text
FROM:
information active in current event model

TRIGGER:
event boundary / global model shift

TO:
stored but lower-accessibility prior-event information
```

---

## T5 — Coherent model → Model conflict

```text
FROM:
current model internally coherent

TRIGGER:
new information incompatible with accessible prior model

TO:
model_conflict
```

---

## T6 — Model conflict → Revised model

```text
FROM:
conflict detected

TRIGGER:
sufficient explanatory / corrective information

TO:
modified model incorporating new information
```

Not guaranteed.

---

## T7 — Model conflict → Unresolved / old model persists

```text
FROM:
conflict detected

TRIGGER:
insufficient explanation / strong prior model / update failure

TO:
old model persists or conflict remains unresolved
```

---

## T8 — Situation changes accumulate → Stronger boundary

```text
FROM:
ongoing event

TRIGGER:
multiple meaningful situation dimensions change

TO:
higher probability / stronger perception of event boundary
```

Directional only; no threshold.

---

## T9 — Unexpected shift → Expected shift via foreshadowing, while boundary remains

```text
FROM:
event shift likely experienced as unexpected

TRIGGER:
prior foreshadowing / expectation support

TO:
event shift still segmented/updated
but less unexpected processing cost
```

This is an important handoff to E2-03.

---

# 10. Handoff to E1-03 / E2

## E1-03 — Appraisal → Emotion / Judgment

E1-02 can tell E1-03:
- what changed
- whether current model was maintained, revised, or segmented
- whether causal/goal relations changed
- whether control/risk/relationship variables may have changed as world facts

E1-03 must determine:
- appraisal meaning
- emotion/judgment consequence
- responsibility
- controllability
- fairness/legitimacy

---

## E2-01 — Information Gap / Curiosity

E1-02 can identify:
- unresolved update
- missing bridge
- model conflict
- competing alternatives

E2-01 must determine when these produce curiosity rather than confusion/indifference.

---

## E2-02 — Narrative Expectation / Suspense

E1-02 can identify:
- active event model
- current causal/goal constraints
- boundary status
- prediction reliability changes

E2-02 must determine how these support suspense/tension.

---

## E2-03 — Expectation Violation → Surprise → Reappraisal / Reframe

E1-02 establishes a critical input:

```text
event/model update
can occur
without surprise
```

E2-03 must determine:
- when a mismatch is actually experienced as expectation violation
- when violation becomes surprise
- when surprise produces reappraisal/reframe
- when it instead produces arbitrariness/confusion/rejection

---

# 11. P0 Roadmap implications

## No major ordering change

Current approved P0 remains:

1. E1-01 Causal + Goal Model Construction — COMPLETE
2. E1-02 Event / State Updating — COMPLETE FOR REVIEW
3. E1-03 Appraisal → Emotion / Judgment
4. E2-01 Information Gap / Curiosity
5. E2-02 Narrative Expectation / Suspense
6. E2-03 Expectation Violation → Surprise → Reappraisal / Reframe
7. E1-04 Processing Capacity

## Minor architecture refinements

### Refinement A
Story State should explicitly represent:
- current event model
- prior event model(s)
- boundary candidate/status
- update status

### Refinement B
Information accessibility should probably be multidimensional rather than one enum:
- known?
- currently active?
- current-event vs prior-event?
- causally relevant now?
- suppressed/low accessibility?

### Refinement C
Model conflict remains an intermediate state, not a synonym for surprise or reframe.

### Refinement D
Event boundary should not be inferred from simple surface edit/location change alone.
Boundary judgment should depend on meaningful situation change and model continuity.

---

# 12. Minimal evidence summary

## DIRECT / strong foundation

- Zwaan, Langston & Graesser (1995) — event-indexing dimensions
- Zacks, Speer & Reynolds (2009) — situation changes predict segmentation in reading/listening/film
- Kurby & Zacks (2012) — evidence for incremental and global updating within one narrative
- Speer, Zacks & Reynolds (2007) — spontaneous narrative event boundaries; goal/situation changes
- Speer et al. (2009) — neural tracking/updating of situation changes
- Swallow, Zacks & Abrams (2009) — event boundaries alter short-term event memory/accessibility
- Huff, Meitz & Papenmeier (2014) — multi-dimensional changes at audiovisual event boundaries
- Pettijohn & Radvansky (2016) — boundary/update dissociated from unexpectedness
- Brich et al. (2024) — direct visual-narrative distinction between updating and construction
- O'Brien et al. (1998) — prior information can reactivate during updating
- Rinck et al. (2001) — temporal inconsistency affects updating/integration
- Rapp & Kendeou (2007) — narrative revision not guaranteed; explanation can facilitate revision

## BRIDGE / boundary support

- doorway/location updating research
- broader comprehension monitoring / validation research
- developmental and aging differences in segmentation/updating

## APPLICATION HYPOTHESES

- exact runtime enum for information accessibility
- model reweighting operation
- coexistence as a formal update operation
- exact boundary score
- exact dimension weights
- exact mapping from event boundary to scene/chapter structure

---

# 13. Core sources

1. Zwaan RA, Langston MC, Graesser AC. The Construction of Situation Models in Narrative Comprehension: An Event-Indexing Model. Psychological Science. 1995;6(5):292–297. DOI: 10.1111/j.1467-9280.1995.tb00513.x
2. Zwaan RA, Radvansky GA. Situation models in language comprehension and memory. Psychological Bulletin. 1998;123(2):162–185. DOI: 10.1037/0033-2909.123.2.162
3. Zacks JM, Speer NK, Swallow KM, Braver TS, Reynolds JR. Event perception: a mind-brain perspective. Psychological Bulletin. 2007;133(2):273–293. DOI: 10.1037/0033-2909.133.2.273
4. Kurby CA, Zacks JM. Segmentation in the perception and memory of events. Trends in Cognitive Sciences. 2008;12(2):72–79. DOI: 10.1016/j.tics.2007.11.004
5. Speer NK, Zacks JM, Reynolds JR. Human brain activity time-locked to narrative event boundaries. Psychological Science. 2007;18(5):449–455. DOI: 10.1111/j.1467-9280.2007.01920.x
6. Zacks JM, Speer NK, Reynolds JR. Segmentation in reading and film comprehension. Journal of Experimental Psychology: General. 2009;138(2):307–327. DOI: 10.1037/a0015305
7. Speer NK, Reynolds JR, Swallow KM, Zacks JM. Reading Stories Activates Neural Representations of Visual and Motor Experiences. Psychological Science. 2009;20(8):989–999. DOI: 10.1111/j.1467-9280.2009.02397.x
8. Swallow KM, Zacks JM, Abrams RA. Event boundaries in perception affect memory encoding and updating. Journal of Experimental Psychology: General. 2009;138(2):236–257. DOI: 10.1037/a0015631
9. Kurby CA, Zacks JM. Starting from scratch and building brick by brick in comprehension. Memory & Cognition. 2012;40(5):812–826. DOI: 10.3758/s13421-011-0179-8
10. Huff M, Meitz TGK, Papenmeier F. Changes in situation models modulate processes of event perception in audiovisual narratives. Journal of Experimental Psychology: Learning, Memory, and Cognition. 2014;40(5):1377–1388. DOI: 10.1037/a0036780
11. Pettijohn KA, Radvansky GA. Narrative event boundaries, reading times, and expectation. Memory & Cognition. 2016;44(7):1064–1075. DOI: 10.3758/s13421-016-0619-6
12. Brich IR, Papenmeier F, Huff M, Merkt M. Construction or updating? Event model processes during visual narrative comprehension. Psychonomic Bulletin & Review. 2024;31(5):2092–2101. DOI: 10.3758/s13423-023-02424-w
13. O'Brien EJ, Rizzella ML, Albrecht JE, Halleran JG. Updating a situation model: a memory-based text processing view. Journal of Experimental Psychology: Learning, Memory, and Cognition. 1998.
14. Rinck M, Hähnel A, Becker G. Using temporal information to construct, update, and retrieve situation models of narratives. Journal of Experimental Psychology: Learning, Memory, and Cognition. 2001.
15. Rapp DN, Kendeou P. Revising what readers know: updating text representations during narrative comprehension. Memory & Cognition. 2007/2008 publication record.
16. Radvansky GA, Zacks JM. Event Boundaries in Memory and Cognition. Current Opinion in Behavioral Sciences. 2017;17:133–140. DOI: 10.1016/j.cobeha.2017.08.006

---

# 14. Final E1-02 model

```text
CANONICAL / WORLD CHANGE
        ↓
AUDIENCE DETECTS CHANGE?
        ↓
IS IT RELEVANT TO CURRENT EVENT MODEL?
        ↓
CAN CURRENT MODEL ABSORB IT?
     ↙                ↘
   YES                NO / LARGE BREAK
    ↓                       ↓
LOCAL / INCREMENTAL      EVENT BOUNDARY
UPDATE                   / NEW MODEL
    ↓                       ↓
ACTIVE INFORMATION      PRIOR MODEL DEACTIVATED
REORGANIZED             NEW MODEL ACTIVE
     \                    /
      \                  /
       → POSSIBLE MODEL CONFLICT
          / REACTIVATION / REVISION
                    ↓
             NEW STORY STATE
```

Critical constraints:

```text
World change ≠ detected audience change
Detected change ≠ state update
State update ≠ event boundary
Event boundary ≠ surprise
Conflict ≠ automatic revision
Revision ≠ deletion of old model
Known ≠ active ≠ causally relevant
```

This is the E1-02 contribution to the Foundation Pair.

E1-03 was not started.
