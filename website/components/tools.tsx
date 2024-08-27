import {
	type EuiBasicTableColumn,
	EuiButtonIcon,
	EuiDescriptionList,
	EuiFlexGroup,
	EuiFlexItem,
	EuiIcon,
	EuiInMemoryTable,
	EuiLoadingSpinner,
	EuiNotificationBadge,
	EuiScreenReaderOnly,
	type EuiSearchBarProps,
	EuiSpacer,
} from "@elastic/eui";

import {
	QueryClient,
	QueryClientProvider,
	useQuery,
} from "@tanstack/react-query";
import axios from "axios";
import { capitalize, uniq } from "lodash";
import { type ReactNode, useState } from "react";
const queryClient = new QueryClient();

type Platform =
	| "Android"
	| "IOS"
	| "Windows"
	| "Linux"
	| "MacOS"
	| "ChromeOS"
	| "Mac";

const platformUrls: Record<Platform, string> = {
	Windows: "/platforms/windows.svg",
	Linux: "/platforms/linux.svg",
	MacOS: "/platforms/macos.svg",
	IOS: "/platforms/ios.svg",
	Mac: "/platforms/macos.svg",
	Android: "/platforms/android.svg",
	ChromeOS: "/platforms/chromeos.svg",
};

async function getTools() {
	return await axios.get("/api/rmm_tools.json").then((res) => res.data);
}

export function RMMTable() {
	return (
		<QueryClientProvider client={queryClient}>
			<div style={{ backgroundColor: "black" }}>
				<Table />
			</div>
		</QueryClientProvider>
	);
}

type Artifact = {
	Disk: string[];
	Eventlog: string[];
	Registry: string[];
	Network: {
		Description: string;
		Domains: string[];
		Ports: string[] | number[];
	}[];
};

type Detection = {
	Sigma: string;
	Description: string;
};

type Details = {
	Website: string;
	PEMetadata: {
		Filename: string;
		OriginalFileName: string;
		Description: string;
	};
	Privileges: string;
	Free: string;
	Verification: "None" | "";
	SupportedOS: Platform[];
	Capabilities: string[];
	Vulnerabilities: string[];
	InstallationPaths: string[];
};

type Tool = {
	Name: string;
	Description: string;
	Author: string;
	Created: string;
	LastModified: string;
	Details: Details;
	Detections: Detection[];
	Artifacts: Artifact;
	References: string[];
	Acknowledgement: string[];
};

export function Table() {
	const [itemIdToExpandedRowMap, setItemIdToExpandedRowMap] = useState<
		Record<string, ReactNode>
	>({});

	const { isLoading, error, data } = useQuery<Tool[]>({
		queryKey: ["lolrmms"],
		queryFn: getTools,
	});

	const toggleDetails = (tool: Tool) => {
		const itemIdToExpandedRowMapValues = { ...itemIdToExpandedRowMap };

		if (itemIdToExpandedRowMapValues[tool.Name]) {
			delete itemIdToExpandedRowMapValues[tool.Name];
		} else {
			const listItems = [
				{
					title: "Description",
					description: tool.Description,
				},
			];
			itemIdToExpandedRowMapValues[tool.Name] = (
				<>
					<EuiSpacer size="xxl" />
					<EuiDescriptionList listItems={listItems} compressed={true} />
					<EuiSpacer size="xxl" />
				</>
			);
		}
		setItemIdToExpandedRowMap(itemIdToExpandedRowMapValues);
	};

	if (isLoading) {
		return <EuiLoadingSpinner />;
	}
	if (error) {
		return <div>Error: {error.message}</div>;
	}

	const columns: EuiBasicTableColumn<Tool>[] = [
		{
			field: "Name",
			name: "Name",
			sortable: true,
			width: "auto",
			render: (value: string) => {
				return (
					<a
						href={`/tools/${value.replace(/[^a-zA-Z0-9.]/g, "_").toLowerCase()}`}
					>
						{value}
					</a>
				);
			},
		},
		{
			field: "Author",
			name: "Author",
			sortable: true,
			textOnly: true,
			width: "auto",
		},
		{
			field: "Details.SupportedOS",
			name: "Supported OS",
			sortable: false,
			textOnly: true,
			width: "auto",
			render: (value) => {
				return (
					<EuiFlexGroup gutterSize={"s"}>
						{value.sort().map((x) => {
							return (
								<EuiFlexItem grow={false} key={x}>
									<EuiIcon type={platformUrls[x] ?? ""} size="xl" title={x} />
								</EuiFlexItem>
							);
						})}
					</EuiFlexGroup>
				);
			},
		},
		{
			name: "Actions",
			actions: [
				{
					name: "Open",
					description: "Open the tool website",
					type: "icon",
					icon: "link",
					available: (tool: Tool) => tool.Details.Website !== "",
					onClick: (tool: Tool) => window.open(tool.Details.Website, "_blank"),
				},
			],
		},
		{
			align: "right",
			width: "30px",
			isExpander: true,
			name: (
				<EuiScreenReaderOnly>
					<span>Expand row</span>
				</EuiScreenReaderOnly>
			),
			mobileOptions: { header: false },
			render: (tool: Tool) => {
				const itemIdToExpandedRowMapValues = { ...itemIdToExpandedRowMap };
				return (
					<EuiButtonIcon
						onClick={() => toggleDetails(tool)}
						aria-label={
							itemIdToExpandedRowMapValues[tool.Name] ? "Collapse" : "Expand"
						}
						iconType={
							itemIdToExpandedRowMapValues[tool.Name]
								? "arrowDown"
								: "arrowRight"
						}
					/>
				);
			},
		},
	];

	const search: EuiSearchBarProps = {
		toolsLeft: [
			<EuiNotificationBadge key={1}>
				{(data ?? []).length}
			</EuiNotificationBadge>,
		],
		box: {
			incremental: true,
			schema: false,
		},
		filters: [
			{
				type: "is",
				field: "Details.Free",
				name: "Freeware",
				negatedName: "Offline",
			},
			{
				type: "field_value_selection",
				field: "Details.Privileges",
				name: "Privileges",
				multiSelect: "or",
				options: uniq(data.map((x) => x.Details.Privileges.toLowerCase())).map(
					(x) => ({
						value: x,
						name: x === "" ? "None" : capitalize(x),
					}),
				),
			},
			{
				type: "field_value_selection",
				field: "Details.SupportedOS",
				name: "Supported OS",
				multiSelect: "or",
				options: uniq(data.flatMap((x) => x.Details.SupportedOS)).map((x) => ({
					value: x,
					name: x,
					view: (
						<>
							<EuiButtonIcon
								size="m"
								iconType={platformUrls[x] ?? ""}
								aria-label={x}
								color="success"
							/>
							{x}
						</>
					),
				})),
			},
		],
	};

	return (
		<EuiInMemoryTable<Tool>
			tableCaption="LOLRMM"
			columns={columns}
			items={data ?? []}
			loading={isLoading}
			itemId="Name"
			itemIdToExpandedRowMap={itemIdToExpandedRowMap}
			sorting={{
				sort: {
					field: "Name",
					direction: "asc",
				},
			}}
			search={search}
			pagination={{
				pageSizeOptions: [10, 20, 50, 0],
				initialPageSize: 10,
				initialPageIndex: 0,
			}}
		/>
	);
}
