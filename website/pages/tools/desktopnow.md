---
description: "DesktopNow is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "DesktopNow"
displayTitle: "DesktopNow"
---



# DesktopNow


### Description

DesktopNow is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `desktopnow.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.nchuser.com`


### Detections
- Detects potential network activity of DesktopNow RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/desktopnow_network_sigma.yml)
- Detects potential processes activity of DesktopNow RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/desktopnow_processes_sigma.yml)

### References
- [https://forums.ivanti.com/s/article/Network-Ports-used-by-Environment-Manager?language=en_US](https://forums.ivanti.com/s/article/Network-Ports-used-by-Environment-Manager?language=en_US)


