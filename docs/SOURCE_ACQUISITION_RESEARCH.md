# REVIEW² Source Acquisition Research

Research date: 2026-09-16

## 1. Problem

REVIEW²의 신뢰는 영상의 포장보다 앞단에서 결정된다.

핵심 질문:

- 무엇을 검색했는가
- 어떤 결과를 봤는가
- 무엇을 버렸는가
- 이 자료는 원출처인가 재전재인가
- 정확히 어느 문장 / 어느 시점이 근거인가
- 당시 페이지 상태를 다시 확인할 수 있는가
- 사람이 무엇을 직접 확인했는가
- 영상에 실제 사용된 캡처가 어느 원출처에서 파생됐는가

단순 URL 목록으로는 이 질문들에 답할 수 없다.

---

## 2. Standards and systems reviewed

### W3C PROV

PROV는 provenance를 다음 핵심 개념으로 나눈다.

- Entity
- Activity
- Agent
- Derivation

REVIEW²에 대응하면:

```text
live source page      = Entity
snapshot capture      = Activity
snapshot              = derived Entity
human verification    = Activity
evidence packet       = derived Entity
claim                 = derived Entity
editor / automation   = Agent
```

모든 PROV 기능을 구현할 필요는 없지만,
"무엇이 무엇에서 파생되었는가"를 기록하는 사고방식을 채택한다.

### W3C Web Annotation

웹의 특정 근거를 단순 CSS selector 하나로 저장하는 것은 취약하다.

참고할 locator:

- TextQuoteSelector
  - exact
  - prefix
  - suffix
- TextPositionSelector
  - start
  - end
- Fragment / range concepts

REVIEW²는 text evidence에
quote + position을 같이 저장하는 것을 기본으로 한다.

### Hypothesis

실제 annotation implementation에서도
TextQuoteSelector와 TextPositionSelector를 함께 사용한다.

참고점:

```text
one locator method fails
→ another locator helps re-anchor
```

### WARC

WARC는 웹 수집 당시의 HTTP response/resource와 관련 metadata를
archive record로 보존하기 위한 널리 쓰이는 web archive format이다.

REVIEW²는 모든 페이지를 반드시 WARC로 저장하지는 않는다.

그러나 다음 자료에는 archive capture를 권장한다.

- 핵심 official source
- 이후 수정될 가능성이 높은 page
- 동적/삭제 가능성이 큰 evidence page
- 최종 영상의 핵심 결론을 지탱하는 source

### WACZ

WACZ는 WARC와 index/context metadata를 ZIP package로 묶는다.

특히 참고할 부분:

- manifest
- resource list
- SHA-256 fixity
- context metadata
- optional signature / verification

REVIEW²의 local source vault도
모든 capture에 hash를 기록한다.

### Zotero

참고할 부분:

- source bibliographic identity
- author / title / URL
- publication date
- access date
- snapshot attachment

REVIEW²는 bibliography manager가 아니므로
더 강한 product identity / source lineage / evidence locator가 필요하다.

### ArchiveBox / Webrecorder family

참고할 부분:

- snapshot identity
- capture timestamp
- archive artifacts
- metadata + stored representation 분리

---

## 3. Core conclusion

REVIEW² source system should not be:

```text
URL
→ claim
```

It should be:

```text
QUERY
→ SEARCH RUN
→ CANDIDATE
→ SOURCE
→ SOURCE RELATION
→ SNAPSHOT
→ LOCATOR
→ EVIDENCE PACKET
→ CLAIM
```

---

## 4. Critical distinctions

### Source != Snapshot

Source:
logical publication identity.

Example:

```text
Sony product page for model X
```

Snapshot:
the observed representation at one moment.

Example:

```text
Sony product page captured at 2026-09-16T13:20Z
```

A source may have many snapshots.

### Source != Asset

Source:
the publication.

Asset:
a crop, frame, clip or screenshot used in production.

```text
Source S014
→ Snapshot N022
→ Capture A091
→ 00:31.2–00:34.8 clip
```

### Claim != Evidence

Claim:
normalized proposition.

Evidence Packet:
the inspectable evidence backing that claim.

One claim may have multiple Evidence Packets.

### Multiple URLs != multiple independent sources

```text
manufacturer press release
→ news article
→ affiliate blog
→ retailer article
```

may represent one origin chain.

Therefore source lineage and independence grouping are mandatory.

---

## 5. Human role

AI can assist:

- query generation
- result collection
- metadata extraction
- canonical URL suggestion
- original/derived hypothesis
- duplicate detection
- source relation suggestion
- relevant text/time suggestion
- product model suggestion
- candidate ranking

Human verifies:

- source identity
- actual original source
- product/model/market match
- date
- author/publisher
- sponsored / affiliate context when material
- exact evidence
- context around evidence
- capture worthiness
- source relationship
- final acceptance/rejection

The user should spend judgment,
not time manually typing metadata.

---

## 6. Storage conclusion

GitHub stores:

- schemas
- metadata examples
- search/source architecture
- code
- rules

Mac Studio source vault stores:

- WARC/WACZ where used
- HTML/PDF
- screenshots
- captured frames
- clips
- extracted text
- thumbnails/contact sheets
- hashes/manifests

Large evidence artifacts should not be committed to Git.

---

## 7. Design principle

```text
Search must be auditable.
Sources must be identifiable.
Evidence must be pinpointable.
Captures must be reproducible.
Derivations must be traceable.
Human verification must be explicit.
```
