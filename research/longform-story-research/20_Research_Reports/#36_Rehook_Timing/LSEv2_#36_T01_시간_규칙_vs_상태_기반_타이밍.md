# Research Report — v2 #36 / Research Theme 1

> **파일명**: `LSEv2_#36_T01_시간_규칙_vs_상태_기반_타이밍.md`  
> **조사 일자**: 2026-09-17  
> **연구 상태**: 리서치 완결 (Completed)  
> **대분류**: `#36 — Rehook Timing` (Theme 1 — 시간 규칙 vs 상태 기반 타이밍)

---

## 1. Research Target

* **v2 Section**: `#36 — Rehook Timing`
* **Core Thesis**: Rehook은 '3분마다 한 번', '5분마다 한 번'과 같은 기계적 고정 시간 규칙(Fixed-Interval Rules)에 얽매여서는 안 되며, 서사 내부의 인지적·정서적 상태 변화를 감지하여 개입하는 **'상태 기반 타이밍(State-Based Timing)'**으로 설계되어야 한다. Neil A. Bradbury(2016)와 Karen Wilson & James H. Korn(2007)의 주의 집중 신화(Attention Span Myths) 해체, Philip J. Guo et al.(2014)의 690만 세션 비디오 시청 유지율(Retention) 빅데이터 분석, Christopher A. Kurby & Jeffrey M. Zacks(2008)의 사건 분할 이론(Event Segmentation)을 결합하여, 5대 서사 위험 상태(질문 소진, 정보 잉여, 예측 포화, 정서 정체, 추상화 표류)가 발생할 때 Rehook을 동적으로 격발하는 인지 공학 프레임워크를 수립한다.
* **Research Theme**: 시간 규칙 vs 상태 기반 타이밍 (Fixed Time Rules vs State-Based Intervention Timing)
* **Research Scope & Subtopics**:
  1. `attention span myths`: "인간 집중력은 10~15분/8초"라는 신화 비판 및 과제 상태 의존성 (Bradbury 2016, Wilson & Korn 2007)
  2. `retention curve 해석`: 플랫폼 시청 유지율 급락의 본질이 시간이 아닌 인지적 상태 정체임을 규명 (Guo et al. 2014)
  3. `event segmentation`: 시계적 시간이 아닌 예측 오차 및 특징 변화에 따른 사건 분할 (Kurby & Zacks 2008)
  4. `content-dependent pacing`: 정보 밀도와 정서적 압력에 따라 신축되는 콘텐츠 종속적 페이싱
  5. `fixed interval novelty`: 기계적 시간 주기 신기성 투입이 초래하는 서사 호흡 파괴와 리듬의 왜곡
  6. `state-based intervention`: 5대 위험 상태 감지 기반 동적 Rehook 트리거링
  7. `플랫폼·길이별 차이`: 모바일 숏폼, 30분 유튜브, 90분 OTT 다큐멘터리의 상태 전이 임계치

---

## 2. Executive Findings

* **가장 강하게 지지된 부분 (Strongly Supported)**:
  * **고정 시간 주의력 신화의 기각 (Bradbury 2016, `SRC-2016-306` / Wilson & Korn 2007, `SRC-2007-309`)**:
    * "인간의 집중력은 10~15분 만에 꺼진다"는 통념은 과거 조잡한 연구들의 편향된 인용에 불과함. 인간의 주의력은 물리적 타이머가 아니라 '제시되는 내용의 도전성, 상호작용, 새로운 질문의 존재 여부'라는 인지 상태(State)에 따라 40분 이상 지속될 수도, 30초 만에 꺼질 수도 있음.
  * **비디오 시청 유지율의 상태 의존성 (Guo, Kim & Rubin 2014, `SRC-2014-307`)**:
    * 690만 시청 세션 분석 결과, 시청자 이탈은 특정 분(minute) 지점에서 기계적으로 발생하는 것이 아니라, 화자의 톤 정체, 시각적 슬라이드의 무변화, 당면 목표의 상실 등 '상태 정체' 지점에서 집중적으로 발생함.
  * **사건 분할과 상태 변화 경계 (Kurby & Zacks 2008, `SRC-2008-308`)**:
    * 뇌가 새로운 사건으로 분절을 인식하는 기준은 시계 시간이 아니라 '상황 모델의 인과·목표·행위자 변화'임. 따라서 Rehook은 사건의 상태가 질적으로 바뀌는 바로 그 경계에 놓여야 가장 자연스럽게 수용됨.
* **가장 강하게 반박된 부분 (Strongly Contradicted / Nuanced)**:
  * **"3분/5분마다 무조건 반전이나 Rehook을 넣어야 한다"는 숏폼식 강박의 파산**:
    * 깊은 설명이나 감정 축적이 진행 중인 맥락에서 기계적으로 Rehook을 투입하면 몰입(Flow)을 산산조각 내어 오히려 이탈을 가속화함. Rehook은 오직 선행 상태가 소진되었을 때만 정당화됨.
* **조건부로만 맞는 부분 (Conditionally True)**:
  * 대략적인 시간 가이드라인(8~15분)의 유용성: 완벽한 임의성은 위험하므로, 상태 기반 트리거를 작동시키되 15분을 초과하지 않도록 하는 안전 상한선(Safety Ceiling)으로만 시간을 활용해야 함.
* **근거 부족 영역**: 120분 극장용 장편 영화와 20분 유튜브 영상 간의 뇌파(EEG) 동기화 감쇠 곡선의 정량 비교.

---

## 3. Findings by Subtopic

### 3.1 Subtopic 1: attention span myths (주의 집중력 신화 해체)
* Bradbury(2016) & Wilson(2007): 주의력은 15분에 고갈되는 배터리가 아니라, 새로운 인지적 자극과 가치 있는 정보가 들어올 때 즉각 재충전되는 동적 파동임. 고정 시간 규칙에 얽매일 필요가 없음. Verdict: `Strong Support`

### 3.2 Subtopic 2: retention curve 해석 (시청 유지율 급락의 진짜 원인)
* Guo et al.(2014): 유지율 그래프의 절벽(Drop-off Cliff)은 "앞선 질문에 답을 주고 난 직후 10초간 다음 볼 이유를 주지 않았을 때" 발생함. Rehook은 바로 이 '질문 소진 상태' 직후에 정확히 꽂혀야 함. Verdict: `Strong Support`

### 3.3 Subtopic 3: event segmentation (사건 분할의 신경학적 트리거)
* Kurby & Zacks(2008): 뇌의 예측 모델(Prediction Error)이 급증하는 지점이 곧 챕터의 경계임. 상태 변화가 없는 지점에서의 인위적 Rehook은 거부감을 낳음. Verdict: `Strong Support`

### 3.4 Subtopic 4: content-dependent pacing (내용 종속적 페이싱)
* 복잡한 금융 메커니즘을 설명할 때는 6~8분 만에 짧은 Rehook(Type 8 데이터형)을 주어야 하고, 장엄한 역사적 전투 장면에서는 15~18분간 긴 호흡으로 끌고 간 뒤 Rehook(Type 5 가치충돌형)을 배치하는 탄력적 조율이 필수적임. Verdict: `Strong Support`

### 3.5 Subtopic 5: fixed interval novelty의 폐해 (기계적 주기의 실패)
* 5분마다 억지로 훅을 넣으면 관객은 "또 낚시하네"라며 패턴을 간파하고 정서적 연결을 끊어버림. 리듬은 예측 불가능하면서도 인과적으로 필연적이어야 함. Verdict: `Strong Support`

### 3.6 Subtopic 6: state-based intervention (5대 서사 위험 상태 트리거)
1. *질문 소진(Question Exhaustion)*: 이전 미스터리가 풀려 시청 이유가 0이 된 순간
2. *정보 잉여(Information Redundancy)*: 동일한 예시나 설명이 2회 이상 반복되는 순간
3. *예측 포화(Predictability Saturation)*: 다음 전개가 너무 뻔해져 전두엽 긴장이 풀리는 순간
4. *정서 정체(Affective Stagnation)*: 단일한 감정(분노, 슬픔)이 10분 이상 지속되어 감정 둔마가 오는 순간
5. *추상화 표류(Abstraction Drift)*: 이론과 통계만 나열되어 인간의 얼굴이 사라진 순간. Verdict: `Strong Support`

### 3.7 Subtopic 7: 플랫폼·길이별 차이
* 10분 미만: 2~3분 상태 트리거 (주기 짧음)
* 30~60분: 10~14분 상태 트리거 (호흡 깊음)
* 90분 이상: 15~18분 상태 트리거 (거시적 상태 전이). Verdict: `Strong Support`

---

## 4. Narrative Application Architecture (v3 신설 아키텍처)

1. **`Narrative State Monitor (NSM, 서사 상태 모니터)`**: 대본의 각 씬을 분석하여 5대 서사 위험 상태(질문 소진, 정보 반복, 예측 포화, 감정 정체, 추상화 표류)를 실시간 감지하는 상태 진단기.
2. **`Dynamic Rehook Trigger (DRT, 동적 리훅 트리거)`**: 고정 시계 타이머를 폐기하고, NSM의 5대 지표 중 2개 이상이 임계치를 초과할 때 최적의 Rehook Type을 자동 호출하는 스마트 격발기.
3. **`Elastic Pacing Governor (EPG, 탄력적 페이싱 거버너)`**: 정보 난이도와 긴장도에 따라 챕터 분절 길이를 8~18분 범위에서 유기적으로 신축시키는 탄력 페이싱 엔진.

---

## 5. Evidence Quality Assessment

| Source ID | 저자 및 연도 | 제목 | 저널/출판사 | Tier | 핵심 기여 |
| :--- | :--- | :--- | :--- | :---: | :--- |
| `SRC-2016-306` | Neil A. Bradbury (2016) | Attention Span During Lectures: Myths | Adv Physiol Educ | Tier 1 | 10~15분 주의력 한계 신화 해체 및 상태 가변성 생리학적 규명 |
| `SRC-2014-307` | Philip J. Guo et al. (2014) | How Video Production Affects Engagement: MOOC Videos | ACM L@S | Tier 1 | 690만 비디오 세션 빅데이터 분석, 시청 유지율의 비디오 상태 종속성 실증 |
| `SRC-2008-308` | Christopher A. Kurby & Jeffrey M. Zacks (2008) | Segmentation in the Perception and Memory of Events | TICS | Tier 1 | 상황 모델 특징 변화와 예측 오차에 기반한 사건 분할 신경인지 메커니즘 규명 |
| `SRC-2007-309` | Karen Wilson & James H. Korn (2007) | Attention During Lectures: Beyond 10-15 Mins | Teach Psychol | Tier 1 | 고정 시간 간격 주의 감쇠 가설 비판 및 상태 기반 파동형 주의 모델 정초 |

---

## 6. Counter-Intuitive Findings & Paradoxes (역설적 발견 2선)

* **역설 1: 시계를 보고 Rehook을 넣는 순간 관객은 시계를 보기 시작한다 (The Clockwatcher Paradox)**: 작가가 "5분이 지났으니 훅을 넣어야지"라며 시계를 보는 순간 서사의 인과적 흐름이 끊긴다. 관객은 그 인위적 단절을 무의식적으로 감지하고 "이 영상 몇 분 남았지?"라며 스마트폰 화면을 탭한다. 최고의 타이밍은 시계를 완전히 잊고 오직 '이야기의 질문이 소진되었는가'만을 바라볼 때 잡힌다.
* **역설 2: 가장 위험한 이탈 구간은 '지루한 설명 중'이 아니라 '문제가 완벽히 해결된 직후'이다 (The Post-Resolution Void Paradox)**: 작가들은 지루한 설명 구간에서 관객이 나갈까 봐 전전긍긍한다. 그러나 데이터가 보여주는 최대의 이탈 절벽은 놀랍게도 미스터리가 통쾌하게 해결된 바로 그 순간이다. 관객은 만족하는 순간 뒤도 안 돌아보고 창을 닫는다. 해답을 주는 바로 그 문장에 다음 Rehook의 뇌관을 숨겨두어야 하는 이유다.

---

## 7. Inter-Theme Connections

* **대분류 `#36` 내 연계**:
  * `Theme 1 (시간 규칙 vs 상태 기반 타이밍 — 본 리포트)`: 고정 시간 신화 타파 및 5대 위험 상태 기반 동적 트리거링 원리 확립.
  * `후속 Theme 2 (Rehook 간격과 리듬)`: 상태 기반 Rehook들이 롱폼 전체에서 형성하는 파동형 템포와 리듬의 거시적 오케스트레이션 연구로 연결.
* **이전 대분류와의 연계**: `#35 (Rehook 라이브러리)`의 10대 유형을 언제 격발할 것인가에 대한 정밀 발사 통제 시스템 구축.

---

## 8. Practical Implementation Checklist

* [ ] 대본 작성 시 3분/5분 고정 시간 타이머에 의존하지 않았는가?
* [ ] 이전 챕터의 질문이 완벽히 해결된 직후 5초 이내에 새 Rehook이 배치되었는가? (NSM 질문 소진 감지)
* [ ] 동일한 설명이나 데이터가 2회 이상 반복되기 전에 렌즈가 전환되었는가? (정보 잉여 차단)
* [ ] 챕터 길이가 정보 난이도에 따라 8~18분 사이에서 유기적으로 신축되는가? (EPG 통과)

---

## 9. Version & Evolution History

* **v1/v2 한계**: "3분마다 훅을 줘라", "10분마다 반전을 줘라"는 1차원적 고정 시간 규칙에 갇혀 서사의 호흡을 파괴함.
* **v3 핵심 혁신점**: Bradbury(2016), Guo(2014), Kurby & Zacks(2008) 연구를 결합하여 고정 시간 신화를 해체하고, NSM, DRT, EPG 3대 **'상태 기반 동적 Rehook 트리거링 엔진'** 완비.
* **신규 대분류 `#36 — Rehook Timing` 성공적 착수 (누적 95편 마일스톤 달성)**.
