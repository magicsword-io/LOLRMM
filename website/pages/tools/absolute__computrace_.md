---
description: "Absolute (Computrace) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Absolute (Computrace)"
displayTitle: "Absolute (Computrace)"
---



# Absolute (Computrace)


### Description

Absolute (Computrace) is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 6/18/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rpcnet.exe`
- `ctes.exe`
- `ctespersitence.exe`
- `cteshostsvc.exe`
- `rpcld.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*search.namequery.com`
    - `*server.absolute.com`


### Detections
- Detects potential network activity of Absolute (Computrace) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/absolute__computrace__network_sigma.yml)
- Detects potential processes activity of Absolute (Computrace) RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/absolute__computrace__processes_sigma.yml)

### References
- [https://community.absolute.com/s/article/Understanding-Absolutes-Endpoint-Agents-Rpcnet-CTES-and-search-namequery-com](https://community.absolute.com/s/article/Understanding-Absolutes-Endpoint-Agents-Rpcnet-CTES-and-search-namequery-com)


