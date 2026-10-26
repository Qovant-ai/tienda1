# Tema "Pawlet Club v2"

Copia del tema publicado "Pawlet Club" (familia Horizon 4.3.0), con la tienda y los productos al frente.
Creada el 26-oct-2026.

| | |
|---|---|
| ID del tema | `gid://shopify/OnlineStoreTheme/189339795518` |
| Origen | "Pawlet Club" (`189338452030`, publicado) |
| Estado | **Sin publicar.** Se revisa en *Tienda online → Temas → Pawlet Club v2 → Vista previa* y se publica desde ahí |

Esta carpeta guarda **solo los archivos modificados o nuevos**, con el mismo contenido que se subió al tema.

## Páginas

**Inicio** (`templates/index.json`), en este orden:
1. Portada: "Everyday favorites for your best friend, delivered." con botones *Shop dogs* y *Shop cats*.
2. Barra de confianza: envío gratis desde $30, garantía de 30 días, pago seguro con PayPal, atención en
   inglés y español.
3. Categorías con foto: Shop for Dogs y Shop for Cats (grandes), Walk, Play & Scratch, Sleep & Groom y
   Shop All.
4. "Our best sellers": grilla con los 8 productos (compra rápida en computador y celular).
5. "Why Pawlet Club": franja azul con foto.
6. El Club: tarjetas de Club Dog y Club Cat con el sello "Launching January 2027" y **lista de espera**.
   El correo crea un cliente con las etiquetas `newsletter, club-waitlist` (filtrar en *Clientes*).
   Cuando los productos del Club se activen, los botones llevan solos al producto.
7. Preguntas frecuentes.

**Producto** (`templates/product.json`): galería con miniaturas, título y precio, variantes con botones,
botón de compra, beneficios (`pawlet-product-perks`), descripción, acordeón de envío / devoluciones / ayuda
(`pawlet-product-accordion`), "You may also like" y barra de confianza.

**Colección** (`templates/collection.json`): la del tema más la barra de confianza al final.

## Archivos

| Archivo | Qué es |
|---|---|
| `config/settings_data.json` | Logo, colores, Rubik y compra rápida también en celular |
| `sections/header-group.json`, `sections/footer-group.json` | Encabezado y pie (sin cambios en v2) |
| `templates/index.json` | Página de inicio |
| `templates/product.json` | Página de producto |
| `templates/collection.json` | Página de colección |
| `snippets/pawlet-styles.liquid` | Colores de marca y estilos compartidos |
| `snippets/pawlet-icon.liquid` | Íconos en SVG (huellas, caja, camión, escudo, candado, devolución, etc.) |
| `sections/pawlet-hero.liquid` | Portada |
| `sections/pawlet-trust.liquid` | Barra de confianza (hasta 4 promesas) |
| `sections/pawlet-categories.liquid` | Tarjetas de categoría: usan la imagen de la colección y muestran cuántos productos tiene |
| `sections/pawlet-plans.liquid` | Planes del Club con lista de espera |
| `sections/pawlet-gift.liquid` | Franja con foto y puntos (se usa para "Why Pawlet Club") |
| `sections/pawlet-faq.liquid` | Preguntas frecuentes |
| `sections/pawlet-steps.liquid`, `pawlet-inside.liquid`, `pawlet-shop.liquid` | Secciones de la v1 (cómo funciona, qué trae la caja, mosaicos). Siguen disponibles en el editor |
| `blocks/pawlet-product-perks.liquid` | Beneficios junto al botón de compra. Dice "Free US shipping" si el producto cuesta $30 o más |
| `blocks/pawlet-product-accordion.liquid` | Envío, devoluciones y ayuda, desplegables |

Todo se edita desde el editor de temas. Los archivos propios pasaron **Theme Check** sin errores.

## Notas

- Shopify rechazó, sin mensaje, un rótulo con el tipo de producto (`{{ closest.product.type }}`) sobre el
  título; se quitó.
- Quedó una plantilla de prueba `templates/product.ta.json`. La API no permite borrar archivos del tema:
  se puede borrar en *Editar código*. No afecta a nada.
- Los textos del tema están en inglés. Para traducirlos: *Configuración → Idiomas → Español → Traducir*
  (o la app Translate & Adapt).
