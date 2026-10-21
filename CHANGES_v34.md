# v34 변경 사항 (2026-10-21)

## 방향
- 첫 화면 = 직무 제목 + 한 줄 주장 + 근거 3줄 + **Fig. 1**(실측값 vs 기준선 그림)
- 3D 칩 영상 제거 → 직무별 실제 연구 결과 그림으로 대체
- 강조색(울트라마린)은 "본인 방법 · 결과"에만 사용

## 직무별 첫 화면
| 페이지 | 제목 | Fig. 1 (a) | Fig. 1 (b) | 지원 근거 3건 |
|---|---|---|---|---|
| `/` | Data Scientist · ML Researcher | K 복원 | ROUGE-1 | P03 · P06 · P01 |
| `/ml/` | ML Researcher · Applied Scientist | K 복원 | Topic Coherence | P03 · P08 · P05 (KITTI는 Fig. 3) |
| `/nlp/` | NLP · LLM Engineer | ROUGE-1 | Topic Coherence | P09 · P04 · P08 |
| `/ds/` | Data Scientist | 메타데이터 정규화 | 기숙사 수용률 · 기준선 | P06 · P10 · P01 |
| `/av/` | 자율주행 Research Engineer | ROUGE-1 (BDD-X) | KITTI BEV AP | P05 · P04 · P03 |
| `/ai-engineer/` | AI Engineer | ROUGE-1 | 메타데이터 정규화 | P09 · P04 · P10 |

## 사실 수정
- SCI급 논문: "2026.09 투고 예정" → "투고 준비 중" (논문 목록 · 프로젝트 · 상세 · 이력 · 메타 설명 전부)
- AV 트랙의 강화학습 링크 `#/p/rl`(404) → `#/p/pika`
- 수상표 · 이력: 포스터(AWSGLD) → 학위논문(AWSGHMC, P03) 발전 관계 명시

## 구조 · 성능
- 내장 base64 이미지 13장 → `assets/img/*.jpg|png` 분리. HTML 1.37MB → 약 120KB (페이지당)
- 폰트: IBM Plex Sans KR + Pretendard 중복 → Pretendard + JetBrains Mono(수치 · 주소 전용)
- 모바일 메뉴 버튼 아이콘 안 보이던 문제 수정
- 프로젝트 목록: 카드 15장 → 번호 · 제목 · 핵심 결과 · 분류 · 기간 표 형식
- `build_roles.py`: `assets/` 경로 일괄 `../assets/` 치환, 루트 제목 문자열 갱신

## 배포 전 확인
- `assets/hero.mp4` 저장소에서 삭제 가능 (더 이상 참조 안 함)
- `resume*.pdf`, `career*.pdf`, `assets/poster-*.pdf`는 기존 저장소 파일 그대로 사용 (zip에 없음)
- `.impeccable/`, `PRODUCT.md`, `DESIGN.md`는 디자인 기록용 — 배포에 불필요하면 제외 가능
