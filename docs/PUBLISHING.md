# Publier Voxwrist Notes 2.0.0 (gratuite) : ce qui reste à faire (Jules)

Fichier à envoyer : `~/garmin-store/dist/voxwrist-notes-2.0.0-free.iq` (UUID `51249208-8649-42a0-9b00-abebbbedab19`, 23 montres avec micro).
Il est signé avec ta clé développeur habituelle (`photowatchface/developer_key`). **Garde cette clé** : toute mise à jour devra être signée avec la même.
Voxwrist Ask est **en pause** : ne l'envoie pas (`dist/voxwrist-ask.iq` est l'ancienne version payante).

## 0. Une seule fois
1. **Héberger la page de confidentialité** (le Store demande une URL). Gratuit : pousse `~/garmin-store/voxwrist-site` sur un dépôt GitHub public › Settings › Pages › branche `main`. Tu obtiens `https://<ton-user>.github.io/voxwrist-site/privacy.html`.
2. Ajoute une adresse de contact sur la page si tu veux (pas obligatoire pour une app gratuite).

## 1. Envoyer l'app (pas de compte marchand : elle est gratuite)
1. https://apps.garmin.com/developer › connexion › **Upload an app** › `voxwrist-notes-2.0.0-free.iq`.
2. Type Watch App, catégorie Outils / Productivité, prix **gratuit**.
3. Titre, descriptions FR/EN et mots-clés : copier-coller depuis `docs/STORE_LISTING.md`.
4. Icône `assets/icon-notes-500.png`, captures `store-screenshots/notes-*.png`, URL de confidentialité de l'étape 0.
5. Champ « notes pour le testeur » : le texte EN de `STORE_LISTING.md`. Le testeur a besoin d'une clé OpenAI. Sans clé il verra l'écran de configuration, ce que Garmin accepte en général pour une appli « apportez votre clé ». Si tu veux, crée une clé dédiée avec un plafond de 1 $ (platform.openai.com › Limits), mets-la dans les notes, puis révoque-la après la revue.
6. Soumets. La revue prend quelques jours.

## 2. Le relais (déjà en ligne sur le NAS)
- URL publique : `https://jular.tail4e27eb.ts.net:10000` (Tailscale Funnel → conteneur `voxwrist-relay` sur `jular`). C'est l'adresse par défaut de l'app.
- Santé : `https://jular.tail4e27eb.ts.net:10000/v1/health`.
- Mise à jour et retour arrière : `voxwrist-relay/deploy/NAS.md`.
- Le NAS doit rester allumé et Tailscale connecté, sinon l'app affiche « Erreur serveur » ou « Pas de réponse ».

## 3. Après publication
- Installe-la depuis le Store sur ta fēnix 8, colle ta clé dans Garmin Connect, fais une vraie note.
- Mise à jour : augmente `version` dans `manifest.xml`, `./build.sh export`, envoie le nouveau `.iq`.
