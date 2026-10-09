export const GET = () =>
  new Response(
    `# Allow all crawlers
User-agent: *
Allow: /

# AI/LLM crawlers - allow access to public content
User-agent: ChatGPT-User
User-agent: GPTBot
User-agent: Google-Extended
User-agent: anthropic-ai
User-agent: Claude-Web
User-agent: cohere-ai
User-agent: PerplexityBot
User-agent: Applebot-Extended
User-agent: YouBot
User-agent: Diffbot
User-agent: meta-externalagent
Allow: /

# Disallow redirect paths (already marked noindex)
User-agent: *
Disallow: /rmm_tools/

# Sitemap
Sitemap: https://lolrmm.io/sitemap.xml
`,
  );
