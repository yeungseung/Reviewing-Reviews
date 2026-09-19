# Q1-01 EVIDENCE TAXONOMY — Precision Research Report v0

> Track: A — Epistemic Integrity  
> Research ID: Q1-01  
> Legacy origin: #60 Evidence Layer / Theme 1  
> Status: PRECISION RESEARCH — PROVISIONAL COMPLETE  
> Research date: 2026-09-19  
> Product target: LONGFORM STORY ENGINE Evidence Layer

---

# 1. Research Target

## Core question

How should the Story Engine classify a nonfiction claim and its supporting material so that it can preserve provenance, inference distance, causal status, scope, uncertainty, and source independence without silently upgrading weak or indirect evidence into factual certainty?

## Legacy hypothesis under audit

The legacy Evidence Layer proposed one flat list:

- FACT
- SOURCE CLAIM
- OPINION
- REVIEW
- COMMENT
- ANECDOTE
- INFERENCE
- FORECAST

This research does **not** assume the list is wrong, but tests whether those labels belong to one mutually exclusive taxonomy.

---

# 2. Executive Findings

## Finding 1 — The legacy eight labels do not form one clean taxonomy

**Verdict: REFRAME**

The eight labels mix different dimensions.

Examples:

- COMMENT is primarily a **communication/source form**
- REVIEW is a **communication/source form** that may contain observation, opinion, comparison, or inference
- ANECDOTE is an **evidence scope/form**
- INFERENCE is an **epistemic relationship**
- FORECAST is a **future-oriented claim type**
- OPINION may be a **judgment type**
- FACT is not a source form at all; it is closer to the status assigned to a claim after sufficient verification

A comment can contain:
- an observation,
- an anecdote,
- an opinion,
- an inference,
- or a forecast.

Therefore COMMENT and INFERENCE cannot be mutually exclusive labels on the same axis.

## Finding 2 — Evidence quality is not safely represented by one universal hierarchy

**Verdict: STRONG SUPPORT for multi-dimensional assessment**

Major evidence frameworks assess multiple properties rather than relying only on source/study category.

Cochrane/GRADE assesses certainty using domains including:
- risk of bias
- inconsistency
- indirectness
- imprecision
- publication bias

AHRQ additionally emphasizes:
- directness
- applicability/generalizability
- consistency
- precision
- risk of bias

Cochrane qualitative evidence guidance uses a different confidence logic for qualitative synthesis and highlights:
- methodological limitations
- coherence
- adequacy of data
- relevance

This matters because the correct evidence form depends on the question.

Examples:
- randomized trials may be useful for causal intervention effects
- qualitative evidence may be better suited to experience, feasibility, meaning, context, or implementation
- a first-hand testimony may be strong evidence that one person reports an experience but weak evidence for population prevalence
- a review may be useful for one consumer experience while unsuitable for estimating how common that experience is

## Finding 3 — Primary vs secondary is a provenance relation, not a truth score

**Verdict: VERIFIED DISTINCTION / REJECT universal ranking**

The Library of Congress defines primary sources as original/first-hand records and secondary sources as later accounts that analyze, interpret, summarize, or criticize.

However, journalism and historical source practices require:
- sourcing
- context
- corroboration
- source motive / perspective evaluation

Reuters explicitly prefers named sources and cross-checking, and treats source position, track record, motive, and corroboration as relevant to reliability.

Therefore:

> PRIMARY ≠ TRUE  
> SECONDARY ≠ WEAK

A primary source may be:
- mistaken
- biased
- deceptive
- incomplete
- nonrepresentative

A high-quality secondary synthesis may integrate many stronger independent sources.

## Finding 4 — Evidence strength must be claim-relative

**Verdict: STRONG SUPPORT**

The same material can be strong for one claim and weak for another.

Example:

> “This reviewer says the battery lasted three hours.”

A verified review is direct evidence that this reviewer made that statement.

It is only anecdotal evidence that the device may behave that way in a case.

It is not sufficient evidence that:
- typical battery life is three hours,
- most owners have the same problem,
- or the product design caused the failure.

Therefore the Engine must classify **the relationship between evidence and the specific claim**, not just the evidence item itself.

## Finding 5 — Source credibility and information/claim credibility must remain separable

**Verdict: STRONG SUPPORT**

ODNI analytic standards require analysts to:
- describe the quality and credibility of sources, data, and methods
- express uncertainty in judgments
- distinguish underlying information from assumptions and judgments
- consider alternatives

This supports a key Engine design rule:

> A credible source can make an uncertain claim, and a less authoritative source can provide a directly verifiable observation.

Do not collapse SOURCE QUALITY and CLAIM SUPPORT into one score.

## Finding 6 — Expert judgment is a distinct evidence form, not automatic fact

**Verdict: STRONG SUPPORT**

Structured expert judgment literature treats expert elicitation as useful when data/models cannot fully answer a question, but explicitly treats expert judgment as something that should be structured, calibrated, and validated where possible.

Expertise therefore changes the evidential role of a judgment but does not convert the judgment into direct observation.

## Finding 7 — Reviews/comments can be evidence, but population inference requires sampling support

**Verdict: STRONG SUPPORT**

Research on online reviews documents self-selection, extremity, platform, and measurement biases.

Therefore:

- a review can evidence the reviewer’s reported experience
- comments can evidence that reactions exist
- a collection of comments may be useful for exploratory theme discovery
- review/comment counts are not automatically representative of all users, buyers, or viewers

Population claims require a defensible sampling frame or explicit limitation.

## Finding 8 — Observation, association, causal inference, interpretation, and forecast must be separated

**Verdict: CORE ENGINE REQUIREMENT**

Several audit failures occurred when the corpus performed silent upgrades:

- theory → causal experiment
- association → causal mechanism
- qualitative mechanism → exact percentage
- bridge-domain finding → direct Story Engine law
- forecast/inference → fact
- general psychology → platform KPI

The Evidence Layer should make these upgrades structurally difficult.

---

# 3. Legacy Label Collision Matrix

| Legacy label | Claim type | Evidence form | Source/form | Inference status | Temporal status | Can overlap? |
|---|---:|---:|---:|---:|---:|---|
| FACT | partial | no | no | low/verified status | any | yes |
| SOURCE CLAIM | partial | no | yes/provenance relation | varies | any | yes |
| OPINION | yes | sometimes | sometimes | judgment | any | yes |
| REVIEW | no | yes | yes | varies | usually retrospective/current | yes |
| COMMENT | no | yes | yes | varies | any | yes |
| ANECDOTE | partial | yes | yes | limited-scope | usually past/current | yes |
| INFERENCE | yes | no | no | yes | any | yes |
| FORECAST | yes | sometimes model-based | no | yes | future | yes |

## Interpretation

The legacy list contains at least four separate conceptual axes.

A flat classification forces false exclusivity.

Example:

```text
YouTube comment:
"My TV died after two weeks. I think the power board overheats, and this model will fail for everyone."
```

This single COMMENT contains:

- reported personal event → ANECDOTAL / TESTIMONIAL OBSERVATION
- causal interpretation → INFERENCE
- population generalization → unsupported extrapolation
- future statement → FORECAST

One label cannot preserve this structure.

---

# 4. Framework Comparison

| Framework / tradition | Unit classified | Main dimensions | Hierarchy? | Key contribution | Main limitation for Story Engine |
|---|---|---|---|---|---|
| Cochrane / GRADE | body of quantitative evidence for an outcome | bias, inconsistency, indirectness, imprecision, publication bias | calibrated certainty, not simple source rank | shows evidence certainty is multidimensional | designed for health intervention evidence |
| AHRQ Methods Guide | body/study applicability and evidence | bias, consistency, directness, precision, applicability | domain-specific | separates internal quality and real-world applicability | healthcare context |
| Cochrane qualitative / CERQual | synthesized qualitative finding | methodological limitations, coherence, adequacy, relevance | confidence categories | proves qualitative evidence needs question-appropriate logic | not a generic nonfiction taxonomy |
| Journalism standards (SPJ/Reuters) | reported information/source | verification, original sourcing, attribution, context, corroboration | no universal ladder | provenance and corroboration are operational requirements | ethical/professional standards, not causal methodology |
| Library of Congress source distinction | source provenance | primary vs secondary | no truth hierarchy | provenance role is distinct from interpretation | history-oriented framing |
| ODNI analytic standards | analytic judgment | source quality, uncertainty, assumptions/judgments, alternatives | no universal source ladder | separates raw information from analytic judgment | intelligence context |
| Federal Rules of Evidence | admissible testimony/evidence | personal knowledge, lay opinion, expert testimony, direct/circumstantial | procedural/legal | useful distinctions between observation and opinion/expertise | admissibility ≠ scientific truth |
| Structured expert judgment | expert estimates | expertise, elicitation, calibration, aggregation | performance may be calibrated | expert opinion is evidence under uncertainty, not direct fact | formal elicitation is expensive and domain-specific |
| Online review research | user-generated observations/opinions | selection bias, extremity, measurement/platform bias | no | comments/reviews are not automatically representative | specific to user-generated review systems |

---

# 5. Category Boundary Findings

## 5.1 Observation

### Definition
A report of something directly perceived or recorded.

### Includes
- eyewitness observation
- directly observed event
- instrument reading, if the instrument and method are separately documented

### Excludes
- explanation of why it happened
- generalization beyond the observation
- prediction

### Failure mode
Observation silently becomes interpretation.

---

## 5.2 Measurement

### Definition
A value generated by a defined measurement procedure.

### Includes
- survey proportion
- instrument reading
- counted events
- retention metric

### Requires
- denominator
- method
- population/sample
- time/window
- uncertainty where relevant

### Failure mode
A number is treated as inherently objective despite measurement/sampling bias.

---

## 5.3 Descriptive claim

### Definition
A claim describing observed characteristics, frequencies, states, or patterns.

### Does not by itself imply
- cause
- explanation
- universal generalization

---

## 5.4 Associational claim

### Definition
A claim that variables/events co-vary or are statistically related.

### Must not be upgraded to
CAUSAL_CLAIM without an appropriate identification strategy.

---

## 5.5 Causal claim

### Definition
A claim that changing/exposing X produces or contributes to change in Y under specified conditions.

### Requires explicit causal basis
Potential bases include:
- randomized manipulation
- credible quasi-experimental design
- strong causal identification strategy
- domain-specific causal evidence

### Failure mode
“Causal” in the semantic subject of a paper is confused with causal identification in research design.

---

## 5.6 Interpretation

### Definition
A reasoned account of what observations/evidence mean.

### Key rule
Interpretation may be well supported without becoming observation.

---

## 5.7 Expert judgment

### Definition
A judgment relying on specialized knowledge, skill, experience, or structured elicitation.

### Key rule
Expert status affects relevance and potential credibility, not truth status.

---

## 5.8 Normative judgment

### Definition
A claim about what should be done, what is fair, ethical, valuable, acceptable, or preferable.

### Key rule
Do not present normative conclusions as empirical findings.

---

## 5.9 Estimate

### Definition
An inferred value for an uncertain quantity.

Examples:
- estimated audience size
- estimated cost
- modeled prevalence

### Key rule
Estimate ≠ observation.

---

## 5.10 Forecast / projection

### Definition
A future-oriented claim based on assumptions, models, judgment, trends, or scenarios.

### Key rule
Authoritative source status does not make the future outcome a fact.

Store:
- forecast horizon
- assumptions
- model/method if known
- uncertainty if reported

---

# 6. Evidence Form Findings

Evidence form should be stored separately from claim type.

Candidate forms:

- DOCUMENT_RECORD
- PHYSICAL_OR_DIGITAL_ARTIFACT
- DATASET_STATISTIC
- EXPERIMENT
- QUASI_EXPERIMENT
- OBSERVATIONAL_STUDY
- QUALITATIVE_STUDY
- TESTIMONY_INTERVIEW
- CASE_REPORT
- ANECDOTE
- EXPERT_JUDGMENT
- USER_REVIEW
- COMMENT_SOCIAL_REACTION
- SYSTEMATIC_REVIEW_META_ANALYSIS
- NARRATIVE_REVIEW
- THEORY_CONCEPTUAL
- MODEL_SIMULATION
- OFFICIAL_STATEMENT
- SECONDARY_REPORTING

A source can produce several claim types.

Example:
An EXPERIMENT can report:
- descriptive measurements,
- associations,
- causal estimates,
- interpretations.

Therefore study/evidence form must not replace claim classification.

---

# 7. Primary vs Secondary Source

## Research conclusion

Keep provenance level, but never use it as the master quality score.

Candidate provenance labels:

- ORIGINAL_RECORD
- FIRSTHAND_SOURCE
- PRIMARY_RESEARCH
- SECONDARY_SYNTHESIS
- SECONDARY_REPORTING
- TERTIARY_SUMMARY
- DERIVATIVE_REPOST
- UNKNOWN

The word PRIMARY is domain-dependent.

Examples:
- history: contemporaneous document / firsthand record
- science: original research publication
- journalism: reporter/source closest to the event or original document

The Engine should therefore store a specific provenance role rather than rely on PRIMARY alone where ambiguity matters.

---

# 8. Anecdote, Case, Testimony, Interview, Qualitative Evidence

These must not be collapsed.

## ANECDOTE

Usually an informal report of one/few experiences.

Strong for:
- existence of a reported case
- hypothesis generation
- human illustration

Weak for:
- prevalence
- typicality
- population effect size

## TESTIMONY / INTERVIEW

Can be direct evidence of:
- what a person reports seeing
- their own experience
- their beliefs/intentions

Requires consideration of:
- personal knowledge
- memory
- incentives
- context
- corroboration

## CASE REPORT / CASE STUDY

More structured than anecdote.

May provide:
- detailed causal-process hypotheses
- rare-event documentation
- contextual mechanism information

Does not automatically establish population frequency.

## QUALITATIVE STUDY

Must not be treated as “just anecdotes.”

Systematic qualitative research can use:
- explicit sampling
- structured collection
- analytic methods
- cross-case synthesis

Its strength should be evaluated for the type of question it answers.

---

# 9. Expert Opinion

## Research conclusion

Retain EXPERT_JUDGMENT as an evidence form / claim source.

Do not create:

```text
expert = fact
```

Structured expert judgment research demonstrates why:
- expertise can be useful where empirical data are incomplete
- judgments can be elicited systematically
- calibration matters
- expert accuracy varies

Candidate metadata:

- expertise_domain
- expertise_relevance
- elicitation_method
- independent_experts_count
- consensus_or_disagreement
- calibration_known
- conflicts_of_interest
- supporting_empirical_evidence

Most of these should be optional in normal content research.

---

# 10. Reviews, Comments, Social Reactions

## Core distinction

A review/comment can support at least four very different claims.

### Level A — Existence

> “At least one user reported X.”

A verified comment/review can directly support this.

### Level B — Theme existence

> “Multiple users mention X.”

Requires transparent collection/coding and duplicate/bot awareness.

### Level C — Frequency within collected comments

> “18% of collected reviews mention X.”

Requires defined corpus and method.

### Level D — Population prevalence

> “18% of customers experience X.”

Requires a defensible sampling relationship to customers/users.

Public reviews usually do not provide this automatically because review participation is self-selected and platform-dependent.

## Engine rule

```text
COMMENT / REVIEW
→ may support individual experience or observed discourse
→ must not auto-upgrade to representative public opinion
```

---

# 11. Statistical / Aggregate Evidence

Minimum fields for aggregate numerical claims:

- population
- sampling_frame
- sample_size
- denominator
- measurement_definition
- study_design
- time_period
- estimate
- uncertainty_interval if reported
- missingness/nonresponse if relevant
- representativeness
- causal_status
- source

For Story Engine use, these fields can be partially optional, but absence should reduce what language is allowed.

---

# 12. Directness and Domain Transfer

The current Audit shows that DIRECTNESS is essential.

Proposed directness values:

- DIRECT
- INDIRECT
- BRIDGE
- APPLICATION_HYPOTHESIS
- DOES_NOT_TEST

## DIRECT

Evidence directly studies the target construct/population/content relation.

## INDIRECT

Evidence addresses a close proxy or part of the claim.

## BRIDGE

Evidence comes from another domain but provides a plausible mechanism.

## APPLICATION_HYPOTHESIS

The Story Engine proposes a production implication that has not been directly tested.

## DOES_NOT_TEST

The cited work is relevant background but does not test the claimed proposition.

This dimension directly prevents:
- infant attention → adult longform retention law
- animal habituation → exact story pacing law
- general emotion theory → YouTube completion-rate percentage

---

# 13. Source Independence

Independent source count must be separated from citation count.

Candidate values:

- INDEPENDENT
- SAME_DATASET
- SAME_RESEARCH_PROGRAM
- DERIVED_FROM_SAME_ORIGINAL
- DUPLICATE_RECORD
- UNKNOWN

Example:

Three reviews of the same original study are not three independent experimental replications.

This is especially important for the current corpus because source-family duplication is already documented.

---

# 14. Flat vs Multi-Axis Architecture Test

## Model A — Flat taxonomy

Example values:
FACT / OPINION / REVIEW / COMMENT / ANECDOTE / INFERENCE / FORECAST

### Advantages
- simple
- fast to annotate
- easy to display

### Failures
- categories overlap
- mixes source type and claim type
- cannot represent review + anecdote + inference simultaneously
- cannot express directness
- cannot express causal status
- cannot express population scope
- cannot express source independence
- encourages one-dimensional “weight” thinking

### Verdict
**REJECT as canonical internal schema**

A simplified display label can still be generated from the richer schema.

---

## Model B — Multi-axis Evidence Object

### Advantages
- preserves provenance
- separates claim from evidence form
- separates source quality from claim support
- expresses domain transfer
- blocks causal upgrades
- allows review/comment evidence without overgeneralization
- compatible with later confidence language and empirical validation

### Costs
- more annotation fields
- some inter-rater ambiguity
- requires conflict rules
- must be usability-tested

### Verdict
**ADOPT AS PROVISIONAL ARCHITECTURE**

---

# 15. Candidate Story Engine Evidence Object

Minimum required core:

```yaml
claim:
  claim_text:
  claim_type:

evidence:
  evidence_form:
  provenance_role:
  directness:
  support_relation:

scope:
  target_scope:
  evidence_scope:
  representativeness:

causal:
  causal_status:

lineage:
  source_id:
  source_verification:
  source_family:
  independence:

limits:
  known_limitations: []
  unresolved: []
```

Optional modules:

```yaml
quantitative:
  sample_size:
  denominator:
  effect_estimate:
  uncertainty:
  time_period:

expert:
  expertise_domain:
  elicitation_method:
  consensus_status:

forecast:
  horizon:
  assumptions: []
  model_or_method:

qualitative:
  sampling:
  analytic_method:
  context:

platform_reaction:
  collection_method:
  deduplication:
  sampling_bias:
```

---

# 16. Story Engine Field Map

| Engine field | Required? | Downstream decision | Primary error prevented |
|---|---:|---|---|
| claim_type | yes | determines what verb/causal language is permissible | interpretation → fact |
| evidence_form | yes | determines what the evidence can naturally support | comment → population evidence |
| provenance_role | yes | tracks origin / derivative chain | secondary summary mistaken for original |
| source_verification | yes | blocks unresolved source from numeric support | bibliographic conflation |
| directness | yes | controls domain-transfer language | bridge → direct law |
| support_relation | yes | identifies whether source actually tests claim | relevant citation → support |
| causal_status | yes for causal-sounding claims | controls cause verbs | association → causation |
| target_scope | yes | identifies claim population/unit | case → population |
| evidence_scope | yes | identifies what was actually observed | sample scope inflation |
| representativeness | conditional | permits/blocks prevalence generalization | reviews → all users |
| source_family | recommended | deduplication | duplicate citations → fake replication |
| independence | recommended | confidence aggregation | same dataset counted repeatedly |
| quantitative fields | conditional | numeric language | injected percentage |
| uncertainty fields | handoff Q1-02 | wording calibration | false certainty |

---

# 17. What the Engine Must Not Infer

The Evidence Layer should implement explicit forbidden upgrades.

```text
PRIMARY_SOURCE -> TRUE                  [FORBIDDEN]
SECONDARY_SOURCE -> WEAK                [FORBIDDEN]
EXPERT -> FACT                          [FORBIDDEN]
COMMENT -> POPULATION_OPINION           [FORBIDDEN]
REVIEW -> REPRESENTATIVE_EXPERIENCE     [FORBIDDEN]
ANECDOTE -> PREVALENCE                  [FORBIDDEN]
ASSOCIATION -> CAUSATION                [FORBIDDEN]
THEORY -> EXPERIMENTAL_EFFECT           [FORBIDDEN]
BRIDGE -> DIRECT_STORY_EVIDENCE         [FORBIDDEN]
FORECAST -> FUTURE_FACT                 [FORBIDDEN]
CITATION_COUNT -> INDEPENDENT_SUPPORT   [FORBIDDEN]
SOURCE_PRESTIGE -> CLAIM_VERIFICATION   [FORBIDDEN]
QUALITATIVE_RESULT -> NUMERIC_EFFECT    [FORBIDDEN]
GENERAL_PSYCHOLOGY -> PLATFORM_KPI      [FORBIDDEN]
```

---

# 18. Evidence Weight Boundary Table

| Material | Strong support for | Weak/insufficient for |
|---|---|---|
| eyewitness testimony | what witness reports/perceived | objective full event account without corroboration |
| official record | content/status of that record | truth of every claim inside the record |
| one user review | that user's reported experience | population prevalence |
| many self-selected reviews | discourse/themes among reviewers | representative population preference |
| representative survey | prevalence/opinion in target population within sampling limits | individual causal mechanism |
| randomized experiment | causal effect under studied conditions | universal generalization outside studied conditions |
| observational study | association/pattern | causal effect without identification |
| qualitative synthesis | experience/context/implementation/meaning | precise prevalence/effect size |
| expert judgment | informed estimate/interpretation | direct empirical fact |
| systematic review | synthesis of included evidence | guarantee against bias/indirectness |
| model forecast | conditional future estimate | known future outcome |
| theory paper | conceptual mechanism/framework | measured effect size |

---

# 19. Existing Corpus Stress-Test Summary

Detailed cases are stored separately in:
`Q1-01_STRESS_TEST_v0.md`

High-level result:

The multi-axis schema correctly exposes all eight tested audit failures.

It catches:

1. theoretical emotion paper → invented retention percentages
2. conflated QUEST bibliography → quantitative causal claims
3. Event-Indexing mechanism → invented sample/threshold/application
4. animal habituation → longform pacing law
5. narrative memory prediction error → dopamine/pleasure reinterpretation
6. wrong Annie Lang DOI → exact cut-frequency rules
7. infant complexity preference → adult narrative uncertainty optimum
8. Damasio hypothesis → knowledge-retention effect sizes

No single flat label can expose all eight failure modes.

---

# 20. Counterevidence / Boundary Conditions

## 20.1 No universal evidence ladder

The research does not support one universal hierarchy that ranks all evidence forms for every question.

A randomized experiment is not automatically “better” than qualitative research when the question concerns:
- lived experience
- implementation barriers
- meaning
- context

Likewise, qualitative evidence is not the appropriate source for a precise intervention effect size.

## 20.2 Primary source is not inherently reliable

Firsthand status answers:

> Where did this information originate?

It does not fully answer:

> Is it accurate?

## 20.3 Secondary synthesis may be stronger than one primary study

A high-quality systematic synthesis can integrate:
- multiple studies
- bias assessment
- consistency
- precision
- directness

This may produce a more reliable conclusion than one original study.

## 20.4 Circumstantial / indirect evidence is not “bad evidence”

Indirect evidence can legitimately support an inference.

The issue is whether the inference steps are visible and justified.

## 20.5 More sources are not necessarily more independent evidence

Ten articles that repeat one press release or one original study may represent one source family.

## 20.6 Numerical evidence is not automatically stronger

A precise-looking number can be weak if:
- sampling is biased
- construct validity is poor
- measurement is unreliable
- model assumptions dominate
- uncertainty is ignored

---

# 21. Provisional Architecture

## Recommended internal architecture

**Multi-Axis Claim–Evidence Object**

Core layers:

```text
CLAIM TYPE
    +
EVIDENCE FORM
    +
PROVENANCE
    +
SOURCE VERIFICATION
    +
DIRECTNESS
    +
SUPPORT RELATION
    +
CAUSAL STATUS
    +
SCOPE / REPRESENTATIVENESS
    +
SOURCE FAMILY / INDEPENDENCE
    +
OPTIONAL DOMAIN MODULES
```

## Recommended user-facing simplification

The engine may later generate simple display labels such as:

- Verified record
- Direct measurement
- Study finding
- Expert judgment
- Personal experience
- Public reaction
- Inference
- Estimate
- Forecast
- Disputed / mixed

But these should be **rendered labels**, not the canonical storage schema.

---

# 22. Implication for Legacy #60

## Legacy 8-type disposition

| Legacy label | Disposition |
|---|---|
| FACT | REFRAME into claim verification/status, not Evidence Form |
| SOURCE CLAIM | SPLIT into provenance + source-reported claim |
| OPINION | KEEP as judgment class, distinguish expert/normative/personal |
| REVIEW | KEEP as evidence/source form |
| COMMENT | KEEP as evidence/source form |
| ANECDOTE | KEEP but distinguish from testimony/case/qualitative study |
| INFERENCE | KEEP as epistemic claim status/directness relation |
| FORECAST | KEEP as future-oriented claim type/module |

## Missing legacy dimensions

Add:

- causal status
- measurement/statistical evidence
- qualitative evidence
- study design
- provenance role
- source verification
- source family / independence
- scope
- representativeness
- directness
- support relation
- theory/conceptual evidence
- model/simulation

---

# 23. Handoff

## Q1-02 — Confidence / uncertainty language

Needs to decide how schema values map to language such as:
- confirmed
- supported
- suggests
- may
- estimated
- disputed
- unclear
- forecast

Q1-01 does not set a universal confidence phrase table.

## Q1-04 — Counterevidence / alternatives

Needs:
- support relation logic
- contradictory evidence
- competing explanations
- asymmetric evidence quality

## Q1-05 — Source monitoring / correction

Needs:
- provenance
- source verification
- source family
- derivative chains
- visual/document source labeling

## Track K — empirical validation

Needs to test:
- inter-rater agreement on claim_type
- evidence_form assignment
- directness assignment
- causal_status assignment
- representativeness
- source-family classification

Fields with poor reliability should be merged or given clearer decision rules.

---

# 24. Provisional Verdict

```yaml
research_id: Q1-01
construct: Evidence Taxonomy

architecture_test:
  flat_taxonomy:
    status: REJECT_AS_CANONICAL_SCHEMA
    strengths:
      - simple
      - fast
      - usable as display labels
    failures:
      - mixes multiple axes
      - overlapping categories
      - cannot express causal status
      - cannot express directness
      - cannot express scope
      - cannot express source independence

  multi_axis_taxonomy:
    status: PROVISIONALLY_ADOPT
    strengths:
      - preserves claim/evidence distinction
      - supports provenance
      - blocks silent evidence upgrades
      - supports domain transfer labeling
      - compatible with later confidence layer
    failures:
      - annotation complexity
      - requires inter-rater validation

  recommended_architecture: MULTI_AXIS_CLAIM_EVIDENCE_OBJECT

evidence_summary:
  strong_distinctions:
    - claim_type vs evidence_form
    - provenance vs truth
    - observation vs inference
    - association vs causation
    - individual_case vs population_claim
    - direct vs bridge evidence
    - source_count vs independent_source_family_count
    - expert_judgment vs empirical_observation
    - forecast vs observed_outcome
  conditional_distinctions:
    - primary vs secondary terminology across domains
    - evidence hierarchy terminology
  domain_specific_distinctions:
    - legal admissibility
    - GRADE certainty
    - intelligence confidence
  rejected_distinctions:
    - universal source-type truth ladder
    - primary_equals_stronger
  missing_from_legacy:
    - directness
    - causal_status
    - representativeness
    - source_independence
    - source_verification
    - study_design
    - qualitative_evidence
    - measurement
    - support_relation

confidence:
  source_integrity: HIGH
  taxonomy_support: HIGH_FOR_MULTI_AXIS_NEED
  cross_domain_transfer: MODERATE
  operational_utility: PROVISIONAL_HIGH
  quantitative_support: NOT_APPLICABLE

story_engine:
  required_fields:
    - claim_type
    - evidence_form
    - provenance_role
    - source_verification
    - directness
    - support_relation
    - causal_status
    - target_scope
    - evidence_scope
  optional_or_conditional_fields:
    - representativeness
    - source_family
    - independence
    - quantitative
    - expert
    - forecast
    - qualitative
    - platform_reaction
  forbidden_upgrades:
    - primary_to_true
    - expert_to_fact
    - anecdote_to_prevalence
    - association_to_causation
    - theory_to_experimental_effect
    - bridge_to_direct
    - forecast_to_fact
    - citation_count_to_independence
    - qualitative_to_invented_quantification
    - psychology_to_platform_kpi
  unresolved_questions:
    - confidence language calibration
    - field inter-rater reliability
    - minimal schema for production speed
    - source-family automation

recommended_status:
  - VERIFIED_MECHANISM
  - DESIGN_HEURISTIC
```

---

# 25. Core Sources

## Evidence synthesis / methodology

1. Schünemann HJ, Higgins JPT, Vist GE, Glasziou P, Akl EA, Skoetz N, Guyatt GH. Cochrane Handbook, Chapter 14: certainty of evidence.  
   Stable source: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-14

2. AHRQ Effective Health Care Program. Grading a Body of Evidence on Diagnostic Tests.  
   Stable source: https://effectivehealthcare.ahrq.gov/products/methods-guidance-tests-grading/methods

3. Atkins D, Chang SM, Gartlehner G, et al. Assessing applicability when comparing medical interventions. J Clin Epidemiol. 2011;64(11):1198-1207.  
   DOI / metadata referenced by AHRQ. Stable source: https://effectivehealthcare.ahrq.gov/products/methods-guidance-applicability/methods

4. Murad MH, Asi N, Alsawas M, Alahdab F. New evidence pyramid. Evidence-Based Medicine. 2016;21(4):125-127.  
   DOI: 10.1136/ebmed-2016-110401

5. Cochrane Handbook, Chapter 21: Qualitative evidence.  
   Stable source: https://www.cochrane.org/authors/handbooks-and-manuals/handbook/current/chapter-21

6. WHO summary of GRADE-CERQual qualitative evidence confidence.  
   Stable source: https://www.who.int/news/item/18-01-2018-new-series-published-to-support-the-use-of-qualitative-research-in-decision-making

## Journalism / provenance

7. Society of Professional Journalists. Code of Ethics — Seek Truth and Report It.  
   Stable source: https://www.spj.org/spj-code-of-ethics/

8. Reuters. Journalistic Standards — Accuracy / Sourcing.  
   Stable source: https://reutersagency.com/about/standards-values/

9. Library of Congress. What is a primary source?  
   Stable source: https://ask.loc.gov/faq/303148

## Analytical reasoning

10. Office of the Director of National Intelligence. ICD 203 / Objectivity and Analytic Standards.  
    Stable source: https://www.dni.gov/index.php/how-we-work/objectivity

11. Office of the Director of National Intelligence. Source Citations technical specification overview.  
    Stable source: https://www.dni.gov/index.php/ncsc-how-we-work/ncsc-know-the-risk-raise-your-shield/ncsc-awareness-materials/cyber-training-series/223-about/organization/chief-information-officer/2806-source-citations

## Expert judgment

12. Colson AR, Cooke RM. Expert Elicitation: Using the Classical Model to Validate Experts' Judgments. Review of Environmental Economics and Policy. 2018;12(1):113-132.  
    DOI: 10.1093/reep/rex022

## Legal comparative lane

13. Federal Rules of Evidence, Rule 602 — Personal Knowledge.  
    Stable source: https://www.law.cornell.edu/rules/fre/rule_602

14. Federal Rules of Evidence, Rule 702 — Expert Witnesses.  
    Stable source: https://www.law.cornell.edu/rules/fre/rule_702

15. Legal Information Institute — Direct and Circumstantial Evidence definitions.  
    Stable sources:
    - https://www.law.cornell.edu/wex/direct_evidence
    - https://www.law.cornell.edu/wex/circumstantial_evidence

## Review / social-reaction representativeness

16. Karaman H. Online Review Solicitations Reduce Extremity Bias in Online Review Distributions and Increase Their Representativeness. Management Science. 2020.  
    DOI: 10.1287/mnsc.2020.3758

17. Han S, Anderson CK. The Platform Matters: Selection and Measurement Bias in Online Reviews. Cornell Hospitality Quarterly. Published online 2025 / volume publication 2026.  
    DOI: 10.1177/19389655251327536

## Data provenance

18. NIST Research Data Framework (RDaF), metadata and provenance guidance.  
    Stable source: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/1500-18/NIST.SP.1500-18r2.html

---

# 26. Final one-sentence result

> The Story Engine should not ask “What type of evidence is this?” once; it should ask “What kind of claim is being made, what form of evidence supports it, where did that evidence come from, how directly does it support the claim, what scope can it justify, and which inference steps remain?”
