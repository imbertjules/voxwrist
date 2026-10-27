# Fiches Connect IQ Store (gratuites, BYOK)

---------------------------------------------------------------------------------------------------
## 1. Voxwrist Notes 2.1

- **Nom** : Voxwrist Notes · **Type** : Watch App · **Catégorie** : Outils / Productivité · **Prix** : gratuit
- **Fichier** : `~/garmin-store/dist/voxwrist-notes-2.1.0-free.iq` (version 2.1.0, UUID `51249208-8649-42a0-9b00-abebbbedab19`, mise à jour de la 2.0)
- **Icône** : `assets/icon-notes-500.png`
- **Captures** : `store-screenshots/notes21-*.png` (416×416 fēnix 8, 390×390 Venu 4, 454×454 FR570)
- **Confidentialité** : https://imbertjules.github.io/voxwrist/privacy.html (site : https://imbertjules.github.io/voxwrist/)
- **Mots-clés** : voice notes, dictation, transcription, email, notion, todoist, memo, dictée, note vocale, e-mail

### Description FR
Dictez une note depuis votre poignet en deux appuis : START, parlez, START. Elle arrive dans votre boîte e-mail.

Voxwrist Notes enregistre votre voix avec le micro de la montre, la fait transcrire avec VOTRE clé API (OpenAI, ou une clé gratuite Groq ou Google Gemini), affiche le texte sur la montre et l'envoie où vous voulez :
• E-mail (par défaut) : indiquez simplement votre adresse ;
• Notion : une nouvelle page (ou une ligne de base de données) ;
• Todoist : une nouvelle tâche ;
• Autre (lien) : pour les utilisateurs avancés (Zapier, Make, n8n…).

Pensé pour la montre : un gros bouton, des états clairs (prêt, enregistrement, envoi, envoyée, erreur avec la cause et la solution), français et anglais, aucun clavier, aucun appui long.
Sans connexion ? La note est gardée sur la montre (jusqu'à 5) et part toute seule au retour du téléphone.

Réglages (appli Garmin Connect › Applis Connect IQ › Voxwrist Notes › Réglages) :
• Une clé de transcription au choix : Groq (gratuite, console.groq.com), Google Gemini (gratuite, aistudio.google.com) ou OpenAI (platform.openai.com ; environ 0,006 $ par minute d'audio) ;
• Destination : E-mail, Notion, Todoist ou Autre (lien) ;
• Votre adresse e-mail, ou le jeton Notion + le lien de la page, ou le jeton Todoist ;
• Langue, durée maximale.

Chaque e-mail contient un lien de désinscription. Ni l'audio, ni le texte, ni vos clés ne sont conservés par le relais Voxwrist. Pas de compte, pas de publicité, pas de traceur.
Nécessite une montre Garmin avec micro (Connect IQ 6.0.3+) connectée à l'appli Garmin Connect.

### Description EN
Dictate a note from your wrist in two presses: START, speak, START. It lands in your inbox.

Voxwrist Notes records your voice with the watch microphone, has it transcribed using YOUR own API key (OpenAI, or a free Groq or Google Gemini key), shows the text on the watch and sends it where you want:
• Email (default): just enter your address;
• Notion: a new page (or database row);
• Todoist: a new task;
• Other (link): for power users (Zapier, Make, n8n…).

Built for the wrist: one big button, clear states (ready, recording, sending, sent, error with cause and fix), English and French, no keyboard, no long press.
Offline? The note is kept on the watch (up to 5) and sent automatically when the phone is back.

Settings (Garmin Connect app › Connect IQ apps › Voxwrist Notes › Settings): one transcription key: Groq (free, console.groq.com), Google Gemini (free, aistudio.google.com) or OpenAI (about $0.006 per audio minute), destination, your email address or Notion token + page link or Todoist token, language, max duration.

Every email has an unsubscribe link. Audio, text and keys are never stored by the Voxwrist relay. No account, no ads, no trackers.
Requires a Garmin watch with a microphone (Connect IQ 6.0.3+) paired with the Garmin Connect app.

### Notes pour le testeur (reviewer notes)
EN: Needs one of the user's own API keys: OpenAI, Groq (free) or Google Gemini (free) (Garmin Connect › app settings). Without a key the watch shows a setup screen. Default destination is Email: enter any address you own in "Your email address"; the note arrives from the Voxwrist sender with an unsubscribe link. Notion (integration token + page link) and Todoist (API token) are optional. Relay health: https://jular.tail4e27eb.ts.net:10000/v1/health

---------------------------------------------------------------------------------------------------
## 2. Voxwrist Ask 2.0.1

- **Nom** : Voxwrist Ask · **Type** : Watch App · **Catégorie** : Outils / Productivité · **Prix** : gratuit
- **Fichier** : `~/garmin-store/voxwrist-ask/dist/voxwrist-ask-2.0.1.iq` (version 2.0.1, UUID `fd13665c-b9c3-4a38-a44d-6a8ffbf46dcf`, 26 appareils avec micro — export 26/26, 23 modèles du manifeste dont certains en plusieurs variantes ; mise à jour de la 2.0.0)
- **Icône (couverture 500×500)** : `assets-v2/voxwrist-ask-cover-500.png`
- **Hero (1440×720)** : FR `assets-v2/voxwrist-ask-hero-1440x720-fr.jpg` · EN `assets-v2/voxwrist-ask-hero-1440x720-en.jpg`
- **Galerie FR (5 JPG)** : `assets-v2/voxwrist-ask-screenshot-1-ask-voice-fr.jpg`, `-2-daily-brief-fr.jpg`, `-3-voice-reminders-fr.jpg`, `-4-follow-up-fr.jpg`, `-5-live-orb-fr.jpg`
- **Galerie EN (5 JPG)** : `assets-v2/voxwrist-ask-screenshot-1-ask-voice-en.jpg`, `-2-daily-brief-en.jpg`, `-3-voice-reminders-en.jpg`, `-4-follow-up-en.jpg`, `-5-live-orb-en.jpg`
- **Mots-clés** : assistant IA, AI assistant, voice assistant, assistant vocal, IA, AI, OpenAI, Gemini, Claude, Groq, email, e-mail, calendar, agenda, météo, weather, reminders, rappels, daily brief
- **Accroche (1re ligne de la description)** : FR « Assistant IA vocal au poignet : posez vos questions, écoutez la réponse, retrouvez vos e-mails, votre agenda et la météo. » · EN “AI voice assistant on your wrist: ask anything, hear the answer, and check your emails, calendar and weather.” (le Store Connect IQ n'a pas de champ sous-titre : le titre reste « Voxwrist Ask »)

### Description FR
Assistant IA vocal au poignet : posez vos questions, écoutez la réponse, retrouvez vos e-mails, votre agenda et la météo.

Appuyez sur START, parlez, appuyez sur START : la réponse s'affiche à l'écran et elle est lue à voix haute (avec une clé OpenAI ou Gemini).

CE QUE FAIT VOXWRIST ASK
• Assistant vocal IA : posez n'importe quelle question à la voix, réponse à l'écran et à voix haute.
• Brief du jour à l'ouverture : météo de votre ville, rendez-vous restants de la journée, nombre d'e-mails non lus avec les derniers expéditeurs et objets.
• Rappels à la voix : « rappelle-moi à 18 h d'appeler Paul » ; la montre vous prévient à l'heure dite.
• Questions de suivi : enchaînez (« et demain ? ») sans tout répéter.
• Un orbe animé qui écoute, réfléchit et parle ; donnez-lui un nom et une couleur (Aurore, Lagon, Braise).
• 2 appuis maximum, aucun clavier, aucun appui long.

FONCTIONNE AVEC VOS E-MAILS, VOTRE AGENDA ET LA MÉTÉO
Réglages facultatifs (appli Garmin Connect › Applis Connect IQ › Voxwrist Ask › Réglages) :
• Météo : entrez votre ville (par exemple Paris).
• Agenda : collez le lien iCal privé de votre agenda Google Agenda, iCloud ou Outlook.
• E-mails : votre adresse et un mot de passe d'application (accès IMAP en lecture seule). Fonctionne avec Gmail, iCloud, Yahoo, Orange et Free. Les e-mails Outlook/Hotmail ne sont pas pris en charge.

VOTRE CLÉ IA, GRATUITE OU PAYANTE
• Google Gemini : gratuite (aistudio.google.com), réponses, et voix si disponible.
• Groq : gratuite (console.groq.com), réponses à l'écran.
• OpenAI : la meilleure voix, quelques centimes par jour.
• Anthropic Claude : pour les réponses, avec une clé Gemini, Groq ou OpenAI pour comprendre la voix.
Sans clé OpenAI ni Gemini, la réponse s'affiche sans être lue.

CONFIDENTIALITÉ
• Ni l'audio, ni les textes, ni vos clés ne sont conservés par le relais Voxwrist.
• Boîte e-mail lue en lecture seule ; les rappels restent sur la montre.
• Pas de compte, pas de publicité.

Nécessite une montre Garmin avec micro, associée à l'appli Garmin Connect.

### Description EN
AI voice assistant on your wrist: ask anything, hear the answer, and check your emails, calendar and weather.

Press START, speak, press START: the answer appears on screen and is read out loud (with an OpenAI or Gemini key).

WHAT VOXWRIST ASK DOES
• AI voice assistant: ask any question by voice, get the answer on screen and out loud.
• Daily brief at launch: weather for your city, today's remaining calendar events, unread email count with the latest senders and subjects.
• Voice reminders: "remind me at 6 pm to call Paul"; the watch alerts you on time.
• Follow-up questions: keep going ("and tomorrow?") without repeating yourself.
• An animated orb that listens, thinks and speaks; give it a name and a colour (Aurore, Lagon, Braise).
• 2 presses max, no keyboard, no long press.

WORKS WITH YOUR EMAILS, CALENDAR AND WEATHER
Optional settings (Garmin Connect app › Connect IQ apps › Voxwrist Ask › Settings):
• Weather: enter your city (for example Paris).
• Calendar: paste the private iCal link of your Google Calendar, iCloud or Outlook calendar.
• Email: your address and an app password (read-only IMAP access). Works with Gmail, iCloud, Yahoo, Orange and Free. Outlook/Hotmail mail is not supported.

YOUR AI KEY, FREE OR PAID
• Google Gemini: free (aistudio.google.com), answers, and voice when available.
• Groq: free (console.groq.com), on-screen answers.
• OpenAI: best voice, a few cents a day.
• Anthropic Claude: for answers, with a Gemini, Groq or OpenAI key to understand your voice.
Without an OpenAI or Gemini key, answers are shown, not spoken.

PRIVACY
• Audio, texts and keys are never stored by the Voxwrist relay.
• Mailbox is read-only; reminders stay on the watch.
• No account, no ads.

Requires a Garmin watch with a microphone, paired with the Garmin Connect app.

### Notes pour le testeur (reviewer notes)
EN: Needs one of the user's own API keys: Google Gemini (free), Groq (free) or OpenAI (Garmin Connect › app settings). Without one the watch shows a setup screen (an Anthropic key alone is not enough: it cannot transcribe audio). Press START, speak, press START: the answer is shown, and spoken through the watch speaker with an OpenAI or Gemini key (on watches with a speaker). Swipe up/down (or UP/DOWN) for the "Today" brief and the reminders list. Calendar/mail connectors are optional.
