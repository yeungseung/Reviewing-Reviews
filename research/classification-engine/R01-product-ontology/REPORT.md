# R01 — Product Ontology / Product Classification Report

조사일: 2026-09-18 (KST)
범위: 제품 카탈로그·분류·시맨틱 모델이 Product, Class, Property, Value, Unit, Variant, 용어와 버전을 **실제로** 표현하는 방법을 조사했다. 이 문서는 REVIEW²의 최종 Architecture 또는 Schema가 아니며, Candidate Fields도 채택 결정이 아니다.

표기 규칙: **SOURCE FACT**는 외부 원출처의 직접 진술, **RESEARCH INTERPRETATION**은 출처 간 비교, **REVIEW² APPLICATION HYPOTHESIS**는 향후 요구사항 검토를 위한 추론이다. 근거 ID의 상세는 `evidence.jsonl`, 출처 메타데이터는 `SOURCES.md`에 있다.

## 1. 분야 정의

**SOURCE FACT.** ETIM은 제품 그룹·제품 클래스·Feature·Value·Unit·Synonym을 분류 모델의 Entity로 둔다. ECLASS는 분류용 `ClassificationClass`와 같은 Property 집합으로 개별 항목을 기술하는 `CharacterizationClass`를 구분한다. GS1은 GPC의 분류 계층과 GTIN/카탈로그 속성 체계를 함께 사용하며, Schema.org는 `ProductGroup`·`ProductModel`·`Product`·`PropertyValue`를 웹 어휘로 제공한다. [R01-E001, R01-E006, R01-E013, R01-E015, R01-E019, R01-E025]

**RESEARCH INTERPRETATION.** “Product ontology”라는 한 이름 아래에도 (a) 선택·교환을 위한 기술 분류(ETIM/ECLASS), (b) 유통 식별·카탈로그 동기화(GS1), (c) 웹 공개 메타데이터(Schema.org), (d) 형식적 모델/인스턴스 제약(W3C WoT)의 목적이 공존한다. 따라서 Entity 명칭이 같아도 동일한 모델로 간주할 수 없다.

**REVIEW² APPLICATION HYPOTHESIS.** 이후 Classification Requirements에서는 먼저 각 외부 구조가 어떤 목적의 Product Entity를 가리키는지 표시한 뒤에만 리뷰 Claim의 대상 식별에 참고할 수 있다. [R01-E022]

## 2. 이 분야가 해결하려는 문제

**SOURCE FACT.** ETIM은 클래스에 중요한 객관적 기술 특성을 붙여 제품 선택과 클래스 간 구분을 돕되, 마지막 개별 제품의 차이까지 기술하려는 목적은 아니라고 명시한다. GS1 GDM은 전역·카테고리·지역·국가/로컬 계층으로 카탈로그 속성의 공통성과 지역 요구를 나눈다. [R01-E005, R01-E014]

**RESEARCH INTERPRETATION.** 이 분야의 직접 문제는 제품 데이터의 탐색, 교환, 동기화, 비교 가능성이다. 리뷰 문장의 주장 추출·감정·사용자 경험 판정은 이 연구 대상 시스템들의 원래 목적이 아니다.

**REVIEW² APPLICATION HYPOTHESIS.** 카탈로그 구조는 Claim의 대상을 안정적으로 지칭하거나 측정 주장에 단위를 붙이는 보조 근거가 될 수 있으나, 리뷰 평가 자체의 정답 모델로 가져오면 안 된다.

## 3. 대표 표준 / 프레임워크 / 연구 계보

| 시스템 | 이 조사에서 확인한 역할 | 근거 |
| --- | --- | --- |
| ETIM | 기술 제품을 Group/Class와 typed Feature로 분류하는 산업 분류 모델 | R01-E001–R01-E005 |
| ECLASS | 분류와 Property 데이터 모델, IRDI, Unit, Dependency, release를 함께 다루는 표준 | R01-E006–R01-E012 |
| GS1 (GPC/GDM/GDSN/Web Vocabulary) | 거래 품목 식별, 계층 분류, 카탈로그 속성, 시장별 제약·코드 목록 | R01-E013–R01-E018 |
| Schema.org | 웹에서 Product group/model/variant 및 generic property-value를 공개하는 어휘 | R01-E019–R01-E021 |
| W3C WoT Thing Description 1.1 (추가 조사) | 제품 카탈로그 표준은 아니지만, typed DataSchema·템플릿/인스턴스·제약·다국어·버전의 비교용 시맨틱 모델 | R01-E022–R01-E024 |

추가 조사한 W3C WoT는 제품 분류의 대체 표준이 아니다. 단, R01 질문 중 값 유형·Unit·모델 계승·버전의 형식적 표현을 검증할 수 있어 1개 추가 비교 대상으로만 사용했다. [R01-E022–R01-E024]

## 4. 핵심 Entity

| Entity 층 | 시스템별 SOURCE FACT | 연구상 주의 |
| --- | --- | --- |
| 분류 단위 | ETIM `ProductGroup`/`ProductClass`; ECLASS `ClassificationClass`; GS1 GPC Segment→Family→Class→Brick | 모두 분류 단위이나 계층 깊이와 산업 범위가 다르다. [R01-E001, R01-E006, R01-E013] |
| 제품/모델/변형 | GS1 GTIN은 공급망 trade item의 unique identification용이며, GS1 Product 어휘는 Product ID·product range·target market·variant description을 제공한다. Schema.org는 `ProductGroup` template과 `ProductModel` base-to-variant 관계를 제공한다. | ETIM 기본 모델의 Class는 개별 SKU/모델과 동의어가 아니다. [R01-E015, R01-E019, R01-E025] |
| Property / Feature | ETIM Feature, ECLASS Property, GS1 BMS ID가 붙은 Attribute, Schema.org `PropertyValue` | 명칭은 달라도 식별자·자료형·값/제약을 연결하는 역할이 반복된다. [R01-E002, R01-E007, R01-E016, R01-E020] |
| 값·단위 | ETIM Value/Unit, ECLASS Quantity/UoM, GS1 code list/Measurement, Schema.org value/unit, WoT DataSchema unit | 값 자체와 값의 해석 단위는 분리되어 있거나 명시적으로 연결된다. [R01-E002, R01-E007, R01-E010, R01-E020, R01-E023] |
| 용어 | ETIM language-dependent description/synonym, ECLASS IRDI/synonym, WoT language-tagged titles/descriptions | 표시명과 식별자를 혼동하지 않는 방식이 반복된다. [R01-E003, R01-E006, R01-E023] |

## 5. 핵심 Classification Dimensions

| Dimension | 확인된 실제 표현 | 비교 결과 |
| --- | --- | --- |
| Identity | ETIM/ECLASS는 언어 독립 ID, ECLASS는 version을 포함하는 IRDI, GS1은 trade-item GTIN·BMS ID, Schema.org는 `propertyID`/URL을 허용한다. | stable identifier와 표시 문자열 분리가 넓게 반복된다. [R01-E003, R01-E006, R01-E015, R01-E016, R01-E020, R01-E025, R01-E026] |
| 계층/범주 | ETIM two-level Group/Class, ECLASS monohierarchical Class, GS1 four-level GPC, GS1 GDM layer | 계층은 보편적이지만 깊이와 ‘전역/지역’ 축은 시스템별이다. [R01-E001, R01-E006, R01-E013, R01-E014] |
| 값 유형 | ETIM A/L/N/R, ECLASS Integer/Real/Rational·Boolean·String 등, Schema.org Boolean/Number/Text/StructuredValue 등, WoT JSON-schema 계열 type/enum | 같은 ‘텍스트’도 ETIM closed list, Schema.org open Text처럼 제약 강도가 다르다. [R01-E002, R01-E009, R01-E020, R01-E023] |
| 변형 | Schema.org variant dimensions/base model, GS1 target market·product range·variant description | Variant의 구조적 관계와 자유 서술이 함께 존재한다. [R01-E015, R01-E019] |
| 수명주기 | ETIM dynamic release change/deletion tag, ECLASS release/IRDI version과 deprecation flag, GS1 GDSN maintenance release | 용어/속성의 현재 의미는 release와 분리해 읽을 수 없다. [R01-E004, R01-E011, R01-E018, R01-E026] |

## 6. Entity 간 관계

**SOURCE FACT.** ETIM에서는 클래스에 Feature가 배정되고, Feature에는 type 및 Unit 및/또는 Value가 연결된다. ECLASS의 `CharacterizationClass`는 같은 Property 집합으로 기술할 수 있는 제품 인스턴스 집합이며, Property는 data type·value domain을 갖고 quantitative property는 primary UoM을 갖는다. [R01-E001, R01-E002, R01-E006, R01-E007]

**SOURCE FACT.** Schema.org의 `ProductGroup`은 명시된 variation dimension에서만 달라지는 Product들의 template이며, `ProductModel`에서 base product로 향하는 `isVariantOf`는 로컬에 달리 정의되지 않는 한 feature 상속을 허용한다. W3C Thing Model도 인스턴스용 template 및 `tm:extends`를 정의한다. [R01-E019, R01-E022, R01-E024]

**RESEARCH INTERPRETATION.** `Class → allowed/descriptive Property → typed Value (+ Unit)` 관계와 `model/group → variant/instance` 관계는 여러 계열에서 반복되지만, 이들은 하나의 공통 그래프 규격이 아니다.

## 7. Context / Condition 표현 방식

**SOURCE FACT.** ECLASS는 Condition Property가 Depending Property의 조건으로 작용하며, Depending Property는 비어 있지 않은 Condition 집합에 의존한다고 정의한다. GS1 GDM은 attribute의 적용 계층을 global/category/regional/country-local로 나누며, GDM Navigator 예시는 target market·GPC category·다른 속성값의 조합으로 mandatory rule을 표현한다. Schema.org의 `valueReference`는 측정 기준·참조 온도 같은 secondary value를 붙일 수 있다. [R01-E008, R01-E014, R01-E017, R01-E020]

**SOURCE FACT / negative finding.** 이번에 확인한 ETIM **basic classification** 공식 model-information 및 현재 검색 결과만으로는, ECLASS와 동등한 일반적 dependent-property activation 규칙을 확인하지 못했다. 검색 결과의 ETIM Modelling Class optional feature는 별도 3D/모델링 프로파일이므로 basic ETIM의 일반 규칙 근거로 전용하지 않았다. [R01-SR006]

**RESEARCH INTERPRETATION.** 여기서의 condition은 제품 데이터의 적용 조건·시장·측정 참조·속성 의존성이다. 사용자·활동·물리 환경의 context-of-use는 R03 범위이며 이 보고서에서 모델링하지 않는다.

## 8. 비교 가능성 / Conflict 처리

**SOURCE FACT.** ETIM은 numeric/range Feature에 보통 Unit을 붙이고, ECLASS는 quantitative property에 primary/alternative unit을 둔다. Schema.org는 `PropertyValue`에서 range와 unit을 별도 항목으로, `value`에 Boolean/Number/Text 등을 허용한다. GS1은 BMS ID·category layer·mandatory/conditionally mandatory·data type·repeatability를 attribute metadata로 다룬다. [R01-E002, R01-E010, R01-E016, R01-E020]

**RESEARCH INTERPRETATION.** 카탈로그 데이터 비교에서 단순 label 일치보다 property identity, value type, unit, allowed value set, 대상 variant/market, version이 더 강한 비교 단서가 된다. 그러나 표준들이 리뷰 Claim 간 contradiction 판정 규칙을 제공한 것은 아니다.

**REVIEW² APPLICATION HYPOTHESIS.** 향후 Claim 비교 규칙을 검토한다면 Context/condition 또는 variant가 다른 두 Claim을 자동 Conflict로 표시하지 않고, 우선 대상·property·value representation·condition의 정렬 가능성을 분리해 확인해야 한다. 이는 최종 규칙이나 schema가 아니다.

## 9. Reliability / Uncertainty 처리

| 항목 | 이번 조사에서의 처리 |
| --- | --- |
| 출처 우선순위 | 20개 모두 표준기관/표준 어휘의 공식 원출처이다. 블로그·2차 요약을 핵심 근거로 사용하지 않았다. |
| 독립성 | 동일 기관 내부의 여러 문서는 상호 독립 증거 수가 아니다. 각 source의 origin chain과 관계를 `SOURCES.md`에 남겼고, source count로 결론 강도를 정하지 않았다. |
| version risk | live vocabulary/documentation은 접속 시점 상태이며, ETIM 10.0, ECLASS 15.0, GDSN maintenance releases, Schema.org V30.1, WoT TD 1.1처럼 확인 가능한 판본을 함께 기록했다. [R01-E004, R01-E012, R01-E018, R01-E019, R01-E024] |
| 접근 제한 | GS1 GDM Attribute Implementation Guideline의 원문 직접 열람은 403이었고, 공식 검색 색인의 excerpt로만 locator를 확보했다. 해당 Evidence confidence는 medium으로 낮췄다. [R01-E016] |
| 범위 한계 | 카탈로그 standard의 data constraint가 리뷰 서술의 진실성·경험 품질을 검증하지는 않는다. |

## 10. 실제 데이터 구조 또는 필드 사례

| 시스템 | 확인된 필드/구조 사례 | Evidence |
| --- | --- | --- |
| ETIM | Feature type `A`(alphanumeric closed list), `L`(logical), `N`(numeric), `R`(range); Unit; feature/value/class ID; class synonym | R01-E002, R01-E003 |
| ECLASS | `ClassificationClass`, `CharacterizationClass`, `Property`, `PropertyLevel` (min/max/typ/nom), `Quantity`, primary/alternative UoM, `ConditionProperty`, IRDI, deprecation/multi-value flag | R01-E006–R01-E011 |
| GS1 | GTIN, GPC Segment/Family/Class/Brick/Attribute, BMS ID, Global/Category/Regional/Local layer, attribute data type/size/repeatability, target market, code list | R01-E013–R01-E018, R01-E025 |
| Schema.org | `ProductGroup`, `ProductModel`, `isVariantOf`, `variesBy`, `PropertyValue.propertyID/value/minValue/maxValue/unitCode/unitText/valueReference`, `additionalProperty` | R01-E019–R01-E021 |
| W3C WoT | `ThingModel`, `DataSchema.type/enum/unit/const/default`, language-tagged title/description maps, `version.model`, `tm:extends` | R01-E022–R01-E024 |

## 11. REVIEW²에 직접 참고 가능한 구조

아래는 채택 결정이 아니라, 서로 다른 공식 시스템에서 반복되어 재검토 가치가 높은 구조다.

- **stable identifier와 human-readable label의 분리**: ETIM, ECLASS, GS1, Schema.org, W3C가 서로 다른 방식으로 이를 지원한다. [R01-E003, R01-E006, R01-E015, R01-E020, R01-E023, R01-E026]
- **Property의 typed value와 Unit의 명시적 연결**: ETIM/ECLASS/Schema.org/W3C에 모두 직접 근거가 있다. [R01-E002, R01-E007, R01-E010, R01-E020, R01-E023]
- **model/group과 variant/instance를 별도 관계로 표현**: Schema.org 및 W3C에서 template/instance 또는 base/variant 관계가 명시적이다. [R01-E019, R01-E022, R01-E024]
- **version/lifecycle를 concept record와 함께 남김**: ETIM, ECLASS, GS1, W3C에서 release/version/change의 필요성이 확인된다. [R01-E004, R01-E011, R01-E018, R01-E024, R01-E026]

## 12. 수정해서 참고해야 하는 구조

- **Class-to-property template**: ETIM/ECLASS의 클래스 특성표는 Claim 대상의 가능한 기술적 property를 찾는 데 참고할 수 있으나, 리뷰의 주장 하나가 모든 class property를 가져야 한다는 뜻은 아니다. [R01-E005, R01-E006]
- **conditional/mandatory rule**: ECLASS·GS1의 제품 마스터데이터 제약은 보조 참조가 될 수 있지만, 리뷰 문장에 property가 누락되었다고 오류라고 판정하는 규칙으로 옮길 수는 없다. [R01-E008, R01-E016, R01-E017]
- **variant inheritance**: Schema.org/W3C의 계승 관계는 대상 정렬 후보일 뿐, market·generation·configuration이 다른 실제 제품을 자동 동치로 만들지 않는다. [R01-E015, R01-E019, R01-E024]
- **지역 계층**: GS1의 market/local layer는 지역 variant 탐색에 유용하지만, 사용 상황 context를 대체하지 않는다. [R01-E014]

## 13. 가져오면 안 되는 구조 / 한계

- ETIM의 표준 Feature는 개별 제품 간 마지막 차이를 모두 선택할 정도로 상세하지 않다고 명시되어 있다. 따라서 class Feature 목록을 리뷰 Claim의 완전한 속성 목록으로 사용하면 안 된다. [R01-E005]
- GS1 GPC/GDM은 공급망 카탈로그의 식별·교환 목적이다. 제품에 관한 사람의 주관적 평가, 비교 표현, 경험의 신뢰도를 그 계층만으로 표현하지 못한다. [R01-E013, R01-E014]
- Schema.org `additionalProperty`는 generic extension point이므로 specific property가 있을 때는 그쪽을 권장한다. 자유로운 PropertyValue만으로는 단일 의미 체계를 보장하지 않는다. [R01-E021]
- W3C WoT의 interaction/security/hypermedia 영역은 제품 카탈로그 또는 리뷰 Claim 분류 목적으로 이식하지 않는다. 이 연구에서는 DataSchema/계승/버전 표현만 제한적으로 비교했다. [R01-E022–R01-E024]

## 14. Candidate Fields

다음은 외부 근거가 확인된 **검토 후보**다. 이 표는 최종 schema나 필수 필드 목록이 아니다.

| Candidate | 의미 | 외부 구조 / Evidence | 범위 | 상태 | 주의사항 |
| --- | --- | --- | --- | --- | --- |
| `entity_id` | product/class/model/property 등 개념의 stable ID | ETIM IDs, ECLASS IRDI, GS1 GTIN/BMS ID, Schema `propertyID` [R01-E003, R01-E006, R01-E015, R01-E016, R01-E020, R01-E025, R01-E026] | 범용 | strong_candidate | ID scheme와 버전을 분리 검토 |
| `entity_kind` | class, model, variant, instance, property 등 대상 층 | ETIM/ECLASS/Schema/WoT Entity 구분 [R01-E001, R01-E006, R01-E019, R01-E022] | 범용 | strong_candidate | 시스템마다 용어의 경계가 다름 |
| `classification_reference` | 분류 체계 내 code/path | ETIM class, ECLASS class, GPC hierarchy [R01-E001, R01-E006, R01-E013] | 범용 | candidate | 단일 분류를 강제하지 않음 |
| `classification_version` | 참조한 taxonomy/release 판본 | ETIM/ECLASS/GDSN release [R01-E004, R01-E012, R01-E018] | 범용 | strong_candidate | 개체 version과 출처 access date를 혼동하지 않음 |
| `property_id` | property/feature/attribute의 stable 의미 ID | ETIM feature ID, ECLASS IRDI, GS1 BMS ID, Schema `propertyID` [R01-E002, R01-E006, R01-E016, R01-E020] | 범용 | strong_candidate | label만으로 동치 처리하지 않음 |
| `property_label` | 사람이 읽는 property 명칭과 언어 | ETIM language-dependent description, WoT multilingual title [R01-E003, R01-E023] | 범용 | candidate | ID의 대체물이 아님 |
| `value_type` | numeric/boolean/enum/range/text 등 해석 유형 | ETIM A/L/N/R, ECLASS datatype, Schema/WoT typed value [R01-E002, R01-E009, R01-E020, R01-E023] | 범용 | strong_candidate | 시스템별 type map은 후속 검토 필요 |
| `value` | 관측/기재된 value | ECLASS Quantity, Schema `value`, WoT DataSchema [R01-E007, R01-E020, R01-E023] | 범용 | strong_candidate | claim assertion과 catalog value를 구분 |
| `value_range` | min/max 또는 lower/upper/typical/nominal | ETIM R, ECLASS PropertyLevel, Schema min/max [R01-E002, R01-E007, R01-E020] | 범용 | candidate | range의 의미(허용/측정/주장)를 명시해야 함 |
| `allowed_value_set` | closed list/enum/code list와 그 참조 | ETIM A closed list, GS1 code list, WoT enum [R01-E002, R01-E016, R01-E023] | 범용 | candidate | 열린 text와 혼동하지 않음 |
| `unit_id` | Unit의 semantic ID/code | ETIM Unit, ECLASS UoM, Schema unitCode, WoT semantic unit 권고 [R01-E002, R01-E010, R01-E020, R01-E023] | 범용 | strong_candidate | display text와 canonical ID를 분리 검토 |
| `unit_role` | primary/alternative/none 및 conversion 관련 역할 | ECLASS primary/alternative unit, ETIM numeric exception [R01-E002, R01-E010] | 범용 | candidate | 변환 규칙 자체는 아직 조사하지 않음 |
| `cardinality` | single/multi-value/repeatability | ECLASS multi-value flag, GS1 repeatability/multiplicity [R01-E011, R01-E016] | 범용 | candidate | 리뷰 문장 수와 property multiplicity를 동일시하지 않음 |
| `condition_reference` | property 적용/활성의 조건 또는 measurement reference | ECLASS ConditionProperty, GS1 conditional rule, Schema `valueReference` [R01-E008, R01-E017, R01-E020] | 범용 | candidate | R03 context-of-use와 별도 검토 |
| `variant_relation` | group/model/variant/base 또는 replacement 관계 | Schema `isVariantOf`, GS1 Product fields [R01-E015, R01-E019] | 범용 | candidate | generation과 variant의 정확한 구분은 unresolved |
| `variant_dimension` | 변형을 구분하는 명시 축 | Schema.org ProductGroup `variesBy` concept [R01-E019] | 범용 | candidate | 자유 서술 variant와 함께 검토 필요 |
| `market_scope` | target market/지역 적용 범위 | GS1 GDM layer, Product target market [R01-E014, R01-E015] | 범용 | candidate | 판매 시장과 실제 사용 환경은 다름 |
| `term_relation` | synonym/alternate label 관계 | ETIM class synonym, ECLASS synonym/IRDI [R01-E003, R01-E006] | 범용 | candidate | synonym이 항상 1:1 동의어는 아님 |
| `lifecycle_status` | active/deprecated/deleted/replaced 상태 | ETIM dynamic release, ECLASS deprecation flag [R01-E004, R01-E011] | 범용 | candidate | release-specific 해석이 필요 |

## 15. Unresolved Questions

1. **ETIM basic classification의 조건부/종속 property.** 확인한 공식 basic-model 자료에는 ECLASS식 general dependency rule을 찾지 못했다. ETIM Modelling Class의 optional feature를 일반 규칙으로 전용하지 않았다. `not_found`는 이번 접근 범위에 한정된다. [R01-SR006]
2. **Product/Class/Model/Variant/Generation의 범용 교차 매핑.** 네 핵심 시스템이 이 층을 완전히 같은 방식으로 정의하지 않아, one-to-one mapping 근거가 없다. [R01-E001, R01-E006, R01-E015, R01-E019]
3. **Schema.org의 catalog-level required/conditional property 제약.** 확인한 공개 term 문서에는 GS1/ECLASS와 동등한 product-category 의존 필수 제약을 확인하지 못했다. 이 조사에서의 `not_found`이며, Schema.org 전체 생태계의 부재 선언은 아니다. [R01-SR006]
4. **Unit conversion의 canonicalization 정책.** ECLASS alternate unit과 여러 표준의 unit identifier는 확인했으나, 표준 간 변환/rounding/measurement-condition 통합 정책은 조사 범위를 넘어 unresolved로 남긴다. [R01-E010, R01-E020, R01-E023]
5. **GS1 regional/local extension의 정규화 한계.** 표준 계층과 local code list 존재는 확인했지만, market-specific value를 cross-market semantic equivalence로 판정하는 규칙은 확인하지 못했다. [R01-E014, R01-E018]
6. **deprecated/replaced concept의 historical mapping.** ETIM/ECLASS의 lifecycle signal은 확인했으나, 이전 property/class를 현재 Concept에 자동 매핑하는 안전한 일반 규칙은 확인하지 못했다. [R01-E004, R01-E011]
7. **카탈로그 property와 review claim subject의 대응.** 외부 표준은 catalog representation을 목표로 한다. 한 리뷰 문장이 model-level, variant-level, bundle-level 중 무엇을 가리키는지 해석하는 규칙은 R01에서 확정하지 않는다.
8. **필수 property의 의미.** ETIM의 class feature assignment, ECLASS/GS1의 mandatory/conditional mandatory, Schema.org의 optional web vocabulary는 서로 다른 층의 제약일 수 있다. 공통의 ‘필수’로 합치지 않는다. [R01-E001, R01-E008, R01-E016, R01-E021]

## 16. Evidence Map

| Evidence IDs | 다루는 finding |
| --- | --- |
| R01-E001–R01-E005 | ETIM entity, typed feature/value/unit, language/synonym, release, class-feature 한계 |
| R01-E006–R01-E012, R01-E026 | ECLASS class/property/data type/unit/dependency/IRDI version/release |
| R01-E013–R01-E018 | GS1 GPC/GDM, product/variant, BMS attribute constraint, release |
| R01-E019–R01-E021 | Schema.org ProductGroup/variant, PropertyValue, additionalProperty |
| R01-E022–R01-E024 | W3C Thing Model/DataSchema/multilingual/version/extension |
| R01-E025 | GS1 trade-item GTIN identity and scope |

총 26개 Evidence는 모두 `evidence.jsonl`의 동일 ID와 연결된다. R01-SR006은 evidence가 아니라 gap search의 search-ledger ID다.

## 17. 주요 Sources

주요 source는 공식 표준기관의 원출처 20개다. 상세한 publication/version/origin/relation/access 정보는 `SOURCES.md`를 따른다. 핵심 계열은 ETIM (R01-S01–S03), ECLASS (S04–S09), GS1 (S10–S14 및 S19–S20), Schema.org (S15–S17), W3C (S18)이다.

## 18. Potential Conflict with Existing REVIEW²

기존 REVIEW² 문서의 Product scope는 brand/family/model/variant/capacity/market/generation 등을 source matching 관점에서 다룬다. R01의 외부 자료는 기술 class, item characterization, trade item identity, web product group/model을 서로 다르게 정의한다. 따라서 현재 REVIEW² 필드와 외부 Entity를 자동으로 1:1 대응하거나 기존 source/evidence/claim schema를 변경해서는 안 된다.

특히 GS1의 catalog-level mandatory rule, ETIM/ECLASS의 class property template, Schema.org/W3C의 inheritance는 리뷰 Claim의 증명·감정·conflict 판정 규칙이 아니다. 이 차이는 후속 Classification Requirements 단계에서 별도 검토할 potential conflict이며, 이번 R01에서는 기존 파일을 수정하지 않았다.
