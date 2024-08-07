+++
description = "GatherPlace-desktop sharing is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "GatherPlace-desktop sharing"
weight = 10
displayTitle = "GatherPlace-desktop sharing"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# GatherPlace-desktop sharing


### Description

GatherPlace-desktop sharing is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `gp3.exe`
- `gp4.exe`
- `gp5.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `*.gatherplace.com`
    - `*.gatherplace.net`
    - `gatherplace.com`


### Detections
- Detects potential network activity of GatherPlace-desktop sharing RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gatherplace-desktop_sharing_network_sigma.yml)
- Detects potential processes activity of GatherPlace-desktop sharing RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gatherplace-desktop_sharing_processes_sigma.yml)

### References
- [https://www.gatherplace.com/kb?id=136377](https://www.gatherplace.com/kb?id=136377)



{{< /column >}}
{{< /block >}}
