import { EuiCard, type EuiCardProps, EuiFlexItem } from "@elastic/eui";
import React from "react";

export function Card(
	props: Pick<EuiCardProps, "icon" | "title" | "description">,
) {
	return (
		<EuiFlexItem>
			<EuiCard hasBorder {...props} />
		</EuiFlexItem>
	);
}
