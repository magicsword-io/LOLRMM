+++
description = "Tanium is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Tanium"
weight = 10
displayTitle = "Tanium"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Tanium


### Description

Tanium is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `TaniumClient.exe`
- `TaniumCX.exe`
- `TaniumExecWrapper.exe`
- `TaniumFileInfo.exe`
- `TPowerShell.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `cloud.tanium.com`
    - `*.cloud.tanium.com`


### Detections
- Detects potential network activity of Tanium RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tanium_network_sigma.yml)
- Detects potential processes activity of Tanium RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tanium_processes_sigma.yml)

### References
- [https://help.tanium.com/bundle/ug_client_cloud/page/client/platform_connections.html](https://help.tanium.com/bundle/ug_client_cloud/page/client/platform_connections.html)



{{< /column >}}
{{< /block >}}
