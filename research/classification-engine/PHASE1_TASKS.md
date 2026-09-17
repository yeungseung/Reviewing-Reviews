# Phase 1 Tasks: R01~R03

이 문서는 Phase 1의 실제 연구 결과를 기록하는 문서가 아니라 R01~R03의 목적, 질문, 기록 경계를 정의하는 조사 명세다. Phase 1에서는 이 명세를 바탕으로 R01~R03의 실제 리서치를 수행한다. 아래 내용 자체는 finding, schema, architecture 결론이 아니다.

## R01 — Product Ontology / Product Classification

### 목적

제품과 제품 속성을 기존 표준들이 어떤 구조로 표현하는지 조사한다.

### 중점 질문

- Product / Class / Property / Feature / Value / Unit 관계는 어떻게 표현되는가
- Property type에는 어떤 종류가 있는가
- Numeric / Boolean / Range / Enum / Text 등의 차이를 어떻게 처리하는가
- Unit은 Property와 어떻게 연결되는가
- Conditional property 또는 dependent property 개념이 존재하는가
- Variant / Model / Generation 차이는 어떻게 표현되는가
- Category별 특수 속성과 범용 속성을 어떻게 분리하는가
- Synonym / multilingual terminology는 어떻게 관리하는가
- 제품 ontology를 Claim 분석에 연결할 때 어떤 구조가 재사용 가능한가

### 후보 조사 대상

ETIM, ECLASS, GS1 관련 제품 taxonomy, Schema.org Product 구조 및 그 밖의 유의미한 산업 Product Ontology를 조사 대상으로 고려한다. 이 목록은 제한 목록이 아니다.

## R02 — Aspect-Based Sentiment Analysis / Opinion Mining

### 목적

리뷰 문장에서 평가 가능한 Claim과 Aspect를 어떤 단위로 추출하는지 조사한다.

### 중점 질문

- Aspect Term과 Aspect Category 차이는 무엇인가
- Opinion Term은 어떻게 표현되는가
- Explicit Aspect와 Implicit Aspect는 어떻게 다루는가
- Sentiment polarity 외에 intensity / certainty / comparison 등의 구조가 있는가
- 하나의 문장에 여러 Aspect가 있을 때 어떻게 분리하는가
- 객관적 Claim과 주관적 Opinion을 구분하는 방법이 있는가
- Comparative Opinion은 어떻게 표현되는가
- Aspect hierarchy는 어떻게 구성되는가
- Context가 다른 동일 Aspect를 어떻게 처리하는가
- 기존 ABSA 구조가 제품 리뷰 분석에 어디까지 유효하고 어디서 한계가 있는가

## R03 — Context-of-Use / Usability Evaluation

### 목적

동일한 제품이 사용자, 환경, 활동, 시간, 거리 등의 조건에 따라 다르게 평가되는 구조를 조사한다.

### 중점 질문

- Context-of-use를 어떤 dimension으로 나누는가
- User / Task / Activity / Environment / Equipment 관계는 어떻게 정의되는가
- Physical context와 social context는 어떻게 구분되는가
- Usage condition을 어떤 형태로 기록하는가
- 동일 Property라도 Context에 따라 평가가 달라지는 것을 어떻게 표현하는가
- Objective measurement condition과 Subjective experience condition을 어떻게 구분하는가
- usability requirement와 test condition을 어떻게 연결하는가
- Condition mismatch 때문에 발생하는 apparent conflict를 구별할 구조가 있는가
- Context를 너무 세분화해 데이터가 폭발하는 문제를 어떻게 방지하는가

## Phase 1 이후 예정 작업

아래 항목은 후속 연구 예정 목록일 뿐, 이 문서에서 상세 설계나 실제 리서치를 시작하지 않는다.

- R04 Professional Product Testing
- R05 Multi-Criteria Decision Making / Kano / QFD
- R06 Review Reliability / Evidence Quality
- R07 Comparability / Conflict / Contradiction
- R08 Knowledge Graph / Claim Data Model
- R09 Cross-category Stress Test
- R10 Synthesis / Classification Requirements

## Phase 1 종료 경계

R01~R03의 실제 조사 결과가 쌓인 뒤에도, 이 Phase의 산출물은 외부 구조를 추적 가능하게 비교하기 위한 기록이다. Classification Requirements, Claim Classification Architecture, Schema의 결정은 후속 단계에서 별도 검토한다.
