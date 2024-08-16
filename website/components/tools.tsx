import {
  EuiBadge,
  type EuiBasicTableColumn,
  EuiButtonIcon,
  EuiFlexGroup,
  EuiFlexItem,
  EuiInMemoryTable,
  EuiLoadingSpinner,
  EuiNotificationBadge,
  EuiSearchBar,
  type EuiSearchBarOnChangeArgs,
  type EuiSearchBarProps,
  EuiToolTip,
} from "@elastic/eui";

import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";
import axios from "axios";
import React, { useRef } from "react";
import { useEffect, useState } from "react";
const queryClient = new QueryClient();

async function getTools() {
  return await axios.get("/api/tools.json").then((res) => res.data);
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
  Verification: string;
  SupportedOS: string[];
  Capabilities: string[];
  Vulnerabilities: string[];
  InstallationPaths: string[];
};
type RMM = {
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
  const ref = useRef<EuiInMemoryTable<RMM>>();

  const { isLoading, error, data } = useQuery<RMM[]>({
    queryKey: ["lolrmms"],
    queryFn: getTools,
  });

  if (isLoading) {
    return <EuiLoadingSpinner />;
  }
  if (error) {
    return <div>Error: {error.message}</div>;
  }

  const columns: EuiBasicTableColumn<RMM>[] = [
    {
      field: "Name",
      name: "Name",
      sortable: true,
      width: "auto",
      render: (value: string) => {
        return <a href={`/rmm/${value}`}>{value}</a>;
      },
    },
    // { // TODO: Where is the data ?
    // 	field: "Category",
    // 	name: "Category",
    // 	sortable: false,
    // 	textOnly: true,
    // 	width: "auto",
    // },
    {
      field: "Description",
      name: "Description",
      sortable: false,
      textOnly: true,
      width: "auto",
    },
    {
      field: "Author",
      name: "Author",
      sortable: true,
      textOnly: true,
      width: "auto",
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
  };

  return (
    <EuiInMemoryTable<RMM>
      tableCaption="LOLRMM"
      columns={columns}
      items={data ?? []}
      loading={isLoading}
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
