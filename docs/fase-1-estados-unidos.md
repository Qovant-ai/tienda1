# Fase 1 — Estados Unidos con PayPal

**Modelo:** una sola tienda (esta), a nombre de la **SpA chilena**, cobrando con **PayPal** en **USD**.
**Secuencia:** 🇺🇸 EE. UU. → 🇲🇽 México → 🇨🇱 Chile. · **Fecha:** 26-oct-2026
*Los puntos ⚖️ deben validarse con un contador (Chile) o un CPA (EE. UU.).*

---

## 1. Lo que ya está configurado en Shopify

| Área | Estado |
|---|---|
| Mercados | **Estados Unidos activo** (impuesto sumado en el checkout) · México y Chile en borrador |
| Idioma | Inglés como idioma principal (ideal para EE. UU.) · **español publicado** como segundo idioma (público latino; México y Chile después) |
| Catálogo | 12 productos y 4 colecciones **en inglés**, con traducción completa al español · precios en USD · todo en borrador |
| Envíos | Zona única: **48 estados contiguos + DC**. **Gratis desde $30**; $5.99 por debajo. Se eliminaron las tarifas heredadas de AutoDS (150 y 360 MXN) |
| Zona horaria | America/New_York ✅ |
| Políticas | Redactadas en inglés en [`politicas-usa/`](politicas-usa/) (para pegar; el conector no puede escribirlas) |

## 2. Lo que te toca a ti (en este orden)

1. ✅ **Moneda de la tienda → USD** (hecho).
2. **Nombre de la tienda → Pawlet Club** y datos de la empresa (razón social de la SpA). **Publicar el tema "Pawlet Club"**.
3. ✅ **PayPal conectado** (hecho).
4. **Pedir a PayPal las "transacciones de referencia"** (*reference transactions*). Sin esa aprobación,
   PayPal no permite cobros automáticos y las suscripciones no funcionan. PayPal revisa la cuenta (puede
   pedir información del negocio). Es el paso con más espera: hazlo ya.
5. **Instalar Shopify Subscriptions** y crear los planes de Club Dog y Club Cat (mensual, cobro fijo el día 1).
6. **Pegar las 4 políticas** de `docs/politicas-usa/` en *Configuración → Políticas* y completar los
   datos entre corchetes. Generar la política de privacidad con la app gratuita de Shopify para cumplir
   con la ley de privacidad de California (CCPA).
7. **AutoDS:** mantenerlo. La tienda a la carta (correas, camas, rascadores) hace los pedidos automáticos con AutoDS.
   Elige el plan más barato antes del 29-oct y revisa en *Settings → Pricing* que la regla de precios no
   baje los precios que cargué (recomendado: costo × 2.2 como mínimo, o desactivar el ajuste automático de precio).

## 3. Operación en EE. UU.

| Tema | Recomendación |
|---|---|
| **Inventario** | Comprar a **mayoristas en EE. UU.** (no hay que importar) o marcas hechas en EE. UU. o México. Importar desde China implica ser importador registrado y pagar aranceles altos en 2026 |
| **3PL (bodega y armado)** | Cotizar **ShipMonk** y **ShipBob** (aceptan marcas extranjeras y arman cajas de suscripción). Se conectan con Shopify |
| **Optimización fiscal del 3PL** | El inventario en un estado obliga a registrarse para el *sales tax* en ese estado. Una bodega en un estado **sin sales tax** (Delaware, Oregon, New Hampshire, Montana) evita ese registro, a cambio de envíos algo más caros a la costa opuesta ⚖️ |
| **Sales tax** | Registrarse en el estado del 3PL (si tiene sales tax) y activar el cobro en *Configuración → Impuestos*. En los demás estados solo hay obligación al superar sus umbrales de ventas (muchos usan US$100,000 al año) |
| **Impuesto a la renta en EE. UU.** | Con el convenio Chile–EE. UU., una bodega de un tercero usada solo para almacenar y despachar normalmente **no constituye establecimiento permanente**: las utilidades tributarían en Chile ⚖️ (validar con un CPA y si conviene presentar declaración informativa) |
| **Retiro de fondos** | PayPal → banco chileno vía intermediarios (Tenpo, Global66) o retiro directo. Comparar comisión y tipo de cambio |

## 4. Costos de cobro con PayPal *(supuestos, verificar en tu cuenta)*

| Concepto | Club Dog US$39.99 |
|---|---|
| Comisión PayPal (cuenta chilena, venta internacional, ~5–6% + US$0.30) | ≈ –2.50 |
| Comisión de Shopify por pasarela externa (plan Basic: 2%) | –0.80 |
| **Total cobro** | **≈ –3.30 (8%)** |
| Productos, empaque, armado y envío | –24.50 |
| Apps | –0.40 |
| **Margen de contribución** | **≈ 11.80 (29%)** |

Con Shopify Payments el cobro costaría ~US$1.46 (2.9% + 30¢) y el margen subiría a ~33%. Ver sección 6.

## 5. Calendario

| Semana | Entregables |
|---|---|
| 26 oct–1 nov | Moneda USD · PayPal + transacciones de referencia · Shopify Subscriptions · políticas · marca · plan de AutoDS (antes del 29-oct) |
| 2–15 nov | Proveedores mayoristas en EE. UU. · muestras · cotizaciones de 3PL · registro de sales tax (si aplica) |
| 16–30 nov | Contrato con el 3PL · primer inventario · fotos reales · páginas (Inicio, How it works, FAQ) · lista de espera |
| Dic 2026 | *(Opcional)* Holiday Box si el inventario llega al 3PL antes del ~5 de diciembre · pruebas de pedido y de suscripción |
| **Ene 2027** | **Lanzamiento del Club en EE. UU.** ("New Year, New Box") · anuncios en NY, LA, Miami, Chicago y Boston + público latino |

> **Cambio del 27-oct-2026:** el Club se abrió de inmediato como **plan prepagado** (1, 3 o 6 meses, pago único,
> sin renovación automática; primeras cajas del 8 al 10 de noviembre). La suscripción con cobro mensual
> automático se agrega cuando PayPal apruebe las transacciones de referencia y esté instalada Shopify
> Subscriptions (pasos 4 y 5).

## 6. ¿Y la dirección fiscal de Miami?

**No es necesaria para esta fase.** Con PayPal, la tienda funciona con la dirección chilena actual.

Puede servir **después** para pedir **Shopify Payments EE. UU.**, que significaría:
- cobro con tarjeta directo (sin depender de PayPal), Apple Pay, Google Pay y Shop Pay;
- comisión de ~2.9% + 30¢ y **sin el 2% extra de Shopify** (~US$1.30 de ahorro por caja);
- suscripciones nativas sin esperar la aprobación de PayPal;
- **cobro en pesos mexicanos y chilenos** para las fases 2 y 3.

Requisitos (todos): que la SpA tenga **EIN** y una **cuenta bancaria en EE. UU. a su nombre**, que la
dirección de Miami sea una **oficina física (no virtual ni de agente registrado)** y, probablemente, que la
SpA esté registrada como empresa extranjera en Florida ⚖️. Cambiar la dirección sin cumplirlos puede
terminar en rechazo o en fondos retenidos. **Si me confirmas esos datos, lo evaluamos para después del lanzamiento.**

## 7. Fases siguientes (resumen)

| Fase | Cómo cobrar | Punto a resolver |
|---|---|---|
| 🇲🇽 México | PayPal en USD (PayPal convierte al cliente) o, con Shopify Payments, en MXN | Vender desde inventario en México exige un contribuyente mexicano (filial) o despachar desde el 3PL de EE. UU. con impuestos pagados |
| 🇨🇱 Chile | PayPal no acepta CLP: cobrar en USD o sumar Shopify Payments (CLP) o una tienda chilena con Flow | La SpA ya es contribuyente local: IVA 19% y boleta |

### Fuentes
- [Suscripciones con PayPal: requieren transacciones de referencia (Ordergroove)](https://help.ordergroove.com/hc/en-us/articles/1500011030302-PayPal-for-Subscriptions)
- [Subscriptions API admite PayPal (Shopify changelog)](https://shopify.dev/changelog/subscriptions-apis-now-support-paypal-express.md)
- [Aprobación de transacciones de referencia (WooCommerce)](https://woocommerce.com/document/paypal-reference-transactions/)
- [Comisión de Shopify por pasarelas externas](https://qualimero.com/en/blog/shopify-transaction-fees)
- [Basic + PayPal donde no hay Shopify Payments (Shopify Community)](https://community.shopify.com/t/shopify-transaction-fees-with-3rd-party-provider/265747)
- [Multimoneda solo con Shopify Payments (Shopify Community)](https://community.shopify.com/t/multicurrency-in-checkout-without-shopify-payments/246427)
- [Retiro de PayPal a Chile (Tenpo)](https://www.tenpo.cl/paypal/retirar-dolares-paypal)
- [Requisitos de Shopify Payments EE. UU.](https://help.shopify.com/en/manual/payments/shopify-payments/supported-countries/united-states/requirements)
- [Direcciones virtuales no aceptadas (Shopify Community)](https://community.shopify.com/t/setting-up-shopify-payments-on-llc-and-ein-without-ssn/402552/1)
