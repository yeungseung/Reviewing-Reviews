# REVIEW² Source Acquisition Architecture v1

## 1. Mission

이 계층은 REVIEW²에서 가장 중요한 질문을 담당한다.

```text
"우리는 정확히 무엇을 보고 이 말을 하는가?"
```

Presentation Engine이 "어떻게 보여줄 것인가"를 담당한다면,
Source Acquisition Engine은 **무엇을 믿고 사용할 수 있는가**를 담당한다.

---

## 2. Pipeline

```text
PRODUCT SCOPE
     ↓
SEARCH INTENT
     ↓
QUERY PLAN
     ↓
SEARCH RUN
     ↓
SOURCE CANDIDATE
     ↓
SOURCE TRIAGE
     ↓
HUMAN SOURCE GATE
     ↓
SOURCE RECORD
     ↓
SOURCE LINEAGE
     ↓
SNAPSHOT / CAPTURE
     ↓
LOCATOR
     ↓
EVIDENCE PACKET
     ↓
CLAIM
     ↓
FINDING
```

---

## 3. Core entities

### 3.1 Query Plan

무엇을 찾아야 하는지 정의한다.

포함:

- product scope
- buyer questions
- query families
- target source tiers
- target source kinds
- region/language
- time window
- coverage goals

Query Plan은 실제 검색 기록이 아니다.

### 3.2 Search Run

실제로 어떤 검색을 언제 어디서 수행했는지 기록한다.

포함:

- query
- provider
- locale
- timestamp
- requested depth
- observed result count
- candidate URLs
- selected/rejected counts
- gap notes

검색 결과가 없었던 것도 기록한다.

### 3.3 Source Candidate

검색에서 발견했지만 아직 신뢰할 source로 승인되지 않은 항목.

상태:

```text
new
triaged
needs_human
accepted
rejected
duplicate
wrong_product
inaccessible
```

### 3.4 Source

논리적인 출처 identity.

예:

- 제조사 제품 페이지
- 설명서 PDF
- 전문 매체 리뷰 한 편
- YouTube 영상 한 편
- Amazon 리뷰 한 건
- 가격 비교 페이지

Source는 "어디에서 나온 정보인가"를 나타낸다.

### 3.5 Source Relation

Source 간의 관계.

초기 relation type:

```text
same_as
mirror_of
syndicated_from
quotes
summarizes
derived_from
embeds
references
unknown_relation
```

이 relation을 이용해
"10개 URL = 10개 독립 근거" 오류를 방지한다.

### 3.6 Snapshot

Source를 특정 시점에 관찰한 고정 상태.

포함:

- access time
- final URL
- response metadata where available
- capture method
- local artifact paths
- hash
- content type
- extracted text hash
- screenshot / PDF / WARC / WACZ references

### 3.7 Locator

Source/Snapshot 내부에서 정확히 어느 부분을 근거로 삼았는지 나타낸다.

지원 locator:

```text
text_quote
text_position
css
xpath
pdf_page
pdf_region
media_time
image_region
table_cell
manual_note
```

가능하면 locator를 하나만 쓰지 않는다.

웹 텍스트 기본:

```text
Text Quote
+
Text Position
+
snapshot id
```

영상 기본:

```text
media_time
+
transcript quote
+
snapshot/source id
```

### 3.8 Evidence Packet

Claim을 만들기 직전의 최소 검증 단위.

```text
Evidence Packet
├─ source
├─ snapshot
├─ locator
├─ exact evidence
├─ context
├─ product scope
├─ lineage / independence
├─ verification
└─ usability
```

Analysis Engine은 가능하면 raw URL보다 Evidence Packet을 소비한다.

---

## 4. Source identity model

Source는 최소 다음을 식별한다.

```text
source_id
tier
kind
title
canonical_url
platform
publisher
author
published_at
language
region
product_scope
publication_role
lineage_root
independence_group
human_verification
```

### tier

기존 3-tier 유지:

- official
- expert
- user

### kind

더 세밀한 유형:

```text
manufacturer_product_page
manual
support_document
press_release
regulatory_document
expert_review
lab_test
comparison_article
news_article
retailer_listing
retailer_review
marketplace_review
forum_post
community_thread
youtube_video
social_post
blog_post
price_tracker
other
```

Tier와 kind는 분리한다.

예:

```text
tier = user
kind = marketplace_review
```

### publication_role

```text
ORIGINAL
DERIVED
SYNDICATED
AGGREGATOR
MIRROR
UNKNOWN
```

이 값은 "source quality"가 아니라
정보의 lineage 역할이다.

---

## 5. Product scope verification

제품 리뷰에서 가장 위험한 오류 중 하나:

```text
비슷한 제품
다른 세대
다른 국가 모델
다른 firmware
다른 용량
```

을 같은 제품으로 합치는 것.

모든 Source/Evidence Packet에 product match를 기록한다.

```text
EXACT
COMPATIBLE_VARIANT
RELATED_MODEL
AMBIGUOUS
MISMATCH
```

가능하면:

- brand
- family
- model
- variant
- capacity
- region
- release generation
- firmware / software version

를 분리한다.

Human Source Gate에서
AMBIGUOUS / MISMATCH는 자동 분석에 넣지 않는다.

---

## 6. Search architecture

### 6.1 Query families

제품마다 최소 다음 query family를 고려한다.

```text
IDENTITY
SPEC
POSITIVE
NEGATIVE
FAILURE
LONG_TERM
NOISE / HEAT / BATTERY etc.
COMPARISON
PRICE
MAINTENANCE
SUPPORT
RECALL / ISSUE
USER COMMUNITY
VIDEO
```

카테고리에 따라 확장한다.

### 6.2 Coverage matrix

검색을 끝내는 기준을
"링크를 많이 모았다"로 두지 않는다.

예:

```text
buyer question      official expert user
────────────────────────────────────────
noise                  ✓       ✓     ✓
filter cost             ✓       -     ✓
long-term failure       -       ✓     ✓
cleaning difficulty     ✓       ✓     ✓
```

빈칸은 Search Gap이다.

### 6.3 Search Ledger

모든 Search Run을 남긴다.

기록할 것:

- query
- provider
- executed_at
- locale / region
- result depth
- result URLs
- decision
- rejection reason
- next-query suggestion
- uncovered question

목적:

```text
"왜 이 결론이 나왔는가"
→ 검색 과정까지 역추적
```

---

## 7. Human Source Gate

AI가 candidate를 수집한 다음
사람이 들어오는 공식 gate.

### Human actions

```text
ACCEPT
REJECT
DUPLICATE
WRONG_PRODUCT
MARK_DERIVED
LINK_ORIGIN
CAPTURE
NEEDS_MORE_RESEARCH
```

### Required human checks for accepted evidence source

- source identity 확인
- product match 확인
- publisher/author 가능한 만큼 확인
- published date 확인
- original/derived 판단
- relevant evidence 직접 읽기/보기
- 주변 context 확인
- capture 실행 여부 확인

Human Source Gate 통과 전에는
candidate를 production evidence로 사용하지 않는다.

---

## 8. Source lineage and independence

### Problem

```text
A press release
→ site B
→ site C
→ blogger D
```

텍스트가 반복되어도
독립된 4개 evidence가 아니다.

### independence_group_id

같은 정보 origin chain이라고 판단되는 source를
같은 independence group으로 묶을 수 있다.

예:

```text
IG_0021
├─ manufacturer press release
├─ syndicated article
├─ affiliate rewrite
└─ retailer summary
```

Consensus 계산 시
동일 independence group을 별도 독립 표본처럼 세지 않는다.

### lineage confidence

```text
confirmed
probable
possible
unknown
```

AI가 relation을 추정할 수 있지만
중요 relation은 사람이 승인한다.

---

## 9. Snapshot and capture policy

### 9.1 Immutable raw

한 번 승인된 snapshot raw artifact는 수정하지 않는다.

수정/가공된 파일은 derivative artifact로 새로 만든다.

```text
RAW
→ EXTRACTED
→ CROPPED
→ REDACTED
→ VIDEO_ASSET
```

각 derivative는 parent artifact id를 가진다.

### 9.2 Minimum snapshot package

가능하면:

```text
metadata.json
content.*
extracted.txt
page.png or evidence screenshot
sha256
```

중요 웹페이지는 WARC/WACZ 추가를 권장한다.

### 9.3 Hash

capture마다 SHA-256 기록.

목적:

- accidental modification detection
- duplicate capture detection
- provenance

Hash는 "웹 서버가 그 내용을 보냈다는 법적 증명"을 의미하지 않는다.
우리 시스템이 보관한 artifact의 동일성 검증용이다.

### 9.4 Capture tier

```text
LIGHT
metadata + selected screenshot/text

STANDARD
HTML/PDF + extracted text + screenshot + hash

ARCHIVE
WARC/WACZ + screenshot + extracted text + hash
```

핵심 결론 source는 STANDARD 이상 권장.

---

## 10. Locator model

### Web text

기본:

```json
{
  "type": "text_quote",
  "exact": "...",
  "prefix": "...",
  "suffix": "..."
}
```

가능하면 추가:

```json
{
  "type": "text_position",
  "start": 1255,
  "end": 1321
}
```

CSS/XPath는 보조 locator로 취급한다.

### PDF

```text
page
+
text quote
+
optional bounding box
```

### Video

```text
start_time
end_time
+
transcript quote
+
frame capture
```

### Image

```text
image_region
+
human note
```

---

## 11. Evidence Packet contract

Evidence Packet은 raw source를
analysis-ready evidence로 바꾸는 gate다.

필수 개념:

```text
packet_id
source_id
snapshot_id
locator_ids
evidence_type
exact_text / observed_value
context_text
product_match
independence_group
origin_type
human_verified
verification_notes
usable_for_claim
usable_for_video
```

### usable_for_claim

팩트 분석에 사용 가능한가.

### usable_for_video

영상에서 직접 화면으로 보여줘도 되는가.

둘은 다를 수 있다.

예:

```text
공식 PDF의 표
→ claim: yes
→ video: yes

사용자 리뷰 긴 원문
→ claim: yes
→ video: quote card only

검색 snippet
→ claim: no
→ video: no
```

검색 결과 snippet 자체를 evidence로 사용하지 않는다.

---

## 12. Capture asset provenance

Production asset에도 provenance chain을 유지한다.

예:

```text
A_VIDEO_042
↓ derived_from
A_FRAME_017
↓ derived_from
N_SNAPSHOT_008
↓ snapshot_of
S_SOURCE_014
↓ supports
EP_0031
↓ supports
C_0114
↓ contributes_to
F_0018
↓ used_by
SCENE_S14
```

최종 영상의 한 문장/장면에서
원출처까지 올라갈 수 있어야 한다.

---

## 13. Source Desk

Mac Studio에서 사람이 사용할 UI/도구 개념.

```text
┌──────────────────────────────────────────────────────┐
│ Query / Buyer Question                    [SEARCH]   │
├───────────────┬──────────────────────────────────────┤
│ Candidates    │ Source Viewer                        │
│               │                                      │
│ ○ Official    │ Title / Publisher / Date            │
│ ○ Expert      │ Canonical URL                       │
│ ○ User        │ Product match                       │
│               │ Original / Derived chain            │
│               │                                      │
│               │ Relevant passage / timestamp        │
│               │ Context before / after              │
│               │                                      │
│               │ [ACCEPT] [REJECT] [LINK ORIGIN]     │
│               │ [CAPTURE] [CREATE EVIDENCE]         │
└───────────────┴──────────────────────────────────────┘
```

목표:

사람이 metadata를 타이핑하는 것이 아니라
**판단 버튼을 누르는 것**.

---

## 14. Automation boundary

### Automate aggressively

- query expansion
- search collection
- metadata extraction
- canonical URL resolution
- duplicate detection
- text similarity
- source lineage suggestion
- timestamps
- transcription
- screenshot candidate
- hash
- capture manifest
- Evidence Packet draft

### Human authority

- source acceptance
- product identity match
- original-source judgment for important evidence
- misleading-context judgment
- capture framing
- final locator verification
- evidence interpretation
- source relationship confirmation when material

---

## 15. Search failure is data

다음도 결과로 기록한다.

```text
NO_RESULT
INSUFFICIENT_OFFICIAL
INSUFFICIENT_EXPERT
INSUFFICIENT_USER
CONFLICT_UNRESOLVED
PRODUCT_IDENTITY_AMBIGUOUS
ACCESS_BLOCKED
PAYWALLED
REMOVED
REGION_BLOCKED
```

Finding Engine은
"찾지 못함"을 "없음"으로 바꾸면 안 된다.

---

## 16. Local folder contract

GitHub repo와 별개로
실제 제품 프로젝트는 Mac Studio에서 다음 구조를 권장한다.

```text
/projects/<product_slug>/
  /research/
    search_plan.json
    search_runs.jsonl
    candidates.jsonl
    sources.jsonl
    source_relations.jsonl
    snapshots.jsonl
    locators.jsonl
    evidence_packets.jsonl
    claims.jsonl

  /source-vault/
    /<source_id>/
      /<snapshot_id>/
        metadata.json
        raw/
        extracted/
        screenshots/
        clips/
        derivatives/
        manifest.sha256

  /analysis/
  /script/
  /scenes/
  /assets/
  /render/
  /output/
```

`source-vault`는 Git에 넣지 않는다.

---

## 17. IDs

ID prefix 권장:

```text
QP_   Query Plan
SR_   Search Run
SC_   Source Candidate
S_    Source
REL_  Source Relation
N_    Snapshot
L_    Locator
EP_   Evidence Packet
A_    Asset / Capture Derivative
C_    Claim
F_    Finding
```

ID는 의미를 인코딩하지 않는 stable identifier를 권장한다.

---

## 18. Verification states

Source:

```text
candidate
verified
rejected
deprecated
```

Snapshot:

```text
pending
captured
verified
invalid
```

Evidence Packet:

```text
draft
human_verified
rejected
superseded
```

Claim은 기본적으로
human_verified Evidence Packet만 production Finding에 사용한다.

자동 실험 모드에서는 예외를 명시적으로 opt-in한다.

---

## 19. Quality gates

### Search Gate

- major buyer questions covered?
- official/expert/user balance adequate?
- known gaps recorded?

### Source Gate

- product identity correct?
- original/derived relation considered?
- canonical source known where possible?
- source tier/kind correct?

### Snapshot Gate

- capture readable?
- timestamp present?
- hash present?
- dynamic content preserved sufficiently?

### Evidence Gate

- exact locator exists?
- surrounding context checked?
- lineage/independence known enough?
- human verified?
- claim wording faithful?

---

## 20. Non-negotiable rules

### Rule 1

Search result snippet is discovery material, not evidence.

### Rule 2

A URL is not a provenance record.

### Rule 3

Repeated wording across many pages is not automatically independent evidence.

### Rule 4

Every important claim must point to at least one Evidence Packet.

### Rule 5

Every Evidence Packet must point to a Snapshot and Locator,
unless the source cannot technically be captured and the exception is recorded.

### Rule 6

Original raw capture is immutable.

### Rule 7

AI may suggest provenance.
Human confirms material provenance decisions.

### Rule 8

Product/model mismatch is a hard failure,
not a low-confidence evidence item.

---

## 21. Architecture formula

```text
SEARCH LEDGER
+ SOURCE IDENTITY
+ SOURCE LINEAGE
+ IMMUTABLE SNAPSHOT
+ PRECISE LOCATOR
+ HUMAN VERIFICATION
+ EVIDENCE PACKET
= REVIEW² TRUST LAYER
```

---

## 22. Relationship to Presentation Engine

```text
SOURCE ACQUISITION
→ 무엇을 믿을 것인가

ANALYSIS
→ 자료가 무엇을 말하는가

STORY
→ 무엇을 이야기할 것인가

PRESENTATION
→ 어떻게 이해시킬 것인가

RENDER
→ 어떻게 픽셀로 만들 것인가
```

REVIEW²의 품질 우선순위는 이 순서를 거꾸로 뒤집지 않는다.
