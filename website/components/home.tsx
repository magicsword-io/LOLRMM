import {
	EuiFlexGroup,
	EuiLink,
	EuiPageTemplate,
	EuiSpacer,
	EuiTitle,
	EuiToast,
	EuiImage,
} from "@elastic/eui";
import "@elastic/eui/dist/eui_theme_dark.css";
import { RMMTable } from "./tools";

function Contents() {
	return (
		<>
			<EuiSpacer size="xxl" />
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
							, or suggest new RMM tools to be added. You can also access the RMM tools list via API using{" "}
							<EuiLink href="/api/rmm_tools.csv">CSV</EuiLink> or{" "}
							<EuiLink href="/api/rmm_tools.json">JSON</EuiLink>. For users of
							security monitoring tools, check out the pre-built{" "}
							<EuiLink href="https://github.com/magicsword-io/lolrmm/blob/main/detections/sigma">
									<EuiImage
										alt="Sigma Logo"
										src="/images/sigma_logo.png"
										style={{ width: '20px', height: '20px', marginRight: '5px', verticalAlign: 'middle' }}
									/>
									Sigma rules
							</EuiLink>
						</>
					}
					color="primary"
					iconType="iInCircle"
				/>
				<EuiToast
					title={
						<>
							Interested in learning how to <span style={{ color: 'red' }}>block</span> these remote management tools natively on Windows?
							<br />
							<EuiLink href="https://www.magicsword.io/premium">
								<EuiImage
									alt="MagicSword Logo"
									src="/images/magicsword.png"
									style={{ width: '110px', height: '110px', verticalAlign: 'middle', display: 'inline-block', marginRight: '10px', marginTop: '10px' }}
								/>
								Explore MagicSword Premium
							</EuiLink>
						</>
					}
					color="warning"
					iconType="lock"
					/>
			</EuiFlexGroup>
			<EuiSpacer size="xxl" />

			<EuiTitle size="m">
				<h4>RMM Tools</h4>
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
				description={
					<>
						<img src="/images/logo.png" alt="LOLRMM Logo" style={{ width: '200px', display: 'block' }} />
						<p>
							LOLRMM is a curated list of Remote Monitoring and Management (RMM) tools that could potentially be abused by threat actors. Inspired by the original <EuiLink href="https://lolbas-project.github.io/">LOLBAS project</EuiLink> for tracking binaries and closely associated with <EuiLink href="https://loldrivers.io">LOLDrivers</EuiLink> for malicious drivers, this project aims to assist security professionals in staying informed about these tools and their potential for misuse. For a collection of similar "Living Off The Land" projects, visit <EuiLink href="https://lolol.farm/">lolol.farm</EuiLink>.
						</p>
					</>
				}
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
