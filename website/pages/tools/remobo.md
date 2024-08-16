---
description: "Remobo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Remobo"
displayTitle: "Remobo"
---



# Remobo


### Description

Remobo is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `remobo.exe`
- `remobo_client.exe`
- `remobo_tracker.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `remobo.en.softonic.com`


### Detections
- Detects potential network activity of Remobo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remobo_network_sigma.yml)
- Detects potential processes activity of Remobo RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/remobo_processes_sigma.yml)

### References
- [https://www.remobo.com - DOA as of 2024](https://www.remobo.com - DOA as of 2024)


