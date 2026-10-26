import type { CatalogTool } from './catalog';

// Per-tool snippet overrides for pages that rank but get few clicks
// (Search Console, Sep 27 – Oct 25 2026). Keyed by tool slug.
export const seoOverrides: Record<string, { title?: string; description?: string }> = {
  'mouse-without-borders': {
    title: 'Mouse Without Borders: Security Risks & IOCs | LOLRMM',
    description:
      'Mouse Without Borders (Microsoft Garage, in PowerToys) shares a keyboard, mouse and clipboard across PCs. See its executables, network IOCs and detections.',
  },
  pitunnel: {
    title: 'PiTunnel: Remote Shell & Tunnel Risks, IOCs | LOLRMM',
    description:
      'PiTunnel exposes a remote shell and TCP tunnels from Raspberry Pi and Linux hosts via *.pitunnel.com. See install commands, network IOCs and detections.',
  },
  'itsupport247-connectwise': {
    title: 'ITSupport247 (ConnectWise) RMM: IOCs & Detection | LOLRMM',
    description:
      'ITSupport247 is a ConnectWise RMM agent (control.itsupport247.net, saazapsc.exe). See its file paths, domains and detections for unauthorized access.',
  },
};

const SITE = ' | LOLRMM';
const TITLE_MAX = 60;
const DESC_MAX = 155;

const categoryLabel = (category?: string) =>
  category === 'RMM'
    ? 'remote monitoring and management (RMM) tool'
    : 'remote access tool';

export function toolTitle(tool: CatalogTool): string {
  const override = seoOverrides[tool.slug]?.title;
  if (override) return override;
  for (const suffix of [': Security Risks, IOCs & Detection', ': Risks, IOCs & Detection', '']) {
    const title = tool.Name + suffix + SITE;
    if (title.length <= TITLE_MAX) return title;
  }
  return tool.Name.slice(0, TITLE_MAX - SITE.length - 1) + '…' + SITE;
}

export function toolDescription(tool: CatalogTool): string {
  const override = seoOverrides[tool.slug]?.description;
  if (override) return override;
  const lead = `${tool.Name} is a ${categoryLabel(tool.Category)} attackers can abuse.`;
  for (const tail of [
    ' See its executables, domains, file paths and detection rules to spot unauthorized use.',
    ' See its executables, domains and detections.',
    '',
  ]) {
    if ((lead + tail).length <= DESC_MAX) return lead + tail;
  }
  return lead.slice(0, DESC_MAX - 1) + '…';
}
