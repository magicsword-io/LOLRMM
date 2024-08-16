---
description: "ShowMyPC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "ShowMyPC"
displayTitle: "ShowMyPC"
---



# ShowMyPC


### Description

ShowMyPC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `SMPCSetup.exe`
- `showmypc*.exe`
- `showmypc.exe`
- `smpcsetup.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.showmypc.com`
    - `showmypc.com`


### Detections
- Detects potential network activity of ShowMyPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/showmypc_network_sigma.yml)
- Detects potential processes activity of ShowMyPC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/showmypc_processes_sigma.yml)

### References
- [https://showmypc.com/service/faq/ShowMyPCSecurityOverview1.pdf](https://showmypc.com/service/faq/ShowMyPCSecurityOverview1.pdf)


