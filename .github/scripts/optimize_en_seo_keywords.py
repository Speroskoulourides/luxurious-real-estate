from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
repls = {
'  <title>SNK Real Estate | Private Investment Opportunities in Greece</title>': '  <title>SNK Real Estate | Luxury Real Estate & Investment Properties in Greece</title>',
'  <meta name="description" content="SNK Real Estate presents selected private real estate and hospitality investment opportunities in Greece, including Mykonos, Paros and Athens.">': '  <meta name="description" content="SNK Real Estate presents selected luxury real estate, luxury homes, villas and investment properties in Greece, including Mykonos, Paros and Athens.">',
'<p class="lead">SNK Real Estate provides qualified investors with direct access to carefully selected investment opportunities across Greece.</p>': '<p class="lead">SNK Real Estate provides qualified investors with direct access to carefully selected luxury real estate, investment properties and hospitality opportunities across Greece.</p>'
}
for old, new in repls.items():
    if s.count(old) != 1:
        raise SystemExit(f'Expected exactly one match for: {old[:80]} | found {s.count(old)}')
    s = s.replace(old, new, 1)
p.write_text(s, encoding='utf-8')
