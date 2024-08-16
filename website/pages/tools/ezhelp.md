---
description: "ezHelp is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "ezHelp"
displayTitle: "ezHelp"
---



# ezHelp


### Description

ezHelp is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `ezhelpclientmanager.exe`
- `ezHelpManager.exe`
- `ezhelpclient.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `*.ezhelp.co.kr`
    - `ezhelp.co.kr`


### Detections
- Detects potential network activity of ezHelp RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ezhelp_network_sigma.yml)
- Detects potential processes activity of ezHelp RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/ezhelp_processes_sigma.yml)

### References
- [https://www.exhelp.co.kr](https://www.exhelp.co.kr)


