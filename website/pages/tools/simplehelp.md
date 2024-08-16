---
description: "SimpleHelp is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "SimpleHelp"
displayTitle: "SimpleHelp"
---



# SimpleHelp


### Description

SimpleHelp is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/9/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `simplehelpcustomer.exe`
- `simpleservice.exe`
- `simplegatewayservice.exe`
- `remote access.exe`
- `windowslauncher.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `simple-help.com`


### Detections
- Detects potential network activity of SimpleHelp RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/simplehelp_network_sigma.yml)
- Detects potential processes activity of SimpleHelp RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/simplehelp_processes_sigma.yml)

### References
- [https://simple-help.com/remote-support](https://simple-help.com/remote-support)


