---
description: "Sophos-Remote Management System is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Sophos-Remote Management System"
displayTitle: "Sophos-Remote Management System"
---



# Sophos-Remote Management System


### Description

Sophos-Remote Management System is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `clientmrinit.exe`
- `mgntsvc.exe`
- `routernt.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.sophos.com`
    - `*.sophosupd.com`
    - `*.sophosupd.net`
    - `community.sophos.com/on-premise-endpoint/f/sophos-endpoint-software/5725/sophos-remote-management-system`


### Detections
- Detects potential network activity of Sophos-Remote Management System RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/sophos-remote_management_system_network_sigma.yml)
- Detects potential processes activity of Sophos-Remote Management System RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/sophos-remote_management_system_processes_sigma.yml)

### References
- [community.sophos.com/on-premise-endpoint/f/sophos-endpoint-software/5725/sophos-remote-management-system](community.sophos.com/on-premise-endpoint/f/sophos-endpoint-software/5725/sophos-remote-management-system)


