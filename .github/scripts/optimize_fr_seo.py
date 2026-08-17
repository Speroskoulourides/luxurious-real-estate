from pathlib import Path

p = Path('fr/index.html')
s = p.read_text(encoding='utf-8')

repls = {
'<title>SNK Real Estate | Opportunités d’investissement privé en Grèce</title>': '<title>SNK Real Estate | Immobilier de Luxe & Investissement en Grèce</title>',
'<meta content="SNK Real Estate présente une sélection d’opportunités d’investissement immobilier privé et hôtelier en Grèce, notamment à Mykonos, Paros et Athènes." name="description"/>': '<meta content="SNK Real Estate présente une sélection de biens immobiliers de luxe, villas et investissements immobiliers et hôteliers en Grèce, notamment à Mykonos, Paros et Athènes." name="description"/>',
'<link href="https://snkrealestate.com/" rel="canonical"/>': '<link href="https://snkrealestate.com/fr/" rel="canonical"/>',
'<meta content="SNK Real Estate | Opportunités d’investissement privé en Grèce" property="og:title"/>': '<meta content="SNK Real Estate | Immobilier de Luxe & Investissement en Grèce" property="og:title"/>',
'<meta content="https://snkrealestate.com/" property="og:url"/>': '<meta content="https://snkrealestate.com/fr/" property="og:url"/>',
'<meta content="athens-investment-fr/index.htmlmonastiraki-view.jpg" property="og:image"/>': '<meta content="https://snkrealestate.com/athens-investment-fr/monastiraki-view.jpg" property="og:image"/>',
'    SNK Real Estate offre aux investisseurs qualifiés un accès direct à des opportunités d’investissement soigneusement sélectionnées à travers la Grèce.': '    SNK Real Estate offre aux investisseurs qualifiés un accès direct à une sélection de biens immobiliers de luxe, villas, investissements immobiliers et opportunités hôtelières à travers la Grèce.'
}
for old, new in repls.items():
    if s.count(old) != 1:
        raise SystemExit(f'Expected exactly one match for: {old[:90]} | found {s.count(old)}')
    s = s.replace(old, new, 1)

anchor = '<link href="https://snkrealestate.com/fr/" rel="canonical"/>\n'
hreflang = '''<link href="https://snkrealestate.com/" hreflang="en" rel="alternate"/>\n<link href="https://snkrealestate.com/el/" hreflang="el" rel="alternate"/>\n<link href="https://snkrealestate.com/fr/" hreflang="fr" rel="alternate"/>\n<link href="https://snkrealestate.com/es/" hreflang="es" rel="alternate"/>\n<link href="https://snkrealestate.com/" hreflang="x-default" rel="alternate"/>\n'''
if hreflang not in s:
    if s.count(anchor) != 1:
        raise SystemExit(f'Expected one canonical anchor, found {s.count(anchor)}')
    s = s.replace(anchor, anchor + hreflang, 1)

p.write_text(s, encoding='utf-8')
