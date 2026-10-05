import fs from 'node:fs';
import path from 'node:path';
import { parse } from 'yaml';

export type Value =
  string | number | boolean | null | Value[] | { [key: string]: Value };
export interface Tool {
  Name: string;
  Category: string;
  Description: string;
  Author?: string;
  Created: string;
  LastModified: string;
  Details: {
    Website: string;
    PEMetadata?: Record<string, Value>[] | Record<string, Value>;
    Privileges?: string;
    Free?: string | boolean;
    Verification?: string | boolean;
    SupportedOS: string[];
    Capabilities: string[];
    InstallationPaths?: string[] | string;
    Vulnerabilities?: string[];
  };
  Artifacts?: Record<string, Record<string, Value>[]>;
  Detections?: Record<string, Value>[];
  CodeSigning?: Record<string, Value>;
  FileHashes?: Value;
  InstallationPaths?: Value;
  References?: string[];
  Acknowledgement?: Record<string, Value>[];
}

export const slugify = (name: string) =>
  name
    .toLowerCase()
    .replace(/[^a-z0-9\s-]/g, '')
    .replace(/[\s_-]+/g, '-')
    .replace(/^-+|-+$/g, '');
export type CatalogTool = Tool & { slug: string; sourceFile: string };
// Read source files at build time to keep duplicate-name records distinct.
const yamlDir = path.resolve(process.cwd(), '../yaml');
const records = fs
  .readdirSync(yamlDir)
  .filter((file) => /\.ya?ml$/.test(file))
  .sort()
  .map((sourceFile) => ({
    ...(parse(fs.readFileSync(path.join(yamlDir, sourceFile), 'utf8')) as Tool),
    sourceFile,
  }));
const canonical = new Map<string, string>();
for (const record of [...records].sort(
  (a, b) =>
    b.LastModified.localeCompare(a.LastModified) ||
    a.sourceFile.localeCompare(b.sourceFile),
)) {
  const slug = slugify(record.Name);
  if (!canonical.has(slug)) canonical.set(slug, record.sourceFile);
}
export const tools: CatalogTool[] = records.map((record) => {
  const base = slugify(record.Name);
  return {
    ...record,
    slug:
      canonical.get(base) === record.sourceFile
        ? base
        : `${base}--${record.sourceFile.replace(/\.ya?ml$/, '')}`,
  };
});
export const rawTool = ({ slug, sourceFile, ...record }: CatalogTool): Tool =>
  record;
export const toolUrl = (tool: CatalogTool) => `/tools/${tool.slug}/`;
export const repository = 'https://github.com/magicsword-io/LOLRMM';
export const display = (value: unknown): string =>
  value === null || value === undefined || value === ''
    ? 'Not recorded'
    : typeof value === 'boolean'
      ? value
        ? 'Yes'
        : 'No'
      : String(value);
export const platform = (name: string) =>
  ({ mac: 'macOS', macos: 'macOS', ios: 'iOS', windows: 'Windows' })[
    name.toLowerCase()
  ] || name;
export const platforms = (tool: Tool) =>
  [...new Set(tool.Details.SupportedOS.map(platform))].sort();
export function safeUrl(value: unknown) {
  if (typeof value !== 'string') return undefined;
  try {
    const url = new URL(value);
    return ['https:', 'http:'].includes(url.protocol) ? url.href : undefined;
  } catch {
    return undefined;
  }
}
export const newest = [...tools].sort(
  (a, b) => b.Created.localeCompare(a.Created) || a.Name.localeCompare(b.Name),
);
export const stats = {
  tools: tools.length,
  rmm: tools.filter((t) => t.Category === 'RMM').length,
  rat: tools.filter((t) => t.Category === 'RAT').length,
  domains: new Set(
    tools.flatMap((t) =>
      (t.Artifacts?.Network || []).flatMap((a) =>
        Array.isArray(a.Domains) ? a.Domains.map(String) : [],
      ),
    ),
  ).size,
  certificates: tools.filter(
    (t) => (t.CodeSigning?.certificates as Value[] | undefined)?.length,
  ).length,
};

const slugs = tools.map((t) => t.slug);
if (new Set(slugs).size !== slugs.length)
  throw new Error('Duplicate tool slugs: tool URLs would collide.');
