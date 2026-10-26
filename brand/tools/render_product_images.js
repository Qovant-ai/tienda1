// Convierte las páginas HTML de make_product_images.py en JPG de 1600 x 1600 con Chromium.
// Uso: node render_product_images.js <carpeta_html> <carpeta_jpg>
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [src, out] = process.argv.slice(2);
const SIZE = 1600;

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: SIZE, height: SIZE } });
  const files = fs.readdirSync(src).filter((f) => f.endsWith('.html')).sort();
  for (const file of files) {
    await page.goto('file://' + path.resolve(src, file));
    await page.evaluate(() => document.fonts.ready);
    await page.waitForLoadState('networkidle');
    await page.screenshot({
      path: path.join(out, file.replace('.html', '.jpg')),
      type: 'jpeg',
      quality: 90,
      clip: { x: 0, y: 0, width: SIZE, height: SIZE },
    });
    console.log(file);
  }
  await browser.close();
})();
