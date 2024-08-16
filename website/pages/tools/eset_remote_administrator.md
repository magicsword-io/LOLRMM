---
description: "ESET Remote Administrator is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "ESET Remote Administrator"
displayTitle: "ESET Remote Administrator"
---



# ESET Remote Administrator


### Description

ESET Remote Administrator is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `einstaller.exe`
- `era.exe`
- `ERAAgent.exe`
- `ezhelp*.exe`
- `eratool.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `eset.com/me/business/remote-management/remote-administrator/`


### Detections
- Detects potential network activity of ESET Remote Administrator RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/eset_remote_administrator_network_sigma.yml)
- Detects potential processes activity of ESET Remote Administrator RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/eset_remote_administrator_processes_sigma.yml)

### References
- [eset.com/me/business/remote-management/remote-administrator/](eset.com/me/business/remote-management/remote-administrator/)


