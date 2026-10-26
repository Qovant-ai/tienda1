# tienda1 — Club mensual para perros y gatos

Repositorio de trabajo de la tienda online: plan, decisiones y registro de cada cambio hecho en
Shopify y AutoDS.

| | |
|---|---|
| Tienda | `mcgsp1-yj.myshopify.com` · una sola tienda · SpA chilena |
| Cobro | PayPal (USD) |
| Secuencia | 🇺🇸 EE. UU. (lanzamiento ene 2027) → 🇲🇽 México → 🇨🇱 Chile |
| Idiomas | Inglés (principal) + español |
| Modelo | Suscripción mensual de cajas temáticas (Club Dog y Club Cat) + regalos + extras |
| Proveedor conectado | AutoDS (tienda `5917626`): mantenerlo (tienda a la carta); elegir plan antes del 29-oct |

## Documentos

- [`PLAN.md`](PLAN.md): plan maestro.
- [`docs/fase-1-estados-unidos.md`](docs/fase-1-estados-unidos.md): **fase actual**, con el paso a paso, comisiones y la opción de Miami.
- [`docs/politicas-usa/`](docs/politicas-usa/): Terms, Subscription, Refund y Shipping (para pegar en Shopify).
- [`docs/politicas-chile/`](docs/politicas-chile/): políticas para la fase 3.
- [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md): estructuras alternativas para optimizar más adelante.
- [`CHANGELOG.md`](CHANGELOG.md): bitácora de todos los cambios en la tienda.
- [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md): estado de la tienda antes de empezar.
- [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv): catálogo con IDs, SKU y precios en USD, MXN y CLP.
- [`data/eliminados-autods-2026-10-26.csv`](data/eliminados-autods-2026-10-26.csv): productos eliminados.

## Regla del repo

Todo cambio en la tienda (productos, precios, colecciones, apps, configuración) se anota en
`CHANGELOG.md` con fecha, IDs y motivo.
