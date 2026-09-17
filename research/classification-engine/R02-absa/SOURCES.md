# R02 — Source Register

모든 항목은 R02 finding에 실제 사용한 원출처, 공식 shared-task 원문, 또는 저자가 작성한 scholarly synthesis다. `source_relation`은 citation 관계가 아니라 provenance/독립성 판단을 위한 기록이다. 같은 원출처의 mirror, author-page copy, PDF rendition은 별도 source로 세지 않았다.

| source_id | title | author 또는 organization | publication_date | version_or_edition | url | accessed_at | source_type | original_or_secondary | research_id |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| R02-S01 | Mining and Summarizing Customer Reviews | Minqing Hu; Bing Liu / ACM SIGKDD | 2004 | KDD 2004 | https://dl.acm.org/doi/10.1145/1014052.1014073 | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S02 | Sentiment Analysis and Opinion Mining | Bing Liu / Morgan & Claypool | 2012 | Synthesis Lectures on Human Language Technologies 5(1) | https://www.cs.uic.edu/~liub/FBS/SentimentAnalysis-and-OpinionMining.pdf | 2026-09-17 | scholarly monograph | secondary synthesis with author formalization | R02 |
| R02-S03 | SemEval-2014 Task 4: Aspect Based Sentiment Analysis | Maria Pontiki et al. / ACL | 2014 | SemEval 2014 Task 4 | https://aclanthology.org/S14-2004/ | 2026-09-17 | official shared-task paper | original | R02 |
| R02-S04 | SemEval-2016 Task 5: Aspect Based Sentiment Analysis | Maria Pontiki et al. / ACL | 2016 | SemEval 2016 Task 5 | https://aclanthology.org/S16-1002/ | 2026-09-17 | official shared-task paper | original | R02 |
| R02-S05 | Mining Comparative Sentences and Relations | Nitin Jindal; Bing Liu / AAAI | 2006 | AAAI 2006 | https://cdn.aaai.org/AAAI/2006/AAAI06-209.pdf | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S06 | Recognizing Contextual Polarity in Phrase-Level Sentiment Analysis | Theresa Wilson; Janyce Wiebe; Paul Hoffmann / ACL | 2005 | HLT/EMNLP 2005 | https://aclanthology.org/H05-1044/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S07 | SemEval 2022 Task 10: Structured Sentiment Analysis | Jeremy Barnes et al. / ACL | 2022 | SemEval 2022 Task 10 | https://aclanthology.org/2022.semeval-1.180/ | 2026-09-17 | official shared-task paper | original | R02 |
| R02-S08 | Position-Aware Tagging for Aspect Sentiment Triplet Extraction | Lu Xu et al. / ACL | 2020 | EMNLP 2020 | https://aclanthology.org/2020.emnlp-main.183/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S09 | Aspect Sentiment Quad Prediction as Paraphrase Generation | Wenxuan Zhang et al. / ACL | 2021 | EMNLP 2021 | https://aclanthology.org/2021.emnlp-main.726/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S10 | Aspect-Category-Opinion-Sentiment Quadruple Extraction with Implicit Aspects and Opinions | Hongjie Cai et al. / ACL | 2021 | ACL 2021 | https://aclanthology.org/2021.acl-long.29/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S11 | MPQA 3.0: An Entity/Event-Level Sentiment Corpus | Lingjia Deng; Janyce Wiebe / ACL | 2015 | NAACL-HLT 2015 | https://aclanthology.org/N15-1146/ | 2026-09-17 | peer-reviewed corpus/annotation paper | original | R02 |
| R02-S12 | Context-Guided BERT for Targeted Aspect-Based Sentiment Analysis | Zhengxuan Wu; Desmond C. Ong / AAAI | 2021 | AAAI 2021 | https://ojs.aaai.org/index.php/AAAI/article/view/17659 | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S13 | Domain-Assisted Product Aspect Hierarchy Generation: Towards Hierarchical Organization of Unstructured Consumer Reviews | Jianxing Yu et al. / ACL | 2011 | EMNLP 2011 | https://aclanthology.org/D11-1013/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S14 | A Hierarchical Aspect-Sentiment Model for Online Reviews | Suin Kim et al. / AAAI | 2013 | AAAI 2013 | https://ojs.aaai.org/index.php/AAAI/article/view/8700 | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S15 | A Hierarchical Model of Reviews for Aspect-based Sentiment Analysis | Sebastian Ruder; Parsa Ghaffari; John G. Breslin / ACL | 2016 | EMNLP 2016 | https://aclanthology.org/D16-1103/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |
| R02-S16 | Recommend for a Reason: Unlocking the Power of Unsupervised Aspect-Sentiment Co-Extraction | Zeyu Li et al. / ACL | 2021 | Findings of EMNLP 2021 | https://aclanthology.org/2021.findings-emnlp.66/ | 2026-09-17 | peer-reviewed conference paper | original | R02 |

## Provenance / independence notes

| source_id | source_origin | source_relation | same_origin_chain | independence_note | notes |
| --- | --- | --- | --- | --- | --- |
| R02-S01 | ACM-published original Hu–Liu study | R02-S02 later explains and cites this feature-based lineage | yes — Hu/Liu lineage | R02-S01 and R02-S02 are not counted as independent confirmation of the same initial formulation. | Official ACM landing record was not directly readable in the research client; its original bibliographic identity was verified and substantive later exposition is separately located in R02-S02. |
| R02-S02 | author-hosted scholarly monograph PDF | Later synthesis by the same researcher; cites R02-S01 and comparative work | yes — Hu/Liu lineage | Use for its own formal definitions; do not count its restatement of R02-S01 as a second independent observation. | Author-authored scholarly synthesis, not a blog or summary. |
| R02-S03 | ACL Anthology official task paper | Earlier official SemEval ABSA edition | yes — SemEval ABSA task lineage with R02-S04 | Distinct task edition; supports 2014 task definition, not an independent replication of every ABSA claim. | Official task definition. |
| R02-S04 | ACL Anthology official task paper | Later official SemEval ABSA edition | yes — SemEval ABSA task lineage with R02-S03 | Distinct task edition; used for its explicit E#A/OTE/polarity slots. | Official task definition and data-format description. |
| R02-S05 | AAAI original proceedings PDF | Comparative-opinion line cited by R02-S02 | yes — cited in Hu/Liu opinion-mining lineage | Original comparative study; its relation definition is not treated as a generic sentiment standard. | Uses comparison relation as a separate task. |
| R02-S06 | ACL Anthology original paper | Part of MPQA/contextual-polarity research lineage | yes — contextual-polarity/MPQA lineage with R02-S11 | Different annotation/problem focus from R02-S11; use each only for stated scope. | Primary paper on phrase-level contextual polarity. |
| R02-S07 | ACL Anthology official task paper | Later structured-sentiment shared task; related conceptually, not a mirror of SemEval ABSA tasks | no | Independent official task definition with different graph structure. | Official shared-task source. |
| R02-S08 | ACL Anthology original paper | Contemporary ASTE line | no | Independent paper; not used to infer a universal product ontology. | Triplet extraction structure. |
| R02-S09 | ACL Anthology original paper | Contemporary quad-extraction line, conceptually adjacent to R02-S08/S10 | no | Independent original paper; fields are compared, not source-counted as replicated evidence. | Quad prediction structure. |
| R02-S10 | ACL Anthology original paper | Quad extraction line, conceptually adjacent to R02-S09 | no | Independent original paper; unique use is implicit aspect/opinion scope. | Explicit and implicit elements in a joint task. |
| R02-S11 | ACL Anthology original corpus paper | Extends MPQA annotation infrastructure | yes — MPQA lineage with R02-S06 | Same broader lineage but distinct entity/event target addition; not a mirror. | Used for eTarget and attributed-source limitations. |
| R02-S12 | AAAI original paper | Targeted ABSA textual-context model | no | Model-specific use of textual context; does not establish a context-of-use taxonomy. | Kept separate from R03 scope. |
| R02-S13 | ACL Anthology original paper | Product-aspect hierarchy generation | no | Domain-assisted hierarchy generation, not a standard vocabulary. | Used only to establish that model-derived aspect hierarchies exist. |
| R02-S14 | AAAI original paper | Hierarchical aspect–sentiment tree model | no | Independent model; tree is learned from reviews and is not canonical product ontology. | Used only for learned hierarchy limitation. |
| R02-S15 | ACL Anthology original paper | Review discourse/context model | no | Independent model of document structure, not a usage-condition schema. | Used to distinguish discourse context from R03 context-of-use. |
| R02-S16 | ACL Anthology original paper | Recommender application using aspect-sentiment pairs | no | Application paper; does not make recommendation a required ABSA tuple slot. | Used for limited recommendation/preference boundary finding. |

## Register integrity notes

- All URLs above resolve to the publisher, official proceeding, official shared-task record, or author-hosted scholarly monograph; no mirror or syndicated copy is registered separately.
- `publication_date` and `version_or_edition` are recorded separately because task editions and proceedings matter for field definitions.
- The register contains 16 sources. Evidence strength is assessed per finding in `evidence.jsonl`, not by source count.
