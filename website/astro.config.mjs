import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://lolrmm.io',
  output: 'static',
  trailingSlash: 'always',
  redirects: {
    '/tools/quickassist/': '/tools/quick-assist/',
    '/tools/microsoft_quick_assist/': '/tools/quick-assist/',
    '/tools/microsoft-quick-assist/': '/tools/quick-assist/',
    '/rmm_tools/microsoft-quick-assist/': '/tools/quick-assist/',
    '/tools/itsupport247-connectwise--itsupport247connectwise/':
      '/tools/itsupport247-connectwise/',
    '/rmm_tools/itsupport247-connectwise--itsupport247connectwise/':
      '/tools/itsupport247-connectwise/',
  },
  devToolbar: { enabled: false },
});
