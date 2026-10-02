# LOLRMM.io

A static Astro site using the existing LOLRMM logo and green/cream identity.
The layout follows the companion LOLDrivers site. Tool pages render as HTML;
small TypeScript modules add search, filters, pagination, chart scrubbing, and
persisted dark/light themes. The catalog and evidence remain readable without JS.

## Local development

Use Node.js 22.19+ and Python 3.12+ with PyYAML installed. From the repository root:

```sh
python3 -m venv .venv
source .venv/bin/activate
pip install pyyaml
cd website
npm ci
npm run dev
```

Open http://localhost:4321. `dev` and `build` run `bin/site.py` first to regenerate
catalog exports, domains, and detection files from the source YAML. Poetry users
can instead use `poetry run npm run dev` from this directory after `poetry install`.
Restart the dev server after changing YAML to regenerate exports. Tool pages read
the same YAML files directly at build time, retaining their source filenames.

```sh
npm run check
npm run build
npm run preview
npx playwright install chromium
npm test
```

The build produces `website/dist/`. It verifies all tool pages, per-tool JSON
exports, legacy redirects, internal asset/page links, and analytics configuration.
Playwright covers filtering, search URLs, pagination, chart ranges and keyboard
interaction, query copying, mobile overflow, themes, and JavaScript-free content.

## Data and routes

- `/tools/<slug>/` preserves existing tool URLs; both `/tools/name` and the
  trailing-slash form are served by GitHub Pages.
- `/rmm_tools/<slug>/` redirects legacy CSV links to their tool pages.
- All existing `/api/` JSON, CSV, and Sigma URLs are preserved.
- `/api/tools/<slug>.json` adds an individual tool export.
- `/data/search.json` contains searchable evidence without certificate DER blobs.
- Duplicate names keep the canonical URL for the most recently modified record;
  other records get a stable filename suffix and link to related research.
  All records remain counted in the chart and original API.
- `bin/site.py` generates data only; Astro replaces the generated MDX pages.
- Existing certificate feeds retain their previous publication process.

## Growth charts

The cumulative growth chart counts current RMM and RAT entries by their
recorded `Created` date, filling missing months with zero additions through the
build month. The chart defaults to the latest 36 months; cumulative counts retain
the earlier baseline. 1Y and All views and a keyboard/touch range slider are
available. Invalid and future creation dates are excluded and disclosed.
The current month can be partial. These are catalog metadata dates, including
older imported records, not observations of attacks or historical repository sizes.

## Google Analytics

The original LOLRMM property **G-D04FRZLYM5** is unchanged. Set
`PUBLIC_ENABLE_ANALYTICS=true` for a production build, as the Pages workflow does.
Development and default local builds omit analytics. Even when enabled, the
configuration only sends page views on `lolrmm.io` or `www.lolrmm.io`. Navigation
uses ordinary page loads, so each page gets one configuration call. The build
verification checks the ID, script count, and production/local hostname behavior.

The deployment workflow publishes `dist/` and still commits generated data and
detections. The PR workflow builds the site and runs its browser tests without
publishing it.
