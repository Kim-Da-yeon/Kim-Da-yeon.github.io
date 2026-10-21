# Product

<!-- impeccable:product-schema 1 -->

> Interview round substituted: the owner delegated all open decisions ("너가 알아서 채워줘"). Facts marked *(inferred)* come from the existing site content and the owner's brief, not from an interview answer.

## Platform

web

## Users
- **Primary:** hiring reviewers at Korean tech companies and labs (team leads, senior researchers, HR screeners) deciding whether to interview 김다연 for one specific role. They arrive from a résumé link, skim the first viewport for 30 seconds on a desktop, then dive into one or two projects. *(inferred from owner brief: "면접관 입장", "직무 적합성이 우선적으로 보이는게 필요")*
- **Secondary:** interviewers re-reading project details right before or during an interview. *(inferred)*

## Product Purpose
A personal research-and-engineering portfolio for 김다연 (Kim Dayeon, M.S. candidate, Korea University Big Data Science, graduating 2027.02). Success = the reviewer sees role fit within the first viewport and finds verifiable evidence (papers, DOIs, metrics, repos) fast enough to decide on an interview.

## Positioning
A candidate who validates models against ground truth: she designs simulation environments where the true answer is known, then shows the model recovers it, and reports every claim with a number, a baseline, and a source (DOI, repo, poster). First-author journal papers and an NRF grant as PI back this up — evidence a template portfolio cannot copy.

## Operating Context
- Five role-specific entry points generated from one root page: `ml/` ML Researcher · Applied Scientist, `nlp/` NLP · LLM Engineer, `ds/` Data Scientist, `av/` 자율주행 Research Engineer, `ai-engineer/` AI Engineer (Language AI). Each role page must lead with that role's fit.
- Hosted on GitHub Pages (`kim-da-yeon.github.io`). Résumé/career PDFs per role live in the repo root (not in this bundle).
- Korean-first copy with English technical terms.

## Capabilities and Constraints
- Static single `index.html` (inline CSS/JS) + `build_roles.py` that clones it into role folders by string replacement. Keep that workflow working.
- Hash router: `#/p/<id>` project detail pages, keyboard ←/→ navigation, project filters.
- Project data lives in JS arrays (`P`, `D`, `FEAT`, `PAPERS`, `ROLES`, `AV_ITEMS`).
- SCI-level journal paper (BNTM, master's thesis) is **not yet submitted** — must read "투고 준비 중", never a past date. *(confirmed by owner 2026-10-21)*

## Brand Commitments
- Name 김다연 / Kim Dayeon; existing point color green `#3B7A57` was a prior choice, not a binding commitment. *(inferred)*
- The 3D blue chip hero video is decorative and may be removed. *(confirmed by owner)*

## Evidence on Hand
- Papers: JKDAS 28(1) 109–121 (DOI 10.37727/jkdas.2026.28.1.109), JKDAS 27(3) 769–780 (DOI 10.37727/jkdas.2025.27.3.769); BNTM thesis paper in preparation.
- Grants: NRF 석사과정생연구장려금 PI (RS-2025-25437035), NRF 참여 (RS-2024-00352792), KIAT 참여 (RS-2025-02215617).
- Awards: KDAS 2026 포스터 장려상, 고려대 통계학술제 최우수상 2023, 세종 미래모빌리티 공모전 장려상 2023.
- 15 projects with metrics; real figures embedded (FAERS topic path graph, KITTI detection comparison, taxi cluster/QGIS maps, dorm charts, SONY chatbot screenshots, metadata normalization diagrams), profile photo.
- Public repos: llmrec-metadata-standard, GCIoU-SGMCMC-3D-Detection, SONY_Chatbot, mcmc-r-packages, Pykachu-Volleyball. bntm-topic-model private until publication.
- Absent: no testimonials, no company logos, no employment beyond the JERESFARM internship — do not invent.

## Product Principles
1. Role fit first: every role page answers "why this person for this role" before anything else.
2. Prove, don't claim: every headline number carries its baseline and source.
3. Hierarchy over volume: the strongest research outranks class projects visually.
4. Honest status: pending work is labeled as pending.

## Accessibility & Inclusion
WCAG AA contrast, keyboard navigation, reduced-motion respect, works at 390px mobile width. *(inferred standard)*
