---
description: "LiteManager is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "LiteManager"
displayTitle: "LiteManager"
---



# LiteManager


### Description

LiteManager is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `lmnoipserver.exe`
- `ROMFUSClient.exe`
- `romfusclient.exe`
- `romviewer.exe`
- `romserver.exe`
- `ROMServer.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.litemanager.ru`
    - `*.litemanager.com`
    - `litemanager.com`


### Detections
- Detects potential network activity of LiteManager RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/litemanager_network_sigma.yml)
- Detects potential processes activity of LiteManager RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/litemanager_processes_sigma.yml)

### References
- [https://www.litemanager.com/articles/LiteManager_remote_access_to_a_desktop_via_the_Internet_or_LAN/](https://www.litemanager.com/articles/LiteManager_remote_access_to_a_desktop_via_the_Internet_or_LAN/)


