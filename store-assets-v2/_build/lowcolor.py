from PIL import Image, ImageDraw
O='/workspace/voxstore/assets-v2/'
S=8; N=128*S
im=Image.new('RGB',(N,N),(0x00,0x00,0x55))
d=ImageDraw.Draw(im)
c=N/2
# glow disc
d.ellipse((c-N*0.40,c-N*0.40,c+N*0.40,c+N*0.40),fill=(0x55,0x00,0xAA))
# rings (left/right arcs)
for r,col,w in [(0.47,(0x55,0x55,0xAA),5),(0.40,(0xAA,0x55,0xFF),6)]:
    R=N*r
    d.arc((c-R,c-R,c+R,c+R),140,220,fill=col,width=w*S//2)
    d.arc((c-R,c-R,c+R,c+R),-40,40,fill=col,width=w*S//2)
R=N*0.30
d.ellipse((c-R,c-R,c+R,c+R),fill=(0x55,0x55,0xFF))
# pink upper-right lobe
m=Image.new('L',(N,N),0); md=ImageDraw.Draw(m); md.ellipse((c-R,c-R,c+R,c+R),fill=255)
lay=Image.new('RGB',(N,N),(0xFF,0x55,0xAA)); lm=Image.new('L',(N,N),0); ImageDraw.Draw(lm).ellipse((c-R*0.1,c-R*1.3,c+R*1.5,c+R*0.25),fill=255)
from PIL import ImageChops
im.paste(lay,(0,0),ImageChops.multiply(lm,m))
lay=Image.new('RGB',(N,N),(0x55,0xFF,0xFF)); lm=Image.new('L',(N,N),0); ImageDraw.Draw(lm).ellipse((c+R*0.05,c+R*0.05,c+R*1.6,c+R*1.6),fill=255)
im.paste(lay,(0,0),ImageChops.multiply(lm,m))
lay=Image.new('RGB',(N,N),(0xAA,0x55,0xFF)); lm=Image.new('L',(N,N),0); ImageDraw.Draw(lm).ellipse((c-R*1.4,c-R*0.2,c+R*0.2,c+R*1.4),fill=255)
im.paste(lay,(0,0),ImageChops.multiply(lm,m))
# highlight
d.ellipse((c-R*0.62,c-R*0.68,c-R*0.18,c-R*0.42),fill=(0xFF,0xFF,0xFF))
# rim
d.ellipse((c-R,c-R,c+R,c+R),outline=(0xFF,0xAA,0xFF),width=S*2)
small=im.resize((128,128),Image.LANCZOS)
pal=[]
for r in (0,0x55,0xAA,0xFF):
  for g in (0,0x55,0xAA,0xFF):
    for b in (0,0x55,0xAA,0xFF): pal+=[r,g,b]
p=Image.new('P',(1,1)); p.putpalette(pal+[0]*(768-len(pal)))
q=small.quantize(palette=p,dither=Image.Dither.NONE).convert('RGB')
q.save('/workspace/voxstore/assets-v2/proposals/E-device-icon-128-64color.png',optimize=True)
q.resize((384,384),Image.NEAREST).save('lc_prev.png')
print(len(set(q.getdata())))
