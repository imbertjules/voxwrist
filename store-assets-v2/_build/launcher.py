from lib import *
from PIL import Image, ImageDraw
O='/workspace/voxstore/launcher/'
import os; os.makedirs(O,exist_ok=True)
def full(size):
    S=8; W=size*S
    img=Image.new('RGBA',(W,W),(0,0,0,0))
    R=W*0.40
    # soft glow (alpha) around the orb
    x,y=grid(W,W); d=np.sqrt((x-W/2)**2+(y-W/2)**2)
    g=np.exp(-np.clip(d/R-1,0,None)/0.18)*(d>=R*0.98)*0.55
    gc=PAL['aurore'][0]*0.55+PAL['aurore'][1]*0.45
    gl=Image.fromarray((np.dstack([np.broadcast_to(gc,(W,W,3)),g[...,None]])*255).astype(np.uint8),'RGBA')
    img.alpha_composite(gl)
    orb,_=orb_layer((W,W),R,W/2,W/2,pal='aurore',accent='lagon',ss=1,swirl=1.3)
    img.alpha_composite(orb)
    return img.resize((size,size),Image.LANCZOS)
def flat(size):
    S=8; N=size*S; c=N/2; R=N*0.42
    im=Image.new('RGBA',(N,N),(0,0,0,0)); d=ImageDraw.Draw(im)
    d.ellipse((c-R,c-R,c+R,c+R),fill=(0x55,0x55,0xFF,255))
    from PIL import ImageChops
    m=Image.new('L',(N,N),0); ImageDraw.Draw(m).ellipse((c-R,c-R,c+R,c+R),fill=255)
    for col,box in [((0xFF,0x55,0xAA),(c-R*0.1,c-R*1.3,c+R*1.5,c+R*0.25)),((0x55,0xFF,0xFF),(c+R*0.05,c+R*0.05,c+R*1.6,c+R*1.6)),((0xAA,0x55,0xFF),(c-R*1.4,c-R*0.2,c+R*0.2,c+R*1.4))]:
        lm=Image.new('L',(N,N),0); ImageDraw.Draw(lm).ellipse(box,fill=255)
        im.paste(Image.new('RGBA',(N,N),col+(255,)),(0,0),ImageChops.multiply(lm,m))
    d.ellipse((c-R*0.62,c-R*0.68,c-R*0.18,c-R*0.42),fill=(255,255,255,255))
    d.ellipse((c-R,c-R,c+R,c+R),outline=(0xFF,0xAA,0xFF,255),width=S*2)
    sm=im.resize((size,size),Image.LANCZOS)
    a=np.asarray(sm).copy(); a[...,3]=np.where(a[...,3]>110,255,0)  # hard alpha for MIP
    rgb=a[...,:3].astype(int); rgb=((rgb+42)//85*85).clip(0,255); a[...,:3]=rgb
    return Image.fromarray(a.astype(np.uint8),'RGBA')
for s in (60,65,54):
    full(s).save(O+f'launcher_{s}.png')
flat(40).save(O+'launcher_40.png')
P=Image.new('RGB',(4*140,140),(0,0,0))
for i,s in enumerate((65,60,54,40)):
    im=Image.open(O+f'launcher_{s}.png'); bg=Image.new('RGBA',im.size,(0,0,0,255)); bg.alpha_composite(im)
    P.paste(bg.convert('RGB').resize((s*2,s*2),Image.NEAREST),(i*140+5,5))
P.save('launcher_prev.png')
