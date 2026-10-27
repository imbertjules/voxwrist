# Publier Voxwrist Notes 2.1 et Voxwrist Ask 2.0 (gratuites) : ce qui reste à faire (Jules)

| App | Fichier | UUID |
|---|---|---|
| Notes 2.1.0 (mise à jour) | `~/garmin-store/dist/voxwrist-notes-2.1.0-free.iq` | `51249208-8649-42a0-9b00-abebbbedab19` |
| Ask 2.0.0 (nouvelle fiche) | `~/garmin-store/dist/voxwrist-ask-2.0.0-free.iq` | `fd13665c-b9c3-4a38-a44d-6a8ffbf46dcf` |

Les deux sont signés avec ta clé développeur habituelle (`photowatchface/developer_key`). **Garde cette clé**, toute mise à jour devra être signée avec elle.
Les fichiers `*-OBSOLETE-payant.iq` sont les anciennes versions payantes : ne les envoie pas.

## 0. Activer l'e-mail (destination par défaut de Notes) : 10 minutes, gratuit
Sans cette étape, Notes affiche « e-mail pas encore actif » quand la destination est E-mail (Notion, Todoist et l'affichage sur la montre marchent quand même).
1. Crée un compte gratuit sur https://www.brevo.com (300 e-mails/jour).
2. **Expéditeurs, domaines et IP dédiées** › ajoute l'adresse d'expédition et vérifie-la. Idéal : un domaine à toi (Brevo te donne les enregistrements SPF/DKIM/DMARC à ajouter chez ton registrar). Avec une simple adresse Gmail comme expéditeur, beaucoup d'e-mails finiront en spam, voire seront refusés (DMARC de Gmail).
3. **SMTP et API** › onglet **SMTP** : note le *login SMTP* et génère une *clé SMTP*.
4. Sur le NAS, édite **`/volume1/docker/voxwrist/secrets/email.env`** (déjà créé, `chmod 600`, avec un `UNSUB_SECRET` déjà généré : ne le change pas) :
   ```
   EMAIL_MODE=smtp
   EMAIL_FROM=Voxwrist Notes <notes@ton-domaine.fr>     # l'adresse vérifiée à l'étape 2
   SMTP_USER=<login SMTP Brevo>
   SMTP_PASS=<clé SMTP Brevo>
   ```
   (variante API : `EMAIL_MODE=brevo` + `EMAIL_API_KEY=xkeysib-...` ; ou Resend : `EMAIL_MODE=resend` + `EMAIL_API_KEY=re_...`)
5. Redémarre le relais :
   `cd /volume1/docker/voxwrist/src/deploy && sudo docker compose -f docker-compose.hosted.yml up -d --force-recreate`
6. Vérifie : `https://jular.tail4e27eb.ts.net:10000/v1/health` doit afficher `"email":true`.

## 1. Page de confidentialité (une seule fois)
Pousse `~/garmin-store/voxwrist-site` sur un dépôt GitHub public › Settings › Pages › branche `main` → `https://<ton-user>.github.io/voxwrist-site/privacy.html` (elle couvre les deux apps).

## 2. Tester sur ta fēnix 8 avant d'envoyer
- Brancher la montre en USB puis `~/garmin-store/voxwrist-notes/tools/install-watch.sh` (sideload ; une app sideloadée ne reçoit pas les réglages Garmin Connect, d'où la clé de test intégrée au build local).
- Après publication, installe depuis le Store, mets ta clé et ton adresse e-mail dans Garmin Connect et fais une vraie note / une vraie question.

## 3. Envoyer sur le Store (https://apps.garmin.com/developer)
- **Notes** : ouvre la fiche existante › *Upload new version* › `voxwrist-notes-2.1.0-free.iq`. Mets à jour descriptions, mots-clés et captures avec `docs/STORE_LISTING.md` (section 1) et `store-screenshots/notes21-*.png`.
- **Ask** : *Upload an app* › `voxwrist-ask-2.0.0-free.iq`, gratuit, catégorie Outils/Productivité, textes de la section 2, icône `assets/icon-ask-500.png`, captures `store-screenshots/ask-*.png`, même URL de confidentialité.
- Notes pour le testeur : textes EN des sections. Le testeur a besoin d'une clé OpenAI ; tu peux créer une clé dédiée plafonnée à 1 $ (platform.openai.com › Limits), la donner dans les notes puis la révoquer après la revue.

## 4. Le relais (en ligne sur le NAS)
- `https://jular.tail4e27eb.ts.net:10000` (Tailscale Funnel → conteneur `voxwrist-relay` 2.1.0), adresse par défaut des deux apps.
- Mise à jour, retour arrière : `voxwrist-relay/deploy/NAS.md`. Le NAS doit rester allumé et Tailscale connecté.
