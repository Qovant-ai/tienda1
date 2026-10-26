# Bitácora de cambios

Registro de todos los cambios en la tienda (Shopify, AutoDS y configuración). El más reciente va primero.

## 2026-10-27 (10) — Fotos de producto nuevas y textos corregidos

Pedido del dueño: mejorar la presentación de los productos ("las fotos por defecto son horribles y nada
estratégicas") según 4 videos de YouTube. **No se pudieron ver los videos**: YouTube está bloqueado en este
entorno. Se aplicaron las prácticas habituales de fotos de producto para e-commerce.

### Fotos (ver [`brand/product-images/README.md`](brand/product-images/README.md))
- 38 imágenes nuevas de 1600 × 1600 px: 8 fotos principales (producto recortado sobre fondo crema), 8
  infografías de beneficios, 3 guías de tallas o medidas, 18 fotos limpias por color o versión y 1 imagen de
  garantía Pawlet (en los 8 productos).
- Galerías reordenadas: principal → en uso → beneficios → tallas → fotos del proveedor → colores → garantía.
- Cada variante muestra su foto limpia (cama 8 colores, túnel 3, correa retráctil 5, cepillo 5).
- **41 fotos del proveedor eliminadas**: texto en chino, collages, etiquetas de color, medidas que no
  coincidían con las variantes y duplicadas. Textos alternativos descriptivos en las que quedan.
- Imágenes de colección: Sleep & Groom usa la nueva foto de la cama; Play & Scratch, un gato dentro del túnel.
- Herramientas: `brand/tools/cutout_products.py` (recorte con rembg), `make_product_images.py` y
  `render_product_images.js` (HTML → JPG con la paleta, Rubik y el logo).

### Textos corregidos al revisar las fotos
| Antes | Ahora | Por qué |
|---|---|---|
| Stainless Steel Grooming Comb (`stainless-steel-grooming-comb`) | **Self-Cleaning Slicker Brush for Cats & Dogs** (`self-cleaning-slicker-brush`) | Es un cepillo con botón autolimpiable; la versión "Set" trae un guante de aseo |
| Cat Scratch Pad with Interactive Balls (`cat-scratch-pad-interactive-balls`) | **Interactive Cat Play Box with Balls & Pom-Pom** (`interactive-cat-play-box`) | Es una caja tipo laberinto con pelotas y pompón con resorte |
| Collapsible Cat Tunnel & Hideout (`collapsible-cat-tunnel`) | **Peek-a-Boo Felt Cat Tunnel & Hideout** (`peek-a-boo-cat-tunnel`) | Es de fieltro con agujeros y broches; se arma como túnel o queda plano |
| Cama L "small-to-medium dogs" | S hasta 9 lb, M hasta 13 lb, **L hasta 22 lb** | Tabla de tallas del proveedor |

Los handles viejos redirigen a los nuevos. Descripción, SEO y traducción al español actualizados en los 5
productos tocados (también el rascador árbol: base de 15.7 in).

## 2026-10-26 (9) — Tema v2 publicado y revisión

- El dueño publicó **"Pawlet Club v2"** (`189339795518`, ahora MAIN). "Pawlet Club" (`189338452030`) quedó
  sin publicar.
- Revisión por API: los archivos del tema publicado coinciden con los de `theme/`; los 8 productos usan la
  plantilla estándar, están disponibles y tienen stock; todas las colecciones y páginas enlazadas están
  publicadas. No se pudo ver la tienda: la red de este entorno bloquea `mcgsp1-yj.myshopify.com`.
- Peine: opción "quantity" (1Pcs / 2Pcs) renombrada a **"Pack"** (1 comb / 2 combs) y "Color" a
  **"Style"** (incluye la variante "Set"). Descripción y traducciones al español actualizadas.
- Pendiente en el editor de temas (la API no permite editar el tema publicado): texto del pie de página,
  que todavía habla solo de cajas mensuales.

## 2026-10-26 (8) — Catálogo limpio y rediseño para vender (tema "Pawlet Club v2")

Pedido del dueño: "que se vea dónde están los productos, intuitivo y profesional" y "todo lo que tiene que
estar publicado, publicado; lo que no sirve, eliminado".

### Catálogo
| Acción | Detalle |
|---|---|
| **Eliminados** (Shopify) | Holiday Box · Limited Edition y los 7 extras "Add to Your Box" (placa grabada, bolsas, juguete resistente, kit dental, bandana, varita, toallitas). Nunca se vendieron y no tenían inventario. Quedan registrados en `data/catalogo-shopify.csv` |
| **Colecciones eliminadas** | `frontpage` (vacía, del tema), `limited-edition`, `add-to-your-box` |
| **Página eliminada** | Track Order (sin uso) |
| **Activos y publicados** | Los 8 artículos dropship, todos con fotos |
| **Borradores que se mantienen** | Club Dog, Club Cat, Gift the Club Dog y Gift the Club Cat (lanzamiento enero 2027) y sus colecciones `the-club` y `gift-the-club`, sin publicar |
| **Fotos nuevas** | Correa retráctil: 13 fotos desde AutoDS (una por color, asignada a su variante; se descartaron 2 con textos "US Seller"/"HOT"). Arnés: 1 foto (el proveedor solo tiene esa y muestra el logo VEVOR) |
| **Textos alternativos** | 60 fotos con el título del proveedor (texto de relleno) pasan a una descripción corta en inglés |

### Colecciones nuevas (publicadas, automáticas por etiqueta)
`shop-all` (etiqueta `a-la-carte`, 8), `leashes-harnesses` (etiqueta `walk`, 3), `play-scratch` (`play`, 3), `sleep-groom`
(`rest`, 2). `shop-for-dogs` y `shop-for-cats` ahora están publicadas (antes no). Todas con imagen,
descripción, SEO y traducción al español.

### Descripciones de producto
Las 8 reescritas con la misma estructura: introducción, "Why you'll love it", "Details". Título y
descripción SEO nuevos. Traducción al español actualizada (cuerpo y SEO). El envío y las devoluciones
salen ahora de un bloque del tema, no del texto de cada producto.

### Menús
| Menú | Ahora |
|---|---|
| `main-menu` | Shop All (Todos, Leashes & Harnesses, Play & Scratch, Sleep & Groom) · Dogs · Cats · The Club · FAQ |
| `footer-club` "Shop" | Shop All, Shop for Dogs, Shop for Cats, The Club, About Us |

Antes enlazaban a Club Dog, Club Cat y Gift the Club, que están en borrador (daban error 404).
Todos los enlaces del menú tienen traducción al español.

### Páginas
- FAQ: reorganizada en Pedidos y envíos, Devoluciones, El Club y Ayuda. Sin el juguete resistente eliminado.
- How It Works: aviso de lanzamiento en enero 2027 y enlace a la lista de espera (`/#club`); "Extras" se
  cambia por "While you wait" con enlace a la tienda.
- Refund Policy: sin la sección de placas grabadas. Shipping Policy: sin "Add to Your Box" ni "limited
  edition". About Us: incluye la tienda.
- Traducidas al español: FAQ, How It Works, Refund Policy, Shipping Policy, About Us y el título de Contact.

### Tema "Pawlet Club v2" (`gid://shopify/OnlineStoreTheme/189339795518`, sin publicar)
Copia del tema publicado. Ver [`theme/README.md`](theme/README.md).
- **Inicio**: portada con botones "Shop dogs" / "Shop cats", barra de confianza, categorías con foto
  (perros, gatos, paseo, juego, descanso, todo), grilla con los 8 productos y compra rápida, franja
  "Why Pawlet Club", el Club con **lista de espera** (correo → cliente con etiquetas
  `newsletter, club-waitlist`) y preguntas frecuentes.
- **Producto**: galería con miniaturas, selector de variantes con botones, beneficios junto al botón de
  compra (envío, origen, devoluciones, pago seguro), acordeón de envío / devoluciones / ayuda,
  "You may also like" y barra de confianza.
- **Colección**: barra de confianza al final.
- Compra rápida también en celular.
- Theme Check sin errores en los archivos propios.
- Shopify rechazó (sin mensaje) un rótulo con el tipo de producto sobre el título; se quitó. Quedó una
  plantilla de prueba `product.ta` en el tema que la API no permite borrar.

## 2026-10-26 (7) — Tienda a la carta publicada

- El dueño confirma que **mantiene AutoDS** (pedidos automáticos de la tienda a la carta).
- Los **8 artículos dropship** pasan a **ACTIVO** y se publican en el canal **Tienda online**
  (`gid://shopify/Publication/228083990590`): rascador árbol de Navidad, rascador con pelotas, peine,
  correa de cuerda, túnel, cama cueva, arnés + correa y correa retráctil. Precios verificados sin cambios.
- El rascador árbol de Navidad usaba una plantilla de producto propia de AutoDS
  (`product.31-5in-christmas-tree-cat`); ahora usa la plantilla estándar del tema.
- Siguen en **borrador**: Club Dog, Club Cat, los 2 regalos, Holiday Box y los 7 extras (faltan
  suscripciones, aprobación de PayPal e inventario).
- Pendiente antes de vender: completar en las políticas el correo de soporte y la razón social de la SpA,
  y quitar la contraseña de la tienda cuando se decida abrir.

## 2026-10-26 (6) — Logo, paleta y página de inicio de Pawlet Club

### Identidad (ver [`brand/README.md`](brand/README.md))
- Logo elegido: **huella grande y chica** (propuesta 8) con la **paleta 1**: azul noche `#1B2B48`, durazno
  `#FF9F6E`, crema `#FFF3EA`. Tipografía **Rubik**.
- Archivos en `brand/logo/` (SVG con texto en trazos + PNG). Subidos a Shopify Files:
  `pawlet-logo-horizontal.png`, `pawlet-logo-horizontal-white.png`, `pawlet-favicon.png`, `pawlet-icon.png`.
- Fotos de Unsplash subidas para la portada y la franja de regalo (`photo-1599194921977-…`,
  `photo-1686419682443-…`). Una tercera foto se subió y se borró porque mostraba una caja de otra marca.

### Tema nuevo "Pawlet Club" (sin publicar) — ver [`theme/README.md`](theme/README.md)
- Copia de Helio: `gid://shopify/OnlineStoreTheme/189338452030`.
- `settings_data.json`: logo, logo blanco, favicon, Rubik, paleta de marca, botones redondeados.
- Encabezado blanco sin transparencia; pie de página con boletín (durazno) y columnas de enlaces (azul).
- **Página de inicio nueva** con 7 secciones propias: portada, cómo funciona, planes Club Dog/Club Cat,
  qué trae cada caja, tienda a la carta, regalo y preguntas frecuentes. Pasó Theme Check sin errores.

### Menús
| Menú | Cambio |
|---|---|
| `footer-club` "Pawlet Club" | **Creado**: Club Dog, Club Cat, Gift the Club, Shop for Dogs, Shop for Cats, About Us |
| `footer` "Help" | Renombrado y reordenado: How It Works, FAQ, Contact, las 4 políticas y Your Privacy Choices |

### Páginas con la marca
About Us (incluye el significado de "Pawlet"), Terms of Service ("Pawlet Club is a brand operated by…"),
Refund Policy, Subscription Terms y Shipping Policy. Mismos cambios en `docs/politicas-usa/`.

### Pendiente (dueño)
- **Publicar el tema "Pawlet Club"** (la API no permite publicarlo).
- Nombre de la tienda → "Pawlet Club" y comprar `pawletclub.com`.
- Activar los productos cuando estén listas las suscripciones.

## 2026-10-26 (5) — Marca Pawlet Club y PayPal

### Marca
- Nombre elegido por el dueño: **Pawlet Club** (*paw* + *-let*, "patita"). No se encontró una marca "Pawlet"
  registrada en EE. UU. (búsqueda web; falta confirmar en USPTO). Dominio sugerido: `pawletclub.com` (disponible
  al 26-oct, sin comprar).
- Shopify: proveedor de los **20 productos** cambiado de "Club Mascotas" a **"Pawlet Club"**. Título SEO de
  Club Dog, Club Cat y los dos regalos terminado en "| Pawlet Club".
- Pendiente: nombre de la tienda (solo en el admin), marca en páginas y políticas, logo.
- Logo: 9 propuestas en un lienzo privado de Claude (3 rondas: conceptos, variaciones de la patita-caja,
  patitas y huellas). Falta elegir.

### Pagos
- **PayPal conectado** por el dueño. Siguiente paso: pedir a PayPal las transacciones de referencia
  (necesarias para cobrar la suscripción cada mes) e instalar Shopify Subscriptions.

## 2026-10-26 (4) — Tienda lista para EE. UU.: páginas, menús, envíos y tienda a la carta

### Configuración
| Cambio | Detalle |
|---|---|
| Moneda | **USD** (cambiada por el dueño en el admin) |
| Envíos | Tarifa gratis corregida a USD. **Gratis desde $30** ("Free standard shipping") y **$5.99** por debajo ("Standard shipping") |
| Pesos | Peso por variante en los 12 productos del Club y extras (cajas 2–3.5 lb; extras 0.1–0.8 lb) |
| SEO | Título y descripción SEO en Club Dog, Club Cat y los dos regalos |

### Páginas (en inglés; reemplazan las plantillas vacías de AutoDS y usan la plantilla estándar de Horizon)
| Página | Handle | Acción |
|---|---|---|
| About Us | `about-us` | Contenido nuevo |
| FAQ | `faqs` | 11 preguntas (precio, cobros, pausa, alergias, regalos, pagos, envíos, daños, español) |
| How It Works | `how-it-works` | **Creada** |
| Subscription Terms | `subscription-terms` | **Creada** (términos de renovación automática para EE. UU.) |
| Refund Policy | `return-policy` | Política de reembolsos |
| Shipping Policy | `shipping-policy` | Política de envíos (actualizada con el umbral de $30) |
| Terms of Service | `terms-and-conditions` | Términos |
| Track Order | `track-order` | **Despublicada** (dependía de una app de AutoDS) |

### Menús
- **Principal:** Club Dog · Club Cat · Gift the Club · Shop (Shop for Dogs, Shop for Cats, Add to Your Box) · How It Works · FAQ.
- **Pie de página:** How It Works · FAQ · About Us · Contact · Shipping Policy · Refund Policy · Subscription Terms · Terms of Service · Your Privacy Choices · Search.

### Colecciones nuevas (automáticas por etiqueta)
| ID | Colección | Regla |
|---|---|---|
| 512782532670 | Shop for Dogs (`shop-for-dogs`) | etiqueta `shop-dog` |
| 512782565438 | Shop for Cats (`shop-for-cats`) | etiqueta `shop-cat` |

Los 7 extras quedaron etiquetados `a-la-carte` + `shop-dog` y/o `shop-cat`.

### Tienda a la carta (dropshipping con AutoDS) — ver `docs/tienda-a-la-carta.md`
Importados desde CJdropshipping (bodega en EE. UU.) y pasados de inmediato a **BORRADOR**, con títulos y descripciones reescritos:

| Shopify ID | Producto | Precio | Costo proveedor |
|---|---|---|---|
| 15445481357374 | Christmas Tree Cat Scratching Post · 31.5 in | $39.99 | $16.97 (envío gratis) |
| 15445481455678 | Cat Scratch Pad with Interactive Balls | $34.99 | $16.27 (envío gratis) |
| 15445482274878 | Stainless Steel Grooming Comb for Cats & Dogs | $16.99 (2-pack $24.99) | $1.99–7.72 + envío |
| 15445482635326 | Heavy-Duty Rope Leash · 6 ft, Reflective | $17.99 | $6.29 (envío gratis) |

Desde proveedores privados de AutoDS (bodega en EE. UU.). El primer intento falló con
`SupplierProductDoesntExist` (se usó el ID de la tienda del proveedor); funcionó con el ID de AutoDS:

| Shopify ID | Producto | Precio | Costo proveedor |
|---|---|---|---|
| 15445488009278 | Calming Plush Cave Bed for Cats & Small Dogs | S $34.99 · M $42.99 · L $52.99 | $9.78–20.57 + $7.29 envío |
| 15445487943742 | Collapsible Cat Tunnel & Hideout | 24 in $29.99 · 35 in $34.99 | $7.24–11.27 + $7.29 envío |
| 15445490499646 | No-Pull Harness + 5 ft Leash Set · Large Dogs | $29.99 | $12.95 (envío gratis) |
| 15445490696254 | Retractable Dog Leash · 16.5 ft | $24.99 | $9.91 (envío gratis) |

En los 8: título, descripción, handle y tipo en inglés, proveedor "Club Mascotas", etiquetas `shop-dog`/`shop-cat`,
traducción al español y opciones legibles (tallas en pulgadas y cm; "Bliue" → "Blue", "Grey" → "Gray").
AutoDS había cargado la cama a $395–645 (regla de precios de AutoDS); se corrigió a mano.

### No aplicado
- Código **WELCOME30** (30% en la primera caja): Shopify no permite descuentos de suscripción hasta que
  esté instalada una app de suscripciones. Crear después de instalar Shopify Subscriptions.

## 2026-10-26 (3) — Configuración para EE. UU. primero, con PayPal

### Decisión del dueño
Una sola tienda, a nombre de la SpA chilena, cobrando con **PayPal**. Secuencia **EE. UU. → México → Chile**.
La dirección fiscal de Miami **no se usa por ahora** (no es necesaria con PayPal; se evaluará para Shopify Payments).
Guía: [`docs/fase-1-estados-unidos.md`](docs/fase-1-estados-unidos.md).

### Shopify
| Cambio | Detalle |
|---|---|
| Mercado creado | **Estados Unidos** (`gid://shopify/Market/63897501758`, handle `us`), activo, impuesto sumado en el checkout |
| Mercado modificado | **Chile** → borrador (fase 3). México sigue en borrador (fase 2) |
| Envíos | Perfil general: eliminadas las zonas heredadas de AutoDS "Domestic" (México: 150/0/195 MXN) e "International" (360 MXN). Creada la zona **"Estados Unidos (48 estados + DC)"** con **"Free standard shipping" (3–7 business days)** a US$0 |
| Productos (12) | Títulos, descripciones, handles, tipos y opciones **en inglés**; **precios en USD** (Club Dog 39.99, Club Cat 32.99, etc.; ver `data/catalogo-shopify.csv`) |
| Colecciones (4) | En inglés: The Club · Monthly Subscription (`the-club`), Gift the Club (`gift-the-club`), Limited Edition (`limited-edition`), Add to Your Box (`add-to-your-box`) |
| Traducciones | **Español** registrado para los 12 productos y las 4 colecciones (título, descripción, handle y tipo), adaptado a EE. UU. (envío, libras). Las opciones de variante siguen solo en inglés |
| Texto "eco" | Se quitó "biodegradables/compostables" de las bolsas (en EE. UU. requiere certificación) |

### Pendiente en el admin (no se puede por API)
- Moneda de la tienda **MXN → USD** (los precios ya están en dólares).
- Políticas en inglés: [`docs/politicas-usa/`](docs/politicas-usa/) (falta el permiso `write_legal_policies`).
- PayPal Business + transacciones de referencia · instalar Shopify Subscriptions.

## 2026-10-26 (2) — Estructura por países y conversión a tienda Chile
*(Reemplazado por la entrada (3): el mercado Chile quedó en borrador y los textos pasaron a inglés.)*

### Decisión
- Estructura: **1 marca, 2 entidades, 2 tiendas**. Esta tienda = **tienda Chile** (SpA chilena);
  una **LLC en EE. UU.** operará la tienda Global (EE. UU. y, después, México vía filial).
  Detalle: [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md).
- Tema **Horizon** publicado (por el dueño).

### Shopify
| Cambio | Detalle |
|---|---|
| Mercado creado | **Chile** (`gid://shopify/Market/63897370686`, handle `cl`), activo |
| Mercado modificado | **México** (`gid://shopify/Market/63857557566`) → borrador |
| Idioma | Español (`es`) agregado y publicado. El predeterminado sigue en inglés (solo se cambia en el admin) |
| Descripciones | Club Perro, Club Gato, Regala Perro, Regala Gato y Caja Navideña adaptadas a Chile (despacho a Chile continental, marcas locales, medios de pago) |

### No aplicado (falta permiso o requiere el admin)
- Políticas: el conector no tiene el permiso `write_legal_policies`. Textos listos en
  [`docs/politicas-chile/`](docs/politicas-chile/) para pegarlos en *Configuración → Políticas*.
- Moneda (MXN → CLP), zona horaria e idioma predeterminado: solo desde el admin.
- Precios en CLP: preparados en `data/catalogo-shopify.csv`; se cargan después del cambio de moneda.

## 2026-10-26 (1) — Auditoría y catálogo inicial

### Auditoría
- Revisión inicial de Shopify y AutoDS → [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md).
- Hallazgos críticos: precios en MXN con cifras de USD (p. ej., cepillo a $7.99 MXN), negocio registrado
  en **Chile**, zona horaria de Nueva York y prueba de AutoDS que vence el 29-oct.

### AutoDS + Shopify — productos eliminados (10)
Eliminados de AutoDS **y** de Shopify (`remove_from_marketplace: true`), a petición del dueño.
Snapshot previo: [`data/eliminados-autods-2026-10-26.csv`](data/eliminados-autods-2026-10-26.csv).

| Shopify ID | Producto |
|---|---|
| 15443389251646 | Cat Tree for Large Cats Cat Tower for Indoor |
| 15443389153342 | Dog Drinking Water Bowl with Floating Design |
| 15443388923966 | Dog Paw Cleaner |
| 15443388727358 | Dog Umbrella |
| 15443388629054 | Automatic Retractable Dog Leash |
| 15443388399678 | 4 in 1 Electric Pet Grooming Kit |
| 15443388366910 | Cat Litter Trapping Mat |
| 15443388137534 | Luxury Plush Shark Pet Bed |
| 15443387973694 | Automatic Cat Toy – Interactive Smart LED Laser |
| 15443387580478 | Electric Cat Steam Brush – 3-In-1 |

### Shopify — colecciones creadas (4)
| ID | Colección | Handle |
|---|---|---|
| 512769753150 | El Club · Suscripción mensual | `el-club-suscripcion-mensual` |
| 512769785918 | Regala el Club | `regala-el-club` |
| 512769818686 | Edición limitada | `edicion-limitada` |
| 512769851454 | Añade a tu caja | `anade-a-tu-caja` |

### Shopify — productos creados (12, todos en BORRADOR)
Detalle de variantes, SKU y costos objetivo: [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv).

| ID | Producto | Precio MXN |
|---|---|---|
| 15443418021950 | Club Perro · Caja mensual | 649 |
| 15443418153022 | Club Gato · Caja mensual | 579 |
| 15443418382398 | Regala el Club Perro · Pago único | 699 / 1,857 / 3,534 |
| 15443418579006 | Regala el Club Gato · Pago único | 629 / 1,650 / 3,150 |
| 15443418710078 | Caja Navideña · Edición limitada | 799 / 799 / 699 |
| 15443418906686 | Placa de identificación grabada | 199 |
| 15443419004990 | Bolsas biodegradables · 8 rollos + dispensador | 149 |
| 15443419103294 | Juguete extra resistente · masticadores fuertes | 249 |
| 15443419201598 | Kit dental · cepillo de dedo + pasta enzimática | 169 |
| 15443419299902 | Bandana temática del mes | 149 |
| 15443419398206 | Varita con plumas + 3 repuestos | 139 |
| 15443419496510 | Toallitas para patas y pelaje · 100 piezas | 119 |

Notas:
- Las 5 cajas llevan una foto **provisional** de Unsplash (licencia de uso libre); los extras aún no tienen foto.
- Proveedor provisional: "Club Mascotas" (cambiar al definir la marca).
- Sin planes de suscripción: deben crearse desde la app Shopify Subscriptions (ver `PLAN.md` §6.4).
- Inventario sin seguimiento y sin peso por variante (pendiente).

### Repositorio
- Creados `README.md`, `PLAN.md`, `CHANGELOG.md`, `docs/auditoria-2026-10-26.md` y `data/`.
