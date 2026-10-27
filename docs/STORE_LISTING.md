# Fiche Connect IQ Store : Voxwrist Notes (gratuite)

- **Nom** : Voxwrist Notes
- **Type** : Watch App · **Catégorie** : Outils / Productivité · **Prix** : gratuit (pas de compte marchand, pas d'essai)
- **Fichier** : `~/garmin-store/dist/voxwrist-notes-2.0.0-free.iq` (version 2.0.0, UUID `51249208-8649-42a0-9b00-abebbbedab19`)
- **Icône** : `assets/icon-notes-500.png`
- **Captures** (416×416, fēnix 8 43 mm) : `store-screenshots/notes-1-ready-*.png`, `notes-2-recording-*.png`, `notes-3-sent-*.png`, `notes-4-error-en.png`, `notes-5-setup-fr.png`
- **Confidentialité** : URL publique de `privacy.html`
- **Mots-clés** : voice notes, dictation, transcription, whisper, openai, todoist, ntfy, notion, memo, dictée, note vocale

## Description FR

Dictez une note depuis votre poignet en deux appuis : START, parlez, START.

Voxwrist Notes enregistre votre voix avec le micro de la montre, la fait transcrire par OpenAI (Whisper) avec VOTRE clé API, puis :
• affiche le texte sur la montre ;
• l'envoie en notification sur votre téléphone (appli gratuite ntfy) ;
• crée une tâche Todoist ;
• ou l'envoie à n'importe quel webhook https (Notion, Zapier, Make, n8n… y compris par e-mail via Zapier/Make).

Pensé pour la montre : gros bouton, états clairs (prêt, enregistrement avec minuteur, envoi, envoyé, erreur avec la cause et la solution), français et anglais, aucun clavier, aucun appui long.

Sans connexion ? La note est gardée sur la montre (jusqu'à 5) et part toute seule au retour du téléphone.

Réglages (dans l'appli Garmin Connect › Applis Connect IQ › Voxwrist Notes › Réglages) :
• Clé API OpenAI (obligatoire, créez-la sur platform.openai.com ; la transcription vous coûte environ 0,006 $ par minute chez OpenAI) ;
• Modèle : whisper-1 ou gpt-4o-mini-transcribe ;
• Langue : automatique, français ou anglais ;
• Destinations facultatives : sujet ntfy, jeton Todoist, URL webhook ;
• Durée max (15 à 120 s).

Confidentialité : ni l'audio, ni le texte, ni votre clé ne sont stockés ou journalisés par le relais Voxwrist. Pas de compte, pas de publicité, pas de traceur.

Nécessite une montre Garmin avec micro (Connect IQ 6.0.3 ou plus récent) connectée à l'appli Garmin Connect.

## Description EN

Dictate a note from your wrist in two presses: START, speak, START.

Voxwrist Notes records your voice with the watch microphone, has it transcribed by OpenAI (Whisper) using YOUR own API key, then:
• shows the text on the watch;
• pushes it to your phone as a notification (free ntfy app);
• creates a Todoist task;
• or posts it to any https webhook (Notion, Zapier, Make, n8n… including e-mail through Zapier/Make).

Built for the wrist: big record button, clear states (ready, recording with timer, sending, sent, error with cause and fix), English and French, no keyboard, no long press.

Offline? The note is kept on the watch (up to 5) and sent automatically when the phone is back.

Settings (Garmin Connect app › Connect IQ apps › Voxwrist Notes › Settings):
• OpenAI API key (required, create one at platform.openai.com; transcription costs about $0.006 per minute at OpenAI);
• Model: whisper-1 or gpt-4o-mini-transcribe;
• Language: automatic, French or English;
• Optional destinations: ntfy topic, Todoist token, webhook URL;
• Max duration (15–120 s).

Privacy: audio, text and your key are never stored or logged by the Voxwrist relay. No account, no ads, no trackers.

Requires a Garmin watch with a microphone (Connect IQ 6.0.3+) paired with the Garmin Connect app.

## Notes pour le testeur Garmin (champ « reviewer notes »)

EN: The app needs the user's own OpenAI API key (Garmin Connect › app settings › "OpenAI API key"). Without a key the watch shows a setup screen. With an invalid key it shows "OpenAI key rejected". Optional destinations: ntfy topic (install the ntfy phone app and subscribe to the same topic), Todoist API token, https webhook. Relay: https://jular.tail4e27eb.ts.net:10000/v1/health
