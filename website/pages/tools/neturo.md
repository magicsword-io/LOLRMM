---
description: "Neturo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Neturo"
displayTitle: "Neturo"
---



# Neturo


### Description

Neturo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `neturo*.exe`
- `ntrntservice.exe`
- `neturo.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `neturo.uplus.co.kr`


### Detections
- Detects potential network activity of Neturo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/neturo_network_sigma.yml)
- Detects potential processes activity of Neturo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/neturo_processes_sigma.yml)

### References
- [Obscure, located an older copy here: http://www.iconpos.com/pos/home/iconpos/bbs.php?id=file&q=view&uid=2](Obscure, located an older copy here: http://www.iconpos.com/pos/home/iconpos/bbs.php?id=file&q=view&uid=2)


