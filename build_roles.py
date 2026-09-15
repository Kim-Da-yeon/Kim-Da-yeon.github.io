# -*- coding: utf-8 -*-
"""index.html 하나로 직무별 폴더(ml/ nlp/ ds/ av/)의 index.html을 재생성합니다.
사용: 저장소 루트에서  python build_roles.py
루트 index.html을 고친 뒤 이 스크립트만 다시 돌리면 4개 폴더가 갱신됩니다."""
import os, re, io

ROLES = {
    'ml':  {'name': 'ML Researcher',              'card': 'ML Researcher · 베이지안 추론'},
    'nlp': {'name': 'NLP · LLM Engineer',         'card': 'NLP · LLM Engineer · RAG'},
    'ds':  {'name': 'Data Scientist',             'card': 'Data Scientist · 데이터 분석'},
    'av':  {'name': '자율주행 AI · Data Scientist', 'card': '자율주행 AI · 데이터 분석'},
}

here = os.path.dirname(os.path.abspath(__file__))
src = io.open(os.path.join(here, 'index.html'), encoding='utf-8').read()

for key, r in ROLES.items():
    s = src
    # 1) 직무 고정 메타 (JS가 이 값을 읽어 ?role= 없이도 해당 직무로 렌더링)
    s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="role" content="%s">' % key, 1)
    # 2) 탭 제목 · OG · 상단 브랜드 · ID카드 부제
    s = s.replace('<title>김다연 · Data Scientist</title>', '<title>김다연 · %s</title>' % r['name'], 1)
    s = s.replace('<meta property="og:title" content="김다연 · Data Scientist">', '<meta property="og:title" content="김다연 · %s">' % r['name'], 1)
    s = s.replace('<meta name="description" content="김다연 · Data Scientist —', '<meta name="description" content="김다연 · %s —' % r['name'], 1)
    s = s.replace('<em>Data Scientist</em></a>', '<em>%s</em></a>' % r['name'], 1)
    s = s.replace('<span>Data Scientist · 데이터 분석</span>', '<span>%s</span>' % r['card'], 1)
    s = s.replace('<link rel="canonical" href="https://kim-da-yeon.github.io/">', '<link rel="canonical" href="https://kim-da-yeon.github.io/%s/">' % key, 1)
    s = s.replace('<meta property="og:url" content="https://kim-da-yeon.github.io/">', '<meta property="og:url" content="https://kim-da-yeon.github.io/%s/">' % key, 1)
    # 3) 직무별 페이지에서는 "다른 직무 기준으로 보기" 전환 링크 제거
    s = re.sub(r'\s*<div class="roleview">.*?</nav></div>', '', s, count=1, flags=re.S)
    os.makedirs(os.path.join(here, key), exist_ok=True)
    io.open(os.path.join(here, key, 'index.html'), 'w', encoding='utf-8').write(s)
    print('wrote %s/index.html' % key)
