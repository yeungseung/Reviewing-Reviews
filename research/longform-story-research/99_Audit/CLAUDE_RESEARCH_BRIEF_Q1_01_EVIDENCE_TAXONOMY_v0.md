# CLAUDE RESEARCH BRIEF — Q1-01 Evidence Taxonomy v0

> Track: A — Epistemic Integrity  
> Precision Research ID: Q1-01  
> Legacy origin: #60 Evidence Layer / Research Theme 1 — Evidence Type 분류 검증  
> Status: EXECUTION BRIEF  
> Purpose: build a reusable Evidence Layer for the Story Engine, not merely a literature summary.

---

# 0. Task identity

## Research Objective

Investigate how evidence and claim types are distinguished across research methodology, science communication, journalism, documentary/investigative practice, and adjacent evidence-governance fields, then derive a traceable taxonomy that the Story Engine can use to classify claims before writing nonfiction scripts.

The task is **not** to prove the legacy 8-type list.

Legacy list:

- FACT
- SOURCE CLAIM
- OPINION
- REVIEW
- COMMENT
- ANECDOTE
- INFERENCE
- FORECAST

Treat this list as a hypothesis to audit.

The research must determine:

1. which labels represent genuinely distinct evidence/claim categories,
2. which labels belong to different classification axes,
3. which important categories are missing,
4. which distinctions are domain-specific rather than universal,
5. what minimum representation the Story Engine needs to preserve source provenance, inference distance, causal status, and generalizability.

---

# 1. Product question

The final Story Engine must be able to answer, for every meaningful nonfiction claim:

> What kind of claim is this, what evidence supports it, how directly does that evidence support it, and what can the script safely say without silently upgrading the evidence?

The intended product is an **Evidence Layer** that sits between research material and prose generation.

Candidate flow:

```text
SOURCE / OBSERVATION
        ↓
CLAIM
        ↓
EVIDENCE TYPE + PROVENANCE
        ↓
INFERENCE / DIRECTNESS
        ↓
SCOPE + GENERALIZABILITY
        ↓
CAUSAL STATUS
        ↓
UNCERTAINTY / CONTESTATION
        ↓
ALLOWED SCRIPT LANGUAGE
```

This flow is provisional and must be revised if research supports a better representation.

---

# 2. Legacy hypothesis to test

Legacy #60 assumes eight types can be used as a single Evidence Type taxonomy.

Critical audit question:

> Are FACT, SOURCE CLAIM, OPINION, REVIEW, COMMENT, ANECDOTE, INFERENCE, and FORECAST actually mutually comparable categories?

Do **not** assume yes.

A central possibility to test is that the legacy list mixes several orthogonal dimensions, for example:

- epistemic status of a claim,
- evidence form,
- source/provenance role,
- inference distance,
- temporal orientation,
- population scope,
- causal status.

This is a research hypothesis, not a predetermined conclusion.

---

# 3. Scope

## In scope

Research distinctions relevant to nonfiction story construction, including:

- fact vs claim
- observation vs interpretation
- direct evidence vs indirect evidence
- primary vs secondary vs tertiary source
- individual case / anecdote vs aggregate evidence
- testimony / interview / document / record / dataset
- expert opinion
- user review
- public comment / social reaction
- statistical evidence
- qualitative evidence
- correlational vs causal evidence
- descriptive vs explanatory claims
- inference
- estimate
- forecast / projection
- normative judgment
- consensus / disagreement
- source independence
- replication / corroboration
- representativeness and generalizability

## Out of scope for Q1-01

Do not expand this task into later Track A questions.

Specifically defer:

- exact confidence wording and uncertainty language → Q1-02
- emotional framing effects → Q1-03
- counterargument / alternative explanation modules → Q1-04
- correction and source-memory mechanisms → Q1-05
- vivid example vs representative evidence effects → Q1-06
- platform CTR / retention / watch-time claims → Track I
- final Story Engine confidence scoring formula → later synthesis

Q1-01 may identify fields needed by those later tasks, but must not pretend to solve them.

---

# 4. Required Research Questions

Answer all questions explicitly.

## RQ1 — Category validity

What established distinctions are used to separate:

- observed facts,
- source-reported claims,
- interpretations,
- opinions,
- anecdotal/case evidence,
- aggregate/statistical evidence,
- expert judgment,
- public reactions,
- inference,
- prediction/forecast?

Which distinctions are broadly reusable, and which are domain-specific?

## RQ2 — Axis problem

Does evidence classification work better as a single hierarchy or as multiple axes?

Test at minimum whether the following need to be represented separately:

1. **Claim epistemic type**
2. **Evidence form**
3. **Source provenance**
4. **Study / evidence design**
5. **Inference directness**
6. **Causal status**
7. **Population / scope**
8. **Temporal status**
9. **Support relationship**
10. **Source independence / corroboration**

Do not preserve an axis unless evidence or practical classification need justifies it.

## RQ3 — Primary vs secondary

What does “primary” and “secondary” mean across different domains?

Determine where the terms are stable and where they change meaning.

Important:
A primary source must **not** automatically be treated as more truthful or stronger than a secondary synthesis.

## RQ4 — Anecdote / case / testimony

How should the system distinguish:

- anecdote,
- case study,
- testimony,
- eyewitness account,
- interview,
- qualitative evidence,
- case series,
- illustrative example?

Determine what each can and cannot support.

## RQ5 — Opinion / expertise

When does expert judgment count as evidence, interpretation, or informed opinion?

Distinguish:

- domain expertise,
- expert elicitation,
- expert commentary,
- normative opinion,
- consensus statements.

## RQ6 — Review / comment / social reaction

What evidential role can:

- user reviews,
- comments,
- social posts,
- audience reactions

legitimately play?

Distinguish at minimum:

- evidence of one person's experience,
- evidence that a reaction exists,
- social signal,
- population prevalence claim.

## RQ7 — Statistical / aggregate evidence

What fields are necessary to prevent an aggregate result from being overstated?

Consider:

- sample/population,
- sampling method,
- denominator,
- uncertainty,
- effect size,
- study design,
- representativeness,
- replication/corroboration.

## RQ8 — Observation vs inference

What minimum representation prevents a Story Engine from turning:

- observation → interpretation,
- association → causation,
- interpretation → fact,
- theory → demonstrated mechanism,
- forecast → established outcome?

## RQ9 — Evidence weight

Can evidence “weight” be universally ranked?

Search specifically for critiques and limitations of universal evidence hierarchies.

Determine whether evidence strength is:

- question-dependent,
- domain-dependent,
- claim-dependent,
- design-dependent,
- or reasonably reducible to a universal scale.

## RQ10 — Story Engine representation

What is the smallest practical schema that preserves epistemically important distinctions without becoming unusably complex?

---

# 5. Comparative research lanes

Research must use multiple independent traditions because no single domain owns a universal evidence taxonomy.

## Lane A — Research methodology / evidence synthesis

Use for:

- study design
- causal inference
- systematic evidence
- hierarchy limitations
- quantitative vs qualitative evidence
- generalizability

Preferred source types:

- systematic methodology papers
- peer-reviewed research methods literature
- authoritative evidence-synthesis handbooks
- recognized institutional methodological standards

## Lane B — Journalism / investigative standards

Use for:

- attribution
- source verification
- on-record claims
- documents and records
- corroboration
- anonymous sources
- eyewitness accounts
- separating reporting from interpretation/opinion

Preferred sources:

- authoritative journalism standards
- professional handbooks
- peer-reviewed journalism research where relevant

## Lane C — Science / risk communication

Use for:

- fact vs uncertainty
- consensus
- expert judgment
- projection
- model-based inference
- communicating evidence status

Do not let Q1-01 drift into wording calibration; that belongs to Q1-02.

## Lane D — Legal / evidentiary reasoning

Use only comparatively for concepts such as:

- testimony
- documentary evidence
- expert evidence
- direct/circumstantial distinctions
- corroboration

Hard boundary:

Legal admissibility or burden-of-proof rules are **not** universal truth hierarchies and must not be imported directly into the Story Engine.

## Lane E — Forecasting / intelligence / analytic reasoning

Use where useful for:

- estimate vs forecast
- confidence
- inference from incomplete evidence
- source reliability vs information credibility
- alternative hypotheses

Again, domain-specific scoring systems must not be copied as universal fact.

---

# 6. Source hierarchy

Use source quality appropriate to the claim being researched.

## Priority 1 — Primary authoritative framework

Examples of acceptable source classes:

- official methodological handbooks
- professional standards documents
- peer-reviewed original methods/framework papers
- official definitions from recognized institutions

## Priority 2 — High-quality synthesis

- systematic reviews
- methodological reviews
- academic handbooks
- consensus or guideline documents

## Priority 3 — Explanatory secondary sources

Use only to discover terminology or locate primary materials.

They cannot be the sole support for a core taxonomy decision.

## Disallowed as core support

- SEO blogs
- uncited explainers
- AI-generated summaries
- anonymous listicles
- citation aggregators without source verification
- secondary summaries that cannot identify the original framework

---

# 7. Mandatory execution process

Claude must execute the following gates in order.

Do not jump directly to a taxonomy.

## GATE 0 — Input lock

Read before external research:

1. `99_Audit/EVIDENCE_COVERAGE_MATRIX_v0.md`
2. `99_Audit/RESEARCH_MAP_V2_DRAFT_v0.md`
3. `99_Audit/CLAUDE_PRECISION_RESEARCH_QUEUE_v0.md`
4. `99_Audit/AUDIT_LOG.md`
5. legacy `#60 — Evidence Layer` in the Master Research List

Record a short “Legacy assumptions under audit” section.

Do not treat existing Gemini conclusions as verified facts.

## GATE 1 — Construct decomposition

Before searching for validation, decompose the legacy 8 labels.

For every legacy label, ask:

- Is this a claim type?
- Is this an evidence form?
- Is this a source type?
- Is this an inference status?
- Is this a temporal status?
- Is this a communication genre?
- Can it overlap with other labels?

Output an initial collision matrix.

Example question:

> Can a COMMENT contain a FACT, OPINION, ANECDOTE, INFERENCE, or FORECAST?

If yes, those categories cannot all be mutually exclusive on one axis.

Do not resolve the issue by intuition alone; use it to guide research.

## GATE 2 — Framework discovery

Search each research lane for established classification systems and terminology.

For every candidate framework capture:

- domain
- purpose
- classification unit
- categories
- whether categories are mutually exclusive
- whether hierarchy is implied
- what “strength” means
- known limitations
- relevance to Story Engine

Do not yet merge frameworks.

## GATE 3 — Source identity verification

For every source used in a core conclusion verify:

- exact title
- authors / issuing body
- year
- venue / institution
- DOI or stable official URL
- source type
- whether full text or authoritative abstract/summary was inspected

If identity is unresolved:

`UNVERIFIED`

Do not extract numeric claims from an unresolved source.

If title / DOI / author conflict exists:

`BIBLIOGRAPHIC_CONFLICT`

Do not silently repair it.

## GATE 4 — Claim-level extraction

Extract traceable claims, not paper-level vibes.

Each research claim must use the schema in Section 10.

If a source says only that a framework is useful or common, do not rewrite that as proof that the framework is universally valid.

## GATE 5 — Counterevidence search

For every proposed hierarchy or taxonomy, actively search for:

- critiques
- exceptions
- alternative frameworks
- contexts where the hierarchy reverses
- qualitative evidence that does not fit experiment-centered hierarchies
- cases where primary sources are unreliable
- cases where secondary synthesis is stronger than a single primary study
- failures of expert opinion
- sampling / representativeness failures
- domain-specific definitions that conflict

At least one explicit counterevidence search is required for every major synthesis claim.

## GATE 6 — Cross-framework comparison

Build a comparison matrix.

Do not collapse terms merely because labels sound similar.

For each candidate dimension determine:

- equivalent constructs
- near-neighbors
- false friends
- domain-specific meanings
- whether the distinction matters operationally for Story Engine output

## GATE 7 — Candidate taxonomy construction

Only now propose a taxonomy.

Test two architectures:

### Model A — Flat taxonomy

One mutually exclusive Evidence Type label per claim/evidence unit.

### Model B — Multi-axis taxonomy

A claim/evidence unit receives several independent labels.

Claude must compare both and explain which better preserves evidence status with lower classification ambiguity.

A hybrid model is allowed.

## GATE 8 — Stress test against real examples

Stress-test the proposed taxonomy against at least:

- 8 claims sampled from the existing research corpus that exhibit known audit risks, and
- 8 representative nonfiction content claims spanning data, testimony, expert comment, review, social reaction, inference, and forecast.

For existing-corpus samples, prefer examples related to known audit failures such as:

- theory → causal upgrade
- correlation → causation
- qualitative result → injected percentage
- general psychology → platform KPI
- anecdote → population claim
- source metadata conflict

For each example record:

- original claim
- proposed labels
- what the taxonomy prevents
- remaining ambiguity

Do not rewrite original repository files during this step.

## GATE 9 — Engine translation

Convert only supported distinctions into Story Engine fields.

Every proposed field must answer:

- What error does this field prevent?
- Can a researcher reliably assign it?
- Can a writer/engine act on it?
- Is it redundant with another field?

Fields that do not change downstream decisions should be removed or marked optional.

---

# 8. Source Verification Gate

A source may support a core taxonomy decision only if all required identity fields are verified.

## PASS

Required:

- title verified
- author/issuer verified
- year verified
- venue/institution verified
- DOI or stable URL verified
- source type verified
- relevant passage/result traceable

## CONDITIONAL

Allowed only for conceptual context:

- authoritative source with incomplete bibliographic metadata
- source accessible only through an official abstract/summary
- framework documented across multiple authoritative secondary sources but original unavailable

Must be labeled.

## FAIL

Do not use for a core conclusion when:

- title and DOI disagree
- author identity conflicts
- source cannot be located
- only an AI summary exists
- quantitative result cannot be traced
- quoted wording cannot be verified

---

# 9. Evidence relationship labels to test

Do not assume these are final.

Use them as candidate distinctions during research.

## Source relation

- PRIMARY
- SECONDARY
- TERTIARY
- DERIVATIVE / AGGREGATED

## Claim epistemic status

- OBSERVATION
- MEASUREMENT
- DESCRIPTIVE_CLAIM
- ASSOCIATIONAL_CLAIM
- CAUSAL_CLAIM
- INTERPRETATION
- EXPERT_JUDGMENT
- NORMATIVE_JUDGMENT
- INFERENCE
- ESTIMATE
- FORECAST

## Evidence form

- DOCUMENT / RECORD
- DATASET / STATISTIC
- EXPERIMENT
- OBSERVATIONAL_STUDY
- QUALITATIVE_STUDY
- TESTIMONY / INTERVIEW
- CASE / ANECDOTE
- EXPERT_OPINION
- REVIEW / USER_EXPERIENCE
- COMMENT / SOCIAL_REACTION
- SYNTHESIS / REVIEW
- MODEL / SIMULATION

## Directness

- DIRECT
- INDIRECT
- BRIDGE
- APPLICATION_HYPOTHESIS

## Support relation

- SUPPORTS
- PARTIALLY_SUPPORTS
- CONTEXTUALIZES
- CONTRADICTS
- DOES_NOT_TEST
- UNRESOLVED

Claude may add, merge, or reject labels only with reasons.

---

# 10. Claim Extraction Schema

Every important research claim must be represented in a structured block.

```yaml
claim_id:
claim_text:

source:
  title:
  authors_or_issuer:
  year:
  venue_or_institution:
  doi_or_stable_url:
  source_type:
  verification_status: VERIFIED | CONDITIONAL | UNVERIFIED | CONFLICT
  source_location:

classification:
  research_domain:
  claim_epistemic_type:
  evidence_form:
  provenance_level:
  study_or_evidence_design:
  directness:
  causal_status:
  temporal_status:
  population_or_scope:
  representativeness:
  source_independence:

support:
  relationship: SUPPORTS | PARTIALLY_SUPPORTS | CONTEXTUALIZES | CONTRADICTS | DOES_NOT_TEST | UNRESOLVED
  result_or_reasoning:
  quantitative_result:
  uncertainty:
  limitations:
  counterevidence:

story_engine_relevance:
  prevents_error:
  candidate_field:
  candidate_rule:
  should_not_infer:
```

Do not fabricate unavailable fields.

Use `NOT_REPORTED`, `NOT_APPLICABLE`, or `UNRESOLVED` where appropriate.

---

# 11. Required comparison tables

The final report must include all of the following.

## Table A — Legacy label collision matrix

Rows:

- FACT
- SOURCE CLAIM
- OPINION
- REVIEW
- COMMENT
- ANECDOTE
- INFERENCE
- FORECAST

Columns should test whether each is primarily:

- claim type
- evidence form
- source type
- inference status
- temporal status
- communication genre

Multiple assignments are allowed.

## Table B — Framework comparison

Columns:

- framework
- domain
- classification unit
- major categories
- hierarchy?
- purpose
- strength
- limitation
- Story Engine relevance

## Table C — Category boundary table

For every proposed category:

- definition
- inclusion
- exclusion
- nearest confusable category
- example
- failure mode

## Table D — Evidence weight boundary table

Show cases where “stronger evidence” depends on the question.

The purpose is to prevent a universal one-dimensional truth score unless clearly justified.

## Table E — Story Engine field map

Columns:

- engine field
- allowed values
- required/optional
- upstream source
- downstream decision
- error prevented
- confidence in field design

---

# 12. Counterevidence requirements

The final synthesis is incomplete unless it addresses all of these challenges:

1. A primary source can be biased, mistaken, forged, selective, or context-poor.
2. A high-quality secondary synthesis can be stronger than one primary study.
3. An anecdote may be weak for prevalence but strong evidence that an event occurred to one person.
4. Expert opinion may be useful where direct empirical data are sparse, but expertise does not guarantee correctness.
5. User reviews/comments can establish that a reaction exists without establishing how common it is.
6. Qualitative evidence may answer questions that quantitative hierarchies do not address.
7. Correlation can be strong evidence of association without being causal evidence.
8. A forecast is not made factual by coming from an authoritative source.
9. Multiple citations may not be independent if they derive from the same underlying source.
10. Source prestige is not a substitute for claim-level traceability.

---

# 13. Forbidden behaviors

Claude must not:

- validate the legacy 8 categories by assumption
- force mutually overlapping concepts into a single flat taxonomy
- create a universal “truth score” without evidence
- equate PRIMARY with TRUE
- equate SECONDARY with WEAK
- equate EXPERT with CORRECT
- treat comments or reviews as representative population evidence without sampling support
- convert association into causation
- convert theory/review into experiment
- convert qualitative findings into percentages
- infer platform KPIs from general psychology
- use citation count as evidence strength
- use source count without deduplicating shared originals
- invent sample sizes, effect sizes, thresholds, or confidence values
- merge legal, scientific, journalistic, and intelligence standards as if their purposes are identical
- turn an application heuristic into a research finding
- rewrite the old corpus merely because a better taxonomy is proposed

---

# 14. Acceptance criteria

Q1-01 passes only if all criteria are satisfied.

## A. Construct coverage

- Every legacy #60 Theme 1 subtopic is addressed.
- Every legacy 8-type label is mapped, split, retained, or rejected with reasons.
- Missing evidence/claim categories are explicitly identified.

## B. Source integrity

- Core conclusions rely on verified authoritative or peer-reviewed sources.
- Bibliographic conflicts are exposed, not silently repaired.
- Quantitative claims are traceable to original sources.
- Independent source families are distinguished from duplicate citations.

## C. Comparative breadth

At minimum, the report must include credible frameworks from:

- research methodology / evidence synthesis
- journalism / investigative standards
- at least one additional lane among science communication, legal reasoning, forecasting/intelligence

No single domain may define the universal taxonomy by itself.

## D. Counterevidence

- Major proposed distinctions include limitations or boundary conditions.
- Universal evidence hierarchy assumptions are explicitly tested rather than assumed.
- At least one plausible alternative architecture to the final taxonomy is considered.

## E. Product usefulness

The final proposal must let the Story Engine distinguish at minimum:

- what was directly observed/reported
- what is measured/aggregated
- what is interpretation or inference
- what is causal vs correlational
- what is anecdotal vs population-level
- what is expert judgment
- what is public reaction/review
- what is forecast/estimate
- how direct the evidence is
- whether multiple sources are independent

## F. Restraint

A successful result may conclude:

- some labels cannot be cleanly separated,
- some domains use incompatible definitions,
- no universal hierarchy exists,
- some Story Engine fields remain design choices.

`INSUFFICIENT EVIDENCE` is acceptable.

---

# 15. Required output structure

Produce one main report plus structured handoff artifacts.

## File 1 — Main report

Suggested path:

`99_Audit/Precision_Research/Q1-01_EVIDENCE_TAXONOMY_REPORT_v0.md`

Sections:

1. Research Target
2. Legacy Assumptions Under Audit
3. Construct Decomposition
4. Search / Source Method
5. Verified Frameworks by Domain
6. Claim-Level Findings
7. Counterevidence / Boundary Conditions
8. Cross-Framework Comparison
9. Flat vs Multi-Axis Architecture Test
10. Stress Test
11. Candidate Evidence Taxonomy
12. Story Engine Field Map
13. What the Engine Must Not Infer
14. Unresolved Questions
15. Provisional Verdict
16. Sources

## File 2 — Candidate machine-readable schema

Suggested path:

`99_Audit/Precision_Research/Q1-01_EVIDENCE_TAXONOMY_SCHEMA_v0.yaml`

Must contain:

- field names
- allowed values
- definitions
- required/optional status
- conflict rules
- null / unknown handling
- examples
- version

## File 3 — Source verification ledger

Suggested path:

`99_Audit/Precision_Research/Q1-01_SOURCE_LEDGER_v0.yaml`

For every core source:

- identity
- verification status
- domain lane
- evidence type
- exact role in conclusions
- duplicate/source-family relation

## File 4 — Stress-test cases

Suggested path:

`99_Audit/Precision_Research/Q1-01_STRESS_TEST_v0.md`

Keep this separate so the taxonomy can be revised without rewriting the literature report.

---

# 16. Provisional verdict schema

The report must end with this block.

```yaml
research_id: Q1-01
construct: Evidence Taxonomy

bibliographic_status:
  verified_sources: []
  corrected_sources: []
  unresolved_sources: []
  rejected_sources: []

architecture_test:
  flat_taxonomy:
    status:
    strengths: []
    failures: []
  multi_axis_taxonomy:
    status:
    strengths: []
    failures: []
  recommended_architecture:
  rationale:

evidence_summary:
  strong_distinctions: []
  conditional_distinctions: []
  domain_specific_distinctions: []
  rejected_distinctions: []
  missing_from_legacy: []

confidence:
  source_integrity:
  taxonomy_support:
  cross_domain_transfer:
  operational_utility:
  quantitative_support:

story_engine:
  required_fields: []
  optional_fields: []
  conflict_rules: []
  forbidden_upgrades: []
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

Do not mark all fields High by default.

---

# 17. Next-stage handoff fields

Q1-01 must explicitly hand off unresolved issues to later research.

## To Q1-02 — Confidence / uncertainty language

Pass:

- evidence-status fields that require language calibration
- distinctions between unknown / inferred / disputed / forecast
- cases where confidence cannot be inferred from source type alone

## To Q1-04 — Counterevidence / alternatives

Pass:

- claims needing competing explanations
- evidence asymmetry cases
- source diversity / independence issues

## To Q1-05 — Source monitoring / correction

Pass:

- provenance fields
- primary/secondary source confusion
- visual/document source attribution issues

## To Track K — Empirical Story Engine Validation

Pass:

- fields that need inter-rater reliability testing
- ambiguous categories
- labels likely to create annotation disagreement
- proposed conflict rules

---

# 18. Definition of success

The best result is **not** a prettier version of the original eight labels.

The best result is a taxonomy that prevents the kinds of failures already found in the corpus.

A successful Q1-01 should make transformations like these mechanically visible:

```text
one person's review
≠ population preference

correlation
≠ causal effect

theoretical mechanism
≠ experimentally demonstrated effect

expert interpretation
≠ observed fact

official forecast
≠ known future outcome

three citations to one original study
≠ three independent evidence families

general psychology finding
≠ YouTube retention percentage
```

The Story Engine should preserve useful evidence while making unsupported upgrades difficult.

That is the purpose of Q1-01.
