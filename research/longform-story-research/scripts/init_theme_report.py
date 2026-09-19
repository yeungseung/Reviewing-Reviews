#!/usr/bin/env python3
"""
scripts/init_theme_report.py
============================
LONGFORM STORY ENGINE v2 마스터 리스트에서 특정 항목(item)과 테마(theme)를 읽어
표준 9대 섹션 규격의 리서치 보고서 초안(markdown)을 자동 생성하는 유틸리티.

사용법:
    python3 scripts/init_theme_report.py --item 1 --theme 1
"""

import argparse
import os
import re
import sys
from pathlib import Path

MASTER_LIST_PATH = Path("00_Knowledge/LONGFORM_STORY_ENGINE_v2_RESEARCH_MASTER_LIST.md")
TEMPLATE_PATH = Path("templates/template_research_report.md")
REPORTS_DIR = Path("20_Research_Reports")


def sanitize_filename(text: str) -> str:
    """공백과 특수문자를 언더스코어로 치환하여 파일명에 적합하게 변환"""
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"[\s_]+", "_", text).strip("_")


def parse_theme(item_num: int, theme_num: int):
    """마스터 리스트 파일에서 지정된 item과 theme의 내용을 정규표현식으로 추출"""
    if not MASTER_LIST_PATH.exists():
        print(f"Error: {MASTER_LIST_PATH} not found.", file=sys.stderr)
        sys.exit(1)

    content = MASTER_LIST_PATH.read_text(encoding="utf-8")

    # #1 — [제목] 패턴 검색
    item_pattern = rf"^#\s*#{item_num}\s*—\s*(.+?)$"
    item_matches = list(re.finditer(item_pattern, content, re.MULTILINE))
    if not item_matches:
        print(f"Error: Item #{item_num} not found in master list.", file=sys.stderr)
        sys.exit(1)

    item_title = item_matches[0].group(1).strip()
    start_pos = item_matches[0].start()

    # 다음 item 시작 위치 찾기
    next_item_pattern = r"^#\s*#\d+\s*—"
    next_matches = [m for m in re.finditer(next_item_pattern, content[start_pos + 1:], re.MULTILINE)]
    if next_matches:
        end_pos = start_pos + 1 + next_matches[0].start()
        item_text = content[start_pos:end_pos]
    else:
        item_text = content[start_pos:]

    # Core Thesis 추출
    thesis_match = re.search(r"##\s*Core Thesis\s*\n+>\s*(.+?)(?=\n\n|\n##)", item_text, re.DOTALL)
    core_thesis = thesis_match.group(1).strip() if thesis_match else ""

    # Theme 검색
    theme_pattern = rf"##\s*Research Theme\s*{theme_num}\b"
    theme_matches = list(re.finditer(theme_pattern, item_text))
    if not theme_matches:
        print(f"Error: Research Theme {theme_num} not found in Item #{item_num}.", file=sys.stderr)
        sys.exit(1)

    t_start = theme_matches[0].start()
    next_t_match = re.search(r"##\s*Research Theme\s*\d+\b", item_text[t_start + 1:])
    if next_t_match:
        theme_text = item_text[t_start: t_start + 1 + next_t_match.start()]
    else:
        theme_text = item_text[t_start:]

    # 대주제 추출
    title_match = re.search(r"###\s*대주제\s*\n+\*\*([^\*]+)\*\*", theme_text)
    theme_title = title_match.group(1).strip() if title_match else ""

    # 서머리 추출
    summary_match = re.search(r"###\s*서머리\s*\n+([^\n#]+(?:\n[^\n#]+)*)", theme_text)
    summary = summary_match.group(1).strip() if summary_match else ""

    # 소주제 리스트 추출
    subtopics_match = re.search(r"###\s*소주제\s*\n+((?:-\s*.+\n*)+)", theme_text)
    subtopics = []
    if subtopics_match:
        for line in subtopics_match.group(1).strip().split("\n"):
            line = line.strip()
            if line.startswith("-"):
                subtopics.append(line[1:].strip())

    return {
        "item_num": item_num,
        "item_title": item_title,
        "core_thesis": core_thesis,
        "theme_num": theme_num,
        "theme_title": theme_title,
        "summary": summary,
        "subtopics": subtopics
    }


def generate_report(parsed_data: dict, force: bool = False):
    """추출된 데이터를 바탕으로 보고서 파일 생성"""
    slug = sanitize_filename(parsed_data["theme_title"][:30])
    filename = f"LSEv2_#{parsed_data['item_num']:02d}_T{parsed_data['theme_num']:02d}_{slug}.md"
    
    target_dir = REPORTS_DIR / f"#{parsed_data['item_num']:02d}_{sanitize_filename(parsed_data['item_title'])}"
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / filename

    if target_file.exists() and not force:
        print(f"File already exists: {target_file}")
        print("Use --force to overwrite.")
        return target_file

    # 서브토픽 섹션 빌드
    subtopic_sections = []
    for idx, sub in enumerate(parsed_data["subtopics"], 1):
        subtopic_sections.append(f"""### 3.{idx} Subtopic {idx}: {sub}
* **핵심 발견 (Key Finding)**: 
* **Supporting Evidence (지지 근거)**:
  * 출처: 
  * 인용/데이터: 
* **Counter Evidence (반대 근거 / 반례)**:
* **Boundary Conditions (작동 경계 조건)**:
* **대표 사례 (Representative Case)**:
* **연구 한계 (Limitations)**:
* **현재 판단 (Subtopic Verdict)**: `[Strong / Conditional / Mixed / Contradicted / Insufficient]`
""")

    subtopics_formatted = "\n".join(f"{i}. {s}" for i, s in enumerate(parsed_data["subtopics"], 1))
    subtopics_rendered = "\n".join(subtopic_sections)

    report_content = f"""# Research Report — v2 #{parsed_data['item_num']} / Research Theme {parsed_data['theme_num']}

> **파일명**: `{filename}`  
> **생성일시**: 2026-09-15  
> **연구 상태**: 리서치 대기 (Draft)

---

## 1. Research Target

* **v2 Section**: #{parsed_data['item_num']} — {parsed_data['item_title']}
* **Core Thesis**: {parsed_data['core_thesis']}
* **Research Theme**: {parsed_data['theme_title']}
* **Research Summary**: {parsed_data['summary']}
* **Subtopics**:
{subtopics_formatted}

---

## 2. Executive Findings

* **가장 강하게 지지된 부분 (Strongly Supported)**:
  * 
* **가장 강하게 반박된 부분 (Strongly Contradicted / Nuanced)**:
  * 
* **조건부로만 맞는 부분 (Conditionally True / Boundary Dependent)**:
  * 
* **아직 근거가 부족한 부분 (Insufficient Evidence / Evidence Gap)**:
  * 

---

## 3. Findings by Subtopic

{subtopics_rendered}

---

## 4. Cross-Source Synthesis

### 4.1 Common Claims
* 

### 4.2 Disagreements
* 

### 4.3 Boundary Conditions
* 

### 4.4 Failure Modes
* 

### 4.5 Evidence Gaps
* 

---

## 5. Theory vs Case

### 5.1 Theory
* 

### 5.2 Supporting Cases
* 

### 5.3 Counterexamples
* 

### 5.4 Failed / Overused Cases
* 

---

## 6. Implications for LONGFORM STORY ENGINE v3

* **판정 코드**: `[KEEP | MODIFY | NARROW | EXPAND | SPLIT | MERGE | REJECT | UNRESOLVED]`
* **세부 제언**:
  * 

---

## 7. Provisional Verdict

* **최종 판정**: `[Strong Support | Conditional Support | Mixed Evidence | Weak Support | Contradicted | Insufficient Evidence]`
* **신뢰도 수준 (Confidence)**: `[High | Medium | Low]`
* **판정 이유 (Rationale)**: 
* **판정 번복 조건 (Falsification Criteria)**: 

---

## 8. Aggregation Block

```yaml
CONSENSUS: []
COUNTER: []
BOUNDARY: []
FAILURE: []
MISSING: []
V3_SIGNAL: ""
```

---

## 9. Sources

### 9.1 Primary / Academic Sources
1. 

### 9.2 Official / Original Sources
1. 

### 9.3 High-quality Secondary Sources
1. 

### 9.4 Case / Interview Sources
1. 
"""

    target_file.write_text(report_content, encoding="utf-8")
    print(f"Successfully generated research report scaffold: {target_file}")
    return target_file


def main():
    parser = argparse.ArgumentParser(description="Initialize a standardized research report scaffold from master list.")
    parser.add_argument("--item", type=int, required=True, help="v2 item number (1-86)")
    parser.add_argument("--theme", type=int, required=True, help="Research theme number")
    parser.add_argument("--force", action="store_true", help="Overwrite existing report file")
    args = parser.parse_args()

    data = parse_theme(args.item, args.theme)
    generate_report(data, args.force)


if __name__ == "__main__":
    main()
