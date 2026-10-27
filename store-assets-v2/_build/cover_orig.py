from PIL import Image
import numpy as np
O='/workspace/voxstore/assets-v2/'
src=Image.open('/workspace/voxstore/src/dist/icon-ask-500.png').convert('RGBA')
def on(bgcol,size,pad):
    c=Image.new('RGBA',(size,size),bgcol+(255,))
    s=size-2*pad
    c.alpha_composite(src.resize((s,s),Image.LANCZOS),(pad,pad))
    return c.convert('RGB')
cov=on((255,255,255),500,10); cov.save(O+'voxwrist-ask-cover-500.png',optimize=True)
cov.save(O+'voxwrist-ask-cover-500.jpg',quality=95,optimize=True)
d=on((0,0,0),128,4); d.save(O+'voxwrist-ask-device-icon-128-fullcolor.png',optimize=True)
pal=[]
for r in (0,0x55,0xAA,0xFF):
  for g in (0,0x55,0xAA,0xFF):
    for b in (0,0x55,0xAA,0xFF): pal+=[r,g,b]
p=Image.new('P',(1,1)); p.putpalette(pal+[0]*(768-len(pal)))
lc=d.quantize(palette=p,dither=Image.Dither.NONE).convert('RGB'); lc.save(O+'voxwrist-ask-device-icon-128-64color.png',optimize=True)
P=Image.new('RGB',(500+20+256+20+256,500),(120,120,130)); P.paste(cov,(0,0)); P.paste(d.resize((256,256),Image.NEAREST),(520,0)); P.paste(lc.resize((256,256),Image.NEAREST),(796,0)); P.save('orig_prev.png')
