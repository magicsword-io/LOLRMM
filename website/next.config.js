const withNextra = require("nextra")({
	theme: "nextra-theme-docs",
	themeConfig: "./theme.config.tsx",
	defaultShowCopyCode: true,
	flexsearch: {
		codeblocks: false,
	},
});

module.exports = withNextra({
	reactStrictMode: true,
	output: "export",
	images: {
		unoptimized: true,
	},
	experimental: { optimisticClientCache: false }
});
