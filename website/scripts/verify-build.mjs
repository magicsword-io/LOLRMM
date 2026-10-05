import fs from 'node:fs';
import assert from 'node:assert/strict';
import vm from 'node:vm';
const out = new URL('../dist/', import.meta.url);
const read = (file) => fs.readFileSync(new URL(file, out), 'utf8');
const tools = JSON.parse(read('api/rmm_tools.json'));
assert.equal(JSON.parse(read('api/rmm_tools_count.json')).count, tools.length);
const index = JSON.parse(read('data/search.json'));
assert.equal(index.length, tools.length);
assert(!read('data/search.json').includes('certificate_der_base64'));
const pages = [
  'index.html',
  'about/index.html',
  'api/index.html',
  'detections/index.html',
  '404.html',
  ...index.map((t) => `tools/${t.slug}/index.html`),
];
const broken = new Set();
for (const file of pages) {
  const html = read(file);
  assert(
    html.includes('<html lang="en"'),
    `Missing document language: ${file}`,
  );
  const enabled = process.env.PUBLIC_ENABLE_ANALYTICS === 'true';
  assert.equal(
    (html.match(/googletagmanager\.com\/gtag\/js\?id=G-D04FRZLYM5/g) || [])
      .length,
    enabled ? 1 : 0,
    `Analytics mismatch: ${file}`,
  );
  assert(
    !html.includes('G-33C5VXLWPQ'),
    'LOLDrivers analytics must not be carried over',
  );
  for (const [, raw] of html.matchAll(
    /(?:href|src)="(\/[^"?#]*)(?:[?#][^"]*)?"/g,
  )) {
    if (raw.startsWith('//')) continue;
    const relative = decodeURIComponent(raw.slice(1));
    const asset = new URL(relative, out);
    if (!fs.existsSync(asset)) broken.add(`${file}: ${relative}`);
  }
}
assert.equal(
  broken.size,
  0,
  `Broken internal links:\n${[...broken].join('\n')}`,
);
for (const entry of index) {
  const slug = entry.slug;
  const tool = JSON.parse(read(`api/tools/${slug}.json`));
  assert(
    tools.some((t) => JSON.stringify(t) === JSON.stringify(tool)),
    `Export differs from source: ${slug}`,
  );
  assert(read(`rmm_tools/${slug}/index.html`).includes(`/tools/${slug}/`));
  assert(!read(`tools/${slug}/index.html`).includes('certificate_der_base64'));
}
if (process.env.PUBLIC_ENABLE_ANALYTICS === 'true') {
  const snippet = [
    ...read('index.html').matchAll(/<script[^>]*>([\s\S]*?)<\/script>/g),
  ].find(([, body]) => body.includes("gtag('config'"))?.[1];
  assert(snippet, 'Analytics configuration script missing');
  for (const hostname of [
    'lolrmm.io',
    'www.lolrmm.io',
    'localhost',
    '127.0.0.1',
  ]) {
    const context = { location: { hostname } };
    context.window = context;
    vm.runInNewContext(snippet, context);
    assert.equal(
      context.dataLayer?.filter(
        (args) => args[0] === 'config' && args[1] === 'G-D04FRZLYM5',
      ).length || 0,
      hostname.endsWith('lolrmm.io') ? 1 : 0,
    );
  }
}
console.log(
  `Verified ${pages.length} pages, ${tools.length} tool exports and legacy redirects, internal links, and analytics configuration.`,
);
