---
description: "EMCO Remote Console is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "EMCO Remote Console"
displayTitle: "EMCO Remote Console"
---



# EMCO Remote Console


### Description

EMCO Remote Console is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/7/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `remoteconsole.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `emcosoftware.com`


### Detections
- Detects potential network activity of EMCO Remote Console RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/emco_remote_console_network_sigma.yml)
- Detects potential processes activity of EMCO Remote Console RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/emco_remote_console_processes_sigma.yml)



