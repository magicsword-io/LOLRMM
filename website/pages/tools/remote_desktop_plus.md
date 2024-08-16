---
description: "Remote Desktop Plus is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Remote Desktop Plus"
displayTitle: "Remote Desktop Plus"
---



# Remote Desktop Plus


### Description

Remote Desktop Plus is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rdp.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `donkz.nl`


### Detections
- Detects potential network activity of Remote Desktop Plus RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote_desktop_plus_network_sigma.yml)
- Detects potential processes activity of Remote Desktop Plus RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote_desktop_plus_processes_sigma.yml)

### References
- [https://www.donkz.nl/](https://www.donkz.nl/)


