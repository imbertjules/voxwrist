from lib import *
O='/workspace/voxstore/assets-v2/'
T=400; G=28; W=5*T+6*G
H=120+ (360+70) + 2*(T+70) + 40
cs=Image.new('RGB',(W,H),(14,11,32)); d=ImageDraw.Draw(cs)
d.text((G,36),'Voxwrist Ask — Connect IQ Store assets v2',font=font('head',44,'Bold'),fill=(255,255,255))
lab=font('body',20,'Medium')
y=120
items=[('voxwrist-ask-cover-500.png','Cover / app icon 500×500',(360,360)),
       ('voxwrist-ask-device-icon-128-fullcolor.png','Device icon 128 (full colour)',(128,128)),
       ('voxwrist-ask-device-icon-128-64color.png','Device icon 128 (64-colour MIP)',(128,128)),
       ('voxwrist-ask-hero-1440x720-en.png','Hero 1440×720 — EN',(720,360)),
       ('voxwrist-ask-hero-1440x720-fr.png','Hero 1440×720 — FR',(720,360))]
x=G
for f,t,sz in items:
    im=Image.open(O+f).convert('RGB').resize(sz,Image.LANCZOS)
    if sz[0]==128:
        cs.paste(im,(x,y+116)); d.text((x,y+260),t.split(' (')[0],font=lab,fill=(190,188,215)); d.text((x,y+286),'('+t.split(' (')[1],font=lab,fill=(190,188,215)); x+=128+G+40 if '64' not in f else 128+G
    else:
        cs.paste(im,(x,y)); d.text((x,y+368),t,font=lab,fill=(190,188,215)); x+=sz[0]+G
names=['1-ask-voice','2-daily-brief','3-voice-reminders','4-follow-up','5-live-orb']
y+=360+70
for l in ('en','fr'):
    for i,n in enumerate(names):
        im=Image.open(O+f'voxwrist-ask-screenshot-{n}-{l}.jpg').convert('RGB').resize((T,T),Image.LANCZOS)
        xx=G+i*(T+G); cs.paste(im,(xx,y)); d.text((xx,y+T+8),f'Screenshot {i+1} — {l.upper()} (1000×1000)',font=lab,fill=(190,188,215))
    y+=T+70
print(W,y)
cs=cs.crop((0,0,W,y))
cs.save(O+'contact-sheet.png',optimize=True)
