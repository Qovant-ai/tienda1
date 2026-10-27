# Tema "Pawlet Club v4"

Copia de "Pawlet Club v3" (familia Horizon 4.3.0) con las tarjetas de categoría rediseñadas, la franja "Why"
corregida y un aviso para visitantes de fuera de EE. UU. Creada el 27-oct-2026.

| Tema | ID | Estado |
|---|---|---|
| **Pawlet Club v4** | `gid://shopify/OnlineStoreTheme/189374595134` | **Sin publicar: falta que el dueño lo publique** |
| Pawlet Club v3 | `gid://shopify/OnlineStoreTheme/189348905022` | Publicado (27-oct-2026): Club abierto, sin lista de espera |
| Pawlet Club v2 | `gid://shopify/OnlineStoreTheme/189339795518` | Sin publicar |
| Pawlet Club | `gid://shopify/OnlineStoreTheme/189338452030` | Sin publicar (v1) |

La API no permite editar el tema publicado: los cambios se hacen en el editor o en una copia nueva.

Esta carpeta guarda **solo los archivos modificados o nuevos**, con el mismo contenido que se subió al tema.

## Páginas

**Inicio** (`templates/index.json`), en este orden:
1. Portada: "Everyday favorites for your best friend, delivered." con botones *Shop dogs* y *Shop cats*.
2. Barra de confianza: envío gratis desde $30, garantía de 30 días, pago seguro con PayPal, atención en
   inglés y español.
3. Categorías: Shop for Dogs y Shop for Cats (grandes, estilo "studio": texto a la izquierda y la escena a la
   derecha, sin degradado), Walk, Play & Scratch, Sleep & Groom y Shop All. Cada tarjeta toma el color de
   fondo de su imagen (`card_color`); las imágenes son las de las colecciones (`brand/scene-images/`).
4. "Our best sellers": grilla con los 8 productos (compra rápida en computador y celular).
5. "Why Pawlet Club": franja azul con la escena del beagle y el gato. En v4 se arregló que los 3 puntos
   salían en azul sobre azul (invisibles).
6. El Club ("Now open"): tarjetas de Club Dog y Club Cat con el precio del producto ("desde" el plan de
   1 mes) y botón al producto. Planes prepagados de 1, 3 o 6 meses, sin renovación automática.
   La lista de espera sigue disponible en la sección (*Show waitlist form*), apagada.
7. Preguntas frecuentes (incluye cómo funciona el Club).

**Producto** (`templates/product.json`): galería con miniaturas, título y precio, variantes con botones,
botón de compra, beneficios (`pawlet-product-perks`), descripción, acordeón de envío / devoluciones / ayuda
(`pawlet-product-accordion`), "You may also like" y barra de confianza.

**Colección** (`templates/collection.json`): la del tema más la barra de confianza al final.

## Archivos

| Archivo | Qué es |
|---|---|
| `config/settings_data.json` | Logo, colores, Rubik y compra rápida también en celular |
| `sections/header-group.json`, `sections/footer-group.json` | Encabezado y pie. v3: texto de marca y del boletín sin "launch". v4: aviso de envío arriba del encabezado |
| `sections/pawlet-ship-notice.liquid` | Barra para visitantes de países sin mercado activo (hoy, todo lo que no es EE. UU.): Shopify les muestra los productos como "Unavailable"; la barra explica que enviamos a EE. UU. y cambia la tienda a EE. UU. con un clic. En inglés o español según el idioma |
| `templates/index.json` | Página de inicio |
| `templates/product.json` | Página de producto |
| `templates/collection.json` | Página de colección |
| `snippets/pawlet-styles.liquid` | Colores de marca y estilos compartidos |
| `snippets/pawlet-icon.liquid` | Íconos en SVG (huellas, caja, camión, escudo, candado, devolución, etc.) |
| `sections/pawlet-hero.liquid` | Portada |
| `sections/pawlet-trust.liquid` | Barra de confianza (hasta 4 promesas) |
| `sections/pawlet-categories.liquid` | Tarjetas de categoría: usan la imagen de la colección y muestran cuántos productos tiene. v4: color de tarjeta y estilo "studio" para las grandes |
| `sections/pawlet-plans.liquid` | Planes del Club (lista de espera opcional mientras un plan no está a la venta) |
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
