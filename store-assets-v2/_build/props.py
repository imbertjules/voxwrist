import cairosvg, io, sys, math
from PIL import Image
HUE={
 'aurore':dict(hi='#FFC9E4',mid='#FF74B8',lo='#5536E8',rim='#B68DFF',deep='#2A1580'),
 'lagon': dict(hi='#D6FDFF',mid='#40D8E8',lo='#0A5BD0',rim='#74E4FF',deep='#062A6E'),
}
INK='#16112E'
def snap(h):
    h=h.lstrip('#'); c=[int(h[i:i+2],16) for i in (0,2,4)]
    return '#'+''.join('%02X'%(min(3,(v+42)//85)*85) for v in c)

def bot(cx,cy,r,hue='aurore',flat=False,gid='b',shadow=True,gloss=True):
    H=HUE[hue]; s=r/49.0
    # original geometry (100-unit icon, orb r=49 at 50,50)
    def X(x): return cx+(x-50)*s
    def Y(y): return cy+(y-50)*s
    out=[]
    if flat:
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{snap(H["lo"])}"/>')
        out.append(f'<circle cx="{cx-r*0.12}" cy="{cy-r*0.14}" r="{r*0.80}" fill="{snap(H["mid"])}"/>')
        out.append(f'<ellipse cx="{cx-r*0.36}" cy="{cy-r*0.56}" rx="{r*0.24}" ry="{r*0.13}" transform="rotate(-28 {cx-r*0.36} {cy-r*0.56})" fill="{snap(H["hi"])}"/>')
    else:
        out.append(f'''<defs>
<radialGradient id="{gid}g" cx="40%" cy="34%" r="72%" fx="36%" fy="28%">
 <stop offset="0" stop-color="{H['hi']}"/><stop offset="0.36" stop-color="{H['mid']}"/><stop offset="0.82" stop-color="{H['lo']}"/><stop offset="1" stop-color="{H['deep']}"/></radialGradient>
<radialGradient id="{gid}rim" cx="50%" cy="50%" r="50%" fx="30%" fy="25%">
 <stop offset="0.80" stop-color="{H['rim']}" stop-opacity="0"/><stop offset="0.97" stop-color="{H['rim']}" stop-opacity="0.85"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.9"/></radialGradient>
<radialGradient id="{gid}spec" cx="50%" cy="50%" r="50%">
 <stop offset="0" stop-color="#FFFFFF" stop-opacity="0.85"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0"/></radialGradient>
<radialGradient id="{gid}sh" cx="50%" cy="50%" r="50%">
 <stop offset="0" stop-color="#000000" stop-opacity="0.45"/><stop offset="1" stop-color="#000000" stop-opacity="0"/></radialGradient>
<linearGradient id="{gid}eye" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#241A4A"/><stop offset="1" stop-color="{INK}"/></linearGradient>
</defs>''')
        if shadow:
            out.append(f'<ellipse cx="{cx}" cy="{cy+r*0.98}" rx="{r*0.80}" ry="{r*0.16}" fill="url(#{gid}sh)"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{gid}g)"/>')
        # rim light (bottom-right), via offset radial gradient
        out.append(f'''<defs><radialGradient id="{gid}rl" cx="44%" cy="40%" r="62%">
 <stop offset="0.78" stop-color="{H['rim']}" stop-opacity="0"/><stop offset="0.93" stop-color="{H['rim']}" stop-opacity="0.55"/><stop offset="1" stop-color="#FFFFFF" stop-opacity="0.75"/></radialGradient></defs>''')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{gid}rl)"/>')
        out.append(f'<circle cx="{cx}" cy="{cy}" r="{r*0.995}" fill="none" stroke="#FFFFFF" stroke-opacity="0.18" stroke-width="{max(1,r*0.012)}"/>')
        if gloss:
            out.append(f'<ellipse cx="{cx-r*0.36}" cy="{cy-r*0.52}" rx="{r*0.30}" ry="{r*0.15}" transform="rotate(-28 {cx-r*0.36} {cy-r*0.52})" fill="url(#{gid}spec)"/>')
    eye=snap(INK) if flat else f'url(#{gid}eye)'
    for ex in (31,60):
        out.append(f'<rect x="{X(ex)}" y="{Y(35)}" width="{9*s}" height="{17*s}" rx="{4.5*s}" fill="{eye if not flat else "#000055"}"/>')
    out.append(f'<path d="M{X(40)} {Y(63)} Q{X(50)} {Y(71)} {X(60)} {Y(63)}" fill="none" stroke="{INK if not flat else "#000055"}" stroke-width="{5*s}" stroke-linecap="round"/>')
    return '\n'.join(out)

def svg(body,N=500):
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{N}" height="{N}" viewBox="0 0 500 500">{body}</svg>'

def bgrad(id,stops,cx='50%',cy='45%',r='75%'):
    s=''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in stops)
    return f'<defs><radialGradient id="{id}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient></defs><rect width="500" height="500" fill="url(#{id})"/>'
def lgrad(id,stops,x1=0,y1=0,x2=1,y2=1):
    s=''.join(f'<stop offset="{o}" stop-color="{c}"/>' for o,c in stops)
    return f'<defs><linearGradient id="{id}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}">{s}</linearGradient></defs><rect width="500" height="500" fill="url(#{id})"/>'
def glow(cx,cy,r,col,op=0.6,id='gl'):
    return f'<defs><radialGradient id="{id}" cx="50%" cy="50%" r="50%"><stop offset="0" stop-color="{col}" stop-opacity="{op}"/><stop offset="1" stop-color="{col}" stop-opacity="0"/></radialGradient></defs><circle cx="{cx}" cy="{cy}" r="{r}" fill="url(#{id})"/>'

# ---------- proposals ----------
def A(flat=False):
    if flat:
        b='<rect width="500" height="500" fill="#000055"/>'
        b+='<circle cx="250" cy="250" r="205" fill="#550055"/>'
        for rr in (190,222):
            b+=f'<path d="M{250-rr*0.81} {250-rr*0.59} A{rr} {rr} 0 0 0 {250-rr*0.81} {250+rr*0.59}" fill="none" stroke="#AA55FF" stroke-width="10" stroke-linecap="round"/>'
            b+=f'<path d="M{250+rr*0.81} {250-rr*0.59} A{rr} {rr} 0 0 1 {250+rr*0.81} {250+rr*0.59}" fill="none" stroke="#AA55FF" stroke-width="10" stroke-linecap="round"/>'
        return b+bot(250,250,150,flat=True)
    b=bgrad('bga',[(0,'#3A2496'),(0.55,'#1A1150'),(1,'#0A0824')])
    b+=glow(250,250,240,'#8A4DFF',0.55,'g1')+glow(250,250,170,'#FF74B8',0.35,'g2')
    for rr,op,w in ((188,0.55,5),(214,0.35,4),(238,0.18,3)):
        for side in (-1,1):
            x0=250+side*rr*math.cos(math.radians(40)); y0=250-rr*math.sin(math.radians(40)); y1=250+rr*math.sin(math.radians(40))
            sweep=1 if side==1 else 0
            b+=f'<path d="M{x0} {y0} A{rr} {rr} 0 0 {sweep} {x0} {y1}" fill="none" stroke="#D9C2FF" stroke-opacity="{op}" stroke-width="{w}" stroke-linecap="round"/>'
    return b+bot(250,250,150)

def B(flat=False):
    if flat:
        b='<rect width="500" height="500" fill="#5500AA"/>'
        b+='<circle cx="250" cy="250" r="200" fill="#555555"/><circle cx="250" cy="250" r="184" fill="#000000"/>'
        b+='<rect x="440" y="226" width="22" height="48" rx="8" fill="#555555"/>'
        return b+bot(250,250,120,flat=True)
    b=lgrad('bgb',[(0,'#7B3CF0'),(0.55,'#4A22B8'),(1,'#1A0E5A')],0,0,1,1)
    b+=glow(250,260,250,'#000000',0.45,'gs')
    # case
    b+='<defs><linearGradient id="case" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#8E93A0"/><stop offset="0.35" stop-color="#2C2E36"/><stop offset="0.6" stop-color="#B9BDC8"/><stop offset="1" stop-color="#1A1B20"/></linearGradient></defs>'
    b+='<rect x="436" y="222" width="26" height="56" rx="10" fill="url(#case)"/>'
    b+='<rect x="180" y="20" width="140" height="60" rx="18" fill="#1C1B24"/><rect x="180" y="420" width="140" height="60" rx="18" fill="#1C1B24"/>'
    b+='<circle cx="250" cy="250" r="200" fill="url(#case)"/><circle cx="250" cy="250" r="186" fill="#0E0D14"/>'
    for k in range(12):
        a=math.radians(k*30); r1,r2=(182,170) if k%3==0 else (182,176)
        b+=f'<line x1="{250+r1*math.cos(a)}" y1="{250+r1*math.sin(a)}" x2="{250+r2*math.cos(a)}" y2="{250+r2*math.sin(a)}" stroke="#6E6C80" stroke-width="{4 if k%3==0 else 2}" stroke-linecap="round"/>'
    b+='<circle cx="250" cy="250" r="164" fill="#000000"/>'
    b+=glow(250,250,160,'#8A4DFF',0.45,'g3')
    b+='<path d="M250 86 A164 164 0 0 1 392 168" fill="none" stroke="#B68DFF" stroke-width="7" stroke-linecap="round"/>'
    b+='<defs><linearGradient id="gls" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0.10"/><stop offset="0.5" stop-color="#FFFFFF" stop-opacity="0"/></linearGradient></defs>'
    return b+bot(250,255,112)+'<circle cx="250" cy="250" r="164" fill="url(#gls)"/>'

def C(flat=False):
    hue='lagon'
    if flat:
        b='<rect width="500" height="500" fill="#0055AA"/>'
        b+=bot(215,275,150,hue,flat=True)
        b+='<path d="M330 70 h110 a30 30 0 0 1 30 30 v60 a30 30 0 0 1 -30 30 h-70 l-34 30 v-30 h-6 a30 30 0 0 1 -30 -30 v-60 a30 30 0 0 1 30 -30z" fill="#FFFFFF"/>'
        for i,hh in enumerate((26,52,36,60,30)):
            b+=f'<rect x="{336+i*22}" y="{130-hh/2}" width="11" height="{hh}" rx="5.5" fill="#0055AA"/>'
        return b
    b=lgrad('bgc',[(0,'#1FB6D9'),(0.5,'#1167D6'),(1,'#0B2A86')],0,0,1,1)
    b+=glow(215,275,230,'#74E4FF',0.35,'g4')
    b+=bot(215,275,150,hue,gid='c')
    b+='<path d="M330 70 h110 a30 30 0 0 1 30 30 v60 a30 30 0 0 1 -30 30 h-70 l-34 30 v-30 h-6 a30 30 0 0 1 -30 -30 v-60 a30 30 0 0 1 30 -30z" fill="#FFFFFF"/>'
    for i,hh in enumerate((26,52,36,60,30)):
        b+=f'<rect x="{336+i*22}" y="{130-hh/2}" width="11" height="{hh}" rx="5.5" fill="#1167D6"/>'
    return b

def D(flat=False):
    if flat:
        b='<rect width="500" height="500" fill="#FF55AA"/>'
        b+='<polygon points="500,120 500,500 120,500" fill="#AA55FF"/>'
        b+='<circle cx="250" cy="248" r="194" fill="#FFFFFF"/>'
        return b+bot(250,248,185,flat=True)
    b=lgrad('bgd',[(0,'#FFC07A'),(0.42,'#FF6F91'),(1,'#6A2BE8')],0.1,0,0.9,1)
    b+=glow(250,262,230,'#3A0C6E',0.55,'g5')
    b+='<circle cx="250" cy="248" r="191" fill="none" stroke="#FFFFFF" stroke-opacity="0.55" stroke-width="5"/>'
    return b+bot(250,248,185,gid='d')

PROPS={'A':A,'B':B,'C':C,'D':D}
def render(fn,N,flat=False):
    png=cairosvg.svg2png(bytestring=svg(fn(flat),N).encode(),output_width=N,output_height=N)
    return Image.open(io.BytesIO(png)).convert('RGB')
def quant64(im):
    pal=[]
    for r in (0,0x55,0xAA,0xFF):
        for g in (0,0x55,0xAA,0xFF):
            for b in (0,0x55,0xAA,0xFF): pal+=[r,g,b]
    p=Image.new('P',(1,1)); p.putpalette(pal+[0]*(768-len(pal)))
    return im.quantize(palette=p,dither=Image.Dither.NONE).convert('RGB')

if __name__=='__main__':
    tag=sys.argv[1]
    row=Image.new('RGB',(4*(500+20)+20,500+128+60),(235,235,240))
    for i,(k,fn) in enumerate(PROPS.items()):
        big=render(fn,500); row.paste(big,(20+i*520,10))
        x=20+i*520
        for s in (128,64,48):
            row.paste(render(fn,s),(x,520)); x+=s+10
        m=quant64(render(fn,128,flat=True)); row.paste(m,(x,520))
    row.save(f'prev_{tag}.png')
