from lib import *
import sys
N=500; SS=2
def make_icon(N=500,pal='aurore',accent='lagon'):
    W=N*SS
    bg=background(W,W,[(W*0.5,W*0.5,W*0.50,hx('3B22A8'),0.30),(W*0.05,W*1.0,W*0.45,PAL['lagon'][0],0.22),(W*0.95,W*0.0,W*0.45,hx('8a2a7a'),0.18)],
                  base_top=hx('170F40'),base_bot=hx('0A0824'),grain=0.0)
    img=to_img(bg).convert('RGBA')
    R=W*0.27; cx=cy=W/2
    # sound-wave rings (thick, soft)
    x,y=grid(W,W)
    d=np.sqrt((x-cx)**2+(y-cy)**2)
    ang=np.arctan2(y-cy,x-cx)
    rings=np.zeros((W,W))
    for k,(rr,wd,a) in enumerate([(1.30,0.045,0.55),(1.58,0.040,0.33),(1.84,0.035,0.17)]):
        # arcs only left and right (voice)
        side=np.abs(np.cos(ang))**2.2
        rings+=np.exp(-((d-R*rr)/(R*wd))**2)*a*side
    ringcol=PAL['aurore'][2]*0.55+PAL['aurore'][1]*0.25+PAL['lagon'][2]*0.2
    arr=np.asarray(img.convert('RGB')).astype(float)/255
    arr=1-(1-arr)*(1-np.clip(rings,0,1)[...,None]*ringcol)
    # glow halo
    g=np.exp(-np.clip(d/R-1,0,None)/0.42)*(d>0)
    gc=PAL['aurore'][0]*0.55+PAL['aurore'][1]*0.45
    arr=1-(1-arr)*(1-np.clip(g*0.60,0,1)[...,None]*gc)
    img=to_img(arr).convert('RGBA')
    orb,_=orb_layer((W,W),R,cx,cy,pal=pal,accent=accent,ss=1,swirl=1.3)
    img.alpha_composite(orb)
    return img.resize((N,N),Image.LANCZOS).convert('RGB')
if __name__=='__main__':
    im=make_icon()
    im.save('icon_test.png')
    # preview at several sizes
    P=Image.new('RGB',(500+256+128+64+48+60,500),(240,240,240))
    x=0
    for s in (500,256,128,64,48):
        P.paste(im.resize((s,s),Image.LANCZOS),(x,0)); x+=s+10
    P.save('icon_prev_%s.png'%(sys.argv[1] if len(sys.argv)>1 else 'x'))
