# Imágenes de Gift List Co

Creadas el 6-nov-2026 con las fotos de los proveedores de los 14 productos. Todas siguen el mismo estilo:
**fondo de color, un círculo suave y los productos recortados sobre una sombra de piso**.

## Dónde se usan

| Imagen | Uso | Tamaño |
|---|---|---|
| `giftlist-hero.jpg` | Portada (marco 4:5) | 1120 × 1400 |
| `giftlist-why.jpg` | Franja "Why Gift List Co" (4:5) | 960 × 1200 |
| `giftlist-for-*.jpg` | Tarjetas "Who are you shopping for?" e imagen de cada colección | 1000 × 1000 |
| `giftlist-all.jpg` | Tarjeta y colección "All Gifts" (fondo oscuro) | 1000 × 1000 |

| Tarjeta | Productos | Fondo |
|---|---|---|
| For Your Daughter | Rizador + mini impresora | `#fce1ec` |
| For Your Son | Proyector astronauta + cámara | `#dceafa` |
| For Mom | Masajeador de ojos + calentador rosado | `#ffe4dc` |
| For Dad | Aspiradora + almohada masajeadora | `#e2e7ef` |
| For Your Girlfriend | Rosa eterna + espejo LED | `#fbe0e3` |
| For Your Boyfriend | Calentador gris + aspiradora | `#dff0ea` |
| For Grandma | Almohada masajeadora + calentador rosado | `#f3e6f5` |
| For Grandpa | Almohada masajeadora + calentador gris | `#ece6dc` |
| Best Friend (Her) | Mini impresora + calentador rosado | `#ffe9d6` |
| Best Friend (Him) | Proyector + calentador gris | `#e6e3f7` |
| For Your Pet | Puzzle + pelota dispensadora | `#fff1c7` |
| All Gifts | Almohada, proyector, rosa e impresora | `#24203f` |

## Archivos

| Ruta | Qué es |
|---|---|
| `scenes.json` | Tamaño, fondo, círculo y posición de cada producto en cada escena |
| `cut/P1.png` … `cut/P14.png` | Recortes con fondo transparente (los códigos P1–P14 son los de `docs/tienda-regalos.md`) |
| `final/` | Las imágenes subidas a Shopify (Archivos) |

## Cómo rehacerlas

Las fotos originales son la imagen principal de cada producto en AutoDS
(`autods-scraper-images.s3-us-west-2.amazonaws.com/<id>.png`, ver la tabla de productos en
`docs/tienda-regalos.md`). Guárdalas como `P1.png` … `P14.png` en una carpeta y:

```bash
# 1. Recortes: rembg para casi todos; por color para los que están sobre blanco (rizador, cámara, aspiradora)
<venv con rembg>/bin/python brand/tools/cutout_gifts.py <fotos> brand/gift-images/cut
python3 brand/tools/cutout_white_bg.py <fotos> brand/gift-images/cut
# 2. Escenas
python3 brand/tools/compose_gift_scenes.py brand/gift-images/cut brand/gift-images/final brand/gift-images/scenes.json
```

rembg recortaba mal tres productos: el rizador (peluche rosado claro), la cámara (rosada clara sobre blanco) y
la aspiradora (le comía la base negra). Por eso esos tres se recortan por color de fondo.
