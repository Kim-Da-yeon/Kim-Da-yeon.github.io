# 김다연 데이터 분석 포트폴리오

**추론 알고리즘을 직접 구현하고, 그 모델로 센서 · 텍스트 · 교통 데이터를 분석합니다**

### → **[kim-da-yeon.github.io](https://kim-da-yeon.github.io/)** ← 포트폴리오 보기

[![이력서 PDF](https://img.shields.io/badge/이력서-PDF_내려받기-5A2B47?style=for-the-badge)](https://kim-da-yeon.github.io/resume.pdf)
[![GitHub](https://img.shields.io/badge/GitHub-Kim--Da--yeon-16211E?style=for-the-badge&logo=github)](https://github.com/Kim-Da-yeon)

> 고려대학교 세종캠퍼스 빅데이터사이언스학과 석사과정 · 졸업예정 2027.02 · 지도교수 전수영

---

## 담고 있는 것

| 장 | 내용 |
|---|---|
| **01 실무 경험** | JERESFARM 데이터 사이언티스트 인턴 (2023.12–2024.03) — 결측이 잦은 단기 센서 데이터로 예측 파이프라인 구축, 그리고 *분석이 불가능하다는 결론* 자체를 정량적으로 확인한 과정 |
| **02 연구 · 논문** | 동일 모델(TNTM)의 제약을 단계적으로 해제한 연속 연구 3편, 전부 제1저자 |
| **03 분석 프로젝트** | 스마트팜 작물 적합도 분류 · 택시 수요 군집화 · 자율주행 sLLM 파인튜닝 · 규제 원문 토픽 모델링 |
| **04 데이터 설계 · 품질** | MySQL ER 설계 및 정규화, LLM 생성 메타데이터의 국제 표준 정규화 |
| **Code** | 각 프로젝트의 구현 저장소 |
| **Record** | 이력 · 참여 연구 3건 · 수상 |
| **Fit** | 데이터 분석 직무 요구 역량과의 대응표 |

## 논문

| 논문 | 게재 |
|---|---|
| AWSGLD를 이용한 전이 네트워크 토픽 모델 추론 | 한국자료분석학회지 28(1) 109–121 · 제1저자 · 2026 |
| 자율주행 도메인에서 LoRA 기반 sLLM 파인튜닝 | 한국자료분석학회지 27(3) 769–780 · 제1저자 · 2025 |
| Fixed-K Shrinkage BNTM with AWSGLD Inference | 한국자료분석학회 하계학술발표대회 포스터논문 **장려상** · 2026 |
| Fixed-K Shrinkage BNTM with AWSGHMC Inference | SCI급 학술지 투고 중 · 석사 학위논문 |

## 코드 저장소

| 저장소 | 내용 |
|---|---|
| [llmrec-metadata-standard](https://github.com/Kim-Da-yeon/llmrec-metadata-standard) | LLM 생성 메타데이터의 ISO 3166-1 / BCP 47 정규화 — 상호운용성 0 → 80.3% |
| [GCIoU-SGMCMC-3D-Detection](https://github.com/Kim-Da-yeon/GCIoU-SGMCMC-3D-Detection) | SGMCMC를 3D 객체 탐지 최적화기로 썼을 때의 비교 실험 |
| [SONY_Chatbot](https://github.com/Kim-Da-yeon/SONY_Chatbot) | 제품 설명서 대상 한국어 RAG — 페이지 단위 출처 표기 |
| [mcmc-r-packages](https://github.com/Kim-Da-yeon/mcmc-r-packages) | SAMC를 R · C/Rcpp · Python 세 백엔드로 구현한 R 패키지 |
| [Pykachu-Volleyball](https://github.com/Kim-Da-yeon/Pykachu-Volleyball) | gymnasium 환경 표 기반 Q-learning |
| `bntm-topic-model` | 석사 학위논문 코드 — 심사 중 비공개, 게재 후 공개 예정 |

---

## 이 저장소에 대해

`index.html` 한 장으로 된 정적 사이트입니다. 프레임워크도 빌드 단계도 없고,
CSS와 JS는 파일 안에 인라인으로 들어 있습니다. 외부에서 받아오는 것은 Google Fonts의
IBM Plex Sans KR / IBM Plex Mono뿐입니다.

```
.
├── index.html    # 사이트 전체 (인라인 CSS/JS, 그림은 base64 임베드)
├── resume.pdf    # 이력서 — 페이지 Record 장에서 내려받기
└── .nojekyll     # Pages가 Jekyll 빌드를 시도하지 않게 함
```

`.nojekyll`이 있어야 합니다. 없으면 GitHub Pages가 이 저장소를 Jekyll 사이트로
빌드하려 하고, Jekyll이 처리할 것이 없어 빌드가 실패해 사이트가 404가 됩니다.
**파일을 다시 업로드할 때 이 파일이 빠지지 않게 주의하세요.**

### 수정 방법

`index.html`을 직접 편집하고 `main`에 올리면 1–2분 안에 반영됩니다.
색은 파일 상단 `:root`의 CSS 변수로 모아두었습니다.

```css
--paper:#F1F2ED;  --ink:#16211E;  --plum:#5A2B47;  --teal:#14706A;
```
