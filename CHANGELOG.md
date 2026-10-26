# Bitácora de cambios

Registro de todos los cambios en la tienda (Shopify, AutoDS y configuración). El más reciente va primero.

## 2026-10-26

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
