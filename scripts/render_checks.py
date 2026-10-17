"""Render the article collection from its structured, source-linked record.

Run from any directory: python scripts/render_checks.py
"""
from pathlib import Path
import html
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REVIEW = '18 October 2026 (IST)'


def links(sources):
    return '<ul>' + ''.join(
        f'<li><a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">'
        f'{html.escape(label)} ↗</a></li>' for label, url in sources
    ) + '</ul>'


def render(case, number):
    e = html.escape
    table = ''
    if 'table' in case:
        t = case['table']
        table = ('<div class="evidence-table"><table><caption>' + e(t['caption'])
                 + '</caption><thead><tr>'
                 + ''.join('<th scope="col">' + e(v) + '</th>' for v in t['headers'])
                 + '</tr></thead><tbody>'
                 + ''.join('<tr>' + ''.join('<td>' + e(v) + '</td>' for v in row)
                           + '</tr>' for row in t['rows'])
                 + '</tbody></table></div>')
    history = case['history']
    historical = (
        '<section class="history" aria-label="Historical context">'
        '<h4>Historical position</h4><p class="history-scope">' + e(history['scope']) + '</p>'
        + ''.join('<p>' + e(v) + '</p>' for v in history['before_2014'])
        + '<h4>What the comparison tells us</h4><p>' + e(history['comparison']) + '</p>'
        + '<h4>Historical sources</h4>' + links(history['sources']) + '</section>'
    )
    corrections = ''.join(
        '<p class="correction"><strong>Correction, ' + e(item['date']) + ':</strong> '
        + e(item['note']) + '</p>' for item in case.get('corrections', [])
    )
    review = 'Historical context added 18 October 2026 (IST). '
    if not corrections:
        review += 'No verdict change in this update.' if case.get('batch') != '2026-10-18-history10' else 'Initial publication.'
    else:
        review += 'Correction recorded above.'
    label = (case.get('date_label', '') + ' ' + case['date']).strip()
    return (
        f'<article id="{e(case["id"])}" data-topic="{e(case["topic"])}" data-date="{case["date"]}">'
        f'<div class="article-top"><span class="number">{number:02}</span>'
        f'<span>{e(case["topic"])} / {e(case["kind"])}</span>'
        f'<time datetime="{case["date"]}">{e(label)}</time></div>'
        '<div class="article-body"><div>'
        f'<span class="verdict {case["verdict"].lower()}">{e(case["verdict"])}</span>'
        f'<h3><a href="#{e(case["id"])}">{e(case["title"])}</a></h3>'
        f'<p class="summary">{e(case["summary"])}</p></div><div>'
        '<p class="claim-label">THE CLAIM · PARAPHRASED</p>'
        f'<p class="claim">{e(case["claim"])}</p>'
        '<details><summary><span class="closed-label">Read the evidence &amp; history</span>'
        '<span class="open-label">Close evidence &amp; history</span>'
        '<span class="expand-icon" aria-hidden="true">↗</span></summary>'
        f'<h4>Context</h4><p>{e(case["context"])}</p>'
        + historical
        + f'<h4>Evidence for this claim</h4><p>{e(case["evidence"])}</p>'
        + table
        + f'<h4>Assessment</h4><p>{e(case["finding"])}</p>'
        + f'<h4>What remains unverified</h4><p>{e(case["limit"])}</p>'
        + '<h4>Claim sources</h4>' + links(case['sources']) + corrections
        + '<p class="review">' + e(review) + '</p></details></div></div></article>'
    )


def main():
    cases = json.loads((ROOT / 'data/checks.json').read_text())
    assert len({c['id'] for c in cases}) == len(cases), 'Duplicate claim ID'
    for c in cases:
        assert c['verdict'] in {'Supported', 'False', 'Misleading', 'Unverified'}
        h = c['history']
        assert h['scope'] and h['before_2014'] and h['comparison'] and h['sources']
        for _, url in c['sources'] + h['sources']:
            assert url.startswith('https://'), url
    cases.sort(key=lambda c: c['date'], reverse=True)
    page = (ROOT / 'index.html').read_text()
    page, n = re.subn(
        r'<div id="articles">.*?</article></div><p id="empty"',
        lambda _: '<div id="articles">' + ''.join(render(c, i) for i, c in enumerate(cases, 1))
                  + '</div><p id="empty"', page, flags=re.S
    )
    assert n == 1, 'Article container missing or repeated'
    page = re.sub(r'<b>\d+</b> fact checks', f'<b>{len(cases)}</b> fact checks', page)
    page = re.sub(r'(<p id="count" role="status">).*?(</p>)',
                  lambda m: m[1] + f'{len(cases)} checks · Statement or source dates shown below · Reviewed {REVIEW}' + m[2], page)
    page = re.sub(r'(<select id="topic">).*?(</select>)',
                  lambda m: m[1] + '<option value="">All topics</option>'
                  + ''.join('<option>' + html.escape(t) + '</option>' for t in sorted({c['topic'] for c in cases}))
                  + m[2], page, flags=re.S)
    for tag, filename in [('style', 'styles.css'), ('script', 'app.js')]:
        content = (ROOT / filename).read_text()
        page = re.sub(f'<{tag}>.*?</{tag}>', lambda _: f'<{tag}>' + content + f'</{tag}>', page, flags=re.S)
    (ROOT / 'index.html').write_text(page)
    print(f'Rendered {len(cases)} checks with historical context.')


if __name__ == '__main__':
    main()
