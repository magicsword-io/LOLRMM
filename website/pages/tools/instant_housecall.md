---
description: "Instant Housecall is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Instant Housecall"
displayTitle: "Instant Housecall"
---



# Instant Housecall


### Description

Instant Housecall is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `hsloader.exe`
- `InstantHousecall.exe`
- `ihcserver.exe`
- `instanthousecall.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.instanthousecall.com`
    - `secure.instanthousecall.com`
    - `*.instanthousecall.net`
    - `instanthousecall.com`


### Detections
- Detects potential network activity of Instant Housecall RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/instant_housecall_network_sigma.yml)
- Detects potential processes activity of Instant Housecall RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/instant_housecall_processes_sigma.yml)

### References
- [https://instanthousecall.com/features/](https://instanthousecall.com/features/)


