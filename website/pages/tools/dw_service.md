---
description: "DW Service is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "DW Service"
displayTitle: "DW Service"
---



# DW Service


### Description

DW Service is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `dwagsvc.exe`
- `dwagent.exe`
- `dwagsvc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.dwservice.net`


### Detections
- Detects potential network activity of DW Service RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/dw_service_network_sigma.yml)
- Detects potential processes activity of DW Service RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/dw_service_processes_sigma.yml)

### References
- [https://news.dwservice.net/dwservice-security-infrastructure/](https://news.dwservice.net/dwservice-security-infrastructure/)


