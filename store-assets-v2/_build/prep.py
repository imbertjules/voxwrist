from PIL import Image, ImageFilter; import numpy as np, glob
S='/workspace/voxstore/src/'
def crop(p): return np.asarray(Image.open(p).convert('RGB').crop((609-416,866-416,609+416,866+416))).astype(float)
fs=sorted(glob.glob(S+'f8/f8-*.png'))
stack=np.stack([crop(f).max(-1) for f in fs])
static=(stack>35).all(0)
y,x=np.mgrid[0:832,0:832]; r=np.sqrt((x-416)**2+(y-416)**2)
static&=(r>300)&(np.sqrt((x-416)**2+(y-120)**2)>115)
m=Image.fromarray((static*255).astype(np.uint8)).filter(ImageFilter.MaxFilter(5))
static=np.asarray(m)>0
print('static px',static.sum())
def clean(path,out):
    a=crop(path)
    a[static]=0
    a[r>404]=0
    Image.fromarray(a.astype(np.uint8)).resize((416,416),Image.LANCZOS).save(out)
for l in ('en','fr'):
    clean(S+f'f8/f8-{l}-8-followup.png',f'scr-followup-{l}.png')
