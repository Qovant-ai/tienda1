"""Recorta los productos de regalo con rembg (modelo isnet-general-use).

Uso: <venv>/bin/python cutout_gifts.py <carpeta_fotos> <carpeta_recortes>
Cada producto se recorta antes a la zona indicada (fracciones de ancho y alto).
"""
import sys,os
from PIL import Image
from rembg import remove, new_session
src,out=sys.argv[1],sys.argv[2]
crops={'P1':(0,0,1,1),'P3':(0.80,0.03,0.995,0.41),'P4':(0,0,1,1),'P5':(0,0,1,0.67),
 'P6':(0,0.22,0.64,1),'P7':(0,0.1,0.62,1),'P8':(0.6,0.12,1,0.56),
 'P11':(0,0.27,0.86,1),'P12':(0,0,1,1),'P13':(0,0,1,0.6),'P14':(0.05,0.1,0.56,0.72)}
# P2, P9 y P10 van con cutout_white_bg.py.
sess=new_session('isnet-general-use')
for n,(a,b,c,d) in crops.items():
    im=Image.open(os.path.join(src,n+'.png')).convert('RGB'); w,h=im.size
    im=im.crop((int(a*w),int(b*h),int(c*w),int(d*h)))
    o=remove(im,session=sess,post_process_mask=True)
    bb=o.getchannel('A').point(lambda v:255 if v>12 else 0).getbbox()
    o=o.crop(bb)
    if n=='P11':  # quita la marca de medidas que queda en el borde derecho
        o=o.crop((0,0,int(o.width*0.96),o.height)); o=o.crop(o.getchannel('A').point(lambda v:255 if v>12 else 0).getbbox())
    o.save(os.path.join(out,n+'.png')); print(n,o.size,flush=True)
