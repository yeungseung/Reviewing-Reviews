# LONGFORM STORY RESEARCH — Audit Log

## Audit purpose

This audit treats the existing research corpus as exploratory evidence for building a practical Story Engine, not as a final academic knowledge base.

Primary goals:
- verify structural integrity and evidence traceability
- estimate source/research reliability without discarding useful exploratory signals
- identify repeated cross-theme mechanisms
- distinguish independent evidence from repeated reuse of the same source
- detect meaning inflation across Source → Report → Evidence Card → Synthesis
- redesign the remaining research map when current findings justify it
- translate sufficiently supported patterns into Story Engine principles

## Mutation policy

- Original research files remain unchanged unless an issue is mechanically certain or externally verified.
- Audit findings are recorded here first.
- Quantitative claims, quotations, DOI metadata, causal claims, and Tier changes require verification before correction.
- Practical Story Engine interpretations are kept separate from claims made directly by the cited research.

## Corpus baseline

Branch: `research/longform-story-audit`

- Planned top-level research items: 86
- Planned Research Themes: 257
- Completed reports: 165
- Fully completed top-level items: 57
- Partially completed items: #12 and #59
- Untouched top-level items: #60–#86 (27 items)
- Remaining Themes: 92
- Sources DB files: 589
- Evidence Cards: 317 (NAR 159 / PSY 155 / EMO 3)
- Factcheck Checklist: 1
- Synthesis Registry: 1
- Implemented Story Structure files: 0

## Confirmed structural findings

### A-001 — Source schema drift
Status: CONFIRMED
Severity: MEDIUM

The Source DB contains at least three schemas:
1. rich nested/index-linked schema through Source index entry 289
2. flat schema from entry 290
3. reduced/minimal flat schema for entries 558–589

The last 32 sources map exactly to #57 T1–T3, #58 T1–T3, and #59 T1–T2 and lack much of the metadata used in the previous flat schema.

### A-002 — Source duplication across Themes
Status: CONFIRMED
Severity: HIGH for evidence counting, LOW/MEDIUM for storage

Title-normalized index analysis found 77 duplicate-title candidate groups and at least 113 registrations beyond the first copy.
At least 20 duplicate URL/DOI groups are present in the URL-bearing section.

Interpretation:
Repeated rediscovery of the same source across independently researched Themes can be a useful pattern signal, but it must not be counted as independent evidence.

Required distinction for Pattern Mining:
- number of Themes repeating a claim
- number of Source DB records
- number of independent original sources

### A-003 — Report schema drift
Status: CONFIRMED
Severity: MEDIUM

At least three Report schemas exist:
- Schema A: original template format
- Schema B: transition format around #29–#31
- Schema C: current format beginning at #31 T3

The current `template_research_report.md` and `init_theme_report.py` still generate Schema A.

### A-004 — Evidence Card verifier coverage gap
Status: CONFIRMED
Severity: MEDIUM

Actual cards:
- NAR: 159
- PSY: 155
- EMO: 3
- Total: 317

`verify_integrity.py` checks only CARD-NAR-* and CARD-PSY-* and reports 314 cards.
CARD-EMO-001 through CARD-EMO-003 are excluded from the integrity count.

### A-005 — Story Structure layer not implemented
Status: CONFIRMED
Severity: DESIGN QUESTION

README and template files describe a `30_Story_Structures/` layer, but the repository contains no implemented Story Structure files.

This should be revisited during Research Map / Story Engine redesign rather than treated automatically as an error.

### A-006 — Early Report → Source lineage is indirect
Status: CONFIRMED
Severity: HIGH for audit traceability

Many early Reports contain bibliographic references but not explicit `SRC-*` identifiers.
Their Source linkage must be reconstructed through Theme tags in `10_Sources_DB/index.yaml`.

Later Reports use explicit Source IDs.

Audit lineage classes:
- DIRECT: Report explicitly contains Source ID
- RECONSTRUCTED: Source is inferred through matching Theme/index metadata

### A-007 — Synthesis calibration anomaly
Status: CONFIRMED AS SIGNAL, NOT YET AS BIAS
Severity: HIGH for later synthesis audit

Actual registry distribution:
- Strong Support: 163/165
- Conditional Support: 2/165
- Mixed / Weak / Contradicted / Insufficient: 0
- Confidence: High for 165/165
- EXPAND signal: 165/165

These counts are internally consistent with the registry.
Whether this reflects confirmation bias, verdict inflation, or genuinely strong evidence remains to be audited.

## Phase 2 evidence-audit examples

### E-001 — CARD-NAR-100
Status: HIGH-RISK UNSUPPORTED QUANTIFICATION

Card claim:
- emotional-state transition in longform reduces mid-video dropout by 72%
- completion rate increases 3.1x

Cited sources:
- Oatley & Johnson-Laird (1987)
- Russell (1980)

The cited Oatley & Johnson-Laird paper is a theoretical cognitive-emotion paper about transitions between plans/goals, not a longform-video retention experiment.
The corresponding #37 T1 Report does not contain the 72% / 3.1x figures.
This suggests the quantitative effect was introduced at the Evidence Card transformation stage.

### E-002 — #21 T2 / CARD-PSY-050
Status: HIGH-RISK UNSUPPORTED QUANTIFICATION

Claim:
- causal coherence +73%
- memory retention 2.1x
- p < .001

The Report contains these values and attributes them to Graesser et al. / QUEST.
The Source DB itself contains highly specific model-fit and causal language that requires original-source verification.
Public bibliographic/abstract evidence for QUEST describes a question-answering/convergence model and does not establish the claimed +73% / 2.1x result.

### E-003 — CARD-PSY-100
Status: HIGH-RISK UNSUPPORTED QUANTIFICATION

Claim:
- Roseman (1991) changed anger into sadness/pity with 87%+ accuracy

The actual Roseman study experimentally manipulated five appraisal dimensions in 120 college students and found predicted appraisal effects on emotion intensities.
The 87% transformation figure is not supported by the available bibliographic/abstract record and is absent from the Source DB entry.

### E-004 — #59 T2 / CARD-PSY-166
Status: MIXED — ONE REAL NUMBER + MULTIPLE UNSUPPORTED NUMBERS

Wade et al. (2002):
- 20 participants
- 50% developed complete or partial false memories after repeated fake-photo + guided-imagery exposure
This 50% figure is supported.

Vaccari & Chadwick (2020):
- deceptive deepfakes increased uncertainty
- reported uncertainty levels were roughly 35.1% / 36.9% vs 27.5% in the educational-reveal condition
- uncertainty mediated lower trust in news on social media

The Report/Card numbers such as 74% betrayal/displeasure and -58% or +46% trust shifts are not supported by the published results inspected so far.

This example confirms that valid findings and invented/overstated quantitative claims can coexist within the same Card.

## Working rule

Never collapse a Theme or mechanism merely because one quantitative detail is wrong.

For every issue classify separately:
1. source existence
2. bibliographic correctness
3. methodology / Tier
4. qualitative mechanism
5. quantitative effect
6. generalization
7. Story Engine application leap
8. downstream Synthesis effect


## Phase 2 additional verified findings

### E-005 — SRC-2009-419 bibliographic conflation
Status: CONFIRMED ERROR
Severity: CRITICAL for source traceability

Repository entry:
- ID: `SRC-2009-419`
- claimed title: "Changes in events alter how people remember them"
- claimed authors: Kael W. Swallow, Jeffrey M. Zacks, Nicole K. Speer
- claimed DOI: `10.1111/j.1467-8721.2009.01642.x`

External verification:
- DOI `10.1111/j.1467-8721.2009.01642.x` belongs to Anuj K. Shah & Daniel M. Oppenheimer, "The Path of Least Resistance: Using Easy-to-Access Information."
- A real 2009 event-memory paper is Swallow, Zacks & Abrams, "Event Boundaries in Perception Affect Memory Encoding and Updating," DOI `10.1037/a0015631`.
- A later related paper is Swallow et al., "Changes in Events Alter How People Remember Recent Information," DOI `10.1162/jocn.2010.21524`.

Interpretation:
The DB entry appears to conflate multiple real event-segmentation papers while attaching an unrelated DOI. It should not be silently corrected until the intended source lineage is resolved.

Downstream impact:
#45 T2 uses this entry to support 2.4x recall and 79% next-chapter/next-episode continuation metrics. Those values are not supported by the actual event-segmentation papers inspected.

### E-006 — SRC-1978-238 Generation Effect metadata inflation
Status: PARTIALLY CONFIRMED + OVERCLAIM
Severity: HIGH

Real paper:
Slamecka & Graf (1978), "The Generation Effect: Delineation of a Phenomenon," DOI `10.1037/0278-7393.4.6.592`.

Verified:
- five experiments
- 96 undergraduates total
- generated words were remembered better than read words across several tests

Repository metadata incorrectly states:
- "총 200여 명 학부생"
- "Self-Generation Directly Doubles Long-Term Retention"
- universal direct extension to narrative inference/storytelling

The original article establishes a real generation advantage, but does not state a general 2x law for long-term retention or direct applicability to narrative revelation.

Story Engine implication:
KEEP the qualitative mechanism as a research lead.
DROP/REVERIFY the 2x magnitude and the universal narrative generalization.

### E-007 — SRC-2011-241 Bonawitz pedagogy effect inflation
Status: QUALITATIVE SUPPORT / QUANTITATIVE OVERCLAIM
Severity: HIGH

Real paper:
Bonawitz et al. (2011), "The double-edged sword of pedagogy: Instruction limits spontaneous exploration and discovery."

Verified Experiment 1:
- N=85 preschoolers
- pedagogical condition explored for less time
- fewer unique actions
- fewer non-demonstrated functions discovered
- non-demonstrated functions discovered: Pedagogical M=.72; Interrupted M=1.3; Naive M=1.2; Baseline M=1.15

Verified Experiment 2:
- N=64
- Direct/Indirect Child conditions showed more constrained exploration than comparison conditions

Repository claims:
- exploration/discovery "60% 급감"
- incomplete demonstration produces "3배 이상 폭증"
- p<.001 generalized to the discovery effect

These are not faithful summaries of the reported outcome statistics. The paper supports the direction of the mechanism, not the repository's generalized 3x narrative rule.

Domain caution:
This is a preschool toy-exploration paradigm. Extension to adult longform-story curiosity is a Story Engine hypothesis, not a directly tested result.

### E-008 — #45 T2 platform-metric injection
Status: CONFIRMED TRANSFORMATION ERROR
Severity: CRITICAL

Report claims include:
- state-change chapter recall 2.4x higher
- next-chapter/episode playback rate 79% vs 32%
- dropout +64% when State Change = 0
- risk escalation lowers mid-series dropout by 64%

The cited event-segmentation literature concerns perception, event boundaries, working/episodic memory, and recognition tasks.
It does not measure streaming continuation, episode playback, or platform dropout.

This is a clear example of:
real cognitive mechanism
→ unsupported effect magnitude
→ invented platform KPI
→ Engine Rule

### E-009 — #45 T3 review/theory converted into numerical engineering rule
Status: HIGH-RISK OVERCLAIM
Severity: HIGH

`SRC-2008-423` is Kurby & Zacks (2008), "Segmentation in the perception and memory of events," a Trends in Cognitive Sciences review.
Its abstract supports:
- event segmentation at multiple timescales
- hierarchical grouping
- links to working-memory updating and long-term memory

The #45 T3 Report converts this into:
- 2.3x recall improvement
- an optimal hierarchy where 3–4 micro boundaries converge into one macro boundary

The same Report converts Schank & Abelson's script theory into a 70% routine / 30% breach production formula.

Treat these ratios as proposed Engine heuristics unless independently validated; do not store them as direct research findings.

### E-010 — #53 T3 YouTube/platform KPI fabrication pattern
Status: CONFIRMED TRANSFORMATION ERROR
Severity: CRITICAL

Report claims:
- negative emotional brand association → sponsorship CTR -43%
- paid membership conversion -65%
- positive ending → subscription conversion +28%
- negative ending → unsubscribe rate 3.4x
- stressed viewers choose uplifting endings 3.2x more often

The cited source set consists primarily of general evaluative conditioning, mood management, brand equity, habit, news avoidance, and emotion research.
Several key cited works predate YouTube and modern creator subscription/membership metrics.

Their Source DB entries contain no such CTR, membership, subscription, or unsubscribe figures.

Interpretation:
Generic psychological/branding mechanisms were transformed into fabricated creator-platform KPIs.

Story Engine implication:
The qualitative concern about cumulative emotional brand association may remain useful.
All platform percentages and multipliers must be removed or independently re-researched.

### E-011 — #54 T1 theory-to-effect-size injection
Status: CONFIRMED TRACEABILITY FAILURE / HIGH-RISK QUANTIFICATION
Severity: HIGH

Report claims:
- emotional hook before knowledge content → elaboration +42%
- concept comprehension +35%
- emotional narrative → 30-day retention 3.8x
- causal explanation after tragedy → amygdala -38%
- perceived control +52%
- emotionally tagged data → memory up to 3x

Cited sources include:
- Damasio (1996) somatic marker hypothesis
- Scherer et al. (2001) appraisal-process framework/book
- Forgas (1995) Affect Infusion Model
- Kunda (1990) motivated reasoning review
- Lieberman et al. (2007) affect-labeling fMRI experiment

The Source DB entries do not contain the Report's +42%, +35%, 3.8x, -38%, +52%, or 3x values.

External verification confirms Damasio (1996) is explicitly a hypothesis paper on reasoning/decision making rather than a knowledge-content retention experiment.

Interpretation:
The Report combines legitimate theoretical mechanisms into a synthetic production claim and then adds precise effect sizes without traceable provenance.

## Emerging error taxonomy

The following repeated failure modes are now stable enough to use as audit labels:

1. BIBLIOGRAPHIC_CONFLATION
   - real papers/authors/topics combined with the wrong DOI/title/year

2. METADATA_INFLATION
   - wrong sample size, citation count, replication status, study type, or "causal law" label

3. QUANTIFICATION_INJECTION
   - qualitative result converted into an unsupported percentage, multiplier, p-value, or threshold

4. PLATFORM_KPI_INJECTION
   - generic psychology/media research converted into YouTube/OTT CTR, retention, subscription, continuation, or churn metrics not measured by the cited work

5. DOMAIN_TRANSFER_LEAP
   - child learning, word memory, lab perception, etc. treated as direct proof of adult longform storytelling effects

6. THEORY_TO_CAUSAL_UPGRADE
   - theoretical/review paper relabeled as experimental causal evidence

7. ENGINE_HEURISTIC_AS_EMPIRICAL_FACT
   - useful production heuristic (80/20, 70/30, exact timing, exact layer counts) presented as if directly derived from research

8. LINEAGE_BREAK
   - Source → Report → Card transformation cannot identify where a number or rule entered the chain

## Current audit interpretation

A consistent pattern is emerging:

- qualitative mechanisms are often more trustworthy than the precise numbers attached to them
- source existence is frequently real even when metadata or effect sizes are wrong
- the most severe distortion often happens when a research mechanism is translated into a Story Engine rule
- therefore the corpus remains valuable for mechanism discovery and cross-theme pattern mining, but quantitative claims and exact production formulas require a separate verification layer


### E-012 — Synthesis confidence inflation after upstream distortion
Status: CONFIRMED LINEAGE PROBLEM
Severity: CRITICAL

Representative Themes with verified or high-risk upstream issues still arrive in the Synthesis registry as:
- Strong Support
- High confidence
- KEEP
- EXPAND

Checked examples include:
- #21 T2
- #30 T1
- #37 T1
- #37 T2
- #45 T2
- #45 T3
- #53 T3
- #54 T1
- #59 T2

This shows that the Synthesis layer currently does not encode uncertainty introduced by:
- unsupported quantitative claims
- source metadata inflation
- domain-transfer leaps
- bibliographic conflation

Most importantly, #59 T2's registry summary explicitly preserves some unsupported numeric claims as part of the justification chain.

Interpretation:
The current registry is useful as a map of Gemini's preferred conclusions, but it is not yet a calibrated evidence-confidence layer.

Required redesign later:
Synthesis confidence must be derived from separate fields for:
- source existence/bibliographic confidence
- mechanism support
- quantitative support
- domain transfer confidence
- independent source-family count
- counterevidence status
- application/engine-rule confidence

A Theme should be allowed to remain useful even when its exact numbers fail, but the registry must be able to represent that distinction.


### E-013 — SRC-1992-155 QUEST bibliographic conflation
Status: CONFIRMED ERROR
Severity: CRITICAL for source identity

Repository entry combines:
- title fragments: "Mechanisms that generate questions / QUEST: A model of question answering"
- authors: Graesser, Person, Huber
- year: 1992
- DOI: `10.1016/0010-0285(92)90003-V`
- venue: Cognitive Psychology

External verification found:
- "QUEST: A model of question answering" is a real 1992 article in *Computers & Mathematics with Applications*, DOI `10.1016/0898-1221(92)90132-2`
- a related empirical QUEST study, "Question answering in the context of scientific mechanisms," is a 1991 *Journal of Memory and Language* article, DOI `10.1016/0749-596X(91)90003-3`

The repository's title/DOI/venue combination does not correspond to one verified publication.

The record also contains unsupported:
- "hundreds" sample description
- r=.75–.85 model-human agreement
- quoted wording not verified in the located abstracts

Interpretation:
Remove this record from independent-evidence counting until reconstructed from a specific original publication.

### E-014 — SRC-1995-015 Event-Indexing model: mechanism valid, metadata/application inflated
Status: MIXED
Severity: MEDIUM/HIGH

Verified original:
Zwaan, Langston & Graesser (1995), "The Construction of Situation Models in Narrative Comprehension: An Event-Indexing Model," DOI `10.1111/j.1467-9280.1995.tb00513.x`.

Verified core:
- events are focal points in narrative situation models
- events are connected along time, space, protagonist, causality, intentionality
- a verb-clustering task supported the model

Repository inflation:
- sample_size = 120 is not established by the verified abstract
- relationship_type = "Causal Mental Representation" overstates the evidence type
- "2 or more dimensions unclear → situation model collapse" is a Story Engine extrapolation, not the paper's demonstrated rule
- direct extension to visual montage/video is explicitly beyond the paper's tested task

Interpretation:
KEEP the five-dimension situation-model mechanism.
REVERIFY sample/method metadata.
MOVE visual/video thresholds into application hypotheses.

### E-015 — SRC-1985-022 Trabasso/van den Broek: causal-network finding valid, experimental metadata inflated
Status: MIXED
Severity: MEDIUM/HIGH

Verified original:
Trabasso & van den Broek (1985), "Causal thinking and the representation of narrative events," DOI `10.1016/0749-596X(85)90049-X`.

Verified abstract:
- causal network representations predicted immediate/delayed recall, summarization, and judged importance
- causal-chain membership and number of causal connections explained substantial variance
- the study reanalyzed existing stories/data

Repository inflation:
- study labeled "Experimental / Cognitive Modeling"
- sample_size = 128 and target "adult and child readers" require source-level verification
- relationship_type = "Causal" risks confusing causal-network structure with experimental causal identification
- direct rule that every important event should be a necessary causal node is a craft extrapolation

Interpretation:
KEEP causal-network centrality as a strong narrative-comprehension lead.
Do not treat the paper as proof of a universal "every important scene must be causally necessary" engine law.


### E-016 — Appraisal/Emotion family: mechanism convergence stronger than application claims
Status: MECHANISM SUPPORTED / APPLICATION OVEREXTENDED
Severity: MEDIUM for mechanism, HIGH for engine-rule lineage

Externally verified lines include:
- Oatley & Johnson-Laird (1987): theoretical model of emotions coordinating transitions between plans/goals
- Roseman (1991): experimental test with 120 college students; manipulated appraisal dimensions affected emotional intensities
- Scherer (2001): sequential appraisal checking as part of a dynamic component-process model
- Forgas (1995): review/integrative Affect Infusion Model for mood effects on judgment

Corpus implication:
The broad proposition "changes in appraisal/goal evaluation can change emotion/judgment" has multiple independent research lines.

Repository overextensions include:
- converting plan-transition theory into direct "attention reset" / longform retention mechanisms
- treating appraisal models as exact emotion-conversion formulas
- using AIM to claim emotional arousal directly improves complex narrative information processing
- attaching exact percentages (e.g. 87%) not present in the verified records

Audit disposition:
KEEP M3 Appraisal→Emotion as an A-priority mechanism.
Separate:
1. appraisal structure
2. emotion/judgment consequence
3. attention consequence
4. Story Engine manipulation
5. exact effect magnitude

### E-017 — Capacity/Multimedia family: strong mechanism, unsupported timing formula
Status: MECHANISM SUPPORTED / ENGINE HEURISTIC INFLATION
Severity: HIGH for timing rules

Externally verified lines include:
- Sweller (1988): means-ends problem solving can consume cognitive processing capacity needed for schema acquisition
- Lang (2000): mediated-message processing is capacity limited and can be modeled through allocation to encoding/storage/retrieval
- later LC4MP meta-analysis: 142 articles / 683 effects, pooled effects across cognitive-load, motivation, and memory domains roughly r=.314–.398
- Mayer multimedia-learning work: dual channels, limited capacity, active processing
- segmenting principle: learner-paced segmentation outperforms continuous presentation under relevant conditions

Repository overextensions include:
- "information ↔ emotion periodic alternation" as if directly established by Lang
- "arousal recovery" as a universal longform pacing law
- converting multimedia segmenting into a universal 60–90 second content block
- treating educational transfer findings as direct YouTube retention findings

Important correction:
Mayer's segmenting principle is about manageable/learner-paced segments. Some experimental examples use very short segments, but the literature does not establish a universal 60–90 second story interval.

Audit disposition:
KEEP M4 Capacity-Limited Processing as an A-priority mechanism.
DROP universal timing constants until directly tested in comparable longform/video conditions.
