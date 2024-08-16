---
description: "Quick Assist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Quick Assist"
displayTitle: "Quick Assist"
---



# Quick Assist


### Description

Quick Assist is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.




### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `quickassist.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.support.services.microsoft.com`


### Detections
- Detects potential network activity of Quick Assist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/quick_assist_network_sigma.yml)
- Detects potential processes activity of Quick Assist RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/quick_assist_processes_sigma.yml)



