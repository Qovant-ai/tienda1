# Auditoría inicial — 26 oct 2026

Estado real de la tienda y las herramientas al empezar el proyecto (antes de cualquier cambio).

## 1. Shopify

| Dato | Valor encontrado | Debería ser |
|---|---|---|
| Dominio | `mcgsp1-yj.myshopify.com` (sin dominio propio) | Dominio `.com` de la marca |
| Nombre de la tienda | `bys-user-store-1140213` (nombre genérico de AutoDS "Build Your Store") | Nombre de la marca |
| Plan | Basic | OK para empezar |
| Moneda | MXN | USD (fase 1: EE. UU.) |
| Impuestos incluidos en el precio | Sí | EE. UU.: impuesto sumado en el checkout (ya configurado en el mercado) |
| **País del negocio** | **Chile** (Merced 838 A, Santiago) | Chile (SpA): correcto para cobrar con PayPal |
| **Zona horaria** | **America/New_York** | OK para la fase 1 (EE. UU.) |
| Ubicación de inventario | Santiago, Chile | 3PL en EE. UU. |
| Mercados | Solo "Mexico" (principal) | EE. UU. activo; México y Chile en borrador |
| Tema activo | "Build Your Store Theme" (de AutoDS) | **Horizon** (publicado por el dueño) |
| Políticas | Solo privacidad | + Términos de suscripción, Envíos, Reembolsos |
| Billeteras digitales | Ninguna activa | Con PayPal no aplican; Shop Pay, Apple Pay y Google Pay requieren Shopify Payments |
| Canales | Tienda online, Shop, POS | OK |

### Hallazgo crítico: país = Chile
**Shopify Payments no parece estar disponible para negocios en Chile** (verificar en *Configuración → Pagos*).
Sin Shopify Payments, las suscripciones solo pueden cobrarse con PayPal Express (o Stripe/Authorize.net
en casos limitados). Además, la tienda opera en MXN para México con una dirección de Chile.
**Resuelto:** una sola tienda a nombre de la SpA, cobrando con PayPal en USD, empezando por EE. UU. (ver `docs/fase-1-estados-unidos.md`).

## 2. AutoDS

| Dato | Valor |
|---|---|
| Tienda vinculada | id `5917626` (Shopify) |
| Plan | Prueba activa, **vence el 29-oct-2026 00:16 UTC** (y se cobra ese día) |
| Add-on | `orders_processor` (Fulfilled by AutoDS), también en prueba hasta el 29-oct |
| Créditos | 5 de auto-pedido · 400 de búsqueda de productos · 30 de reescritura con IA |
| Pedidos | 0 |

El feed gratuito de "productos ganadores" de AutoDS devolvió artículos que no son de mascotas
(arcos de juguete, fajas, etc.): no sirve para elegir productos.

## 3. Catálogo encontrado (10 productos, ya eliminados)

Snapshot: [`data/eliminados-autods-2026-10-26.csv`](../data/eliminados-autods-2026-10-26.csv)

| Problema | Detalle |
|---|---|
| **Error de moneda (confirmado)** | Precios con cifras de USD guardados en MXN: cepillo a **$7.99 MXN** (costo ~US$6), árbol para gato a $49.99 MXN (costo ~US$40). Cada venta habría perdido ~95% del costo. |
| Margen | Aun en USD, el precio era solo 1.25–1.35× el costo (margen bruto ~20%). |
| Idioma | Títulos y descripciones en inglés. |
| Inventario | Sin seguimiento y sin costo unitario registrado. |
| Encaje con el modelo | Productos genéricos y voluminosos, no aptos para una caja mensual. |
| Envío a México | Proveedor sin almacén en México: impuestos de importación y tiempos largos. |

**Acción tomada:** los 10 productos se eliminaron de AutoDS y de Shopify (a petición del dueño)
y se reemplazaron por el catálogo del club. Ver `CHANGELOG.md`.

## 4. Implicación principal

**AutoDS + dropshipping no puede armar por sí solo una "caja" mensual.** Cada producto sale de un
proveedor distinto y llega en un paquete distinto. Un club por suscripción necesita **inventario propio
y armado (kitting)**, ya sea propio o con un 3PL. Ver `PLAN.md`, secciones 3 y 4.
