---
description: "Pcvisit is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "Pcvisit"
displayTitle: "Pcvisit"
---



# Pcvisit


### Description

Pcvisit is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `pcvisit.exe`
- `pcvisit_client.exe`
- `pcvisit-easysupport.exe`
- `pcvisit_service_client.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.pcvisit.de`
    - `pcvisit.de`


### Detections
- Detects potential network activity of Pcvisit RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pcvisit_network_sigma.yml)
- Detects potential processes activity of Pcvisit RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/pcvisit_processes_sigma.yml)

### References
- [https://www.pcvisit.de/](https://www.pcvisit.de/)


