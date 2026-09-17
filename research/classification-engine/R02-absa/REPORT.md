# R02 — Aspect-Based Sentiment Analysis / Opinion Mining Report

## 연구 범위와 판독 규칙

이 보고서는 리뷰·전문가 평가·사용 경험 문장에서 **대상**, **aspect**, **의견 표현**, **sentiment**, **비교**, **표현상의 조건**을 어떤 단위로 구조화해 왔는지 조사한 결과다. 최종 REVIEW² Classification Architecture나 schema를 설계하거나 확정하지 않는다. R03의 사용자·활동·환경 Context-of-Use 연구도 수행하지 않는다.

표기 규칙은 다음과 같다.

- **SOURCE FACT**: source가 실제로 정의하거나 annotation한 구조다.
- **RESEARCH INTERPRETATION**: source들을 비교한 R02의 해석이다.
- **REVIEW² APPLICATION HYPOTHESIS**: 후속 requirement 검토에 쓸 수 있는 가설이며 채택 결정이 아니다.

R01의 product identity, property, variant, market/measurement condition 개념은 비교 입력으로만 사용했다. R01의 Candidate Field를 R02의 정답 또는 최종 field로 취급하지 않았다.

## 1. 분야 정의

**SOURCE FACT.** 초기 feature-based opinion mining은 product feature에 대해 언급된 opinion sentence와 그 orientation을 찾아 요약하는 문제로 제시되었다. [R02-E001] Liu의 정식화에서는 opinion target을 entity와 aspect의 쌍으로 세분할 수 있고, opinion은 entity/aspect, sentiment, holder, time을 포함하는 tuple로 나타낼 수 있다. [R02-E002] SemEval-2014는 전체 문장 polarity만으로는 모델의 서로 다른 aspect에 대한 상반된 평가나 객관 정보를 보존하지 못한다고 설명하며, entity의 aspect별 sentiment를 찾는 ABSA를 task로 삼았다. [R02-E007]

**RESEARCH INTERPRETATION.** R02에서 `Aspect-Based Sentiment Analysis (ABSA)`는 하나의 고정 data model이 아니라, (a) feature/aspect와 sentiment의 연결, (b) text span과 predefined category의 연결, (c) holder·target·expression 관계 graph, (d) target/aspect/opinion/sentiment joint extraction을 포함하는 연구 계열의 묶음이다. 따라서 “aspect”라는 단어만 같다고 같은 entity라고 가정할 수 없다.

## 2. 이 분야가 해결하려는 문제

**SOURCE FACT.** SemEval-2014의 예시는 한 laptop review가 성능에는 긍정, 가격에는 부정, CD slot에는 객관 정보를 동시에 가질 수 있음을 보인다. [R02-E007] Liu는 한 문장 전체에 하나의 holder·sentiment가 있다는 단순화가 여러 aspect와 상반된 평가가 섞인 문장에서 실패한다고 지적한다. [R02-E005] Comparative opinion mining은 공통 feature에 관해 둘 이상의 entity를 순서화하는 비교문과 그 relation을 별도 대상으로 정의한다. [R02-E017]

**RESEARCH INTERPRETATION.** 이 분야의 핵심 문제는 “긍정/부정 분류”가 아니라, 그 방향성이 **누가**, **무엇의 어느 측면에**, **어떤 표현으로**, **어느 비교 대상 및 언어적 한정 아래** 적용되는지를 복원하는 것이다. “배터리는 8시간 간다”, “배터리가 오래 간다”, “경쟁 제품보다 오래 간다”, “내 사용에서는 하루를 못 버틴다”는 polarity만으로는 서로 구별되지 않는다. 첫 문장은 수치·측정 claim일 수 있고, 둘째는 evaluative opinion, 셋째는 비교 relation, 넷째는 경험 및 condition을 포함한다. 이 구분 자체는 R02의 분석이며, 현행 ABSA benchmark의 공통 field라고 주장하지 않는다.

## 3. 대표 연구 / 프레임워크 / 연구 계보

| 연구 계보 | SOURCE FACT로 확인된 semantic unit | R02에서의 의미 |
| --- | --- | --- |
| Feature-based opinion mining (Hu & Liu) | product feature/aspect, opinion sentence, orientation; 후속 정식화의 entity–aspect–sentiment–holder–time tuple [R02-E001] [R02-E002] | aspect와 의견을 분리해 본 초기 구조다. |
| SemEval ABSA 2014/2016 | aspect term/category, entity–attribute category, target-expression span, polarity [R02-E007] [R02-E009] | text mention, controlled category, polarity가 서로 다른 slot이 될 수 있음을 보인다. |
| Contextual polarity / MPQA | subjective expression, source, target, entity/event target, contextual polarity [R02-E012] [R02-E013] | holder·target·표현을 ABSA보다 넓은 opinion annotation으로 분리한다. |
| Comparative opinion mining | compared entities, common aspect, preferred entity, comparison relation [R02-E006] [R02-E017] | 비교는 polarity label 하나가 아니라 relation 구조다. |
| ASTE / ASQP / ACOS | target–opinion span–sentiment triplet; category–aspect term–opinion term–sentiment quad; implicit aspect/opinion을 포함한 quad [R02-E014] [R02-E015] [R02-E016] | 최근 joint extraction은 opinion expression과 span relation을 명시적으로 복원한다. |
| Structured Sentiment Analysis (SemEval-2022) | holder, target, expression, polarity로 된 sentiment graph [R02-E011] | category 중심 ABSA와 달리 holder와 relation을 한 graph에 둔다. |
| Aspect hierarchy / review structure | review text에서 유도한 product-aspect hierarchy 또는 aspect–sentiment tree, 문장 간 discourse 관계 [R02-E020] [R02-E021] [R02-E022] | hierarchy는 존재하지만 대개 domain/model/data-driven이며 R01 product-property ontology와 동일하지 않다. |

## 4. 핵심 Entity

| Entity | SOURCE FACT | R02 구분 |
| --- | --- | --- |
| Entity | Liu는 product, service, person, event 등을 entity로 다루고, target을 entity와 aspect의 pair로 세분할 수 있다고 설명한다. [R02-E002] | 리뷰가 말하는 사물/서비스/사건의 의미 대상이다. |
| Opinion target / target expression | SemEval-2016의 OTE는 reviewed entity를 가리키는 **linguistic expression**이며 offset으로 기록되고, 명시 표현이 없으면 `null`이다. [R02-E009] | text span과 실제 product identity는 별개일 수 있다. |
| Aspect term | SemEval 계열은 text에서 언급된 aspect/term을 다룬다. [R02-E007] | 문장 표면의 대상 또는 그 일부를 가리키는 span이다. |
| Aspect category | SemEval-2016은 predefined inventory에서 entity `E`와 attribute `A` pair를 고른다. [R02-E009] | aspect term과 별개인 controlled category다. |
| Attribute / property | Liu는 entity의 part와 attribute를 hierarchy로 설명하되, 단순화한 두 level에서는 모두 aspect라고 부른다고 명시한다. [R02-E003] | source 용어상 `aspect`가 R01의 catalog property와 자동 동치가 아니다. |
| Opinion expression | ASTE는 target에 대한 이유가 되는 opinion span을, ASQP는 opinion term을 별도 element로 둔다. [R02-E014] [R02-E015] | “빠르다”, “너무 무겁다” 같은 평가 표현이다. |
| Holder / source | Liu의 opinion quintuple에는 holder가 있고, Structured Sentiment Analysis는 holder·target·expression·polarity를 함께 graph로 예측한다. [R02-E002] [R02-E011] | 작성자 경험, 인용된 제조사 주장, 제3자 견해를 같은 말로 합치지 않기 위한 출발점이다. |
| Comparison | comparative formulation은 두 entity, aspect, preferred entity 등을 포함한다. [R02-E006] | `더 좋다`의 방향과 기준 대상은 독립 정보다. |
| Contextual modifier | contextual polarity 연구는 negation, intensifier, diminisher, modality, word sense, syntactic context를 polarity 판정 조건으로 다룬다. [R02-E012] | 사용 환경 전체가 아니라 표현 해석에 가까운 문장 내/근접 문맥이다. |

## 5. 핵심 Classification Dimensions

**SOURCE FACT.** SemEval-2016 sentence-level tuple은 `(Aspect Category=E#A, OTE, Sentiment Polarity)`의 세 slot을 정의한다. [R02-E009] Structured Sentiment Analysis는 `(holder, target, expression, polarity)` opinion graph를 정의한다. [R02-E011] ASQP는 aspect category, aspect term, opinion term, sentiment의 quadruple을, ASTE는 target, sentiment, opinion span의 triplet을 joint extraction 대상으로 둔다. [R02-E014] [R02-E015]

| Dimension | 확인된 표기/구조 | 공통성 판정 |
| --- | --- | --- |
| 대상 referent | entity, target, eTarget, reviewed entity | 넓게 반복되나 text span·ontology entity의 범위가 다르다. |
| aspect | feature, aspect term, aspect category, entity#attribute | 반복되나 term/category/property 의미가 같지 않다. |
| opinion expression | opinion sentence, opinion span/term, expression | 현대 joint extraction과 structured sentiment에서 명시적이다. |
| direction | orientation, polarity, preferred entity | 평가 polarity와 비교 우선순위는 분리된다. |
| source | holder, source, nested source | 일부 corpus/structured task에 명시적이며 전통 SemEval ABSA slot에는 없다. |
| explicitness | explicit OTE, `null`, implicit aspect/opinion | 일부 task가 직접 모델링한다. [R02-E010] [R02-E016] |
| modifier | negation, intensity, modality, contextual polarity | phrase-level opinion mining에서 중요하나 공통 ABSA tuple slot은 아니다. [R02-E012] |
| relation | target–opinion, holder–target–expression, compared entity pair | structured extraction에서 핵심이다. |
| hierarchy | aspect hierarchy / aspect-sentiment tree | domain/model-specific이며 controlled standard가 아니다. [R02-E020] [R02-E021] |

## 6. Entity 간 관계

**SOURCE FACT.** 다음은 실제 연구에서 쓰인 서로 다른 relation 단위다.

| 구조 | source의 표현 | 주의점 |
| --- | --- | --- |
| Opinion quintuple | `(entity, aspect, sentiment, holder, time)` [R02-E002] | context를 포함하지 않는다고 source가 명시한다. [R02-E018] |
| SemEval-2016 tuple | `(E#A, OTE, polarity)` [R02-E009] | OTE는 `E`의 text expression이지 product identity key가 아니다. |
| Structured sentiment graph | `(holder, target, expression, polarity)` [R02-E011] | aspect category가 필수 node인 것은 아니다. |
| ASTE triplet | target, opinion span, sentiment [R02-E014] | holder·comparison·usage condition은 기본 element가 아니다. |
| ASQP quad | category, aspect term, opinion term, sentiment [R02-E015] | category와 term 둘 다 있으므로 one-to-one을 전제하지 않는다. |
| Comparative sextuple | `(E1, E2, A, preferred entity, holder, time)` [R02-E006] | 두 entity와 common aspect를 보존한다. |

**RESEARCH INTERPRETATION.** “카메라는 좋다”는 entity-level target과 broad opinion expression을 가질 수 있고, “자동초점은 빠르다”는 narrower aspect/target을 갖는다. “야간 촬영에서는 자동초점이 느리다”는 같은 aspect span에 condition-like qualifier가 추가된다. “이 모델보다 이전 세대가 더 빠르다”는 두 entity와 comparative relation이 필요하다. 위 차이는 여러 source의 tuple을 대조한 해석이지 단일 benchmark의 annotation rule이 아니다.

## 7. Context / Condition 표현 방식

**SOURCE FACT.** Liu는 opinion quintuple이 context를 포괄하지 못한다고 적고, “키 큰 사람에게 이 차는 너무 작다”에서 `키 큰 사람`을 context로 예시한다. [R02-E018] Wilson 등은 polarity가 negation, intensifier, modality, diminishers 및 syntactic context에 의해 변할 수 있음을 phrase-level로 다룬다. [R02-E012] Context-Guided BERT는 target-aspect sentiment에서 주변 textual context를 이용하지만, 그 논문이 R03 수준의 user/task/environment taxonomy를 정의하지는 않는다. [R02-E019] Ruder 등은 review의 문장들이 discourse relation으로 연결되어 문장 간 context가 sentiment 해석에 도움을 줄 수 있다고 모델링한다. [R02-E022]

**RESEARCH INTERPRETATION.** R02에서 확인한 `context`는 최소 세 가지를 섞어 부르는 위험이 있다: (1) negation·intensity·modality 같은 linguistic modifier, (2) 인접 문장/담화 문맥, (3) “야간”, “특정 앱”, “장시간”, “키 큰 사용자”처럼 평가가 성립하는 사용·상황 조건이다. 첫째와 둘째는 ABSA/structured sentiment에서 직접 다뤄졌고, 셋째는 Liu의 example처럼 필요성이 드러나지만 공통 benchmark slot으로 정착했다고 확인되지 않았다.

**R03 boundary.** R02는 문장에 실제로 표현된 context/qualifier span과 target·opinion의 relation을 기록할 필요성을 발견하는 데까지만 다룬다. User, Task, Activity, Physical/Social Environment, Equipment의 분해·정규화·granularity 관리는 R03에 남긴다. R01의 `condition`(property applicability, measurement/market scope 등 catalog-data 의미)과 여기의 경험/언어 조건도 같은 field라고 가정하지 않는다.

## 8. 비교 가능성 / Conflict 처리

**SOURCE FACT.** Comparative opinion은 둘 이상의 entity를 common feature에 대해 순서화하고 preferred entity를 찾는 별도 problem으로 정의된다. [R02-E006] [R02-E017] SemEval-2014는 한 review 안에서도 aspect별로 opposing sentiments와 objective information이 함께 있을 수 있음을 보인다. [R02-E007]

**RESEARCH INTERPRETATION.** 조사한 ABSA task는 polarity·tuple/graph 추출을 평가하지만, 서로 다른 review claim 두 개가 실제로 conflict인지 판정하는 일반 규칙을 제공하지 않는다. 동일 aspect label과 polarity 차이만으로 conflict를 선언할 수 없다. target referent, aspect granularity, holder, comparison basis, explicit modifier, textual/usage condition, observation/test scope가 다른지 먼저 보아야 한다.

**REVIEW² APPLICATION HYPOTHESIS.** 후속 requirement에서는 “비교 가능한가”와 “polarity가 다른가”를 분리해 검토할 가치가 있다. 이것은 candidate field 채택이나 conflict algorithm 결정이 아니다.

## 9. Reliability / Uncertainty 처리

**SOURCE FACT.** Contextual polarity annotation은 positive/negative뿐 아니라 neutral/both와 contextual modifier의 영향을 다루며, modality와 realis/irrealis도 고려 대상으로 든다. [R02-E012] MPQA 3.0은 source와 target span을 구분하고, 기존 review corpus target은 product/service aspect에 제한되는 경향 및 writer 이외 attribution의 누락을 지적한다. [R02-E013] SemEval-2016 polarity slot은 positive/negative/neutral label을 사용한다. [R02-E009]

**RESEARCH INTERPRETATION.** 이 source들은 표현의 polarity 해석과 attribution의 불확실성 문제를 보여 주지만, REVIEW²가 요구할 evidence reliability, test method quality, factual measurement confidence를 위한 공통 ABSA standard를 제공하지 않는다. “seems”, “probably”, “usually”, “sometimes”의 문법·modal 정보와 source reliability는 다른 층이다.

**REVIEW² APPLICATION HYPOTHESIS.** modality/certainty cue와 evidence reliability를 하나의 점수로 합치지 않고 별도 검토 대상으로 둘 필요가 있을 수 있다. 이 가설은 source reliability field의 확정이 아니다.

## 10. 실제 데이터 구조 또는 필드 사례

| Source/model | 실제 unit 또는 slot | R02가 보존해야 할 차이 |
| --- | --- | --- |
| SemEval-2014 | aspect별 sentiment; overall과 aspect level을 구분 [R02-E007] | overall review label ≠ aspect evaluation |
| SemEval-2016 | `E#A`, OTE character offsets/`null`, polarity [R02-E009] [R02-E010] | controlled category ≠ surface mention; explicitness도 별도다. |
| MPQA 3.0 | source, attitude/ESE span, entity/event eTarget [R02-E013] | target은 product feature에 한정되지 않을 수 있다. |
| SemEval-2022 SSA | holder, target, expression, polarity sentiment graph [R02-E011] | holder–target–expression relation을 tuple 단위로 묶는다. |
| ASTE | target, opinion span, sentiment triplet [R02-E014] | aspect word와 evaluation word의 연결을 보존한다. |
| ASQP | aspect category, aspect term, opinion term, sentiment quad [R02-E015] | category/term/opinion expression을 분리한다. |
| ACOS | all aspect-category–opinion–sentiment quads, implicit aspect/opinion 포함 [R02-E016] | 명시/암시 여부를 별도 문제로 만든다. |
| Comparative formulation | `E1`, `E2`, common `A`, preferred entity, holder, time [R02-E006] | comparative direction과 basis는 simple polarity가 아니다. |

## 11. REVIEW²에 직접 참고 가능한 구조

아래는 **구조의 존재**를 참고할 수 있다는 뜻이며 채택 결정이 아니다.

1. **표면 mention과 controlled category의 분리**: SemEval-2016의 OTE와 `E#A` 분리는 text span과 category를 다른 slot으로 둔다. [R02-E009]
2. **opinion expression과 target의 relation**: ASTE/ASQP/SSA는 평가 표현을 target 또는 aspect와 연결한다. [R02-E011] [R02-E014] [R02-E015]
3. **holder/source의 명시성**: Liu quintuple, MPQA, SSA는 누가 의견을 냈는지를 의미 단위로 보존한다. [R02-E002] [R02-E011] [R02-E013]
4. **comparative relation의 독립성**: 비교 대상, common basis, preferred direction은 polarity로 축약되지 않는다. [R02-E006] [R02-E017]
5. **explicit/implicit의 구분**: explicit OTE `null`과 ACOS의 implicit aspect/opinion은 “text에 없는 aspect”를 억지 span으로 만들지 않는 방법을 보인다. [R02-E010] [R02-E016]

## 12. 수정해서 참고해야 하는 구조

1. **Aspect ↔ R01 property 연결**: Liu는 part와 attribute를 단순화해 모두 aspect라고 부를 수 있다고 하므로, ABSA aspect를 product ontology property ID에 곧바로 대응시키면 안 된다. [R02-E003]
2. **Target ↔ product entity identity 연결**: SemEval OTE는 character-offset mention이고, MPQA eTarget은 entity/event general target이다. 어느 쪽도 family/model/generation/variant/individual-unit taxonomy를 제공하지 않는다. [R02-E009] [R02-E013]
3. **Context**: linguistic modifier·discourse context·usage condition을 단일 `context`로 합치지 말아야 한다. R03의 context-of-use 분해를 기다려야 한다. [R02-E012] [R02-E018] [R02-E022]
4. **Hierarchy**: product aspect hierarchy 또는 aspect-sentiment tree는 실제 연구 구조이나, data-driven/domain-specific model로서 R01의 안정된 product-property hierarchy와 같은 것으로 가져오면 안 된다. [R02-E020] [R02-E021]
5. **Recommendation/preference**: recommendation 연구는 user-attention과 item-property를 aspect-sentiment pair로 다루지만, 이를 일반 ABSA opinion tuple의 필수 slot으로 제시하지 않는다. [R02-E023]

## 13. 가져오면 안 되는 구조 / 한계

- **polarity = Claim**: SemEval-2014의 objective information과 mixed aspect sentiment 사례는 polarity가 factual measurement, evaluation, comparison, recommendation을 모두 대체하지 못함을 보인다. [R02-E007]
- **문장당 하나의 평가**: 여러 aspect/상반 polarity/holder가 있을 수 있어 sentence-level aggregation은 손실을 낸다. [R02-E005] [R02-E013]
- **aspect term = catalog property**: aspect는 text term, predefined category, hierarchy node 등 서로 다른 의미로 쓰인다. [R02-E003] [R02-E009]
- **동일 aspect의 polarity 차이 = conflict**: 비교 대상·holder·modifier·조건이 다른 경우를 task label만으로 conflict로 판정할 근거를 찾지 못했다.
- **data-driven hierarchy = universal ontology**: Yu와 Kim의 hierarchy는 review/domain data에서 생성·발견하는 방법이다. 표준 product vocabulary 또는 canonical hierarchy로 확인되지 않았다. [R02-E020] [R02-E021]
- **ABSA tuple = evidence quality model**: 조사한 annotation/task는 source credibility나 professional test methodology의 reliability를 일반적으로 model하지 않는다. [R02-E009] [R02-E011]

## 14. Candidate Fields

아래는 외부 구조에 근거한 검토 후보일 뿐 최종 schema가 아니다. 이름도 추후 requirement 단계에서 바뀔 수 있다.

| Candidate | 의미 | 외부 근거 | 범위 | 상태 | 주의사항 |
| --- | --- | --- | --- | --- | --- |
| `opinion_target_text` | 대상의 surface span 또는 mention | OTE, eTarget, target [R02-E009] [R02-E013] | 범용 | strong_candidate | text span이지 product ID가 아니다. |
| `target_entity_kind` | target이 entity/event/product-aspect 등 어떤 semantic kind인지 | MPQA eTarget, Liu entity [R02-E002] [R02-E013] | 범용 | candidate | product class/model/variant taxonomy는 제공하지 않는다. |
| `aspect_term` | text에 나타난 aspect 표현 | SemEval, ASQP [R02-E007] [R02-E015] | 범용 | strong_candidate | label/property ID와 분리한다. |
| `aspect_category` | controlled entity–attribute 또는 category | SemEval-2016, ASQP [R02-E009] [R02-E015] | domain-specific | candidate | domain inventory 의존성이 높다. |
| `opinion_expression` | 평가를 나타내는 span/term | SSA, ASTE, ASQP [R02-E011] [R02-E014] [R02-E015] | 범용 | strong_candidate | factual value span과 같지 않을 수 있다. |
| `polarity` | expression/target 관계의 방향 label | SemEval, SSA [R02-E009] [R02-E011] | 범용 | strong_candidate | claim truth나 recommendation을 대신하지 않는다. |
| `opinion_holder` | opinion을 낸 사람/조직/attributed source | Liu, MPQA, SSA [R02-E002] [R02-E011] [R02-E013] | 범용 | candidate | writer·quoted manufacturer·third party 구분의 상세 모델은 추가 연구가 필요하다. |
| `target_aspect_relation` | target과 aspect/category의 연결 | Liu, SemEval-2016 [R02-E002] [R02-E009] | 범용 | candidate | category와 surface term은 many-to-many일 수 있다. |
| `explicit_or_implicit` | target/aspect/opinion이 명시됐는지 | OTE `null`, ACOS [R02-E010] [R02-E016] | 범용 | candidate | implicit inference의 confidence/근거는 별도 문제다. |
| `comparison_relation` | 비교임 및 relation type | comparative mining [R02-E006] [R02-E017] | 범용 | candidate | non-comparative polarity와 섞지 않는다. |
| `comparison_target` | 비교 대상 entity/mention | comparative sextuple [R02-E006] | 범용 | candidate | referent resolution 및 entity level은 별도다. |
| `comparison_basis` | 공통 aspect/property/criterion | comparative common aspect [R02-E006] [R02-E017] | 범용 | candidate | price/value-for-money처럼 복합 기준일 수 있다. |
| `preferred_entity` | 비교에서 우선되는 entity | comparative formulation [R02-E006] | 범용 | candidate | recommendation 또는 purchase decision과 동치가 아니다. |
| `polarity_modifier` | negation/intensity/diminisher 같은 해석 modifier | contextual polarity [R02-E012] | 범용 | candidate | modifier 범위(scope) 판정이 필요하다. |
| `modality_or_certainty_cue` | probably/seems/may 등 표현의 modality | contextual polarity/MPQA tradition [R02-E012] | 범용 | candidate | evidence reliability score와 결합하지 않는다. |
| `textual_context_span` | 인접 문장/표현 내 condition-like qualifier | contextual polarity, discourse context [R02-E012] [R02-E022] | 범용 | unclear | R03 usage context taxonomy와 혼합 금지. |
| `product_entity_reference_level` | family/model/variant/unit 등 R01 identity level 연결 후보 | R02 공통 format에서 명시적 taxonomy를 **not_found** | product-domain | unclear | R02 단독 근거로 정의·채택하지 않는다. |
| `claim_kind` | factual/evaluative/comparative 등 discourse kind 후보 | Liu의 direct/indirect/comparative 및 SemEval objective examples [R02-E004] [R02-E007] | 범용 | unclear | 통일된 ABSA label set을 확인하지 못했다. |
| `recommendation_or_preference` | purchase/choice 권고 또는 선호 표현 후보 | recommender에서 user interest/item property 분리 [R02-E023] | domain-specific | unclear | 일반 ABSA core tuple로는 확인되지 않았다. |

## 15. Unresolved Questions

1. **Product entity level**: 조사한 SemEval/SSA/ASTE/ASQP/ACOS/MPQA format에서 product family, model, generation, market variant, individual unit, bundle/accessory를 일관되게 구분하는 공통 field taxonomy는 찾지 못했다. 이 범위의 negative finding은 R02 corpus/task에 한정한다. [R02-E009] [R02-E011] [R02-E013] [R02-E014] [R02-E015]
2. **Aspect–property mapping**: aspect term/category가 R01 property identity에 언제 one-to-one, many-to-one, 또는 관계없음인지 판정하는 검증된 cross-domain rule을 찾지 못했다.
3. **Measurable claim**: “8시간 간다”의 quantity/unit/measurement condition과 opinion relation을 함께 annotation하는 ABSA 공통 format은 찾지 못했다.
4. **Usage condition**: user/task/environment/activity를 standard dimensions로 구조화한 것은 R02 범위의 ABSA source에서 충분히 확인되지 않았다. R03로 넘긴다.
5. **Claim conflict**: condition mismatch, variant mismatch, holder/test-method mismatch를 true conflict와 구분하는 ABSA shared-task rule을 찾지 못했다.
6. **Holder granularity**: self-experience, quoted manufacturer claim, expert test, other-user aggregation을 통일해 분류하는 ABSA benchmark convention은 확인하지 못했다.
7. **Modality scope**: negation·intensifier·modality가 어느 target/aspect/opinion relation까지 걸리는지 product-review long text 전반에서 표준화된 representation은 unresolved다.
8. **Implicit inference provenance**: implicit aspect/category를 infer했을 때 inference 근거·confidence·alternative aspect를 보존하는 공통 field는 확인하지 못했다.
9. **Hierarchy governance**: aspect hierarchy의 versioning, multilingual synonym control, deprecation을 product ontology 수준으로 운영하는 ABSA standard는 찾지 못했다.
10. **Recommendation/preference**: 추천·구매 권고를 evaluative opinion·comparative preference와 분리하는 일반 ABSA annotation 기준은 unresolved다.

## 16. Evidence Map

| 핵심 finding | Evidence |
| --- | --- |
| Aspect/sentiment을 전체 polarity보다 세분해 다루는 초기·SemEval 계보 | R02-E001, R02-E002, R02-E007 |
| target, aspect term/category, attribute/property는 source별 범위가 다름 | R02-E002, R02-E003, R02-E009 |
| text target span과 semantic entity identity는 다름 | R02-E009, R02-E013 |
| 하나의 문장/리뷰에 mixed aspect 평가와 객관 정보가 공존 | R02-E005, R02-E007 |
| opinion expression을 target/aspect와 관계로 추출 | R02-E011, R02-E014, R02-E015 |
| explicit/implicit은 별도의 annotation/extraction 문제 | R02-E004, R02-E010, R02-E016 |
| holder/source는 일부 structured sentiment와 corpus의 핵심 요소 | R02-E002, R02-E011, R02-E013 |
| comparative는 두 entity와 common basis/preferred direction을 갖는 relation | R02-E006, R02-E017 |
| negation, intensity, modality는 polarity 해석의 조건 | R02-E012 |
| textual/discourse context와 usage condition은 분리 필요 | R02-E018, R02-E019, R02-E022 |
| aspect hierarchy는 존재하지만 data/domain-driven model임 | R02-E020, R02-E021 |
| R02 format은 R01 product-level taxonomy·measurement claim model을 대체하지 않음 | R02-E009, R02-E011, R02-E013, R02-E014, R02-E015 |

## 17. 주요 Sources

16개 source를 사용했다. 핵심 원출처는 R02-S01~R02-S16이며 상세 provenance와 동일-origin chain은 [SOURCES.md](SOURCES.md)에, finding 단위 locator는 [evidence.jsonl](evidence.jsonl)에 있다. 초기 Hu & Liu 논문(R02-S01)과 동일 저자의 후속 monograph(R02-S02)는 같은 연구 계보이므로 독립 evidence strength로 중복 계산하지 않았다. SemEval-2014/2016과 SemEval-2022도 서로 다른 task definition을 지지하지만 하나의 독립적인 “감성 연구 전체”로 산술 합산하지 않았다.

## 18. Potential Conflict with Existing REVIEW²

R01은 catalog의 entity identity, entity kind, model/variant, property, value, condition/market scope를 구분해 조사했다. R02는 text의 target mention, aspect/category, opinion expression, holder, polarity, comparative relation을 조사했다. 두 층은 연결 가능성이 있지만 외부 source는 다음 동치를 보장하지 않는다.

- `Opinion Target` ≠ R01 `Product Entity ID`
- `Aspect Term/Category` ≠ R01 `Property ID`
- R02의 textual qualifier/context ≠ R01의 property applicability·measurement·market condition
- R02 polarity ≠ REVIEW² Claim의 factual validity, evidence reliability, conflict 상태

기존 REVIEW² Source / Evidence Packet / Claim 구조는 수정하지 않았다. 후속 단계에서 이 불일치가 실제 기존 구조와 충돌하는지 확인할 때에도, R02 결과만으로 기존 field를 자동 변경하거나 final mapping을 확정하면 안 된다.
