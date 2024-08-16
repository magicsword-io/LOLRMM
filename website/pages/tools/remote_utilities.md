---
description: "Remote Utilities is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Remote Utilities"
displayTitle: "Remote Utilities"
---



# Remote Utilities


### Description

Remote Utilities is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `rutview.exe`
- `rutserv.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.internetid.ru`


### Detections
- Detects potential network activity of Remote Utilities RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote_utilities_network_sigma.yml)
- Detects potential processes activity of Remote Utilities RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remote_utilities_processes_sigma.yml)

### References
- [https://www.remoteutilities.com/download/](https://www.remoteutilities.com/download/)


