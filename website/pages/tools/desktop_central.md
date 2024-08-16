---
description: "Desktop Central is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Desktop Central"
displayTitle: "Desktop Central"
---



# Desktop Central


### Description

Desktop Central is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `dcagentservice.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `desktopcentral.manageengine.com`


### Detections
- Detects potential network activity of Desktop Central RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/desktop_central_network_sigma.yml)
- Detects potential processes activity of Desktop Central RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/desktop_central_processes_sigma.yml)



