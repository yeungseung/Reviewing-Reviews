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
