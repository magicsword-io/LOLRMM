import { tools, rawTool, type CatalogTool } from '../../../lib/catalog';
import type { APIRoute } from 'astro';
export function getStaticPaths() {
  return tools.flatMap((tool) => {
    const slugs = [tool.slug];
    // Preserve the JSON export URL of the merged duplicate record.
    if (tool.slug === 'itsupport247-connectwise') {
      slugs.push('itsupport247-connectwise--itsupport247connectwise');
    }
    if (tool.slug === 'level') {
      slugs.push('levelio', 'levelio--levelio');
    }
    return slugs.map((slug) => ({
      params: { slug },
      props: { tool },
    }));
  });
}
export const GET: APIRoute = ({ props }) =>
  new Response(JSON.stringify(rawTool(props.tool as CatalogTool), null, 2), {
    headers: { 'Content-Type': 'application/json' },
  });
