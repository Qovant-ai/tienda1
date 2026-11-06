# Tema "Gift List Co v1"

Copia del tema "Pawlet Club v4" (familia Horizon) convertida en tienda de regalos. Creada el 6-nov-2026.

| Tema | ID | Estado |
|---|---|---|
| **Gift List Co v1** | `gid://shopify/OnlineStoreTheme/189702766654` | **Sin publicar: falta que el dueño lo publique** |
| Pawlet Club v4 | `gid://shopify/OnlineStoreTheme/189374595134` | Publicado (tienda de mascotas, ya sin productos activos) |

Vista previa: <https://mcgsp1-yj.myshopify.com/?preview_theme_id=189702766654>

Esta carpeta guarda **solo los archivos que cambian** respecto de v4. Se generan con
`python3 brand/tools/build_giftlist_theme.py theme theme-giftlist` (lee los de `theme/` y aplica los cambios).
Los nombres internos de las secciones siguen siendo `pawlet-*`; los clientes no los ven.

## Qué cambió

- **Marca**: logo Gift List Co (`brand/logo-giftlist/`), favicon y paleta nueva: tinta `#24203f`, coral
  `#f2675f`, crema `#fff6f0`, rosa suave `#ffe4e1`. Los íconos de huella pasaron a regalo y destellos.
- **Portada** (`templates/index.json`), en este orden:
  1. "Holiday gift guide 2026 · Find the perfect gift for everyone you love." Botones *Shop all gifts* y
     *Gifts for Mom*. Insignia "Shipping $0 every US order".
  2. Barra de confianza: envío gratis en todo pedido, 30 días para devoluciones, pago seguro, atención en
     inglés y español.
  3. **"Who are you shopping for?"**: 12 tarjetas (los 11 destinatarios y All Gifts), cada una con su escena
     y su color. Se subió el límite de la sección a 16 tarjetas.
  4. "Best-selling gifts" (colección `gifts`).
  5. "Why Gift List Co: Gift-giving, solved" (franja oscura).
  6. Preguntas frecuentes (envío, regalo directo a quien lo recibe, devoluciones, pago, español).
  Se quitó la sección del Club.
- **Producto** (`templates/product.json`): "Free US shipping" siempre (umbral 0), envío de 4–8 días hábiles,
  devoluciones y barra de confianza nuevas.
- **Colección** (`templates/collection.json`): barra de confianza nueva.
- **Pie de página** (`sections/footer-group.json`): texto de marca y del boletín de Gift List Co; el menú
  "Shop" muestra All Gifts, Mom, Dad, Her, Him, Kids y About Us.

## Lo que vive fuera del tema (ya hecho en Shopify)

- Menú principal: **Shop by recipient** (11 destinatarios), All Gifts, FAQ y Contact. Los menús son de la
  tienda, así que ya se ven también en el tema publicado.
- 12 colecciones automáticas por etiqueta (`for-mom`, `for-dad`, … y `gift-list-co` para All Gifts).
- Páginas About, FAQ, How It Works, Refund, Shipping y Terms reescritas en inglés y español.
