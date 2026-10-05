// Native disclosure + radio controls retain Tab, arrow-key, and screen-reader support.
export function initFilterSelects() {
  const menus = [
    ...document.querySelectorAll<HTMLDetailsElement>('[data-filter-select]'),
  ];
  const updates = menus.map((menu) => {
    const select = document.getElementById(
      menu.dataset.filterSelect!,
    ) as HTMLSelectElement;
    const summary = menu.querySelector('summary')!;
    const radios = [...menu.querySelectorAll<HTMLInputElement>('input')];
    const sync = () => {
      const label = select.selectedOptions[0]?.textContent || '';
      menu.querySelector('[data-selected-label]')!.textContent = label;
      summary.title = label;
      menu.classList.toggle('has-selection', Boolean(select.value));
      radios.forEach((radio) => {
        radio.checked = radio.value === select.value;
      });
    };
    const close = () => {
      menu.open = false;
      summary.focus();
    };
    radios.forEach((radio) => {
      radio.addEventListener('change', () => {
        select.value = radio.value;
        sync();
        select.dispatchEvent(new Event('change', { bubbles: true }));
      });
      radio.addEventListener('click', close);
    });
    menu.addEventListener('keydown', (event) => {
      if (
        event.key === 'Escape' ||
        (event.key === 'Enter' && event.target instanceof HTMLInputElement)
      ) {
        event.preventDefault();
        close();
      }
    });
    menu.addEventListener('toggle', () => {
      if (menu.open) {
        menus
          .filter((other) => other !== menu)
          .forEach((other) => {
            other.open = false;
          });
        radios.find((radio) => radio.checked)?.focus({ preventScroll: true });
      }
    });
    sync();
    return sync;
  });
  document.addEventListener('click', (event) => {
    menus.forEach((menu) => {
      if (!menu.contains(event.target as Node)) menu.open = false;
    });
  });
  return () => updates.forEach((sync) => sync());
}
