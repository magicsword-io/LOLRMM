const colors = require("tailwindcss/colors");

module.exports = {
	content: [
		"./components/**/*.{js,tsx}",
		"./nextra-theme-docs/**/*.{js,tsx}",
		"./pages/**/*.{md,mdx,tsx}",
		"./theme.config.js",
	],
	theme: {
		extend: {
			colors: {
				dark: "#000",
				gray: colors.neutral,
				blue: colors.blue,
				orange: colors.orange,
				green: colors.green,
				red: colors.red,
				yellow: colors.yellow,
			},
			screens: {
				sm: "640px",
				md: "768px",
				lg: "1024px",
				betterhover: { raw: "(hover: hover)" },
			},
		},
	},
	darkMode: "class",
};
