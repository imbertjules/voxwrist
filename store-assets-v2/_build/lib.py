import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageChops

G='/usr/share/fonts/truetype/sand-box/google/'
FONTS={'head':G+'Inter Tight/InterTight-VariableFont_wght.ttf','body':G+'Inter/Inter-VariableFont_opsz,wght.ttf','word':G+'Sora/Sora-VariableFont_wght.ttf'}
def font(kind,size,weight='Bold'):
    f=ImageFont.truetype(FONTS[kind],size)
    try: f.set_variation_by_name(weight)
    except Exception: pass
    return f

def hx(h): h=h.lstrip('#'); return np.array([int(h[i:i+2],16) for i in (0,2,4)],float)/255
PAL={
 'aurore':[hx('5536E8'),hx('FF74B8'),hx('B68DFF')],
 'lagon':[hx('0A5BD0'),hx('40F0D2'),hx('74E4FF')],
 'braise':[hx('D42F55'),hx('FFB648'),hx('FF8E5E')],
}
INK=hx('16112E'); DEEP=hx('0B0820')

def grid(w,h):
    y,x=np.mgrid[0:h,0:w].astype(float)
    return x,y

def blob(x,y,cx,cy,r):
    return np.exp(-(((x-cx)**2+(y-cy)**2)/(r*r)))

def background(w,h,blobs,base_top=hx('140E34'),base_bot=hx('07061A'),grain=0.012,seed=1):
    """blobs: list of (cx,cy,r,color,intensity) in pixel units"""
    x,y=grid(w,h)
    t=(y/h)[...,None]
    img=base_top*(1-t)+base_bot*t
    for cx,cy,r,c,a in blobs:
        img=img+blob(x,y,cx,cy,r)[...,None]*c*a
    # soft screen-style tone map
    img=1-np.exp(-img*1.15)
    img=img/ (1-np.exp(-1.15))
    rng=np.random.default_rng(seed)
    img=img+rng.normal(0,grain,img.shape[:2])[...,None]
    return np.clip(img,0,1)

def to_img(a):
    return Image.fromarray((np.clip(a,0,1)*255+0.5).astype(np.uint8))

def orb_layer(size,R,cx,cy,pal='aurore',swirl=2.2,glow=1.0,glow_r=0.55,accent=None,ss=2,conic=None,ctrl=None):
    """returns (rgb array float, alpha array) at size (w,h) with orb + glow premultiplied-ish: color and alpha"""
    w,h=size
    W,H=w*ss,h*ss
    x,y=grid(W,H)
    u=(x/ss-cx)/R; v=(y/ss-cy)/R
    d=np.sqrt(u*u+v*v)
    p=PAL[pal]
    acc=PAL[accent] if accent else PAL['lagon']
    inside=np.clip((1-d)*R*ss*0.9,0,1)  # AA edge
    z=np.sqrt(np.clip(1-d*d,0,1))
    od=np.clip(1-d,0,1)
    uc=u-0.18; vc=v-0.22
    dc=np.sqrt(uc*uc+vc*vc)
    th=np.arctan2(vc,uc)+swirl*np.clip(1-dc/1.4,0,1)**1.5
    uu=d*np.cos(th); vv=d*np.sin(th)
    # mesh gradient (softmax of warped distances) -> smooth aurora, no singularity
    wu=u+0.18*np.sin(2.3*v+0.7)+0.10*np.sin(4.1*v+1.9)
    wv=v+0.18*np.sin(2.0*u+2.3)+0.08*np.sin(3.7*u+0.4)
    th=np.arctan2(wv,wu)+swirl*od**1.2
    ru=np.sqrt(wu*wu+wv*wv)
    wu,wv=ru*np.cos(th),ru*np.sin(th)
    pts=ctrl if ctrl is not None else [(-0.6,-0.55,p[0]),(0.65,-0.5,p[1]),(0.6,0.6,acc[1]),(-0.6,0.6,acc[0]*0.7+p[0]*0.3),(0.0,0.0,p[2]),(0.0,0.95,p[0])]
    k=3.2
    wsum=np.zeros((H,W,1)); col=np.zeros((H,W,3))
    for px_,py_,c in pts:
        wgt=np.exp(-k*((wu-px_)**2+(wv-py_)**2))[...,None]
        col+=wgt*c; wsum+=wgt
    col=col/(wsum+1e-9)
    # soften towards centre: luminous core
    core=np.exp(-((u+0.05)**2+(v+0.05)**2)/0.18)
    col=col*(0.62+0.38*z[...,None])+core[...,None]*(np.array([1.0,0.9,1.0])*0.30)
    rib=np.exp(-((wv-0.22*np.sin(2.2*wu+0.8)+0.1)/0.10)**2)*od**0.8
    col=col+rib[...,None]*0.22
    # edge definition: slight darkening then bright fresnel rim
    col=col*(1-0.25*np.clip((d-0.80)/0.2,0,1)[...,None]**2)
    rim=np.exp(-((d-0.985)/0.025)**2)
    col=col+rim[...,None]*(p[2]*0.6+0.25)*np.clip(0.6-0.6*v,0.2,1)[...,None]
    sp=np.exp(-(((u+0.32)/0.22)**2+((v+0.52)/0.11)**2))
    col=col+sp[...,None]*0.35
    col=np.clip(col,0,None)
    col=1-np.exp(-col*1.25); col=col/(1-np.exp(-1.25))
    lum=col.mean(-1,keepdims=True)
    col=np.clip(lum+(col-lum)*1.35,0,1)
    # glow outside
    g=np.exp(-np.clip(d-1,0,None)/glow_r)*(d>=0.0)
    gcol=(p[0]*0.5+p[1]*0.5)
    gl=(g*glow)[...,None]*gcol*np.clip(d-0.9,0,1)[...,None]**0  # glow everywhere
    orb=col
    A=inside
    a_img=Image.fromarray((np.dstack([orb,A[...,None]])*255).clip(0,255).astype(np.uint8),'RGBA').resize((w,h),Image.LANCZOS)
    g_img=Image.fromarray((np.clip(gl,0,1)*255).astype(np.uint8)).resize((w,h),Image.LANCZOS)
    return a_img,g_img

def add_layer(base,glow):
    return ImageChops.add(base.convert('RGB'),glow.convert('RGB'))

def screen_blend(base,glow):
    return ImageChops.screen(base.convert('RGB'),glow.convert('RGB'))

def circle_mask(size,ss=4,inset=0):
    w,h=size
    m=Image.new('L',(w*ss,h*ss),0); ImageDraw.Draw(m).ellipse((inset*ss,inset*ss,(w-inset)*ss-1,(h-inset)*ss-1),fill=255)
    return m.resize((w,h),Image.LANCZOS)

def lin_grad(w,h,stops,angle=90):
    """stops: list of (pos,color array). angle deg: 90 = top->bottom"""
    x,y=grid(w,h)
    a=np.deg2rad(angle)
    t=(x-w/2)*np.cos(a)+(y-h/2)*np.sin(a)
    t=(t-t.min())/(t.max()-t.min()+1e-9)
    out=np.zeros((h,w,3))
    ps=[s[0] for s in stops]; cs=[s[1] for s in stops]
    for ch in range(3):
        out[...,ch]=np.interp(t,ps,[c[ch] for c in cs])
    return out

def watch(screen, D, ss=2, finish='graphite'):
    """Draw a generic round smartwatch. D=case diameter in px. Returns RGBA canvas (W x H) with watch centered, and screen center coords."""
    S=ss
    Dd=D*S
    Wc=int(Dd*1.30); Hc=int(Dd*2.3)
    cx,cy=Wc/2,Hc/2
    canvas=Image.new('RGBA',(Wc,Hc),(0,0,0,0))
    # strap
    sw=Dd*0.56
    strap=Image.new('RGBA',(Wc,Hc),(0,0,0,0))
    sd=ImageDraw.Draw(strap)
    sd.rounded_rectangle((cx-sw/2,0,cx+sw/2,Hc),radius=sw*0.18,fill=(255,255,255,255))
    sm=np.asarray(strap)[...,3].astype(float)/255
    sg=lin_grad(Wc,Hc,[(0,hx('15151c')),(0.5,hx('24242e')),(1,hx('15151c'))],angle=0)
    # horizontal shading across strap width
    x,y=grid(Wc,Hc)
    acr=np.clip(np.abs(x-cx)/(sw/2),0,1)
    sg=sg*(1.0-0.45*acr**3)[...,None]+ (0.06*np.exp(-((x-cx+sw*0.18)/(sw*0.12))**2))[...,None]
    # subtle ribbing
    rib=0.018*np.sin(y/(S*7.0))
    sg=sg+rib[...,None]
    fade=np.clip(1-np.abs(y-cy)/(Hc*0.5),0,1)**0.6
    sa=sm*np.clip(fade*1.6,0,1)
    strapimg=Image.fromarray((np.dstack([np.clip(sg,0,1),sa[...,None]])*255).astype(np.uint8),'RGBA')
    canvas.alpha_composite(strapimg)
    # lugs (case body extension)
    body=Image.new('L',(Wc,Hc),0); bd=ImageDraw.Draw(body)
    R=Dd/2
    lw=sw*1.06
    bd.rounded_rectangle((cx-lw/2,cy-R*1.22,cx+lw/2,cy+R*1.22),radius=lw*0.16,fill=255)
    bd.ellipse((cx-R,cy-R,cx+R,cy+R),fill=255)
    # buttons
    btn=Image.new('L',(Wc,Hc),0); btd=ImageDraw.Draw(btn)
    for ang,ln in [(-38,0.10),(0,0.12),(38,0.10)]:
        a=np.deg2rad(ang); bx=cx+R*np.cos(a); by=cy+R*np.sin(a)
        btd.rounded_rectangle((bx-R*0.03,by-R*0.075,bx+R*ln,by+R*0.075),radius=R*0.04,fill=255)
    for ang in [-150,150]:
        a=np.deg2rad(ang); bx=cx+R*np.cos(a); by=cy+R*np.sin(a)
        btd.rounded_rectangle((bx-R*0.10,by-R*0.07,bx+R*0.03,by+R*0.07),radius=R*0.04,fill=255)
    # metal colours
    if finish=='graphite':
        stops=[(0,hx('5b5f6b')),(0.35,hx('2a2c33')),(0.55,hx('8b909c')),(0.75,hx('2f3139')),(1,hx('14151a'))]
    else:
        stops=[(0,hx('d9d6cf')),(0.4,hx('8f8a80')),(0.6,hx('efece6')),(1,hx('5e5a52'))]
    metal=lin_grad(Wc,Hc,stops,angle=60)
    bm=np.asarray(btn).astype(float)/255
    bmet=lin_grad(Wc,Hc,[(0,hx('6d717c')),(0.5,hx('a6abb6')),(1,hx('3a3c44'))],angle=90)
    btnimg=Image.fromarray((np.dstack([bmet,bm[...,None]])*255).astype(np.uint8),'RGBA')
    canvas.alpha_composite(btnimg)
    bmask=np.asarray(body).astype(float)/255
    # edge highlight: distance-ish via blur
    edge=np.asarray(body.filter(ImageFilter.GaussianBlur(S*3))).astype(float)/255
    rimhl=np.clip((1-edge)*bmask*2.2,0,1)
    metal=metal*(0.85+0.15*edge[...,None])+rimhl[...,None]*0.25
    bodyimg=Image.fromarray((np.dstack([np.clip(metal,0,1),bmask[...,None]])*255).astype(np.uint8),'RGBA')
    canvas.alpha_composite(bodyimg)
    d=ImageDraw.Draw(canvas)
    # bezel ring
    rb=R*0.93
    d.ellipse((cx-rb,cy-rb,cx+rb,cy+rb),fill=(10,10,14,255))
    # bezel inner subtle gradient ring
    rbi=R*0.905
    d.ellipse((cx-rbi,cy-rbi,cx+rbi,cy+rbi),fill=(22,22,28,255))
    # bezel markers (generic minimalist)
    for k in range(60):
        a=np.deg2rad(k*6-90)
        big=(k%5==0)
        r1=R*0.905; r2=R*(0.858 if big else 0.880)
        col=(150,152,160,255) if big else (70,72,80,255)
        d.line((cx+r1*np.cos(a),cy+r1*np.sin(a),cx+r2*np.cos(a),cy+r2*np.sin(a)),fill=col,width=max(1,int(S*(2.2 if big else 1.2))))
    # glass/black display
    rs=R*0.845
    d.ellipse((cx-rs,cy-rs,cx+rs,cy+rs),fill=(0,0,0,255))
    # screen image
    sd_=int(rs*2*0.985)
    scr=screen.convert('RGB').resize((sd_,sd_),Image.LANCZOS)
    m=circle_mask((sd_,sd_))
    canvas.paste(scr,(int(cx-sd_/2),int(cy-sd_/2)),m)
    # glass reflection
    gl=Image.new('RGBA',(Wc,Hc),(0,0,0,0))
    x2,y2=grid(Wc,Hc)
    inside=((x2-cx)**2+(y2-cy)**2)<(rs*rs)
    refl=np.clip(((x2-cx)*-0.6+(y2-cy)*-0.8)/(rs),0,1)
    ga=(inside*(0.07*refl**1.5)).astype(float)
    # thin arc highlight on glass edge
    rr=np.sqrt((x2-cx)**2+(y2-cy)**2)
    edgehl=np.exp(-((rr-rs*0.995)/(S*1.2))**2)*np.clip(-(x2-cx+(y2-cy))/(rs*1.4),0,1)*0.6
    ga=ga+edgehl
    glimg=Image.fromarray((np.dstack([np.ones_like(ga),np.ones_like(ga),np.ones_like(ga),np.clip(ga,0,1)])*255).astype(np.uint8),'RGBA')
    canvas.alpha_composite(glimg)
    out=canvas.resize((Wc//S,Hc//S),Image.LANCZOS)
    return out

def shadow(img,blur=30,opacity=0.55,offset=(0,30)):
    a=img.split()[3].point(lambda v:int(v*opacity))
    sh=Image.new('RGBA',img.size,(0,0,0,0)); sh.putalpha(a)
    sh=sh.filter(ImageFilter.GaussianBlur(blur))
    out=Image.new('RGBA',(img.width,img.height),(0,0,0,0))
    out.alpha_composite(sh,dest=offset) if False else None
    return sh

def text_center(draw,cx,y,txt,f,fill,tracking=0):
    if tracking==0:
        w=draw.textlength(txt,font=f)
        draw.text((cx-w/2,y),txt,font=f,fill=fill)
        return w
    ws=[draw.textlength(c,font=f) for c in txt]
    total=sum(ws)+tracking*(len(txt)-1)
    x=cx-total/2
    for c,wc in zip(txt,ws):
        draw.text((x,y),c,font=f,fill=fill); x+=wc+tracking
    return total

def gradient_text(size,pos,txt,f,c1,c2,tracking=0,angle=0):
    """return RGBA layer with gradient-filled text"""
    w,h=size
    m=Image.new('L',size,0); d=ImageDraw.Draw(m)
    x,y=pos
    if tracking:
        for ch in txt:
            d.text((x,y),ch,font=f,fill=255); x+=d.textlength(ch,font=f)+tracking
    else:
        d.text((x,y),txt,font=f,fill=255)
    g=lin_grad(w,h,[(0,c1),(1,c2)],angle=angle)
    return Image.fromarray((np.dstack([g,np.asarray(m)[...,None]/255.0])*255).astype(np.uint8),'RGBA')
