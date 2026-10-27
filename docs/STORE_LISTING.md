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
- **Mots-clés** : assistant, ai, chatgpt, claude, voice assistant, agent, reminders, daily brief, assistant vocal, rappels

### Description FR
Votre agent personnel, au poignet. Appuyez sur START, posez votre question, il vous répond à voix haute et à l'écran.

• Un agent vivant : un orbe animé qui écoute, réfléchit et parle ; donnez-lui un nom et une couleur.
• Brief du jour : météo, prochains rendez-vous de votre agenda, e-mails non lus, en un coup d'œil.
• Rappels à la voix : « rappelle-moi à 18 h d'appeler Paul » ; la montre vous le rappelle à l'heure dite.
• Conversation : enchaînez (« et demain ? ») sans répéter le contexte.
• 2 appuis maximum, aucun clavier, aucun appui long.

Apportez votre clé, gratuite ou payante : Google Gemini (gratuite, aistudio.google.com : réponses, et voix si disponible), Groq (gratuite, console.groq.com : réponses à l'écran) ou OpenAI (la meilleure voix, quelques centimes par jour). Anthropic Claude peut répondre, avec une clé Gemini, Groq ou OpenAI pour comprendre la voix. Sans clé OpenAI ni Gemini, la réponse s'affiche sans être lue.
Connecteurs facultatifs (réglages) : ville pour la météo, lien iCal privé de votre agenda (Google Agenda, iCloud, Outlook), boîte e-mail IMAP en lecture seule avec mot de passe d'application.
E-mail : fonctionne avec Gmail, iCloud, Yahoo, Orange et Free via un mot de passe d'application ; Outlook/Hotmail n'est pas pris en charge.
Les rappels restent sur la montre. Ni l'audio, ni les textes, ni vos clés ne sont conservés par le relais Voxwrist. Pas de compte, pas de publicité.

### Description EN
Your personal agent, on your wrist. Press START, ask, and it answers out loud and on screen.

• A living agent: an animated orb that listens, thinks and speaks; give it a name and a colour.
• Daily brief: weather, your next calendar events, unread emails, at a glance.
• Voice reminders: "remind me at 6 pm to call Paul"; the watch reminds you on time.
• Conversation: follow up ("and tomorrow?") without repeating yourself.
• 2 presses max, no keyboard, no long press.

Bring your own key, free or paid: Google Gemini (free, aistudio.google.com: answers, and voice when available), Groq (free, console.groq.com: on-screen answers) or OpenAI (best voice, a few cents a day). Anthropic Claude can answer, with a Gemini, Groq or OpenAI key to understand your voice. Without an OpenAI or Gemini key, answers are shown, not spoken.
Optional connectors (settings): weather city, private iCal link of your calendar (Google Calendar, iCloud, Outlook), read-only IMAP mailbox with an app password.
Mail: works with Gmail, iCloud, Yahoo, Orange and Free using an app password; Outlook/Hotmail is not supported.
Reminders stay on the watch. Audio, texts and keys are never stored by the Voxwrist relay. No account, no ads.

### Notes pour le testeur (reviewer notes)
EN: Needs one of the user's own API keys: Google Gemini (free), Groq (free) or OpenAI (Garmin Connect › app settings). Without one the watch shows a setup screen (an Anthropic key alone is not enough: it cannot transcribe audio). Press START, speak, press START: the answer is shown, and spoken through the watch speaker with an OpenAI or Gemini key (on watches with a speaker). Swipe up/down (or UP/DOWN) for the "Today" brief and the reminders list. Calendar/mail connectors are optional.
