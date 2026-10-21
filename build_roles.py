# -*- coding: utf-8 -*-
"""index.html 하나로 직무별 폴더(ml/ nlp/ ds/ av/ ai-engineer/)의 index.html을 재생성합니다.
사용: 저장소 루트에서  python build_roles.py
루트 index.html을 고친 뒤 이 스크립트만 다시 돌리면 4개 폴더가 갱신됩니다."""
import os, re, io

ROLES = {
    'ml':  {'name': 'ML Researcher',              'card': 'ML Researcher'},
    'nlp': {'name': 'NLP · LLM Engineer',         'card': 'NLP · LLM Engineer · RAG'},
    'ds':  {'name': 'Data Scientist',             'card': 'Data Scientist · 데이터 분석'},
    'av':  {'name': '자율주행 Research Engineer', 'card': '자율주행 · Research Engineer'},
    'cj':  {'name': 'AI Engineer', 'card': 'AI Engineer · Language AI', 'dir': 'ai-engineer'},
}

here = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(here, 'index.html'), encoding='utf-8').read()

for key, r in ROLES.items():
    d = r.get('dir', key)
    s = src
    # 1) 직무 고정 메타 (JS가 이 값을 읽어 ?role= 없이도 해당 직무로 렌더링)
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="role" content="%s">' % key, 1)
    # 2) 탭 제목 · OG · 상단 브랜드 · ID카드 부제
    s = s.replace('<title>김다연 · Data Scientist · ML Researcher</title>', '<title>김다연 · %s</title>' % r['name'], 1)
    s = s.replace('<meta property="og:title" content="김다연 · Data Scientist · ML Researcher">', '<meta property="og:title" content="김다연 · %s">' % r['name'], 1)
    s = s.replace('<meta name="description" content="김다연 · Data Scientist · ML Researcher —', '<meta name="description" content="김다연 · %s —' % r['name'], 1)
    s = s.replace('<em>Data Scientist · ML Researcher</em></a>', '<em>%s</em></a>' % r['name'], 1)
    s = s.replace('<link rel="canonical" href="https://kim-da-yeon.github.io/">', '<link rel="canonical" href="https://kim-da-yeon.github.io/%s/">' % d, 1)
    s = s.replace('<meta property="og:url" content="https://kim-da-yeon.github.io/">', '<meta property="og:url" content="https://kim-da-yeon.github.io/%s/">' % d, 1)
    # 2.5) 정적 자산(HTML에 직접 쓴 assets/ 경로)은 직무 폴더에서 한 단계 위를 가리키도록.
    #      JS가 그리는 그림 · 상세 이미지는 스크립트의 ROOT/A 상수가 알아서 ../ 를 붙인다.
    s = s.replace('src="assets/', 'src="../assets/').replace('href="assets/', 'href="../assets/')
    # 3) 직무별 페이지에서는 "다른 직무 기준으로 보기" 전환 링크 제거
    s = re.sub(r'\s*<div class="roleview">.*?</nav></div>', '', s, count=1, flags=re.S)
    os.makedirs(os.path.join(here, d), exist_ok=True)
    io.open(os.path.join(here, d, 'index.html'), 'w', encoding='utf-8').write(s)
    print('wrote %s/index.html' % d)
