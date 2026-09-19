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


### E-018 — Curiosity / Need-for-Closure family: real theory, causal/quantitative inflation
Status: MECHANISM SUPPORTED / METADATA INFLATED
Severity: MEDIUM/HIGH

Loewenstein (1994):
- verified as a Psychological Bulletin review/reinterpretation
- proposes curiosity as cognitively induced deprivation arising from a perceived knowledge/understanding gap

Repository inflation in `SRC-1994-034`:
- "Comprehensive meta-analytic review" is too strong
- relationship_type = "Causal" is not an appropriate summary of a theoretical/review paper
- direct claim that the mechanism drives longform completion is a Story Engine transfer

Kruglanski & Webster (1996):
- verified as a theoretical framework/review of need for cognitive closure
- distinguishes urgency ("seizing") and permanence ("freezing")
- closure can be both trait-like and situationally evoked

Repository inflation in `SRC-1996-139`:
- "multi-study review across thousands of subjects"
- generalized p<.001 claim
- commercial mass audiences and fatigued modern viewers asserted to have higher closure need
- open endings predicted to cause extreme anger/rating attacks

Audit disposition:
KEEP M5 Curiosity/Uncertainty as a strong cross-theme research target.
Separate:
- information-gap curiosity
- tolerance of ambiguity
- need for closure
- suspense
- narrative promise/payoff

Do not assume they are one mechanism or one audience state.

### E-019 — Trust / correction / source monitoring family: strong mechanism, exact percentages weak
Status: MECHANISM SUPPORTED / QUANTIFICATION HIGH-RISK
Severity: HIGH

Lewandowsky et al. (2012):
- verified review of misinformation, continued influence, memory updating, and correction/debiasing
- supports the importance of alternative explanations and correction design

Repository `SRC-2012-582` adds:
- "50% 이상" continued reliance
- "18% 이하" after alternative explanation
These exact values are not established by the verified abstract and require source-level tracing.

Johnson, Hashtroudi & Lindsay (1993):
- verified source-monitoring framework publication
- provides a foundational account of how people attribute memories to sources

Repository `SRC-1993-584` adds:
- "40% 이상" external-source-monitoring error from vivid reenactment/fake graphics
This exact quantified claim is not supported by the verified bibliographic record inspected.

Audit disposition:
M9 Trust/Provenance remains a strong high-priority mechanism family.
This strengthens the case for researching #60–#63 next with Claude under stricter evidence rules.


### E-020 — #29/#31 Prediction construct conflation
Status: CONFIRMED RESEARCH-DESIGN PROBLEM
Severity: CRITICAL for Research Map v2

The current Prediction Engine merges multiple distinct constructs under the word "prediction":

1. **Event-model prediction error**
   - Zacks et al. Event Segmentation Theory
   - short-horizon prediction of ongoing activity
   - transient prediction error → event-model updating / event boundary

2. **Narrative suspense / outcome expectation**
   - Gerrig & Bernardo (1994)
   - Hoeken & van Vliet (2000)
   - direct story-reading manipulations of available solutions, suspense, curiosity, surprise

3. **Mnemonic prediction error**
   - Sinclair et al. (2021)
   - familiar narrative videos interrupted before expected endings
   - hippocampal representation disruption and memory updating

4. **Reward prediction error (RPE)**
   - Schultz, Dayan & Montague (1997)
   - primate dopamine/reinforcement-learning literature
   - expected vs received rewarding/salient events

5. **Predictive processing / Free-Energy Principle**
   - Friston (2010)
   - high-level theoretical/computational framework for perception/action/learning

6. **Counterfactual thinking**
   - Roese (1997)
   - retrospective "what if / if only" simulation after outcomes
   - not the same construct as prospective narrative prediction

7. **Curiosity / complexity / uncertainty selection**
   - Kidd et al. (2012): 7–8 month-old infants' visual attention to intermediate complexity
   - Kang et al. (2009): trivia curiosity, caudate/reward-related activity, information seeking
   - better placed under M5 Curiosity/Managed Uncertainty than under a unified Prediction Engine

These constructs can interact, but the current corpus often treats them as one established neurocognitive mechanism.

Research Map implication:
SPLIT #29/#31 before precision research. Do not ask Claude to "verify Prediction Engine" as a unit.

### E-021 — SRC-2021-256 Sinclair bibliographic metadata corruption + dopamine misread
Status: CONFIRMED ERROR / IMPORTANT BRIDGE SOURCE
Severity: HIGH

Verified publication:
Sinclair, A. H.; Manalili, Grace M.; Brunec, Iva K.; Adcock, R. Alison; Barense, Morgan D. (2021).
"Prediction errors disrupt hippocampal representations and update episodic memories."
PNAS 118(51), e2117625118. DOI: `10.1073/pnas.2117625118`.

Repository author list is incorrect:
- "Matthew L. Manalili" → Grace M. Manalili
- "Gregory W. Brunec" → Iva K. Brunec
- "Michael D. R. Robin" → not an author on the verified paper
- Morgan D. Barense is omitted

Verified design/result:
- human fMRI study
- familiar narrative videos
- mnemonic prediction errors induced by interrupting videos immediately before expected endings
- prediction errors disrupted sustained hippocampal representations
- degree of representation disruption predicted memory updating
- basal forebrain activation moderated the relation between hippocampal representations and memory outcomes

Important negative evidence:
The paper reports no corresponding VTA three-way interaction and no significant main effect supporting a simple "prediction error → dopamine reward" interpretation.

Repository inflation:
- "prediction error size → stronger memory revision" is stronger than the verified result
- "basal forebrain cholinergic modulation maximizes attention/new narrative memory" is interpretive
- using this paper as support for pleasurable/dopaminergic plot-twist reward is incorrect

Disposition:
PROMOTE this as a strong, unusually direct **narrative-video memory-updating** source.
Do NOT use it as RPE/pleasure evidence.

### E-022 — Friston Free-Energy Principle repeatedly converted into Story Engagement law
Status: THEORY-TO-ENGINE LEAP / CONCEPTUAL CONFLATION
Severity: CRITICAL

The same Friston (2010) paper is registered at least three times:
- SRC-2010-229 (#29 T1)
- SRC-2010-255 (#31 T2)
- SRC-2010-311 (#36 T2)

Verified source:
A Nature Reviews Neuroscience review proposing a unifying free-energy framework for action, perception, and learning.

Repository transformations include:
- variational free energy = ordinary subjective uncertainty
- free-energy reduction = curiosity satisfaction
- active inference = page turning / binge watching
- prediction error resolution = dopaminergic intellectual reward
- high predictability = brain turns attention off / mind wandering
- exact Rehook timing derived from FEP

These mappings are not directly tested by Friston (2010).

Technical caution:
The paper treats variational free energy as a bound on surprisal within a generative-model framework. It should not be used as a synonym for ordinary narrative "mystery level," subjective surprise, or engagement.

Disposition:
KEEP FEP only as a broad theoretical analogy/background source unless a narrative-specific bridge study independently tests the proposed mapping.

### E-023 — #29 T2 Goldilocks evidence has a population/domain mismatch
Status: DOMAIN_TRANSFER_LEAP
Severity: HIGH

Kidd, Piantadosi & Aslin (2012):
- two experiments
- 7- and 8-month-old infants
- visual sequences
- looking-away probability highest for very low and very high complexity
- supports selective attention to intermediate information complexity in infants

Repository Report claims:
- "영유아 및 성인"
- optimal narrative prediction-error rate about 30–50%
- direct application to longform narrative immersion

The verified paper does not include adults and does not establish a 30–50% narrative prediction-error optimum.

Kang et al. (2009):
- trivia-question curiosity
- curiosity correlated with caudate activity associated with anticipated reward
- higher curiosity predicted greater willingness to spend resources for answers and better later recall

This supports epistemic curiosity, not a universal "middle prediction uncertainty = dopamine maximum" rule for narrative.

Disposition:
Move these sources primarily to M5 Curiosity/Managed Uncertainty.
Do not use them to calibrate a numeric Prediction Engine.

### E-024 — Direct narrative-prediction evidence exists and should be separated from neuroscience extrapolation
Status: POSITIVE AUDIT FINDING
Severity: HIGH strategic value

Gerrig & Bernardo (1994):
- seven experiments with fictional danger scenarios
- suspense ratings increased when readers believed the range of possible solutions was restricted
- likelihood-of-escape ratings were comparatively little affected

Hoeken & van Vliet (2000):
- manipulated narrative event order in a story
- studied suspense, curiosity, surprise structures
- suspense could occur even when readers knew the ending
- surprising events increased appreciation and improved representation of story events

These sources directly study narrative processing and are more appropriate foundations for Story Engine rules about suspense/curiosity/surprise than reward-learning or free-energy sources.

Disposition:
Create a separate **Narrative Expectation / Suspense / Surprise** research line and prioritize it in precision research.


### E-025 — Groves & Thompson habituation DOI error and major domain transfer
Status: CONFIRMED BIBLIOGRAPHIC ERROR / DOMAIN_TRANSFER_LEAP
Severity: HIGH

Repository `SRC-1970-004`:
- title/authors/year broadly identify the real paper
- stored DOI: `10.1037/h0029800`

Verified DOI:
- `10.1037/h0029810`

The foundational dual-process theory concerns habituation and sensitization in behavioral/neurophysiological systems. PubMed indexes the work under animal behavior and cats; the original theory was built from reflex/learning paradigms.

Repository transformation:
- repeated suspense cues → sensitization
- revealing threat early → habituation
- low-intensity valley → neural "resensitization"
- direct justification for longform emotional-wave design

Interpretation:
The general existence of habituation/sensitization is valid.
The specific mapping to story tension, emotional valleys, and "resensitizing receptors" is a large domain transfer requiring media/narrative bridge evidence.

### E-026 — Hedonic adaptation converted into a 8–10 minute media-emotion clock
Status: CONFIRMED ENGINE-HEURISTIC INJECTION
Severity: CRITICAL for timing rules

Frederick & Loewenstein (1999) is a real book chapter reviewing hedonic adaptation:
- attenuation of emotional/hedonic impact over time
- negative domains include noise, imprisonment, bereavement, disability
- positive domains include food, erotic images, wealth, appearance

It is not a study of:
- longform video
- amygdala baseline recovery after 8–10 minutes
- emotion-tone switching
- "receptor paralysis" after ten minutes

Repository reports/cards repeatedly convert the chapter into:
- same emotion >8–10 min → limbic/amygdala response returns to baseline
- switch emotional tone before 10 min
- low-intensity intervals reset the emotional baseline

Disposition:
KEEP adaptation as a broad caution against assuming constant subjective intensity.
DELETE/REVERIFY every exact media-emotion timing rule derived from this source.

### E-027 — Peak-End / Better-End effect is real but heavily overgeneralized to longform endings
Status: VALID MECHANISM / DOMAIN OVERGENERALIZATION
Severity: HIGH

Verified Kahneman et al. (1993):
- short trial: 60 s hand immersion around 14°C
- long trial: same 60 s plus 30 s during which water warmed slightly to about 15°C
- a significant majority later chose to repeat the longer trial
- retrospective evaluations of these aversive episodes gave relatively small weight to duration and substantial weight to the worst/final moments

This supports:
- retrospective evaluation can be disproportionately affected by end quality in specific experiential contexts
- duration can receive less retrospective weight than moment-to-moment experience

It does **not** directly establish:
- all longform stories are evaluated by the arithmetic mean of Peak + End
- a good ending erases a weak middle
- allocate 60% of production resources to peak/end
- mandatory 3–5 minute post-climax buffer
- ending design guarantees recommendation/rewatch
- universal NPS gains

Important nuance:
Duration neglect/peak-end-like effects have also been studied in other affective/effortful experiences, so the phenomenon should not be discarded. The question is transfer strength to longform narrative evaluation.

Disposition:
KEEP as a B-level retrospective-evaluation mechanism.
RESEARCH narrative/media-specific evidence separately before creating engine constants.

### E-028 — Carroll Narrative Closure has wrong DOI and is philosophical theory, not an empirical neuroscience study
Status: CONFIRMED BIBLIOGRAPHIC ERROR / THEORY_TO_EMPIRICAL_UPGRADE
Severity: CRITICAL

Repository `SRC-2007-503` stores:
- DOI `10.1007/s11098-007-9092-2`

Verified Carroll (2007) DOI:
- `10.1007/s11098-007-9097-9`

Verified contribution:
Carroll develops a theory in which narrative closure is a phenomenological feeling of finality generated when salient questions posed by the narrative are answered.

Repository upgrades this into:
- empirical/cognitive proof
- "affective satiety"
- direct emotional-payoff mechanisms
- backward-design production rules

Later scholarship explicitly critiques and refines Carroll's account, including questions about inclusiveness, gradability, plot vs narrative, and online vs ex-post closure.

Disposition:
KEEP Carroll as a narrative/aesthetic theory source.
Do not count it as behavioral causal evidence.

### E-029 — Payoff taxonomy treated as an empirically exhaustive natural law
Status: CONFIRMED RESEARCH-DESIGN / TRANSFORMATION ERROR
Severity: CRITICAL

#51 T1 asserts that nine payoff types:
Answer, Justice, Catharsis, Reframe, Admiration, Warning, Decision Rule, Hope, Bittersweet

are:
- empirically validated
- exhaustive
- mutually exclusive

The cited source set spans literary theory, emotion research, learning, moral psychology, and craft concepts. It does not constitute a taxonomic validation showing that exactly nine types exhaust the payoff space.

The Report then attaches untraceable claims including:
- closed-question stories +84% satisfaction
- cortisol -72%
- insight gamma activity +320%
- altruistic motivation 2.8x
- warning memory 2.4x / behavioral recall 3.1x
- bittersweet 3x persistence
- repeat viewing/music streaming +260%
- final architecture completion 94%+ / NPS +70

Interpretation:
The nine-type scheme may still be **very useful as a design taxonomy**.
It should be validated like an instrument/classification system:
- coverage
- overlap
- inter-rater agreement
- missing categories
- genre dependence
- predictive usefulness

It should not be called an empirically exhaustive psychological law.

### E-030 — Oliver expectation-disconfirmation is a plausible analogy, not direct narrative payoff evidence
Status: VALID SOURCE / DOMAIN_TRANSFER_CAUTION
Severity: MEDIUM

Verified Oliver (1980):
- consumer satisfaction modeled as expectation + expectancy disconfirmation
- satisfaction linked to attitude change and purchase intention
- supported in a two-stage field study involving flu-inoculation consumers/nonconsumers

Repository uses it as evidence that:
opening promise + ending payoff → audience satisfaction/recommendation.

This is a plausible cross-domain hypothesis, but the original study did not test:
- stories
- viewing completion
- narrative payoff
- creator loyalty

Disposition:
Move this to the future #64–#67 Promise/Expectation Contract research lane rather than using it as direct proof of #51 Payoff.

### E-031 — #52 Ending design converts multiple weakly related theories into exact production formulas
Status: CONFIRMED ENGINE_HEURISTIC_AS_EMPIRICAL_FACT
Severity: CRITICAL

Examples in current reports:
- mandatory 3–5 minute ending buffer
- 20-minute fatigue threshold
- NPS +75
- +40% pruning efficiency from backward ending design
- thematic-ending congruence +42%
- precomputed emotional foreshadowing nodes
- "open ending" dopamine/serotonin persistence

These values are not supported by the verified Carroll, Kahneman, or Oliver sources.

Positive finding:
#52 T2 correctly raises a strategically important **product-level risk**:
in nonfiction/factual storytelling, fixing the desired ending emotion/conclusion in advance can encourage confirmation bias, cherry-picking, and fact-fitting.

That risk should be retained and investigated in #60–#63, but it should not be presented as an experimental result of Carroll/Poe.


### E-032 — Identifiable-victim research is narrower than the corpus's universal "Human Scale" rule
Status: VALID SOURCE / DOMAIN_TRANSFER + QUANTIFICATION INFLATION
Severity: HIGH

Verified Small, Loewenstein & Slovic (2007):
- real peer-reviewed article
- series of field experiments on charitable donations
- central result in the abstract: prompting deliberation about the identifiable/statistical discrepancy reduced giving to identifiable victims without increasing giving to statistical victims

Repository transformation:
- "identifiable victim → 2x empathy/action"
- statistics themselves automatically cause psychic numbing
- direct generalization to all narrative/media audiences
- one person's concrete detail as a universal empathy switch

The identifiable-victim literature is clearly relevant to audience response to individual vs statistical victims, but this paper's core contribution is also about the interaction between affect and deliberation, not simply "one person always beats statistics."

Disposition:
KEEP as one component of M10.
REVERIFY exact magnitude and boundary conditions.
Do not make "one person > aggregate" a universal engine rule.

### E-033 — Slovic psychic-numbing source has wrong DOI and is partly a synthesis/argument, not a direct omnibus experiment
Status: CONFIRMED BIBLIOGRAPHIC ERROR / METHODOLOGY INFLATION
Severity: HIGH

Repository `SRC-2010-098` / cited work:
- title: "If I look at the mass I will never act: Psychic numbing and genocide"
- stored DOI: `10.1017/S1930297500000067`

Verified DOI:
- `10.1017/S1930297500000061`

Verified paper:
- Paul Slovic, Judgment and Decision Making 2(2), 79–95, 2007
- draws on psychological research to explain why statistics of mass harm often fail to evoke feeling/action

Repository inflation:
- labels the paper itself as multiple causal psychophysical experiments
- asserts emotional weight drops as soon as victim count rises from one to two
- treats a "micro-anchor rule" as directly proven for cinematic storytelling

Disposition:
KEEP psychic numbing / scope-response limits as a relevant mechanism family.
Separate evidence from related experiments cited by Slovic from claims made by Slovic's synthesis article.

### E-034 — Construal-Level Theory supports distance→abstraction, not a direct empathy/urgency law
Status: VALID MECHANISM / DOMAIN_TRANSFER_LEAP
Severity: MEDIUM/HIGH

Verified Trope & Liberman (2010):
- psychological distance includes temporal, spatial, social, and hypothetical distance
- greater distance is associated with higher-level/more abstract construal
- distance/construal relations influence prediction, preference, and action

Repository upgrades:
- near/concrete framing "immediately triggers visceral affect"
- Human Scale automatically increases empathy/risk perception
- direct narrative rule to zoom from system statistics to a single family/object

The core concrete-vs-abstract representation mechanism is strong.
The empathy, urgency, and storytelling effects require additional bridge evidence.

Disposition:
KEEP M10 but split "psychological distance/construal" from "identifiable victim/empathy."

### E-035 — Risk perception is a separate mechanism from Human Scale
Status: VALID MECHANISM / CONCEPTUAL CONFLATION
Severity: MEDIUM

Verified Slovic (1987):
- public risk judgment differs from purely technical estimates
- psychometric work identifies dimensions commonly summarized as dread risk and unknown risk

Repository transforms this into:
- "scale reversal" as a story device
- direct maximization of viewer arousal/threat by revealing a local event as a system-wide catastrophe

Risk perception may inform how stakes are framed, but it is not evidence for the same mechanism as identifiable victims or psychological distance.

Research Map implication:
M10 should become a family of related but distinct audience-relevance mechanisms rather than one "Human Scale" law.


### E-036 — SRC-2000-534 is a bibliographic conflation
Status: CONFIRMED ERROR
Severity: CRITICAL

Repository:
- ID: `SRC-2000-534`
- claimed title: "The effects of edit frequency and complexity on television message processing"
- claimed authors: Annie Lang et al.
- claimed venue: Media Psychology 2(1), 17–42
- stored DOI: `10.1207/S1532785XMEP0201_2`

Verified DOI:
`10.1207/S1532785XMEP0201_2` belongs to:
William D. McIntosh, Andria F. Schwegler & Rebecca M. Terry-Murray,
"Threat and Television Viewing in the United States, 1960–1990,"
Media Psychology 2(1), 35–46.

Related real Annie Lang research exists, including:
- Lang, Geiger, Strickwerda & Sumner (1993), related/unrelated cuts and television memory
- Lang, Bolls, Potter & Kawahara (1999), production pacing/arousing content and TV information processing
- Lang, Zhou, Schwartz, Bolls & Potter (2000), effects of edits on arousal, attention, and memory for television messages

Interpretation:
The repository Source appears to conflate a real Lang research program with an unrelated DOI and invented/mixed bibliographic metadata.

Downstream impact:
#55 T1 relies heavily on this record for exact cut-frequency overload claims.

### E-037 — Simons/Chabris and Henderson are valid attention sources but do not prove the corpus's "semantic refresh" metrics
Status: VALID MECHANISMS / APPLICATION + QUANTIFICATION INFLATION
Severity: HIGH

Verified Simons & Chabris (1999):
- inattentional blindness in dynamic events
- noticing an unexpected object depends on attentional task/object similarity and task difficulty
- focused attention strongly constrains what is perceived/remembered

It does **not** establish:
- narrative-semantic changes are always detected while surface changes are ignored
- semantic refresh guarantees attention reset
- exact cut pacing thresholds

Verified Henderson (2003):
- review of gaze control in real-world scenes
- gaze is actively directed toward important/informative scene regions

It does **not** establish the repository's:
- narration-matched object fixation latency -180 ms
- visual search errors -62%
- evidence-object pupil dilation +52%
- narrative "meaning map" as a quantified attention governor

Disposition:
KEEP selective attention/gaze allocation as a visual-design mechanism.
Do not attach the current numeric rules without source-level support.

### E-038 — #55 Visual Story cut-timing constants are unsupported engine heuristics
Status: CONFIRMED ENGINE_HEURISTIC_AS_EMPIRICAL_FACT
Severity: CRITICAL

Current #55 T1 introduces:
- optimal cut rhythm 4–8 s (average 5.5 s)
- overload threshold <2.5 s
- stagnation threshold >12 s
- three fast cuts trigger a minimum 5 s stable shot
- Eye-Trace coordinates must remain within 15%
- >12 cuts/min unrelated edits → memory collapse
- exact memory/attention percentages

The verified underlying literature supports:
- edits/formal features can elicit orienting/resource allocation
- processing capacity is limited
- fast/complex production interacts with information processing
- attention is selective

It does not establish one universal longform cut interval.

Disposition:
REMOVE these constants from "research fact" status.
Retain them, if useful, only as tunable production priors to be validated with actual video/retention experiments.

### E-039 — Dynamic graphics research supports congruence/apprehension constraints, not the #58 timing/acoustic formulas
Status: VALID DIRECTION / QUANTIFICATION INJECTION
Severity: CRITICAL

Verified Tversky, Morrison & Bétrancourt (2002):
- graphics help only when carefully designed
- Congruence Principle: graphic form/content should correspond to the concept
- Apprehension Principle: graphics should be readily/accurately perceived and understood
- animation does not automatically outperform static graphics

Verified Lowe (2003):
- animation provides dynamic information but creates additional processing demands
- learners must select thematically relevant information and integrate it into knowledge structures

These sources are compatible with:
- avoid gratuitous motion
- prioritize comprehensible visual organization
- motion can compete with reading/analysis

They do **not** directly support current #58 rules such as:
- data misreading +50%
- reading speed -60%, error +54%
- 6–9 s minimum proof-footage dwell
- 3 s graph accuracy 32% vs 6 s 86%
- visual element count >3 causes 2.6x gaze wandering
- narration/BGM conflict -42%
- mandatory -12 dB ducking or 1–3 kHz EQ window
- exact 5–8 s fact phase + 4–6 s emotion phase

Disposition:
Retain qualitative **information-motion compatibility** as a strong design concern.
Move all timing/audio engineering constants to empirical production testing.

### E-040 — Visual research block has mixed evidence classes and reduced source provenance
Status: CONFIRMED RESEARCH-DESIGN PROBLEM
Severity: HIGH

#55–#58 combine:
- experimental media psychology
- visual cognition
- educational multimedia research
- film-style analysis
- film theory/craft
- design books
- neuroscience/cinema theory
- general emotion research

They are currently flattened into Tier 1 and then combined into precise production formulas.

Additionally, Sources #558–#589 use a reduced schema with no venue/URL in the index, lowering machine traceability exactly across #57–#59.

Research Map implication:
M11 should be split before further precision research.
