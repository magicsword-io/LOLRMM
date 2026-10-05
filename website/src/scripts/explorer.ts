import { initFilterSelects } from './filter-select';
interface Entry {
  name: string;
  slug: string;
  category: string;
  created: string;
  modified: string;
  author: string;
  platforms: string[];
  privileges: string;
  free: boolean | string;
  detections: boolean;
  search: string;
}
const input = document.querySelector<HTMLInputElement>('#catalog-search');
const body = document.querySelector<HTMLTableSectionElement>('#tool-rows');
if (input && body) {
  const rows = new Map(
    [...body.querySelectorAll<HTMLTableRowElement>('[data-tool-row]')].map(
      (row) => [row.dataset.slug!, row],
    ),
  );
  const controls = {
    platform: document.querySelector<HTMLSelectElement>('#platform')!,
    availability: document.querySelector<HTMLSelectElement>('#availability')!,
    privileges: document.querySelector<HTMLSelectElement>('#privileges')!,
    detections: document.querySelector<HTMLInputElement>('#has-detections')!,
    sort: document.querySelector<HTMLSelectElement>('#sort')!,
  };
  const syncFilters = initFilterSelects();
  let entries: Entry[] = [],
    page = 1;
  const size = 15;
  const previous = document.querySelector<HTMLButtonElement>('#previous-page')!;
  const next = document.querySelector<HTMLButtonElement>('#next-page')!;
  function availability(value: boolean | string) {
    const text = String(value).toLowerCase();
    if (value === true || /^(yes|free|open source)/.test(text)) return 'free';
    if (/trial/.test(text)) return 'trial';
    if (value === false || /^(no|paid)/.test(text)) return 'paid';
    return 'unknown';
  }
  function stateToURL() {
    // Keep campaign attribution (utm_*, gclid, etc.) when updating filter state.
    const params = new URLSearchParams(location.search);
    for (const key of [
      'q',
      'category',
      'platform',
      'availability',
      'privileges',
      'detections',
      'sort',
      'page',
    ])
      params.delete(key);
    if (input!.value) params.set('q', input!.value);
    const category = document.querySelector<HTMLInputElement>(
      '[name="category"]:checked',
    )!.value;
    if (category) params.set('category', category);
    for (const key of ['platform', 'availability', 'privileges'] as const)
      if (controls[key].value) params.set(key, controls[key].value);
    if (controls.detections.checked) params.set('detections', '1');
    if (controls.sort.value !== 'newest')
      params.set('sort', controls.sort.value);
    if (page > 1) params.set('page', String(page));
    const query = params.toString();
    history.replaceState(
      null,
      '',
      location.pathname + (query ? `?${query}` : '') + location.hash,
    );
  }
  function render() {
    const terms = input!.value
      .trim()
      .toLowerCase()
      .split(/\s+/)
      .filter(Boolean);
    const category = document.querySelector<HTMLInputElement>(
      '[name="category"]:checked',
    )!.value;
    const matched = entries.filter(
      (t) =>
        terms.every((term) => t.search.includes(term)) &&
        (!category || t.category === category) &&
        (!controls.platform.value ||
          t.platforms.includes(controls.platform.value)) &&
        (!controls.availability.value ||
          availability(t.free) === controls.availability.value) &&
        (!controls.privileges.value ||
          t.privileges === controls.privileges.value) &&
        (!controls.detections.checked || t.detections),
    );
    const sort = controls.sort.value;
    matched.sort(
      (a, b) =>
        (sort === 'name'
          ? a.name.localeCompare(b.name)
          : sort === 'category'
            ? a.category.localeCompare(b.category)
            : sort === 'author'
              ? a.author.localeCompare(b.author)
              : sort === 'updated'
                ? b.modified.localeCompare(a.modified)
                : b.created.localeCompare(a.created)) ||
        a.name.localeCompare(b.name),
    );
    const pages = Math.max(1, Math.ceil(matched.length / size));
    page = Math.max(1, Math.min(page, pages));
    const start = (page - 1) * size;
    body!.replaceChildren(
      ...matched.slice(start, start + size).map((t) => rows.get(t.slug)!),
    );
    document.querySelector('#result-count')!.textContent =
      `${matched.length} of ${entries.length} tools`;
    document.querySelector<HTMLElement>('#no-results')!.hidden =
      matched.length > 0;
    document.querySelector<HTMLElement>('.catalog-table')!.hidden =
      !matched.length;
    document.querySelector('#page-summary')!.textContent = matched.length
      ? `${start + 1}–${Math.min(start + size, matched.length)} of ${matched.length}`
      : '0 results';
    document.querySelector('#page-number')!.textContent = `${page} / ${pages}`;
    previous.disabled = page === 1;
    next.disabled = page === pages;
    syncFilters();
    stateToURL();
  }
  function reset() {
    input!.value = '';
    document.querySelector<HTMLInputElement>(
      '[name="category"][value=""]',
    )!.checked = true;
    for (const key of ['platform', 'availability', 'privileges'] as const)
      controls[key].value = '';
    controls.detections.checked = false;
    controls.sort.value = 'newest';
    page = 1;
    render();
  }
  fetch('/data/search.json')
    .then((response) => {
      if (!response.ok) throw new Error('Search index unavailable');
      return response.json();
    })
    .then((data: Entry[]) => {
      entries = data;
      const params = new URLSearchParams(location.search);
      input.value = params.get('q') || '';
      document
        .querySelectorAll<HTMLInputElement>('[name="category"]')
        .forEach(
          (radio) =>
            (radio.checked =
              radio.value ===
              (['RMM', 'RAT'].includes(params.get('category') || '')
                ? params.get('category')
                : '')),
        );
      for (const key of [
        'platform',
        'availability',
        'privileges',
        'sort',
      ] as const) {
        const value = params.get(key);
        if (value && [...controls[key].options].some((o) => o.value === value))
          controls[key].value = value;
      }
      controls.detections.checked = params.get('detections') === '1';
      page = Math.max(1, Number.parseInt(params.get('page') || '1') || 1);
      render();
      document
        .querySelectorAll<HTMLElement>(
          '[data-filters], [data-sort-label], .pagination',
        )
        .forEach((e) => (e.hidden = false));
      let timer: ReturnType<typeof setTimeout>;
      input.addEventListener('input', () => {
        clearTimeout(timer);
        timer = setTimeout(() => {
          page = 1;
          render();
        }, 100);
      });
      document
        .querySelectorAll(
          '[name=category], [data-filters] select, #has-detections, #sort',
        )
        .forEach((control) =>
          control.addEventListener('change', () => {
            page = 1;
            render();
          }),
        );
      for (const id of ['reset-filters', 'empty-reset'])
        document.getElementById(id)?.addEventListener('click', reset);
      previous.addEventListener('click', () => {
        page--;
        render();
      });
      next.addEventListener('click', () => {
        page++;
        render();
      });
    })
    .catch(() => {
      document.querySelector('#result-count')!.textContent =
        'Search is unavailable. All tools are shown; use your browser’s Find command.';
      input.disabled = true;
    });
  document.addEventListener('keydown', (event) => {
    if (
      event.key === '/' &&
      !(
        event.target instanceof HTMLElement &&
        (event.target.matches('input,textarea,select') ||
          event.target.isContentEditable)
      )
    ) {
      event.preventDefault();
      input.focus();
    }
  });
}
