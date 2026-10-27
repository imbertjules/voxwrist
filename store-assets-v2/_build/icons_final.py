from icon import make_icon
from PIL import Image
import io
O='/workspace/voxstore/assets-v2/'
ic=make_icon(500); ic.save(O+'voxwrist-ask-cover-500.png',optimize=True)
big=make_icon(1000)
d128=big.resize((128,128),Image.LANCZOS).convert('RGB'); d128.save(O+'voxwrist-ask-device-icon-128-fullcolor.png',optimize=True)
# 64-colour Garmin palette (levels 00,55,AA,FF)
pal=[]
for r in (0,0x55,0xAA,0xFF):
  for g in (0,0x55,0xAA,0xFF):
    for b in (0,0x55,0xAA,0xFF): pal+= [r,g,b]
pimg=Image.new('P',(1,1)); pimg.putpalette(pal+[0]*(768-len(pal)))
lc=d128.quantize(palette=pimg,dither=Image.Dither.FLOYDSTEINBERG)
lc.convert('RGB').save(O+'voxwrist-ask-device-icon-128-64color.png',optimize=True)
lc_nd=d128.quantize(palette=pimg,dither=Image.Dither.NONE)
P=Image.new('RGB',(128*3*3+20,128*3),(255,255,255))
for k,im in enumerate([d128,lc,lc_nd]): P.paste(im.convert('RGB').resize((384,384),Image.NEAREST),(k*394,0))
P.save('dev_icons_prev.png')
