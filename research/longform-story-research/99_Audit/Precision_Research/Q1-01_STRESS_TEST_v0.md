# Q1-01 EVIDENCE TAXONOMY — Stress Test v0

> Purpose: test whether the provisional multi-axis Evidence Object catches known corpus failure modes and representative nonfiction claim types.

---

# 1. Existing Corpus Audit Cases

## Case A1 — Emotional theory → invented retention KPI

### Original corpus pattern
A theoretical emotion source was transformed into claims such as:
- mid-video dropout reduced by 72%
- completion increased 3.1x

### Proposed labels
- claim_type: CAUSAL_CLAIM
- evidence_form: THEORY_CONCEPTUAL
- provenance_role: PRIMARY_RESEARCH or SECONDARY_SYNTHESIS depending the cited item
- directness: DOES_NOT_TEST
- support_relation: DOES_NOT_TEST
- causal_status: CAUSAL_HYPOTHESIS at most
- quantitative: UNRESOLVED / NOT_REPORTED

### What the taxonomy prevents
A theoretical mechanism cannot directly support platform retention percentages.

### Remaining ambiguity
A later direct platform study could independently support the KPI, but that would require a separate evidence object.

---

## Case A2 — QUEST bibliographic conflation → causal percentages

### Original corpus pattern
One source record combined title/DOI/venue elements from different QUEST publications and attached precise model-fit/causal numbers.

### Proposed labels
- source_verification: BIBLIOGRAPHIC_CONFLICT
- evidence_form: UNKNOWN until reconstructed
- support_relation: UNRESOLVED
- quantitative: blocked

### What the taxonomy prevents
A bibliographically unresolved source cannot carry precise numerical claims into synthesis.

### Remaining ambiguity
The QUEST research family itself remains valuable after publication-level reconstruction.

---

## Case A3 — Event-Indexing mechanism → invented threshold / video law

### Original corpus pattern
Zwaan, Langston & Graesser (1995) supports event-index dimensions, but the repository added:
- unverified sample metadata
- “2+ dimensions unclear → situation model collapse”
- direct application to visual montage/video

### Proposed labels
For the verified research finding:
- claim_type: DESCRIPTIVE_CLAIM / ASSOCIATIONAL_CLAIM
- evidence_form: EXPERIMENT or empirical narrative-comprehension study
- directness: DIRECT for narrative comprehension
- support_relation: SUPPORTS for event-index representation

For the production rule:
- directness: APPLICATION_HYPOTHESIS
- support_relation: DOES_NOT_TEST for exact threshold/video rule

### What the taxonomy prevents
A valid mechanism survives while unsupported threshold/application is isolated.

---

## Case A4 — Animal habituation → longform emotional pacing law

### Original corpus pattern
Groves & Thompson habituation/sensitization work was transferred into:
- suspense sensitization
- emotional reset
- resensitization
- longform wave timing rules

### Proposed labels
- evidence_form: THEORY_CONCEPTUAL / behavioral experimental research
- evidence_scope: animal/reflex-learning paradigms
- target_scope: adult longform narrative viewing
- directness: BRIDGE
- support_relation: CONTEXTUALIZES
- engine rule: APPLICATION_HYPOTHESIS

### What the taxonomy prevents
The general mechanism can remain a bridge without becoming direct media evidence.

---

## Case A5 — Narrative mnemonic prediction error → dopamine pleasure

### Original corpus pattern
Sinclair et al. (2021) directly studied familiar narrative video prediction error and memory updating, but downstream interpretation turned it into a dopaminergic/reward/twist-pleasure mechanism.

### Proposed labels
For memory-updating claim:
- evidence_form: EXPERIMENT
- evidence_scope: human fMRI / familiar narrative videos
- directness: DIRECT
- support_relation: SUPPORTS

For dopamine pleasure claim:
- directness: DOES_NOT_TEST
- support_relation: DOES_NOT_TEST
- causal_status: UNKNOWN

### What the taxonomy prevents
One paper can strongly support one mechanism while explicitly not supporting a neighboring mechanism.

---

## Case A6 — Wrong Annie Lang DOI → exact cut-frequency rule

### Original corpus pattern
A repository record attached an Annie Lang-style title to a DOI belonging to another television paper, then used it to support exact editing-frequency rules.

### Proposed labels
- source_verification: BIBLIOGRAPHIC_CONFLICT
- quantitative: blocked
- support_relation: UNRESOLVED until source reconstruction

### What the taxonomy prevents
Relevant research-program familiarity cannot substitute for publication identity.

---

## Case A7 — Infant complexity preference → adult narrative uncertainty optimum

### Original corpus pattern
Kidd et al. infant visual-attention work was used to justify an adult longform “optimal prediction error/uncertainty” range.

### Proposed labels
- evidence_form: EXPERIMENT
- evidence_scope: infants / visual sequence attention
- target_scope: adult longform audience
- directness: BRIDGE
- support_relation: CONTEXTUALIZES
- quantitative transfer: FORBIDDEN

### What the taxonomy prevents
A numeric optimum cannot cross population/domain boundaries without direct validation.

---

## Case A8 — Damasio hypothesis → exact learning/retention effects

### Original corpus pattern
A theoretical/hypothesis source on reasoning and decision making was combined with other theories and transformed into:
- +42%
- +35%
- 3.8x retention
- -38%
- +52%
- 3x memory

### Proposed labels
- evidence_form: THEORY_CONCEPTUAL
- directness: BRIDGE or DOES_NOT_TEST
- quantitative fields: NOT_REPORTED
- support_relation: CONTEXTUALIZES at most

### What the taxonomy prevents
Theory can seed a mechanism hypothesis without manufacturing an effect size.

---

# 2. Representative Nonfiction Claims

These cases are synthetic test cases. They are not claims about real products or events.

## Case B1 — Official record

### Claim
“Agency X recorded the filing date as March 3.”

### Evidence
Original official record.

### Labels
- claim_type: OBSERVATION / DESCRIPTIVE_CLAIM
- evidence_form: DOCUMENT_RECORD
- provenance_role: ORIGINAL_RECORD
- directness: DIRECT
- support_relation: SUPPORTS
- target_scope: specific filing
- evidence_scope: specific filing

### Allowed script
“Agency X’s record lists March 3 as the filing date.”

### Forbidden upgrade
“The event definitely occurred exactly as described elsewhere in the record.”

Reason:
The record directly supports what the record says; separate claims inside the document may need independent verification.

---

## Case B2 — One user review

### Claim
“My battery died after three hours.”

### Evidence
Verified buyer review.

### Labels
- claim_type: OBSERVATION as reported by user
- evidence_form: USER_REVIEW
- provenance_role: FIRSTHAND_SOURCE
- evidence_scope: INDIVIDUAL
- target_scope: INDIVIDUAL
- representativeness: SELF_SELECTED

### Allowed script
“One verified buyer reported about three hours of battery life.”

### Forbidden upgrade
“This model only lasts three hours.”

---

## Case B3 — Review average

### Claim
“The product has a 4.2/5 average across 2,000 posted reviews.”

### Evidence
Platform review dataset.

### Labels
- claim_type: MEASUREMENT / DESCRIPTIVE_CLAIM
- evidence_form: DATASET_STATISTIC
- evidence_scope: POSTED_REVIEWERS
- target_scope: POSTED_REVIEWERS
- representativeness: SELF_SELECTED unless stronger sampling evidence exists

### Allowed script
“Among 2,000 posted reviews, the displayed average is 4.2.”

### Forbidden upgrade
“Customers overall rate it 4.2” unless reviewer population is justified as representative.

---

## Case B4 — Expert engineering judgment

### Claim
“An engineer says the thermal design is likely to cause early throttling.”

### Evidence
Expert interview based on schematic inspection.

### Labels
- claim_type: EXPERT_JUDGMENT / INFERENCE
- evidence_form: EXPERT_OPINION
- provenance_role: FIRSTHAND_SOURCE
- directness: INDIRECT
- causal_status: CAUSAL_HYPOTHESIS
- target_scope: product design
- evidence_scope: schematic/expert interpretation

### Allowed script
“An engineer who reviewed the design thinks the thermal layout could cause early throttling.”

### Forbidden upgrade
“The design causes early throttling.”

---

## Case B5 — Representative survey

### Claim
“60% of the target population prefers option A.”

### Evidence
Probability-based survey with documented sampling and uncertainty.

### Labels
- claim_type: MEASUREMENT / DESCRIPTIVE_CLAIM
- evidence_form: OBSERVATIONAL_STUDY
- evidence_scope: SAMPLE
- target_scope: POPULATION
- representativeness: REPRESENTATIVE_BY_DESIGN
- quantitative module: required

### Allowed script
“In the survey, 60% chose A; the estimate is intended to represent the target population within the survey’s sampling uncertainty.”

### Forbidden upgrade
“60% definitely prefer A” without uncertainty/context.

---

## Case B6 — Observational association

### Claim
“People who used feature X had higher retention.”

### Evidence
Observational platform data.

### Labels
- claim_type: ASSOCIATIONAL_CLAIM
- evidence_form: OBSERVATIONAL_STUDY / DATASET_STATISTIC
- causal_status: ASSOCIATION_ONLY
- directness: DIRECT if same platform/content context

### Allowed script
“Use of X was associated with higher retention in this dataset.”

### Forbidden upgrade
“X increased retention.”

---

## Case B7 — Randomized experiment

### Claim
“Changing X increased outcome Y in the experiment.”

### Evidence
Random assignment to X vs control.

### Labels
- claim_type: CAUSAL_CLAIM
- evidence_form: EXPERIMENT
- causal_status: CAUSAL_IDENTIFICATION_SUPPORTED
- evidence_scope: STUDIED_SAMPLE
- target_scope: studied population/context unless external validity is separately established

### Allowed script
“In this experiment, changing X increased Y.”

### Forbidden upgrade
“X always increases Y for all audiences.”

---

## Case B8 — Social comments

### Claim
“Viewers hated the ending.”

### Evidence
50 negative comments manually collected under one video.

### Labels
- claim_type: DESCRIPTIVE_CLAIM if rewritten to collected comments
- evidence_form: COMMENT_SOCIAL_REACTION
- evidence_scope: COLLECTED_COMMENTERS
- representativeness: SELF_SELECTED
- platform_reaction collection method: required

### Allowed script
“Among the comments we reviewed, many criticized the ending.”

### Forbidden upgrade
“Viewers overall hated the ending.”

---

## Case B9 — Official forecast

### Claim
“Agency X expects demand to fall 10% next year.”

### Evidence
Official model-based forecast.

### Labels
- claim_type: FORECAST
- evidence_form: MODEL_SIMULATION / OFFICIAL_STATEMENT
- temporal_status: FUTURE_FORECAST
- provenance_role: ORIGINAL_RECORD
- forecast_module: required

### Allowed script
“Agency X forecasts a 10% decline next year under its stated assumptions.”

### Forbidden upgrade
“Demand will fall 10% next year.”

---

# 3. Collision Test

## Flat taxonomy failure example

Input:

> “A verified buyer said the laptop shut down twice, thinks overheating caused it, and predicts the motherboard will fail within a year.”

Flat label options:
- REVIEW?
- ANECDOTE?
- INFERENCE?
- FORECAST?

All are simultaneously true.

## Multi-axis representation

```yaml
source_form: USER_REVIEW
reported_event:
  claim_type: OBSERVATION
  evidence_scope: INDIVIDUAL
causal_statement:
  claim_type: INFERENCE
  causal_status: CAUSAL_HYPOTHESIS
future_statement:
  claim_type: FORECAST
representativeness: SELF_SELECTED
```

Result:
No information is destroyed by choosing one label.

---

# 4. Forbidden Upgrade Test

| Upgrade | Detected? | Blocking field |
|---|---:|---|
| theory → measured effect | yes | evidence_form + quantitative traceability |
| comment → public opinion | yes | evidence_scope + representativeness |
| review → typical experience | yes | evidence_scope + representativeness |
| association → cause | yes | claim_type + causal_status |
| bridge → direct story law | yes | directness |
| forecast → fact | yes | claim_type + temporal_status |
| duplicate citations → replications | yes | source_family + independence |
| expert → fact | yes | claim_type + evidence_form |
| primary → true | yes | provenance_role separated from verification |
| qualitative → invented % | yes | evidence_form + quantitative traceability |
| source conflict → precise number | yes | source_verification |
| general psychology → YouTube KPI | yes | directness + evidence_scope + support_relation |

---

# 5. Ambiguities Found

The proposed schema still has unresolved annotation problems.

## Ambiguity 1 — Observation vs descriptive claim

A sentence can describe a directly observed record and therefore be both.

Possible solution:
- claim_type may need primary type + secondary modifiers, or
- OBSERVATION may move from claim_type to evidence relation.

Track K should test annotator agreement before freezing this distinction.

## Ambiguity 2 — Expert judgment vs inference

Expert judgment frequently contains inference.

Possible solution:
- EXPERT_JUDGMENT belongs primarily to evidence/source role
- INFERENCE remains claim epistemic status

This is a likely schema revision candidate.

## Ambiguity 3 — Primary source terminology

“Primary” changes meaning by domain.

Possible solution:
Use more concrete values:
- ORIGINAL_RECORD
- FIRSTHAND_SOURCE
- PRIMARY_RESEARCH

instead of a single PRIMARY label.

## Ambiguity 4 — Direct vs indirect

Directness is claim-relative.

The same source may be DIRECT for one claim and BRIDGE/DOES_NOT_TEST for another.

Therefore directness belongs to the **claim-evidence link**, not the source record alone.

---

# 6. Stress-Test Verdict

```yaml
stress_test_version: "0.1"

existing_corpus_cases: 8
synthetic_nonfiction_cases: 9

flat_taxonomy:
  result: FAIL
  reason:
    - overlapping labels
    - loses causal status
    - loses scope
    - loses domain-transfer distance
    - loses source independence

multi_axis_taxonomy:
  result: PASS_PROVISIONAL
  catches_known_audit_failures: true
  unresolved:
    - observation_vs_descriptive_claim
    - expert_judgment_axis_location
    - annotation burden
    - inter_rater_reliability

recommended_next_action:
  - "Keep multi-axis architecture."
  - "Do not freeze every enum yet."
  - "Move confidence-language calibration to Q1-02."
  - "Use Track K to test annotation reliability before production hard-coding."
```
