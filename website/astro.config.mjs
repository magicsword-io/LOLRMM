import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lolrmm.io',
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/tools/levelio/': '/tools/level/',
    '/rmm_tools/levelio/': '/tools/level/',
    '/tools/levelio--levelio/': '/tools/level/',
    '/rmm_tools/levelio--levelio/': '/tools/level/',
    '/tools/itsupport247-connectwise--itsupport247connectwise/':
      '/tools/itsupport247-connectwise/',
    '/rmm_tools/itsupport247-connectwise--itsupport247connectwise/':
      '/tools/itsupport247-connectwise/',
    '/tools/quickassist/': '/tools/quick-assist/',
    '/tools/microsoft_quick_assist/': '/tools/microsoft-quick-assist/',
  },
  devToolbar: { enabled: false },
});
