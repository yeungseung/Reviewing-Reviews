# R03 — Context-of-Use / Usability Evaluation Report

조사일: 2026-09-18 (KST)

범위: 제품 리뷰·전문가 테스트·사용자 경험 Claim이 **어떤 사용자, 목표·과업, 자원, 환경 및 시간적 조건에서 성립하는가**를 외부 HCI/usability/ergonomics와 context-aware computing의 개념으로 조사했다. 이 문서는 REVIEW²의 Architecture, Schema, Conflict rule, test protocol을 설계하거나 확정하지 않는다. R04 Professional Product Testing은 시작하지 않았다.

표기 규칙: **SOURCE FACT**는 source가 실제 정의·명시한 구조다. **RESEARCH INTERPRETATION**은 source 사이의 비교다. **REVIEW² APPLICATION HYPOTHESIS**는 후속 requirements 검토를 위한 가설일 뿐 채택 결정이 아니다. 모든 근거의 locator·한계는 [evidence.jsonl](evidence.jsonl), source provenance와 접근 제한은 [SOURCES.md](SOURCES.md)에 있다.

## 1. 분야 정의

**SOURCE FACT.** ISO 9241-11:2018은 Context-of-Use를 users, goals and tasks, resources, environment의 조합으로 정의하며 environment에는 technical, physical, social, cultural, organizational environment가 포함된다고 한다. Usability는 지정된 user가 지정된 context에서 goal을 달성하는 결과로 정의된다. [R03-E002, R03-E005] ISO/IEC 25063:2014는 이 Context-of-Use를 high-level 또는 detailed description으로 문서화하는 CIF로서 user/stakeholder group, user-group characteristic, goal, task, environment의 내용을 다룬다. [R03-E007, R03-E009]

**RESEARCH INTERPRETATION.** 이 분야에서 Context는 단순 “사용자 환경” 목록이 아니라, 어떤 결과·경험·평가가 적용되는 상황을 이루는 관계적 조합이다. 따라서 “야간에 AF가 느리다”의 야간, “게임할 때 팬이 시끄럽다”의 gaming, “하루 종일”의 duration은 같은 종류의 값으로 단순 합칠 수 없다.

**REVIEW² APPLICATION HYPOTHESIS.** Claim 비교 전에 Claim의 대상과 평가 표현뿐 아니라, 명시된 Context-of-Use가 결과의 적용 범위를 바꾸는지 확인할 가치가 있다. 이 가설은 Context object나 schema를 채택하라는 뜻이 아니다.

## 2. 이 분야가 해결하려는 문제

**SOURCE FACT.** ISO/IEC 25019:2023은 quality-in-use가 specified context of use의 전제 위에 있고, 제품·서비스가 충족하려는 context가 바뀌면 그 전제를 다시 명세해야 한다고 한다. [R03-E010] Maguire는 usability design/evaluation 전에 user-community goal과 user/task/environment characteristic을 이해해야 한다고 설명한다. [R03-E012]

**RESEARCH INTERPRETATION.** 이 분야는 “제품이 일반적으로 좋다/나쁘다”를 판정하는 대신, 어떤 조건 조합에서 어떤 사용 결과가 관찰·경험되었는지를 분명히 해 결과를 과도하게 일반화하지 않는 문제를 다룬다. 동일 제품에 대한 상반된 문장이 있어도 조건이 다르면 바로 모순이라고 할 수 없다.

## 3. 대표 표준 / 프레임워크 / 연구 계보

| 계보 | SOURCE FACT로 확인한 역할 | R03에서의 제한적 의미 |
| --- | --- | --- |
| ISO 9241-11:2018 | Context-of-Use, user, goal, task, usability의 현행 기본 정의. 산업·소비자 제품과 서비스까지 적용 범위를 둔다. [R03-E001–E005] | R03의 기본 경계다. 상세 field checklist나 Claim conflict rule은 아니다. |
| ISO 9241-210:2019 | human-centred design life-cycle 원칙과 활동의 current framework. [R03-E006] | Context 이해가 design/evaluation과 연결되는 계보를 보여 준다. |
| ISO/IEC 25063:2014 CIF | context description의 content element와 purpose를 다룬다. 현재 published이나 revision 중이다. [R03-E007–E009] | 실제 documentation structure 사례다. 공개 범위를 넘어 상세 checklist를 추측하지 않는다. |
| ISO/IEC 25019:2023 | 현재 quality-in-use model이며 quality-in-use의 context prerequisite를 명시한다. [R03-E010] | context 변화가 평가 적용 범위를 바꾼다는 근거다. |
| NISTIR 7432 CISU-R | context of use, performance/satisfaction criteria, test method/test context를 별도 정보로 둔다. [R03-E011] | R03 Usage Context와 R04 측정·시험 조건을 섞지 않는 근거다. |
| HCI context-of-use analysis (Maguire; Alonso-Ríos et al.) | user, task, environment 중심 분석과 더 자세한 taxonomy proposal을 제시한다. [R03-E012–E014] | 상세화 필요성과 taxonomy 간 차이를 보여 주지만 canonical inventory는 아니다. |
| Context-aware computing (Dey; Dey–Salber–Abowd) | entity-relative context, identity/location/status-or-activity/time, interpreter·situation·ambiguity를 다룬다. [R03-E015–E020] | context abstraction, derived context, uncertainty의 비교 기준이다. 모바일/센서 구조를 리뷰에 그대로 이식하지 않는다. |
| W3C PROV | entity, activity, agent 및 derivation/attribution provenance를 제공한다. [R03-E021, R03-E023] | inferred condition의 유래를 원문 사실과 분리해 남기는 비교 재료일 뿐 Context taxonomy가 아니다. |

## 4. 핵심 Entity

| Entity 또는 층 | SOURCE FACT | R03 구분 |
| --- | --- | --- |
| User | system/product/service와 상호작용하는 사람이며 operator, output user, support/training user까지 포함할 수 있다. [R03-E003] | **누가 사용했는가**다. R02 `opinion_holder`와 같은 정의가 아니다. |
| User group / characteristic | usability에 영향을 주는 user, task, environment characteristic으로 구분된 intended-user subset; CIF는 user-group characteristic을 별도 정보로 든다. [R03-E003, R03-E007] | User identity와 result-relevant characteristic을 분리해 생각할 근거다. |
| Goal | intended outcome. [R03-E004] | 달성하려는 결과이며 Task가 아니다. |
| Task | goal 달성을 위해 수행하는 physical/perceptual/cognitive activity 집합이며 goal의 수단을 묘사한다. [R03-E004] | Task와 Activity를 자동 동치로 두지 않는다. ISO는 activity를 task의 구성으로 둔다. |
| Resource / equipment | ISO 9241-11의 resource, ISO/IEC 25063의 equipment(hardware/software/materials) 및 technical/technological environment. [R03-E002, R03-E008] | companion phone, OS, app, network, lens, accessory 등이 사용을 지원하는 경우의 비교 기준이다. Variant와 같은 뜻은 아니다. |
| Environment | technical, physical, social, cultural, organizational environment. [R03-E002] | 단일 free-text “environment”로 섞지 않고 source의 dimension을 기록한다. |
| Temporal / location / status-or-activity context | context-aware framework의 identity/location/status-or-activity/time categories. [R03-E017] | ISO core set의 대체물이 아니다. 위치·시간·상태가 제품 경험에 관련될 수 있음을 보이는 별도 계보다. |
| Situation / derived context | relevant entity states를 묘사한 higher-level abstraction; one or more context inputs를 interpreter가 변환할 수 있다. [R03-E016, R03-E018] | 직접 진술/관측과 추론·aggregation을 동일 사실로 저장하지 않는 근거다. |

## 5. 핵심 Classification Dimensions

| Dimension | 외부 근거 | 경계 |
| --- | --- | --- |
| User와 user characteristic | user group은 user/task/environment characteristic으로 구분되고, proposed taxonomy는 role·knowledge/experience·physical characteristic을 별도 속성으로 둔다. [R03-E003, R03-E014] | `opinion_holder`는 말한/인용된 source이고, user characteristic은 결과의 적용 가능성에 관련된 특성일 수 있다. 둘을 합치지 않는다. |
| Goal / Task / Activity | goal은 outcome, task는 그 goal을 위한 activities 집합이다. [R03-E004] | Camera 예에서 “좋은 사진”과 “야간 인물 촬영”은 같은 층이라고 source가 말하지 않는다. “들고 이동하며 연속 촬영”을 별도 Activity로 둘지는 unresolved다. |
| Resource / technical environment | equipment는 hardware/software/materials이고 technical environment의 일부로 취급될 수 있다. [R03-E008] | companion equipment가 product identity, variant, dependency, usage resource 중 무엇인지는 source가 일반 규칙을 주지 않는다. |
| Physical / Social / Organizational environment | ISO는 environment 차원을 명시하고, National Research Council은 social collaboration 및 organizational environment를 performance constraint와 함께 둔다. [R03-E002, R03-E022] | 온도·조도·소음과 협업·정책·권한을 같은 subfield로 축약하지 않는다. |
| Temporal / duration / frequency / location | Context-aware computing에는 location/time가 있고, Alonso-Ríos taxonomy는 task duration/frequency를 별도 temporal characteristic으로 제안한다. [R03-E014, R03-E017] | `time of use`, `accumulated use`, `duration`, `frequency`, `lifecycle stage`의 universal mapping은 확인되지 않았다. |
| System state / product configuration | Dey 계보의 status/activity는 context-aware entity 상태이고, R01은 variant relation을 product identity 층에서 조사했다. [R03-E017; R01-E019] | battery 20%, firmware, performance mode, 256GB model을 모두 usage context라고 부를 근거는 없다. |
| Explicit / derived context | Dey framework는 sensed inputs를 higher-level context로 transform할 수 있고, PROV는 derivation trace 개념을 제공한다. [R03-E016, R03-E018, R03-E023] | 이 근거는 review prose에서 추론이 참임을 보증하지 않으며, R02 textual span/implicitness와 같지 않다. |

## 6. Entity 간 관계

**SOURCE FACT.** ISO 9241-11의 기본 관계는 `specified user — specified goal/task — resource/environment — usability outcome`이다. [R03-E002, R03-E005] ISO/IEC 25063은 user population, user/organization goal and responsibility, task, environment를 context description의 content element로 둔다. [R03-E009]

**RESEARCH INTERPRETATION.** 외부 구조가 보여 주는 최소 관계는 아래와 같다. 이는 REVIEW² schema가 아니다.

```text
User / user-group characteristic
          └─ uses → Product or service ─ supported by → Resource/equipment
          └─ pursues → Goal ─ realized through → Task (activities)
                                      └─ occurs in → Environment / temporal-location condition

이 조합이 → 경험·평가·측정 결과의 적용 범위를 제한할 수 있음
```

User의 characteristic은 user를 대체하지 않고, goal은 task의 outcome이며, task는 activity를 포함할 수 있다. Context-aware framework에서 entity의 state를 묶어 “situation”으로 추상화할 수 있지만, 그 abstraction이 R03의 표준 taxonomy라는 뜻은 아니다. [R03-E004, R03-E016]

## 7. Context / Condition 표현 방식

**SOURCE FACT.** ISO/IEC 25063은 context description을 별도 information item으로 다루며 particular layout을 강제하지 않는다. [R03-E009] Dey 계보는 entity-relative context를 collect/aggregate하고 interpreter가 higher-level context를 만들 수 있다고 한다. [R03-E015, R03-E018]

**RESEARCH INTERPRETATION.** 한 “condition”은 최소 세 층을 가리킬 수 있다.

1. **Context-of-Use**: user, goal/task, resource, environment, time/location처럼 평가의 적용 범위를 바꾸는 사용 상황.
2. **Product identity/configuration**: model, storage capacity, firmware, variant 같은 R01 대상 정렬 문제.
3. **Measurement/test condition**: metric, target value, method, protocol, test context처럼 결과를 만드는 평가 절차의 조건.

NISTIR 7432는 (1)과 performance/satisfaction criteria 및 (3)을 별도로 둔다. [R03-E011] 따라서 R03은 “어떤 조건이 결과의 적용 범위를 바꾸는가”까지만 조사한다. 조건을 어떻게 통제하고 측정해 재현 가능한 시험을 만들 것인지는 R04 범위이며 이번 조사에서 수행하지 않았다.

예를 들어 “배터리는 8시간 간다”에서 brightness, network, workload, temperature, battery health, procedure는 결과 해석에 관련될 수 있는 질문이지만, 이 조사는 그 목록을 universal R03 field로 채택하지 않는다. NIST 구조상 use context와 metric/criteria/test method는 분리되며, 어느 변수를 어떻게 통제·측정할지는 R04에서 다룰 시험 설계 문제다. [R03-E011]

**REVIEW² APPLICATION HYPOTHESIS.** 원문에 “야간”, “게임할 때”, “3시간 후”가 있으면 먼저 text-bound condition으로 보존하고, `night → low light`처럼 추가 맥락을 만들 필요가 있다면 source span·derivation·불확실성을 원문 사실과 별도로 검토할 필요가 있다. [R03-E018–E019, R03-E023]

## 8. 비교 가능성 / Conflict 처리

**SOURCE FACT.** Quality-in-use는 specified context를 전제로 하며, context가 바뀌면 전제를 다시 명세해야 한다. [R03-E010] Alonso-Ríos et al.은 한 context에서 얻은 usability result를 다른 context에 직접 일반화할 수 없다고 경고한다. [R03-E014]

**RESEARCH INTERPRETATION.** 조사한 standard/framework는 두 review Claim의 true conflict를 결정하는 일반 알고리즘을 제공하지 않았다. 다만 비교 전에 다음 상태를 구분할 외부 개념을 제공한다.

| 비교 상태 | R03에서 확인할 질문 | Conflict 판정 여부 |
| --- | --- | --- |
| same condition + different result | user/task/resource/environment/time이 실제로 같은가, 대상 identity/measurement method도 같은가 | 여전히 R03만으로 conflict 확정 불가 |
| different condition + different result | context 차이가 result applicability를 설명할 수 있는가 | 자동 conflict 아님 |
| partially overlapping condition | 공통·상이한 context dimension을 명시할 수 있는가 | additional evidence 필요 |
| unspecified condition | 사용 context가 원문에 없는가, inferred인지 | missing context를 임의로 채우지 않음 |
| incompatible context | product variant, market scope, test protocol 차이인가 | R01/R04와 함께 후속 검토 |

### R02에서 전달된 실제 문제에 대한 외부 개념 대조

아래는 final classification이 아니라, R03 source가 각 문장에 대해 **무엇을 보존하고 무엇을 추정하지 말라고 하는지** 시험한 결과다.

| 예시 | R03로 직접 설명 가능한 부분 | 이번 조사에서 확정하지 않는 부분 |
| --- | --- | --- |
| “야간에는 자동초점이 느리다” | `야간`은 원문에 명시된 condition-like expression이며, ISO physical environment와 관련될 가능성은 있다. [R03-E002] | `night`를 자동으로 `low light` 값으로 정규화하거나 AF slowdown의 원인을 확정하지 않는다. |
| “하루 종일 써도 손목이 안 아프다” | `하루 종일`은 duration candidate와 관련되고, 사용 결과/경험의 applicability condition일 수 있다. [R03-E014] | 손 크기·사용 자세·task를 문장에 없는데 만들어 내지 않으며, reviewer-holder와 user characteristic을 같은 것으로 두지 않는다. |
| “게임할 때는 팬 소음이 크다” | `게임할 때`는 task/activity 또는 workload-like condition의 surface expression일 수 있다. ISO는 task를 goal을 위한 activities set으로 둔다. [R03-E004] | 게임을 product-internal state, technical environment, test workload 중 하나로 확정하지 않는다. 팬 소음 property identity는 R01의 별도 문제다. |
| “256GB 모델만 발열이 심하다” | `256GB 모델`은 R01 product identity/variant alignment를 먼저 점검해야 한다. [R01-E019] | 저장용량 variant를 usage context라고 바꾸지 않으며, variant mismatch와 condition mismatch를 같은 비교 이유로 취급하지 않는다. |
| “3개월 지나니 배터리가 빨리 닳는다” | 경과 시간은 temporal context 후보와 관련될 수 있다. [R03-E017] | session duration, accumulated use, product lifecycle, degradation, battery health 중 무엇인지 source 없이 결정하지 않는다. measurement method·battery health는 R04 경계다. |

예를 들어 “이 노트북은 조용하다”와 “게임할 때는 매우 시끄럽다”에서 두 번째 문장은 `게임할 때`라는 사용 조건을 명시한다. 현행 외부 source는 이 두 문장을 같은 claim의 contradiction으로 label하지 않는다. [R03-E005, R03-E010]

## 9. Reliability / Uncertainty 처리

**SOURCE FACT.** Dey–Salber–Abowd는 sensed context가 실제 context와 다를 수 있음을 전제로 automatic/manual disambiguation 및 accuracy measure 전달을 논의한다. [R03-E019] PROV는 production에 관여한 entity/activity/agent 및 derivation을 기록해 quality, reliability, trustworthiness 판단을 지원하려는 framework다. [R03-E021, R03-E023]

**RESEARCH INTERPRETATION.** `Context confidence`는 최소 세 가지와 다르다: (a) reviewer/holder의 신뢰도, (b) product test의 measurement accuracy, (c) linguistic modality. R03 source는 이들을 하나의 점수로 합치는 근거를 제공하지 않는다.

**R03 limitation.** Dey의 accuracy는 sensed context의 quality이고, PROV의 derivation은 provenance 구조다. 둘 다 “클럽에서 찍었다”로부터 “low light”를 inference한 review NLP의 confidence policy를 정의하지 않는다. 이 정책은 unresolved로 남긴다.

## 10. 실제 데이터 구조 또는 필드 사례

| Source | 실제 structure 또는 field 사례 | R03에서 보존할 차이 |
| --- | --- | --- |
| ISO 9241-11 | users; goals/tasks; resources; technical/physical/social/cultural/organizational environment. [R03-E002] | core dimensions와 environment subdimensions |
| ISO/IEC 25063 | user population; user/organization goal and responsibility; user tasks; user environments; problems; high-level/detailed descriptions. [R03-E007, R03-E009] | description content와 layout non-prescription |
| NISTIR 7432 | context of use; performance/satisfaction criteria; test method and test context. [R03-E011] | usage applicability와 test/measurement procedure |
| Alonso-Ríos et al. | user role/experience/physical characteristic; task duration/frequency; physical/social/technical environment. [R03-E014] | detailed proposal과 universal standard의 차이 |
| Dey–Salber–Abowd | entity context attributes; identity/location/status-or-activity/time; coverage/resolution/accuracy/reliability/update frequency/timeliness for sensed context. [R03-E017, R03-E020] | situation metadata와 sensing-quality requirement의 차이 |
| W3C PROV | Entity, Activity, Agent, attribution, derivation. [R03-E021, R03-E023] | direct assertion과 derived assertion의 trace |

## 11. REVIEW²에 직접 참고 가능한 구조

아래는 채택 결정이 아니라, 서로 다른 high-priority source에서 반복되거나 명시된 구조다.

1. **Context-of-Use를 product property와 별도 층으로 보기**: user, goal/task, resource, environment은 ISO의 core combination이다. [R03-E002]
2. **User와 characteristic의 구분**: user group은 usability에 영향을 주는 characteristic으로 구분될 수 있다. [R03-E003, R03-E007]
3. **Goal과 Task의 비동치**: goal은 outcome이고 task는 means/activity set이다. [R03-E004]
4. **Environment의 다차원성**: technical, physical, social, organizational을 적어도 하나의 unqualified environment value로 축약하지 않을 근거가 있다. [R03-E002, R03-E022]
5. **Usage context와 test condition의 분리**: context-of-use, performance criteria, test method/context는 NIST method에서 별도다. [R03-E011]
6. **Context change는 applicability를 바꿀 수 있음**: quality-in-use의 prerequisite는 specified context다. [R03-E010]
7. **Derived context의 provenance 필요성**: context source를 aggregate/interpret하는 구조와 derivation trace 개념이 있다. [R03-E018, R03-E023]

## 12. 수정해서 참고해야 하는 구조

- **ISO/IEC 25063 CIF**: context description을 문서화하는 standard이지 review Claim tuple이 아니다. 또한 current revision 중이며 public preview 밖의 detail을 field로 전용하지 않는다. [R03-E007, R03-E009]
- **Alonso-Ríos taxonomy**: duration/frequency와 detailed user/environment attribute에 유용한 example을 주지만, 단일 paper의 taxonomy이므로 complete or canonical vocabulary로 가져오지 않는다. [R03-E013, R03-E014]
- **Dey context-aware framework**: identity/location/activity/time, sensor accuracy, interpreter는 application context를 위한 구조다. 사용 경험 review의 explicit span, holder, factual claim truth를 대신하지 않는다. [R03-E017–E020]
- **PROV**: derivation trace의 generic model이며 confidence scoring·review-context ontology가 아니다. [R03-E021, R03-E023]

## 13. 가져오면 안 되는 구조 / 한계

- **Context = all metadata**: product model/variant/market/configuration, textual discourse context, usage context, test condition을 하나의 `context`에 자동 통합하지 않는다. [R03-E008, R03-E011; R01-E014–E015, R01-E019; R02-E018–E022]
- **Context-aware categories = review taxonomy**: Dey의 identity/location/status/activity/time은 HCI context-aware application의 essential categories이지 consumer-product review의 exhaustive dimension이 아니다. [R03-E017]
- **Detailed taxonomy = standard**: Alonso-Ríos taxonomy는 proposal이며 source 자신도 detailed model 부족 문제에 응답한다. [R03-E013]
- **Different context = no conflict**: context difference는 automatic contradiction을 막는 comparison input일 수 있을 뿐, claim truth나 final conflict status를 결정하지 않는다. [R03-E005, R03-E010]
- **Derived condition = source fact**: sensed/inferred context에는 ambiguity·accuracy 문제가 있으며, review prose에 없는 condition을 사실로 저장할 근거는 없다. [R03-E016, R03-E019]
- **Test metadata = R03 deliverable**: control variable, measurement procedure, calibration, reproducibility 설계는 R04의 전문 제품 시험 경계다. [R03-E011]

## 14. Candidate Fields

모두 검토 후보이며 final schema가 아니다. 상태는 `strong_candidate`, `candidate`, `domain_specific`, `unclear`, `reject_candidate`만 쓴다.

| Candidate | 의미 | 외부 구조 / Evidence | 범위 | 상태 | 주의사항 |
| --- | --- | --- | --- | --- | --- |
| `user` | 실제 또는 intended user/role | ISO user [R03-E003] | 범용 | candidate | R02 `opinion_holder`와 동치가 아님 |
| `user_group` | characteristic/task/environment로 구분된 user subset | ISO user group, CIF [R03-E003, R03-E007] | 범용 | candidate | review author 집단과 자동 동일시 금지 |
| `user_characteristic` | result에 관련된 ability, experience, role 등의 특성 | CIF; Alonso-Ríos taxonomy [R03-E007, R03-E014] | 범용 | candidate | 모든 demographic을 수집할 근거가 아니며 relevance/provenance 필요 |
| `goal` | intended outcome | ISO [R03-E004] | 범용 | strong_candidate | product feature나 task label로 대체하지 않음 |
| `task` | goal을 위한 activities set/means | ISO [R03-E004] | 범용 | strong_candidate | source span과 broad activity label을 분리 검토 |
| `activity` | task constituent 또는 context-aware activity/status | ISO; Dey et al. [R03-E004, R03-E017] | 범용 | candidate | 독립 entity인지 task substructure인지는 unresolved |
| `resource_or_equipment` | use를 지원하는 hardware/software/materials/resource | ISO/IEC 25063; ISO 9241-11 [R03-E002, R03-E008] | 범용 | candidate | companion product, dependency, variant 중 어느 것인지는 별도 판단 |
| `environment_dimension` | physical/social/organizational/technical 등 dimension label | ISO [R03-E002] | 범용 | candidate | one free-text environment과 섞지 않음 |
| `physical_environment` | thermal/light/noise/location 등 physical condition | ISO; taxonomy proposal [R03-E002, R03-E014] | 범용 | candidate | “night”를 automatic low-light로 확대하지 않음 |
| `social_environment` | co-user, collaboration, public/private interaction condition | ISO; NRC [R03-E002, R03-E022] | 범용 | candidate | social fact와 holder attribution을 구분 |
| `organizational_environment` | policy, procedure, work arrangement, authority constraint | ISO; NRC [R03-E002, R03-E022] | work-domain | candidate | consumer review에 항상 applicable하지 않음 |
| `technical_environment` | supporting device, OS/app/network/materials constraints | ISO/IEC 25063; NRC [R03-E008, R03-E022] | 범용 | candidate | product-internal configuration과 자동 병합 금지 |
| `location` | relevant entity/place location | Dey et al. [R03-E017] | domain_specific | candidate | location privacy/precision policy는 R03 범위 밖 |
| `temporal_context` | time or temporal state of use | Dey et al. [R03-E017] | 범용 | candidate | duration/frequency/lifecycle의 umbrella field로 확정하지 않음 |
| `usage_duration` | task/session duration | Alonso-Ríos taxonomy [R03-E014] | 범용 | candidate | elapsed ownership/lifecycle duration과 구분 필요 |
| `usage_frequency` | repeated task/use frequency | Alonso-Ríos taxonomy; Dey sensing updates는 별개 [R03-E014, R03-E020] | 범용 | candidate | sensor update frequency와 같은 의미가 아님 |
| `system_state` | use 중 mode/battery/workload/state 후보 | Dey status/activity가 비교 단서 [R03-E017] | product-domain | unclear | operating state, product configuration, test setting을 구분하는 universal source rule not_found |
| `product_configuration` | firmware/setting/accessory/model-state 후보 | resource/environment source는 있으나 universal boundary 없음 | product-domain | unclear | R01 `variant_relation`과 병합·채택 금지 |
| `context_expression` | 원문에 쓴 condition-like span | R02 textual-context input; R03 source는 text span model을 주지 않음 [R02-E018–E022] | NLP-domain | unclear | Context-of-Use entity와 raw text span은 다름 |
| `context_explicitness` | explicit, observed, derived/inferred의 상태 후보 | Dey interpreter; PROV derivation [R03-E018, R03-E023] | NLP/domain | unclear | sensed/derived architecture를 review inference confidence로 전용하지 않음 |
| `context_derivation_reference` | derived condition의 input/activity trace 후보 | PROV [R03-E021, R03-E023] | cross-domain | candidate | confidence score나 truth label을 뜻하지 않음 |
| `applicability_context` | result가 적용되는 context combination 후보 | ISO quality-in-use prerequisite [R03-E005, R03-E010] | 범용 | candidate | final conflict/comparability algorithm이 아님 |

## 15. Unresolved Questions

1. **User versus opinion holder.** ISO user 정의와 R02 holder/source definition은 구별되지만, review author가 자신의 use experience를 말할 때 둘을 관계시키는 cross-domain standard rule은 확인하지 못했다.
2. **Goal / Task / Activity의 review-level representation.** ISO는 task를 activities set으로 정의하지만, camera review의 operation·activity·task를 몇 층으로 기록할 universal annotation model은 not_found다.
3. **Companion equipment boundary.** smartphone/OS/app/network/lens/accessory가 resource, technical environment, product dependency, bundle component, variant 중 어디인지 정하는 일반 rule은 확인하지 못했다.
4. **System state / configuration boundary.** battery %, performance mode, firmware, workload, thermal state를 Context-of-Use와 product configuration/test condition으로 나누는 primary usability standard rule은 not_found다.
5. **Duration versus lifecycle/degradation.** session duration, frequency, elapsed ownership, accumulated use, battery-health degradation을 하나의 temporal model로 연결하는 source는 이번 범위에서 확인하지 못했다.
6. **Physical/social/organizational granularity.** ISO는 environment dimensions를 주지만, review claim마다 어느 detail level까지 기록해야 comparison이 가능하면서 data explosion을 피하는지 정하지 않는다.
7. **Context-specific Claim conflict.** same condition/different result, partially overlapping condition, unspecified condition을 true contradiction으로 판정하는 general HCI/usability rule은 확인하지 못했다.
8. **Explicit/inferred review context.** Context-aware computing은 sensor/context interpretation을 다루지만, review text에서 inferred context의 evidence, alternative, confidence를 기록하는 common standard는 확인하지 못했다.
9. **Measurement condition boundary.** context-of-use와 test context가 구분된다는 근거는 있으나, product benchmark의 workload/calibration/test procedure를 어떤 R04 structure로 다룰지는 이번 R03에서 조사하지 않았다.
10. **Product category portability.** ISO framework는 broad하지만 cited detailed taxonomies는 interactive systems/usability studies 중심이다. appliance, camera, wearable, automobile review에 동일 granularity가 적합한지는 unresolved다.
11. **R01 product entity level relation.** family/model/generation/variant/unit과 user/task/environment context의 many-to-many relation을 표준적으로 맵핑하는 evidence는 없다.
12. **Provenance and privacy.** derived context의 traceability는 검토할 수 있으나, user characteristic/location의 disclosure, minimization, retention rule은 조사 범위 밖이다.

## 16. Evidence Map

| 핵심 finding | Evidence |
| --- | --- |
| Context-of-Use core combination과 environment dimensions | R03-E001–E005 |
| Current HCD and quality-in-use standard lineage/status | R03-E001, R03-E006–E007, R03-E010 |
| Context description content, user characteristics, equipment/technical environment | R03-E007–E009 |
| Usage context와 performance criterion/test context 분리 | R03-E011 |
| User/task/environment context analysis와 detailed taxonomy proposal | R03-E012–E014 |
| Entity-relative context, situation, abstraction and granularity trade-off | R03-E015–E018 |
| Context ambiguity, accuracy and quality constraints | R03-E019–E020 |
| Social/organizational/technical system context | R03-E022 |
| Derived-context provenance와 reliability boundary | R03-E021, R03-E023 |

## 17. 주요 Sources

총 11개 Source와 23개 Evidence를 사용했다. 최고 우선 source는 ISO/IEC 표준(R03-S01–S04)이며, NIST 공공 methodology(R03-S05), peer-reviewed HCI 연구(R03-S06–S09), W3C provenance documentation(R03-S10), National Academies methodology(R03-S11)로 보강했다.

동일 origin을 중복 strength로 세지 않았다. ISO 9241 후속 문서에 재사용된 ISO 9241-11 정의, ISO/IEC 25063의 historical ISO 9241-11 definition, author-hosted original paper와 publisher/mirror는 provenance 관계를 [SOURCES.md](SOURCES.md)에 기록했다. ISO/IEC 25063/25019 full text의 access limitation과 ISO/IEC 25063의 pending revision도 별도로 남겼다.

## 18. Potential Conflict with Existing REVIEW²

R01은 product identity/property/value/variant/market/condition reference를 catalog·product representation 관점에서 조사했다. R02는 opinion target text, aspect/category, opinion expression, holder, polarity, textual/discourse context를 조사했다. R03은 user, goal/task, resource, environment, temporal/location condition이 use outcome의 applicability를 바꿀 수 있는 구조를 조사했다. 외부 source는 다음 동치를 보장하지 않는다.

- R02 `Opinion Holder` ≠ R03 `User` 또는 `User Characteristic`.
- R02 `Textual Context Span` ≠ R03 `Context-of-Use`.
- R01 `Variant Relation` / `Product Configuration` ≠ R03 `Usage Context`.
- R01 `Market Scope` ≠ R03 `Physical Environment`.
- R01 `Condition Reference`(catalog applicability/measurement reference) ≠ R03 user/task/environment context.
- R03 `Applicability Context` ≠ final REVIEW² Conflict status.
- R03 derived-context provenance ≠ review author credibility, source reliability, or test-method quality.

따라서 R01/R02 Candidate Field를 정답으로 간주하거나 R03 결과로 mapping을 확정하지 않는다. 기존 REVIEW² Architecture, Source, Evidence Packet, Claim 문서를 수정하지 않았고 schema도 생성하지 않았다.
