---
description: "GotoHTTP is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "GotoHTTP"
displayTitle: "GotoHTTP"
---



# GotoHTTP


### Description

GotoHTTP is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `GotoHTTP_x64.exe`
- `gotohttp.exe`
- `GotoHTTP*.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.gotohttp.com`
    - `gotohttp.com`


### Detections
- Detects potential network activity of GotoHTTP RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotohttp_network_sigma.yml)
- Detects potential processes activity of GotoHTTP RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/gotohttp_processes_sigma.yml)

### References
- [https://gotohttp.com/goto/help.12x](https://gotohttp.com/goto/help.12x)


