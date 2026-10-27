# Imágenes de escena Pawlet Club

Creadas el 27-oct-2026 para reemplazar las fotos de stock elegidas a ciegas (perro en caja con texto en japonés,
estatua de dálmata, etc.). Todas usan el mismo estilo: **fondo de color de la marca, un círculo suave y recortes
reales** de mascotas y productos sobre una sombra de piso.

## Dónde se usan

| Imagen | Uso | Tamaño |
|---|---|---|
| `pawlet-cat-dogs-v2.jpg` | Colección Shop for Dogs (tarjeta grande de la portada) | 1600 × 1120 |
| `pawlet-cat-cats-v2.jpg` | Colección Shop for Cats (tarjeta grande) | 1600 × 1120 |
| `pawlet-cat-walk.jpg`, `-play`, `-sleep`, `-all` | Colecciones Walk, Play & Scratch, Sleep & Groom y Shop All | 1000 × 1000 |
| `pawlet-why.jpg` | Franja "Why Pawlet Club" de la portada (tema v4) | 960 × 1200 |
| `pawlet-club-dog.jpg`, `pawlet-club-cat.jpg` | Foto principal de Club Dog y Club Cat | 1600 × 1600 |
| `pawlet-club-*-inside.jpg`, `pawlet-club-*-plans.jpg` | "Qué trae cada caja" y planes 1/3/6 meses | 1600 × 1600 |
| `pawlet-gift-dog.jpg`, `pawlet-gift-cat.jpg` | Foto principal de Gift the Club Dog / Cat | 1600 × 1600 |
| `pawlet-col-club.jpg`, `pawlet-col-gift.jpg` | Colecciones The Club y Gift the Club | 1600 × 1600 |

Las tarjetas grandes van con el texto a la izquierda: el sujeto ocupa el 45 % derecho. En celular y tablet la
imagen va arriba y se recorta desde la derecha (4:3), así que el sujeto nunca queda tapado.

Colores de fondo: celeste `#dcebf7` (perros), durazno `#ffe7d6` (gatos), menta `#ddf1e6` (paseo),
mantequilla `#fff1c7` (juego), rosa `#fde4e1` (descanso), azul marino `#1b2b48` (todo).

## Archivos

| Ruta | Qué es |
|---|---|
| `scenes.json` | Posición, tamaño y fondo de cada escena |
| `cut/` | Recortes de mascotas y cajas (el resto son los recortes de productos de `../product-images`) |
| `final/` | Las imágenes subidas a Shopify |
| `../tools/compose_scenes.py` | Arma una página HTML por escena |
| `../tools/render_scenes.js` | Convierte esas páginas en JPG |
| `../tools/make_club_box.py` | Dibuja la caja del Club (Club Dog, Club Cat, The Club y regalo) |

Los recortes de mascotas salen de fotos de los proveedores (`dog.png`: beagle del arnés, con el logo VEVOR
borrado; `cat_sit`, `cat_tunnel_gray`: túnel; `cat_tree`: rascador árbol; `kitten_bed`: cama), con rembg.

## Cómo rehacerlas

```bash
# 1. Recortes de productos (ver ../product-images/README.md) + los de cut/ en una sola carpeta
# 2. Páginas y JPG
python3 brand/tools/compose_scenes.py brand/scene-images/scenes.json <carpeta_recortes> html/ [nombres]
node brand/tools/render_scenes.js html/ out/ [nombres]
```
