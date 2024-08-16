---
description: "Goverlan is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Goverlan"
displayTitle: "Goverlan"
---



# Goverlan


### Description

Goverlan is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `goverrmc.exe`
- `govsrv*.exe`
- `GovAgentInstallHelper.exe`
- `GovAgentx64.exe`
- `GovReachClient.exe`
- `C:\Program Files (x86)\PJ Technologies\GOVsrv\*`
- `*\PJ Technologies\GOVsrv\*`
- `*\GovSrv.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `goverlan.com`


### Detections
- Detects potential network activity of Goverlan RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/goverlan_network_sigma.yml)
- Detects potential processes activity of Goverlan RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/goverlan_processes_sigma.yml)

### References
- [https://www.goverlan.com/pdf/Goverlan-Remote-Control-Software.pdf](https://www.goverlan.com/pdf/Goverlan-Remote-Control-Software.pdf)


