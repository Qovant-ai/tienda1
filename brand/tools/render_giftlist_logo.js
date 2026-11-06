// Convierte los SVG del logo Gift List Co a PNG y arma una vista previa.
// Uso: node render_giftlist_logo.js brand/logo-giftlist brand/logo-giftlist/png
const fs=require('fs'),path=require('path');const {chromium}=require('playwright');
const [src,out]=process.argv.slice(2);
const jobs=[['giftlist-logo-horizontal.svg',2000],['giftlist-logo-horizontal-white.svg',2000],['giftlist-icon.svg',1024],['giftlist-favicon.svg',512]];
(async()=>{fs.mkdirSync(out,{recursive:true});const b=await chromium.launch();const p=await b.newPage();
for(const [f,w] of jobs){const svg=fs.readFileSync(path.join(src,f),'utf8');const [, , vw, vh]=svg.match(/viewBox="([^"]+)"/)[1].split(/\s+/).map(Number);const h=Math.round(w*vh/vw);
await p.setViewportSize({width:w,height:h});await p.setContent(`<html><body style="margin:0;background:transparent">${svg.replace(/width="[^"]+" height="[^"]+"/,`width="${w}" height="${h}"`)}</body></html>`);
await p.screenshot({path:path.join(out,f.replace('.svg','.png')),omitBackground:true,clip:{x:0,y:0,width:w,height:h}});}
await p.setViewportSize({width:900,height:420});
const a=fs.readFileSync(path.join(src,'giftlist-logo-horizontal.svg'),'utf8'), c=fs.readFileSync(path.join(src,'giftlist-logo-horizontal-white.svg'),'utf8');
await p.setContent(`<body style="margin:0"><div style="background:#fff6f0;padding:40px">${a.replace(/width="[^"]+" height="[^"]+"/,'height="90"')}</div><div style="background:#24203f;padding:40px">${c.replace(/width="[^"]+" height="[^"]+"/,'height="90"')}</div></body>`);
await p.screenshot({path:path.join(out,'preview.png')});await b.close();})();
