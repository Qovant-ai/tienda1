# Bitácora de cambios

Registro de todos los cambios en la tienda (Shopify, AutoDS y configuración). El más reciente va primero.

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

Intento fallido: arnés + correa, cama redonda de felpa y túnel de fieltro (proveedores privados de AutoDS,
error `SupplierProductDoesntExist` al usar el ID de la tienda del proveedor). Se reintentó con el ID de AutoDS.

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
