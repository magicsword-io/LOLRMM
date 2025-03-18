import {
	EuiFlexGroup,
	EuiLink,
	EuiPageTemplate,
	EuiSpacer,
	EuiTitle,
	EuiToast,
	EuiImage,
	EuiPanel,
	EuiText,
	EuiCodeBlock,
	EuiAccordion,
	EuiIcon,
	EuiTabs,
	EuiTab,
	EuiBadge,
	EuiButtonEmpty,
	EuiHorizontalRule,
	EuiCallOut
} from "@elastic/eui";
import "@elastic/eui/dist/eui_theme_dark.css";
import { RMMTable } from "./tools";
import { useState, useEffect } from 'react';

// Example RMM executables for fallback
const FALLBACK_EXECUTABLES = [
	'anydesk.exe',
	'teamviewer.exe',
	'splashtop.exe',
	'screenconnect.exe',
	'logmein.exe',
	'connectwise.exe',
	'atera.exe',
	'supremo.exe',
	'bomgar.exe',
	'dwservice.exe',
	'rustdesk.exe',
	'ultraviewer.exe',
	'remotepc.exe',
	'zoho.exe',
	'rdp.exe'
];

// Example RMM domains for fallback
const FALLBACK_DOMAINS = [
	'.anydesk.com',
	'.teamviewer.com',
	'.splashtop.com',
	'.connectwise.com', 
	'.bomgar.com',
	'.logmein.com',
	'.supremo.com',
	'.dwservice.com',
	'.atera.com',
	'.rustdesk.com'
];

function Contents() {
	// Default to 'kql' tab to ensure content is always visible
	const [selectedTabId, setSelectedTabId] = useState('kql');
	const [rmmCount, setRmmCount] = useState<number | null>(null);
	const [isAccordionOpen, setIsAccordionOpen] = useState(false);
	const [debugInfo, setDebugInfo] = useState('');
	const [sigmaRuleData, setSigmaRuleData] = useState<any>({
		date: new Date().toISOString().split('T')[0].replace(/-/g, '/'),
		executables: FALLBACK_EXECUTABLES
	});
	const [domainsRuleData, setDomainsRuleData] = useState<any>({
		date: new Date().toISOString().split('T')[0].replace(/-/g, '/'),
		domains: FALLBACK_DOMAINS
	});
	
	useEffect(() => {
		// Debug info
		try {
			setDebugInfo('EUI version: ' + require('@elastic/eui/package.json').version);
		} catch (e) {
			setDebugInfo('Error getting EUI version: ' + e.message);
		}
		
		// Fetch the RMM tools count from the JSON file
		fetch('/api/rmm_tools_count.json')
			.then(response => response.json())
			.then(data => {
				console.log('RMM tools count loaded:', data);
				setRmmCount(data.count);
			})
			.catch(error => console.error('Error fetching RMM tools count:', error));
			
		// Try to fetch the Sigma rule data - ignore 404 errors
		fetch('/api/detections/sigma/generic_rmm_detection.yml')
			.then(response => {
				if (!response.ok) {
					throw new Error(`Status: ${response.status}`);
				}
				return response.text();
			})
			.then(data => {
				try {
					// Simple YAML parsing to extract executables
					const exeSection = data.split('Image|endswith:')[1].split('condition:')[0];
					const executablesList = exeSection.match(/- .*\.exe/g) || [];
					const cleanExeList = executablesList.map(exe => exe.replace(/^- \\\\/, ''));
					
					setSigmaRuleData({
						date: data.match(/date: (.+)/)?.[1] || new Date().toISOString().split('T')[0].replace(/-/g, '/'),
						executables: cleanExeList.length > 0 ? cleanExeList : FALLBACK_EXECUTABLES
					});
				} catch (e) {
					console.error('Error parsing Sigma rule:', e);
				}
			})
			.catch(error => {
				console.error('Error fetching Sigma rule (using fallback):', error);
			});
			
		// Try to fetch the Domains rule data - ignore 404 errors
		fetch('/api/detections/sigma/rmm_domains_dns_queries.yml')
			.then(response => {
				if (!response.ok) {
					throw new Error(`Status: ${response.status}`);
				}
				return response.text();
			})
			.then(data => {
				try {
					// Simple YAML parsing to extract domains
					const domainsSection = data.split('query|contains:')[1].split('filter:')[0];
					const domainsList = domainsSection.match(/- \..*/g) || [];
					const cleanDomainsList = domainsList.map(domain => domain.replace(/^- /, ''));
					
					setDomainsRuleData({
						date: data.match(/date: (.+)/)?.[1] || new Date().toISOString().split('T')[0].replace(/-/g, '/'),
						domains: cleanDomainsList.length > 0 ? cleanDomainsList : FALLBACK_DOMAINS
					});
				} catch (e) {
					console.error('Error parsing Domains rule:', e);
				}
			})
			.catch(error => {
				console.error('Error fetching Domains rule (using fallback):', error);
			});
	}, []);
	
	const tabs = [
		{
			id: 'kql',
			name: 'Microsoft Defender',
			icon: 'logoWindows',
		},
		{
			id: 'splunk',
			name: 'Splunk',
			icon: 'splunk',
		},
		{
			id: 'sigma',
			name: 'Sigma',
			icon: 'sigma',
		},
	];
	
	const onSelectedTabChanged = (id) => {
		console.log('Tab changed to:', id);
		setSelectedTabId(id);
	};
	
	const renderTabs = () => {
		return tabs.map((tab, index) => (
			<EuiTab
				key={index}
				onClick={() => onSelectedTabChanged(tab.id)}
				isSelected={tab.id === selectedTabId}
				prepend={
					tab.id === 'splunk' ? (
						<img 
							alt="Splunk Logo" 
							src="/images/splunk_logo.png" 
							style={{ 
								width: '50px', 
								height: '50px', 
								display: 'inline-block', 
								verticalAlign: 'middle',
								objectFit: 'contain'
							}} 
						/>
					) : tab.id === 'sigma' ? (
						<img
							alt="Sigma Logo"
							src="/images/sigma_logo.png"
							style={{ 
								width: '20px', 
								height: '20px', 
								display: 'inline-block', 
								verticalAlign: 'middle',
								objectFit: 'contain'
							}}
						/>
					) : (
						<EuiIcon type={tab.icon} />
					)
				}
			>
				{tab.name}
			</EuiTab>
		));
	};

	const onAccordionToggle = (isOpen) => {
		console.log('Accordion toggle state:', isOpen);
		setIsAccordionOpen(isOpen);
	};
	
	// Debugging output
	console.log('Current selectedTabId:', selectedTabId);
	console.log('isAccordionOpen:', isAccordionOpen);
	
	return (
		<div className="contents-wrapper">
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
			
			<div className="accordion-container" data-accordion-open={isAccordionOpen ? "true" : "false"}>
				<EuiAccordion
					id="siemDetections"
					buttonContent={
						<EuiTitle size="m">
							<h4>
								<EuiIcon type="visLine" color="success" size="l" style={{ marginRight: '8px' }} />
								SIEM Detections <EuiBadge color="accent">NEW</EuiBadge>
								{/* Hidden debug info - will only show in dev tools */}
								<span style={{ display: 'none' }} data-debug={debugInfo} data-accordion-state={isAccordionOpen ? 'open' : 'closed'} data-selected-tab={selectedTabId}></span>
							</h4>
						</EuiTitle>
					}
					paddingSize="l"
					initialIsOpen={true}
					onToggle={onAccordionToggle}
					className="siemDetectionsAccordion"
					style={{ display: 'block', width: '100%' }}
				>
					<div style={{ minHeight: '200px', width: '100%' }}>
						<EuiPanel paddingSize="l" hasShadow style={{ width: '100%' }}>
							<EuiText>
								<p>
									LOLRMM provides detection capabilities for various SIEM platforms to help you identify unauthorized RMM tools in your environment.
									Select your preferred platform below:
								</p>
							</EuiText>
							
							<EuiSpacer size="m" />
							<EuiTabs>{renderTabs()}</EuiTabs>
							<EuiSpacer size="m" />
							
							{selectedTabId === 'kql' ? (
								<div data-test-id="kql-content" style={{ width: '100%' }}>
									<EuiText>
										<h5>Detecting Unauthorized RMM Domains in Microsoft Defender for Endpoint</h5>
										<p>
											LOLRMM provides a comprehensive list of known RMM domains that you can use to detect unauthorized RMM tools in your environment. 
											The domains list is available via API in <EuiLink href="/api/rmm_domains.csv">CSV format</EuiLink>.
											Below is a sample KQL query for Microsoft Defender for Endpoint:
										</p>
									</EuiText>
									<EuiSpacer size="s" />
									<EuiCodeBlock language="kql" fontSize="s" paddingSize="m" isCopyable>
{`// Detecting Unauthorized RMM Instances in Your MDE Environment

let ApprovedRMM = dynamic("YOUR_APPROVED_RMM_DOMAINS"); // E.g. "teamviewer.com" - Replace with your approved RMM domains
let RMMList = externaldata(URI: string, RMMTool: string)
    [h'https://raw.githubusercontent.com/magicsword-io/LOLRMM/main/website/public/api/rmm_domains.csv'];
let RMMUrl = RMMList | project URI;

DeviceNetworkEvents
| where TimeGenerated > ago(1h)
| where ActionType == @"ConnectionSuccess"
| where RemoteUrl has_any(RMMUrl)
| where not (RemoteUrl has_any(ApprovedRMM))
| summarize arg_max(TimeGenerated, *) by DeviceId`}
									</EuiCodeBlock>
									<EuiSpacer size="s" />
									<EuiText size="s">
										<p>
											Replace <code>YOUR_APPROVED_RMM_DOMAINS</code> with your organization's approved RMM domains to exclude them from the detection.
										</p>
									</EuiText>
								</div>
							) : selectedTabId === 'splunk' ? (
								<div data-test-id="splunk-content" style={{ width: '100%' }}>
									<EuiText>
										<h5>Detecting Unauthorized RMM Tools in Splunk</h5>
										<p>
											This Splunk query uses the Network Traffic datamodel to detect usage of remote access software in your environment.
											It is based on Splunk's <EuiLink href="https://research.splunk.com/network/885ea672-07ee-475a-879e-60d28aa5dd42/" target="_blank">
												Detect Remote Access Software Usage Traffic
											</EuiLink> detection.
										</p>
									</EuiText>
									<EuiSpacer size="s" />
									<EuiCodeBlock language="spl" fontSize="s" paddingSize="m" isCopyable>
{`| tstats \`security_content_summariesonly\` count min(_time) as firstTime max(_time) as lastTime values(All_Traffic.dest_port) as dest_port latest(user) as user from datamodel=Network_Traffic by All_Traffic.src All_Traffic.dest, All_Traffic.app 
| \`drop_dm_object_name("All_Traffic")\` 
| \`security_content_ctime(firstTime)\` 
| \`security_content_ctime(lastTime)\` 
| lookup remote_access_software remote_appid AS app OUTPUT isutility, description as signature, comment_reference as desc, category 
| search isutility = True 
| \`remote_access_software_usage_exceptions\` 
| \`detect_remote_access_software_usage_traffic_filter\``}
									</EuiCodeBlock>
									<EuiSpacer size="s" />
									<EuiText size="s">
										<p>
											This query requires Splunk Enterprise Security and the proper Network Traffic datamodel setup. You may need to customize the lookup tables for your environment.
										</p>
										<p>
											<EuiButtonEmpty 
												href="https://research.splunk.com/network/885ea672-07ee-475a-879e-60d28aa5dd42/" 
												target="_blank"
												iconType="logoSplunk"
												size="s">
												View full detection details on Splunk Research
											</EuiButtonEmpty>
										</p>
									</EuiText>
								</div>
							) : (
								<div data-test-id="sigma-content" style={{ width: '100%' }}>
									<EuiText>
										<h5>Detecting RMM Tools with Sigma Rules</h5>
										<p>
											LOLRMM provides Sigma rules for detecting Remote Monitoring and Management (RMM) tools in your environment.
											These rules can be converted to your specific SIEM platform using the <EuiLink href="https://github.com/SigmaHQ/sigma" target="_blank">Sigma converter</EuiLink>.
											Below is a sample Sigma rule for detecting RMM executables:
										</p>
									</EuiText>
									<EuiSpacer size="s" />
									<EuiCodeBlock language="yaml" fontSize="s" paddingSize="m" isCopyable>
{`title: Generic RMM Tool Detection
id: ba1e3a37-6751-48e8-9f7a-73d9062f137c
status: experimental
description: Detects processes associated with common Remote Monitoring and Management (RMM) tools that could be used for lateral movement
references:
    - https://github.com/magicsword-io/LOLRMM
author: LOLRMM Project
date: ${sigmaRuleData?.date || 'N/A'}
modified: ${sigmaRuleData?.date || 'N/A'}
tags:
    - attack.lateral_movement
    - attack.t1219
logsource:
    category: process_creation
    product: windows
detection:
    selection:
        Image|endswith:
            - '\\\\anydesk.exe'
            - '\\\\teamviewer.exe'
            - '\\\\splashtop.exe'
            - '\\\\screenconnect.exe'
            - '\\\\logmein.exe'
            - '\\\\connectwise.exe'
            - '\\\\atera.exe'
            - '\\\\supremo.exe'
            - '\\\\bomgar.exe'
            - '\\\\dwservice.exe'
            - '\\\\rustdesk.exe'
            - '\\\\ultraviewer.exe'
            # Plus many more RMM executables
    condition: selection
falsepositives:
    - Legitimate usage of remote management tools
level: medium`}
									</EuiCodeBlock>
									<EuiSpacer size="s" />
									<EuiText size="s">
										<p>
											We also provide a DNS-based detection rule for all RMM domains to identify network communication with RMM services:
										</p>
									</EuiText>
									<EuiSpacer size="s" />
									<EuiCodeBlock language="yaml" fontSize="s" paddingSize="m" isCopyable>
{`title: DNS Queries to Known RMM Domains
id: 9fa68c28-79b2-4ab5-af95-0c7b2f706c63
status: experimental
description: Detects DNS queries to known Remote Monitoring and Management (RMM) tool domains that could indicate unauthorized remote access
references:
    - https://github.com/magicsword-io/LOLRMM
author: LOLRMM Project
date: ${domainsRuleData?.date || 'N/A'}
modified: ${domainsRuleData?.date || 'N/A'}
tags:
    - attack.command_and_control
    - attack.t1219
logsource:
    category: dns
    product: any
detection:
    selection:
        query|contains:
            - '.anydesk.com'
            - '.teamviewer.com'
            - '.splashtop.com'
            - '.connectwise.com'
            - '.bomgar.com'
            - '.logmein.com'
            - '.supremo.com'
            # Plus many more RMM domains
    condition: selection
falsepositives:
    - Legitimate usage of remote management tools
level: medium`}
									</EuiCodeBlock>
									<EuiSpacer size="s" />
									<EuiText size="s">
										<p>
											<EuiButtonEmpty 
												href="https://github.com/magicsword-io/lolrmm/tree/main/detections/sigma" 
												target="_blank"
												iconType="logoGithub"
												size="s">
												View all Sigma rules on GitHub
											</EuiButtonEmpty>
										</p>
									</EuiText>
								</div>
							)}
						</EuiPanel>
					</div>
				</EuiAccordion>
			</div>
			
			<EuiSpacer size="xxl" />

			<EuiTitle size="m">
				<h4>RMM Tools {rmmCount !== null && <EuiBadge color="default">Total: {rmmCount}</EuiBadge>}</h4>
			</EuiTitle>

			<EuiSpacer size="xxl" />
			<RMMTable />
		</div>
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
