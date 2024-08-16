---
description: "HelpU is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "HelpU"
displayTitle: "HelpU"
---



# HelpU


### Description

HelpU is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/8/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `helpu_install.exe`
- `HelpuUpdater.exe`
- `HelpuManager.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `helpu.co.kr`
    - `*.helpu.co.kr`


### Detections
- Detects potential network activity of HelpU RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/helpu_network_sigma.yml)
- Detects potential processes activity of HelpU RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/helpu_processes_sigma.yml)

### References
- [https://helpu.co.kr/](https://helpu.co.kr/)


