import {
	EuiBadge,
	type EuiBadgeProps,
	EuiButton,
	EuiCard,
	EuiCode,
	EuiCodeBlock,
	EuiDescriptionList,
	EuiFlexGrid,
	EuiFlexGroup,
	EuiFlexItem,
	EuiIcon,
	EuiInMemoryTable,
	EuiLink,
	EuiSpacer,
	copyToClipboard,
} from "@elastic/eui";
import { isArray, isBoolean, isEmpty } from "lodash";
import type { ReactNode } from "react";

export function Badges({
	badges,
	color,
}: { badges: string[]; color: EuiBadgeProps["color"] }) {
	return (
		<>
			<EuiSpacer size="m" />
			<EuiFlexGroup wrap={true} responsive={false} gutterSize="s">
				{badges.map((badge) => (
					<EuiFlexItem grow={false} key={badge}>
						<EuiBadge color={color}>{badge}</EuiBadge>
					</EuiFlexItem>
				))}
			</EuiFlexGroup>
		</>
	);
}

type DetailProps = {
	author: string;
	category: string;
	created: string;
	lastModified: string;
	website: string;
	privileges: string;
	free: boolean;
	verification: boolean;
};

export function Details(props: DetailProps) {
	const leftItems = [
		!isEmpty(props.author) && { title: "Author", description: props.author },
		!isEmpty(props.category) && { title: "Category", description: props.category },
		!isEmpty(props.created) && { title: "Created", description: props.created },
		!isEmpty(props.lastModified) && { title: "Last Modified", description: props.lastModified },
	].filter(Boolean);

	const rightItems = [
		!isEmpty(props.website) && {
			title: "Website",
			description: <EuiLink href={props.website}>{props.website}</EuiLink>,
		},
		!isEmpty(props.privileges) && { title: "Privileges", description: props.privileges },
		{
			title: "Pricing",
			description: isBoolean(props.free) ? (props.free ? "Free" : "Paid") : "Unknown",
		},
		{
			title: "Verification",
			description: (
				<EuiIcon
					type={props.verification ? "checkInCircleFilled" : "minusInCircleFilled"}
					color={props.verification ? "success" : "danger"}
				/>
			),
		},
	].filter(Boolean);

	return (
		<>
			<EuiSpacer size="m" />
			<EuiFlexGroup>
				{leftItems.length > 0 && (
					<EuiFlexItem>
						<EuiDescriptionList compressed={true} listItems={leftItems} />
					</EuiFlexItem>
				)}
				{rightItems.length > 0 && (
					<EuiFlexItem>
						<EuiDescriptionList compressed={true} listItems={rightItems} />
					</EuiFlexItem>
				)}
			</EuiFlexGroup>
		</>
	);
}

type DiskArtifact = {
	File: string;
	Description: string;
	OS: string;
	Example?: string[];
};

function DiskArtifactItem({ data }: { data: DiskArtifact }) {
	const listItems = [
		{
			title: "File Name",
			description: (
				<EuiCode onClick={() => copyToClipboard(data.File)}>
					{data.File}
				</EuiCode>
			),
		},
		{
			title: "Description",
			description: data.Description,
		},
	];

	if (!isEmpty(data.Example)) {
		listItems.push({
			title: "Example",
			description: (
				<EuiCodeBlock paddingSize="m" isCopyable={true} lineNumbers={true}>
					{data.Example.join("\n")}
				</EuiCodeBlock>
			),
		});
	}

	return (
		<EuiCard
			layout="horizontal"
			betaBadgeProps={{
				label: (
					<EuiIcon size="xl" type={`/platforms/${data.OS.toLowerCase()}.svg`} />
				),
				tooltipContent:
					"This module is not GA. Please help us by reporting any bugs.",
			}}
			title={""}
			description=""
		>
			<EuiDescriptionList compressed={true} listItems={listItems} />
		</EuiCard>
	);
}

export function DiskArtifacts({ data }: { data: DiskArtifact[] }) {
	return (
		<>
			<EuiSpacer size="xxl" />
			<EuiFlexGrid columns={1} gutterSize="xl">
				{data.map((artifact) => (
					<EuiFlexItem key={artifact.File}>
						<DiskArtifactItem data={artifact} />
					</EuiFlexItem>
				))}
			</EuiFlexGrid>
		</>
	);
}

function checkEmptyOrDefaultValue(value: string, replaceWith = "--") {
	if (isEmpty(value)) {
		return replaceWith;
	}
	return value;
}

export function PEMetadata() {
	return (
		<>
			<EuiSpacer size="m" />
			<EuiFlexGroup>
				<EuiFlexItem grow={false}>
					<EuiCard textAlign="left" title="" description="">
						<EuiDescriptionList
							type="column"
							compressed={true}
							listItems={[
								{
									title: "File Name",
									description: "AnyDesk.exe",
								},
								{
									title: "Original File Name",
									description: "AnyDesk.exe",
								},
								{
									title: "Description",
									description: "AnyDesk",
								},
								{
									title: "Product",
									description: "AnyDesk",
								},
								{
									title: "Internal Name",
									description: "AnyDesk",
								},
							]}
						/>
					</EuiCard>
				</EuiFlexItem>
			</EuiFlexGroup>
		</>
	);
}

type EventLog = {
	EventID: number;
	ProviderName: string;
	LogFile: string;
	ServiceName: string;
	ImagePath: string;
	Description: string;
};

export function EventLogTable({ data }: { data: EventLog[] }) {
	const columns = [
		{
			field: "EventID",
			name: "Event ID",
		},
		{
			field: "ProviderName",
			name: "Provider Name",
		},
		{
			field: "LogFile",
			name: "Log File",
		},
		{
			field: "ServiceName",
			name: "Service Name",
		},
		{
			field: "Image Path",
			name: "Image Path",
		},
		{
			field: "Description",
			name: "Description",
		},
	];

	return (
		<EuiInMemoryTable
			tableCaption="EventLog Table"
			items={data}
			columns={columns}
			pagination={{
				pageSizeOptions: [10, 20, 50, 0],
				initialPageSize: 10,
				initialPageIndex: 0,
			}}
			sorting={{
				sort: {
					field: "EventID",
					direction: "asc",
				},
			}}
		/>
	);
}

type NetworkArtifact = {
	Description: string;
	Domains: string[];
	Ports: string[];
};
export function NetworkArtifactsTable({ data }: { data: NetworkArtifact[] }) {
	const columns = [
		{
			field: "Description",
			name: "Description",
		},
		{
			field: "Domains",
			name: "Domains",
			render: (x) => (
				<EuiFlexGroup
					style={{ maxWidth: "300px" }}
					wrap={true}
					responsive={false}
					gutterSize="s"
				>
					{x.map((y) => (
						<EuiCode onClick={() => copyToClipboard(y)} key={y}>
							{y}
						</EuiCode>
					))}
				</EuiFlexGroup>
			),
		},
		{
			field: "Ports",
			name: "Ports",
			innerWidth: "100px",
			render: (x) => (
				<EuiFlexGroup
					style={{ maxWidth: "100px" }}
					wrap={true}
					responsive={false}
					gutterSize="s"
				>
					{x.map((y) => (
						<EuiCode onClick={() => copyToClipboard(y)} key={y}>
							{y}
						</EuiCode>
					))}
				</EuiFlexGroup>
			),
		},
	];

	return (
		<EuiInMemoryTable<NetworkArtifact>
			tableCaption="EventLog Table"
			items={data}
			columns={columns}
			pagination={{
				pageSizeOptions: [10, 20, 50, 0],
				initialPageSize: 10,
				initialPageIndex: 0,
			}}
			sorting={{
				sort: {
					field: "EventID",
					direction: "asc",
				},
			}}
		/>
	);
}

type OtherArtifact = {
	Type: string;
	Value: string;
};

export function OtherArtifactsTable({ data }: { data: OtherArtifact[] }) {
	const listItems = data.map((x) => {
		return {
			title: `${x.Type}:`,
			description: (
				<EuiCode onClick={() => copyToClipboard(x.Value)}>{x.Value}</EuiCode>
			),
		};
	});

	return (
		<EuiDescriptionList
			type="responsiveColumn"
			listItems={listItems}
			compressed={true}
		/>
	);
}

type Registry = {
	Path: string;
	Description: string;
};

export function RegistryTable({ data }: { data: Registry[] }) {
	const columns = [
		{
			field: "Path",
			name: "Path",
		},
		{
			field: "Description",
			name: "Description",
		},
	];

	return (
		<>
			<EuiButton
				key="copyRegistryPaths"
				onClick={() => {
					copyToClipboard(data.map((x) => x.Path).join("\n"));
				}}
			>
				Copy All Registry Paths
			</EuiButton>
			<EuiSpacer size="m" />
			<EuiInMemoryTable
				tableCaption="Registry Table"
				items={data}
				columns={columns}
				pagination={{
					pageSizeOptions: [10, 20, 50, 0],
					initialPageSize: 10,
					initialPageIndex: 0,
				}}
				sorting={{
					sort: {
						field: "Name",
						direction: "asc",
					},
				}}
			/>
		</>
	);
}

export function Card({ code }: { code: string | string[] }) {
	let codeBlock: string;
	if (isArray(code)) {
		codeBlock = (code as string[]).join("\n");
	} else {
		codeBlock = code as string;
	}

	return (
		<>
			<EuiSpacer size="l" />
			<EuiCodeBlock paddingSize="m" isCopyable={true} lineNumbers={true}>
				{codeBlock}
			</EuiCodeBlock>
		</>
	);
}

export function BlockBanner({ name }: { name: string }) {
	return (
		<div
			style={{
				background: "linear-gradient(135deg, #1a1a2e 0%, #16213e 100%)",
				border: "1px solid #2a2a4a",
				borderLeft: "4px solid #e6c300",
				borderRadius: "12px",
				padding: "24px 28px",
				margin: "24px 0",
				display: "flex",
				flexDirection: "column",
				alignItems: "center",
				gap: "16px",
			}}
		>
			<div
				style={{
					display: "flex",
					alignItems: "flex-start",
					gap: "12px",
					width: "100%",
				}}
			>
				<EuiIcon type="lock" size="l" color="#e6c300" />
				<span
					style={{
						color: "#e0e0e0",
						fontSize: "1.1rem",
						lineHeight: "1.5",
					}}
				>
					Prevent <strong style={{ color: "#fff" }}>{name}</strong> from loading
					on your endpoints natively on Windows using{" "}
					<strong style={{ color: "#fff" }}>WDAC</strong>.
				</span>
			</div>
			<EuiButton
				href="https://www.magicsword.io/plan?utm_source=lolrmm&utm_medium=website&utm_campaign=free_prevention&utm_content=block_banner"
				target="_blank"
				color="warning"
				fill={true}
				iconType="arrowRight"
				iconSide="right"
			>
				Get Started Free with MagicSword
			</EuiButton>
		</div>
	);
}

export function Accordion({
	title,
	children,
}: { title: ReactNode; children: ReactNode }) {
	return (
		<details
			open={true}
			className="last-of-type:mb-0 rounded-lg bg-neutral-50 dark:bg-neutral-800 p-2 mt-4"
		>
			<summary>
				<strong className="text-lg">{title}</strong>
			</summary>
			<div className="nx-p-2">{children}</div>
		</details>
	);
}
