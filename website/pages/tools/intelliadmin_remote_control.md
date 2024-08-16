---
description: "IntelliAdmin Remote Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "IntelliAdmin Remote Control"
displayTitle: "IntelliAdmin Remote Control"
---



# IntelliAdmin Remote Control


### Description

IntelliAdmin Remote Control is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `iadmin.exe`
- `intelliadmin.exe`
- `agent32.exe`
- `agent64.exe`
- `agent_setup_5.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `*.intelliadmin.com`
    - `intelliadmin.com/remote-control`


### Detections
- Detects potential network activity of IntelliAdmin Remote Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/intelliadmin_remote_control_network_sigma.yml)
- Detects potential processes activity of IntelliAdmin Remote Control RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/intelliadmin_remote_control_processes_sigma.yml)

### References
- [intelliadmin.com/remote-control](intelliadmin.com/remote-control)


