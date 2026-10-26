// Convierte los SVG del logo a PNG transparentes con Chromium.
// Uso: node render_png.js <carpeta_svg> <carpeta_png>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [src, out] = process.argv.slice(2);
const jobs = [
  ['pawlet-logo-horizontal.svg', 2000],
  ['pawlet-logo-horizontal-white.svg', 2000],
  ['pawlet-logo-stacked.svg', 1200],
  ['pawlet-logo-stacked-white.svg', 1200],
  ['pawlet-icon.svg', 1024],
  ['pawlet-favicon.svg', 512],
];

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage();
  for (const [file, width] of jobs) {
    const svg = fs.readFileSync(path.join(src, file), 'utf8');
    const [, , vw, vh] = svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);
    const height = Math.round((width * vh) / vw);
    await page.setViewportSize({ width, height });
    const sized = svg.replace(/width="[^"]+" height="[^"]+"/, `width="${width}" height="${height}"`);
    await page.setContent(`<html><body style="margin:0;background:transparent">${sized}</body></html>`);
    await page.screenshot({
      path: path.join(out, file.replace('.svg', '.png')),
      omitBackground: true,
      clip: { x: 0, y: 0, width, height },
    });
    console.log(file, width, 'x', height);
  }
  await browser.close();
})();
