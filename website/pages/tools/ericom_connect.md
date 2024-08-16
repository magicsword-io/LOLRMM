---
description: "Ericom Connect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Ericom Connect"
displayTitle: "Ericom Connect"
---



# Ericom Connect


### Description

Ericom Connect is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `EricomConnectRemoteHost*.exe`
- `ericomconnnectconfigurationtool.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `ericom.com`


### Detections
- Detects potential network activity of Ericom Connect RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ericom_connect_network_sigma.yml)
- Detects potential processes activity of Ericom Connect RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ericom_connect_processes_sigma.yml)

### References
- [https://www.ericom.com/connect-accessnow/](https://www.ericom.com/connect-accessnow/)


