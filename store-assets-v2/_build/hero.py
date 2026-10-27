from lib import *
from watch2 import watch2
import sys
SRC='/workspace/voxstore/src/voxwrist-site/store-screenshots/'
HW,HH=1440,720
TXT={'en':('Your AI agent,','on your wrist.','Ask by voice  ·  Daily brief  ·  Voice reminders'),
     'fr':('Votre agent IA,','à votre poignet.','Questions vocales  ·  Brief du jour  ·  Rappels')}
def wordmark(img,x,y,size=46,mark=True):
    d=ImageDraw.Draw(img)
    if mark:
        R=size*0.48
        orb=Image.open('/workspace/voxstore/src/dist/icon-ask-500.png').convert('RGBA').resize((int(R*2+8),int(R*2+8)),Image.LANCZOS)
        # small glow
        gl=Image.new('RGBA',(int(R*6),int(R*6)),(0,0,0,0)); gd=ImageDraw.Draw(gl)
        gd.ellipse((R*1.5,R*1.5,R*4.5,R*4.5),fill=(140,90,255,110)); gl=gl.filter(ImageFilter.GaussianBlur(R*0.7))
        img.alpha_composite(gl,(int(x+R-R*3),int(y+size*0.62-R*3)))
        img.alpha_composite(orb,(int(x),int(y+size*0.62-R-4)))
        x=x+R*2+size*0.38
    f=font('word',size,'SemiBold')
    lay=gradient_text(img.size,(x,y),'voxwrist',f,np.array([1,1,1]),hx('D9C8FF'),tracking=size*0.02,angle=0)
    img.alpha_composite(lay)
def make(l):
    a=PAL['aurore']; g=PAL['lagon']; b=PAL['braise']
    img=to_img(background(HW,HH,[(1060,380,420,a[0],0.55),(1250,120,300,a[1],0.18),(820,700,320,g[0],0.25),(0,0,500,a[0],0.12),(1440,720,300,b[0],0.10)],
        base_top=hx('120C31'),base_bot=hx('07061A'),grain=0.006,seed=7)).convert('RGBA')
    # big aura orb + sound rings behind watch
    cx,cy=1060,372
    x,y=grid(HW,HH); d=np.sqrt((x-cx)**2+(y-cy)**2); ang=np.arctan2(y-cy,x-cx)
    rings=np.zeros((HH,HW))
    for rr,wd,am in [(330,7,0.30),(395,6,0.18),(460,5,0.10)]:
        rings+=np.exp(-((d-rr)/wd)**2)*am*np.abs(np.cos(ang))**1.5
    arr=np.asarray(img.convert('RGB')).astype(float)/255
    rc=a[2]*0.6+g[2]*0.4
    arr=1-(1-arr)*(1-np.clip(rings,0,1)[...,None]*rc)
    glow=np.exp(-(d/300)**2)*0.55
    arr=1-(1-arr)*(1-glow[...,None]*(a[0]*0.6+a[1]*0.4))
    img=to_img(arr).convert('RGBA')
    scr=Image.open(SRC+f'ask-1-home-{l}.png')
    D=470
    wt=watch2(scr,D,strap_up=1.0,strap_down=1.0)
    y0=int(cy-D*(0.55+1.0)); x0=int(cx-wt.width/2)
    sh=Image.new('RGBA',wt.size,(0,0,0,0)); sh.putalpha(wt.split()[3].point(lambda v:int(v*0.6))); sh=sh.filter(ImageFilter.GaussianBlur(28))
    lay=Image.new('RGBA',img.size,(0,0,0,0)); lay.paste(sh,(x0,y0+24),sh); img.alpha_composite(lay)
    lay=Image.new('RGBA',img.size,(0,0,0,0)); lay.paste(wt,(x0,y0),wt); img.alpha_composite(lay)
    # text block
    L=110
    wordmark(img,L,170,size=44)
    d=ImageDraw.Draw(img)
    t1,t2,sub=TXT[l]
    fh=font('head',78,'ExtraBold')
    while max(d.textlength(t1,font=fh),d.textlength(t2,font=fh))>620: fh=font('head',fh.size-2,'ExtraBold')
    d.text((L,270),t1,font=fh,fill=(255,255,255))
    lay=gradient_text(img.size,(L,270+int(fh.size*1.1)),t2,fh,hx('FFB7DA'),hx('B68DFF'),angle=0)
    img.alpha_composite(lay)
    fs=font('body',25,'Medium')
    d.text((L,290+int(fh.size*2.2)+16),sub,font=fs,fill=(200,198,225))
    return img.convert('RGB')
if __name__=='__main__':
    for l in ('en','fr'):
        make(l).save(f'hero_{sys.argv[1]}_{l}.png')
