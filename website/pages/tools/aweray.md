---
description: "AweRay is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "AweRay"
displayTitle: "AweRay"
---



# AweRay


### Description

AweRay is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `aweray_remote*.exe`
- `AweSun.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `asapi*.aweray.net`
    - `client-api.aweray.com`


### Detections
- Detects potential network activity of AweRay RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/aweray_network_sigma.yml)
- Detects potential processes activity of AweRay RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/aweray_processes_sigma.yml)

### References
- [https://sun.aweray.com/help](https://sun.aweray.com/help)


