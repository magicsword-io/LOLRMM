import Document, { Html, Head, Main, NextScript } from "next/document";
import { SkipNavLink } from "nextra-theme-docs";

class MyDocument extends Document {
	render() {
		return (
			<Html lang="en">
				<Head />
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
