---
description: "SunLogin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "SunLogin"
displayTitle: "SunLogin"
---



# SunLogin


### Description

SunLogin is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/26/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `OrayRemoteShell.exe`
- `OrayRemoteService.exe`
- `sunlogin*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `sunlogin.oray.com`
    - `client.oray.net`


### Detections
- Detects potential network activity of SunLogin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/sunlogin_network_sigma.yml)
- Detects potential processes activity of SunLogin RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/sunlogin_processes_sigma.yml)

### References
- [https://sunlogin.oray.com/en/embed/software.html](https://sunlogin.oray.com/en/embed/software.html)


