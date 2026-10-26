# tienda1 — Club mensual para perros y gatos

Repositorio de trabajo de la tienda online: plan, decisiones y registro de cada cambio hecho en
Shopify y AutoDS.

| | |
|---|---|
| Esta tienda | `mcgsp1-yj.myshopify.com` → **tienda Chile** (SpA chilena, CLP) |
| Tienda futura | Tienda Global a nombre de una LLC en EE. UU. (USD; México en fase 3) |
| Proveedor conectado | AutoDS (tienda `5917626`): recomendación, cancelar antes del 29-oct |
| Modelo | Suscripción mensual de cajas temáticas (Club Perro y Club Gato) + regalos + extras |
| Secuencia | 🇨🇱 Chile (nov 2026) → 🇺🇸 EE. UU. (mar 2027) → 🇲🇽 México (2º trim. 2027) |

## Documentos

- [`PLAN.md`](PLAN.md): plan maestro (productos y precios por país, selección de productos, operación, economía, Shopify, legal, marketing y hoja de ruta).
- [`docs/estructura-paises-y-pagos.md`](docs/estructura-paises-y-pagos.md): entidades, tiendas, pagos e impuestos por país.
- [`docs/politicas-chile/`](docs/politicas-chile/): términos, suscripción, devoluciones y despacho (para pegar en Shopify).
- [`CHANGELOG.md`](CHANGELOG.md): bitácora de todos los cambios en la tienda.
- [`docs/auditoria-2026-10-26.md`](docs/auditoria-2026-10-26.md): estado de la tienda antes de empezar.
- [`data/catalogo-shopify.csv`](data/catalogo-shopify.csv): catálogo con IDs, SKU y precios en CLP, MXN y USD.
- [`data/eliminados-autods-2026-10-26.csv`](data/eliminados-autods-2026-10-26.csv): productos eliminados.

## Regla del repo

Todo cambio en la tienda (productos, precios, colecciones, apps, configuración) se anota en
`CHANGELOG.md` con fecha, IDs y motivo.
