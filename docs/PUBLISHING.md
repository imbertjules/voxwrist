# Publier Voxwrist Notes et Voxwrist Ask : ce qui reste à faire (Jules)

Fichiers à envoyer :
- `~/garmin-store/dist/voxwrist-notes.iq` (UUID `51249208-8649-42a0-9b00-abebbbedab19`)
- `~/garmin-store/dist/voxwrist-ask.iq` (UUID `fd13665c-b9c3-4a38-a44d-6a8ffbf46dcf`)

Ils sont signés avec ta clé développeur habituelle (`photowatchface/developer_key`). **Garde cette clé** : toute
mise à jour future devra être signée avec la même.

## 0. Avant tout (une seule fois)
1. **Héberger la page de confidentialité.** Le Store demande une URL. Le plus simple et gratuit : pousse
   `~/garmin-store/voxwrist-site` sur un dépôt GitHub public, puis Settings › Pages › branche `main`.
   Tu obtiens `https://<ton-user>.github.io/voxwrist-site/privacy.html`. Cloudflare Pages ou Vercel marchent aussi.
   Complète d'abord l'e-mail de contact (`[à compléter]` dans `privacy.html`).
2. **Publier le relais** (dépôt GitHub public `voxwrist-relay`), car les clients doivent pouvoir l'installer.
   Mets son lien dans `index.html` (`[lien GitHub du relais]`).
3. (Optionnel) Acheter `voxwrist.com` / `voxwrist.app`. Ils étaient libres le 27/10/2026 (vérifié par RDAP, rien n'a été acheté).
   Vérifie aussi la marque sur EUIPO/INPI (non vérifié).

## 1. Compte marchand (obligatoire pour une app payante)
1. Va sur https://apps.garmin.com/developer › connecte-toi avec ton compte Garmin développeur.
2. Ouvre la partie **Merchant / Payments** (« Become a merchant ») et accepte l'accord Connect IQ Merchant.
3. Paie l'inscription marchand : **100 $ par an** (selon la doc SDK 9.3 consultée). Garmin prend **15 %** de chaque vente.
4. Renseigne ton identité, l'adresse, les coordonnées bancaires (IBAN), le statut fiscal (auto-entrepreneur : SIRET et TVA, ou franchise en base).
5. **Vérification « trader » (DSA, UE).** Pour vendre dans l'UE, déclare-toi *trader* et fournis nom, adresse, e-mail,
   téléphone et SIRET. Ces informations seront **visibles publiquement** sur la fiche. Attends la validation, qui peut prendre plusieurs jours.

## 2. Envoyer chaque app (2 fois : Notes puis Ask)
1. apps.garmin.com/developer › **Upload an app** › choisis le `.iq`.
2. Type : Watch App. Catégorie : Tools / Productivité.
3. **Titre, descriptions FR et EN, mots-clés** : copie-colle depuis `docs/STORE_LISTING.md`.
4. **Icône** : `assets/icon-notes-500.png` / `assets/icon-ask-500.png`.
5. **Captures** : `store-screenshots/notes-*.png` / `store-screenshots/ask-*.png`.
6. **URL de confidentialité** : celle de l'étape 0.
7. **Prix** : choisis l'option payante.
   - Notes : palier **4,25 $**, soit **4,99 €**.
   - Ask : palier **5,00 $**, soit **5,99 €**.
8. **Essai** : active le mode essai (*trial*) proposé pour les apps payantes. Tant que l'app n'est pas achetée,
   `AppBase.isTrial()` renvoie vrai. L'app compte alors 14 jours depuis le 1er lancement : elle affiche
   « Essai : X j restants », Garmin montre au démarrage la notification des jours restants
   (`getTrialDaysRemaining`), et à 0 jour l'app affiche « Essai terminé » et bloque l'enregistrement jusqu'à l'achat.
   Remarque : sur un build sideloadé (non signé par le Store), `isTrial()` est **toujours vrai**. C'est normal.
9. Soumets. La revue Garmin prend quelques jours. Réponds vite à leurs questions. Ils peuvent demander un relais de test :
   prépare une URL publique de démo et un jeton dédié (voir ci-dessous), que tu révoqueras après la revue.

## 3. Relais de démo pour la revue Garmin (recommandé)
- Lance le relais sur ton Mac ou un petit VPS avec un **jeton dédié** (`RELAY_TOKENS=demo-xxxx`), derrière
  Cloudflare Tunnel (`cloudflared tunnel --url http://127.0.0.1:8790`, gratuit).
- Indique l'URL et le jeton dans le champ « notes pour le testeur », puis coupe tout après la revue.

## 4. Après publication
- Teste l'achat réel sur ta fēnix 8 (installation depuis le Store, essai, puis achat).
- Les mises à jour se font en envoyant un nouveau `.iq` avec un numéro de version plus élevé (`manifest.xml`, `version="1.0"`), signé avec la même clé.
