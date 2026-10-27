// Convierte las páginas de compose_scenes.py en JPG, con el tamaño que indica cada página (<meta name="size">).
// Uso: node render_scenes.js <carpeta_html> <carpeta_jpg> [nombres...]
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

const [src, out, ...only] = process.argv.slice(2);

(async () => {
  fs.mkdirSync(out, { recursive: true });
  const browser = await chromium.launch();
  const files = fs
    .readdirSync(src)
    .filter((f) => f.endsWith('.html') && (!only.length || only.includes(f.replace('.html', ''))));
  for (const file of files) {
    const html = fs.readFileSync(path.join(src, file), 'utf8');
    const [width, height] = html.match(/content="(\d+)x(\d+)"/).slice(1).map(Number);
    const page = await browser.newPage({ viewport: { width, height } });
    await page.goto('file://' + path.resolve(src, file));
    await page.waitForLoadState('networkidle');
    await page.screenshot({ path: path.join(out, file.replace('.html', '.jpg')), type: 'jpeg', quality: 90 });
    await page.close();
    console.log(file);
  }
  await browser.close();
})();
