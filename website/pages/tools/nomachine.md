---
description: "NoMachine is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "NoMachine"
displayTitle: "NoMachine"
---



# NoMachine


### Description

NoMachine is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `nomachine*.exe`
- `nxservice*.ese`
- `nxd.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `nomachine.com`


### Detections
- Detects potential network activity of NoMachine RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/nomachine_network_sigma.yml)
- Detects potential processes activity of NoMachine RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/nomachine_processes_sigma.yml)

### References
- [https://kb.nomachine.com/AR04S01122](https://kb.nomachine.com/AR04S01122)


