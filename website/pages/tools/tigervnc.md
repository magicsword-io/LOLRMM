---
description: "TigerVNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "TigerVNC"
displayTitle: "TigerVNC"
---



# TigerVNC


### Description

TigerVNC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `tigervnc*.exe`
- `winvnc4.exe`
- `C:\Program Files\TightVNC\*`
- `*\TightVNC\*`
- `*\tvnserver.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of TigerVNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tigervnc_network_sigma.yml)
- Detects potential processes activity of TigerVNC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/tigervnc_processes_sigma.yml)

### References
- [https://github.com/TigerVNC/tigervnc/releases](https://github.com/TigerVNC/tigervnc/releases)


