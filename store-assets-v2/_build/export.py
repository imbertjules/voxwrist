import shots, hero, io
from PIL import Image
O='/workspace/voxstore/assets-v2/'
names=['1-ask-voice','2-daily-brief','3-voice-reminders','4-follow-up','5-live-orb']
for l in ('en','fr'):
    for i in range(5):
        im=shots.make(l,i)
        q,sz=shots.save_small(im,O+f'voxwrist-ask-screenshot-{names[i]}-{l}.jpg')
        print(names[i],l,q,sz)
    h=hero.make(l)
    h.save(O+f'voxwrist-ask-hero-1440x720-{l}.png',optimize=True)
    q,sz=shots.save_small(h,O+f'voxwrist-ask-hero-1440x720-{l}.jpg',limit=600*1024)
# cover jpg fallback (<150KB)
c=Image.open(O+'voxwrist-ask-cover-500.png')
print('cover jpg',shots.save_small(c,O+'voxwrist-ask-cover-500.jpg'))
