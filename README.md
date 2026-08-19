# 김다연 포트폴리오

**[kim-da-yeon.github.io](https://kim-da-yeon.github.io/)** · [이력서 PDF](https://kim-da-yeon.github.io/resume.pdf)

---

## 구성

| 파일 | 내용 |
|---|---|
| `index.html` | 사이트 전체. CSS·JS 인라인, 그림 base64 임베드 |
| `resume.pdf` | 이력서 |
| `.nojekyll` | Pages의 Jekyll 빌드 비활성화 |

외부 요청은 Google Fonts (IBM Plex Sans KR · IBM Plex Mono) 하나뿐. 프레임워크·빌드 단계 없음.

## `.nojekyll` 주의

없으면 GitHub Pages가 Jekyll 빌드를 시도하고, 처리할 대상이 없어 빌드가 실패해 사이트가 404가 됩니다. **파일 재업로드 시 이 파일이 목록에서 빠지지 않았는지 확인.**

## 수정

- `index.html` 편집 후 `main`에 push. 1~2분 내 반영
- 색상은 파일 상단 `:root` CSS 변수

```css
--paper:#F1F2ED;  --ink:#16211E;  --plum:#5A2B47;  --teal:#14706A;
```

- 이력서 교체: Add file → Upload files → `resume.pdf` 드래그 → commit
