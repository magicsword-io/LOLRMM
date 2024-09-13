import { Analytics } from "@vercel/analytics/react";
import { useRouter } from "next/router";
// @ts-ignore
import { type DocsThemeConfig, useConfig } from "nextra-theme-docs";
import { Logo } from "./components/logo";

const config: DocsThemeConfig = {
	darkMode: false,
	nextThemes: {
		defaultTheme: "dark",
	},
	logo: <Logo />,
	project: {
		link: "https://github.com/magicsword-io/LOLRMM",
	},
	toc: {
		float: true,
		backToTop: true,
	},
	docsRepositoryBase:
		"https://github.com/magicsword-io/LOLRMM/tree/main/website/",
	footer: {
		component: (
			<>
				<Analytics />
				{/* <script
					defer
					src={"https://static.cloudflareinsights.com/beacon.min.js"}
					data-cf-beacon={'{"token": "b59027d62dea4505885f06f6338003d2"}'}
				/> */}
			</>
		),
	},
	useNextSeoProps() {
		return {
			titleTemplate: "LOLRMM - %s",
		};
	},
	head: () => {
		const { frontMatter } = useConfig();
		const { asPath } = useRouter();
		const basePath = "https://lolrmm.com";
		const url = basePath + asPath;
		const ogImage = `${basePath}/og.png`;
		const title = frontMatter.title || "Docs";
		return (
			<>
				<meta name="viewport" content="width=device-width, initial-scale=1.0" />
				<meta property="og:url" content={url} />
				<meta property="og:image" content={ogImage} />
				<meta property="og:image:alt" content="LOLRMM" />
				<meta property="og:title" content={title} />
				<meta
					property="og:description"
					content={frontMatter.description || "LOLRMM site"}
				/>
			</>
		);
	},
};

// biome-ignore lint/style/noDefaultExport: This is a config file
export default config;
