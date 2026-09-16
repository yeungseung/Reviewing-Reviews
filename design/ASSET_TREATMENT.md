# REVIEW² Asset Treatment v1

## 1. Principle

Asset Treatment is a **Human Editorial Layer**.

AI may analyze, classify, timestamp, summarize, rank candidates, and propose usage,
but final visual selection remains human-controlled.

Reason:

- the most informative shot is not always the most visually effective shot
- AI can understand content but may miss visual taste, timing, framing, product appeal, and emotional emphasis
- a strong scene often depends on a 1–3 second editorial choice that is difficult to reduce to rules

Therefore:

```text
AI = assistant
Human = editor
```

---

## 2. AI responsibilities

AI can automate or assist:

- asset inventory
- source metadata
- candidate timestamp extraction
- duplicate detection
- rough quality scoring
- face/product visibility checks
- text-heavy vs visual-heavy classification
- shot type classification
- scene-to-asset suggestion
- evidence/source linkage
- filename normalization
- thumbnail/contact-sheet generation
- usage log generation

AI recommendations are advisory.

---

## 3. Human responsibilities

Human decides:

- final clip
- exact in/out point
- crop
- zoom
- framing
- visual rhythm
- scene order
- emotional emphasis
- whether a technically relevant asset is visually boring
- whether a beautiful asset is misleading
- whether product appearance matches the narrative moment

The human editor may override all automated suggestions.

---

## 4. Asset roles

Every selected asset should have a role.

### HERO
제품 자체를 가장 매력적이고 명확하게 보여준다.

### EVIDENCE
주장이나 측정 결과를 증명한다.

### CONTEXT
제품이 실제로 쓰이는 상황을 보여준다.

### DETAIL
버튼, 재질, 포트, 필터, 내부 구조 등 세부사항.

### COMPARISON
다른 제품이나 상태와 비교.

### SOURCE
웹페이지, 리뷰, 공식 문서, 사용자 후기 등 출처 자체를 보여준다.

### MOOD
정보보다 제품 카테고리의 분위기와 리듬을 만든다.

---

## 5. Selection order

한 scene에 asset을 넣을 때 다음 순서로 판단한다.

1. 이 장면에서 무엇을 이해해야 하는가
2. 그 정보를 가장 직접적으로 보여주는 자료가 있는가
3. 시각적으로 지루하지 않은가
4. 다른 scene과 중복되지 않는가
5. source가 정확히 연결되는가
6. 과장하거나 오해를 만들 가능성이 없는가

---

## 6. Cropping rule

자동 crop은 preview 용도로만 사용한다.

Final crop은 사람이 확인한다.

특히:
- 제품의 주요 형상이 잘리지 않는지
- UI의 중요한 숫자/문구가 잘리지 않는지
- 얼굴/손/제품 관계가 이상하지 않은지
- 원본의 의미가 crop으로 바뀌지 않는지

확인한다.

---

## 7. Review capture

리뷰 캡처는 장식이 아니라 증거다.

기본 규칙:

- 필요한 문장만 강조
- 사용자명 등 불필요한 개인정보는 최소화
- 출처 플랫폼 표시
- 의미가 바뀌도록 문장을 잘라내지 않음
- 여러 리뷰를 하나의 리뷰처럼 합치지 않음
- 번역이 필요한 경우 원문과 연결 가능하게 유지

---

## 8. Expert / official material

전문 테스트와 공식 자료는
가능하면 원 데이터 또는 해당 source와 연결한다.

영상에서는 핵심만 보여주되,
프로젝트 데이터에는 원 출처를 보존한다.

---

## 9. Product image treatment

제품 이미지는 category theme 안에서 보여주되,
제품 고유 색을 억지로 theme color로 바꾸지 않는다.

가능:
- background removal
- subtle shadow
- neutral reflection
- scale / position animation

피함:
- 실제 제품 색 왜곡
- 기능이 있는 것처럼 보이는 합성
- 형태를 과도하게 변형
- 실제 재질과 다른 광택 효과

---

## 10. Human Asset Gate

Scene compiler가 asset requirement를 출력한다.

예:

```json
{
  "scene_id": "S12",
  "asset_requirement": {
    "role": "EVIDENCE",
    "preferred_type": "video",
    "subject": "robot vacuum passing under low furniture",
    "duration_hint": "2-4s",
    "source_priority": ["expert", "official", "user"]
  }
}
```

AI는 후보를 제시한다.

Human editor가 다음 중 하나를 결정한다:

```text
APPROVE
REPLACE
TRIM
CROP
SKIP
```

승인된 asset만 final render에 들어간다.

---

## 11. Automation boundary

자동화 목표:

```text
자료를 찾고
정리하고
후보를 좁히는 것
```

자동화하지 않는 핵심:

```text
무엇을 실제로 보여줄 것인지에 대한 최종 미감 판단
```

이 경계는 v1에서 의도적으로 유지한다.
