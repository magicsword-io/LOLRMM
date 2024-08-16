---
description: "SkyFex is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "SkyFex"
displayTitle: "SkyFex"
---



# SkyFex


### Description

SkyFex is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `Deskroll.exe`
- `DeskRollUA.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `skyfex.com`
    - `deskroll.com`
    - `*.deskroll.com`


### Detections
- Detects potential network activity of SkyFex RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/skyfex_network_sigma.yml)
- Detects potential processes activity of SkyFex RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/skyfex_processes_sigma.yml)

### References
- [https://skyfex.com/](https://skyfex.com/)


