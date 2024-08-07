+++
description = "Remote Utilities is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "Remote Utilities"
weight = 10
displayTitle = "Remote Utilities"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# Remote Utilities


### Description

Remote Utilities is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rutview.exe`
- `rutserv.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.internetid.ru`


### Detections
- Detects potential network activity of Remote Utilities RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote_utilities_network_sigma.yml)
- Detects potential processes activity of Remote Utilities RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote_utilities_processes_sigma.yml)

### References
- [https://www.remoteutilities.com/download/](https://www.remoteutilities.com/download/)



{{< /column >}}
{{< /block >}}
