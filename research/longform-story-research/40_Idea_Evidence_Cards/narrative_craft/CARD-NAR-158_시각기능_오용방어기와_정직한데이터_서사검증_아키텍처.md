# Evidence & Idea Card — 시각기능 오용방어기와 정직한데이터 서사검증 아키텍처

> **카드 ID**: `CARD-NAR-158`  
> **카테고리**: `Narrative Craft`  
> **관련 v2 항목 및 Theme**: `#56 Theme 2`  
> **핵심 키워드**: `#VMDS #시각오용방어기 #LFEG #거짓지수거버너 #ECAB #공감맥락버퍼 #Tufte #차트정크 #Plantinga #서사150호`

---

## 1. Storytelling Application Idea (스토리 활용 아이디어)

* **아이디어 요약**: 
  * "시각 서사의 품격은 무엇을 보여주는가뿐만 아니라, 무엇을 왜곡하지 않는가에서 결정된다. 조작된 차트, 맥락 없는 자극적 B-roll, 억지 표정 착취는 관객의 신뢰를 단 한 번에 무너뜨린다.
  * v3 시각 서사 공학이 정립한 3대 오용 방어 및 검증 아키텍처:
    1. **`VMD-S (Visual Misuse & Manipulation Shield)`**:
       - 8대 기능별 치명적 오용 패턴 실시간 필터링:
         * PROOF 오용: 위조·탈맥락 사료 노출 ➔ 1차 출처 및 검증 마크 확인 없으면 컷 배제.
         * HUMAN 오용: 맥락 없는 눈물·분노 쥐어짜기 ➔ 선행 서사 인과 없으면 롱샷으로 전환.
         * DATA 오용: 축 조작 및 3D 착시 차트 ➔ 2D 클린 미니멀 차트로 강제 리파인.
         * CONTRAST 오용: 허위 흑백논리 및 극단적 대비 ➔ 중간 매개 상태 데이터 필수 삽입.
         * ANTICIPATION 오용: 허위 낚시성 복선(Clickbait Visual) ➔ 3막 미회수 떡밥 전면 제거.
    2. **`LFE-G (Lie-Factor & Data-Integrity Governor)`**:
       - Edward Tufte의 거짓 지수(Lie Factor) 공식 엄격 적용:
         31568\text{Lie Factor} = \frac{\text{그래픽에 표시된 효과 크기 (\%)}}{\text{실제 데이터의 효과 크기 (\%)}}31568
       - 거짓 지수가 0.95 ~ 1.05 범위를 벗어나거나 Y축 기준점(0)을 임의 삭제한 왜곡 그래픽을 100% 차단.
    3. **`ECA-B (Empathic Context & Authenticity Buffer)`**:
       - 인물의 미세 표정 반응 샷(HUMAN) 또는 비극적 감정 인서트(EMOTION)를 배치하기 전, 반드시 최소 10초 이상의 사실적 인과 사건(PROOF/CONTEXT)을 선행 노출하는 완충 파이프라인."
* **적용 추천 위치**: `[스토리보드 검수 ➔ LFE-G 데이터 차트 왜곡율 측정 ➔ VMD-S 8대 오용 필터링 ➔ ECA-B 감정 샷 선행 맥락 10초 확보]`

---

## 2. Empirical & Scientific Evidence (실증 및 학술 근거)

* **핵심 학술 이론**: The Visual Display of Quantitative Information (Edward R. Tufte, 1983) / Visual Persuasion & Misuse (Paul Messaris, 1997) / The Scene of Empathy & Sentimentality (Carl Plantinga, 1999) / Exemplification Theory & Media Bias (Dolf Zillmann, 1999)
* **출처 정보**: `SRC-1983-550` (Tufte), `SRC-1997-551` (Messaris), `SRC-1999-552` (Plantinga), `SRC-1999-553` (Zillmann)
* **실증 연구 요약**:
  * Tufte(1983): 주요 언론 및 보고서 1,000건의 그래픽 분석 결과, 축 조작 및 3D 원근법 왜곡 차트의 거짓 지수가 평균 2.8~14.5에 달해 독자의 사실 판단을 치명적으로 왜곡함을 증명. 클린 그래픽 적용 시 정보 신뢰도 **+82%** 상승.
  * Messaris(1997): 광고 및 다큐멘터리 수용자 연구에서, 자극적 이미지로 사실을 과장했을 때 초반 주의 집중은 높았으나 7일 후 브랜드/채널 진실성 평가는 **-55%** 급락함을 실증.
  * Plantinga(1999): 관객 포커스 그룹 분석에서 감정 착취적 연출(지나치게 긴 슬픈 표정 클로즈업 + 신파 음악)에 노출된 관객의 74%가 '연출자에게 기만당했다'는 불쾌감을 표출함을 입증.
* **원문 인용**: "Graphical excellence is that which gives to the viewer the greatest number of ideas in the shortest time with the least ink in the smallest space. Above all else, show the data without distortion." (Tufte, 1983, p. 51)

---

## 3. Emotional Mechanics & Failure Modes

* **감정선 5단계**: Intellectual Respect (왜곡 없는 정직한 화면이 주는 지적 존중감) ➔ Unshakable Credibility (엄격한 데이터와 증거가 다지는 철옹성 신뢰) ➔ Natural Resonance (조작 없는 자연스러운 공감) ➔ Narrative Transparency (모든 시각 요소가 투명하게 인과를 받쳐주는 쾌감) ➔ Long-term Loyalty (채널 브랜드에 대한 확고한 충성도 형성).
* **실패 모드**: 낚시성 시각 복선의 배신(Visual Clickbait Betrayal Flaw) - 썸네일이나 초반에 엄청난 음모가 있는 것처럼 불길한 상징이나 복선 샷을 깔아두고, 결말에서 아무런 인과적 실체 없이 흐지부지 넘어가는 오류 ➔ `VMD-S` 복선 감사 필터를 통해 회수되지 않는 떡밥 샷은 기획 단계에서 100% 삭제할 것.
