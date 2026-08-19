from pathlib import Path

p = Path('fr/index.html')
s = p.read_text(encoding='utf-8')
marker = '<!-- SNK UNIVERSAL HEADER STYLES END -->\n'
block = '''<!-- SNK UNIVERSAL HEADER STYLES END -->
<style id="fr-corporate-geometry-test">
html{scroll-padding-top:76px!important}
body.snk-universal-header-enabled{padding-top:0!important}
.hero{height:100vh!important}
#company{min-height:calc(100vh - 76px)!important;scroll-margin-top:0!important}
@media(max-width:560px){html{scroll-padding-top:68px!important}body.snk-universal-header-enabled{padding-top:0!important}.hero{height:100vh!important}}
</style>
'''
if s.count(marker) != 1:
    raise SystemExit(f'Expected one header end marker, found {s.count(marker)}')
if 'id="fr-corporate-geometry-test"' in s:
    raise SystemExit('FR Company geometry block already exists')
s = s.replace(marker, block, 1)
p.write_text(s, encoding='utf-8')
