from pathlib import Path

p = Path('es/index.html')
s = p.read_text(encoding='utf-8')
marker = '<!-- SNK UNIVERSAL HEADER STYLES END -->\n'
if s.count(marker) != 1:
    raise SystemExit(f'Expected one universal header end marker, found {s.count(marker)}')
if 'id="es-corporate-geometry-test"' in s:
    raise SystemExit('ES geometry block already exists')
block = marker + '<style id="es-corporate-geometry-test">\n' \
    + 'html{scroll-padding-top:76px!important}\n' \
    + 'body.snk-universal-header-enabled{padding-top:0!important}\n' \
    + '.hero{height:100vh!important}\n' \
    + '#company{min-height:calc(100vh - 76px)!important;scroll-margin-top:0!important}\n' \
    + '@media(max-width:560px){html{scroll-padding-top:68px!important}body.snk-universal-header-enabled{padding-top:0!important}.hero{height:100vh!important}}\n' \
    + '</style>\n'
s = s.replace(marker, block, 1)
p.write_text(s, encoding='utf-8')
