# Tema "Pawlet Club"

Copia sin publicar del tema **Helio** (familia Horizon 4.3.0), creada el 26-oct-2026.

| | |
|---|---|
| ID del tema | `gid://shopify/OnlineStoreTheme/189338452030` |
| Origen | Helio (`189253615678`, tema publicado hasta ahora) |
| Estado | **Sin publicar.** Se publica desde *Tienda online → Temas → Pawlet Club → Publicar* |

Esta carpeta guarda **solo los archivos modificados o nuevos**, con el mismo contenido que se subió al tema.

## Archivos modificados

| Archivo | Cambio |
|---|---|
| `config/settings_data.json` | Logo, logo blanco y favicon; tipografía Rubik; paleta azul noche + durazno; botones, tarjetas y campos redondeados |
| `sections/header-group.json` | Encabezado blanco (sin transparencia en inicio, producto y colección), línea divisoria, sin selector de país |
| `sections/footer-group.json` | Bloque de suscripción al boletín sobre durazno, columnas de enlaces sobre azul (menús `footer-club` y `footer`), sin "Powered by Shopify" ni redes sociales vacías |
| `templates/index.json` | Página de inicio nueva (7 secciones) |

## Archivos nuevos

| Archivo | Qué es |
|---|---|
| `snippets/pawlet-styles.liquid` | Colores de marca (leídos de la paleta del tema) y estilos compartidos: botones, títulos, enlaces |
| `snippets/pawlet-icon.liquid` | Íconos de marca en SVG: huellas, caja, camión, regalo, etc. |
| `sections/pawlet-hero.liquid` | Portada: título con subrayado durazno, 2 botones, 3 beneficios, foto en arco, sello de precio |
| `sections/pawlet-steps.liquid` | Cómo funciona (pasos numerados) |
| `sections/pawlet-plans.liquid` | Tarjetas de Club Dog y Club Cat (precio desde el producto, con texto de respaldo) |
| `sections/pawlet-inside.liquid` | Qué trae cada caja |
| `sections/pawlet-shop.liquid` | Mosaicos de la tienda a la carta (perros, gatos, extras) |
| `sections/pawlet-gift.liquid` | Franja "Regala el Club" con foto |
| `sections/pawlet-faq.liquid` | Preguntas frecuentes en acordeón |

Todas las secciones se editan desde el editor de temas (textos, colores, fotos, enlaces y bloques) y se
pueden agregar a otras páginas. Pasaron **Theme Check** sin errores.

## Antes de publicar

- Los productos están en **borrador**: los botones de Club Dog y Club Cat llevan a páginas que todavía no
  se ven en la tienda, y los planes muestran el precio de respaldo. Al activar los productos, el precio sale
  del producto.
- Revisar la vista previa en computador y en celular.
