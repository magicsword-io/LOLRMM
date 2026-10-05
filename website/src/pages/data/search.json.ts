import { tools, platforms } from '../../lib/catalog';
import type { APIRoute } from 'astro';
// Exclude certificate DER from the search index; retain human-readable evidence.
export const GET: APIRoute = () =>
  new Response(
    JSON.stringify(
      tools.map((t) => ({
        name: t.Name,
        slug: t.slug,
        sourceFile: t.sourceFile,
        category: t.Category,
        created: t.Created,
        modified: t.LastModified,
        author: t.Author || '',
        platforms: platforms(t),
        privileges: t.Details.Privileges || 'unknown',
        free: t.Details.Free ?? '',
        detections: Boolean(
          t.Detections?.some((d) => d.Sigma || d.Link || d.Name),
        ),
        search: JSON.stringify(t, (key, value) =>
          key === 'certificate_der_base64' ? undefined : value,
        ).toLowerCase(),
      })),
    ),
    { headers: { 'Content-Type': 'application/json' } },
  );
