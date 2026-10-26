# Fotos de producto Pawlet Club

Creadas el 27-oct-2026 para reemplazar las fotos del proveedor, que mezclaban fondos, textos en chino,
logos ajenos y etiquetas de color.

## Orden de la galería (igual en los 8 productos)

1. **Foto principal**: el producto recortado sobre un fondo crema con sombra suave, mismo encuadre en todos.
   Es la que se ve en la portada, las colecciones y la búsqueda.
2. **Foto en uso**: la mejor foto del proveedor con una mascota o en una casa (aparece al pasar el mouse).
3. **Beneficios**: infografía con 4 razones de compra, ícono y texto corto.
4. **Guía de tallas o medidas**, cuando el proveedor da datos confiables (cama, rascador árbol, caja de juego).
5. **Mejores fotos del proveedor**: detalles y ambientes, sin textos en otros idiomas ni collages.
6. **Una foto limpia por color o versión**, asignada a su variante (al elegir el color cambia la foto).
7. **Garantía Pawlet**: envío gratis desde $30, 30 días para devolver, envío desde EE. UU., pago seguro.

Se eliminaron 41 fotos del proveedor (duplicadas, con texto en chino, dimensiones que no coincidían,
etiquetas de color o collages).

## Archivos

| Ruta | Qué es |
|---|---|
| `spec.json` | Textos de cada infografía, guía de tallas y recortes por variante |
| `final/` | Las 38 imágenes subidas a Shopify (1600 × 1600 px) |
| `../tools/cutout_products.py` | Recorta el producto de la foto del proveedor (rembg, modelos `isnet-general-use` y `u2net`) |
| `../tools/make_product_images.py` | Arma una página HTML por imagen con la paleta, Rubik y el logo |
| `../tools/render_product_images.js` | Convierte esas páginas en JPG con Chromium |

## Cómo rehacerlas o agregar un producto

```bash
# 1. Fotos del proveedor: AutoDS guarda una copia en
#    https://autods-scraper-images.s3-us-west-2.amazonaws.com/<hash>.png
#    (el <hash> es el nombre del archivo en Shopify).
# 2. Recortes (PNG transparentes) en una carpeta, por ejemplo cut/
python cutout_products.py <carpeta_base> jobs.txt     # requiere: pip install "rembg[cpu]"
# 3. Agregar el producto a spec.json y generar las páginas y los JPG
PAWLET_FONTS=<carpeta con Rubik-400.ttf y Rubik-600.ttf> \
  python3 brand/tools/make_product_images.py brand/product-images/spec.json cut/ html/
node brand/tools/render_product_images.js html/ out/
```

## Pendientes

- **Arnés**: el proveedor solo tiene una foto y muestra el logo VEVOR. Pedir fotos sin marca o cambiar de proveedor.
- **Fotos propias**: cuando haya inventario, una sesión con mascotas reales usando los productos reemplaza
  la foto en uso de cada producto y sube la conversión más que cualquier infografía.
