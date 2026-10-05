import { tools, toolUrl } from '../lib/catalog';
export const GET = () =>
  new Response(
    `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${['/', '/about/', '/api/', '/detections/', ...tools.map(toolUrl)].map((path) => `<url><loc>https://lolrmm.io${path}</loc></url>`).join('')}</urlset>`,
    { headers: { 'Content-Type': 'application/xml' } },
  );
