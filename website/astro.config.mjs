import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lolrmm.io',
  output: 'static',
  trailingSlash: 'always',
  devToolbar: { enabled: false },
});
