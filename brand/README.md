# Marca Pawlet Club

**Pawlet** = *paw* (pata) + *-let* (diminutivo): "patita". **Club** remite al modelo de suscripción,
como los clubes de vino. Elegida el 26-oct-2026.

## Logo

Huella grande (perro) y huella chica (gato). Los textos están convertidos a trazos, así que los SVG
no dependen de ninguna fuente.

| Archivo | Uso |
|---|---|
| `logo/pawlet-logo-horizontal.svg` · `.png` | Logo principal sobre fondos claros (encabezado de la tienda) |
| `logo/pawlet-logo-horizontal-white.svg` · `.png` | Sobre fondos oscuros (azul noche, fotos) |
| `logo/pawlet-logo-stacked.svg` · `.png` | Versión vertical (empaque, redes, stickers) |
| `logo/pawlet-logo-stacked-white.svg` · `.png` | Versión vertical sobre fondos oscuros |
| `logo/pawlet-icon.svg` · `.png` | Solo las huellas (sellos, fondo de agua, detalles) |
| `logo/pawlet-favicon.svg` · `.png` | Ícono de la tienda y foto de perfil en redes |

Reglas:
- Deja alrededor del logo un espacio libre de al menos la altura de la huella chica.
- No lo uses a menos de 120 px de ancho (versión horizontal); por debajo, usa el ícono.
- No cambies los colores fuera de la paleta ni deformes las proporciones.

En Shopify ya están subidos a **Contenido → Archivos** con los mismos nombres.

## Paleta

| Rol | Color | Hex |
|---|---|---|
| Principal (textos, botones, fondos oscuros) | Azul noche | `#1B2B48` |
| Acento (huella chica, destacados, botones sobre azul) | Durazno | `#FF9F6E` |
| Fondo cálido (secciones alternas) | Crema durazno | `#FFF3EA` |
| Apoyo (tarjetas abiertas, íconos) | Durazno suave | `#FFE7D6` |
| Texto secundario | Azul pizarra | `#3B4A66` |
| Líneas y bordes | Arena | `#E7DFD6` |

Contraste: azul sobre blanco o crema cumple AA de sobra. **No uses el durazno para texto sobre fondo
blanco** (no tiene contraste suficiente); sobre durazno, el texto va en azul noche.

## Tipografía

**Rubik** (Google Fonts, incluida en la biblioteca de fuentes de Shopify): SemiBold 600 para títulos y
el logo, Regular 400 para textos y Medium 500 para botones y subtítulos.

## Fotos de la página de inicio

Fotos de Unsplash (licencia libre para uso comercial, sin atribución obligatoria):
- Portada: perro y gato jugando, de Kevin Turcios.
- Regalo: gato sobre silla azul junto a un perro, de Jack Prommel.

Conviene reemplazarlas por fotos propias de las cajas cuando haya inventario.

## Cómo regenerar los archivos

```bash
# 1. Fuentes Rubik 400 y 600 (TTF) en una carpeta, por ejemplo fonts/
# 2. SVG
python3 brand/tools/make_logo.py fonts/ brand/logo
# 3. PNG (usa el Chromium de Playwright)
node brand/tools/render_png.js brand/logo brand/logo/png
```
