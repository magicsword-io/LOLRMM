import { geometry, monthLabel, type GrowthPoint } from '../lib/growth';
const root = document.querySelector<HTMLElement>('[data-growth]');
if (root) {
  const all: GrowthPoint[] = JSON.parse(root.dataset.points || '[]');
  const svg = root.querySelector<SVGSVGElement>('[data-chart]');
  const scrubber = root.querySelector<HTMLInputElement>(
    '[data-growth-scrubber]',
  );
  let points = all.slice(-36);
  let plot = geometry(points).plotted;
  function select(index: number) {
    const point = plot[Math.max(0, Math.min(index, plot.length - 1))];
    if (!point || !scrubber) return;
    root!.querySelector('[data-dot]')?.setAttribute('cx', String(point.x));
    root!.querySelector('[data-dot]')?.setAttribute('cy', String(point.y));
    for (const attr of ['x1', 'x2'])
      root!.querySelector('[data-guide]')?.setAttribute(attr, String(point.x));
    const label = `${monthLabel(point.month)} · ${point.total} entries`;
    root!.querySelector('[data-growth-readout]')!.textContent = label;
    scrubber.value = String(index);
    scrubber.setAttribute('aria-valuetext', label);
  }
  function range(months: number) {
    points = months ? all.slice(-months) : all;
    const g = geometry(points);
    plot = g.plotted;
    root!.querySelector('[data-line]')?.setAttribute('d', g.path);
    root!.querySelector('[data-area]')?.setAttribute('d', g.area);
    const ns = 'http://www.w3.org/2000/svg';
    const ticks = root!.querySelector('[data-ticks]')!;
    ticks.replaceChildren(
      ...[0, Math.floor((plot.length - 1) / 2), plot.length - 1]
        .filter((v, i, a) => a.indexOf(v) === i)
        .map((i, n) => {
          const t = document.createElementNS(ns, 'text');
          t.textContent = monthLabel(plot[i].month);
          Object.entries({
            x: plot[i].x,
            y: 197,
            class: 'chart-date',
            'text-anchor':
              n === 0 ? 'start' : i === plot.length - 1 ? 'end' : 'middle',
          }).forEach(([k, v]) => t.setAttribute(k, String(v)));
          return t;
        }),
    );
    scrubber!.max = String(plot.length - 1);
    select(plot.length - 1);
  }
  if (svg && scrubber && all.length) {
    scrubber.hidden = false;
    root.querySelector<HTMLElement>('[data-growth-ranges]')!.hidden = false;
    root
      .querySelectorAll<HTMLButtonElement>('[data-months]')
      .forEach((button) =>
        button.addEventListener('click', () => {
          root
            .querySelectorAll('[data-months]')
            .forEach((b) =>
              b.setAttribute('aria-pressed', String(b === button)),
            );
          range(Number(button.dataset.months));
        }),
      );
    scrubber.addEventListener('input', () => select(Number(scrubber.value)));
    svg.addEventListener('pointermove', (event) => {
      if (event.pointerType === 'touch' && event.buttons === 0) return;
      const rect = svg.getBoundingClientRect();
      const x = ((event.clientX - rect.left) / rect.width) * 690;
      select(
        Math.max(
          0,
          Math.min(
            plot.length - 1,
            Math.round(((x - 38) / 622) * (plot.length - 1)),
          ),
        ),
      );
    });
    svg.addEventListener('pointerleave', () => select(plot.length - 1));
  }
}
