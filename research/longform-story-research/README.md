# LONGFORM STORY RESEARCH ENGINE (심층 리서치 시스템)

롱폼 스토리 콘텐츠 기획·집필을 위한 과학적·실증적 리서치 지식 베이스 구축 프로젝트입니다.  
`LONGFORM STORY ENGINE v2` 가설집의 257개 Research Theme를 독립적으로 검증·반증·확장하여 차세대 `v3`의 학술적·실증적 근거 체계를 완성하는 것을 목적으로 합니다.

---

## 1. 절대 원칙 (Guiding Principles)

1. **검증과 반증의 동등성**: 기존 가설을 증명하려 들지 않는다. Supporting Evidence뿐 아니라 **Counter Evidence(반례), Boundary Conditions(경계 조건), Failure Modes(실패 모드)**를 반드시 함께 찾는다.
2. **Zero Hallucination / Zero Speculation**: 출처 없는 주장, 추정, 만들어낸 인용문을 절대 포함하지 않는다. 인과관계와 상관관계를 엄격히 분리한다.
3. **독립 보고서 원칙 (1 Theme = 1 Report)**: 효율화를 이유로 Theme를 합치거나, 최대 7개의 소주제를 마음대로 압축·생략하지 않는다.
4. **출처 우선순위 (Strict Hierarchy)**:
   * 학술: 메타분석/동료평가 저널(Tier 1) > 대학 출판/연구기관(Tier 2) > 고품질 2차 분석(Tier 3)
   * 작품/산업: 플랫폼 공식 데이터/1차 제작기록/당사자 심층 인터뷰
   * 단순 요약 블로그, 출처 불명 대중 매체는 단독 근거로 사용 금지.

---

## 2. 디렉토리 구조

```text
longform-story-research/
├── 00_Knowledge/                  # 검증 대상 기준 문서 (옵시디언 볼트 동기화)
│   ├── LONGFORM_STORY_ENGINE_v2.md
│   └── LONGFORM_STORY_ENGINE_v2_RESEARCH_MASTER_LIST.md
├── 10_Sources_DB/                 # 8대 필수 필드 기반 출처 데이터베이스
│   └── archives/                  # 핵심 논문 요약 및 원문 발췌문
├── 20_Research_Reports/           # 257개 Theme별 독립 심층 리서치 보고서
├── 30_Story_Structures/           # 검증된 롱폼 서사 구조 라이브러리 및 비트시트
├── 40_Idea_Evidence_Cards/        # 실무 기획·연출용 아토믹 근거 카드
├── 50_Factcheck_Checklists/       # 집필 전 팩트체크 및 서사 무결성 체크리스트
├── 90_Synthesis_v3/               # 257개 리서치 판정 및 v3 개정 시그널 집계 허브
├── templates/                     # 5대 표준 산출물 템플릿
└── scripts/                       # Theme 자동 추출 및 검증 유틸리티
```

---

## 3. 보고서 명명 규칙 및 고정 형식

* **파일명**: `LSEv2_#[항목번호]_T[Theme번호]_[대주제 축약].md`  
  (예: `LSEv2_#01_T01_감정변화와_몰입의_인과관계.md`)
* **9대 고정 섹션**:
  1. Research Target (v2 항목, 대주제, 서머리, 소주제 전체)
  2. Executive Findings (지지, 반박, 조건부, 근거부족)
  3. Findings by Subtopic (소주제별 100% 개별 조사)
  4. Cross-Source Synthesis (공통 주장, 충돌, 경계, 실패 모드, Gaps)
  5. Theory vs Case (이론, 지지 사례, 반례, 과잉사용/실패 사례)
  6. Implications for LONGFORM STORY ENGINE v3 (KEEP, MODIFY, REJECT 등)
  7. Provisional Verdict (판정, 신뢰도, 판정 근거, 번복 조건)
  8. Aggregation Block (YAML 메타데이터 블록)
  9. Sources (Tier별 출처 상세)

---

## 4. 리서치 실행 방법

### 신규 Theme 보고서 뼈대 생성
```bash
python3 scripts/init_theme_report.py --item 1 --theme 1
```
이 명령어는 `00_Knowledge/LONGFORM_STORY_ENGINE_v2_RESEARCH_MASTER_LIST.md`에서 `#1 Theme 1`의 원본 대주제, 서머리, 소주제를 정확히 추출하여 `20_Research_Reports/`에 표준 템플릿 파일로 생성합니다.
