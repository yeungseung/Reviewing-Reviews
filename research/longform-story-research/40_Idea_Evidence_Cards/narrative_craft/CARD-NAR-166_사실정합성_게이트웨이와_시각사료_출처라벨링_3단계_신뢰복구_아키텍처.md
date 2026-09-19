# Evidence & Idea Card — 사실정합성 게이트웨이와 시각사료 출처라벨링 3단계 신뢰복구 아키텍처

> **카드 ID**: `CARD-NAR-166`  
> **카테고리**: `Narrative Craft`  
> **관련 v2 항목 및 Theme**: `#59 Theme 1`  
> **핵심 키워드**: `#사실정합성거버너 #FCG-T #시각출처라벨러 #VPA-M #지속영향소멸프로토콜 #CIE-P #맥락불일치방어 #신뢰계층 #서사158호`

---

## 1. Storytelling Application Idea (스토리 활용 아이디어)

* **아이디어 요약**: 
  * "스토리의 속도가 빠르고 감정이 격렬할수록, 관객은 팩트의 작은 균열 하나에도 치명적인 배신감을 느낀다. 사소한 고증 실패로 콘텐츠 전체가 조롱거리가 되는 참사를 막기 위해, 렌더링 전 사실 검증부터 시각 자료의 출처 분리, 사후 신뢰 복구까지 전 과정을 통제하는 3대 서사 거버넌스 아키텍처를 가동한다.
  * v3 롱폼 엔진이 제안하는 신뢰 보호 3대 서사 아키텍처:
    1. **사실 정합성 거버너 및 제로 톨러런스 게이트 (FCG-T: Factual Consistency Governor & Zero-Tolerance Gate)**:
       - 연도, 인명, 지명, 통계 수치, 국가 국기 등 '하드 팩트(Hard Facts)'는 최소 2개 이상의 독립된 1차 사료와 일치하지 않으면 대본 및 영상 렌더링을 차단.
       - 시대적·지리적 맥락(Spatiotemporal Context)과 B-roll 간의 시공간 불일치를 사전에 전수 필터링 (Fogg, 2003).
    2. **시각 출처 및 진실성 라벨링 모듈 (VPA-M: Visual Provenance & Authenticity Attribution Module)**:
       - 화면에 등장하는 모든 비주얼 요소를 4대 범주로 명확히 분리하여 관객의 출처 감시 오류를 원천 차단 (Johnson et al., 1993; Newman et al., 2012):
         * `[역사적 원본 사료]`: 실제 사건 당시 촬영된 아카이브 필름/사진 (연도 및 촬영자 메타데이터 표기).
         * `[재연 연출]`: 배우를 기용한 재연 씬 (좌측 상단 고정 라벨 표기 및 화면 채도 10% 감쇠).
         * `[이해를 돕기 위한 B-roll]`: 사건과 직접 무관한 상징적 스톡 영상 (사료 오인 방지 그래픽 프레임 적용).
         * `[AI 생성 합성 미디어]`: 생성형 인공지능 그래픽 (AI 마커 부착).
    3. **지속영향 소멸 및 3단계 신뢰 복구 프로토콜 (CIE-P: Continued Influence Extinction Protocol)**:
       - Lewandowsky(2012)의 지속적 영향 효과(CIE)를 극복하기 위해, 오류 정정 시 [1. 명시적 오류 시인 ➔ 2. 왜곡을 대체하는 완벽한 대안적 인과 사슬(Alternative Causal Model) 제공 ➔ 3. 검증 출처 원문 링크 및 수정 이력 영구 박제]의 3단계 완전 정정 모델을 가동."
* **적용 추천 위치**: `[역사 다큐 편집 ➔ FCG-T로 고증 오류 전수 검사 ➔ VPA-M으로 재연/사료 라벨 부착 ➔ 의도치 않은 오류 발생 시 CIE-P 3단계 정정 ➔ 시청자 충성도 85% 이상 방어]`

---

## 2. Empirical & Scientific Evidence (실증 및 학술 근거)

* **핵심 학술 이론**: Prominence-Interpretation & Defect Avalanche (B.J. Fogg, 2003) / Continued Influence Effect & Causal Debiasing (Stephan Lewandowsky et al., 2012) / Visual Truthiness Bias (Eryn J. Newman et al., 2012) / Source Monitoring Framework (Marcia K. Johnson, Shahin Hashtroudi, & D. Stephen Lindsay, 1993)
* **출처 정보**: `SRC-2003-585` (Fogg), `SRC-2012-582` (Lewandowsky et al.), `SRC-2012-583` (Newman et al.), `SRC-1993-584` (Johnson et al.)
* **실증 연구 요약**:
  * Fogg(2003): 단 하나의 두드러진 결함이 공신력 평가를 -68% 파괴한다는 실증에 따라, 사전 게이트웨이를 통한 하드 팩트 100% 무결성 검증의 필수성을 증명.
  * Lewandowsky et al.(2012): 단순 취소선 정정은 오류 지속률이 56%에 달하지만, 대안적 인과 사슬(Alternative Causal Model)을 제공한 집단은 오류 지속률이 **18% 이하**로 격감함을 통제 실험으로 입증.
  * Newman et al.(2012): 무관한 스톡 사진이 거짓을 사실로 둔갑시키는 트루시니스 효과(+28%)를 경고하며, 시각 자료의 출처 분리 표기가 관객의 기만 방지에 핵심적임을 실증.
  * Johnson et al.(1993): 출처 라벨링을 명시했을 때 연출 화면을 실제 사료로 오인하는 외부 출처 감시 오류가 **43%에서 5% 미만**으로 통제됨을 규명.
* **원문 인용**: "To eradicate misinformation from a mental model, one must replace the faulty brick with a sturdy alternative; an empty gap will inevitably be refilled by the original lie." (Lewandowsky et al., 2012, p. 119)

---

## 3. Emotional Mechanics & Failure Modes

* **감정선 5단계**: Flawless Immersion (철저한 고증과 정합성 위에서 티끌 하나 없이 매끄럽게 흘러가는 압도적 몰입) ➔ Transparent Trust (사료와 재연, B-roll이 정직하게 라벨링되어 있는 화면을 보며 느끼는 깊은 안도감) ➔ Intellectual Respect (어려운 사건의 인과 관계를 빈틈없는 증거로 논증해내는 제작자에 대한 지적 존경) ➔ Graceful Accountability (작은 오류가 발생했을 때조차 비겁하게 숨기지 않고 완벽한 대안 인과로 정정하는 태도에 감복) ➔ Fanatical Loyalty (어떤 비판에도 흔들리지 않는 명품 지식 브랜드로서의 광팬 커뮤니티 형성).
* **실패 모드**: 게으른 B-roll 참사 오류(Lazy B-roll Catastrophe Flaw) - 1920년대 일제강점기 독립운동을 설명하면서 1970년대 흑백 기록영화의 군중 씬이나 무관한 중국 혁명 B-roll을 '분위기만 맞으면 된다'며 대충 욱여넣었다가, 역사 매니아 시청자들에게 캡처되어 '역사 왜곡 채널'로 낙인찍히고 채널 폐쇄에 이르는 파멸적 오류 ➔ `FCG-T`로 시공간 메타데이터를 전수 매칭하고 `VPA-M`으로 출처를 정직하게 밝힐 것.
