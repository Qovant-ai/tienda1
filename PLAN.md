# Plan maestro: club mensual de cajas para perros y gatos

**Mercados:** México (CDMX, Monterrey, Guadalajara) y Estados Unidos (NY, LA, Miami, Chicago, Boston y otras ciudades de alto gasto).
**Fecha del plan:** 26-oct-2026 · **Estado inicial:** [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md) · **Cambios:** [`CHANGELOG.md`](CHANGELOG.md)

> Las cifras de costos y precios son **supuestos de trabajo** que hay que validar con cotizaciones reales
> (proveedores, paqueterías, 3PL). Se marcan con *(supuesto)*.

---

## 0. Acciones urgentes (esta semana)

| # | Acción | Estado |
|---|---|---|
| 1 | Reconectar el conector de Shopify | ✅ Hecho |
| 2 | Eliminar los 10 productos de AutoDS (precios erróneos, sin encaje) | ✅ Hecho |
| 3 | Crear el catálogo del club (en borrador) | ✅ Hecho: 12 productos, 4 colecciones |
| 4 | **Decidir país y entidad de cobro** (la tienda está registrada en **Chile**) | ⏳ Bloquea pagos y suscripciones (sección 6.2) |
| 5 | **Decidir sobre AutoDS** antes del 29-oct 00:16 UTC (se cobra ese día) | ⏳ Ver sección 4.4 |
| 6 | Cambiar la zona horaria a `America/Mexico_City` y el nombre de la tienda | ⏳ Ajustes de Shopify |
| 7 | Publicar el tema **Horizon** (ya instalado) en lugar del tema de AutoDS | ⏳ Debe hacerse desde el admin |

---

## 1. Concepto y propuesta de valor

**Un club mensual, como los clubes de vino, para perros y gatos:** cada mes llega una caja temática
con 5–6 productos elegidos según el perfil de la mascota (especie, tamaño, edad, alergias, tipo de mordida).

**Diferenciadores**
1. **Marca bilingüe (es/en)** pensada para México *y* para la comunidad latina de EE. UU.
   (LA, Miami, Houston, Chicago, NY), un segmento que BarkBox y Meowbox no atienden en su idioma.
2. **Personalización real:** quiz de perfil y cambio de talla o alergias en cualquier momento.
3. **Temas culturales:** Día de Muertos, Navidad y posadas, Reyes, San Valentín, verano, Fiestas Patrias.
4. **Impacto:** una parte de cada caja se dona a refugios locales.
5. **Sin letra chica:** pausar, saltar un mes o cancelar en 2 clics (además, es obligatorio en CA y NY).

**Nombre de marca:** pendiente (el catálogo usa provisionalmente el proveedor "Club Mascotas").
Ideas bilingües para validar (dominio y marca **sin verificar**):
*Pawsito Club*, *Colita Box*, *Huellita Club*, *Bigotes & Colitas*, *Michi & Firu Club*.

---

## 2. Producto: las cajas y los planes

| Línea | Variantes (perfil) | MX (IVA incluido) | EE. UU. (envío incluido) |
|---|---|---|---|
| **Club Perro** | Chico (<10 kg) · Mediano (10–25 kg) · Grande (>25 kg) | MXN 649/mes | US$39.99/mes |
| **Club Gato** | Gatito · Adulto · Senior | MXN 579/mes | US$32.99/mes |

**Opciones de compra**
- **Mensual** con renovación automática: precio completo.
- **Regalo o prepago de 1, 3 o 6 meses** (pago único, sin renovación):

| | 1 caja | 3 meses | 6 meses |
|---|---|---|---|
| Perro | 699 | 1,857 (619/mes, −5%) | 3,534 (589/mes, −9%) |
| Gato | 629 | 1,650 (550/mes, −5%) | 3,150 (525/mes, −9%) |

> **Clave para México:** mucha gente no usa tarjeta de crédito. Los **prepagos y regalos son pagos
> únicos**, así que pueden cobrarse con **OXXO, SPEI o Mercado Pago**. Las suscripciones recurrentes
> solo se cobran con tarjeta (Shopify Payments o PayPal).

---

## 3. Selección inteligente de productos

### 3.1 Criterios de selección (puntuación de 1 a 5)

Cada producto candidato, para la caja o como extra, se califica así. Solo entran los que suman **≥ 28 de 35**.

| Criterio | Qué se busca | Peso |
|---|---|---|
| Valor percibido vs. costo | Precio en tienda ≥ 3× el costo | ×1.5 |
| Peso y volumen | ≤ 250 g, plano o compacto (no sube la tarifa de envío) | ×1.5 |
| Seguridad | Sin piezas pequeñas, materiales no tóxicos, apto para la talla | Filtro (si falla, no entra) |
| Recompra / consumible | Se gasta y se vuelve a necesitar (bolsas, snacks, toallitas) | ×1 |
| Temático y fotogénico | Se adapta al tema del mes y luce en el *unboxing* | ×1 |
| Abastecimiento local | Proveedor en México con stock y factura | ×1 |
| Universal por talla | Sirve a la mayoría de perfiles con pocas variantes | ×1 |

### 3.2 Lo que NO entra (y por qué)

| Producto | Motivo |
|---|---|
| Alimento completo y arena | Pesado, regulado y de marca muy personal |
| Camas, árboles y transportadoras | Voluminosos: rompen la economía del envío |
| Electrónicos con batería (láser, cepillos USB) | Fallas, devoluciones y restricciones de envío |
| Premios importados (sobre todo de China) | Requisitos zoosanitarios y aduana (SENASICA) |
| Juguetes con piezas pequeñas o rellenos sueltos | Riesgo de asfixia |
| Productos genéricos de dropshipping | Sin control de calidad ni presentación de caja |

### 3.3 Catálogo creado en Shopify (en borrador)

Detalle con IDs, SKU y costos objetivo: [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv)

| Colección | Producto | Precio MXN | Por qué está |
|---|---|---|---|
| **El Club** | Club Perro · Caja mensual (3 tallas) | 649 | Producto principal: ingreso recurrente. ~70% del mercado son perros |
| **El Club** | Club Gato · Caja mensual (3 etapas) | 579 | Segundo segmento; cajas más ligeras y baratas de enviar |
| **Regala el Club** | Regala el Club Perro · 1/3/6 meses | 699–3,534 | Captura a quien paga en efectivo y el mercado de regalos |
| **Regala el Club** | Regala el Club Gato · 1/3/6 meses | 629–3,150 | Igual que el anterior |
| **Edición limitada** | Caja Navideña (perro chico, perro mediano o grande, gato) | 699–799 | Validación rápida en Buen Fin, Black Friday y Navidad |
| **Añade a tu caja** | Placa de identificación grabada | 199 | Personalizada, margen ~80%, utilidad real (seguridad) |
| **Añade a tu caja** | Bolsas biodegradables · 8 rollos + dispensador | 149 | Consumible de recompra mensual |
| **Añade a tu caja** | Juguete extra resistente (mediano o grande) | 249 | Resuelve el dolor nº 1: perros que destruyen juguetes |
| **Añade a tu caja** | Kit dental (perro o gato) | 169 | Salud y consumible; ligero |
| **Añade a tu caja** | Bandana temática del mes | 149 | Coleccionable, fotogénica, casi sin peso |
| **Añade a tu caja** | Varita con plumas + 3 repuestos | 139 | El juguete de gato más vendido; repuestos = recompra |
| **Añade a tu caja** | Toallitas para patas y pelaje · 100 pzas | 119 | Consumible de alta rotación |

**Lógica de los extras:** viajan **dentro de la caja del mes**, así que no pagan envío adicional.
Cada extra que se agrega casi duplica el margen de ese pedido sin costo logístico.

### 3.4 Contenido de las primeras 3 cajas *(propuesta)*

| Mes | Tema | Club Perro | Club Gato |
|---|---|---|---|
| **Dic 2026** | Navidad y posadas | Peluche piñata con sonido · cuerda navideña · 2 snacks de temporada · toallitas · bandana navideña | Ratón de fieltro con catnip · varita de estrella · snack lamible · cepillo · moño navideño |
| **Ene 2027** | Año nuevo, hábitos sanos | Tapete olfativo o juguete dispensador · kit dental · snacks bajos en calorías · bolsas biodegradables · bandana | Rascador de cartón · pelota con catnip · snack funcional · kit dental · sorpresa |
| **Feb 2027** | Amor perruno / Amor gatuno | Peluche corazón · cuerda roja resistente · 2 snacks · bálsamo para patas · bandana de San Valentín | Corazón con catnip · varita de repuesto · snack lamible · toallitas · sorpresa |

Cada caja: valor en tienda ≥ 1.6× el precio, costo de producto ≤ MXN 170 (perro) / 150 (gato), peso ≤ 1.5 kg.

### 3.5 Dónde comprar

- **México (fase 1):** distribuidores mayoristas de mascotas en CDMX y GDL, marcas mexicanas de snacks
  **con registro SENASICA**, talleres de bandanas y peluches, grabado láser local para las placas.
  Pide muestras y precios por 100, 500 y 1,000 piezas.
- **EE. UU. (fase 2):** mayoristas (Faire y distribuidores), marcas privadas e importación consolidada
  al 3PL. AutoDS sirve aquí para investigar productos y una tienda a la carta con almacenes en EE. UU.
- **Regulación de premios:** en México, marcas locales registradas y etiquetado en español; en EE. UU.,
  marcas estadounidenses con etiquetado conforme (FDA/AAFCO). **Nunca** enviar alimento de un país al otro.

---

## 4. Operación: cómo llegan las cajas

### 4.1 Por qué no basta con dropshipping
AutoDS envía cada producto por separado, desde proveedores distintos. Eso no es una caja: no hay
presentación, el envío se multiplica y no controlas el contenido. **Un club necesita inventario propio
y armado (kitting).**

### 4.2 Modelo por etapas

| Etapa | Volumen | Cómo se arma | Dónde |
|---|---|---|---|
| **A. Validación** | 0–150 cajas/mes | Armado propio, inventario de mayoreo | CDMX |
| **B. Crecimiento MX** | 150–1,500 | 3PL con kitting: **Cubbo**, **Melonn** o **99minutos Fulfillment** (cotizar) | CDMX o MTY |
| **C. EE. UU.** | desde el lanzamiento | 3PL con kitting: **ShipMonk** o **ShipBob** | Costa este o centro |

### 4.3 Paquetería
- **México:** **Skydropx** o **Envia.com** (se integran con Shopify); **99minutos** para entrega
  el mismo o al día siguiente en CDMX, MTY y GDL.
- **EE. UU.:** tarifas del 3PL (USPS Ground Advantage para menos de 2–3 lb).

### 4.4 Papel de AutoDS
- **Útil para:** investigar productos (400 créditos) y vender una tienda a la carta en **EE. UU.**
- **No útil para:** armar la caja ni vender a la carta en México (sin almacén en México; impuestos de
  importación desde ago-2025 de hasta 33.5% para origen China).
- **Recomendación:** si el cobro del 29-oct no te conviene, **cancela o baja de plan** y reactívalo al
  lanzar EE. UU. (marzo de 2027).

### 4.5 Calendario operativo mensual

| Día | Actividad |
|---|---|
| 1 | Cobro de renovaciones · corte de pedidos |
| 1–3 | Lista de armado por perfil · compra de faltantes |
| 4–8 | Armado de cajas y guías |
| 8–10 | Envío · correo y WhatsApp de "tu caja va en camino" |
| 15 | Avance (*sneak peek*) del tema siguiente (reduce cancelaciones) |
| 25 | Recordatorio: "puedes saltar o cambiar tu caja antes del día 1" |

---

## 5. Economía por caja *(supuestos)*

### México — Club Perro mensual, MXN 649

| Concepto | MXN |
|---|---|
| Precio | 649.00 |
| (–) IVA 16% | –89.50 |
| **Ingreso neto** | **559.50** |
| Productos | –170 |
| Empaque y tarjeta | –35 |
| Armado | –25 |
| Envío nacional (1–1.5 kg) | –120 |
| Comisión de pago (~4%, verificar) | –26 |
| Apps | –5 |
| **Margen de contribución** | **≈178 (32%)** |
| + 1 extra promedio (p. ej. placa: 172 netos − 35) | +137 → **≈315 (44%)** |

### EE. UU. — Club Perro mensual, US$39.99

| Concepto | US$ |
|---|---|
| Precio (sales tax aparte donde aplique) | 39.99 |
| Productos | –10.00 |
| Empaque | –2.00 |
| Kitting en el 3PL | –3.50 |
| Envío USPS (2–3 lb) | –9.00 |
| Comisión de pago + conversión | –1.80 |
| Apps | –0.40 |
| **Margen de contribución** | **≈13.30 (33%)** |

**Metas de unidad:** retención promedio ≥ 6 meses · **CAC máximo ≈ MXN 350 / US$27** (LTV:CAC 3:1) ·
cancelación mensual < 10% · prepagos ≥ 30% de las altas · ≥ 25% de los pedidos con un extra.

---

## 6. Configuración de Shopify

### 6.1 Base
- [ ] Nombre de la tienda y zona horaria (`America/Mexico_City`).
- [ ] Logo, colores y **dominio propio** `.com`.
- [ ] Publicar **Horizon** (Online Store 2.0, requisito para suscripciones) y retirar el tema de AutoDS.
- [ ] Páginas: Inicio, Cómo funciona, Club Perro, Club Gato, Regalar, FAQ, Contacto, Nosotros.
- [ ] Políticas: Términos de suscripción, Envíos, Reembolsos (privacidad ya existe: revisarla).

### 6.2 Pagos — decisión bloqueante
La tienda está registrada en **Chile**, donde Shopify Payments no parece estar disponible (verificar en
*Configuración → Pagos*). Sin Shopify Payments, las suscripciones dependen de PayPal. Opciones:

| Opción | Cómo | Pros | Contras |
|---|---|---|---|
| **A. Negocio en México** (recomendada para el MVP) | RFC mexicano (persona física o moral) + cuenta bancaria en México → **Shopify Payments MX** | Suscripciones con tarjeta, pesos, CFDI, cobro local | Requiere RFC y alta fiscal en México |
| **B. LLC en EE. UU.** | LLC + EIN + cuenta en EE. UU. → Shopify Payments US; México vía Markets | Sirve para ambos mercados en USD y MXN | Costos de constitución, impuestos en EE. UU.; verificar requisitos para dueños no residentes |
| **C. Seguir en Chile** | Solo PayPal (y Mercado Pago para pagos únicos) | Sin trámites | Menor conversión en México; suscripciones limitadas a PayPal |

- [ ] Elegir opción y actualizar la dirección del negocio y la ubicación de inventario.
- [ ] PayPal Express (también admite suscripciones).
- [ ] Mercado Pago, OXXO y SPEI **solo para pagos únicos** (regalos, prepagos, Caja Navideña).
- [ ] Activar Shop Pay, Apple Pay y Google Pay.

### 6.3 Shopify Markets
- [ ] **México:** MXN, es-MX, IVA incluido (ya existe como mercado principal).
- [ ] **Estados Unidos:** USD, en-US + es; impuesto sumado en el checkout; precios fijos por mercado.
- [ ] Traducir con **Translate & Adapt**; perfiles de envío por mercado.

### 6.4 Suscripciones
- [ ] Instalar **Shopify Subscriptions** (gratis) y crear en la app los planes de Club Perro y Club Gato
      (mensual, renovación con fecha fija el día 1). *Los planes deben crearse desde la app para que ella
      gestione los cobros; por eso no los creé por API.*
- [ ] Portal de cliente: pausar, saltar, cambiar talla y cancelar.
- [ ] **Al escalar (>200 suscriptores):** migrar a **Recharge**, **Loop** o **Appstle** (armado de caja,
      extras dentro de la suscripción, flujos para evitar cancelaciones).
- [ ] **Quiz de perfil** (nombre, especie, talla, edad, alergias, mordida) en metacampos del cliente.

### 6.5 Pendientes del catálogo creado
- [ ] Fotos reales del prototipo (las 5 imágenes actuales son provisionales de Unsplash; los 7 extras no tienen foto).
- [ ] Peso de cada variante (para cotizar envíos) y seguimiento de inventario de los extras.
- [ ] Campos de personalización para la placa (nombre y teléfono) en el tema.
- [ ] Reemplazar el proveedor provisional "Club Mascotas" por la marca final.
- [ ] Precios en USD al abrir el mercado de EE. UU.

### 6.6 Apps y herramientas sugeridas

| Necesidad | Herramienta |
|---|---|
| Email y SMS | Klaviyo (o Shopify Email al inicio) |
| WhatsApp (clave en MX) | WhatsApp Business / Cloud API |
| Reseñas con foto | Judge.me |
| Facturación CFDI 4.0 (si se cobra desde México) | App de facturación para Shopify |
| Envíos MX | Skydropx o Envia.com · 99minutos |
| Impuestos EE. UU. | Shopify Tax |
| Analítica | GA4 + Meta Pixel/CAPI + TikTok Pixel |
| Automatizaciones | n8n (listas de armado, alertas, WhatsApp) |

---

## 7. Legal, fiscal y cumplimiento

### México
- [ ] Régimen fiscal y RFC (según la opción de la sección 6.2; consultar a un contador).
- [ ] Emisión de **CFDI 4.0** a quien lo pida.
- [ ] **Aviso de privacidad** conforme a la ley de protección de datos personales vigente.
- [ ] Términos de suscripción claros (PROFECO): precio total con IVA, periodicidad y forma de cancelar.
- [ ] **Registro de marca ante el IMPI** (clases 31 y 35, más 18 o 28 si aplica).

### Estados Unidos
- [ ] **Leyes estatales de renovación automática** (California, Nueva York y otras): términos visibles
      antes del pago, consentimiento explícito, correo de confirmación, **cancelación en línea fácil** y
      recordatorios en planes largos. La regla federal "click-to-cancel" de la FTC fue anulada en 2025,
      pero las leyes estatales siguen vigentes.
- [ ] **Sales tax:** Shopify Tax para monitorear el *nexus* por estado.
- [ ] Marca ante la USPTO cuando haya tracción · seguro de responsabilidad de producto.

---

## 8. Mercados y ciudades

### México
| Ciudad | Zonas a segmentar | Ventaja |
|---|---|---|
| CDMX | Roma, Condesa, Polanco, Del Valle, Narvarte, Coyoacán, Santa Fe, Interlomas | Mayor densidad y entrega el mismo día |
| Monterrey | San Pedro Garza García, Cumbres, Valle Oriente | Ticket alto y cercanía a EE. UU. |
| Guadalajara | Zapopan, Providencia, Chapalita, Andares | Cultura pet-friendly |

Las familias mexicanas gastan en promedio MXN 1,600–2,900 al mes en mascotas, y ~70% de las compras
son para perros: **Club Perro es el producto principal del lanzamiento.**

### Estados Unidos
| Prioridad | Ciudades | Por qué |
|---|---|---|
| 1 (pedidas) | Nueva York, Los Ángeles, Miami, Chicago, Boston | Densidad; NY y Boston con gasto en mascotas superior al promedio |
| 2 (alto gasto) | Seattle, San Francisco | Los metros de mayor gasto mensual en mascotas (Bank of America, 2025) |
| 3 (ángulo latino) | Houston, San Antonio, Dallas, San Diego, Phoenix | Gran comunidad hispana, encaja con la marca bilingüe |
| 4 (expansión) | Austin, Denver, Washington D.C., Filadelfia | Población joven con mascotas e ingreso alto |

Una sola tienda con envío a todo EE. UU.; las ciudades sirven para **segmentar anuncios e influencers**.

---

## 9. Marketing y crecimiento

**Pre-lanzamiento (2–3 semanas):** lista de espera con incentivo (primera caja con 30% de descuento) ·
contenido en Instagram y TikTok con el prototipo · 10–20 micro-influencers de mascotas por ciudad ·
alianzas con veterinarias, estéticas caninas y refugios.

**Adquisición pagada:** Meta + TikTok Ads con videos de *unboxing* segmentados por zona (empezar con
MXN 500–1,000 diarios) · Google Search ("caja para perros", "regalo para perro") · temporadas: Buen Fin
(mediados de nov, verificar fechas), Black Friday y Cyber Monday (27 y 30 nov 2026), Navidad,
San Valentín, Día del Perro (21 jul MX / 26 ago EE. UU.).

**Retención:** flujos de email y WhatsApp (bienvenida → quiz → envío → avance del tema → reseña con foto
→ oferta antes de cancelar → recuperación) · referidos ("da una caja con descuento, recibe un juguete") ·
galería #MiCajaDelMes · extras sugeridos en cada correo previo al cobro.

---

## 10. Hoja de ruta

| Fase | Fechas | Entregables |
|---|---|---|
| **0. Urgente** | 26–29 oct 2026 | ✅ Shopify reconectado · ✅ catálogo nuevo · ⏳ país de cobro · ⏳ AutoDS |
| **1. Fundaciones** | 27 oct–8 nov | Marca · dominio · entidad fiscal · pagos · Horizon · políticas |
| **2. Producto** | 2–15 nov | Proveedores MX · muestras · prototipo de caja · fotos reales · precios finales |
| **3. Club en la tienda** | 9–20 nov | Shopify Subscriptions · quiz · lista de espera · flujos de email |
| **4. Preventa Caja Navideña** | ~13 nov–10 dic | Activar Caja Navideña y Regala el Club para Buen Fin y Black Friday · envíos desde el 7 dic |
| **5. Lanzamiento MX** | dic 2026 | Primeras cajas del club · reseñas · ajustes |
| **6. Optimización MX** | ene–feb 2027 | Cancelación < 12% · CAC en meta · cotizar 3PL · preparar EE. UU. |
| **7. Lanzamiento EE. UU.** | mar 2027 | NY, LA, Miami, Chicago, Boston + segmento latino · 3PL · tienda a la carta con AutoDS |
| **8. Escala** | abr 2027+ | Recharge/Loop · líneas nuevas (cachorro, senior, premium) · más ciudades |

**¿Por qué México primero?** La tienda ya está en MXN, la competencia local es menor y validar el producto
con poco capital reduce el riesgo antes de invertir en inventario y 3PL en EE. UU.

---

## 11. Presupuesto inicial estimado (MVP México) *(supuestos)*

| Concepto | MXN aprox. |
|---|---|
| Shopify, apps y dominio (3 meses) | 4,000–8,000 |
| Diseño de marca y empaque | 5,000–15,000 |
| Cajas impresas (500 piezas) | 12,000–20,000 |
| Inventario de la primera tanda (100 cajas + extras) | 20,000–25,000 |
| Muestras de proveedores | 3,000–5,000 |
| Fotos y video (UGC) | 5,000–10,000 |
| Registro de marca IMPI | 3,000–6,000 |
| Publicidad de lanzamiento (primer mes) | 20,000–30,000 |
| **Total** | **≈ 72,000–120,000** |

---

## 12. KPIs semanales

| KPI | Meta mes 3 (MX) | Meta mes 6 |
|---|---|---|
| Suscriptores activos | 150 | 500 MX + 150 EE. UU. |
| MRR | ≈ MXN 95k | ≈ MXN 320k + US$6k |
| Cancelación mensual | < 12% | < 10% |
| CAC | < MXN 350 | < MXN 300 / US$27 |
| % prepagos | ≥ 25% | ≥ 30% |
| % pedidos con extra | ≥ 20% | ≥ 25% |
| Calificación de la caja | ≥ 4.6/5 | ≥ 4.7/5 |

---

## 13. Reparto del trabajo

**Puedo hacerlo yo (con Shopify y AutoDS conectados):** productos, colecciones, metacampos, descuentos,
páginas y textos legales; precios y traducciones; búsqueda de productos en AutoDS; contenido de marketing;
diseño de automatizaciones; y registrar cada cambio en este repo.

**Te toca a ti:** decidir país y entidad de cobro · activar pagos (datos bancarios y fiscales) · decidir
sobre AutoDS antes del 29-oct · publicar Horizon e instalar Shopify Subscriptions · contratos con
proveedores y paqueterías · aprobar marca y precios · armar el prototipo y tomar fotos.

---

## 14. Decisiones pendientes

1. **País y entidad de cobro** (México, LLC en EE. UU. o Chile): bloquea las suscripciones.
2. **Nombre de marca** y dominio.
3. **AutoDS:** mantener, bajar de plan o cancelar antes del 29-oct.
4. **Secuencia:** México primero (recomendado) o ambos a la vez.
5. **Presupuesto** para el MVP.
6. **Armado:** propio al inicio (recomendado) o 3PL desde el día 1.

---

### Fuentes
- [Shopify Payments disponible en México (changelog de Shopify)](https://changelog.shopify.com/posts/shopify-payments-available-in-mexico)
- [Países con Shopify Payments (Shopify Help Center)](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries)
- [Discusión: Chile fuera de Shopify Payments (Shopify Community)](https://community.shopify.com/t/tienda-multidivisas-en-chile/297788)
- [Shopify Subscriptions: pasarelas compatibles](https://help.shopify.com/docs/apps/selling-strategies/subscriptions/contracts)
- [Configuración de suscripciones en Shopify](https://help.shopify.com/manual/products/purchase-options/subscriptions/setup)
- [Gasto mensual en mascotas en México (El Imparcial, mar-2026)](https://www.elimparcial.com/dinero/2026/03/03/familias-mexicanas-destinan-casi-2900-pesos-al-mes-a-sus-mascotas-en-que-gastan-y-por-que-invierten-cada-vez-mas/)
- [Gasto en mascotas: más de MXN 1,600 al mes (El Imparcial, mar-2026)](https://www.elimparcial.com/dinero/2026/03/17/gastos-en-mascotas-en-mexico-supera-los-1600-pesos-al-mes-60-millones-de-perros-y-gatos-ya-forman-parte-de-las-familias/)
- [Precios de BarkBox (My Subscription Addiction)](https://www.mysubscriptionaddiction.com/category/barkbox-reviews)
- [Cajas de suscripción para gatos 2026](https://catsluvus.com/cat-subscription-boxes/best-cat-subscription-boxes-2026)
- [Gasto en mascotas por área metropolitana en EE. UU. (Bank of America Institute)](https://institute.bankofamerica.com/economic-insights/us-pet-ownership.html)
- [Impuesto de 33.5% a paquetes de China en México (Uno TV)](https://www.unotv.com/negocios/compras-en-shein-y-temu-pagaran-nuevo-impuesto-de-33-5-debo-declararlo-al-sat/)
- [Suspensión del de minimis en EE. UU. (ST&R)](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/february/de-minimis-suspension-remains-in-place)
- [Opciones de fulfillment en México (Cubbo, fuente con sesgo comercial)](https://www.cubbo.com/en/posts/3pl-mexico)
- [Requisitos de importación (Ventanilla Única / SENASICA)](https://ventanillaunica.economia.gob.mx/procedure/583?l=en)
