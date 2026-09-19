#!/usr/bin/env python3
import os
import glob
import yaml

def main():
    print('=== LONGFORM STORY RESEARCH ENGINE INTEGRITY CHECK ===')

    # 1. Reports Check
    reports = glob.glob('20_Research_Reports/*/*.md')
    print(f'1. Total Research Reports: {len(reports)}')
    assert len(reports) == 165, f'Expected 165 reports, found {len(reports)}'

    # Check representative reports
    t01_45 = '20_Research_Reports/#45_Story_State/LSEv2_#45_T01_Story_State_개념의_이론적_근거.md'
    t02_45 = '20_Research_Reports/#45_Story_State/LSEv2_#45_T02_State_Change와_Chapter_가치.md'
    t03_45 = '20_Research_Reports/#45_Story_State/LSEv2_#45_T03_State_Change의_크기와_빈도.md'
    t01_46 = '20_Research_Reports/#46_Micro_Story_Block/LSEv2_#46_T01_Micro_Story_구조의_타당성.md'
    t02_46 = '20_Research_Reports/#46_Micro_Story_Block/LSEv2_#46_T02_Micro_Block과_Retention.md'
    t03_46 = '20_Research_Reports/#46_Micro_Story_Block/LSEv2_#46_T03_정보형_콘텐츠_적용.md'
    t01_47 = '20_Research_Reports/#47_Chapter_Block/LSEv2_#47_T01_Investigative_Chapter_구조.md'
    t02_47 = '20_Research_Reports/#47_Chapter_Block/LSEv2_#47_T02_Answer와_Consequence의_구분.md'
    t03_47 = '20_Research_Reports/#47_Chapter_Block/LSEv2_#47_T03_Chapter_구조의_다양성.md'
    t01_48 = '20_Research_Reports/#48_전체_롱폼_구조/LSEv2_#48_T01_9단계_Macro_Structure_검증.md'
    t02_48 = '20_Research_Reports/#48_전체_롱폼_구조/LSEv2_#48_T02_단계_순서와_필수성.md'
    t03_48 = '20_Research_Reports/#48_전체_롱폼_구조/LSEv2_#48_T03_범용성의_경계.md'
    t01_49 = '20_Research_Reports/#49_Peak의_정의/LSEv2_#49_T01_Climax와_Stake의_관계.md'
    t02_49 = '20_Research_Reports/#49_Peak의_정의/LSEv2_#49_T02_장르별_Peak_형태.md'
    t03_49 = '20_Research_Reports/#49_Peak의_정의/LSEv2_#49_T03_Peak_Inflation과_반례.md'
    t01_50 = '20_Research_Reports/#50_Peak_앞에는_축적이_필요하다/LSEv2_#50_T01_감정별_Build-up_조건.md'
    t02_50 = '20_Research_Reports/#50_Peak_앞에는_축적이_필요하다/LSEv2_#50_T02_축적의_길이강도.md'
    t03_50 = '20_Research_Reports/#50_Peak_앞에는_축적이_필요하다/LSEv2_#50_T03_Setup-Payoff_인과성.md'
    t01_51 = '20_Research_Reports/#51_Payoff/LSEv2_#51_T01_Payoff_유형_분류_검증.md'
    t02_51 = '20_Research_Reports/#51_Payoff/LSEv2_#51_T02_Payoff와_Audience_Satisfaction.md'
    t03_51 = '20_Research_Reports/#51_Payoff/LSEv2_#51_T03_Promise-Payoff_Fit.md'
    t01_52 = '20_Research_Reports/#52_Ending_Emotion/LSEv2_#52_T01_Ending_Emotion과_기억평가.md'
    t02_52 = '20_Research_Reports/#52_Ending_Emotion/LSEv2_#52_T02_끝_감정을_사전_설계하는_효과.md'
    t03_52 = '20_Research_Reports/#52_Ending_Emotion/LSEv2_#52_T03_장르별_Ending_Emotion.md'
    t01_53 = '20_Research_Reports/#53_불쾌한_감정으로_끝낼_때의_위험/LSEv2_#53_T01_Negative_Ending의_단기장기_효과.md'
    t02_53 = '20_Research_Reports/#53_불쾌한_감정으로_끝낼_때의_위험/LSEv2_#53_T02_Positive_Reframe의_효과.md'
    t03_53 = '20_Research_Reports/#53_불쾌한_감정으로_끝낼_때의_위험/LSEv2_#53_T03_채널_누적_감정과_브랜드_경험.md'
    t01_54 = '20_Research_Reports/#54_정보와_감정의_교대/LSEv2_#54_T01_정보-감정_상호작용.md'
    t02_54 = '20_Research_Reports/#54_정보와_감정의_교대/LSEv2_#54_T02_교대_Pacing의_효과.md'
    t03_54 = '20_Research_Reports/#54_정보와_감정의_교대/LSEv2_#54_T03_장르별_최적_비율과_순서.md'
    t01_55 = '20_Research_Reports/#55_Visual_Story의_상위_원칙/LSEv2_#55_T01_Semantic_vs_Surface_Visual_Change.md'
    t02_55 = '20_Research_Reports/#55_Visual_Story의_상위_원칙/LSEv2_#55_T02_멀티모달_의미_정렬.md'
    t03_55 = '20_Research_Reports/#55_Visual_Story의_상위_원칙/LSEv2_#55_T03_장르별_Visual_Refresh.md'
    t01_56 = '20_Research_Reports/#56_화면이_할_수_있는_역할/LSEv2_#56_T01_Visual_Function_8종_분류_검증.md'
    t02_56 = '20_Research_Reports/#56_화면이_할_수_있는_역할/LSEv2_#56_T02_기능별_효과와_오용.md'
    t03_56 = '20_Research_Reports/#56_화면이_할_수_있는_역할/LSEv2_#56_T03_한_컷의_복수_기능.md'
    t01_57 = '20_Research_Reports/#57_컷_길이는_고정하지_않는다/LSEv2_#57_T01_Visual_Duration과_Comprehension.md'
    t02_57 = '20_Research_Reports/#57_컷_길이는_고정하지_않는다/LSEv2_#57_T02_편집_속도와_Attention.md'
    t03_57 = '20_Research_Reports/#57_컷_길이는_고정하지_않는다/LSEv2_#57_T03_자료_유형별_체류_시간.md'
    t01_58 = '20_Research_Reports/#58_시각적_감정_설계/LSEv2_#58_T01_편집_속도와_감정.md'
    t02_58 = '20_Research_Reports/#58_시각적_감정_설계/LSEv2_#58_T02_시각_문법과_정서.md'
    t03_58 = '20_Research_Reports/#58_시각적_감정_설계/LSEv2_#58_T03_감정_목적과_정보_이해의_균형.md'
    t01_59 = '20_Research_Reports/#59_Trust_Layer/LSEv2_#59_T01_사실_오류와_신뢰_붕괴.md'
    t02_59 = '20_Research_Reports/#59_Trust_Layer/LSEv2_#59_T02_Visual_Authenticity와_Source_Co.md'
    
    for fpath, label in [(t01_45, '#45 T01'), (t02_45, '#45 T02'), (t03_45, '#45 T03'), 
                         (t01_46, '#46 T01'), (t02_46, '#46 T02'), (t03_46, '#46 T03'),
                         (t01_47, '#47 T01'), (t02_47, '#47 T02'), (t03_47, '#47 T03'),
                         (t01_48, '#48 T01'), (t02_48, '#48 T02'), (t03_48, '#48 T03'),
                         (t01_49, '#49 T01'), (t02_49, '#49 T02'), (t03_49, '#49 T03'),
                         (t01_50, '#50 T01'), (t02_50, '#50 T02'), (t03_50, '#50 T03'),
                         (t01_51, '#51 T01'), (t02_51, '#51 T02'), (t03_51, '#51 T03'),
                         (t01_52, '#52 T01'), (t02_52, '#52 T02'), (t03_52, '#52 T03'),
                         (t01_53, '#53 T01'), (t02_53, '#53 T02'), (t03_53, '#53 T03'),
                         (t01_54, '#54 T01'), (t02_54, '#54 T02'), (t03_54, '#54 T03'),
                         (t01_55, '#55 T01'), (t02_55, '#55 T02'), (t03_55, '#55 T03'),
                         (t01_56, '#56 T01'), (t02_56, '#56 T02'), (t03_56, '#56 T03'),
                         (t01_57, '#57 T01'), (t02_57, '#57 T02'), (t03_57, '#57 T03'),
                         (t01_58, '#58 T01'),
                         (t02_58, '#58 T02'),
                         (t03_58, '#58 T03'),
                         (t01_59, '#59 T01'),
                         (t02_59, '#59 T02')]:
        assert os.path.exists(fpath), f'{label} report file missing!'
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        for sec in ['## 1. Research Target', '## 2. Executive Findings', '## 3. Findings by Subtopic', 
                    '## 4. Narrative Application Architecture', '## 5. Evidence Quality Assessment', 
                    '## 6. Counter-Intuitive Findings & Paradoxes', '## 7. Inter-Theme Connections', 
                    '## 8. Practical Implementation Checklist', '## 9. Version & Evolution History']:
            assert sec in content, f'Missing section in {label}: {sec}'
    print('   - LSEv2_#45_T01~T03, #46_T01~T03, #47_T01~T03, #48_T01~T03, #49_T01~T03, #50_T01~T03, #51_T01~T03, #52_T01~T03, #53_T01~T03, #54_T01~T03, #55_T01~T03, #56_T01~T03, #57_T01~T03, #58_T01~T03, #59_T01~T02: All 9 standard sections verified.')

    # 2. Sources Check
    source_files = glob.glob('10_Sources_DB/SRC-*.yaml')
    print(f'2. Total Source YAMLs: {len(source_files)}')
    assert len(source_files) == 589, f'Expected 589 sources, found {len(source_files)}'

    with open('10_Sources_DB/index.yaml', 'r', encoding='utf-8') as f:
        idx = yaml.safe_load(f)
    assert idx['total_sources'] == 589, f"index.yaml total_sources mismatch: {idx.get('total_sources')}"
    assert idx['tier_1_sources'] == 585, f"Tier 1 mismatch: {idx.get('tier_1_sources')}"
    assert idx['tier_2_sources'] == 4, f"Tier 2 mismatch: {idx.get('tier_2_sources')}"
    assert len(idx['sources']) == 589, f"index.yaml sources list mismatch: {len(idx['sources'])}"
    print('   - Sources DB & index.yaml: 589 sources perfectly synchronized (Tier 1: 585, Tier 2: 4).')

    # 3. Cards Check
    psy_cards = glob.glob('40_Idea_Evidence_Cards/psychology/CARD-PSY-*.md')
    nar_cards = glob.glob('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-*.md')
    total_cards = len(psy_cards) + len(nar_cards)
    print(f'3. Total Cards: PSY {len(psy_cards)}, NAR {len(nar_cards)} (Total: {total_cards} files)')
    assert len(psy_cards) == 155, f'Expected 155 PSY cards, found {len(psy_cards)}'
    assert len(nar_cards) == 159, f'Expected 159 NAR cards, found {len(nar_cards)}'
    assert total_cards == 314, f'Expected 314 cards, found {total_cards}'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-129_정보공백과_인지적종결_탐구사이클_모델.md'), 'CARD-PSY-129 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-130_6단계_탐구형_챕터블록_조립기와_인과도약_아키텍처.md'), 'CARD-NAR-130 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-130_지적해결과_사회적시뮬레이션_인지도약_모델.md'), 'CARD-PSY-130 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-131_답_파급_분리_아키텍처와_인과연속_엔진.md'), 'CARD-NAR-131 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-131_스키마포화_방어와_인지인지변주_모델.md'), 'CARD-PSY-131 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-132_6대_대체챕터문법과_병렬동기화_아키텍처.md'), 'CARD-NAR-132 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-132_9단계_거시서사와_인지적여정_원형모델.md'), 'CARD-PSY-132 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-133_9단계_범용매크로구조와_위상정렬_엔진.md'), 'CARD-NAR-133 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-133_서사순서역전과_호기심_아이러니_전환모델.md'), 'CARD-PSY-133 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-134_비선형_위상치환과_실용압축_아키텍처.md'), 'CARD-NAR-134 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-134_서사플롯화와_역사과학_인지단순화_위험모델.md'), 'CARD-PSY-134 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-135_7대도메인_적응매트릭스와_공식주의_피로방어_아키텍처.md'), 'CARD-NAR-135 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-135_가치손실위기와_결정적선택의_피크인지모델.md'), 'CARD-PSY-135 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-136_클라이맥스_스테이크_정렬과_이중피크_아키텍처.md'), 'CARD-NAR-136 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-136_도메인별_가치트레이드오프와_패러다임발견_피크모델.md'), 'CARD-PSY-136 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-137_장르별_피크프로파일과_가치선택_엔진.md'), 'CARD-NAR-137 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-137_자극순응과_조용한클라이맥스_인지신경모델.md'), 'CARD-PSY-137 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-138_피크인플레이션_방어와_초월적정적_아키텍처.md'), 'CARD-NAR-138 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-138_감정별_사전축적_인지신경모델.md'), 'CARD-PSY-138 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-139_7대감정_빌드업시퀀서와_축적엔진.md'), 'CARD-NAR-139 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-139_축적구간_인지피로와_고구마한계선_신경심리모델.md'), 'CARD-PSY-139 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-140_계단식강도에스컬레이션과_마이크로페이오프_시퀀서.md'), 'CARD-NAR-140 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-140_망각된복선소환과_인과적카타르시스_인지신경모델.md'), 'CARD-PSY-140 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-141_3단계체호프총검증기와_다층복선교차회수_엔진.md'), 'CARD-NAR-141 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-141_9대페이오프와_인지정서보상_신경모델.md'), 'CARD-PSY-141 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-142_9대페이오프_매트릭스와_복합엔딩_아키텍처.md'), 'CARD-NAR-142 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-142_인지적종결욕구와_기대불일치_페이오프만족_신경모델.md'), 'CARD-PSY-142 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-143_페이오프기대매칭과_정당한종결_보정_아키텍처.md'), 'CARD-NAR-143 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-143_기대지평과_서사적계약_인지배신방어_모델.md'), 'CARD-PSY-143 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-144_에로테틱계약감사와_창의적전복_아키텍처.md'), 'CARD-NAR-144 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-144_피크엔드법칙과_서사회상기억_인지신경모델.md'), 'CARD-PSY-144 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-145_엔딩감정수렴과_사후평가극대화_엔진.md'), 'CARD-NAR-145 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-145_확증편향과_서사적_조기종결의_인지모델.md'), 'CARD-PSY-145 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-146_결말역산_감정설계와_프로크루스테스_방어엔진.md'), 'CARD-NAR-146 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-146_슬픔의역설과_장르별_정서보상_인지신경모델.md'), 'CARD-PSY-146 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-147_7대장르_엔딩감정매트릭스와_해결지향_효능감부스터.md'), 'CARD-NAR-147 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-147_부정성편향과_미디어회피_정서탈진_신경모델.md'), 'CARD-PSY-147 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-148_부정엔딩피로거버너와_고통결속_전환엔진.md'), 'CARD-NAR-148 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-148_위협효능감_불균형과_중화가설_인지신경모델.md'), 'CARD-PSY-148 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-149_3단계_완충시퀀서와_현실기반_리프레임_아키텍처.md'), 'CARD-NAR-149 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-149_평가적조건화와_기분관리이론의_채널낙인_인지모델.md'), 'CARD-PSY-149 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-150_채널누적정서_거버넌스와_습관보상루프_아키텍처.md'), 'CARD-NAR-150 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-150_신체표지와_평가주기_정보감정_상호순환_신경모델.md'), 'CARD-PSY-150 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-151_3단계_감정증거_재귀엔진과_동기화추론_제어아키텍처.md'), 'CARD-NAR-151 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-151_인지부하와_제한용량모델_각성진동_신경모델.md'), 'CARD-PSY-151 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-152_60-90초_교대페이싱_리듬시퀀서와_분절화엔진.md'), 'CARD-NAR-152 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-152_문화적인지와_위험지각_장르별_정보수용_신경모델.md'), 'CARD-PSY-152 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-153_장르별_비율매트릭스와_시퀀싱_순서제어_아키텍처.md'), 'CARD-NAR-153 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-153_정향반응과_장면인지_의미지도_시지각_신경모델.md'), 'CARD-PSY-153 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-154_의미시각갱신_엔진과_강화된연속성_거버너아키텍처.md'), 'CARD-NAR-154 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-154_이중부호화와_시청각불일치_시각우위_신경모델.md'), 'CARD-PSY-154 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-155_멀티모달_의미정렬엔진과_중복자막_배제필터_아키텍처.md'), 'CARD-NAR-155 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-155_표정반응과_전주의적지각_시각적휴지기_신경모델.md'), 'CARD-PSY-155 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-156_장르별_시각갱신프로파일러와_시각적쉼_트리거아키텍처.md'), 'CARD-NAR-156 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-156_시각적사고와_텍스트시각기능격상_지각적상징_신경모델.md'), 'CARD-PSY-156 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-157_8대_시각기능_디스패처와_시각증거_정위_서스펜스_아키텍처.md'), 'CARD-NAR-157 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-157_생생함편향과_감정착취_심리적반발_신경인지모델.md'), 'CARD-PSY-157 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-158_시각기능_오용방어기와_정직한데이터_서사검증_아키텍처.md'), 'CARD-NAR-158 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-158_시선스캔경로와_다층의미_인지과부하방어_신경모델.md'), 'CARD-PSY-158 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-159_이중목적샷_조립기와_계층적신호화_시각경제학_아키텍처.md'), 'CARD-NAR-159 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-159_시각정보밀도와_읽기처리속도_기반_동적체류시간_신경인지모델.md'), 'CARD-PSY-159 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-160_정보밀도_적응형_컷길이_시퀀서와_지루함_방어_거버너_아키텍처.md'), 'CARD-NAR-160 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-160_지향반응과_각성진동_고속편집_인지과부하방어_신경생리모델.md'), 'CARD-PSY-160 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-161_지향반응_각성시퀀서와_시선중심_연속성편집_아키텍처.md'), 'CARD-NAR-161 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-161_자료유형별_인지스캔경로와_정서응고화_다층체류시간_신경인지모델.md'), 'CARD-PSY-161 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-162_7대_자료유형별_동적체류_매트릭스와_정서완충_시퀀서_아키텍처.md'), 'CARD-NAR-162 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-162_감정유형별_신경생리적_주기와_편집속도_각성_성찰_이원화_인지신경모델.md'), 'CARD-PSY-162 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-163_7대_감정별_동적_템포_시퀀서와_정서불일치_방어_아키텍처.md'), 'CARD-NAR-163 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-163_시각적거리감과_원초적감정전염_샷스케일_체화신경인지모델.md'), 'CARD-PSY-163 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-164_4단계_시각거리_매트릭스와_동적_카메라무빙_정서동기화_아키텍처.md'), 'CARD-NAR-164 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-164_시각현저성과_인지부하경합_다중감각통합_인지신경모델.md'), 'CARD-PSY-164 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-165_정서분리_동적체류_엔진과_삼중감각_정합성_거버너_아키텍처.md'), 'CARD-NAR-165 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-165_트루시니스효과와_지속영향_출처감시혼동_사실오류_신경인지모델.md'), 'CARD-PSY-165 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-166_사실정합성_게이트웨이와_시각사료_출처라벨링_3단계_신뢰복구_아키텍처.md'), 'CARD-NAR-166 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/psychology/CARD-PSY-166_시각적진실편향과_거짓말쟁이배당금_출처혼동_신경인지모델.md'), 'CARD-PSY-166 missing'
    assert os.path.exists('40_Idea_Evidence_Cards/narrative_craft/CARD-NAR-167_4단계_시각자료_출처표준과_포렌식워터마크_리얼리티거버너_아키텍처.md'), 'CARD-NAR-167 missing'
    print('   - Atomic Cards: CARD-PSY-166 and CARD-NAR-167 verified. Cumulative 314 cards active.')

    # 4. Verdicts Registry Check
    with open('90_Synthesis_v3/verdicts_registry.yaml', 'r', encoding='utf-8') as f:
        reg = yaml.safe_load(f)
    assert reg['total_themes_analyzed'] == 165, f"Registry total mismatch: {reg.get('total_themes_analyzed')}"
    assert reg['verdict_counts']['strong_support'] == 163, 'Strong support count mismatch'
    assert reg['v3_signal_counts']['keep'] == 155, 'Keep count mismatch'
    assert reg['v3_signal_counts']['expand'] == 165, 'Expand count mismatch'
    assert len(reg['reports']) == 165, f"Registry reports count mismatch: {len(reg.get('reports'))}"
    assert reg['reports'][-1]['theme_id'] == 'LSEv2_#59_T02', 'Last report in registry is not #59 T02!'
    print('   - Verdicts Registry: 165 themes perfectly synchronized.')

    print()
    print('>>> ALL 165 THEMES & 314 CARDS INTEGRITY CHECKS PASSED 100%! <<<')

if __name__ == '__main__':
    main()
