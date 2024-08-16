---
description: "RuDesktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "RuDesktop"
displayTitle: "RuDesktop"
---



# RuDesktop


### Description

RuDesktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rd.exe`
- `rudesktop*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.rudesktop.ru`
    - `rudesktop.ru`


### Detections
- Detects potential network activity of RuDesktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rudesktop_network_sigma.yml)
- Detects potential processes activity of RuDesktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rudesktop_processes_sigma.yml)

### References
- [https://rudesktop.ru](https://rudesktop.ru)


