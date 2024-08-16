---
description: "Pulseway is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Pulseway"
displayTitle: "Pulseway"
---



# Pulseway


### Description

Pulseway is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `PCMonitorManager.exe`
- `pcmonitorsrv.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `pulseway.com`


### Detections
- Detects potential network activity of Pulseway RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pulseway_network_sigma.yml)
- Detects potential processes activity of Pulseway RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pulseway_processes_sigma.yml)

### References
- [https://intercom.help/pulseway/en/](https://intercom.help/pulseway/en/)


