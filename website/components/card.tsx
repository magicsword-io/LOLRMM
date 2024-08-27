import {
	EuiBadge,
	type EuiBadgeProps,
	EuiButton,
	EuiCard,
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
import { isEmpty } from "lodash";

export function Badges({
	badges,
	color,
}: { badges: string[]; color: EuiBadgeProps["color"] }) {
	return (
		<>
			<EuiSpacer size="m" />
			<EuiFlexGroup gutterSize="s">
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
	return (
		<>
			<EuiSpacer size="m" />
			<EuiFlexGroup>
				<EuiFlexItem>
					<EuiDescriptionList
						compressed={true}
						listItems={[
							{
								title: "Author",
								description: props.author ?? "--",
							},
							{
								title: "Category",
								description: props.category ?? "--",
							},
							{
								title: "Created",
								description: props.created ?? "--",
							},
							{
								title: "Last Modified",
								description: props.lastModified ?? "--",
							},
						]}
					/>
				</EuiFlexItem>
				<EuiFlexItem>
					<EuiDescriptionList
						compressed={true}
						listItems={[
							{
								title: "Website",
								description: (
									<EuiLink href={props.website ?? "#"}>
										{props.website ?? "--"}
									</EuiLink>
								),
							},
							{
								title: "Privileges",
								description: props.privileges ?? "--",
							},
							{
								title: "Pricing",
								description: props.free ? "Free" : "Paid",
							},
							{
								title: "Verification",
								description: (
									<EuiIcon
										type={
											props.verification
												? "checkInCircleFilled"
												: "minusInCircleFilled"
										}
										color={props.verification ? "success" : "danger"}
									/>
								),
							},
						]}
					/>
				</EuiFlexItem>
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
				<EuiBadge
					onClick={(event) => copyToClipboard(event.currentTarget.innerText)}
					onClickAriaLabel="Copy text"
				>
					{data.File}
				</EuiBadge>
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
					<EuiIcon
						size="xl"
						type={`https://lolrmm.vercel.app/platforms/${data.OS.toLowerCase()}.svg`}
					/>
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
				key="loadUsers"
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

export function Card({ code }: { code: string }) {
	return (
		<>
			<EuiSpacer size="l" />
			<EuiCodeBlock paddingSize="m" isCopyable={true} lineNumbers={true}>
				{code}
			</EuiCodeBlock>
		</>
	);
}
