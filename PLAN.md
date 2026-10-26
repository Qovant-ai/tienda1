# Plan maestro: club mensual de cajas para perros y gatos

**Secuencia:** 🇺🇸 Estados Unidos → 🇲🇽 México → 🇨🇱 Chile · **Cobro:** PayPal · **Entidad:** SpA chilena · **Una sola tienda**
**Actualizado:** 26-oct-2026 · **Fase actual:** [`docs/fase-1-estados-unidos.md`](docs/fase-1-estados-unidos.md) ·
**Cambios:** [`CHANGELOG.md`](CHANGELOG.md) · **Estado inicial:** [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md)

> Las cifras de costos y precios son **supuestos de trabajo** que hay que validar con cotizaciones reales.
> Se marcan con *(supuesto)*.

---

## 0. Estado

| # | Acción | Estado |
|---|---|---|
| 1 | Eliminar los 10 productos de AutoDS y crear el catálogo del club | ✅ |
| 2 | Publicar el tema Horizon | ✅ (por ti) |
| 3 | Configurar la tienda para EE. UU.: mercado, envíos, catálogo en inglés y USD, traducción al español | ✅ |
| 4 | **Moneda de la tienda → USD** | ✅ Hecho (por ti) |
| 5 | **PayPal Business + transacciones de referencia** (necesarias para suscripciones) | ✅ PayPal conectado · ⏳ Tú: pedir las transacciones de referencia |
| 6 | Shopify Subscriptions · políticas en inglés | ⏳ Tú |
| 7 | **AutoDS: mantenerlo** (lo necesita la tienda a la carta) y elegir el plan más barato antes del 29-oct 00:16 UTC | ⏳ Tú |
| 8 | Páginas, menús, envíos ($30+ gratis), pesos y SEO · tienda a la carta con productos ganadores | ✅ Hecho (ver `docs/tienda-a-la-carta.md`) |
| 9 | Marca **Pawlet Club**: logo, paleta, tema y página de inicio | ✅ Hecho · ⏳ Tú: publicar el tema "Pawlet Club", cambiar el nombre de la tienda y comprar el dominio |

---

## 1. Concepto y propuesta de valor

**Un club mensual, como los clubes de vino, para perros y gatos:** cada mes llega una caja temática con
5–6 productos elegidos según el perfil de la mascota (especie, tamaño, edad, alergias, tipo de mordida).

**Diferenciadores:** personalización real · temas por país (Thanksgiving, Día de Muertos, Fiestas Patrias) ·
**tienda bilingüe** que atiende también a la comunidad latina de EE. UU. (BarkBox y Meowbox no lo hacen) ·
donación a refugios · pausar, saltar o cancelar en 2 clics · línea Senior.

**Marca:** **Pawlet Club** (elegida el 26-oct): logo de huella grande y chica, azul noche y durazno.
Guía: [`brand/README.md`](brand/README.md).

---

## 2. Productos y precios

Detalle con IDs y SKU: [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv). Hoy la tienda tiene
cargados los precios en **USD**.

| Producto (EN / ES) | 🇺🇸 USD | 🇲🇽 MXN | 🇨🇱 CLP |
|---|---|---|---|
| Club Dog / Club Perro · mensual | 39.99 | 649 | 29.990 |
| Club Cat / Club Gato · mensual | 32.99 | 579 | 26.990 |
| Gift the Club Dog / Regala el Club Perro · 1 / 3 / 6 meses | 44.99 / 113.97 / 215.94 | 699 / 1,857 / 3,534 | 32.990 / 85.490 / 163.990 |
| Gift the Club Cat / Regala el Club Gato · 1 / 3 / 6 meses | 36.99 / 94.47 / 179.94 | 629 / 1,650 / 3,150 | 29.990 / 76.990 / 147.990 |
| Holiday Box / Caja Navideña · perro / gato | 44.99 / 39.99 | 799 / 699 | 36.990 / 32.990 |
| Engraved Pet ID Tag / Placa grabada | 14.99 | 199 | 8.990 |
| Waste Bags / Bolsas · 8 rollos + dispensador | 9.99 | 149 | 6.990 |
| Heavy-Duty Chew Toy / Juguete extra resistente | 16.99 | 249 | 11.990 |
| Dental Kit / Kit dental | 11.99 | 169 | 7.990 |
| Monthly Theme Bandana / Bandana temática | 9.99 | 149 | 6.990 |
| Feather Wand / Varita + 3 repuestos | 9.99 | 139 | 6.490 |
| Paw & Coat Wipes / Toallitas · 100 | 8.99 | 119 | 5.490 |

**Opciones de compra:** mensual con renovación automática · regalo o prepago de 1, 3 o 6 meses (pago
único) · edición limitada · extras que viajan dentro de la caja · **artículos por separado (tienda a la carta)**: correas, arneses, camas, rascadores, túneles y cepillos, elegidos por demanda y margen. Detalle: [`docs/tienda-a-la-carta.md`](docs/tienda-a-la-carta.md).

**Envío:** gratis en pedidos de $30+ (todas las cajas califican); $5.99 por debajo.

---

## 3. Selección inteligente de productos

### 3.1 Criterios (puntuación de 1 a 5; entran solo los que suman ≥ 28 de 35)

| Criterio | Qué se busca | Peso |
|---|---|---|
| Valor percibido vs. costo | Precio en tienda ≥ 3× el costo | ×1.5 |
| Peso y volumen | ≤ 250 g, plano o compacto | ×1.5 |
| Seguridad | Sin piezas pequeñas, materiales no tóxicos | Filtro (si falla, no entra) |
| Recompra / consumible | Se gasta y se vuelve a necesitar | ×1 |
| Temático y fotogénico | Se adapta al tema del mes y luce en el *unboxing* | ×1 |
| Abastecimiento local | Proveedor en el país, con stock y factura | ×1 |
| Universal por talla | Sirve a la mayoría de perfiles | ×1 |

### 3.2 Lo que NO entra
Alimento completo y arena · camas y árboles · electrónicos con batería · premios importados (permisos
sanitarios: FDA en EE. UU., SENASICA en México, SAG en Chile) · juguetes con piezas pequeñas · productos
genéricos de dropshipping.

**Ojo con los reclamos "eco" en EE. UU.:** no usar "biodegradable" ni "compostable" en bolsas u otros
plásticos sin una certificación (ASTM D6400); California lo restringe. Por eso el texto en inglés solo dice
"leak-proof".

### 3.3 Por qué está cada producto
- **Club Dog y Club Cat:** ingreso recurrente.
- **Regalos y prepagos:** captan a quien no quiere suscripción y no dependen de la aprobación de cobros automáticos de PayPal.
- **Holiday Box:** opcional, si el inventario llega a tiempo.
- **Extras:** viajan en la misma caja (sin envío extra) y casi duplican el margen del pedido.

### 3.4 Primeras cajas en EE. UU. *(propuesta)*

| Mes | Tema | Club Dog | Club Cat |
|---|---|---|---|
| Ene 2027 | New Year, New Habits | Tapete olfativo o juguete dispensador · kit dental · snacks bajos en calorías · bolsas · bandana | Rascador de cartón · pelota con catnip · snack funcional · kit dental · sorpresa |
| Feb 2027 | Puppy Love / Cat Crush | Peluche corazón · cuerda roja · 2 snacks · bálsamo para patas · bandana de San Valentín | Corazón con catnip · repuesto de varita · snack lamible · toallitas · sorpresa |
| Mar 2027 | Spring Adventures | Juguete para exterior · snacks · toallitas · bolsas · bandana | Juguete con plumas · catnip · snack · cepillo · sorpresa |

Cada caja: valor en tienda ≥ 1.6× el precio · costo de productos ≤ US$10 (perro) / US$8 (gato) · peso ≤ 3 lb.

---

## 4. Operación

**Modelo:** inventario propio + armado de cajas en un **3PL** de cada país. Nada depende de dónde vivas.

| País | 3PL a cotizar | Abastecimiento |
|---|---|---|
| 🇺🇸 EE. UU. | ShipMonk · ShipBob (bodega en un estado sin sales tax, si conviene) | Mayoristas en EE. UU.; marcas hechas en EE. UU. o México |
| 🇲🇽 México | Cubbo · Melonn · 99minutos | Mayoristas en CDMX y GDL |
| 🇨🇱 Chile | Amplifica · Blue Express Fulfillment | Mayoristas en Santiago; snacks con registro SAG |

**Calendario mensual:** día 1 cobro y corte · días 1–3 lista de armado por perfil · días 4–8 armado ·
días 8–10 despacho · día 15 avance del tema siguiente · día 25 recordatorio para saltar o cambiar.

---

## 5. Economía por caja (EE. UU., con PayPal) *(supuestos)*

| Club Dog mensual | US$ |
|---|---|
| Precio (sales tax aparte donde aplique) | 39.99 |
| Productos | –10.00 |
| Empaque | –2.00 |
| Armado en el 3PL | –3.50 |
| Envío USPS (2–3 lb) | –9.00 |
| PayPal (~5–6% + 30¢) + Shopify (2%) | –3.30 |
| Apps | –0.40 |
| **Margen de contribución** | **≈ 11.80 (29%)** |

Con Shopify Payments (vía la dirección de Miami, si cumple los requisitos) el margen subiría a ~33%.
**Metas:** retención ≥ 6 meses · CAC máximo ≈ US$25 · cancelación < 10% mensual · ≥ 30% de prepagos ·
≥ 25% de pedidos con un extra.

---

## 6. Pagos: PayPal por fases

| Fase | Moneda de cobro | Suscripción mensual | Notas |
|---|---|---|---|
| 🇺🇸 EE. UU. | USD | Shopify Subscriptions + PayPal (requiere **transacciones de referencia** aprobadas por PayPal) | Comisión de Shopify del 2% por usar una pasarela externa en el plan Basic |
| 🇲🇽 México | USD (PayPal convierte al cliente) | Igual | Sin Shopify Payments no se puede cobrar en MXN en el checkout |
| 🇨🇱 Chile | USD (PayPal no acepta CLP) | Igual | Alternativas: Shopify Payments con CLP, o una tienda chilena con Flow |

**Mejora futura (sección 6 de la guía de fase 1):** Shopify Payments EE. UU. con la dirección de Miami
resolvería el cobro en MXN y CLP, quitaría el 2% de Shopify y permitiría pagar con tarjeta, Apple Pay y
Google Pay. Requiere EIN, banco en EE. UU. a nombre de la SpA y una oficina física (no virtual).

---

## 7. Legal y cumplimiento

**EE. UU. (fase 1):** leyes estatales de renovación automática (California, Nueva York y otras): términos
claros antes del pago, consentimiento, correo de confirmación, **cancelación en línea** y aviso de cambios
de precio (incluidos en `docs/politicas-usa/`) · sales tax en el estado del 3PL · privacidad (CCPA) · el
convenio Chile–EE. UU. evita la doble tributación ⚖️.

**México (fase 2):** vender desde inventario en México exige un contribuyente mexicano (filial) ⚖️; la
alternativa es despachar desde el 3PL de EE. UU. con impuestos pagados · PROFECO · aviso de privacidad.

**Chile (fase 3):** IVA 19% y boleta electrónica · Ley 19.496 (retracto de 10 días, garantía de 6 meses) ·
políticas listas en `docs/politicas-chile/`.

---

## 8. Mercados y ciudades

| País | Foco | Contexto |
|---|---|---|
| 🇺🇸 EE. UU. | NY, LA, Miami, Chicago, Boston · Seattle y SF (mayor gasto en mascotas) · Houston, San Antonio, Dallas, San Diego, Phoenix (público latino, tienda en español) | Mercado más grande y competido; BarkBox cobra ~US$35 + US$5 de envío al mes |
| 🇲🇽 México | CDMX (Roma, Condesa, Polanco, Del Valle), Monterrey (San Pedro), Guadalajara (Zapopan) | Gasto de MXN 1,600–2,900 al mes por familia; ~70% de las compras son para perros |
| 🇨🇱 Chile | Santiago oriente, Viña del Mar y Concón, Concepción | ~2.7 millones de hogares con gasto recurrente en mascotas; ~CLP 60.000 al mes |

---

## 9. Marketing (EE. UU.)

**Pre-lanzamiento (nov–dic):** lista de espera con 30% de descuento en la primera caja · contenido de
*unboxing* en Instagram y TikTok · micro-influencers de mascotas en NY, LA y Miami (incluidos creadores
latinos) · alianzas con refugios.

**Pagado:** Meta + TikTok segmentados por ciudad e idioma (anuncios en inglés y en español) · Google
Search ("dog subscription box", "cat subscription box", "dog gift") · temporadas: Año Nuevo, San Valentín,
National Dog Day (26 ago), Black Friday.

**Retención:** flujos de email (bienvenida → perfil → envío → avance del tema → reseña → oferta antes de
cancelar) · referidos · galería #MyMonthlyBox · extras sugeridos antes de cada cobro.

---

## 10. Hoja de ruta

| Fase | Fechas | Entregables |
|---|---|---|
| **1a. Tienda lista para EE. UU.** | 26 oct–1 nov 2026 | ✅ Configuración · ⏳ PayPal y transacciones de referencia, Subscriptions, políticas, marca, plan de AutoDS |
| **1b. Producto y operación** | 2–30 nov | Proveedores en EE. UU. · muestras · 3PL · sales tax · fotos reales · páginas · lista de espera |
| **1c. Prueba de temporada (opcional)** | dic 2026 | Holiday Box o regalos si el inventario llega antes del ~5 dic · pedidos de prueba |
| **1d. Lanzamiento EE. UU.** | **ene 2027** | Club en vivo · anuncios en las 5 ciudades foco + público latino |
| **2. México** | 2º trimestre 2027 | Definir cobro (USD con PayPal o MXN con Shopify Payments) e inventario (filial o despacho desde EE. UU.) · activar mercado México |
| **3. Chile** | 2º semestre 2027 | Definir cobro (USD, Shopify Payments con CLP o tienda con Flow) · 3PL en Santiago · activar mercado Chile |

---

## 11. Presupuesto inicial EE. UU. *(supuestos)*

| Concepto | US$ aprox. |
|---|---|
| Shopify, apps y dominio (3 meses) | 200–400 |
| Diseño de marca y empaque | 500–1,500 |
| Cajas impresas (500 unidades) | 800–1,500 |
| Inventario de la primera tanda (100 cajas + extras) | 1,200–1,600 |
| Configuración del 3PL y muestras | 300–800 |
| Fotos y video (UGC) | 300–800 |
| Publicidad de lanzamiento (primer mes) | 1,500–3,000 |
| CPA de EE. UU. (asesoría inicial) | 300–800 |
| **Total** | **≈ 5,100–10,400** |

---

## 12. KPIs (EE. UU.)

| KPI | Mes 3 | Mes 6 |
|---|---|---|
| Suscriptores activos | 150 | 500 |
| Cancelación mensual | < 12% | < 10% |
| CAC | < US$30 | < US$25 |
| % prepagos | ≥ 25% | ≥ 30% |
| % pedidos con un extra | ≥ 20% | ≥ 25% |
| Calificación de la caja | ≥ 4.6/5 | ≥ 4.7/5 |

---

## 13. Decisiones pendientes
1. **AutoDS:** mantener el plan más barato que cubra ~20 productos y pedidos automáticos (la tienda a la carta depende de él). Decidir antes del 29-oct.
2. **Nombre de marca** y dominio.
3. **Dirección de Miami:** ¿es una oficina física? ¿la SpA tiene EIN y banco en EE. UU.? (para evaluar Shopify Payments después del lanzamiento).
4. **Presupuesto** del lanzamiento.
5. Validar con un CPA los puntos ⚖️ (sales tax, convenio, establecimiento permanente).

---

### Documentos relacionados
- [`docs/fase-1-estados-unidos.md`](docs/fase-1-estados-unidos.md): paso a paso de la fase actual, comisiones de PayPal y la opción de Miami.
- [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md): análisis de estructuras alternativas (dos tiendas, LLC, filial mexicana) para optimizar más adelante.
- [`docs/politicas-usa/`](docs/politicas-usa/) y [`docs/politicas-chile/`](docs/politicas-chile/): políticas para pegar en Shopify.

### Fuentes de mercado
- [Precios de BarkBox (My Subscription Addiction)](https://www.mysubscriptionaddiction.com/category/barkbox-reviews)
- [Cajas de suscripción para gatos 2026](https://catsluvus.com/cat-subscription-boxes/best-cat-subscription-boxes-2026)
- [Gasto en mascotas por área metropolitana en EE. UU. (Bank of America Institute)](https://institute.bankofamerica.com/economic-insights/us-pet-ownership.html)
- [Gasto mensual en mascotas en México (El Imparcial, mar-2026)](https://www.elimparcial.com/dinero/2026/03/03/familias-mexicanas-destinan-casi-2900-pesos-al-mes-a-sus-mascotas-en-que-gastan-y-por-que-invierten-cada-vez-mas/)
- [Gasto en mascotas en Chile (CNC, ago-2026)](https://chocale.cl/2026/08/gasto-en-mascotas-sube-un-63-en-los-hogares-de-chile/)
- [Suspensión del de minimis en EE. UU. (ST&R)](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/february/de-minimis-suspension-remains-in-place)
