# tienda1 — Gift List Co, regalos ordenados por destinatario

Repositorio de trabajo de la tienda online: plan, decisiones y registro de cada cambio hecho en
Shopify y AutoDS.

> **6-nov-2026:** la tienda dejó de ser Pawlet Club (mascotas) y pasó a ser **Gift List Co**: 14 regalos con
> envío gratis desde EE. UU., ordenados en 11 destinatarios. Ver [`docs/tienda-regalos.md`](docs/tienda-regalos.md)
> y [`theme-giftlist/README.md`](theme-giftlist/README.md). Lo de Pawlet Club queda como historial.

| | |
|---|---|
| Marca | **Gift List Co** · logo en [`brand/logo-giftlist/`](brand/logo-giftlist/), imágenes en [`brand/gift-images/`](brand/gift-images/README.md) (antes: Pawlet Club, en [`brand/`](brand/README.md)) |
| Tienda | `mcgsp1-yj.myshopify.com` · una sola tienda · SpA chilena |
| Tema | "Gift List Co v1" (**sin publicar**): ver [`theme-giftlist/`](theme-giftlist/README.md). Historial de Pawlet en [`theme/`](theme/README.md) |
| Cobro | PayPal (USD) |
| Secuencia | 🇺🇸 EE. UU. (lanzamiento ene 2027) → 🇲🇽 México → 🇨🇱 Chile |
| Idiomas | Inglés (principal) + español |
| Modelo | Tienda de regalos dropshipping (AutoDS, bodegas en EE. UU.), filtrada por destinatario |
| Proveedor conectado | AutoDS (tienda `5917626`): mantenerlo (tienda a la carta); elegir plan antes del 29-oct |

## Documentos

- [`PLAN.md`](PLAN.md): plan maestro.
- [`brand/README.md`](brand/README.md): guía de marca y archivos del logo.
- [`theme/README.md`](theme/README.md): cambios del tema y de la página de inicio.
- [`docs/fase-1-estados-unidos.md`](docs/fase-1-estados-unidos.md): **fase actual**, con el paso a paso, comisiones y la opción de Miami.
- [`docs/tienda-regalos.md`](docs/tienda-regalos.md): **Gift List Co**: nombres, productos, destinatarios y estado en Shopify.
- [`docs/politicas-usa/`](docs/politicas-usa/): Terms, Refund y Shipping de Gift List Co (para pegar en Shopify).
- [`docs/politicas-chile/`](docs/politicas-chile/): políticas para la fase 3.
- [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md): estructuras alternativas para optimizar más adelante.
- [`CHANGELOG.md`](CHANGELOG.md): bitácora de todos los cambios en la tienda.
- [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md): estado de la tienda antes de empezar.
- [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv): catálogo con IDs, SKU y precios en USD, MXN y CLP.
- [`data/eliminados-autods-2026-10-26.csv`](data/eliminados-autods-2026-10-26.csv): productos eliminados.

## Regla del repo

Todo cambio en la tienda (productos, precios, colecciones, apps, configuración) se anota en
`CHANGELOG.md` con fecha, IDs y motivo.
