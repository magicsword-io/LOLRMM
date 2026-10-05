export interface GrowthPoint {
  month: string;
  added: number;
  total: number;
}
export function catalogGrowth(
  entries: { Created: string }[],
  end = new Date().toISOString().slice(0, 10),
) {
  const counts = new Map<string, number>();
  let undated = 0;
  let future = 0;
  for (const { Created: date } of entries) {
    const timestamp = Date.parse(date);
    if (
      !/^\d{4}-\d{2}-\d{2}$/.test(date) ||
      !Number.isFinite(timestamp) ||
      new Date(timestamp).toISOString().slice(0, 10) !== date
    ) {
      undated++;
      continue;
    }
    if (date > end) {
      future++;
      continue;
    }
    const month = date.slice(0, 7);
    counts.set(month, (counts.get(month) || 0) + 1);
  }
  const months = [...counts.keys()].sort();
  const points: GrowthPoint[] = [];
  if (!months.length) return { points, undated, future };
  const cursor = new Date(`${months[0]}-01T00:00:00Z`);
  let total = 0;
  while (cursor.toISOString().slice(0, 7) <= end.slice(0, 7)) {
    const month = cursor.toISOString().slice(0, 7);
    const added = counts.get(month) || 0;
    total += added;
    points.push({ month, added, total });
    cursor.setUTCMonth(cursor.getUTCMonth() + 1);
  }
  return { points, undated, future };
}
export const monthLabel = (month: string) =>
  new Intl.DateTimeFormat('en-US', {
    month: 'short',
    year: 'numeric',
    timeZone: 'UTC',
  }).format(new Date(`${month}-01T00:00:00Z`));
export function geometry(points: GrowthPoint[]) {
  const left = 38,
    right = 660,
    top = 15,
    bottom = 164;
  const max = Math.max(1, ...points.map((p) => p.total));
  const ceiling = Math.ceil(max / 50) * 50;
  const plotted = points.map((p, i) => ({
    ...p,
    x: left + (i / Math.max(1, points.length - 1)) * (right - left),
    y: bottom - (p.total / ceiling) * (bottom - top),
  }));
  const path = plotted
    .map((p, i) => (i === 0 ? `M${p.x},${p.y}` : `H${p.x}V${p.y}`))
    .join('');
  return {
    plotted,
    path,
    area: plotted.length
      ? `${path}L${plotted.at(-1)!.x},${bottom}H${left}Z`
      : '',
    ceiling,
    left,
    right,
    top,
    bottom,
  };
}
