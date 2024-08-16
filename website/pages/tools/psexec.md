---
description: "PSEXEC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "PSEXEC"
displayTitle: "PSEXEC"
---



# PSEXEC


### Description

PSEXEC is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `psexec.exe`
- `psexecsvc.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`


### Detections
- Detects potential network activity of PSEXEC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/psexec_network_sigma.yml)
- Detects potential processes activity of PSEXEC RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/psexec_processes_sigma.yml)

### References
- [https://learn.microsoft.com/en-us/sysinternals/downloads/psexec](https://learn.microsoft.com/en-us/sysinternals/downloads/psexec)


