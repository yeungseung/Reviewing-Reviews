# E1-01 — Causal + Goal Model Construction
## Precision Research Report v0

> Phase: E1 — Audience Model & Story State Foundation  
> Foundation Pair: **E1-01 Causal + Goal Model Construction ↔ E1-02 Event / State Updating**  
> Status: COMPLETE FOR REVIEW  
> Research date: 2026-09-19  
> Scope guard: E1-01 only. E1-02 and later P0 items were not started.

---

# 0. Research purpose

This task does **not** ask how to write a causal plot.

It asks:

> How does an audience construct an internal model of what caused what, what a character wants, why actions are taken, and how that model shapes subsequent comprehension, expectation, and possible revision?

The Story Engine needs this research so that it can reason about the audience's **current causal + goal model** before choosing the next experience.

Core decision loop:

```text
FACTS / EVENTS ALREADY PRESENTED
        ↓
AUDIENCE CAUSAL + GOAL MODEL
        ↓
ACTIVE / UNRESOLVED CAUSAL OR GOAL RELATIONS
        ↓
CANDIDATE NEW INFORMATION
        ↓
MODEL MAINTAINED / STRENGTHENED / FILLED / REVISED / SUPPRESSED / CONFLICTED
        ↓
POSSIBLE NEXT EXPECTATION / EXPERIENCE
```

E1-01 stops before fully researching:
- event-boundary/state-update dynamics → E1-02
- appraisal/emotion → E1-03
- curiosity → E2-01
- suspense → E2-02
- expectation violation/reframe → E2-03

Only necessary handoff connections are recorded.

---

# 1. Executive findings

## 1.1 Audiences construct causal/goal-based situation models, not only surface sequences

A broad narrative-comprehension research line supports the idea that readers build a situation model and actively seek relations that make actions, events, and states coherent.

Graesser, Singer & Trabasso (1994) describe a constructionist account in which readers attempt to build meaning representations that:
- fit comprehension goals,
- maintain local and global coherence,
- and explain why actions, events, and states are mentioned.

Trabasso & van den Broek (1985) showed that narrative events' causal-chain membership and number of causal connections predict recall, summarization, and judged importance.

Zwaan, Langston & Graesser (1995) further supported representation of narrative events along situation dimensions including causality and intentionality.

### Engine implication

The audience model should not be represented as a flat list of known facts.

It should be able to contain at least:
- causal relations,
- character goals/intentions,
- unresolved causal gaps,
- relevant constraints,
- and confidence/ambiguity where more than one explanation remains plausible.

---

## 1.2 Missing causal links can trigger bridging inference — but only when the gap is bridgeable

Research on causal bridging shows that readers often construct missing causal antecedents when a current event would otherwise lack coherence.

Validation studies show that readers can compute a missing mediating causal relation and validate it against background knowledge.

Ackerman's work on unexpected/inconsistent outcomes also supports the distinction between merely knowing which entities are involved and constructing a causal explanation that makes an outcome follow from earlier information.

Kim (1999) found that implicit story versions could be rated as more interesting than explicit versions when readers actually generated causal bridging inferences; when processing conditions prevented inference generation, the advantage disappeared.

More recent visual-narrative work also shows that removing a bridging action creates a coherence gap that can prompt bridging inference, although whether viewers infer or segment depends on how bridgeable the gap is.

### Engine implication

An unresolved cause is not automatically a defect.

A useful state may exist between:
- fully explicit causality
- and incomprehensible discontinuity.

The relevant question is:

> Does the current audience model contain enough prior information for a plausible bridge?

---

## 1.3 Goal inference is part of causal comprehension

Goal information is not merely character decoration.

Suh & Trabasso (1993) found that readers generated goal-related inferences online when subgoals/actions fit a superordinate goal and when the relevant goal remained unsatisfied.

Poynor & Morris (2003) showed that readers infer goals that are not explicitly stated; the inferred goal can function similarly to an explicitly stated goal in online comprehension and memory.

Bower & Morrow's mental-model account similarly describes readers as relating characters' actions to their goals.

### Engine implication

When the Story Engine evaluates a candidate action/event, it should ask:

- What goal would make this action intelligible?
- Is that goal explicit, inferable, ambiguous, obsolete, or absent?
- Does the audience have enough information to connect action to goal?

This does **not** mean every action needs an explicitly stated goal.

---

## 1.4 Goals are dynamically activated, maintained, and suppressed

Linderholm et al. (2004) directly studied narratives with multiple/changing character goals.

Results support:
- maintaining activation of goals that remain relevant/rementioned,
- suppressing prior goal information when a new goal becomes more relevant.

This matters because a reader's "current character model" is not simply the union of every previously mentioned desire.

### Engine implication

Character goals need status, not just presence.

Candidate statuses:

- ACTIVE
- INFERRED
- EXPLICIT
- SATISFIED
- FAILED
- SUPERSEDED
- SUPPRESSED / LOW_ACCESSIBILITY
- AMBIGUOUS
- UNKNOWN

These are provisional Story State fields, not a final ontology.

---

## 1.5 Goal hierarchy matters

Suh & Trabasso's results support hierarchical relations:
- superordinate goal,
- subordinate goal/action,
- recent unsatisfied goal.

An action or subgoal is easier to integrate when it fits the active higher-level plan.

### Engine implication

A Story State may need:

```yaml
goal_model:
  superordinate_goal:
  active_subgoal:
  goal_status:
  constraints:
```

However, do not assume all narratives contain a clean hierarchy.

Goal hierarchy is a useful representational option, not a mandatory story grammar.

---

## 1.6 Desire alone can cause premature intention inference

Haigh & Bonnefon (2015) showed that readers rapidly infer a protagonist's intention from desire, sometimes even before the protagonist's belief state actually licenses that intention.

When later action contradicted the inferred intention, reading was immediately disrupted.

Belief information subsequently moderated/inhibited the desire-based inference, though the inhibition was not always sustained.

### Engine implication

The audience may form **premature or overconfident intention models**.

The Story Engine should therefore distinguish:

```text
CHARACTER DESIRE
≠
CHARACTER BELIEF / KNOWLEDGE
≠
FEASIBLE INTENTION
≠
ACTION
```

This distinction is important when predicting what the audience currently expects a character to do.

---

## 1.7 Reader perspective changes which goals remain active

Albrecht et al. (1995) provide an important boundary condition.

Readers did not always behave as though they automatically adopted the protagonist's perspective. When explicitly instructed to take the protagonist's point of view, goal accessibility more closely tracked whether the goal was satisfied from the protagonist's perspective.

### Engine implication

The Story Engine should not assume:

> audience goal model = character's own internal goal model

Instead, it may need to distinguish:
- what the character wants,
- what the character believes,
- what the audience knows,
- what the audience thinks the character will do.

This becomes especially important for irony, secrets, false beliefs, and asymmetric information.

Detailed expectation consequences belong to E2.

---

## 1.8 Causal relevance can reactivate previously available information

Sundermeier, van den Broek & Zwaan (2005) showed that object/location information became more available when it became causally relevant to a later event.

This suggests that audience processing is selective:
previously encountered information can become functionally active again when a new event makes it useful for coherence.

### Engine implication

A prior fact need not remain continuously "active."

The engine may benefit from distinguishing:

- KNOWN
- CURRENTLY_ACTIVE / CAUSALLY_RELEVANT
- DORMANT
- REACTIVATED

This is a candidate representation for later testing, not a hard cognitive-state measurement.

---

## 1.9 Causal centrality relates to memory and perceived importance, including in audiovisual narratives

Classic causal-network research found that causally connected/central events are recalled more and judged more important.

Recent naturalistic audiovisual research strengthens the bridge to film/video:

- Lee & Chen (2022): events with more causal connections in movie narratives were more likely to be remembered; causal and semantic centrality made partly independent contributions.
- Song et al. (2021): moments of stronger causal relation to prior movie events were associated with higher subjective comprehension in scrambled-movie paradigms.

### Engine implication

Causal connectedness is a useful signal for:
- importance,
- integration,
- likely memory accessibility,
- comprehension.

### Do not infer

- every scene must be causally central
- higher centrality always improves engagement
- causal centrality predicts retention/CTR
- low-centrality material is inherently bad

---

# 2. Core mechanisms

---

## E101-M01 — Coherence-Driven Causal Integration

### mechanism
Coherence-seeking causal integration

### what_it_models
How the audience links incoming events to prior events in order to maintain an intelligible situation model.

### trigger
A new event/outcome whose relation to prior events matters for understanding.

### preconditions
- prior relevant information exists or is accessible
- the audience can recognize that an explanatory relation is needed
- the gap is not so large that no plausible bridge can be constructed

### from_state
```text
Known prior events
+
new event
+
causal relation incomplete / implicit
```

### to_state
Possible outcomes:

```text
A. causal link inferred → coherence restored
B. several links remain plausible → causal ambiguity
C. no plausible bridge → unresolved coherence gap / confusion risk
```

### moderators
- background knowledge
- inferential distance
- availability of prior premises
- processing capacity
- referential continuity
- text/scene context

### boundary_conditions
Inference is not guaranteed simply because information is omitted.

Large or poorly constrained gaps may fail to produce a useful bridge.

### failure_modes
- arbitrary jump
- insufficient antecedent information
- too many plausible causes
- audience lacks required world knowledge
- gap mistaken for an error rather than intentional omission

### countereffects
Leaving a causal relation implicit can sometimes increase cognitive interest if the audience successfully generates the bridge, but can also increase effort/confusion.

### relation_to
- prediction: inferred cause changes what future events seem plausible
- expectation: coherent causal model constrains expected consequences
- comprehension: direct
- later_state_update: handoff to E1-02 when a new event changes the model

### possible_story_decisions
- REVEAL a missing cause if current gap is not bridgeable
- DELAY a cause if enough evidence exists for productive inference
- PARTIALLY_REVEAL a cause to narrow causal hypotheses
- REACTIVATE prior information needed for a bridge
- PRESERVE ambiguity when several causes remain genuinely plausible

### evidence
- confidence: HIGH for causal/coherence inference in narrative reading
- directness: DIRECT for narrative text; BRIDGE/DIRECT-supporting for visual narrative
- population_domain: mostly adult readers; additional child/L2/visual evidence exists
- important_limits: task/population differences; does not specify optimal omission amount

### application_status
USABLE AS DECISION EVIDENCE

### do_not_claim
- "Causal gaps always increase curiosity"
- "Implicit causality is always better than explicit causality"
- fixed percentage or timing for causal omission

---

## E101-M02 — Causal Network Integration / Centrality

### mechanism
Causal-network integration

### what_it_models
How an event's connections to other events affect its structural role in the audience's representation.

### trigger
An event becomes linked as cause/consequence to one or more earlier/later events.

### from_state
```text
Event represented as relatively isolated
```

### to_state
```text
Event integrated into wider causal network
→ greater structural centrality / accessibility / importance potential
```

### moderators
- number and strength of causal connections
- chain membership
- semantic connections
- memory/task demands

### boundary_conditions
Centrality findings are strongest for importance/memory/comprehension, not for aesthetic quality or engagement.

### failure_modes
- treating every event as needing maximum connectivity
- confusing coder-defined causal centrality with objective causation
- mistaking correlation with memory for an optimization law

### countereffects
Highly connected structures may still become hard to process if too many relations must be held at once; this is handed to E1-04.

### relation_to
- prediction: central events constrain more downstream possibilities
- expectation: consequences become easier to derive
- comprehension: strong
- later_state_update: central events may carry forward strongly into future state representation

### possible_story_decisions
- CONNECT a new event to a relevant prior cause or consequence
- CHECK whether an important event is currently isolated in the audience model
- IDENTIFY which prior event should be reactivated for comprehension
- ALLOW peripheral/context events to remain low-centrality when they serve other functions

### evidence
- confidence: HIGH for memory/importance association
- directness: DIRECT narrative text + DIRECT audiovisual memory evidence
- population_domain: adult readers/viewers
- important_limits: not evidence for retention/CTR or universal story quality

### application_status
USABLE AS STRUCTURAL SIGNAL

### do_not_claim
- "Every important event must be causally necessary"
- "More causal links always means better story"

---

## E101-M03 — Goal Inference as Causal Organizer

### mechanism
Goal inference and goal-action binding

### what_it_models
How the audience infers what a character is trying to achieve and uses that inferred goal to interpret actions.

### trigger
Character behavior/context implies a goal without necessarily stating it.

### preconditions
- cues support a coherent goal inference
- behavior is interpretable as goal-directed
- relevant goal knowledge is available

### from_state
```text
Character action known
+
goal absent / implicit
```

### to_state
```text
Goal inferred
→ action becomes interpretable within a goal plan
```

### moderators
- cue strength
- goal-action fit
- explicit vs implicit goal
- prior context
- reader perspective

### boundary_conditions
Audiences can infer a wrong/oversimplified goal.

Goal inference is not mind reading.

### failure_modes
- action has no inferable motivation
- several goals fit equally well
- later facts reveal the initial goal inference was wrong
- goal is inferred from desire without considering character belief/constraint

### countereffects
Ambiguous goals can maintain multiple interpretations but can also weaken causal comprehension.

### relation_to
- prediction: inferred goal constrains likely next actions
- expectation: goal success/failure creates expected outcomes
- comprehension: strong
- later_state_update: new evidence can strengthen, replace, or suppress the goal model

### possible_story_decisions
- LEAVE goal implicit when action/context makes it inferable
- EXPLICITLY STATE or CLARIFY goal when the action would otherwise be causally opaque
- PRESERVE multiple candidate goals when ambiguity is intended and supported
- ADD constraint/belief information before expecting the audience to infer a specific intention

### evidence
- confidence: HIGH
- directness: DIRECT narrative reading
- population_domain: primarily adult readers; developmental evidence supports broader relevance with limits
- important_limits: not every inferred goal is accurate or equally accessible

### application_status
CORE FOUNDATION MECHANISM

### do_not_claim
- "Every action must have one clear goal"
- "Implicit goals are always more engaging"

---

## E101-M04 — Goal Hierarchy / Active Unsatisfied Goal

### mechanism
Hierarchical goal-plan tracking

### what_it_models
How superordinate goals, subgoals, and current unsatisfied goals organize interpretation of actions.

### trigger
A new subgoal/action appears in relation to an existing higher-level goal.

### from_state
```text
Multiple goal-related elements available
```

### to_state
```text
One goal/subgoal becomes active as the current explanatory frame
```

### moderators
- whether subgoal fits superordinate plan
- recency
- satisfaction status
- explicit reminders
- current causal relevance

### boundary_conditions
Not all stories or real-world behavior form clean goal hierarchies.

### failure_modes
- overfitting all actions into one global purpose
- ignoring side goals or conflicting motivations
- treating "latest goal" as always dominant

### relation_to
- prediction: active goal guides action expectations
- expectation: goal plan creates expected progress/obstacles
- comprehension: supports episode connection
- later_state_update: goal success/failure/new goal can change focus

### possible_story_decisions
- REINFORCE active goal before a causally dependent action
- INTRODUCE a subgoal if it logically supports a higher goal
- CHECK whether a new action appears disconnected because the relevant goal is not active
- ALLOW multiple active goals if the material genuinely supports them

### evidence
- confidence: MODERATE-HIGH
- directness: DIRECT narrative reading
- population_domain: adult reader studies plus developmental research
- important_limits: hierarchical structure is model-dependent and not universal

### application_status
USABLE WITH FLEXIBILITY

### do_not_claim
- one universal goal hierarchy for every narrative

---

## E101-M05 — Goal Relevance Updating / Suppression

### mechanism
Dynamic goal activation and suppression

### what_it_models
How the audience changes which previously represented goals are currently accessible/relevant.

### trigger
- goal is rementioned
- new goal introduced
- old goal becomes irrelevant
- new direction of action dominates

### from_state
```text
Old goal active / accessible
```

### to_state
Possible transitions:

```text
remention → old goal remains/re-becomes highly active
new relevant goal → new goal active + old goal suppressed
ambiguous change → multiple goal states may remain unresolved
```

### moderators
- causal relevance
- recency
- remention
- ambiguity of goal status

### boundary_conditions
Suppressed does not mean erased.

Old goals may remain in memory and can later be reinstated.

### failure_modes
- engine assumes every prior goal remains equally active
- abrupt goal replacement lacks cues
- engine treats goal completion and goal suppression as identical

### relation_to
- prediction: active goal changes expected actions
- expectation: new goal redirects likely outcomes
- comprehension: helps track causal sequence
- later_state_update: direct handoff to E1-02

### possible_story_decisions
- SIGNAL that a prior goal is no longer currently relevant
- REACTIVATE an older goal if a later event depends on it
- INTRODUCE a new goal only with enough context for model transition
- KEEP old goal unresolved if the material requires simultaneous goals

### evidence
- confidence: HIGH for goal activation/suppression phenomenon
- directness: DIRECT narrative reading
- population_domain: adult readers
- important_limits: laboratory narratives; accessibility ≠ conscious awareness

### application_status
CORE FOUNDATION MECHANISM

### do_not_claim
- "new goal deletes old goal"
- fixed time until old goals decay

---

## E101-M06 — Belief–Desire Constraint on Intention Inference

### mechanism
Belief/desire constrained intention inference

### what_it_models
How audiences infer intentions from what a character wants and what the character believes/knows.

### trigger
Information about desire, belief, or action becomes available.

### from_state
```text
Desire cue present
→ provisional intention inference
```

### to_state
Possible transitions:

```text
belief supports desire → intention inference maintained
belief conflicts with desire → intention inference inhibited/revised
later action contradicts inference → processing disruption / model conflict
```

### moderators
- availability of character belief information
- processing effort
- perspective
- timing/order of cues

### boundary_conditions
Desire can produce a premature inference even when belief information does not support it.

### failure_modes
- audience predicts action from desire alone
- engine treats objective reality as equivalent to character knowledge
- hidden information is accidentally given to the character model

### relation_to
- prediction: direct handoff
- expectation: direct handoff
- comprehension: helps explain action consistency
- later_state_update: conflict can require model revision

### possible_story_decisions
- SEPARATE audience knowledge from character knowledge
- ADD character-belief/constraint information if a specific intention must be inferable
- PRESERVE false-belief asymmetry when it is part of the factual situation
- FLAG action as potentially surprising if it conflicts with currently inferred intention

### evidence
- confidence: MODERATE-HIGH
- directness: DIRECT narrative vignette
- population_domain: adults
- important_limits: one research line; do not universalize processing stages

### application_status
USABLE AS CONSTRAINT MODEL

### do_not_claim
- exact universal sequence of desire→belief→intention processing

---

## E101-M07 — Causal Relevance Reactivation

### mechanism
Causal relevance based reactivation

### what_it_models
How previously encountered information becomes more accessible when a later event makes it causally useful.

### trigger
A new event creates a causal need for an earlier object/location/fact.

### from_state
```text
prior information known but not active
```

### to_state
```text
prior information reactivated because it now supports causal coherence
```

### moderators
- causal relevance
- memory accessibility
- distance
- prior encoding quality

### boundary_conditions
Evidence is specific to tested narrative information such as objects/locations.

Generalization to every type of story fact is plausible but not directly proven.

### failure_modes
- crucial earlier fact was never sufficiently encoded
- too much distance/interference
- prior fact is not actually causally relevant

### relation_to
- prediction: reactivated fact can constrain consequences
- expectation: may revive an older causal path
- comprehension: direct
- later_state_update: handoff E1-02

### possible_story_decisions
- REACTIVATE a previously known fact before it becomes causally necessary
- CHECK whether a candidate reveal depends on dormant information the audience may not retrieve
- AVOID re-explaining every prior fact when causal relevance can naturally reactivate it

### evidence
- confidence: MODERATE-HIGH
- directness: DIRECT narrative reading
- population_domain: adults
- important_limits: evidence type is narrower than full Story Engine application

### application_status
BRIDGEABLE CORE SUPPORT

### do_not_claim
- all prior facts are automatically reactivated when needed

---

## E101-M08 — Causal / Goal Model Conflict and Revision

### mechanism
Model conflict detection and revision

### what_it_models
What happens when incoming information does not fit the currently active causal or goal model.

### trigger
- action contradicts inferred intention
- new goal displaces old goal
- outcome lacks expected cause
- new information conflicts with prior explanation

### from_state
```text
coherent active model
+
incoming incompatible information
```

### to_state
Research-supported / plausible outcomes include:

```text
A. prior inference inhibited
B. old goal suppressed / new goal prioritized
C. bridging explanation generated
D. conflict remains unresolved
E. model revision/integration attempted
```

### moderators
- strength of old model
- availability of alternative explanation
- causal distance
- explicit corrective/explanatory information
- perspective and background knowledge

### boundary_conditions
E1-01 evidence supports several component processes but does **not** establish one universal model-revision algorithm.

Detailed event-state transition belongs to E1-02.
Reappraisal/reframe consequences belong to E2-03.

### failure_modes
- forcing immediate single explanation
- calling any contradiction a "reframe"
- deleting old information when it may continue to influence interpretation
- assuming conflict always improves engagement

### countereffects
Conflict may:
- increase explanatory processing
- cause surprise later
- or simply create comprehension failure

### relation_to
- prediction: current prediction can fail
- expectation: conflict can destabilize expectation
- comprehension: may trigger repair or difficulty
- later_state_update: MAJOR E1-02 HANDOFF

### possible_story_decisions
- MARK current model as conflicted rather than instantly replacing it
- ADD explanatory evidence to repair coherence
- MAINTAIN unresolved alternatives when evidence remains ambiguous
- SUPPRESS an obsolete goal when a new goal clearly becomes relevant
- HAND OFF expectation violation consequences to E2-03

### evidence
- confidence: MODERATE
- directness: DIRECT components + BRIDGE knowledge-revision evidence
- population_domain: narrative readers plus broader knowledge-revision work
- important_limits: no single unified narrative revision law established

### application_status
APPLICATION SYNTHESIS / FOUNDATION HANDOFF

### do_not_claim
- "contradiction automatically causes reframe"
- "the audience always discards the old model"

---

## E101-M09 — Competing Causal Hypotheses

### mechanism
Multiple plausible causal explanations

### what_it_models
How an audience may hold more than one causal explanation when available evidence underdetermines the cause.

### trigger
One outcome is compatible with several plausible causes.

### from_state
```text
insufficient evidence for unique cause
```

### to_state
```text
multiple causal hypotheses retained with unequal or unresolved plausibility
```

### moderators
- prior knowledge
- cue diagnosticity
- availability of alternatives
- confirmation/disconfirmation
- explanation quality

### boundary_conditions
Direct story-specific evidence is limited compared with general causal reasoning literature.

### failure_modes
- engine commits prematurely to one cause
- alternatives are created that facts do not support
- false balance between unequally supported causes

### relation_to
- prediction: different causes imply different futures
- expectation: uncertainty can branch
- comprehension: too many alternatives may increase load
- later_state_update: new evidence can collapse or reweight hypothesis set

### possible_story_decisions
- RETAIN multiple causal candidates when the facts warrant ambiguity
- REVEAL discriminating information later
- DO NOT manufacture alternative causes merely to create suspense
- UPDATE weights when new evidence selectively supports one explanation

### evidence
- confidence: MODERATE-LOW for direct narrative use
- directness: BRIDGE from general causal-inference research
- population_domain: adult causal reasoning
- important_limits: not enough direct narrative evidence to hard-code inference weighting

### application_status
BRIDGE / OPTIONAL REPRESENTATION

### do_not_claim
- Bayesian numeric weighting without evidence/data
- audiences always represent every plausible cause

---

# 3. Story State fields suggested by E1-01

The research suggests that the current Story State may need a richer **audience_model** than the earlier draft.

## Candidate additions

```yaml
audience_model:

  causal_model:
    links:
      - cause:
        effect:
        status: explicit | inferred | ambiguous
        confidence:
    unresolved_causal_gaps: []
    competing_causal_hypotheses: []
    model_conflicts: []

  character_model:
    - character:
      desires: []
      beliefs_or_known_information: []
      goals:
        - goal:
          source: explicit | inferred
          status: active | satisfied | failed | superseded | suppressed | ambiguous
          parent_goal:
      constraints: []
      inferred_intentions: []

  active_model:
    causally_relevant_prior_information: []
    dormant_but_known_information: []
```

## Important restraint

These fields are **candidates**, not a frozen schema.

E1-02 may show that some should be:
- merged,
- redefined,
- moved,
- or removed.

---

# 4. FROM → TO transition candidates

## T1 — Unexplained outcome → Bridged causal model

```text
FROM:
event occurs but causal antecedent is missing

TRIGGER:
audience detects a coherence gap + relevant prior knowledge is available

TO:
plausible causal bridge inferred
```

If bridge fails:
```text
TO:
unresolved gap / confusion risk
```

---

## T2 — Action without stated motive → Inferred goal model

```text
FROM:
action known, motive unstated

TRIGGER:
context supports goal-directed interpretation

TO:
goal inferred and linked to action
```

---

## T3 — Inferred/active goal → Strengthened goal model

```text
FROM:
goal active but potentially fragile

TRIGGER:
goal rementioned or action strongly consistent with it

TO:
goal remains highly accessible / explanatory
```

---

## T4 — Old goal active → New goal active / old goal suppressed

```text
FROM:
old goal currently explains action

TRIGGER:
new goal becomes more causally relevant

TO:
new goal becomes current explanatory frame
old goal accessibility reduced
```

---

## T5 — Desire-based intention → Belief-constrained intention

```text
FROM:
audience predicts intention from desire

TRIGGER:
character belief/knowledge information becomes relevant

TO:
intention maintained, inhibited, or made uncertain
```

---

## T6 — Dormant prior fact → Reactivated causal support

```text
FROM:
fact previously known but not currently active

TRIGGER:
new event makes it causally relevant

TO:
prior fact reactivated in the working model
```

---

## T7 — Coherent model → Model conflict

```text
FROM:
one causal/goal model currently dominates

TRIGGER:
incoming event contradicts expected action/cause/goal

TO:
conflict / inhibition / revision-needed state
```

The later transition from conflict to reframe belongs partly to E1-02 and E2-03.

---

## T8 — Ambiguous cause → Competing causal hypotheses

```text
FROM:
outcome known but cause underdetermined

TRIGGER:
several explanations fit available facts

TO:
multiple candidate causal models remain active
```

Evidence status:
BRIDGE / provisional.

---

## T9 — Isolated event → Integrated causal-network event

```text
FROM:
event represented with few meaningful relations

TRIGGER:
cause/consequence links become established

TO:
event becomes structurally integrated / more central
```

Do not equate this with guaranteed engagement.

---

# 5. Important boundaries and failure conditions

## 5.1 Causal omission is not automatically productive

Useful gap:
- audience knows enough to infer
- missing relation is relevant
- inference space is constrained

Bad gap:
- necessary premises absent
- causal distance too large
- world knowledge unavailable
- many uncontrolled explanations fit

---

## 5.2 Goal inference can be wrong

Audiences may over-infer intention from desire.

Therefore:

```text
goal/desire cue
→ audience inference
```

is not the same as:

```text
objective character intention
```

---

## 5.3 Audience knowledge and character knowledge must remain separate

A character can:
- want X,
- not know information required to pursue X,
- while the audience does know it.

The engine must not leak omniscient audience information into the character model.

---

## 5.4 Goal completion, irrelevance, suppression, and forgetting are different

The research does not justify collapsing them.

---

## 5.5 Causal centrality is not a universal quality metric

It predicts importance/memory/comprehension in the cited research.

It does not directly prove:
- emotional impact
- aesthetic value
- platform retention
- satisfaction
- persuasion

---

## 5.6 Direct evidence is still dominated by reading studies

There is valuable recent audiovisual support, but much of the fine-grained goal inference evidence comes from text reading.

Application to radio/video/film is plausible and partially supported, but should retain domain limits.

---

## 5.7 Population differences matter

Child and L2 studies show that causal/goal integration can differ with development and language proficiency.

Do not generalize all processing dynamics to all audiences identically.

---

# 6. Possible Story Decisions enabled by E1-01

The Engine may use E1-01 to ask:

### Causal coherence
- Does the next event have a plausible cause in the current audience model?
- If not, is the missing cause intentionally inferable or simply absent?
- Is there enough prior information to bridge the gap?

### Goal coherence
- What goal currently explains this character's action?
- Is the goal explicit or inferred?
- Is that goal still active?
- Has a newer goal made it obsolete?
- Does the character know enough to plausibly form the inferred intention?

### Information control
- Should a cause be revealed now?
- Can it remain implicit?
- Should prior information be reactivated before it becomes necessary?
- Should multiple causal explanations remain open?

### Conflict handling
- Does new information strengthen the current model?
- Fill a missing link?
- Introduce a competing cause?
- Suppress an old goal?
- Create a model conflict requiring later revision?

### Constraint checking
- Is the engine inventing a motive not supported by facts?
- Is it assigning knowledge to a character who does not possess it?
- Is it collapsing ambiguity too early?
- Is it confusing audience inference with story fact?

---

# 7. Foundation Pair handoff to E1-02

E1-01 describes **what model the audience can hold**.

E1-02 must investigate **when and how incoming change causes that model/state to update**.

Unresolved handoff questions:

1. What magnitude/type of change causes the audience to create a new event model rather than update the existing one?
2. Which dimensions of change matter most:
   - time
   - location
   - protagonist
   - causality
   - intentionality
   - goal
   - risk
   - relation
   - knowledge?
3. When does model conflict cause:
   - local repair,
   - event boundary,
   - state replacement,
   - or coexistence of multiple interpretations?
4. How long do old goals/causal relations remain accessible after a state change?
5. How should the Engine distinguish:
   - model enrichment,
   - model revision,
   - model replacement,
   - event segmentation?
6. When does a causally surprising event produce a **state update** rather than merely comprehension difficulty?

These questions are **not answered in E1-01**.

---

# 8. Handoffs to later P0 items

## E1-03 — Appraisal → Emotion / Judgment

E1-01 can establish:
- who caused what,
- who intended what,
- whether a goal succeeded/failed,
- whether control/constraint changed.

E1-03 must determine how those model changes alter:
- responsibility,
- controllability,
- certainty,
- goal relevance,
- legitimacy,
- emotion/judgment.

---

## E2-01 — Information Gap / Curiosity

E1-01 establishes whether a causal gap is:
- recognized,
- bridgeable,
- meaningful.

E2-01 must determine when that gap becomes curiosity rather than confusion.

---

## E2-02 — Narrative Expectation / Suspense

E1-01 supplies:
- active goals,
- plausible consequences,
- competing causal paths.

E2-02 must determine how these become suspense/expectation.

---

## E2-03 — Expectation Violation → Surprise → Reappraisal / Reframe

E1-01 identifies:
- existing model,
- contradiction,
- model conflict.

E2-03 must determine:
- when violation produces surprise,
- when it produces reappraisal/reframe,
- when it feels arbitrary/incoherent,
- audience judgment and boundary conditions.

---

# 9. Does P0 need revision after E1-01?

## No major structural revision

The Experience-First P0 ordering remains valid.

E1-01 strongly supports keeping E1-01 and E1-02 as a **Foundation Pair**.

## Minor refinements suggested

### Refinement A — audience model should explicitly separate:
- causal model
- character goal model
- character belief/knowledge
- audience knowledge

Reason:
Goal/intention inference can be distorted if desire, belief, audience knowledge, and character knowledge are collapsed.

### Refinement B — "model conflict" should become an explicit intermediate state

Do not jump directly:

```text
old model → reframe
```

Prefer:

```text
old model
→ conflict detected
→ inhibit / bridge / compete / revise / remain unresolved
→ possible new model
```

This preserves the neutral design of E2-03.

### Refinement C — causal relevance should be considered in state accessibility

A fact can be known but not currently active.

This suggests Story State may eventually distinguish:
- stored known information
- currently active/causally relevant information

E1-02 should test how much of this belongs in runtime state.

---

# 10. Minimal evidence firewall summary

Only source-level distinctions necessary for application were retained.

## DIRECT — primary E1-01 foundation

- Graesser, Singer & Trabasso (1994), narrative inference / coherence
- Trabasso & van den Broek (1985), causal network and memory/importance
- Trabasso & Sperry (1985), causal relatedness and importance
- Suh & Trabasso (1993), goal-plan inference
- Poynor & Morris (2003), inferred goals
- Linderholm et al. (2004), changing goals / suppression
- Albrecht et al. (1995), perspective and goal accessibility
- Haigh & Bonnefon (2015), belief/desire/intention inference
- Sundermeier et al. (2005), causal relevance/reactivation
- Kim (1999), causal bridging and interestingness
- Ackerman (1986), causal coherence and inference under unexpected outcomes
- Song et al. (2021), causal integration and naturalistic movie comprehension
- Lee & Chen (2022), causal narrative network centrality in movies

## BRIDGE

- broader causal reasoning under multiple explanations
- knowledge-revision research for conflict/revision
- developmental and L2 work for boundary conditions

## APPLICATION_HYPOTHESIS

- Story State enum/status design
- exact model-conflict transitions
- multi-causal hypothesis weighting
- runtime reactivation policy

---

# 11. Core source list

1. Graesser AC, Singer M, Trabasso T. Constructing inferences during narrative text comprehension. Psychological Review. 1994;101(3):371–395. DOI: 10.1037/0033-295X.101.3.371
2. Trabasso T, van den Broek P. Causal thinking and the representation of narrative events. Journal of Memory and Language. 1985;24(5):612–630. DOI: 10.1016/0749-596X(85)90049-X
3. Trabasso T, Sperry LL. Causal relatedness and importance of story events. Journal of Memory and Language. 1985;24(5):595–611. DOI: 10.1016/0749-596X(85)90048-8
4. Zwaan RA, Langston MC, Graesser AC. The Construction of Situation Models in Narrative Comprehension: An Event-Indexing Model. Psychological Science. 1995;6(5):292–297. DOI: 10.1111/j.1467-9280.1995.tb00513.x
5. Suh SY, Trabasso T. Inferences during Reading: Converging Evidence from Discourse Analysis, Talk-Aloud Protocols, and Recognition Priming. Journal of Memory and Language. 1993;32(3):279–300. DOI: 10.1006/jmla.1993.1015
6. Poynor DV, Morris RK. Inferred goals in narratives: evidence from self-paced reading, recall, and eye movements. J Exp Psychol Learn Mem Cogn. 2003;29(1):3–9. DOI: 10.1037/0278-7393.29.1.3
7. Linderholm T, Gernsbacher MA, van den Broek P, et al. Suppression of Story Character Goals During Reading. Discourse Processes. 2004;37(1):67–78. DOI: 10.1207/s15326950dp3701_4
8. Albrecht JE, O'Brien EJ, Mason RA, Myers JL. The role of perspective in the accessibility of goals during reading. J Exp Psychol Learn Mem Cogn. 1995;21(2):364–372. DOI: 10.1037/0278-7393.21.2.364
9. Haigh M, Bonnefon J-F. Eye Movements Reveal How Readers Infer Intentions From the Beliefs and Desires of Others. Experimental Psychology. 2015;62(3):206–213. DOI: 10.1027/1618-3169/a000290
10. Sundermeier BA, van den Broek P, Zwaan RA. Causal coherence and the availability of locations and objects during narrative comprehension. Memory & Cognition. 2005;33(3):462–470. DOI: 10.3758/BF03193063
11. Kim S-I. Causal bridging inference: A cause of story interestingness. British Journal of Psychology. 1999;90(1):57–71. DOI: 10.1348/000712699161260
12. Ackerman BP. Referential and causal coherence in the story comprehension of children and adults. Journal of Experimental Child Psychology. 1986;41(2):336–366. DOI: 10.1016/0022-0965(86)90044-5
13. Song H, Park BY, Park H, Shim WM. Cognitive and Neural State Dynamics of Narrative Comprehension. Journal of Neuroscience. 2021. Naturalistic movie comprehension.
14. Lee H, Chen J. Predicting memory from the network structure of naturalistic events. Nature Communications. 2022;13:4235. DOI: 10.1038/s41467-022-31965-2
15. van den Broek P. Causal Inferences and the Comprehension of Narrative Texts. Psychology of Learning and Motivation. 1990;25:175–196. DOI: 10.1016/S0079-7421(08)60255-8

---

# 12. Final result

The most useful E1-01 model is not:

```text
FACTS → NEXT EVENT
```

but:

```text
FACTS / EVENTS
   ↓
AUDIENCE CAUSAL MODEL
+
CHARACTER GOAL / BELIEF MODEL
   ↓
ACTIVE CAUSE / ACTIVE GOAL / UNRESOLVED GAP / COMPETING EXPLANATION
   ↓
NEW INFORMATION
   ↓
MAINTAIN / STRENGTHEN / BRIDGE / REACTIVATE / SUPPRESS / CONFLICT / REVISE
   ↓
NEXT EXPECTATION-READY STATE
```

This is the E1-01 contribution to the Foundation Pair.

E1-02 must determine when these model changes become actual **Event / State Updates**.
