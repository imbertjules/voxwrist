from props import *
import sys
sys.path.insert(0,'/workspace/voxstore/build')
from lib import font
from PIL import ImageDraw
P='/workspace/voxstore/assets-v2/proposals/'
DESC={'A':'Bot on dark indigo, glow + sound-wave rings','B':'Bot inside an abstract round watch face','C':'Bot + speech bubble with voice wave (Lagon)','D':'Crisp vector bot on vibrant sunrise gradient','E':'Faceless aurora orb (icon only)'}
for k,fn in PROPS.items():
    render(fn,500).save(P+f'{k}-cover-500.png',optimize=True)
    big=render(fn,1000).resize((128,128),Image.LANCZOS); big.save(P+f'{k}-device-icon-128-fullcolor.png',optimize=True)
    quant64(render(fn,128,flat=True)).save(P+f'{k}-device-icon-128-64color.png',optimize=True)
rowH=600; W=1500
S=Image.new('RGB',(W,90+5*rowH),(250,250,252)); d=ImageDraw.Draw(S)
d.text((30,24),'Voxwrist Ask: icon proposals A–E',font=font('head',44,'Bold'),fill=(20,16,40))
for i,k in enumerate('ABCDE'):
    y=90+i*rowH
    cov=Image.open(P+f'{k}-cover-500.png').convert('RGB')
    f128=Image.open(P+f'{k}-device-icon-128-fullcolor.png').convert('RGB')
    m128=Image.open(P+f'{k}-device-icon-128-64color.png').convert('RGB')
    s48=cov.resize((48,48),Image.LANCZOS)
    d.text((30,y+8),f'{k}',font=font('head',48,'ExtraBold'),fill=(20,16,40))
    d.text((90,y+20),DESC[k],font=font('body',26,'SemiBold'),fill=(70,66,95))
    S.paste(cov,(30,y+70))
    # light panel
    d.rounded_rectangle((560,y+70,960,y+570),radius=18,fill=(238,238,243))
    S.paste(f128,(590,y+100)); S.paste(s48,(750,y+140)); S.paste(m128,(590,y+300))
    d.text((590,y+235),'128 full colour',font=font('body',18,'Medium'),fill=(90,90,110)); d.text((750,y+195),'48 px',font=font('body',18,'Medium'),fill=(90,90,110)); d.text((590,y+435),'128 MIP 64-colour',font=font('body',18,'Medium'),fill=(90,90,110))
    d.text((580,y+530),'on light',font=font('body',18,'Medium'),fill=(120,120,140))
    # dark panel
    d.rounded_rectangle((990,y+70,1470,y+570),radius=18,fill=(18,16,26))
    S.paste(f128,(1020,y+100)); S.paste(s48,(1180,y+140)); S.paste(m128,(1020,y+300))
    d.text((1020,y+235),'128 full colour',font=font('body',18,'Medium'),fill=(170,170,190)); d.text((1180,y+195),'48 px',font=font('body',18,'Medium'),fill=(170,170,190)); d.text((1020,y+435),'128 MIP 64-colour',font=font('body',18,'Medium'),fill=(170,170,190))
    d.text((1010,y+530),'on dark (watch)',font=font('body',18,'Medium'),fill=(150,150,170))
    # 48 on dark: also tiny 1:1 next to 2x zoom
    S.paste(s48.resize((96,96),Image.NEAREST),(1300,y+100)); d.text((1300,y+200),'48 px ×2',font=font('body',18,'Medium'),fill=(170,170,190))
S.save('/workspace/voxstore/assets-v2/icon-proposals.png',optimize=True)
S.resize((W//2,(90+5*rowH)//2),Image.LANCZOS).save('sheet_prev.png')
