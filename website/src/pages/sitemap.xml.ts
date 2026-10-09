import { tools, toolUrl } from '../lib/catalog';

export const GET = () => {
  // Static pages with high priority
  const staticPages = [
    { loc: '/', priority: '1.0', changefreq: 'daily' },
    { loc: '/about/', priority: '0.8', changefreq: 'monthly' },
    { loc: '/api/', priority: '0.9', changefreq: 'weekly' },
    { loc: '/detections/', priority: '0.9', changefreq: 'weekly' },
  ];
  
  // Tool pages with lastmod from catalog
  const toolPages = tools.map((tool) => ({
    loc: toolUrl(tool),
    lastmod: tool.LastModified,
    priority: '0.7',
    changefreq: 'weekly',
  }));
  
  const allPages = [...staticPages, ...toolPages];
  
  const urlEntries = allPages.map((page) => {
    const lastmod = 'lastmod' in page ? `<lastmod>${page.lastmod}</lastmod>` : '';
    return `<url><loc>https://lolrmm.io${page.loc}</loc>${lastmod}<changefreq>${page.changefreq}</changefreq><priority>${page.priority}</priority></url>`;
  }).join('');
  
  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${urlEntries}</urlset>`,
    { headers: { 'Content-Type': 'application/xml' } },
  );
};
