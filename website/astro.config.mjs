import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lolrmm.io',
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/tools/itsupport247-connectwise--itsupport247connectwise/':
      '/tools/itsupport247-connectwise/',
    '/rmm_tools/itsupport247-connectwise--itsupport247connectwise/':
      '/tools/itsupport247-connectwise/',
  },
  devToolbar: { enabled: false },
});
