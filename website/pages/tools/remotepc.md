---
description: "RemotePC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "RemotePC"
displayTitle: "RemotePC"
---



# RemotePC


### Description

RemotePC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `C:\Program Files (x86)\RemotePC\*`
- `Idrive.File-Transfer`
- `*\RemotePC\*`
- `remotepcservice.exe`
- `RemotePC.exe`
- `remotepchost.exe`
- `idrive.RemotePCAgent`
- `rpcsuite.exe`
- `*\RemotePCService.exe`
- `RemotePCService.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.remotedesktop.com`
    - `*.remotepc.com`
    - `www.remotepc.com`
    - `remotepc.com`


### Detections
- Detects potential network activity of RemotePC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remotepc_network_sigma.yml)
- Detects potential processes activity of RemotePC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remotepc_processes_sigma.yml)

### References
- [https://www.remotedesktop.com/helpdesk/faq-firewall](https://www.remotedesktop.com/helpdesk/faq-firewall)


