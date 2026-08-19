from pathlib import Path

p = Path('el/index.html')
s = p.read_text(encoding='utf-8')

old_title = '  <title>SNK Real Estate | Ελλάδα</title>\n'
new_head = '''  <title>SNK Real Estate | Πολυτελή Ακίνητα & Επενδυτικά Έργα στην Ελλάδα</title>\n  <meta name="description" content="Η SNK Real Estate παρουσιάζει επιλεγμένα πολυτελή ακίνητα, κατοικίες, βίλες και επενδυτικά έργα στην Ελλάδα, με έμφαση σε Μύκονο, Πάρο και Αθήνα.">\n  <meta name="robots" content="index,follow,max-image-preview:large">\n  <link rel="canonical" href="https://snkrealestate.com/el/">\n  <link rel="alternate" hreflang="en" href="https://snkrealestate.com/">\n  <link rel="alternate" hreflang="el" href="https://snkrealestate.com/el/">\n  <link rel="alternate" hreflang="fr" href="https://snkrealestate.com/fr/">\n  <link rel="alternate" hreflang="es" href="https://snkrealestate.com/es/">\n  <link rel="alternate" hreflang="x-default" href="https://snkrealestate.com/">\n'''
if s.count(old_title) != 1:
    raise SystemExit(f'Expected one EL title, found {s.count(old_title)}')
s = s.replace(old_title, new_head, 1)

old_lead = '<p class="lead">Η SNK Real Estate προσφέρει σε επιλεγμένους επενδυτές άμεση πρόσβαση σε προσεκτικά επιλεγμένα επενδυτικά έργα σε όλη την Ελλάδα.</p>'
new_lead = '<p class="lead">Η SNK Real Estate προσφέρει σε επιλεγμένους επενδυτές άμεση πρόσβαση σε πολυτελή ακίνητα, επενδυτικά έργα και ξενοδοχειακές επενδύσεις σε όλη την Ελλάδα.</p>'
if s.count(old_lead) != 1:
    raise SystemExit(f'Expected one EL hero lead, found {s.count(old_lead)}')
s = s.replace(old_lead, new_lead, 1)

p.write_text(s, encoding='utf-8')
