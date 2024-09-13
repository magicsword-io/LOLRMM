import Document, { Html, Head, Main, NextScript } from "next/document";
import { SkipNavLink } from "nextra-theme-docs";

class MyDocument extends Document {
	render() {
		return (
			<Html lang="en">
				<Head>
					<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png" />
					<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png" />
					<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png" />
					<link rel="manifest" href="/site.webmanifest" />
					<link rel="mask-icon" href="/safari-pinned-tab.svg" color="#5bbad5" />
					<meta name="msapplication-TileColor" content="#00a300" />
					<meta name="theme-color" content="#ffffff" />
				</Head>
				<body>
					<SkipNavLink styled={true} />
					<Main />
					<NextScript />
				</body>
			</Html>
		);
	}
}

// biome-ignore lint/style/noDefaultExport: This is a global file
export default MyDocument;
