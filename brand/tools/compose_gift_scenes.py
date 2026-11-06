"""Arma las escenas de Gift List Co: fondo de color, círculo suave, sombra y recortes.

Uso: python3 compose_gift_scenes.py <carpeta_recortes> <carpeta_salida> brand/gift-images/scenes.json
"""
import sys,os,json
from PIL import Image, ImageDraw, ImageFilter
cut,out,spec=sys.argv[1],sys.argv[2],json.load(open(sys.argv[3]))
os.makedirs(out,exist_ok=True)
def hexrgb(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
def mix(a,b,t): return tuple(int(a[i]+(b[i]-a[i])*t) for i in range(3))
for name,s in spec.items():
    W,H=s['size']; bg=hexrgb(s['bg'])
    img=Image.new('RGB',(W,H),bg)
    circ=Image.new('L',(W,H),0); d=ImageDraw.Draw(circ)
    cx,cy,r=s['circle']; d.ellipse((cx-r,cy-r,cx+r,cy+r),fill=255)
    tone=hexrgb(s.get('circle_color','#ffffff')); img.paste(Image.new('RGB',(W,H),mix(bg,tone,s.get('circle_mix',0.45))),(0,0),circ)
    items=[]
    for it in s['items']:
        p=Image.open(os.path.join(cut,it['p']+'.png')).convert('RGBA')
        bw,bh=it['box']; sc=min(bw/p.width,bh/p.height); p=p.resize((max(1,int(p.width*sc)),max(1,int(p.height*sc))),Image.LANCZOS)
        x=int(it['cx']-p.width/2); y=int(it['by']-p.height); items.append((p,x,y))
    # floor shadows under each item
    sh=Image.new('L',(W,H),0); sd=ImageDraw.Draw(sh)
    for p,x,y in items:
        ew=p.width*0.92; eh=max(18,p.width*0.10); bx=x+p.width/2; by=y+p.height
        sd.ellipse((bx-ew/2,by-eh/2,bx+ew/2,by+eh/2),fill=int(255*s.get('shadow',0.22)))
    sh=sh.filter(ImageFilter.GaussianBlur(18))
    img.paste(Image.new('RGB',(W,H),mix(bg,(0,0,0),0.55)),(0,0),sh)
    for p,x,y in items: img.paste(p,(x,y),p)
    img.save(os.path.join(out,name+'.jpg'),quality=88,optimize=True,progressive=True); print(name)
