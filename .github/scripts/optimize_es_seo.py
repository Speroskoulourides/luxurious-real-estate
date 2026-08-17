from pathlib import Path

p = Path('es/index.html')
s = p.read_text(encoding='utf-8')

repls = {
' <title>SNK Real Estate | Oportunidades de Inversión Privada en Grecia</title> ': ' <title>SNK Real Estate | Inmobiliario de Lujo e Inversión en Grecia</title> ',
'  <meta name="description" content="SNK presenta oportunidades cuidadosamente seleccionadas de inversión inmobiliaria privada y hotelera en Grecia, incluyendo Mykonos, Paros y Atenas.">': '  <meta name="description" content="SNK Real Estate presenta propiedades de lujo, villas e inversiones inmobiliarias y hoteleras seleccionadas en Grecia, incluyendo Mykonos, Paros y Atenas.">',
'  <meta property="og:title" content="SNK Real Estate | Oportunidades de Inversión Privada en Grecia">': '  <meta property="og:title" content="SNK Real Estate | Inmobiliario de Lujo e Inversión en Grecia">',
'  <meta property="og:image" content="../athens-investment-en/monastiraki-view.jpg">': '  <meta property="og:image" content="https://snkrealestate.com/athens-investment-en/monastiraki-view.jpg">',
'SNK Real Estate ofrece a inversores cualificados acceso directo a oportunidades de inversión cuidadosamente seleccionadas en toda Grecia.': 'SNK Real Estate ofrece a inversores cualificados acceso directo a propiedades de lujo, villas, inversiones inmobiliarias y oportunidades hoteleras cuidadosamente seleccionadas en toda Grecia.',
'  {"@context":"https://schema.org","@type":"RealEstateAgent","name":"SNK Real Estate","url":"https://snkrealestate.com/","email":"investments@snkrealestate.com","telephone":"+30 6985 821148","areaServed":"Greece","description":"Oportunidades de inversión inmobiliaria privada y hotelera en Grecia."\n  </script>': '  {"@context":"https://schema.org","@type":"RealEstateAgent","name":"SNK Real Estate","url":"https://snkrealestate.com/","email":"investments@snkrealestate.com","telephone":"+30 6985 821148","areaServed":"Greece","description":"Inmobiliario de lujo e inversión inmobiliaria y hotelera en Grecia."}\n  </script>'
}
for old, new in repls.items():
    if s.count(old) != 1:
        raise SystemExit(f'Expected exactly one match for: {old[:100]} | found {s.count(old)}')
    s = s.replace(old, new, 1)

anchor = '  <link rel="canonical" href="https://snkrealestate.com/es/">\n'
hreflang = '''  <link rel="alternate" hreflang="en" href="https://snkrealestate.com/">\n  <link rel="alternate" hreflang="el" href="https://snkrealestate.com/el/">\n  <link rel="alternate" hreflang="fr" href="https://snkrealestate.com/fr/">\n  <link rel="alternate" hreflang="es" href="https://snkrealestate.com/es/">\n  <link rel="alternate" hreflang="x-default" href="https://snkrealestate.com/">\n'''
if hreflang not in s:
    if s.count(anchor) != 1:
        raise SystemExit(f'Expected one canonical anchor, found {s.count(anchor)}')
    s = s.replace(anchor, anchor + hreflang, 1)

p.write_text(s, encoding='utf-8')
