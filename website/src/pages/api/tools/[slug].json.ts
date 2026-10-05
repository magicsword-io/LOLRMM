import { tools, rawTool, type CatalogTool } from '../../../lib/catalog';
import type { APIRoute } from 'astro';
export function getStaticPaths() {
  return tools.map((tool) => ({
    params: { slug: tool.slug },
    props: { tool },
  }));
}
export const GET: APIRoute = ({ props }) =>
  new Response(JSON.stringify(rawTool(props.tool as CatalogTool), null, 2), {
    headers: { 'Content-Type': 'application/json' },
  });
