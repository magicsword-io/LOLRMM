+++
description = "KHelpDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "KHelpDesk"
weight = 10
displayTitle = "KHelpDesk"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# KHelpDesk


### Description

KHelpDesk is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `KHelpDesk.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.khelpdesk.com.br`


### Detections
- Detects potential network activity of KHelpDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/khelpdesk_network_sigma.yml)
- Detects potential processes activity of KHelpDesk RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/khelpdesk_processes_sigma.yml)

### References
- [https://www.khelpdesk.com.br/en-us](https://www.khelpdesk.com.br/en-us)



{{< /column >}}
{{< /block >}}
