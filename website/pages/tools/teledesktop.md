---
description: "TeleDesktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available."
title: "TeleDesktop"
displayTitle: "TeleDesktop"
---



# TeleDesktop


### Description

TeleDesktop is a remote monitoring and management (RMM) tool. More information will be added as it becomes available.



**Last Modified**: 2/14/2024

### Details


#### PE Metadata
- **Filename**: 
- **OriginalFileName**: 
- **Description**: 


- **Free**: No

- **Verification**: No




#### Installation Paths
- `pstlaunch.exe`
- `ptdskclient.exe`
- `ptdskhost.exe`

### Forensic Artifacts




#### Network Artifacts
- **Description**: Known remote domains
<br/>**Domains**:
    - `user_managed`
    - `tele-desk.com`


### Detections
- Detects potential network activity of TeleDesktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/teledesktop_network_sigma.yml)
- Detects potential processes activity of TeleDesktop RMM tool
  - [Sigma Rule](https://github.com/magicsword-io/LOLRMM/blob/main/detections/sigma/teledesktop_processes_sigma.yml)

### References
- [http://potomacsoft.com/ - DOA as of 2024](http://potomacsoft.com/ - DOA as of 2024)


