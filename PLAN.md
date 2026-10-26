# Plan maestro: club mensual de cajas para perros y gatos

**Mercados:** 🇨🇱 Chile → 🇺🇸 Estados Unidos → 🇲🇽 México.
**Actualizado:** 26-oct-2026 · **Estructura legal y pagos:** [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md) ·
**Estado inicial:** [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md) · **Cambios:** [`CHANGELOG.md`](CHANGELOG.md)

> Las cifras de costos y precios son **supuestos de trabajo** que hay que validar con cotizaciones reales.
> Se marcan con *(supuesto)*.

---

## 0. Estado y acciones urgentes

| # | Acción | Estado |
|---|---|---|
| 1 | Reconectar Shopify · eliminar los 10 productos de AutoDS · crear el catálogo del club | ✅ Hecho |
| 2 | Publicar el tema Horizon | ✅ Hecho (por ti) |
| 3 | Definir la estructura por países | ✅ 2 entidades, 2 tiendas (ver documento de estructura) |
| 4 | Convertir esta tienda en la **tienda Chile** | 🟡 Mercado Chile, idioma y textos listos · **falta: moneda CLP, zona horaria, idioma predeterminado y políticas (en el admin)** |
| 5 | **Decidir sobre AutoDS antes del 29-oct 00:16 UTC** (se cobra ese día) | ⏳ Recomendación: cancelar; no se usa en Chile |
| 6 | Iniciar la **LLC en EE. UU.** (tarda 3–8 semanas) | ⏳ Pendiente |

---

## 1. Concepto y propuesta de valor

**Un club mensual, como los clubes de vino, para perros y gatos:** cada mes llega una caja temática con
5–6 productos elegidos según el perfil de la mascota (especie, tamaño, edad, alergias, tipo de mordida).

**Diferenciadores:** personalización real · temas locales por país (Fiestas Patrias en Chile, Día de Muertos
en México, Thanksgiving en EE. UU.) · marca bilingüe que atiende también a la comunidad latina de EE. UU. ·
donación a refugios · pausar, saltar o cancelar en 2 clics · línea **Senior** (en Chile, el 35% de los
perros y el 32% de los gatos son senior, según Cadem 2026).

**Marca:** pendiente (proveedor provisional "Club Mascotas"). Ideas para validar: *Pawsito Club*, *Colita Box*,
*Huellita Club*, *Bigotes & Colitas*. Debe funcionar en los tres países.

---

## 2. Productos y precios por país

### 2.1 Catálogo (creado en esta tienda, en borrador)
Detalle: [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv)

| Producto | 🇨🇱 CLP (IVA incl.) | 🇲🇽 MXN (IVA incl.) | 🇺🇸 USD |
|---|---|---|---|
| Club Perro · mensual | 29.990 | 649 | 39.99 |
| Club Gato · mensual | 26.990 | 579 | 32.99 |
| Regala el Club Perro · 1 caja / 3 meses / 6 meses | 32.990 / 85.490 / 163.990 | 699 / 1,857 / 3,534 | 44.99 / 113.97 / 215.94 |
| Regala el Club Gato · 1 caja / 3 meses / 6 meses | 29.990 / 76.990 / 147.990 | 629 / 1,650 / 3,150 | 36.99 / 94.47 / 179.94 |
| Caja Navideña · perro / gato | 36.990 / 32.990 | 799 / 699 | 44.99 / 39.99 |
| Placa de identificación grabada | 8.990 | 199 | 14.99 |
| Bolsas biodegradables · 8 rollos + dispensador | 6.990 | 149 | 9.99 |
| Juguete extra resistente | 11.990 | 249 | 16.99 |
| Kit dental | 7.990 | 169 | 11.99 |
| Bandana temática | 6.990 | 149 | 9.99 |
| Varita con plumas + 3 repuestos | 6.490 | 139 | 9.99 |
| Toallitas · 100 piezas | 5.490 | 119 | 8.99 |

Hoy los precios cargados en la tienda son los de México (MXN). **Cuando cambies la moneda a CLP, cargo la columna de Chile.**

### 2.2 Cómo se cobra en cada país

| | Mensual con renovación | Prepagos, regalos, Navidad y extras |
|---|---|---|
| 🇨🇱 Chile | **Flow Suscripciones** (tarjeta inscrita, cobro automático) → pedido en Shopify vía n8n | Checkout de Shopify con Flow, Mercado Pago o Khipu |
| 🇺🇸 EE. UU. | Shopify Subscriptions + Shopify Payments US | Checkout de Shopify |
| 🇲🇽 México | Shopify Subscriptions + Shopify Payments MX (filial) | Checkout de Shopify + OXXO/SPEI |

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
Alimento completo y arena (pesados, regulados) · camas y árboles (voluminosos) · electrónicos con batería
(fallas y devoluciones) · premios importados (permisos sanitarios: SAG en Chile, SENASICA en México, FDA en
EE. UU.) · juguetes con piezas pequeñas · productos genéricos de dropshipping.

### 3.3 Por qué está cada producto
- **Club Perro y Club Gato:** ingreso recurrente; los perros son la mayoría del mercado.
- **Regalos y prepagos (pago único):** captan a quien no quiere suscripción o no usa tarjeta de crédito, y en Chile cubren el hueco del cobro recurrente.
- **Caja Navideña:** validación rápida con la temporada alta de diciembre.
- **Extras "Añade a tu caja":** viajan en el mismo paquete (sin envío extra) y casi duplican el margen del pedido. Placa grabada (personalizada, margen ~80%), bolsas, kit dental y toallitas (recompra), juguete resistente (dolor nº 1 de los dueños), bandana (coleccionable) y varita (el juguete de gato más vendido).

### 3.4 Primeras cajas *(propuesta, Chile)*

| Mes | Tema | Club Perro | Club Gato |
|---|---|---|---|
| Dic 2026 | Navidad de verano | Peluche navideño con sonido · cuerda · 2 snacks · toallitas · bandana | Ratón con catnip · varita de estrella · snack lamible · cepillo · moño |
| Ene 2027 | Verano y vacaciones | Juguete refrescante o para agua · snacks hidratantes · bolsas · bálsamo para patas · bandana | Juguete con catnip · pelota · snack lamible · kit dental · sorpresa |
| Feb 2027 | Amor perruno / gatuno | Peluche corazón · cuerda roja · 2 snacks · kit dental · bandana | Corazón con catnip · repuesto de varita · snack · toallitas · sorpresa |

Cada caja: valor en tienda ≥ 1.6× el precio · costo de productos ≤ CLP 8.500 (perro) / 7.500 (gato) · peso ≤ 1.5 kg.

### 3.5 Dónde comprar
- **Chile:** distribuidores mayoristas de mascotas en Santiago, marcas chilenas de snacks con registro **SAG**, talleres de bandanas y grabado láser local.
- **EE. UU.:** mayoristas (Faire, distribuidores) e importación consolidada al 3PL. AutoDS sirve aquí para investigar productos y para una tienda a la carta.
- **México (fase 3):** mayoristas en CDMX y GDL; snacks de marcas con registro SENASICA.

---

## 4. Operación

**Modelo:** inventario propio + armado de cajas (*kitting*) en un **3PL de cada país**. Es lo que permite
operar como nómada: nada depende de dónde estés.

| País | 3PL a cotizar | Paquetería |
|---|---|---|
| 🇨🇱 Chile | Amplifica (partner de Shopify) · Blue Express Fulfillment | Blue Express, Starken, Chilexpress (vía el 3PL) |
| 🇺🇸 EE. UU. | ShipMonk · ShipBob | USPS Ground Advantage (vía el 3PL) |
| 🇲🇽 México | Cubbo · Melonn · 99minutos | Skydropx, Envia.com, 99minutos |

**Calendario mensual:** día 1 cobro y corte · días 1–3 lista de armado por perfil · días 4–8 armado ·
días 8–10 despacho · día 15 avance del tema siguiente · día 25 recordatorio para saltar o cambiar.

**AutoDS:** no arma cajas ni tiene almacén en Chile ni en México. Útil solo para investigar productos y,
más adelante, para una tienda a la carta en EE. UU. **Recomendación: cancelar antes del 29-oct y
reactivarlo al lanzar EE. UU.**

---

## 5. Economía por caja *(supuestos)*

| Club Perro mensual | 🇨🇱 Chile (CLP) | 🇲🇽 México (MXN) | 🇺🇸 EE. UU. (USD) |
|---|---|---|---|
| Precio | 29.990 | 649 | 39.99 |
| Ingreso neto (sin IVA) | 25.202 | 559.50 | 39.99 (sales tax aparte) |
| Productos | –8.500 | –170 | –10.00 |
| Empaque y tarjeta | –1.800 | –35 | –2.00 |
| Armado (3PL) | –1.500 | –25 | –3.50 |
| Despacho | –3.800 | –120 | –9.00 |
| Comisión de pago | –1.050 | –26 | –1.80 |
| Apps | –300 | –5 | –0.40 |
| **Margen de contribución** | **≈8.250 (33%)** | **≈178 (32%)** | **≈13.30 (33%)** |

Un extra por pedido (por ejemplo, la placa) suma ~70–80% de margen sin costo de envío.
**Metas:** retención ≥ 6 meses · CAC máximo ≈ CLP 17.000 / MXN 350 / US$27 · cancelación < 10% mensual ·
≥ 30% de prepagos · ≥ 25% de pedidos con un extra.

---

## 6. Configuración de Shopify

### 6.1 Tienda Chile (esta)
- [x] Mercado Chile creado y activo · México en borrador.
- [x] Español agregado y publicado · textos de producto adaptados a Chile.
- [x] Políticas chilenas redactadas (`docs/politicas-chile/`).
- [ ] *(Tú)* Moneda CLP · zona horaria Santiago · idioma predeterminado español · nombre, razón social y RUT.
- [ ] *(Tú)* Pegar las políticas · activar Flow, Mercado Pago o Khipu · app de boleta electrónica SII.
- [ ] *(Yo)* Cargar precios en CLP · páginas (Inicio, Cómo funciona, FAQ) · automatización Flow → Shopify con n8n.
- [ ] Fotos reales del prototipo, peso por variante y campos de personalización de la placa.

### 6.2 Tienda Global (nueva, a nombre de la LLC)
- [ ] Shopify Payments US · Shopify Subscriptions (mensual con fecha fija el día 1) · Shopify Tax.
- [ ] Mercado EE. UU. (USD, inglés y español) · lista de espera para México.
- [ ] *(Yo)* Copiar catálogo, colecciones y textos, traducidos al inglés.

### 6.3 Apps sugeridas

| Necesidad | Chile | EE. UU. / México |
|---|---|---|
| Pagos | Flow · Mercado Pago · Khipu | Shopify Payments · PayPal |
| Suscripciones | Flow Suscripciones + n8n | Shopify Subscriptions → Recharge o Loop al escalar |
| Comprobantes | e-Boletas, Bsale u OpenFactura | Shopify Tax · CFDI (México) |
| Email y SMS | Klaviyo (o Shopify Email) | Igual |
| WhatsApp | WhatsApp Business | Igual |
| Reseñas | Judge.me | Igual |

---

## 7. Legal y cumplimiento

**Chile (SpA):** IVA 19% y boleta electrónica · Ley 19.496 del consumidor: **retracto de 10 días** en
compras a distancia y **garantía legal de 6 meses** · información clara de la suscripción · nueva ley de
datos personales (Ley 21.719, con entrada en vigor escalonada: verificar la fecha) · marca en INAPI.

**EE. UU. (LLC):** leyes estatales de renovación automática (CA, NY y otras): consentimiento explícito,
cancelación en línea y recordatorios · sales tax con Shopify Tax · Form 5472 + 1120 *pro forma* · marca en USPTO.

**México (filial, fase 3):** RFC, CFDI 4.0, aviso de privacidad, términos claros (PROFECO), marca en IMPI.

Detalle y puntos para validar con tu contador: [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md).

---

## 8. Mercados y ciudades

| País | Ciudades y zonas foco | Contexto |
|---|---|---|
| 🇨🇱 Chile | Santiago oriente (Las Condes, Vitacura, Providencia, Ñuñoa, Lo Barnechea, La Reina), Viña del Mar y Concón, Concepción | ~2.7 millones de hogares con gasto recurrente en mascotas; gasto promedio de ~CLP 60.000/mes (CNC 2026). Santiago concentra la demanda, así que la logística es barata |
| 🇺🇸 EE. UU. | NY, LA, Miami, Chicago, Boston · Seattle y SF (mayor gasto) · Houston, San Antonio, Dallas, San Diego, Phoenix (ángulo latino) | Mercado más grande y más competido (BarkBox, Meowbox) |
| 🇲🇽 México | CDMX (Roma, Condesa, Polanco, Del Valle), Monterrey (San Pedro), Guadalajara (Zapopan) | Gasto de MXN 1,600–2,900 al mes por familia; ~70% de las compras son para perros |

---

## 9. Marketing

**Pre-lanzamiento en Chile (2–3 semanas):** lista de espera con 30% de descuento en la primera caja ·
contenido en Instagram y TikTok con el prototipo · micro-influencers de mascotas en Santiago · alianzas con
veterinarias, peluquerías caninas y refugios.

**Pagado:** Meta + TikTok con videos de *unboxing* segmentados por comuna · Google Search ("caja para
perros", "regalo para perro") · temporadas: Black Friday Chile (fines de nov) y Cyber Day, Navidad,
Fiestas Patrias, Día del Perro.

**Retención:** flujos de email y WhatsApp (bienvenida → perfil → despacho → avance del tema → reseña →
oferta antes de cancelar) · referidos · galería #MiCajaDelMes · extras sugeridos antes de cada cobro.

---

## 10. Hoja de ruta

| Fase | Fechas | Entregables |
|---|---|---|
| **0. Base** | 26 oct–2 nov 2026 | ✅ Catálogo y estructura · ajustes de la tienda Chile en el admin · AutoDS cancelado · LLC iniciada |
| **1. Chile: producto** | 2–15 nov | Proveedores en Santiago · muestras · prototipo · fotos reales · cotizaciones de 3PL |
| **2. Chile: tienda lista** | 9–20 nov | Precios en CLP · pagos · boletas · Flow Suscripciones + n8n · páginas · lista de espera |
| **3. Chile: preventa Navidad** | ~20 nov–10 dic | Caja Navideña y regalos para Black Friday y Navidad · despachos desde el 7 dic |
| **4. Chile: lanzamiento del club** | dic 2026–ene 2027 | Primeras cajas mensuales · reseñas · ajustes |
| **5. EE. UU.: preparación** | nov 2026–feb 2027 | LLC, EIN, banco, Shopify Payments, 3PL, tienda Global en inglés |
| **6. EE. UU.: lanzamiento** | mar 2027 | Lanzamiento suave en NY, LA, Miami, Chicago y Boston + segmento latino · lista de espera México |
| **7. México** | 2º trimestre 2027 | Filial mexicana, Shopify Payments MX, 3PL y lanzamiento en CDMX, MTY y GDL |
| **8. Escala** | 2º semestre 2027 | Recharge o Loop · líneas nuevas (cachorro, senior, premium) · evaluar Shopify Plus para unificar tiendas |

---

## 11. Presupuesto inicial *(supuestos)*

| Concepto | Chile (CLP aprox.) |
|---|---|
| Shopify, apps y dominio (3 meses) | 150.000–300.000 |
| Diseño de marca y empaque | 300.000–700.000 |
| Cajas impresas (500 unidades) | 500.000–900.000 |
| Inventario de la primera tanda (100 cajas + extras) | 1.000.000–1.300.000 |
| Muestras y fotos o video | 300.000–600.000 |
| Marca en INAPI | 100.000–200.000 |
| Publicidad de lanzamiento (primer mes) | 800.000–1.500.000 |
| **Total Chile** | **≈ 3,2–5,5 millones** |
| LLC en EE. UU. (primer año, sin inventario) | ~US$1,000–2,500 |

---

## 12. KPIs

| KPI | Mes 3 (Chile) | Mes 6 (Chile + EE. UU.) |
|---|---|---|
| Suscriptores activos | 150 | 400 CL + 150 EE. UU. |
| Cancelación mensual | < 12% | < 10% |
| CAC | < CLP 17.000 | < CLP 15.000 / US$27 |
| % prepagos | ≥ 25% | ≥ 30% |
| % pedidos con un extra | ≥ 20% | ≥ 25% |
| Calificación de la caja | ≥ 4.6/5 | ≥ 4.7/5 |

---

## 13. Decisiones pendientes
1. **AutoDS:** cancelar antes del 29-oct (recomendado).
2. **Iniciar la LLC** y elegir el servicio de constitución.
3. **Nombre de marca** y dominio (válidos en los tres países).
4. **Presupuesto** del lanzamiento en Chile.
5. Validar con tu contador los puntos ⚖️ del documento de estructura.

---

### Fuentes
Ver [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md) para las fuentes de pagos,
estructura y Chile. Fuentes de mercado de México y EE. UU.:
- [Gasto mensual en mascotas en México (El Imparcial, mar-2026)](https://www.elimparcial.com/dinero/2026/03/03/familias-mexicanas-destinan-casi-2900-pesos-al-mes-a-sus-mascotas-en-que-gastan-y-por-que-invierten-cada-vez-mas/)
- [Precios de BarkBox (My Subscription Addiction)](https://www.mysubscriptionaddiction.com/category/barkbox-reviews)
- [Cajas de suscripción para gatos 2026](https://catsluvus.com/cat-subscription-boxes/best-cat-subscription-boxes-2026)
- [Gasto en mascotas por área metropolitana en EE. UU. (Bank of America Institute)](https://institute.bankofamerica.com/economic-insights/us-pet-ownership.html)
- [Impuesto de 33.5% a paquetes de China en México (Uno TV)](https://www.unotv.com/negocios/compras-en-shein-y-temu-pagaran-nuevo-impuesto-de-33-5-debo-declararlo-al-sat/)
- [Suspensión del de minimis en EE. UU. (ST&R)](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/february/de-minimis-suspension-remains-in-place)
- [Shopify Subscriptions: pasarelas compatibles](https://help.shopify.com/docs/apps/selling-strategies/subscriptions/contracts)
