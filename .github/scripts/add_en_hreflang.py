from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '  <link rel="canonical" href="https://snkrealestate.com/">\n'
block = marker + '  <link rel="alternate" hreflang="en" href="https://snkrealestate.com/">\n  <link rel="alternate" hreflang="el" href="https://snkrealestate.com/el/">\n  <link rel="alternate" hreflang="fr" href="https://snkrealestate.com/fr/">\n  <link rel="alternate" hreflang="es" href="https://snkrealestate.com/es/">\n  <link rel="alternate" hreflang="x-default" href="https://snkrealestate.com/">\n'
if s.count(marker) != 1:
    raise SystemExit(f'Expected one EN canonical, found {s.count(marker)}')
if 'hreflang="en"' in s:
    raise SystemExit('EN hreflang already exists')
s = s.replace(marker, block, 1)
p.write_text(s, encoding='utf-8')
