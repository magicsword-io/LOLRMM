---
description: "rdp2tcp is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "rdp2tcp"
displayTitle: "rdp2tcp"
---



# rdp2tcp


### Description

rdp2tcp is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `tdp2tcp.exe`
- `rdp2tcp.py`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `github.com/V-E-O/rdp2tcp`


### Detections
- Detects potential network activity of rdp2tcp RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rdp2tcp_network_sigma.yml)
- Detects potential processes activity of rdp2tcp RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/rdp2tcp_processes_sigma.yml)

### References
- [github.com/V-E-O/rdp2tcp](github.com/V-E-O/rdp2tcp)


