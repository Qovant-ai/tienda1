# Estructura por países, entidades y pagos

> **Decisión vigente (26-oct-2026, más tarde ese día):** el dueño eligió **una sola tienda**, a nombre de la
> **SpA chilena**, cobrando con **PayPal**, con la secuencia **EE. UU. → México → Chile**. Ver
> [`fase-1-estados-unidos.md`](fase-1-estados-unidos.md). Este documento queda como **referencia de
> optimizaciones futuras** (Shopify Payments vía Miami o LLC, tienda chilena en CLP, filial mexicana).

**Situación:** dueño chileno, empresa chilena (SpA), nómada digital (hoy en México, cambia seguido).
**Objetivo:** vender en Chile, México y Estados Unidos de la forma más optimizada posible.
**Fecha:** 26-oct-2026 · *No es asesoría legal ni tributaria: valida los puntos marcados con ⚖️ con un contador.*

---

## 1. Por qué una sola tienda no sirve para los tres países (hoy)

| Restricción | Consecuencia |
|---|---|
| En planes Basic/Grow/Advanced, **una tienda cobra a nombre de una sola entidad legal** | No se puede vender como SpA en Chile y como otra entidad en EE. UU. desde la misma tienda. Vender con varias entidades en una tienda exige **Shopify Plus** (~US$2,300/mes): no se justifica hoy |
| **Shopify Payments no está disponible en Chile** | Sin él no hay checkout en varias monedas, y las suscripciones dependen de PayPal |
| **PayPal no acepta pesos chilenos (CLP)** | En una tienda en CLP, la app de suscripciones de Shopify no puede cobrar mensualmente |
| **El lugar del inventario define los impuestos** | Un producto guardado en un país y vendido allí paga el impuesto local (Chile IVA 19%, México IVA 16%, EE. UU. sales tax) y necesita un contribuyente local |
| **Enviar una caja de un país a otro destruye el margen** | Chile cobra IVA a las importaciones de hasta US$500 desde oct-2025; México cobra 17–33.5% a la paquetería; EE. UU. suspendió el *de minimis* |

**Conclusión:** cada mercado necesita **inventario local + una entidad que pueda vender allí + una pasarela que funcione en su moneda**.

---

## 2. Estructura recomendada: 1 marca, 2 entidades, 2 tiendas (+1 después)

```
                 SpA chilena (ya existe) ── dueña de ──► LLC en EE. UU. (nueva)
                        │                                     │
             Tienda CHILE (esta tienda)             Tienda GLOBAL (nueva)
             CLP · español                          USD + MXN · inglés y español
             3PL en Santiago                        3PL en EE. UU. (+ México en fase 3)
```

| | **Tienda Chile** (esta) | **Tienda Global** (nueva) | **México** (fase 3) |
|---|---|---|---|
| Entidad que vende | SpA chilena | LLC en EE. UU. propiedad de la SpA ⚖️ | Filial mexicana de la SpA ⚖️ |
| Moneda | CLP | USD (y MXN si se usa la opción M2) | MXN |
| Pagos únicos | Flow (Webpay, tarjetas), Mercado Pago, Khipu: según disponibilidad en Shopify | Shopify Payments US (tarjetas, Apple Pay, Google Pay, Shop Pay) + PayPal | Shopify Payments MX + OXXO/SPEI |
| Suscripción mensual | **Flow Suscripciones** (inscripción de tarjeta y cobro automático) conectado a Shopify con n8n | **Shopify Subscriptions** (nativo) | Shopify Subscriptions (nativo) |
| Prepagos y regalos | Productos de pago único en Shopify ✅ (ya creados) | Productos de pago único | Productos de pago único |
| Comprobantes | Boleta electrónica SII (app e-Boletas, Bsale u OpenFactura) | Recibo · sales tax con Shopify Tax | CFDI 4.0 |
| Logística | 3PL en Santiago: **Amplifica** (partner de Shopify) o **Blue Express Fulfillment** | 3PL: **ShipMonk** o **ShipBob** | **Cubbo**, **Melonn** o **99minutos** |
| Lanzamiento | **Nov 2026** (preventa navideña) | **Feb–mar 2027** | **2º trimestre 2027** |

### Por qué es la mejor opción para un nómada
- **Nada depende de dónde vivas:** las bodegas (3PL), los bancos, las pasarelas y la contabilidad funcionan en línea.
- **La SpA ya existe:** Chile puede lanzarse ya, sin crear nada nuevo.
- **La LLC se crea y se administra a distancia**, sin residencia en EE. UU., y destraba Shopify Payments, el cobro en dólares y las suscripciones nativas.
- **No necesitas residencia en México:** México entra después con una filial de la SpA, cuando el modelo esté validado.

---

## 3. Paso a paso

### A. Tienda Chile (esta tienda), ahora

**Ya hecho por mí:** mercado Chile creado y activo · mercado México en borrador · español agregado y
publicado · descripciones adaptadas a Chile · políticas chilenas redactadas en [`docs/politicas-chile/`](politicas-chile/).

**Tú, en el admin de Shopify (unos 15 minutos):**
1. **Configuración → Detalles de la tienda:** nombre de la marca, **moneda → Peso chileno (CLP)**,
   **zona horaria → Santiago**, razón social y RUT. La moneda puede cambiarse porque aún no hay ventas.
2. **Configuración → Idiomas:** cambiar el idioma predeterminado a **Español** (hoy es inglés, por eso el checkout saldría en inglés).
3. **Configuración → Mercados:** dejar **Chile** como mercado principal, si el admin lo permite.
4. **Configuración → Políticas:** pegar los 4 textos de `docs/politicas-chile/` y completar los datos entre corchetes.
   *(El conector no tiene permiso para escribir políticas.)*
5. **Configuración → Pagos:** activar el proveedor chileno que aparezca disponible (Flow, Mercado Pago, Khipu; Webpay está en piloto).
6. Instalar una app de **boleta electrónica SII**.
7. Avísame cuando la moneda esté en CLP: cargo los precios en pesos chilenos (tabla en `PLAN.md` §2).

**Después:** cotizar con Amplifica y Blue Express (almacenaje, armado de cajas y despacho) · abrir una
cuenta en Flow y crear los planes de suscripción · yo armo la automatización Flow → pedido en Shopify (n8n).

### B. LLC en EE. UU. (empezar ya: tarda 3–8 semanas)

| Paso | Detalle | Tiempo |
|---|---|---|
| 1. Formar la LLC | Wyoming o Delaware, con un servicio de constitución para no residentes (Stripe Atlas, doola, Firstbase) | 1–7 días |
| 2. Dueña | **La SpA chilena** como socia única (consolida todo bajo tu empresa) ⚖️ | — |
| 3. EIN | Lo tramita el servicio de constitución (formulario SS-4) | 1–6 semanas |
| 4. Banco en EE. UU. | Mercury, Relay o Wise Business (verificar que acepten dueños desde Chile) | 1–2 semanas |
| 5. Dirección física en EE. UU. | Shopify Payments **rechaza direcciones virtuales**: se necesita una dirección real (oficina o coworking con contrato) | — |
| 6. Tienda Global | Crear la tienda a nombre de la LLC; yo copio el catálogo, las colecciones y los textos (en inglés y español) | 1 día |
| 7. Shopify Payments US | Los representantes no residentes pueden identificarse con pasaporte. La aprobación es manual y puede ser rechazada | Días a semanas |
| Respaldo | Si rechazan Shopify Payments: **PayPal Business** (sí admite suscripciones en USD) | — |

**Obligaciones de la LLC ⚖️:** Form 5472 + 1120 *pro forma* cada año (multa mínima de US$25,000 si se
omite) · reporte anual del estado · sales tax con Shopify Tax según el *nexus* · si el inventario está en
EE. UU., probablemente haya ingreso "efectivamente conectado" y una declaración 1120-F. Chile y EE. UU.
tienen un convenio para evitar la doble tributación. **Contratar un CPA para dueños no residentes.**

### C. México (fase 3)

| Opción | Cómo | Cuándo usarla |
|---|---|---|
| **M1. Filial mexicana** (recomendada) | S. de R.L. de C.V. propiedad de la SpA ⚖️: RFC, CFDI, IVA, padrón de importadores y **Shopify Payments MX** → tercera tienda | Cuando Chile y EE. UU. estén validados, o si la lista de espera de México supera ~500 personas |
| **M2. Prueba sin entidad** | Mercado México en la tienda Global, cobrando en MXN y enviando desde el 3PL de EE. UU. con impuestos pagados (DDP) | Solo para regalos o ediciones especiales: el envío transfronterizo es caro y lento |
| **Mientras tanto** | Lista de espera para México en la tienda Global | Desde el lanzamiento en EE. UU. |

*Si en algún momento decides quedarte 6 meses o más en México con residencia temporal, podrías sacar un RFC
como persona física: es la vía más rápida para Shopify Payments MX, pero no encaja con tu vida de nómada.*

---

## 4. Costos aproximados de la estructura *(supuestos, verificar)*

| Concepto | Costo |
|---|---|
| 2 tiendas Shopify Basic | ~US$80/mes |
| Formación de la LLC + agente registrado | ~US$300–800 el primer año |
| CPA de EE. UU. (5472, 1120 y estado) | ~US$600–1,500/año |
| Banco en EE. UU. | US$0–20/mes |
| Contador en Chile | El que ya tienes |
| Filial mexicana (fase 3) | ~US$1,500–3,500 de constitución + US$200–500/mes de contabilidad |

---

## 5. Validar con tu contador ⚖️
1. Que la SpA sea la dueña de la LLC (o tú personalmente) y cómo tributa en Chile lo que gane la LLC.
2. Tu **residencia tributaria personal** como nómada (define dónde tributas lo que retires).
3. Si el inventario en el 3PL de EE. UU. genera ingreso efectivamente conectado y qué declaración corresponde.
4. La estructura de la filial mexicana y el representante legal cuando llegue la fase 3.

### Fuentes
- [Requisitos de Shopify Payments en EE. UU. (pasaporte para no residentes)](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-states/requirements)
- [Shopify no acepta direcciones virtuales para Shopify Payments US (Shopify Community)](https://community.shopify.com/t/setting-up-shopify-payments-on-llc-and-ein-without-ssn/402552/1)
- [Rechazos a vendedores no residentes en 2026 (NVinc, fuente secundaria)](https://nvinc.com/shopify-payments-us-is-rejecting-non-resident-sellers/)
- [Países con Shopify Payments](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries)
- [Suscripciones en Chile: solo PayPal Express (Shopify Community)](https://community.shopify.com/t/app-suscripcion-que-sirva-en-chile/286157)
- [App de Webpay en Shopify (en piloto)](https://apps.shopify.com/webpay)
- [Flow en Shopify](https://chocale.cl/2023/07/flow-pasarela-pagos-shopify-e-commerce-chile/)
- [Manual de Flow Suscripciones](https://web.flow.cl/manual-suscripciones-flowpagos.pdf)
- [Mercado Pago Suscripciones Chile](https://www.mercadopago.cl/herramientas-para-vender/suscripciones)
- [App e-Boletas DTE Chile SII](https://apps.shopify.com/e-boleta)
- [IVA a compras internacionales en Chile (Aduanas)](https://www.aduana.cl/desde-cuando-y-a-quien-aplica/aduana/2025-10-20/120230.html)
- [Amplifica, fulfillment para Shopify en Chile](https://www.shopify.com/partners/directory/partner/amplifica-spa)
- [Blue Express Fulfillment](https://www.blue.cl/en/fulfillment-en/)
- [Form 5472 para LLC de dueño extranjero](https://help.taxesforexpats.com/en/articles/11143846-us-single-member-llc-owned-by-a-nonresident-alien-nra)
- [IVA a ventas de extranjeros con bienes en México (Expansión)](https://expansion.mx/especiales/2013/10/23/en-ecommerce-como-se-pagan-impuestos)
- [Gasto en mascotas en Chile (CNC, ago-2026)](https://chocale.cl/2026/08/gasto-en-mascotas-sube-un-63-en-los-hogares-de-chile/)
- [Estudio Mascotas Cadem (ago-2026)](https://cadem.cl/wp-content/uploads/2026/08/Brochure-Mascotas-2026_agosto.pdf)
