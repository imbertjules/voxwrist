"""Vérifications de contenu T28 (guide / fiche Store / confidentialité / rewrite).

Usage : python3 tests/test_t28_content.py            (le dépôt entier)
        python3 tests/test_t28_content.py <dossier>  (une autre copie, pour comparer)

Chaque contrôle est une assertion sur le texte publié : trois destinations, adresse des rappels
et sa confirmation, limite des 5 minutes, annulation à la voix en mode e-mail seul, échec d'e-mail
avec rappel conservé, FR/EN de même structure, aucun secret ni e-mail personnel, rewrite /v1 intact.
Sort en 1 si un contrôle échoue, et affiche le compte des contrôles.
"""
import os
import re
import sys
from html.parser import HTMLParser

VOID = {'area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link',
        'meta', 'param', 'source', 'track', 'wbr'}
ROOT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
checks = []


def read(p):
    with open(os.path.join(ROOT, p), encoding='utf-8') as f:
        return f.read().replace('&nbsp;', ' ').replace('\u00a0', ' ')


def ck(label, cond):
    checks.append((label, bool(cond)))


class P(HTMLParser):
    def __init__(s):
        super().__init__(convert_charrefs=True)
        s.stack, s.err, s.ids, s.hrefs = [], [], set(), []

    def handle_starttag(s, t, a):
        d = dict(a)
        if 'id' in d:
            s.ids.add(d['id'])
        if t == 'a' and 'href' in d:
            s.hrefs.append(d['href'])
        if t not in VOID:
            s.stack.append(t)

    def handle_endtag(s, t):
        if t in VOID:
            return
        if s.stack and s.stack[-1] == t:
            s.stack.pop()
        elif t in s.stack:
            s.err.append('mal imbrique %s' % t)
            del s.stack[len(s.stack) - 1 - s.stack[::-1].index(t):]
        else:
            s.err.append('fermeture %s sans ouverture' % t)


pages = {}
for f in ('index.html', 'guide.html', 'privacy.html'):
    p = P()
    p.feed(read(f))
    pages[f] = p
    ck('HTML equilibre : %s' % f, not p.err and not p.stack)

g = read('guide.html')
s = read('docs/STORE_LISTING.md')
pv = read('privacy.html')
idx = read('index.html')
fr, en = g.split('<hr id="en">')

# liens internes
for h in pages['guide.html'].hrefs:
    if h.startswith('#'):
        ck('ancre %s existe dans le guide' % h, h[1:] in pages['guide.html'].ids)
    elif not h.startswith(('http', 'mailto')):
        ck('cible %s existe' % h, os.path.exists(os.path.join(ROOT, h.split('#')[0])))
ck("l'accueil FR pointe vers guide.html", 'href="guide.html"' in idx)
ck("l'accueil EN pointe vers guide.html#en", 'href="guide.html#en"' in idx)
ck('le guide revient vers index.html', 'href="index.html"' in g)
ck('le guide pointe vers privacy.html', 'href="privacy.html"' in g)

# trois destinations, FR et EN
for lab, part in (('FR', fr), ('EN', en)):
    ck('3 destinations (%s) : montre seule' % lab,
       ('sur la montre seulement' in part.lower() if lab == 'FR' else 'watch only' in part.lower()))
    ck('3 destinations (%s) : montre + e-mail' % lab,
       ('montre + e-mail calendrier' in part.lower() if lab == 'FR'
        else 'watch + calendar email' in part.lower()))
    ck('3 destinations (%s) : e-mail seul' % lab,
       ('e-mail calendrier seulement' in part.lower() if lab == 'FR'
        else 'calendar email only' in part.lower()))
    ck('repli adresse des notes (%s)' % lab,
       ('adresse des notes' in part if lab == 'FR' else 'notes email address' in part))
    ck('confirmation par lien 30 min (%s)' % lab,
       ('confirmation' in part and '30' in part) if lab == 'FR'
       else ('confirmation email' in part and '30' in part))
    ck('limite Garmin 5 minutes (%s)' % lab,
       '5 minutes' in part if lab == 'FR' else '5 minutes' in part)
    ck('message rappel court FR exact' if lab == 'FR' else 'message rappel court EN exact',
       ('Moins de 5 min : peut sonner jusqu\'à 5 min plus tard' in part) if lab == 'FR'
       else ('Under 5 min: may ring up to 5 min late' in part))
    ck('deplacement sans doublon (%s)' % lab,
       ('jamais dupliqué' in part) if lab == 'FR' else ('never duplicated' in part))
    ck('annulation a la voix (%s)' % lab,
       ('Annule le rappel' in part) if lab == 'FR' else ('Cancel the reminder' in part))
    ck('annulation en mode e-mail seul (%s)' % lab,
       ('mode e-mail seul' in part.lower()) if lab == 'FR' else ('email only' in part.lower()))
    ck('rappel retenu 40 jours (%s)' % lab,
       ('40' in part) if lab == 'FR' else ('40 days' in part))
    ck('echec e-mail : rappel garde (%s)' % lab,
       ('Rappel gardé' in part and 'reste sur la montre' in part) if lab == 'FR'
       else ('Reminder kept' in part and 'stays on the watch' in part))
    ck('aucune promesse « stocké sur la montre seulement » (%s)' % lab,
       'uniquement sur la montre' not in part if lab == 'FR'
       else 'on the watch only' not in part)

ck('sections FR = sections EN', fr.count('<section') == en.count('<section') == 7)
ck('le guide ne dit jamais « agent »', 'agent' not in g.lower())
ck('le guide ne contient aucun mailto', 'mailto:' not in g)
ck('le guide ne contient aucun e-mail', not re.search(r'[\w.+-]+@[\w-]+\.[a-z]{2,}', g))

# fiche Store
ck('fiche Store : description FR a jour', 'Trois destinations au choix' in s)
ck('fiche Store : description EN a jour', 'Three destinations' in s)
ck('fiche Store : limite des 5 minutes FR', 'jusqu\'à 5 minutes plus tard' in s)
ck('fiche Store : limite des 5 minutes EN', 'up to 5 minutes late' in s)
ck('fiche Store : jamais « agent »', ' agent ' not in s.lower())
ck('fiche Store : aucun e-mail personnel', not re.search(r'[\w.+-]+@[\w-]+\.[a-z]{2,}', s))
ck('fiche Store : etat = prochaine version', 'prochaine mise à jour' in s)
ck('fiche Store : ne pretend pas 2.0.6', 'rappels de la 2.0.6' not in s)

# confidentialite
ck('confidentialite : relais nomme pour les rappels', 'passent par le relais' in pv)
ck('confidentialite : fournisseur d\'e-mail nomme', 'Brevo' in pv)
ck('confidentialite : texte et heure du rappel', 'texte et l\'heure du rappel' in pv)
ck('confidentialite : phrase fausse supprimee', 'stockés uniquement sur la montre' not in pv)
ck('confidentialite : pas de version non publiee affirmee', 'Ask 2.0.6' not in pv)
ck('confidentialite : EN coherent', 'reminder text and time go through the relay' in pv)

# rewrite vercel
vz = read('vercel.json')
ck('rewrite /v1 conserve', '"/v1/:path*"' in vz and 'voxwrist-relay.vercel.app' in vz)

# aucun secret dans les fichiers touches
joined = g + s + pv + idx + vz
ck('aucune cle ou secret', not re.search(
    r'((?<![A-Za-z])sk-[A-Za-z0-9]{10,}|api[_-]?key\s*=\s*["\'][^"\']{8,}|xkeysib-|BEGIN [A-Z ]*PRIVATE KEY)', joined, re.I))

bad = [x for x in checks if not x[1]]
for label, ok in checks:
    if not ok:
        print('ECHEC :', label)
print('%d controles, %d echec(s)' % (len(checks), len(bad)))
sys.exit(1 if bad else 0)
