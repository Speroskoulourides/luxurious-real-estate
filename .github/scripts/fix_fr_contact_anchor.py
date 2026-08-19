from pathlib import Path

p = Path('fr/index.html')
s = p.read_text(encoding='utf-8')
marker = '#approach{scroll-margin-top:0!important}\n'
insert = marker + '#contact{scroll-margin-top:0!important}\n'
if s.count(marker) != 1:
    raise SystemExit(f'Expected one FR Approach rule, found {s.count(marker)}')
if '#contact{scroll-margin-top:0!important}' in s:
    raise SystemExit('FR Contact anchor rule already exists')
s = s.replace(marker, insert, 1)
p.write_text(s, encoding='utf-8')
