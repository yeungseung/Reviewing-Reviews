# REVIEW² ENGINE — Architecture v0.1

## 1. Mission

「리뷰를 리뷰하다」는 제품 자체를 직접 평가하는 단일 리뷰 채널이 아니라,
여러 출처의 리뷰·테스트·사용기·공식 정보를 구조화해 **구매 판단을 재구성하는 시스템**이다.

영상은 최종 출력물이며, 핵심 자산은 제품별 Evidence / Claim / Finding 데이터다.

---

## 2. Pipeline

```text
PRODUCT
  ↓
SEARCH INTENT
  ↓
SOURCE COLLECTION
  ↓
CLAIM EXTRACTION
  ↓
EVIDENCE NORMALIZATION
  ↓
CLUSTER / CONFLICT / CONDITION ANALYSIS
  ↓
BUYER QUESTIONS
  ↓
STORY
  ↓
NARRATION
  ↓
SCENE JSON
  ↓
RENDER
  ↓
QA
  ↓
PUBLISH
  ↓
PERFORMANCE FEEDBACK
```

---

## 3. Core entities

### Product
분석 대상 제품과 버전, 지역, 판매 시점 등을 정의한다.

### Source
공식 문서, 전문 리뷰, 사용자 후기, 커뮤니티 등 원 출처.

### Claim
한 출처에서 추출한 최소 단위의 주장.

예:
- "취침 모드에서도 소리가 신경 쓰인다"
- "필터 교체 비용이 생각보다 크다"
- "거실에서는 충분히 조용하다"

### Finding
여러 Claim을 묶어 얻은 분석 결과.

유형:
- consensus
- recurring_complaint
- conflict
- conditional
- insufficient_evidence

### Buyer Question
검색자가 실제로 답을 원하는 구매 질문.

### Story Beat
영상의 논리·감정 전개 단위.

### Scene
렌더러가 소비하는 화면 단위.

---

## 4. Evidence hierarchy

### Official
- 제조사 페이지
- 설명서
- 스펙표
- 지원 문서

강점: 기능과 공식 사양 확인  
한계: 실제 사용성 판단에는 부족

### Expert
- 전문 매체 리뷰
- 측정 테스트
- 비교 실험

강점: 조건 통제, 측정값  
한계: 샘플 수와 테스트 조건 제한

### User
- 구매 후기
- 장기 사용기
- 커뮤니티 경험담

강점: 실제 생활 문제, 장기 사용 문제  
한계: 환경 차이, 선택 편향, 광고성 가능성

---

## 5. Claim-first model

리뷰 하나를 하나의 레코드로 끝내지 않는다.
리뷰 내부에서 독립적인 Claim을 분해한다.

```text
Review A
 ├─ Claim: 디자인이 좋다
 ├─ Claim: 취침 시 소음이 거슬린다
 └─ Claim: 필터 교체가 쉽다
```

이 구조가 있어야 출처가 달라도 같은 주제를 비교할 수 있다.

---

## 6. Analysis engine

### 6.1 Consensus
여러 독립 출처에서 같은 평가가 반복되는가

### 6.2 Recurring complaint
실사용자에게서 같은 불만이 반복되는가

### 6.3 Conflict
평가가 갈리는가

### 6.4 Conditional split
평가 차이가 사실상 환경 차이 때문인가

예:

```text
"조용하다"
→ 거실 / 낮 / 풍량 1~2

"시끄럽다"
→ 침실 / 밤 / 머리맡 1m
```

### 6.5 Insufficient evidence
주장은 많아 보이지만 독립된 근거가 부족한가

---

## 7. Claim origin / contamination detection

리뷰 생태계가 마케팅 문구를 반복하는지 확인한다.

Origin type:

- MARKETING_ORIGIN
- EXPERT_ORIGIN
- USER_ORIGIN
- MIXED
- UNKNOWN

예:

```text
브랜드 공식 페이지  7회
보도자료            11회
제휴 블로그          23회
실구매 후기           2회
```

이 경우 "많은 리뷰가 칭찬한다"가 아니라
"자주 언급되지만 실제 구매자 후기에서는 많이 등장하지 않는다"로 해석할 수 있다.

---

## 8. Search-intent engine

검색 최적화는 제작 마지막 단계가 아니라 제품 선정 단계부터 시작한다.

예시 쿼리:

```text
商品名 レビュー
商品名 口コミ
商品名 評判
商品名 デメリット
商品名 うるさい
商品名 壊れやすい
商品名 比較
商品名 違い
商品名 買うべき
商品名 おすすめしない
```

핵심 교집합:

```text
검색자가 궁금해함
    ∩
실사용자가 반복해서 언급함
    ∩
전문 리뷰가 검증 가능함
    =
영상에서 반드시 답할 질문
```

---

## 9. Story grammar

고정 템플릿이 아니라 고정 문법을 사용한다.

```text
HOOK
↓
왜 이 제품을 고민하는가
↓
공통적으로 인정되는 장점
↓
그런데
↓
반복해서 등장하는 문제
↓
평가가 갈리는 지점
↓
왜 평가가 갈렸는가
↓
어떤 사용 조건에서 결과가 달라지는가
↓
누구에게 맞는가
↓
누가 피하는 편이 나은가
↓
구매 전 확인할 것
```

제품에 따라 순서와 길이는 달라진다.

---

## 10. Scene grammar

렌더러는 Scene JSON을 입력으로 받는다.

초기 Scene 타입 후보:

- hook
- product_intro
- review_wall
- consensus
- complaint_cluster
- review_conflict
- condition_split
- expert_test
- spec_vs_reality
- price_compare
- timeline
- who_fits
- who_avoids
- final_check

예:

```json
{
  "scene_id": "S14",
  "type": "review_conflict",
  "duration": 7.2,
  "narration": "그런데 소음에 대한 평가는 완전히 갈렸습니다",
  "data": {
    "positive": 73,
    "negative": 41,
    "condition_a": "living_room",
    "condition_b": "bedroom"
  },
  "visual": {
    "layout": "split",
    "animation": "review_cards_to_two_groups"
  }
}
```

---

## 11. Renderer architecture

### HyperFrames
메인 영상 엔진

담당:
- 리뷰 카드
- 숫자
- 그래프
- 제품 비교
- 키워드 군집
- 연결선
- 타이포그래피
- 실제 영상/이미지 배치

### srt-whiteboard-animation
서브 렌더러

담당:
- 원리 설명
- 구조 설명
- 복잡한 개념
- 사용 과정

전체 영상의 특수 설명 컷에 제한적으로 사용한다.

---

## 12. Project folder contract

```text
/projects/<product_slug>/
  project.yaml

  /research/
    sources.json
    raw_reviews.jsonl
    claims.jsonl
    evidence.json

  /analysis/
    clusters.json
    conflicts.json
    buyer_questions.json
    findings.json

  /script/
    outline.json
    narration_ja.md
    narration_ko.md

  /audio/
    narration.wav
    transcript.json

  /scenes/
    scenes.json

  /assets/
    official/
    expert/
    reviews/
    product/
    charts/

  /render/
    hyperframes/
    whiteboard/

  /output/
    preview.mp4
    final.mp4
    thumbnail/

  /publish/
    title.txt
    description.txt
    chapters.txt
    sources.md
```

---

## 13. Human-in-the-loop gates

### Product Gate
영상화 가치 판단

### Evidence Gate
출처 충분성·편향 검토

### Story Gate
핵심 질문·서사 결정

### Final Gate
팩트·뉘앙스·영상 완성도 검토

그 외 반복적인 작업은 가능한 한 자동화한다.

---

## 14. Long-term asset

최종 자산은 영상 파일이 아니다.

```text
제품별 Evidence DB
+ Claim DB
+ Finding DB
+ Scene component library
+ 제작 성과 데이터
```

이 자산이 누적되면 같은 제품 재활용, 카테고리 비교, 후속 영상, 세대별 비교가 쉬워진다.


---

## 15. Source Acquisition Engine

REVIEW²의 앞단 trust layer는 별도 Source Acquisition Architecture를 사용한다.

상세:
- `docs/SOURCE_ACQUISITION_ARCHITECTURE.md`
- `docs/SOURCE_ACQUISITION_RESEARCH.md`
- `docs/SOURCE_DESK.md`

Canonical evidence path:

```text
Query Plan
→ Search Run
→ Source Candidate
→ Human Source Gate
→ Source
→ Source Relation
→ Snapshot
→ Locator
→ Evidence Packet
→ Claim
→ Finding
```

Source URL에서 Claim으로 바로 점프하지 않는다.

Production Finding은 원칙적으로
human-verified Evidence Packet을 사용한다.

Long-term asset은 다음을 포함한다.

```text
Search Ledger
+ Source Graph
+ Snapshot Vault
+ Evidence Packets
+ Claims
+ Findings
+ Scene Component Library
+ Performance Data
```
