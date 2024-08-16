---
description: "ZeroTier is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "ZeroTier"
displayTitle: "ZeroTier"
---



# ZeroTier


### Description

ZeroTier is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `zerotier*.msi`
- `zerotier*.exe`
- `zero-powershell.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `zerotier.com`
    - `*.zerotier.com`


### Detections
- Detects potential network activity of ZeroTier RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/zerotier_network_sigma.yml)
- Detects potential processes activity of ZeroTier RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/zerotier_processes_sigma.yml)

### References
- [https://my.zerotier.com/](https://my.zerotier.com/)


