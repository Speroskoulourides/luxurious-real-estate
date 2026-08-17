from pathlib import Path

p = Path('es/index.html')
s = p.read_text(encoding='utf-8')
marker = '#company{min-height:calc(100vh - 76px)!important;scroll-margin-top:0!important}\n'
insert = marker + '#opportunities{scroll-margin-top:0!important}\n'
if s.count(marker) != 1:
    raise SystemExit(f'Expected one ES Company rule, found {s.count(marker)}')
if '#opportunities{scroll-margin-top:0!important}' in s:
    raise SystemExit('ES Opportunities anchor rule already exists')
s = s.replace(marker, insert, 1)
p.write_text(s, encoding='utf-8')
