from lib import *
from watch2 import watch2
import sys, io, os
SRC='/workspace/voxstore/src/voxwrist-site/store-screenshots/'
OUT='/workspace/voxstore/assets-v2/'
W=1000
def scr(name,l):
    if name=='followup': return Image.open(f'scr-followup-{l}.png')
    return Image.open(SRC+f'ask-{name}-{l}.png')
TH={'en':'braise','fr':'aurore'}
COPY={
 'en':[('VOICE ASSISTANT','Ask out loud.\nHear the answer.','Talk to your watch. It answers by voice and on screen.','4-answer'),
       ('DAILY BRIEF','Your day,\nat a glance.','Weather, agenda and reminders in one smart brief.','2-brief'),
       ('VOICE REMINDERS','Reminders?\nJust say it.','“Remind me to call Paul at 6pm.” Done.','5-reminder'),
       ('FOLLOW-UP','Keep the\nconversation going.','Ask a follow-up. It remembers the context.','followup'),
       ('LIVE ORB','Listens. Thinks.\nSpeaks.','A living orb shows what your assistant is doing.','orb')],
 'fr':[('ASSISTANT VOCAL','Parlez.\nÉcoutez la réponse.','Posez votre question : réponse à voix haute et à l’écran.','4-answer'),
       ('BRIEF DU JOUR','Votre journée\nen un coup d’œil.','Météo, agenda et rappels dans un seul brief.','2-brief'),
       ('RAPPELS VOCAUX','Un rappel ?\nDites-le.','« Rappelle-moi d’appeler Paul à 18 h. » C’est noté.','5-reminder'),
       ('CONVERSATION','La conversation\ncontinue.','Enchaînez naturellement, le contexte est gardé.','followup'),
       ('ORBE VIVANT','Écoute. Réflexion.\nRéponse.','Un orbe vivant montre ce que fait votre assistant.','orb')],
}
LBL={'en':['Thinking','Listening','Speaking'],'fr':['Réflexion','Écoute','Réponse']}

SLIDEPAL=['aurore','braise','lagon','aurore','lagon']
def bg_for(pal,seed):
    p=PAL[pal]; a=PAL['aurore']
    return background(W,W,[(W*0.5,W*0.70,W*0.40,a[0],0.30),(W*0.5,W*0.72,W*0.30,p[0],0.12),(W*0.92,W*0.18,W*0.35,p[1],0.10),(W*0.0,W*1.0,W*0.45,a[0],0.22),(W*0.0,W*0.0,W*0.40,a[0],0.14)],
        base_top=hx('130D33'),base_bot=hx('07061A'),grain=0.006,seed=seed)

def place_watch(img,screen,D,cx,cy,dim=0.0,glowpal=None):
    wt=watch2(screen,D,strap_up=1.5,strap_down=1.4)
    if dim>0:
        dark=Image.new('RGBA',wt.size,(8,6,22,int(255*dim)))
        m=wt.split()[3]
        dl=Image.new('RGBA',wt.size,(0,0,0,0)); dl.paste(dark,(0,0),m)
        wt.alpha_composite(dl)
    sh=Image.new('RGBA',wt.size,(0,0,0,0))
    a=wt.split()[3].point(lambda v:int(v*0.6))
    sh.putalpha(a); sh=sh.filter(ImageFilter.GaussianBlur(D*0.06))
    x0=int(cx-wt.width/2); y0=int(cy-D*(0.55+1.5))
    img.alpha_composite(sh,(x0,y0+int(D*0.05))) if x0>=0 and y0>=0 else None
    tmp=Image.new('RGBA',img.size,(0,0,0,0)); tmp.paste(sh,(x0,y0+int(D*0.05)),sh); img.alpha_composite(tmp) if (x0<0 or y0<0) else None
    tmp=Image.new('RGBA',img.size,(0,0,0,0)); tmp.paste(wt,(x0,y0),wt); img.alpha_composite(tmp)

def halo(img,cx,cy,r,pal,amt=0.8):
    x,y=grid(W,W)
    p=PAL[pal]
    g=np.exp(-((x-cx)**2+(y-cy)**2)/(r*r))*amt
    arr=np.asarray(img.convert('RGB')).astype(float)/255
    c=p[0]*0.6+p[1]*0.4
    arr=1-(1-arr)*(1-g[...,None]*c)
    return to_img(arr).convert('RGBA')

def header(img,eyebrow,head,sub,pal,top=64):
    d=ImageDraw.Draw(img)
    p=PAL[pal]
    fe=font('body',22,'SemiBold')
    # eyebrow in accent colour
    acc=tuple(int(v*255) for v in (p[1]*0.6+np.array([1,1,1])*0.4))
    text_center(d,W/2,top,eyebrow,fe,acc,tracking=5)
    fh=font('head',70,'ExtraBold')
    y=top+44
    for line in head.split('\n'):
        tw=d.textlength(line,font=fh)
        while tw>W-90:
            fh=font('head',fh.size-2,'ExtraBold'); tw=d.textlength(line,font=fh)
    for line in head.split('\n'):
        text_center(d,W/2,y,line,fh,(255,255,255))
        y+=int(fh.size*1.08)
    fs=font('body',29,'Medium')
    while d.textlength(sub,font=fs)>W-110: fs=font('body',fs.size-1,'Medium')
    text_center(d,W/2,y+16,sub,fs,(206,204,228))
    return y+16+fs.size

def save_small(img,path,limit=148000):
    rgb=img.convert('RGB')
    for q in (92,90,88,86,84,82,80,78,75,72,70):
        b=io.BytesIO(); rgb.save(b,'JPEG',quality=q,optimize=True,progressive=True,subsampling=0 if q>=86 else 2)
        if b.tell()<limit: break
    open(path,'wb').write(b.getvalue()); return q,b.tell()

def pill(img,cx,cy,txt,pal):
    d=ImageDraw.Draw(img)
    f=font('body',24,'SemiBold')
    tw=d.textlength(txt,font=f); w=tw+56; h=44
    lay=Image.new('RGBA',img.size,(0,0,0,0)); ld=ImageDraw.Draw(lay)
    ld.rounded_rectangle((cx-w/2,cy-h/2,cx+w/2,cy+h/2),radius=h/2,fill=(255,255,255,30),outline=(255,255,255,60),width=1)
    c=tuple(int(v*255) for v in PAL[pal][1])
    ld.ellipse((cx-w/2+18,cy-5,cx-w/2+28,cy+5),fill=c+(255,))
    img.alpha_composite(lay)
    d.text((cx-w/2+38,cy-h/2+8),txt,font=f,fill=(240,240,250))

def make(l,i):
    eb,head,sub,key=COPY[l][i]
    pal=TH[l]
    sp=SLIDEPAL[i]
    img=to_img(bg_for(sp,i+1)).convert('RGBA')
    if key=='orb':
        img=halo(img,W/2,690,320,'aurore',0.38)
        place_watch(img,scr('6-think',l),320,W/2-290,700,dim=0.30)
        place_watch(img,scr('4-answer',l),320,W/2+290,700,dim=0.30)
        place_watch(img,scr('3-listen',l),460,W/2,680)
        header(img,eb,head,sub,sp)
        labs=LBL[l]
        pill(img,W/2-290,905,labs[0],'aurore' if pal!='aurore' else 'lagon')
        pill(img,W/2,950,labs[1],pal)
        pill(img,W/2+290,905,labs[2],'lagon')
        return img
    img=halo(img,W/2,680,330,sp,0.42)
    place_watch(img,scr(key,l),540,W/2,668)
    header(img,eb,head,sub,sp)
    return img

if __name__=='__main__':
    os.makedirs(OUT,exist_ok=True)
    tag=sys.argv[1] if len(sys.argv)>1 else 't'
    for l in ('en','fr'):
        for i in range(5):
            im=make(l,i)
            im.convert('RGB').save(f'prev_{tag}_{l}{i+1}.png')
