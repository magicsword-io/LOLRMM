import {
	EuiFlexGroup,
	EuiLink,
	EuiPageTemplate,
	EuiSpacer,
	EuiTitle,
	EuiToast,
} from "@elastic/eui";
import "@elastic/eui/dist/eui_theme_dark.css";
import { RMMTable } from "./tools";

function Contents() {
	return (
		<>
			<EuiFlexGroup>
				<EuiToast
					title={
						<>
							Feel free to open a{" "}
							<EuiLink href="https://github.com/magicsword-io/lolrmm/pulls">
								PR
							</EuiLink>
							, raise an{" "}
							<EuiLink href="https://github.com/magicsword-io/lolrmm/issues/new/choose">
								issue
							</EuiLink>
							, or suggest new RMM tools to be added.
						</>
					}
					color="warning"
					iconType="iInCircle"
				/>
				<EuiToast
					title={
						<>
							You can also access the RMM tools list via API using{" "}
							<EuiLink href="/api/rmm_tools.csv">CSV</EuiLink> or{" "}
							<EuiLink href="/api/rmm_tools.json">JSON</EuiLink>. For users of
							security monitoring tools, check out the pre-built{" "}
							<EuiLink href="https://github.com/magicsword-io/lolrmm/blob/main/detections/configs">
								configurations
							</EuiLink>
							. We also provide{" "}
							<EuiLink href="https://github.com/magicsword-io/lolrmm/blob/main/detections/sigma">
								Sigma rules{" "}
							</EuiLink>
							for SIEMs.
						</>
					}
					color="primary"
					iconType="iInCircle"
				/>
			</EuiFlexGroup>
			<EuiSpacer size="xxl" />

			<EuiTitle size="m">
				<h4>Tools</h4>
			</EuiTitle>

			<EuiSpacer size="xxl" />
			<RMMTable />
		</>
	);
}

export function App() {
	return (
		<EuiPageTemplate
			panelled={null}
			restrictWidth="90%"
			css={{ backgroundColor: "black" }}
		>
			<EuiPageTemplate.Header
				pageTitle="LOLRMM"
				description="LOLRMM is a curated list of Remote Monitoring and Management (RMM) tools that could potentially be abused by threat actors. This project aims to assist security professionals in staying informed about these tools and their potential for misuse."
				iconProps={{
					href: "/images/logo.png",
				}}
			/>

			<EuiPageTemplate.Section color="transparent">
				<Contents />
			</EuiPageTemplate.Section>
		</EuiPageTemplate>
	);
}
