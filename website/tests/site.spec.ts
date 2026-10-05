import { test, expect } from '@playwright/test';
import { catalogGrowth } from '../src/lib/growth';
import fs from 'node:fs';
const snapshot: { Category: string }[] = JSON.parse(
  fs.readFileSync(
    new URL('../public/api/rmm_tools.json', import.meta.url),
    'utf8',
  ),
);
const total = snapshot.length;
const rats = snapshot.filter((tool) => tool.Category === 'RAT').length;

test('growth uses valid creation dates, fills missing months, and excludes future entries', () => {
  const result = catalogGrowth(
    [
      { Created: '2024-01-01' },
      { Created: '2024-03-02' },
      { Created: '2024-02-30' },
      { Created: 'invalid' },
      { Created: '2025-01-01' },
    ],
    '2024-04-01',
  );
  expect(result).toEqual({
    points: [
      { month: '2024-01', added: 1, total: 1 },
      { month: '2024-02', added: 0, total: 1 },
      { month: '2024-03', added: 1, total: 2 },
      { month: '2024-04', added: 0, total: 2 },
    ],
    undated: 2,
    future: 1,
  });
  expect(catalogGrowth([], '2024-04-01').points).toEqual([]);
});

test('search, filters, pagination, and shareable URLs', async ({ page }) => {
  await page.goto('/?utm_source=regression&gclid=test-click');
  await expect(page.locator('#result-count')).toContainText(`of ${total}`);
  await expect(page.locator('[data-tool-row]')).toHaveCount(15);
  const first = await page.locator('.tool-name').first().textContent();
  await page.getByRole('button', { name: 'Next page', exact: true }).click();
  await expect(page.locator('.tool-name').first()).not.toHaveText(first!);
  await page.getByRole('searchbox').fill('anydesk.exe');
  await expect(page.locator('.tool-name')).toContainText(['AnyDesk']);
  await expect(page).toHaveURL(/q=anydesk/);
  await expect(page).toHaveURL(/utm_source=regression/);
  await expect(page).toHaveURL(/gclid=test-click/);
  await page.reload();
  await expect(page.getByRole('searchbox')).toHaveValue('anydesk.exe');
  await expect(page.locator('.tool-name')).toContainText(['AnyDesk']);
  await page.getByRole('searchbox').fill('this-does-not-exist-123xyz');
  await expect(
    page.getByRole('heading', { name: 'No matching tools' }),
  ).toBeVisible();
  await page.getByRole('button', { name: 'Reset search and filters' }).click();
  await page.locator('[name="category"][value="RAT"]').check();
  await expect(page.locator('#result-count')).toContainText(
    `${rats} of ${total}`,
  );
  await expect(page.locator('#tool-rows .badge').first()).toHaveText('RAT');
  await page.getByRole('button', { name: 'Reset filters' }).click();
  await page.locator('[data-filter-select="platform"] summary').click();
  await page.getByRole('radio', { name: 'macOS', exact: true }).check();
  await expect(
    page.locator('[data-filter-select="platform"] summary'),
  ).toContainText('macOS');
  await expect(
    page
      .locator(
        '#tool-rows td:nth-child(3) .platform img[src="/platforms/macos.svg"]',
      )
      .first(),
  ).toBeVisible();
  await page.locator('[data-filter-select="privileges"] summary').click();
  await page.keyboard.press('ArrowDown');
  await page.keyboard.press('Escape');
  await expect(
    page.locator('[data-filter-select="privileges"]'),
  ).not.toHaveAttribute('open');
  await expect(page.locator('#tool-rows .platforms').first()).toContainText(
    'macOS',
  );
  await page.getByRole('button', { name: 'Reset filters' }).click();
  await page.getByRole('searchbox').fill('relay-');
  await expect(page.locator('#result-count')).not.toHaveText(
    `0 of ${total} tools`,
  );
});

test('chart ranges and keyboard scrubber expose real monthly values', async ({
  page,
}) => {
  await page.goto('/');
  const slider = page.getByRole('slider', {
    name: 'Explore monthly catalog totals',
  });
  await expect(slider).toBeVisible();
  const latest = await slider.getAttribute('aria-valuetext');
  await slider.focus();
  await page.keyboard.press('ArrowLeft');
  await expect(slider).not.toHaveAttribute('aria-valuetext', latest!);
  await page.getByRole('button', { name: 'All', exact: true }).click();
  await expect(page.locator('[data-ticks]')).toContainText('Sep 2011');
  await page.getByRole('button', { name: '1Y', exact: true }).click();
  await expect(slider).toHaveAttribute('max', '11');
});

test('duplicate-name records remain independently accessible', async ({
  page,
}) => {
  await page.goto('/?q=SimpleHelp');
  const links = page
    .locator('#tool-rows')
    .getByRole('link', { name: 'SimpleHelp', exact: true });
  await expect(links).toHaveCount(2);
  const urls = await links.evaluateAll((elements) =>
    elements.map((element) => element.getAttribute('href')),
  );
  expect(new Set(urls).size).toBe(2);
  for (const url of urls) {
    await page.goto(url!);
    await expect(
      page.getByRole('heading', { name: 'SimpleHelp', exact: true }),
    ).toBeVisible();
    await expect(page.locator('.related-entries a')).toHaveCount(1);
    await expect(
      page.getByRole('link', { name: 'View source YAML' }),
    ).toHaveAttribute('href', /\/yaml\//);
  }
});

test('detail evidence, existing exports, query copy, and old URL work', async ({
  page,
  context,
}) => {
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);
  await page.goto('/tools/anydesk/');
  await expect(
    page.getByRole('heading', { name: 'AnyDesk', exact: true }),
  ).toBeVisible();
  await expect(page.locator('#code-signing')).toContainText(
    'AnyDesk Software GmbH',
  );
  await expect(page.locator('#artifacts-network')).toContainText(
    'boot.net.anydesk.com',
  );
  await expect(page.locator('#details')).toContainText('macOS');
  const api = await page.request.get('/api/tools/anydesk.json');
  expect((await api.json()).Name).toBe('AnyDesk');
  for (const path of [
    '/api/rmm_tools.csv',
    '/api/rmm_domains.csv',
    '/api/rmm_certificates.json',
    '/api/detections/sigma/generic_rmm_detection.yml',
  ])
    expect((await page.request.get(path)).ok()).toBeTruthy();
  await page.goto('/rmm_tools/anydesk/');
  await expect(page).toHaveURL(/\/tools\/anydesk\/$/);
  await page.goto('/detections/');
  await page
    .getByRole('button', { name: 'Copy Microsoft Defender query' })
    .click();
  expect(await page.evaluate(() => navigator.clipboard.readText())).toContain(
    'DeviceNetworkEvents',
  );
});

test('desktop and mobile themes have no page overflow or script errors', async ({
  page,
}) => {
  const errors: string[] = [];
  page.on('pageerror', (error) => errors.push(error.message));
  for (const width of [1440, 390, 320]) {
    await page.setViewportSize({ width, height: 900 });
    for (const route of [
      '/',
      '/tools/anydesk/',
      '/tools/rustdesk/',
      '/api/',
      '/about/',
      '/detections/',
    ]) {
      await page.goto(route);
      await expect(page.locator('h1')).toBeVisible();
      expect(
        await page.evaluate(
          () => document.documentElement.scrollWidth <= innerWidth,
        ),
        `${route} at ${width}px`,
      ).toBeTruthy();
    }
  }
  await page.goto('/');
  await page.getByRole('button', { name: 'Switch to light theme' }).click();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
  await page.reload();
  await expect(page.locator('html')).toHaveAttribute('data-theme', 'light');
  expect(errors).toEqual([]);
});

test('catalog, growth, and detail evidence remain readable without JavaScript', async ({
  browser,
}) => {
  const context = await browser.newContext({ javaScriptEnabled: false });
  const page = await context.newPage();
  await page.goto('http://127.0.0.1:4321/');
  await expect(page.locator('[data-tool-row]')).toHaveCount(total);
  await expect(
    page.getByRole('img', {
      name: 'LOLRMM catalog growth',
    }),
  ).toBeVisible();
  await page.goto('http://127.0.0.1:4321/tools/anydesk/');
  await expect(page.locator('#artifacts-network')).toContainText(
    'boot.net.anydesk.com',
  );
  await context.close();
});
