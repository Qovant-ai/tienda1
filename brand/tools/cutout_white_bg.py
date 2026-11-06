"""Recorta productos sobre fondo blanco por color (sin IA).

Uso: python3 cutout_white_bg.py <carpeta_fotos> <carpeta_recortes>
"""
import sys,os
from PIL import Image, ImageDraw, ImageFilter, ImageChops
src,out=sys.argv[1],sys.argv[2]
def key(n,crop,thr=238,global_white=False):
    im=Image.open(os.path.join(src,n+'.png')).convert('RGB'); w,h=im.size; a,b,c,d=crop
    im=im.crop((int(a*w),int(b*h),int(c*w),int(d*h)))
    px=im.load(); W,H=im.size
    m=Image.new('L',(W,H),0); mp=m.load()
    for y in range(H):
        for x in range(W):
            r,g,bb=px[x,y]
            if min(r,g,bb)>thr and max(r,g,bb)-min(r,g,bb)<14: mp[x,y]=255
    if global_white:
        bg=m
    else:
        for seed in [(0,0),(W-1,0),(0,H-1),(W-1,H-1),(W//2,0),(W//2,H-1),(0,H//2),(W-1,H//2)]:
            if mp[seed]==255: ImageDraw.floodfill(m,seed,128)
        bg=m.point(lambda v:255 if v==128 else 0)
    alpha=ImageChops.invert(bg).filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(1.2))
    o=im.convert('RGBA'); o.putalpha(alpha)
    bbox=alpha.point(lambda v:255 if v>20 else 0).getbbox(); o=o.crop(bbox)
    o.save(os.path.join(out,n+'.png')); print(n,o.size)

if __name__ == '__main__':
    # Productos sobre fondo blanco que rembg recorta mal (ver brand/gift-images/README.md).
    key('P2', (0.45, 0, 1, 0.97), thr=236, global_white=True)   # rizador: el blanco del centro del lazo también sale
    key('P9', (0, 0, 1, 0.56))                                   # cámara rosada clara
    im = Image.open(os.path.join(out, 'P9.png')); im.crop((85, 0, 735, 435)).save(os.path.join(out, 'P9.png'))  # sin correa ni línea
    key('P10', (0, 0.19, 0.3, 1))                                # aspiradora negra, sin el efecto de aire de arriba
