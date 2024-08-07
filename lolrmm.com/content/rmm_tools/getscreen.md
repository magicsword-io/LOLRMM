+++
description = "GetScreen is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title = "GetScreen"
weight = 10
displayTitle = "GetScreen"
+++


{{< block "grid-1" >}}
{{< column "mt-2 pt-1">}}

# GetScreen


### Description

GetScreen is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `GetScreen.exe`
- `getscreen.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains  **Domains**:
    - `getscreen.me`
    - `GetScreen.me`
    - `*.getscreen.me`


### Detections
- Detects potential network activity of GetScreen RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/getscreen_network_sigma.yml)
- Detects potential processes activity of GetScreen RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/getscreen_processes_sigma.yml)

### References
- [https://docs.getscreen.me/self-hosted/system-requirements/](https://docs.getscreen.me/self-hosted/system-requirements/)



{{< /column >}}
{{< /block >}}
