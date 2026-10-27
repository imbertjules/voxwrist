from lib import *
def _rgba(rgb,a):
    return Image.fromarray((np.dstack([np.clip(rgb,0,1),np.clip(a,0,1)[...,None]])*255+0.5).astype(np.uint8),'RGBA')
def smooth_mask(m,rad):
    return m.filter(ImageFilter.GaussianBlur(rad)).point(lambda v:255 if v>127 else 0).filter(ImageFilter.GaussianBlur(0.8))
def watch2(screen,D,ss=2,tone='titanium',strap_up=0.55,strap_down=1.6):
    S=ss; Dd=D*S; R=Dd/2
    Wc=int(Dd*1.25); Hc=int(Dd*(1.1+strap_up+strap_down))
    cx,cy=Wc/2,Dd*(0.55+strap_up)
    x,y=grid(Wc,Hc)
    ang=np.arctan2(y-cy,x-cx); rr=np.sqrt((x-cx)**2+(y-cy)**2)
    cv=Image.new('RGBA',(Wc,Hc),(0,0,0,0))
    # strap
    sw=Dd*0.56
    sm=Image.new('L',(Wc,Hc),0); ImageDraw.Draw(sm).rectangle((cx-sw/2,0,cx+sw/2,Hc),fill=255)
    acr=np.clip(np.abs(x-cx)/(sw/2),0,1)
    base=hx('1b1b22')
    srgb=base[None,None,:]*(1.0-0.55*acr[...,None]**4)+0.035*np.exp(-((x-cx+sw*0.2)/(sw*0.10))**2)[...,None]
    # pin-hole/texture lines
    srgb=srgb+0.012*np.sin(y/(S*5))[...,None]
    dy=(y-cy)/R
    fade=np.where(dy<0,np.clip(1-(-dy-0.9)/strap_up,0,1),np.clip(1-(dy-1.0)/strap_down,0,1))
    fade=fade*fade*(3-2*fade)
    sa=np.asarray(sm).astype(float)/255*fade**1.3
    cv.alpha_composite(_rgba(srgb,sa))
    # case outline + slim connectors
    body=Image.new('L',(Wc,Hc),0); bd=ImageDraw.Draw(body)
    bd.ellipse((cx-R,cy-R,cx+R,cy+R),fill=255)
    cw=sw*1.04
    bd.rounded_rectangle((cx-cw/2,cy-R*1.06,cx+cw/2,cy+R*1.06),radius=cw*0.22,fill=255)
    body=smooth_mask(body,S*8)
    # buttons (drawn under case)
    btn=Image.new('L',(Wc,Hc),0); btd=ImageDraw.Draw(btn)
    for a_,len_,h_ in [(-32,0.07,0.07),(0,0.085,0.11),(32,0.07,0.07)]:
        a=np.deg2rad(a_); bx=cx+R*0.99*np.cos(a); by=cy+R*0.99*np.sin(a)
        dx=np.sign(np.cos(a))
        x1=bx-R*0.02*dx; x2=bx+R*len_*dx
        btd.rounded_rectangle((min(x1,x2),by-R*h_/2,max(x1,x2),by+R*h_/2),radius=R*0.03,fill=255)
    bmet=lin_grad(Wc,Hc,[(0,hx('3a3d45')),(0.45,hx('a9aeb8')),(0.55,hx('d0d4dc')),(1,hx('2c2e35'))],angle=90)
    # per-button vertical shading
    bl=np.asarray(btn).astype(float)/255
    cv.alpha_composite(_rgba(bmet*0.85,bl))
    # metal: anisotropic conic
    if tone=='titanium':
        lo,hi=hx('16171c'),hx('7a7f8a')
    else:
        lo,hi=hx('1a1a1f'),hx('8a8d96')
    t=0.5+0.38*np.cos(2*(ang-np.deg2rad(-50)))+0.10*np.cos(4*ang+0.6)
    t=np.clip(t,0,1)[...,None]
    metal=lo*(1-t)+hi*t
    # vertical light on lugs
    bmask=np.asarray(body).astype(float)/255
    inner=np.asarray(body.filter(ImageFilter.GaussianBlur(S*4))).astype(float)/255
    edge=np.clip((1-inner)*bmask*1.8,0,1)
    metal=metal*(1-0.25*edge[...,None])+np.clip(-(x-cx)*0.4-(y-cy)*0.6,0,None)[...,None]/Dd*0.0
    cv.alpha_composite(_rgba(metal,bmask))
    # chamfer highlight ring at case edge
    ring=np.exp(-((rr-R*0.975)/(S*1.6))**2)*np.clip(0.5+0.5*np.cos(ang-np.deg2rad(-120)),0,1)
    cv.alpha_composite(_rgba(np.ones((Hc,Wc,3)),ring*0.75*bmask))
    # bezel (ceramic, dark) with soft gradient
    rb=R*0.94
    bez=(rr<rb).astype(float)
    bezc=hx('0c0c11')*(1)+(0.06*np.clip(0.5+0.5*np.cos(ang-np.deg2rad(-110)),0,1))[...,None]
    cv.alpha_composite(_rgba(bezc,bez))
    # minimal 4 markers
    d=ImageDraw.Draw(cv)
    for k in range(12):
        a=np.deg2rad(k*30-90)
        r1=R*0.925; r2=R*(0.895 if k%3==0 else 0.91)
        c=(170,172,180,255) if k%3==0 else (80,82,90,255)
        d.line((cx+r1*np.cos(a),cy+r1*np.sin(a),cx+r2*np.cos(a),cy+r2*np.sin(a)),fill=c,width=int(S*(2.6 if k%3==0 else 1.6)))
    # inner bezel lip
    rl=R*0.88
    lip=np.exp(-((rr-rl)/(S*1.2))**2)*0.18
    cv.alpha_composite(_rgba(np.ones((Hc,Wc,3)),lip))
    # display
    rs=R*0.87
    d.ellipse((cx-rs,cy-rs,cx+rs,cy+rs),fill=(0,0,0,255))
    sd_=int(rs*2*0.99)
    scr=screen.convert('RGB').resize((sd_,sd_),Image.LANCZOS)
    cv.paste(scr,(int(cx-sd_/2),int(cy-sd_/2)),circle_mask((sd_,sd_)))
    # glass sheen
    inside=(rr<rs).astype(float)
    sheen=np.clip(((cx-x)*0.55+(cy-y)*0.85)/rs,0,1)**2*0.08
    cv.alpha_composite(_rgba(np.ones((Hc,Wc,3)),inside*sheen))
    return cv.resize((Wc//S,Hc//S),Image.LANCZOS)
if __name__=='__main__':
    import sys
    im=Image.open('/workspace/voxstore/src/voxwrist-site/store-screenshots/ask-4-answer-en.png')
    w=watch2(im,540)
    bg=Image.new('RGBA',w.size,(30,24,60,255)); bg.alpha_composite(w); bg.convert('RGB').save('w2_%s.png'%sys.argv[1])
    print(w.size)
